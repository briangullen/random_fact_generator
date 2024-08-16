import random

from fastapi import FastAPI
from pydantic import BaseModel


class Fact(BaseModel):
    id: int
    fact: str


facts = [
    Fact(id=0, fact="Owls don't have eyeballs. They have eye tubes."),
    Fact(id=1, fact="Giraffes are 30 times more likely to get hit by lightning than people."),
    Fact(id=2, fact="Butterflies can taste with their feet."),
    Fact(id=3, fact="The extinct colossus penguin stood as tall as LeBron James."),
    Fact(id=4, fact="The blue whale's tongue can weight as much as an elephant."),
    Fact(id=5, fact="Fish form orderly queues in emergencies.")
]

app = FastAPI()


@app.get('/fact')
async def get_random():
    random_fact = random.choice(facts)
    return random_fact


@app.get('/fact/all')
async def get_all():
    return facts


@app.get('/fact/{fact_id}')
async def get_fact_id(fact_id: int):
    return facts[fact_id]


@app.post('/fact')
async def add_fact(fact: Fact):
    facts.append(fact)
    return fact
