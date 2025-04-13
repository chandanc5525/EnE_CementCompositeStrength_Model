from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from src.<project_name>.utils import load_model

app = FastAPI()
model = load_model("models/xgb_model.pkl")

class InputData(BaseModel):
    data: list

@app.post("/predict")
def predict(input_data: InputData):
    data = np.array(input_data.data).reshape(1, -1)
    prediction = model.predict(data)
    return {"prediction": prediction.tolist()}
