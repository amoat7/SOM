"""
Script to use local deployment of SOM

Author: David Amoateng
Date: 03-06-22
"""
import shutil
import time
import numpy as np
from som_library import Som

  
start = time.time()
# specify input parameters to SOM
training_data = np.random.rand(10, 3)
MAX_EPOCHS = 200
MAP_SIZE = 30
LEARNING_RATE = 0.1
LOCAL = True


my_som = Som(input_data=training_data, max_epochs=MAX_EPOCHS,
                map_size=MAP_SIZE, learning_rate=LEARNING_RATE, local=LOCAL)

my_som.train_som()
end = time.time()
total_time = end - start
print(f"Total time - {total_time} seconds")
