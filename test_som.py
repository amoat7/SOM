import requests
import numpy as np 
import json
import shutil

from sklearn.model_selection import learning_curve

training_data = np.random.rand(10, 3)
training_data = json.dumps(training_data.tolist())
max_epochs = 1000
map_size = 100
learning_rate = 0.1

payload = {
    "input_data":training_data,
    "max_epochs": max_epochs,
    "map_size": map_size,
    "learning_rate": learning_rate
}

session = requests.Session()
with session.post("http://0.0.0.0:80/kohonen", json=payload, stream=True) as r:
    with open('image.png', 'wb') as f:
        shutil.copyfileobj(r.raw, f)