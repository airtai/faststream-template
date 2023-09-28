import asyncio
import random

from faststream import FastStream, Logger
from faststream.kafka import KafkaBroker
from pydantic import BaseModel, Field


class Name(BaseModel):
    name: str = Field(..., description="Name of the person")


class Greeting(BaseModel):
    greeting: str = Field(..., description="Greeting message")


broker = KafkaBroker("localhost:9092")
app = FastStream(
    broker, title="My service", version="0.1.0", description="My service description"
)

to_greetings = broker.publisher("greetings")


@broker.subscriber("names")  # type: ignore
async def on_names(msg: Name, logger: Logger) -> None:
    result = f"hello {msg.name}"
    logger.info(result)
    greeting = Greeting(greeting=result)
    await to_greetings.publish(greeting)


@app.after_startup
async def publish_names() -> None:
    async def _publish_names() -> None:
        while True:
            name = random.choice(  # nosec
                [
                    "Ana",
                    "Mario",
                    "Pedro",
                    "João",
                    "Gustavo",
                    "Joana",
                    "Mariana",
                    "Juliana",
                ],
            )
            await broker.publish(Name(name=name), topic="names")
            await asyncio.sleep(2)

    asyncio.create_task(_publish_names())
