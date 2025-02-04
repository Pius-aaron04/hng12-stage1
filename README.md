# HNG12 - Stage 1 Task

## Classify number API
This is a simple API app that takes an integer via a query parameter and returns its mathematical properties like wise a fun fact as related to mathematics.

### Resources
* [Fun fact API](https://numbersapi.com)
* [Parity](https://en.wikipedia.org/wiki/Parity)

### API Specification
* Endpoint: ```GET https://hng12-stage1-7jig.onrender.com/api/classify?number=371```
* Response 200(OK):
  ```json
  {
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
  }
  ```
  * Response 400(Bad Request):
  ```json
  {
    "number": "alphabet",
    "error": true
  }
  ```

  ### Installation
* Clone repository
    ```bash
    git clone https://github.com/Pius-aaron04/hng12-stage1
    cd hng12-stage1
    ```
* Install requirements
     ```bash
     pip install -r requirements.txt
     ```

  ### Execution
  ```bash
  fastapi run app.py
  ```
