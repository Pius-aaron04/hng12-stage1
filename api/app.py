from fastapi import FastAPI, Request
from .maths_utils import (
        is_perfect, is_even, get_fact,
        is_prime, is_armstrong, digit_sum
        )
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request,
                                       exc: RequestValidationError):
    query_string = request.scope['query_string'].decode()
    if len(query_string.split('=')) <= 1:
        return JSONResponse(status_code=400,
                            content={"number": None, "error": "true"})
    return JSONResponse(status_code=400,
                        content={"number": "alphabet", "error": True})


@app.get('/')
async def api_root():
    return "WELCOME TO HNG-12 stage 1 root"


@app.get('/api/')
async def api_root():
    return "WELCOME TO HNG-12 stage 1 API root"


@app.get('/api/classify-number')
async def classify_number(number: int) -> dict:

    factos = await get_fact(number)
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
                "fun_fact": factos
             }

    return response
