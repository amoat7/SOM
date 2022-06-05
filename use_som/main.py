"""
Script to use som library

Author: David Amoateng
Date: 03-06-22
"""
import json
from typing import Optional
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from som_library import Som


class Items(BaseModel):
    '''
    parameter definitions
    '''
    input_data: str
    max_epochs: Optional[int] = 100
    map_size: Optional[int] = 10
    learning_rate: Optional[float] = 0.1
    local: Optional[bool] = False


app = FastAPI()


@app.post("/kohonen")
def kohonen(params: Items):
    '''
    post request function

    returns Streaming response
    '''

    training_data = params.input_data
    max_epochs = params.max_epochs
    map_size = params.map_size
    learning_rate = params.learning_rate
    training_data = np.asarray(json.loads(training_data))
    local = params.locals

    my_som = Som(input_data=training_data, max_epochs=max_epochs,
                 map_size=map_size, learning_rate=learning_rate, local=local)
    response = my_som.train_som()
    return response
