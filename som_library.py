"""
Script to implement Kohonen self organising map using numpy

Author: David Amoateng
Date: 03-06-22
"""
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from fastapi.responses import StreamingResponse


class Som:
    """
    2D Kohonen self organising map class
    """

    def __init__(self,
                 input_data: np.ndarray,
                 max_epochs: int = 50,
                 map_size: int = 10,
                 learning_rate: int = 0.1) -> None:
        """
        Parameters
        ----------
        input_data : np.ndarray
            The input data
        max_epochs: int, optional
            Maximum number of epochs required to stop training
        map_size: int, optional
            Size of kohonen network. Assumes a square shape
        learning_rate: int, optional
            Initial learning rate for upadting SOM
        """
        self.input_data = input_data
        self.max_epochs = max_epochs
        self.map_size = map_size
        self.learning_rate = learning_rate
        # initialise SOM
        self.intial_som = np.random.rand(
            self.map_size, self.map_size, self.input_data.shape[1])
        np.random.shuffle(self.input_data)

    @staticmethod
    def find_bmu(som: np.ndarray, sample: np.ndarray):
        """
        Calculates and returns best matching unit (bmu)

        inputs:
            som: np.ndarray
                2D self organising map
            sample: np.ndarray
                A sample of the input data
        output:
            Tuple of best matching unit coordinate array
        """
        # euclidean distance calculation
        dist_metric = (np.square(som - sample)
                       ).sum(axis=2)
        # coordinate array of bmu
        return np.unravel_index(np.argmin(dist_metric, axis=None), dist_metric.shape)

    def update_weights(self, som: np.ndarray,
                       train_ex: np.ndarray,
                       radius: float, bmu_coord: tuple):
        """
        Updates node weights of SOM

        inputs:
            som: np.ndarray
                2D self organising map
            train_ex: np.ndarray
                A training example
            radius: float
                Neighbourhood radius
            bmu_coord: tuple

        output:
            som: np.ndarray
                updated weights of SOM

        """
        bmu_x, bmu_y = bmu_coord  # unpack tuple

        # change all cells in the neighbourhood of BMU
        for node_x in range(self.map_size):
            for node_y in range(self.map_size):
                # calculate distance of nodes to BMU
                bmu_distance = np.square(
                    node_x-bmu_x) + np.square(node_y-bmu_y)
                # calculate influence decay over time
                influence = np.exp(-bmu_distance/2/radius)
                # update the weights of a given node
                som[node_x, node_y] += self.learning_rate * \
                    influence * (train_ex - som[node_x, node_y])
        return som

    def update_lr(self, epoch: int) -> None:
        """
        input:
            epoch: int
                training epoch
        output:
            None
        """
        # calculate learning rate and decay
        initial_lr = self.learning_rate
        lr_decay = self.max_epochs/np.log(initial_lr)
        self.learning_rate = initial_lr * np.exp(-epoch / lr_decay)

    def train_som(self) -> None:
        """
        input:
            None
        output:
            None
        """

        # matplotlib axes to plot SOM network updates
        Fig, axes = plt.subplots(
            nrows=1, ncols=5, figsize=(20, 5))

        # plot randomly initialised self organising map
        som = self.intial_som
        axes[0].imshow((som*255).astype(np.uint8))
        axes[0].title.set_text('Randomly Initialised SOM Grid')

        # initial radius
        initial_radius = self.map_size/2
        # radius decay
        radius_decay = self.max_epochs/np.log(initial_radius)

        # update interval for matplotlib axes
        graph_update = int(self.max_epochs/5)
        epoch = 0
        for epoch in np.arange(0, self.max_epochs):

            # Update the radius
            radius = (initial_radius * np.exp(-epoch / radius_decay))**2

            # calculate index of bmu and updated som
            for sample in self.input_data:
                bmu_index = self.find_bmu(som, sample)
                som = self.update_weights(som, sample, radius, bmu_index)

            # update matplotlib axes at regukar interval
            if epoch % graph_update == 0 and epoch > 0:
                axes[int(epoch/graph_update)
                     ].imshow((som*255).astype(np.uint8))
                axes[int(epoch/graph_update)
                     ].title.set_text('Epochs = ' + str(epoch))

        axes[4].imshow((som*255).astype(np.uint8))
        axes[4].title.set_text('Epochs = ' + str(epoch+1))

        # return plot of som as a streaming response
        image = BytesIO()
        plt.savefig(image, format="JPEG")
        image.seek(0)
        return StreamingResponse(image, media_type="image/jpg")


