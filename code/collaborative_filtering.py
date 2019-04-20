import numpy as np
from .k_nearest_neighbor import KNearestNeighbor


def collaborative_filtering(input_array, n_neighbors,
                            distance_measure='euclidean', aggregator='mode'):
    """
    This is a wrapper function for your KNearestNeighbors class, that runs kNN
    as a collaborative filter.

    If there is a 0 in the array, you must impute a value determined by using your
    kNN classifier as a collaborative filter. All non-zero entries should remain
    the same.

    For example, if `input_array`(containing data we are trying to impute) looks like:

        [[0, 1],
         [1, 1],
         [1, 0]]

    We are trying to impute the 0 values by replacing the 0 values with an aggregation of the
    neighbors for that feature. If aggregation is 'mean', then the output should be:

        [[.66, 1],
         [1, 1],
         [1, .66]]

    The non-zero values are left untouched. If aggregation is 'mode', then the output should be:

        [[1, 1],
         [1, 1],
         [1, 1]]


    Arguments:
        input_array {np.ndarray} -- An input array of shape (n_samples, n_features).
            Any zeros will get imputed.
        n_neighbors {int} -- Number of neighbors to use for prediction.

        distance_measure {str} -- Which distance measure to use. Can be one of
            'euclidean', 'manhattan', or 'cosine'. This is the distance measure
            that will be used to compare features to produce labels.

        aggregator {str} -- How to aggregate a label across the `n_neighbors` nearest
            neighbors. Can be one of 'mode', 'mean', or 'median'.
    """
    raise NotImplementedError()