"""
Main file for API.
"""

from typing import Union, List
from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/")
async def read_root():
    """


    Gets factual results from keyword or topic entered into the search bar.
    """
    return {"Hello": "World"}


@app.get("/facts")
async def read_fact(fact_id: int, description: str, q: Union[str, None] = None):
    """
    A concise description of what the function does.

    Args:
        fact_id: .
        chat_description: .

    Returns:
        The value returned by the function. Describe its type and meaning.

    Gets factual results from keyword or topic entered into the search bar.
    """
    return {"fact_id": fact_id, "description": description,"q": q, }

@app.get("/facts/{fact_id}")
async def read_fact_id(fact_id: int, q: Union[str, None] = None):
    """
    Gets factual results from keyword or topic entered into the search bar by ID.
    """
    return {"fact_id": fact_id, "q": q}

@app.post("/facts")
async def add_to_fun_fact(fun_fact: str, q: Union[str, None] = None):
    """
    Add fact result to fun fact list.
    """
    return {"fun_fact":fun_fact}
    ...

@app.delete("/facts")
async def delet_fun_fact(fun_fact: str, q: Union[str, None] = None):
    """
    Delete fact from your fun fact list.
    """
    ...

@app.put("/facts")
async def update_prompt(q: Union[str, None] = None):
    """
    Update prompt to expand or change search result.
    """
    ...

