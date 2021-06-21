import numpy as np
import matplotlib.pyplot as plt


class DataSegment():
    def __init__(self, raw_data=[], data_size=0) -> None:
        self.raw_data = raw_data
        if type(self.raw_data) != list:
            raise ValueError("No data given to normalize")
        self.data_size = data_size
        if len(self.raw_data) != self.data_size:
            raise ValueError("Size of data and data don't match")

    def standardize(self):
        use_data = np.asarray(self.raw_data)
        self.data = (use_data - np.mean(use_data))/np.std(use_data)
        plt.plot(self.data)
        plt.show()

    def scale(self, ptp=1, centre=0):
        use_data = np.asarray(self.raw_data)
        self.data = ptp*((use_data - np.min(use_data)) /
                         np.ptp(use_data)-0.5+centre)
        plt.plot(self.data, c='k')
        plt.show()
