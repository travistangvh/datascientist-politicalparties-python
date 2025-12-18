from pathlib import Path

from matplotlib import pyplot

from political_party_analysis.loader import DataLoader
from political_party_analysis.visualization import scatter_plot
from political_party_analysis.dim_reducer import DimensionalityReducer
from political_party_analysis.estimator import DensityEstimator
from political_party_analysis.visualization import plot_density_estimation_results

if __name__ == "__main__":

    data_loader = DataLoader()
    # Data pre-processing step
    ##### YOUR CODE GOES HERE #####
    data_loader.preprocess_data()
    # Dimensionality reduction step
    ##### YOUR CODE GOES HERE #####
    dim_reducer = DimensionalityReducer("PCA", data_loader.party_data)
    reduced_dim_data = dim_reducer.transform()
    ## Uncomment this snippet to plot dim reduced data
    pyplot.figure()
    splot = pyplot.subplot()
    scatter_plot(
        reduced_dim_data,
        color="r",
        splot=splot,
        label="dim reduced data",
    )
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "dim_reduced_data.png"]))

    # Density estimation/distribution modelling step
    ##### YOUR CODE GOES HERE #####
    density_estimator = DensityEstimator(reduced_dim_data, dim_reducer, data_loader.party_data.columns)
    density_estimator.model.fit(reduced_dim_data)
    b = density_estimator.sample()
    # a = density_estimator.map_back()
    # print(b)

    # Plot density estimation results here
    ##### YOUR CODE GOES HERE #####
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "density_estimation.png"]))

    # Plot left and right wing parties here
    pyplot.figure()
    splot = pyplot.subplot()
    ##### YOUR CODE GOES HERE #####
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "left_right_parties.png"]))
    pyplot.title("Lefty/righty parties")

    # Plot finnish parties here
    ##### YOUR CODE GOES HERE #####
    # plot_density_estimation_results(reduced_dim_data, density_estimator.sample(), density_estimator.map_back())
#     plot_density_estimation_results(
#     X: pd.DataFrame,
#     Y_: np.ndarray,
#     means: np.ndarray,
#     covariances: np.ndarray,
#     title: str,
# ):
    plot_density_estimation_results(reduced_dim_data, density_estimator.sample(), density_estimator.model.means_, density_estimator.model.covariances_, "Density Estimation")


    print("Analysis Complete")
