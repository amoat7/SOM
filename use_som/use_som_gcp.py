"""
Script to test cloud deployment of SOM

Author: David Amoateng
Date: 03-06-22
"""
import json
import shutil
import time
import requests
import numpy as np

start = time.time()

training_data = np.random.rand(10, 3)
training_data = json.dumps(training_data.tolist())
MAX_EPOCHS = 100
MAP_SIZE = 10
LEARNING_RATE = 0.1

payload = {
    "input_data": training_data,
    "max_epochs": MAX_EPOCHS,
    "map_size": MAP_SIZE,
    "learning_rate": LEARNING_RATE
}


session = requests.Session()
with session.post("https://kohonen-ermg44f2xa-uc.a.run.app/kohonen",
                  json=payload, stream=True) as sess:
    with open(f'som_plots/som_{int(time.time())}.png', 'wb') as file_:
        shutil.copyfileobj(sess.raw, file_)
end = time.time()
total_time = end - start
print(f"Total time - {total_time} seconds")
