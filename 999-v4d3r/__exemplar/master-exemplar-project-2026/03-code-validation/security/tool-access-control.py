#!/usr/bin/env python3
"""
Tool Access Control Framework for LLM Agent Systems
===================================================

Comprehensive permission system and human-in-the-loop gates for controlling
LLM agent tool execution, preventing excessive agency vulnerabilities.

OWASP LLM Coverage:
- LLM08: Excessive Agency
- LLM02: Insecure Output Handling (tool execution)
- LLM01: Prompt Injection (action validation)

Author: Security Audit Expert Agent
Date: 2026-02-18
Version: 1.0.0
"""

import time
import logging
import json
from typing import Dict, List, Optional, Set, Callable, Any
from dataclasses import dataclass, field, asdict
from enum import Enum
from abc import ABC, abstractmethod
from collections import defaultdict, deque
import threading

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# Section 1: Permission Levels and Access Control
# ============================================================================


class PermissionLevel(Enum):
    """
    Tool permission levels defining risk and required controls.
    """
    # Safe read-only operations
    READ_ONLY = 1

    # Operations requiring validation but generally safe
    RESTRICTED = 2

    # Potentially destructive operations requiring approval
    ELEVATED = 3

    # Critical operations requiring explicit human approval
    ADMIN = 4


class ToolCategory(Enum):
    """Tool categories for permission grouping."""
    INFORMATION_RETRIEVAL = "information_retrieval"
    COMPUTATION = "computation"
    DATA_MODIFICATION = "data_modification"
    EXTERNAL_COMMUNICATION = "external_communication"
    SYSTEM_OPERATION = "system_operation"
    FILE_OPERATION = "file_operation"


@dataclass
class ToolPermission:
    """
    Permission configuration for a tool.
    """
    tool_name: str
    permission_level: PermissionLevel
    category: ToolCategory
    requires_approval: bool = False
    requires_logging: bool = True
    rate_limit: Optional[int] = None  # Max calls per minute
    allowed_agents: Optional[Set[str]] = None  # None = all agents
    forbidden_agents: Set[str] = field(default_factory=set)
    parameter_validators: Dict[str, Callable] = field(default_factory=dict)
    output_validators: List[Callable] = field(default_factory=list)
    description: str = ""


# ============================================================================
# Section 2: Agent Authorization System
# ============================================================================


@dataclass
class AgentCredentials:
    """
    Agent identity and authorization credentials.
    """
    agent_id: str
    agent_type: str  # 'autonomous', 'supervised', 'restricted'
    permission_level: PermissionLevel
    allowed_tools: Set[str]
    forbidden_tools: Set[str] = field(default_factory=set)
    max_tool_calls_per_session: int = 100
    requires_supervision: bool = False
    created_at: float = field(default_factory=time.time)


class AgentRegistry:
    """
    Central registry for agent credentials and permissions.
    """

    def __init__(self):
        self.agents: Dict[str, AgentCredentials] = {}
        self._lock = threading.Lock()

    def register_agent(self, credentials: AgentCredentials) -> bool:
        """
        Register a new agent.

        Args:
            credentials: Agent credentials

        Returns:
            True if registered successfully
        """
        with self._lock:
            if credentials.agent_id in self.agents:
                logger.warning(f"Agent {credentials.agent_id} already registered")
                return False

            self.agents[credentials.agent_id] = credentials
            logger.info(f"Registered agent {credentials.agent_id} with level {credentials.permission_level.name}")
            return True

    def get_agent(self, agent_id: str) -> Optional[AgentCredentials]:
        """Get agent credentials."""
        return self.agents.get(agent_id)

    def revoke_agent(self, agent_id: str) -> bool:
        """Revoke agent access."""
        with self._lock:
            if agent_id in self.agents:
                del self.agents[agent_id]
                logger.warning(f"Revoked agent {agent_id}")
                return True
        return False

    def list_agents(self) -> List[AgentCredentials]:
        """List all registered agents."""
        return list(self.agents.values())


# ============================================================================
# Section 3: Human-in-the-Loop Approval System
# ============================================================================


@dataclass
class ApprovalRequest:
    """
    Request for human approval of tool execution.
    """
    request_id: str
    agent_id: str
    tool_name: str
    parameters: Dict[str, Any]
    reason: str
    risk_assessment: str
    timestamp: float = field(default_factory=time.time)
    timeout: float = 300.0  # 5 minutes default
    status: str = "pending"  # pending, approved, rejected, expired
    approver: Optional[str] = None
    approval_timestamp: Optional[float] = None


class HumanApprovalInterface(ABC):
    """
    Abstract interface for human approval.

    Implementations can use:
    - Web UI
    - CLI prompts
    - Slack/Teams notifications
    - Email requests
    - Webhook callbacks
    """

    @abstractmethod
    def request_approval(self, request: ApprovalRequest) -> bool:
        """
        Request human approval for action.

        Args:
            request: Approval request details

        Returns:
            True if approved, False if rejected
        """
        pass

    @abstractmethod
    def get_approval_status(self, request_id: str) -> str:
        """Get approval status."""
        pass


class CLIApprovalInterface(HumanApprovalInterface):
    """
    Command-line approval interface for testing/development.
    """

    def request_approval(self, request: ApprovalRequest) -> bool:
        """
        Request approval via CLI prompt.
        """
        print("\n" + "=" * 60)
        print("HUMAN APPROVAL REQUIRED")
        print("=" * 60)
        print(f"Request ID: {request.request_id}")
        print(f"Agent: {request.agent_id}")
        print(f"Tool: {request.tool_name}")
        print(f"Parameters: {json.dumps(request.parameters, indent=2)}")
        print(f"Reason: {request.reason}")
        print(f"Risk Assessment: {request.risk_assessment}")
        print("-" * 60)

        response = input("Approve this action? (yes/no): ").strip().lower()

        if response in ['yes', 'y']:
            request.status = "approved"
            request.approver = "cli_user"
            request.approval_timestamp = time.time()
            print("✓ Action APPROVED")
            return True
        else:
            request.status = "rejected"
            request.approver = "cli_user"
            request.approval_timestamp = time.time()
            print("✗ Action REJECTED")
            return False

    def get_approval_status(self, request_id: str) -> str:
        """Get approval status (synchronous for CLI)."""
        return "approved"  # Handled synchronously


class ApprovalQueue:
    """
    Queue for managing approval requests.

    Supports:
    - Async approval workflows
    - Request expiration
    - Approval history
    """

    def __init__(self, approval_interface: HumanApprovalInterface):
        self.interface = approval_interface
        self.pending_requests: Dict[str, ApprovalRequest] = {}
        self.completed_requests: deque = deque(maxlen=1000)  # History
        self._lock = threading.Lock()

    def request_approval(self, request: ApprovalRequest) -> bool:
        """
        Submit approval request and wait for decision.

        Args:
            request: Approval request

        Returns:
            True if approved, False if rejected or timed out
        """
        with self._lock:
            self.pending_requests[request.request_id] = request

        try:
            # Request approval (blocks until decision)
            approved = self.interface.request_approval(request)

            # Move to history
            with self._lock:
                if request.request_id in self.pending_requests:
                    del self.pending_requests[request.request_id]
                self.completed_requests.append(request)

            return approved

        except Exception as e:
            logger.error(f"Approval request failed: {e}")
            request.status = "error"
            return False

    def get_pending_requests(self) -> List[ApprovalRequest]:
        """Get all pending approval requests."""
        return list(self.pending_requests.values())

    def cleanup_expired(self):
        """Remove expired pending requests."""
        current_time = time.time()
        expired = []

        with self._lock:
            for request_id, request in self.pending_requests.items():
                if current_time - request.timestamp > request.timeout:
                    request.status = "expired"
                    expired.append(request_id)
                    self.completed_requests.append(request)

            for request_id in expired:
                del self.pending_requests[request_id]

        if expired:
            logger.warning(f"Expired {len(expired)} approval requests")


# ============================================================================
# Section 4: Audit Logging System
# ============================================================================


@dataclass
class AuditLogEntry:
    """
    Comprehensive audit log entry for tool execution.
    """
    timestamp: float
    agent_id: str
    tool_name: str
    parameters: Dict[str, Any]
    result: Optional[Dict[str, Any]]
    success: bool
    error: Optional[str]
    execution_time: float
    permission_level: str
    approval_required: bool
    approval_granted: bool
    approver: Optional[str]
    security_events: List[str] = field(default_factory=list)


class AuditLogger:
    """
    Comprehensive audit logging for tool execution.

    Features:
    - Structured logging
    - Secure storage
    - Query capabilities
    - Compliance reporting
    """

    def __init__(self, log_file: str = "tool_execution_audit.jsonl"):
        self.log_file = log_file
        self.entries: deque = deque(maxlen=10000)  # In-memory buffer
        self._lock = threading.Lock()

    def log_execution(self, entry: AuditLogEntry):
        """
        Log tool execution.

        Args:
            entry: Audit log entry
        """
        with self._lock:
            # Add to memory buffer
            self.entries.append(entry)

            # Append to file
            try:
                with open(self.log_file, 'a') as f:
                    f.write(json.dumps(asdict(entry)) + '\n')
            except Exception as e:
                logger.error(f"Failed to write audit log: {e}")

        # Log security events
        if entry.security_events:
            logger.warning(
                f"Security events for {entry.tool_name}: {entry.security_events}"
            )

    def query(self, filters: Dict[str, Any], limit: int = 100) -> List[AuditLogEntry]:
        """
        Query audit logs.

        Args:
            filters: Filter criteria (e.g., {'agent_id': 'agent1', 'success': False})
            limit: Maximum results

        Returns:
            List of matching entries
        """
        results = []

        for entry in reversed(self.entries):
            if len(results) >= limit:
                break

            # Check filters
            match = True
            for key, value in filters.items():
                if getattr(entry, key, None) != value:
                    match = False
                    break

            if match:
                results.append(entry)

        return results

    def get_agent_statistics(self, agent_id: str) -> Dict[str, Any]:
        """
        Get execution statistics for an agent.

        Args:
            agent_id: Agent ID

        Returns:
            Statistics dictionary
        """
        agent_entries = [e for e in self.entries if e.agent_id == agent_id]

        if not agent_entries:
            return {'agent_id': agent_id, 'total_executions': 0}

        total = len(agent_entries)
        successful = sum(1 for e in agent_entries if e.success)
        failed = total - successful
        avg_execution_time = sum(e.execution_time for e in agent_entries) / total

        tools_used = defaultdict(int)
        for entry in agent_entries:
            tools_used[entry.tool_name] += 1

        return {
            'agent_id': agent_id,
            'total_executions': total,
            'successful': successful,
            'failed': failed,
            'success_rate': successful / total if total > 0 else 0,
            'avg_execution_time': avg_execution_time,
            'tools_used': dict(tools_used),
            'security_events': sum(len(e.security_events) for e in agent_entries)
        }


# ============================================================================
# Section 5: Rate Limiting
# ============================================================================


class RateLimiter:
    """
    Rate limiter for tool execution.

    Implements token bucket algorithm.
    """

    def __init__(self, max_calls: int, time_window: float = 60.0):
        """
        Initialize rate limiter.

        Args:
            max_calls: Maximum calls allowed
            time_window: Time window in seconds (default 60s = 1 minute)
        """
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls: Dict[str, deque] = defaultdict(lambda: deque())
        self._lock = threading.Lock()

    def check_limit(self, key: str) -> bool:
        """
        Check if call is within rate limit.

        Args:
            key: Rate limit key (e.g., agent_id, tool_name, or combination)

        Returns:
            True if within limit, False if exceeded
        """
        current_time = time.time()
        cutoff_time = current_time - self.time_window

        with self._lock:
            # Remove old calls outside time window
            while self.calls[key] and self.calls[key][0] < cutoff_time:
                self.calls[key].popleft()

            # Check limit
            if len(self.calls[key]) >= self.max_calls:
                logger.warning(
                    f"Rate limit exceeded for {key}: "
                    f"{len(self.calls[key])} calls in {self.time_window}s"
                )
                return False

            # Record this call
            self.calls[key].append(current_time)
            return True

    def get_remaining(self, key: str) -> int:
        """Get remaining calls in current window."""
        current_time = time.time()
        cutoff_time = current_time - self.time_window

        with self._lock:
            # Clean old calls
            while self.calls[key] and self.calls[key][0] < cutoff_time:
                self.calls[key].popleft()

            return self.max_calls - len(self.calls[key])


# ============================================================================
# Section 6: Secure Tool Executor
# ============================================================================


@dataclass
class ToolExecutionResult:
    """Result of tool execution with security metadata."""
    success: bool
    output: Optional[Any]
    error: Optional[str]
    execution_time: float
    security_events: List[str]
    approval_required: bool
    approval_granted: bool
    rate_limited: bool


class SecureToolExecutor:
    """
    Secure tool execution with comprehensive access controls.

    Features:
    - Permission checking
    - Human-in-the-loop approval
    - Rate limiting
    - Audit logging
    - Parameter validation
    - Output validation
    """

    def __init__(self,
                 agent_registry: AgentRegistry,
                 approval_interface: Optional[HumanApprovalInterface] = None,
                 audit_logger: Optional[AuditLogger] = None):
        """
        Initialize secure tool executor.

        Args:
            agent_registry: Agent registry for authorization
            approval_interface: Interface for human approvals
            audit_logger: Audit logger for tool execution
        """
        self.agent_registry = agent_registry
        self.tool_permissions: Dict[str, ToolPermission] = {}
        self.tools: Dict[str, Callable] = {}
        self.rate_limiters: Dict[str, RateLimiter] = {}

        # Initialize approval system
        if approval_interface is None:
            approval_interface = CLIApprovalInterface()
        self.approval_queue = ApprovalQueue(approval_interface)

        # Initialize audit logging
        self.audit_logger = audit_logger or AuditLogger()

    def register_tool(self, tool_name: str, tool_function: Callable,
                      permission: ToolPermission):
        """
        Register a tool with permissions.

        Args:
            tool_name: Tool name
            tool_function: Tool execution function
            permission: Tool permission configuration
        """
        self.tools[tool_name] = tool_function
        self.tool_permissions[tool_name] = permission

        # Create rate limiter if specified
        if permission.rate_limit:
            self.rate_limiters[tool_name] = RateLimiter(
                max_calls=permission.rate_limit,
                time_window=60.0  # Per minute
            )

        logger.info(f"Registered tool {tool_name} with level {permission.permission_level.name}")

    def execute_tool(self, agent_id: str, tool_name: str,
                     parameters: Dict[str, Any]) -> ToolExecutionResult:
        """
        Execute tool with security controls.

        Args:
            agent_id: Agent requesting execution
            tool_name: Tool to execute
            parameters: Tool parameters

        Returns:
            ToolExecutionResult with output and security metadata
        """
        start_time = time.time()
        security_events = []

        # 1. Verify agent exists
        agent = self.agent_registry.get_agent(agent_id)
        if not agent:
            security_events.append("unknown_agent")
            return ToolExecutionResult(
                success=False,
                output=None,
                error=f"Unknown agent: {agent_id}",
                execution_time=0.0,
                security_events=security_events,
                approval_required=False,
                approval_granted=False,
                rate_limited=False
            )

        # 2. Verify tool exists
        if tool_name not in self.tools:
            security_events.append("unknown_tool")
            return ToolExecutionResult(
                success=False,
                output=None,
                error=f"Unknown tool: {tool_name}",
                execution_time=0.0,
                security_events=security_events,
                approval_required=False,
                approval_granted=False,
                rate_limited=False
            )

        tool_permission = self.tool_permissions[tool_name]

        # 3. Check agent authorization
        if tool_name in agent.forbidden_tools:
            security_events.append("forbidden_tool")
            logger.warning(f"Agent {agent_id} attempted to use forbidden tool {tool_name}")
            return ToolExecutionResult(
                success=False,
                output=None,
                error=f"Tool {tool_name} forbidden for agent {agent_id}",
                execution_time=0.0,
                security_events=security_events,
                approval_required=False,
                approval_granted=False,
                rate_limited=False
            )

        if (tool_permission.allowed_agents is not None and
                agent_id not in tool_permission.allowed_agents):
            security_events.append("unauthorized_agent")
            logger.warning(f"Agent {agent_id} not authorized for tool {tool_name}")
            return ToolExecutionResult(
                success=False,
                output=None,
                error=f"Agent {agent_id} not authorized for {tool_name}",
                execution_time=0.0,
                security_events=security_events,
                approval_required=False,
                approval_granted=False,
                rate_limited=False
            )

        # 4. Check permission level
        if tool_permission.permission_level.value > agent.permission_level.value:
            security_events.append("insufficient_permissions")
            logger.warning(
                f"Agent {agent_id} has insufficient permissions for {tool_name}: "
                f"requires {tool_permission.permission_level.name}, "
                f"has {agent.permission_level.name}"
            )
            return ToolExecutionResult(
                success=False,
                output=None,
                error=f"Insufficient permissions for {tool_name}",
                execution_time=0.0,
                security_events=security_events,
                approval_required=False,
                approval_granted=False,
                rate_limited=False
            )

        # 5. Rate limiting
        rate_limited = False
        if tool_name in self.rate_limiters:
            rate_limit_key = f"{agent_id}:{tool_name}"
            if not self.rate_limiters[tool_name].check_limit(rate_limit_key):
                security_events.append("rate_limit_exceeded")
                rate_limited = True
                return ToolExecutionResult(
                    success=False,
                    output=None,
                    error=f"Rate limit exceeded for {tool_name}",
                    execution_time=time.time() - start_time,
                    security_events=security_events,
                    approval_required=False,
                    approval_granted=False,
                    rate_limited=True
                )

        # 6. Parameter validation
        validation_errors = []
        for param_name, validator in tool_permission.parameter_validators.items():
            if param_name in parameters:
                try:
                    if not validator(parameters[param_name]):
                        validation_errors.append(f"Invalid parameter: {param_name}")
                except Exception as e:
                    validation_errors.append(f"Validation error for {param_name}: {e}")

        if validation_errors:
            security_events.append("parameter_validation_failed")
            return ToolExecutionResult(
                success=False,
                output=None,
                error=f"Parameter validation failed: {validation_errors}",
                execution_time=time.time() - start_time,
                security_events=security_events,
                approval_required=False,
                approval_granted=False,
                rate_limited=False
            )

        # 7. Human-in-the-loop approval
        approval_required = tool_permission.requires_approval
        approval_granted = False

        if approval_required:
            # Create approval request
            request = ApprovalRequest(
                request_id=f"{agent_id}_{tool_name}_{int(time.time())}",
                agent_id=agent_id,
                tool_name=tool_name,
                parameters=parameters,
                reason=f"Agent {agent_id} requesting {tool_name}",
                risk_assessment=f"Permission level: {tool_permission.permission_level.name}"
            )

            # Request approval (blocks until decision)
            approval_granted = self.approval_queue.request_approval(request)

            if not approval_granted:
                security_events.append("approval_denied")
                return ToolExecutionResult(
                    success=False,
                    output=None,
                    error="Human approval denied",
                    execution_time=time.time() - start_time,
                    security_events=security_events,
                    approval_required=True,
                    approval_granted=False,
                    rate_limited=False
                )

            security_events.append("approval_granted")

        # 8. Execute tool
        try:
            tool_function = self.tools[tool_name]
            output = tool_function(**parameters)

            # 9. Output validation
            for validator in tool_permission.output_validators:
                try:
                    if not validator(output):
                        security_events.append("output_validation_failed")
                        raise ValueError("Output validation failed")
                except Exception as e:
                    raise ValueError(f"Output validation error: {e}")

            execution_time = time.time() - start_time

            # 10. Audit logging
            audit_entry = AuditLogEntry(
                timestamp=start_time,
                agent_id=agent_id,
                tool_name=tool_name,
                parameters=parameters,
                result={'output': str(output)[:500]},  # Truncate for logging
                success=True,
                error=None,
                execution_time=execution_time,
                permission_level=tool_permission.permission_level.name,
                approval_required=approval_required,
                approval_granted=approval_granted,
                approver=None,  # Could track from approval request
                security_events=security_events
            )
            self.audit_logger.log_execution(audit_entry)

            return ToolExecutionResult(
                success=True,
                output=output,
                error=None,
                execution_time=execution_time,
                security_events=security_events,
                approval_required=approval_required,
                approval_granted=approval_granted,
                rate_limited=False
            )

        except Exception as e:
            execution_time = time.time() - start_time
            security_events.append("execution_error")

            # Audit log error
            audit_entry = AuditLogEntry(
                timestamp=start_time,
                agent_id=agent_id,
                tool_name=tool_name,
                parameters=parameters,
                result=None,
                success=False,
                error=str(e),
                execution_time=execution_time,
                permission_level=tool_permission.permission_level.name,
                approval_required=approval_required,
                approval_granted=approval_granted,
                approver=None,
                security_events=security_events
            )
            self.audit_logger.log_execution(audit_entry)

            return ToolExecutionResult(
                success=False,
                output=None,
                error=str(e),
                execution_time=execution_time,
                security_events=security_events,
                approval_required=approval_required,
                approval_granted=approval_granted,
                rate_limited=False
            )


# ============================================================================
# Section 7: Example Usage & Test Cases
# ============================================================================


def example_tools():
    """Example tool implementations."""

    def search_web(query: str) -> Dict[str, Any]:
        """Safe search tool."""
        return {'results': [{'title': 'Result', 'url': 'https://example.com'}]}

    def read_file(path: str) -> str:
        """Safe file reader (would validate path in production)."""
        return f"Contents of {path}"

    def write_file(path: str, content: str) -> bool:
        """Potentially dangerous file writer."""
        # In production, validate path, check permissions, etc.
        return True

    def delete_file(path: str) -> bool:
        """Dangerous deletion tool."""
        # Requires approval!
        return True

    return {
        'search_web': search_web,
        'read_file': read_file,
        'write_file': write_file,
        'delete_file': delete_file
    }


def run_demo():
    """
    Demonstrate tool access control system.
    """
    print("\n" + "=" * 60)
    print("Tool Access Control System Demo")
    print("=" * 60)

    # 1. Initialize systems
    agent_registry = AgentRegistry()
    audit_logger = AuditLogger("demo_audit.jsonl")
    approval_interface = CLIApprovalInterface()

    executor = SecureToolExecutor(
        agent_registry=agent_registry,
        approval_interface=approval_interface,
        audit_logger=audit_logger
    )

    # 2. Register tools with permissions
    tools = example_tools()

    # Safe search tool
    executor.register_tool(
        'search_web',
        tools['search_web'],
        ToolPermission(
            tool_name='search_web',
            permission_level=PermissionLevel.READ_ONLY,
            category=ToolCategory.INFORMATION_RETRIEVAL,
            requires_approval=False,
            rate_limit=10,  # 10 calls per minute
            description="Web search tool"
        )
    )

    # File read (restricted)
    executor.register_tool(
        'read_file',
        tools['read_file'],
        ToolPermission(
            tool_name='read_file',
            permission_level=PermissionLevel.RESTRICTED,
            category=ToolCategory.FILE_OPERATION,
            requires_approval=False,
            rate_limit=5,
            description="Read file contents"
        )
    )

    # File write (elevated - requires approval)
    executor.register_tool(
        'write_file',
        tools['write_file'],
        ToolPermission(
            tool_name='write_file',
            permission_level=PermissionLevel.ELEVATED,
            category=ToolCategory.FILE_OPERATION,
            requires_approval=True,
            description="Write file contents"
        )
    )

    # File delete (admin - requires approval)
    executor.register_tool(
        'delete_file',
        tools['delete_file'],
        ToolPermission(
            tool_name='delete_file',
            permission_level=PermissionLevel.ADMIN,
            category=ToolCategory.FILE_OPERATION,
            requires_approval=True,
            description="Delete file"
        )
    )

    # 3. Register agents with different permission levels
    # Restricted agent - read-only
    agent_registry.register_agent(
        AgentCredentials(
            agent_id='restricted_agent',
            agent_type='restricted',
            permission_level=PermissionLevel.READ_ONLY,
            allowed_tools={'search_web', 'read_file'},
            requires_supervision=True
        )
    )

    # Standard agent - can write with approval
    agent_registry.register_agent(
        AgentCredentials(
            agent_id='standard_agent',
            agent_type='supervised',
            permission_level=PermissionLevel.ELEVATED,
            allowed_tools={'search_web', 'read_file', 'write_file'},
            requires_supervision=False
        )
    )

    # Admin agent - full access
    agent_registry.register_agent(
        AgentCredentials(
            agent_id='admin_agent',
            agent_type='autonomous',
            permission_level=PermissionLevel.ADMIN,
            allowed_tools={'search_web', 'read_file', 'write_file', 'delete_file'},
            requires_supervision=False
        )
    )

    # 4. Test scenarios
    print("\n--- Test Scenario 1: Safe tool execution ---")
    result = executor.execute_tool(
        agent_id='restricted_agent',
        tool_name='search_web',
        parameters={'query': 'test query'}
    )
    print(f"Result: {result.success}")
    print(f"Security events: {result.security_events}")

    print("\n--- Test Scenario 2: Permission denied ---")
    result = executor.execute_tool(
        agent_id='restricted_agent',
        tool_name='write_file',
        parameters={'path': '/tmp/test', 'content': 'data'}
    )
    print(f"Result: {result.success}")
    print(f"Error: {result.error}")

    print("\n--- Test Scenario 3: Approval required (manual input) ---")
    print("Next test will require your approval...")
    result = executor.execute_tool(
        agent_id='standard_agent',
        tool_name='write_file',
        parameters={'path': '/tmp/test', 'content': 'data'}
    )
    print(f"Result: {result.success}")
    print(f"Approval granted: {result.approval_granted}")

    # 5. Show audit statistics
    print("\n--- Audit Statistics ---")
    stats = audit_logger.get_agent_statistics('restricted_agent')
    print(f"Agent: restricted_agent")
    print(f"Total executions: {stats['total_executions']}")
    print(f"Success rate: {stats.get('success_rate', 0):.2%}")

    print("\n" + "=" * 60)
    print("Demo complete")


if __name__ == '__main__':
    run_demo()
