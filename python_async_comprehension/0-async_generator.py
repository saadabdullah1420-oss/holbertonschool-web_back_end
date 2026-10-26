#!/usr/bin/env python3
"""Generate ten random numbers with asynchronous delays."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Wait one second before yielding each of ten random numbers."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
