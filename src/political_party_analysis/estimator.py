import pandas as pd


class DensityEstimator:
    """Class to estimate Density/Distribution of the given data.
    1. Write a function to model the distribution of the political party dataset
    2. Write a function to randomly sample 10 parties from this distribution
    3. Map the randomly sampled 10 parties back to the original higher dimensional
    space as per the previously used dimensionality reduction technique.
    """

    def __init__(self, data: pd.DataFrame, dim_reducer, high_dim_feature_names):
        self.data = data
        self.dim_reducer_model = dim_reducer
        self.feature_names = high_dim_feature_names

        from sklearn.mixture import GaussianMixture
        self.model = GaussianMixture(n_components=10)
        self.model.fit(self.data)

    ##### YOUR CODE GOES HERE #####
    def sample(self):
        return self.model.sample(10)

    def map_back(self):
        return self.model.map_back(self.sample)