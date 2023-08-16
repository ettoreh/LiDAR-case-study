import pandas as pd
import numpy as np

from scipy.spatial import distance_matrix
from sklearn.metrics import silhouette_score
from sklearn.cluster import DBSCAN, HDBSCAN, OPTICS


def get_labels(df, model="DBSCAN", eps=0.67):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        model (str, optional): _description_. Defaults to "DBSCAN".
        eps (float, optional): _description_. Defaults to 0.67.

    Returns:
        list: _description_
    """
    models = {
        "DBSCAN": DBSCAN(eps=eps),
        "HDBSCAN": HDBSCAN(),
        "OPTICS": OPTICS(min_samples=2)
    }

    clustering = models[model].fit(df)
    return clustering.labels_


def get_eps(df):
    """_summary_

    Args:
        df (pd.DataFrame): _description_

    Returns:
        float: _description_
    """
    test = pd.DataFrame(
        distance_matrix(df.values, df.values)).describe().transpose()
    return (test["75%"] / test["max"]).mean()


def get_eps_by_iteration(df):
    """_summary_

    Args:
        df (pd.DataFrame): _description_

    Returns:
        float: _description_
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
