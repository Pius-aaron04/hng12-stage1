from fastapi import FastAPI
from .maths_utils import (
        is_perfect, is_even, get_fact,
        is_prime, is_armstrong, digit_sum
        )

app = FastAPI()


@app.get('/')
async def api_root():
    return "WELCOME TO HNG-12 stage 1 root"


@app.get('/api/')
async def api_root():
    return "WELCOME TO HNG-12 stage 1 API root"


@app.get('/api/classify-number')
async def classify_number(number: int) -> dict:

    # number properties
    properties = ["even" if is_even(number) else "odd"]
    if is_armstrong(number):
        properties.append("armstrong")
    response = {
                "number": number,
                "is_prime": is_prime(number),
                "is_perfect": is_perfect(number),
                "properties": properties,
                "digit_sum": digit_sum(number),
                "fun_fact": get_fact(number)
             }

    return response
