#!/usr/bin/env python3
"""
Minimal Working Example: Error Recovery System
===============================================

Demonstrates error classification and recovery strategies.

Error Categories (from DOC-04):
- RETRIABLE: Network timeout, rate limit → Retry with backoff
- FIXABLE: Invalid input → Validate and correct
- FALLBACK: Component failure → Use alternative approach
- TERMINAL: Authentication error → Graceful failure

Usage:
    python error_recovery_example.py
"""

import sys
from pathlib import Path
import time
import random

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "mocks"))

from mock_tools import MockToolRegistry, FailingMockTool


class ErrorCategory:
    """Error classification categories."""
    RETRIABLE = "retriable"
    FIXABLE = "fixable"
    FALLBACK = "fallback"
    TERMINAL = "terminal"


class ErrorRecoverySystem:
    """
    Comprehensive error recovery with classification and strategies.

    Based on DOC-04 ErrorRecoverySystem pattern.
    """

    def __init__(self, max_retries=3):
        """Initialize error recovery system."""
        self.max_retries = max_retries
        self.recovery_history = []

    def classify_error(self, error: Exception) -> str:
        """
        Classify error into recovery category.

        Args:
            error: Exception to classify

        Returns:
            Error category (RETRIABLE, FIXABLE, FALLBACK, TERMINAL)
        """
        if isinstance(error, (TimeoutError, ConnectionError)):
            return ErrorCategory.RETRIABLE
        elif isinstance(error, ValueError):
            return ErrorCategory.FIXABLE
        elif isinstance(error, NotImplementedError):
            return ErrorCategory.FALLBACK
        else:
            return ErrorCategory.TERMINAL

    def retry_with_backoff(self, func, *args, **kwargs):
        """
        Retry function with exponential backoff.

        Args:
            func: Function to retry
            *args, **kwargs: Function arguments

        Returns:
            Function result if successful

        Raises:
            Exception if max retries exceeded
        """
        for attempt in range(self.max_retries):
            try:
                print(f"[RETRY] Attempt {attempt + 1}/{self.max_retries}")
                result = func(*args, **kwargs)
                print(f"[RETRY] Success on attempt {attempt + 1}")
                return result

            except Exception as e:
                category = self.classify_error(e)

                if category != ErrorCategory.RETRIABLE:
                    print(f"[RETRY] Error not retriable: {category}")
                    raise

                if attempt < self.max_retries - 1:
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                    print(f"[RETRY] Waiting {wait_time:.2f}s before retry...")
                    time.sleep(wait_time)
                else:
                    print(f"[RETRY] Max retries ({self.max_retries}) exceeded")
                    raise

    def fix_and_retry(self, func, error, *args, **kwargs):
        """
        Fix error and retry operation.

        Args:
            func: Function to retry
            error: Error that occurred
            *args, **kwargs: Function arguments

        Returns:
            Function result after fix
        """
        print(f"[FIX] Attempting to fix error: {error}")

        # Apply fixes based on error type
        if isinstance(error, ValueError):
            # Example fix: validate and correct parameters
            fixed_kwargs = kwargs.copy()
            for key, value in fixed_kwargs.items():
                if value is None:
                    fixed_kwargs[key] = "default_value"
                    print(f"[FIX] Replaced None in '{key}' with default")

            print(f"[FIX] Retrying with fixed parameters...")
            return func(*args, **fixed_kwargs)

        raise error

    def execute_fallback(self, primary_func, fallback_func, *args, **kwargs):
        """
        Execute primary function with fallback.

        Args:
            primary_func: Primary function to try
            fallback_func: Fallback function if primary fails
            *args, **kwargs: Function arguments

        Returns:
            Result from primary or fallback
        """
        try:
            print(f"[PRIMARY] Attempting primary method...")
            result = primary_func(*args, **kwargs)
            print(f"[PRIMARY] Success!")
            return result

        except Exception as e:
            category = self.classify_error(e)

            if category == ErrorCategory.FALLBACK:
                print(f"[FALLBACK] Primary failed, using fallback...")
                result = fallback_func(*args, **kwargs)
                print(f"[FALLBACK] Success!")
                return result

            raise

    def handle_error(self, error, func, *args, **kwargs):
        """
        Main error handling dispatcher.

        Args:
            error: Error to handle
            func: Function that failed
            *args, **kwargs: Function arguments

        Returns:
            Recovery result
        """
        category = self.classify_error(error)

        print(f"\n[HANDLER] Error: {type(error).__name__}")
        print(f"[HANDLER] Category: {category}")

        self.recovery_history.append({
            "error": str(error),
            "category": category,
            "timestamp": time.time()
        })

        if category == ErrorCategory.RETRIABLE:
            return self.retry_with_backoff(func, *args, **kwargs)

        elif category == ErrorCategory.FIXABLE:
            return self.fix_and_retry(func, error, *args, **kwargs)

        elif category == ErrorCategory.FALLBACK:
            # Would need fallback function provided
            print(f"[HANDLER] Fallback needed but not provided")
            raise

        else:  # TERMINAL
            print(f"[HANDLER] Terminal error - cannot recover")
            raise


def simulate_retriable_error(attempt_number=[0]):
    """Simulate operation that fails first 2 times."""
    attempt_number[0] += 1
    if attempt_number[0] < 3:
        raise TimeoutError(f"Simulated timeout on attempt {attempt_number[0]}")
    return {"status": "success", "attempt": attempt_number[0]}


def simulate_fixable_error(**kwargs):
    """Simulate operation with invalid parameters."""
    if kwargs.get('param') is None:
        raise ValueError("Parameter 'param' cannot be None")
    return {"status": "success", "param": kwargs['param']}


def simulate_fallback_error():
    """Simulate operation that requires fallback."""
    raise NotImplementedError("Primary method not available")


def fallback_method():
    """Fallback implementation."""
    return {"status": "success", "method": "fallback"}


def main():
    """Run error recovery examples."""
    print("\n" + "="*60)
    print("Minimal Working Example: Error Recovery System")
    print("="*60 + "\n")

    recovery = ErrorRecoverySystem(max_retries=3)

    # Example 1: RETRIABLE Error
    print("\n" + "-"*60)
    print("Example 1: RETRIABLE Error (Timeout)")
    print("-"*60)
    try:
        result = recovery.retry_with_backoff(simulate_retriable_error)
        print(f"[SUCCESS] Recovered: {result}")
    except Exception as e:
        print(f"[FAILED] Could not recover: {e}")

    # Example 2: FIXABLE Error
    print("\n" + "-"*60)
    print("Example 2: FIXABLE Error (Invalid Parameter)")
    print("-"*60)
    try:
        # This will fail first, then be fixed
        simulate_fixable_error(param=None)
    except ValueError as e:
        result = recovery.fix_and_retry(simulate_fixable_error, e, param=None)
        print(f"[SUCCESS] Recovered after fix: {result}")

    # Example 3: FALLBACK Error
    print("\n" + "-"*60)
    print("Example 3: FALLBACK Error (Not Implemented)")
    print("-"*60)
    try:
        result = recovery.execute_fallback(
            simulate_fallback_error,
            fallback_method
        )
        print(f"[SUCCESS] Recovered with fallback: {result}")
    except Exception as e:
        print(f"[FAILED] Could not recover: {e}")

    # Show recovery history
    print("\n" + "-"*60)
    print("Recovery History Summary")
    print("-"*60)
    print(f"Total recovery attempts: {len(recovery.recovery_history)}")
    for i, record in enumerate(recovery.recovery_history):
        print(f"  {i+1}. {record['category']}: {record['error']}")

    print("\n" + "="*60)
    print("Example Complete! ✅")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
