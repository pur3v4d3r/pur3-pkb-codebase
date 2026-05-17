"""
Shared rate-limiter instance.

Imported by both main.py (to register with the app) and any router that
needs to apply a custom per-endpoint limit, avoiding circular imports.
"""
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address, default_limits=["60/minute"])
