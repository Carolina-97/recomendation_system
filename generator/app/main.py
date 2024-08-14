from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/generate/")
async def generate_recommendation(model_name: str = Body(...), viewerid: int = Body(...)):
    import random
    random_number = random.randint(1, 100)
    return {"reason": model_name, "result": random_number}
