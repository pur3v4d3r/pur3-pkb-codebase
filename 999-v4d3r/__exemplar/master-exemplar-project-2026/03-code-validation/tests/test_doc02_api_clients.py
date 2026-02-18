"""
Unit Tests for DOC-02 Extended Thinking Architecture - API Clients & Caching
============================================================================

Tests for Extended Thinking API client initialization, request generation,
budget tracking, and caching system behavior.

Test Coverage:
- Extended Thinking API client initialization with configuration
- Extended thinking generation with token budget tracking
- Cache hit/miss behavior and invalidation logic

Reference: doc2-extended-thinking-architecture-implementation-guide.md
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta


# ============================================================================
# Extended Thinking API Client Implementation (stub for testing)
# ============================================================================

class ExtendedThinkingConfig:
    """Configuration for Extended Thinking API client."""

    def __init__(
        self,
        model: str = "claude-sonnet-4",
        thinking_mode: str = "enabled",
        max_tokens: int = 4000,
        thinking_budget: int = 1000,
        temperature: float = 1.0,
        enable_caching: bool = True
    ):
        self.model = model
        self.thinking_mode = thinking_mode
        self.max_tokens = max_tokens
        self.thinking_budget = thinking_budget
        self.temperature = temperature
        self.enable_caching = enable_caching

    def validate(self):
        """Validate configuration parameters."""
        if self.thinking_mode not in ["enabled", "disabled", "auto", "interleaved"]:
            raise ValueError(f"Invalid thinking_mode: {self.thinking_mode}")

        if self.max_tokens < 100:
            raise ValueError("max_tokens must be at least 100")

        if self.thinking_budget > self.max_tokens:
            raise ValueError("thinking_budget cannot exceed max_tokens")

        if not (0.0 <= self.temperature <= 2.0):
            raise ValueError("temperature must be between 0.0 and 2.0")

        return True


class ExtendedThinkingClient:
    """API client for Extended Thinking requests."""

    def __init__(self, api_key: str, config: ExtendedThinkingConfig):
        """
        Initialize Extended Thinking API client.

        Args:
            api_key: API authentication key
            config: ExtendedThinkingConfig instance
        """
        if not api_key:
            raise ValueError("API key is required")

        self.api_key = api_key
        self.config = config
        self.config.validate()

        # Initialize tracking
        self.total_tokens_used = 0
        self.thinking_tokens_used = 0
        self.output_tokens_used = 0
        self.request_count = 0

    def generate(self, prompt: str, system_prompt: str = None) -> dict:
        """
        Generate extended thinking response.

        Args:
            prompt: User prompt
            system_prompt: Optional system prompt

        Returns:
            Dict with thinking_content, output_content, and token usage
        """
        if not prompt:
            raise ValueError("Prompt cannot be empty")

        self.request_count += 1

        # Simulate token usage
        thinking_tokens = min(len(prompt) * 2, self.config.thinking_budget)
        output_tokens = len(prompt) * 3
        total_tokens = thinking_tokens + output_tokens

        # Check budget constraints
        if thinking_tokens > self.config.thinking_budget:
            thinking_tokens = self.config.thinking_budget

        if total_tokens > self.config.max_tokens:
            # Scale down proportionally
            scale = self.config.max_tokens / total_tokens
            thinking_tokens = int(thinking_tokens * scale)
            output_tokens = int(output_tokens * scale)
            total_tokens = thinking_tokens + output_tokens

        # Update tracking
        self.thinking_tokens_used += thinking_tokens
        self.output_tokens_used += output_tokens
        self.total_tokens_used += total_tokens

        return {
            "thinking_content": f"[Extended thinking for: {prompt[:50]}...]",
            "output_content": f"Response to: {prompt[:50]}...",
            "usage": {
                "thinking_tokens": thinking_tokens,
                "output_tokens": output_tokens,
                "total_tokens": total_tokens
            },
            "model": self.config.model,
            "thinking_mode": self.config.thinking_mode
        }

    def get_usage_stats(self) -> dict:
        """Get cumulative usage statistics."""
        return {
            "total_tokens": self.total_tokens_used,
            "thinking_tokens": self.thinking_tokens_used,
            "output_tokens": self.output_tokens_used,
            "request_count": self.request_count,
            "avg_tokens_per_request": (
                self.total_tokens_used / self.request_count
                if self.request_count > 0 else 0
            )
        }


# ============================================================================
# Caching System Implementation (stub for testing)
# ============================================================================

class CacheEntry:
    """Cache entry with expiration and metadata."""

    def __init__(self, key: str, value: dict, ttl_seconds: int = 3600):
        self.key = key
        self.value = value
        self.created_at = datetime.now()
        self.ttl_seconds = ttl_seconds
        self.access_count = 0
        self.last_accessed = self.created_at

    def is_expired(self) -> bool:
        """Check if cache entry has expired."""
        age = (datetime.now() - self.created_at).total_seconds()
        return age > self.ttl_seconds

    def access(self):
        """Record cache access."""
        self.access_count += 1
        self.last_accessed = datetime.now()


class ExtendedThinkingCache:
    """Cache system for Extended Thinking responses."""

    def __init__(self, default_ttl: int = 3600, max_entries: int = 1000):
        """
        Initialize cache system.

        Args:
            default_ttl: Default time-to-live in seconds
            max_entries: Maximum cache entries before eviction
        """
        self.default_ttl = default_ttl
        self.max_entries = max_entries
        self.cache = {}
        self.hits = 0
        self.misses = 0
        self.evictions = 0

    def get(self, key: str) -> dict:
        """
        Get cached response.

        Args:
            key: Cache key (typically prompt hash)

        Returns:
            Cached response or None
        """
        if key not in self.cache:
            self.misses += 1
            return None

        entry = self.cache[key]

        # Check expiration
        if entry.is_expired():
            del self.cache[key]
            self.misses += 1
            return None

        # Valid hit
        entry.access()
        self.hits += 1
        return entry.value

    def set(self, key: str, value: dict, ttl: int = None):
        """
        Cache response.

        Args:
            key: Cache key
            value: Response to cache
            ttl: Optional custom TTL (uses default if None)
        """
        # If updating existing key, just update it
        if key in self.cache:
            ttl = ttl if ttl is not None else self.default_ttl
            self.cache[key] = CacheEntry(key, value, ttl)
            return

        # Enforce max entries with LRU eviction for new keys
        if len(self.cache) >= self.max_entries:
            self._evict_lru()

        ttl = ttl if ttl is not None else self.default_ttl
        self.cache[key] = CacheEntry(key, value, ttl)

    def invalidate(self, key: str) -> bool:
        """
        Invalidate cache entry.

        Args:
            key: Cache key to invalidate

        Returns:
            True if entry was found and removed
        """
        if key in self.cache:
            del self.cache[key]
            return True
        return False

    def clear(self):
        """Clear all cache entries."""
        self.cache.clear()
        self.hits = 0
        self.misses = 0
        self.evictions = 0

    def get_stats(self) -> dict:
        """Get cache statistics."""
        total_requests = self.hits + self.misses
        hit_rate = self.hits / total_requests if total_requests > 0 else 0

        return {
            "hits": self.hits,
            "misses": self.misses,
            "evictions": self.evictions,
            "hit_rate": hit_rate,
            "entry_count": len(self.cache),
            "max_entries": self.max_entries
        }

    def _evict_lru(self):
        """Evict least recently used entry."""
        if not self.cache:
            return

        # Find LRU entry
        lru_key = min(
            self.cache.keys(),
            key=lambda k: self.cache[k].last_accessed
        )

        del self.cache[lru_key]
        self.evictions += 1


# ============================================================================
# Test Cases
# ============================================================================

@pytest.mark.doc02
@pytest.mark.unit
class TestExtendedThinkingAPIClient:
    """Test suite for Extended Thinking API client initialization and generation."""

    def test_api_client_initialization(self, sample_extended_thinking):
        """
        Test API client initialization with configuration.

        Validates:
        - Client initializes with valid API key and config
        - Configuration validation catches invalid parameters
        - Default configuration values are set correctly
        - Client tracks usage statistics from initialization
        """
        # Arrange
        api_key = "test-api-key-12345"
        config = ExtendedThinkingConfig(
            model="claude-sonnet-4",
            thinking_mode="enabled",
            max_tokens=4000,
            thinking_budget=1000,
            temperature=1.0,
            enable_caching=True
        )

        # Act
        client = ExtendedThinkingClient(api_key=api_key, config=config)

        # Assert - Client initialization
        assert client.api_key == api_key
        assert client.config.model == "claude-sonnet-4"
        assert client.config.thinking_mode == "enabled"
        assert client.config.max_tokens == 4000
        assert client.config.thinking_budget == 1000
        assert client.config.temperature == 1.0
        assert client.config.enable_caching is True

        # Assert - Initial usage tracking
        assert client.total_tokens_used == 0
        assert client.thinking_tokens_used == 0
        assert client.output_tokens_used == 0
        assert client.request_count == 0

        # Test invalid configurations
        with pytest.raises(ValueError, match="Invalid thinking_mode"):
            invalid_config = ExtendedThinkingConfig(thinking_mode="invalid")
            ExtendedThinkingClient(api_key=api_key, config=invalid_config)

        with pytest.raises(ValueError, match="max_tokens must be at least 100"):
            invalid_config = ExtendedThinkingConfig(max_tokens=50)
            ExtendedThinkingClient(api_key=api_key, config=invalid_config)

        with pytest.raises(ValueError, match="thinking_budget cannot exceed max_tokens"):
            invalid_config = ExtendedThinkingConfig(
                max_tokens=1000,
                thinking_budget=2000
            )
            ExtendedThinkingClient(api_key=api_key, config=invalid_config)

        # Test missing API key
        with pytest.raises(ValueError, match="API key is required"):
            ExtendedThinkingClient(api_key="", config=config)

    def test_api_client_generate(self, sample_extended_thinking):
        """
        Test extended thinking generation with budget tracking.

        Validates:
        - Client generates response with thinking and output content
        - Token usage is tracked correctly (thinking + output)
        - Thinking budget constraints are enforced
        - Max tokens limit is respected
        - Multiple requests accumulate usage statistics
        """
        # Arrange
        api_key = "test-api-key-12345"
        config = ExtendedThinkingConfig(
            model="claude-sonnet-4",
            thinking_mode="enabled",
            max_tokens=4000,
            thinking_budget=1000,
            temperature=1.0
        )
        client = ExtendedThinkingClient(api_key=api_key, config=config)

        prompt = "Explain the concept of extended thinking in AI systems."

        # Act
        response = client.generate(prompt)

        # Assert - Response structure
        assert "thinking_content" in response
        assert "output_content" in response
        assert "usage" in response
        assert "model" in response
        assert "thinking_mode" in response

        assert response["model"] == "claude-sonnet-4"
        assert response["thinking_mode"] == "enabled"
        assert prompt[:50] in response["thinking_content"]
        assert prompt[:50] in response["output_content"]

        # Assert - Token usage
        usage = response["usage"]
        assert "thinking_tokens" in usage
        assert "output_tokens" in usage
        assert "total_tokens" in usage

        assert usage["thinking_tokens"] > 0
        assert usage["output_tokens"] > 0
        assert usage["total_tokens"] == usage["thinking_tokens"] + usage["output_tokens"]

        # Assert - Budget constraint enforcement
        assert usage["thinking_tokens"] <= config.thinking_budget
        assert usage["total_tokens"] <= config.max_tokens

        # Assert - Client tracking updated
        assert client.request_count == 1
        assert client.thinking_tokens_used == usage["thinking_tokens"]
        assert client.output_tokens_used == usage["output_tokens"]
        assert client.total_tokens_used == usage["total_tokens"]

        # Test multiple requests accumulate stats
        response2 = client.generate("Follow-up question")

        assert client.request_count == 2
        assert client.total_tokens_used == (
            usage["total_tokens"] + response2["usage"]["total_tokens"]
        )

        # Test usage stats method
        stats = client.get_usage_stats()
        assert stats["request_count"] == 2
        assert stats["total_tokens"] == client.total_tokens_used
        assert stats["thinking_tokens"] == client.thinking_tokens_used
        assert stats["output_tokens"] == client.output_tokens_used
        assert stats["avg_tokens_per_request"] == client.total_tokens_used / 2

        # Test empty prompt validation
        with pytest.raises(ValueError, match="Prompt cannot be empty"):
            client.generate("")


@pytest.mark.doc02
@pytest.mark.unit
class TestExtendedThinkingCache:
    """Test suite for Extended Thinking caching system."""

    def test_caching_system_hit_miss(self, sample_cache_scenarios):
        """
        Test cache hit/miss behavior and invalidation.

        Validates:
        - Cache miss on first access
        - Cache hit on subsequent access with same key
        - Expired entries return cache miss
        - Cache invalidation removes entries
        - LRU eviction when max entries exceeded
        - Cache statistics track hits/misses/evictions
        """
        # Arrange
        cache = ExtendedThinkingCache(default_ttl=3600, max_entries=100)

        prompt1 = "What is 2+2?"
        key1 = "hash_prompt1"
        response1 = {
            "thinking_content": "Let me calculate 2+2...",
            "output_content": "The answer is 4"
        }

        prompt2 = "What is the meaning of life?"
        key2 = "hash_prompt2"
        response2 = {
            "thinking_content": "This is a philosophical question...",
            "output_content": "42"
        }

        # Act & Assert - Cache miss on first access
        result = cache.get(key1)
        assert result is None
        assert cache.misses == 1
        assert cache.hits == 0

        # Act & Assert - Set cache entry
        cache.set(key1, response1)
        assert len(cache.cache) == 1

        # Act & Assert - Cache hit on subsequent access
        result = cache.get(key1)
        assert result is not None
        assert result == response1
        assert cache.hits == 1
        assert cache.misses == 1

        # Verify access tracking
        entry = cache.cache[key1]
        assert entry.access_count == 1

        # Act & Assert - Multiple hits increment counter
        cache.get(key1)
        cache.get(key1)
        assert cache.hits == 3
        assert entry.access_count == 3

        # Act & Assert - Different key results in miss
        result = cache.get(key2)
        assert result is None
        assert cache.misses == 2

        # Set second entry
        cache.set(key2, response2)
        assert len(cache.cache) == 2

        # Test cache invalidation
        invalidated = cache.invalidate(key1)
        assert invalidated is True
        assert len(cache.cache) == 1
        assert key1 not in cache.cache

        result = cache.get(key1)
        assert result is None
        assert cache.misses == 3

        # Test invalidating non-existent key
        invalidated = cache.invalidate("nonexistent_key")
        assert invalidated is False

        # Test expiration behavior
        short_ttl_cache = ExtendedThinkingCache(default_ttl=1)
        short_ttl_cache.set("temp_key", {"data": "temporary"})

        # Immediate access should hit
        result = short_ttl_cache.get("temp_key")
        assert result is not None
        assert short_ttl_cache.hits == 1

        # Simulate expiration by manipulating entry
        short_ttl_cache.cache["temp_key"].created_at = (
            datetime.now() - timedelta(seconds=2)
        )

        # Access after expiration should miss
        result = short_ttl_cache.get("temp_key")
        assert result is None
        assert short_ttl_cache.misses == 1
        assert "temp_key" not in short_ttl_cache.cache

        # Test LRU eviction
        small_cache = ExtendedThinkingCache(default_ttl=3600, max_entries=3)
        small_cache.set("key1", {"data": "value1"})
        small_cache.set("key2", {"data": "value2"})
        small_cache.set("key3", {"data": "value3"})

        # Access key1 and key2 to make key3 LRU
        small_cache.get("key1")
        small_cache.get("key2")

        # Adding 4th entry should evict key3 (LRU)
        small_cache.set("key4", {"data": "value4"})

        assert len(small_cache.cache) == 3
        assert "key3" not in small_cache.cache
        assert "key1" in small_cache.cache
        assert "key2" in small_cache.cache
        assert "key4" in small_cache.cache
        assert small_cache.evictions == 1

        # Test cache statistics
        stats = cache.get_stats()
        assert stats["hits"] == cache.hits
        assert stats["misses"] == cache.misses
        assert stats["evictions"] == cache.evictions
        assert stats["entry_count"] == len(cache.cache)
        assert stats["max_entries"] == cache.max_entries
        assert 0.0 <= stats["hit_rate"] <= 1.0

        # Test clear functionality
        cache.clear()
        assert len(cache.cache) == 0
        assert cache.hits == 0
        assert cache.misses == 0
        assert cache.evictions == 0

        # Test custom TTL
        cache.set("custom_ttl_key", {"data": "value"}, ttl=7200)
        entry = cache.cache["custom_ttl_key"]
        assert entry.ttl_seconds == 7200


# ============================================================================
# Test Execution Entry Point
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-m", "doc02"])
