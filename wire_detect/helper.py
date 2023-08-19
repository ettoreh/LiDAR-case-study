"""This module provides functions to get labels and eps value."""
import pandas as pd
import numpy as np

from scipy.spatial import distance_matrix
from sklearn.metrics import silhouette_score
from sklearn.cluster import DBSCAN, HDBSCAN, OPTICS


def get_labels(df, model="DBSCAN", eps=0.67):
    """
    Execute one clustering model to determine point labels.

    Args:
        df (pd.DataFrame): point cloud dataset
        model (str, optional): ml model used for clustering. Defaults to
        "DBSCAN".
        eps (float, optional): ml model parameter. Defaults to 0.67.

    Returns:
        list: label of every point of the dataset
    """
    models = {
        "DBSCAN": DBSCAN(eps=eps),
        "HDBSCAN": HDBSCAN(),
        "OPTICS": OPTICS(min_samples=2)
    }

    clustering = models[model].fit(df)
    return clustering.labels_


def get_eps(df):
    """
    Use dataset info to determine a value of eps.

    Args:
        df (pd.DataFrame): point cloud dataset

    Returns:
        float: estimated eps value
    """
    test = pd.DataFrame(
        distance_matrix(df.values, df.values)).describe().transpose()
    return (test["75%"] / test["max"]).mean()


def get_eps_by_iteration(df):
    """
    Iterate on eps value and calculate silouhette score to find the best eps.

    Args:
        df (pd.DataFrame): point cloud dataset

    Returns:
        float: estimated optimal eps value
    """
    eps = {}
    for i in np.linspace(0.1, 1.5, 15):
        try:
            clustering = DBSCAN(eps=i).fit(df)
            clustering.labels_
            score = silhouette_score(df, clustering.labels_)
            eps[round(i, 3)] = score
        except Exception:
            pass
    return min(eps, key=eps.get)
