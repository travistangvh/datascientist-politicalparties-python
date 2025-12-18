from pathlib import Path
from typing import List
from urllib.request import urlretrieve

import pandas as pd


class DataLoader:
    """Class to load the political parties dataset"""

    data_url: str = "https://www.chesdata.eu/s/CHES2019V3.dta"

    def __init__(self):
        self.party_data = self._download_data()
        self.non_features = []
        self.index = ["party_id", "party", "country"]

    def _download_data(self) -> pd.DataFrame:
        data_path, _ = urlretrieve(
            self.data_url,
            Path(__file__).parents[2].joinpath(*["data", "CHES2019V3.dta"]),
        )
        return pd.read_stata(data_path)

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to remove duplicates in a dataframe"""
        return df.drop_duplicates()
        ##### YOUR CODE GOES HERE #####
        pass

    def remove_nonfeature_cols(
        self, df: pd.DataFrame, non_features: List[str], index: List[str]
    ) -> pd.DataFrame:
        """Write a function to remove certain features cols and set certain cols as indices
        in a dataframe"""
        ##### YOUR CODE GOES HERE #####
        df = df.drop(columns=non_features).set_index(index)
        return df
        pass

    def handle_NaN_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to handle NaN values in a dataframe"""
        ##### YOUR CODE GOES HERE #####
        df = df.dropna(axis=1, how='all')
        df = df.fillna(0)
        return df
        pass

    def scale_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to normalise values in a dataframe. Use StandardScaler."""
        ##### YOUR CODE GOES HERE #####
        numerical_cols = df.select_dtypes(include=['number']).columns
        from sklearn.preprocessing import StandardScaler
        ss = StandardScaler()
        ss.fit(df[numerical_cols])
        df[numerical_cols] = ss.transform(df[numerical_cols])
        return df
        pass

    def preprocess_data(self):
        """Write a function to combine all pre-processing steps for the dataset"""
        ##### YOUR CODE GOES HERE #####
        print(self.party_data)
        df = self.remove_duplicates(self.party_data)
        df = self.remove_nonfeature_cols(df, self.non_features, self.index)
        df = self.handle_NaN_values(df)
        df = self.scale_features(df)
        self.party_data = df
        print(df)
        pass
