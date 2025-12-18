import pandas as pd


class DimensionalityReducer:
    """Class to model a dimensionality reduction method for the given dataset.
    1. Write a function to convert the high dimensional data to 2 dimensional.
    """

    def __init__(self, type, data: pd.DataFrame, n_components: int = 2):
        self.n_components = n_components
        self.data = data

    ##### YOUR CODE GOES HERE #####
    def transform(self):
        from sklearn.decomposition import PCA
        pca = PCA(n_components = self.n_components)
        pca.fit(self.data)
        return pd.DataFrame(pca.transform(self.data))
