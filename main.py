from typing import Optional 

from fastapi import FastAPI, Path
from typing import List
from pydantic import BaseModel
from som_library import Som
import numpy as np 
import json

class Items(BaseModel):
    input_data: str
    max_epochs: Optional[int] = 100
    map_size: Optional[int] = 10
    learning_rate: Optional[float] = 0.1

app = FastAPI()

@app.post("/kohonen")
def kohonen(params: Items):
    
    training_data = params.input_data
    max_epochs = params.max_epochs
    map_size = params.map_size
    learning_rate = params.learning_rate
    training_data = np.asarray(json.loads(training_data))

    my_som = Som(input_data=training_data, max_epochs=max_epochs,
             map_size=map_size, learning_rate=learning_rate)
    a = my_som.train_som()
    return a 
