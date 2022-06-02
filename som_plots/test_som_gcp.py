import requests
import numpy as np 
import json
import shutil


training_data = np.random.rand(10, 3)
training_data = json.dumps(training_data.tolist())
max_epochs = 200
map_size = 10
learning_rate = 0.1

payload = {
    "input_data":training_data,
    "max_epochs": max_epochs,
    "map_size": map_size,
    "learning_rate": learning_rate
}

session = requests.Session()
with session.post("http://0.0.0.0:80/kohonen", json=payload, stream=True) as sess:
    with open('/som_plots/som.png', 'wb') as file_:
        shutil.copyfileobj(sess.raw, file_)