import asyncio
import json
import logging
from typing import Callable, Awaitable

logger = logging.getLogger(__name__)


class MQTTHandler:
    """Async MQTT message handler for ESP32 sensor data."""

    def __init__(self, broker_host: str = "emqx", broker_port: int = 1883) -> None:
        self.broker_host = broker_host
        self.broker_port = broker_port
        self._handlers: dict[str, Callable[[dict], Awaitable[None]]] = {}

    def subscribe(self, topic: str):
        def decorator(fn: Callable[[dict], Awaitable[None]]):
            self._handlers[topic] = fn
            return fn
        return decorator

    async def dispatch(self, topic: str, payload: bytes) -> None:
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            logger.warning("Invalid JSON on topic %s", topic)
            return
        handler = self._handlers.get(topic)
        if handler:
            await handler(data)
        else:
            logger.debug("No handler for topic %s", topic)

    async def run(self) -> None:
        logger.info("MQTT handler connecting to %s:%d", self.broker_host, self.broker_port)
        await asyncio.sleep(0)
