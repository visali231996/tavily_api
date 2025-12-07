from fastapi import FastAPI

from example import get_response
app = FastAPI(title="sales Agent", description="latest news updates")
@app.get("/agent/{query}")
def get_ai_response(query:str):
    response = get_response(query)
    return {'response': response}