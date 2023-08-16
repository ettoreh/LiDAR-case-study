"""Module providing a class for a wire detector."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from wire_detect.equation import plan, catenary2d, catenary3d
from wire_detect.helper import get_labels, get_eps
from wire_detect.rotation import rotate_matrix
from wire_detect.wire import Wire


colors = {
    0: "blue",
    1: "orange",
    2: "green",
    3: "red",
    4: "purple",
    5: "brown",
    6: "pink",
    7: "grey",
    8: "olive",
    9: "cyan"
}


class Detector:
    """
    Class taking a point cloud dataset in input and fin the wire located in.
    """

    def __init__(self, df, method="DBSCAN", eps=None) -> None:
        """
        Initialize the detector and locate wires.

        Args:
            df (pd.DataFrame): point cloud dataset where to find wires.
            method (str, optional): algorithm of machine learning used for the
            detection. Defaults to "BDSCAN".
            eps (float, optional): argument for the choosen method. Defaults to
            None.
        """
        self.df = df
        self.method = method
        self.eps = eps
        if self.eps is None:
            self.eps = get_eps(df)
        self.labels = None
        self.plans = None
        self.catenaries = None
        self.wires = []
        self.predictions = []
        self.find_plan_coefficient()
        self.find_catenary_coefficient()
        self.create_wire()
        self.make_prediction()

    def find_plan_coefficient(self):
        """
        Use clustering to labels the wire.

        Then, we find the plan (x, y) of those wire by curve fitting.
        Later, we will try to group same plan wire and use number of point in
        wire to do the same.
        """
        labels = get_labels(self.df, model=self.method, eps=self.eps)
        plans = []
        for label in range(max(labels)+1):
            one_wire = self.df[labels == label].copy()
            [a, b], _ = curve_fit(plan, one_wire.x, one_wire.y)
            plans.append((a, b))

        # TODO: add logic for same plan
        self.labels = labels
        self.plans = plans

    def find_catenary_coefficient(self):
        """Use curve fitting from scipy to get catenaries coeffient."""
        catenaries = []
        for label in range(max(self.labels)+1):
            one_wire = self.df[self.labels == label].copy()
            angle = np.rad2deg(np.arctan(-self.plans[label][0]))
            one_wire = rotate_matrix(one_wire, angle)
            [xo, zo, c], _ = curve_fit(catenary2d, one_wire.x, one_wire.z)
            catenaries.append((xo, zo, c))

        self.catenaries = catenaries

    def create_wire(self):
        """Create a Wire object for each one found in the dataset."""
        for label in range(max(self.labels)+1):
            a, b = self.plans[label]
            xo, zo, c = self.catenaries[label]
            wire = Wire(xo, zo, a, b, c)
            self.wires.append(wire)

    def make_prediction(self):
        """
        Generate prediction based on coefficients found.

        Usefull for plots after to visualy check the algorithm quality.
        """
        for label in range(max(self.labels)+1):
            one_wire = self.df[self.labels == label].copy()
            xx = np.linspace(one_wire.x.min(), one_wire.x.max(), num=200)
            a, b = self.plans[label]
            yy = plan(xx, a, b)
            xo, zo, c = self.catenaries[label]
            zz = catenary3d(xx, yy, xo, zo, c, a)
            prediction = pd.DataFrame(
                np.transpose([xx, yy, zz]), columns=["x", "y", "z"])
            self.predictions.append(prediction)

    def plot_dataset(self):
        """
        Plot the point cloud dataset.

        Returns:
            matplotlib.figure: a graph
        """
        fig = plt.figure(figsize=(10, 7))
        ax = plt.axes(projection='3d')
        ax.scatter(self.df.x, self.df.y, self.df.z, c='b')
        ax.set_title("Point cloud dataset", fontsize=13)
        ax.set_xlabel('x', fontsize=11)
        ax.set_ylabel('y', fontsize=11)
        ax.set_zlabel('Z', fontsize=11)
        return fig

    def plot_wires(self):
        """
        Plot wire according to the equation found.

        Returns:
            matplotlib.figure: a graph
        """
        fig = plt.figure(figsize=(10, 7))
        ax = plt.axes(projection='3d')

        for label in range(max(self.labels)+1):
            ax.plot(
                self.predictions[label].x,
                self.predictions[label].y,
                self.predictions[label].z,
                c=colors[label])

        ax.set_title("Wire on the point cloud dataset", fontsize=13)
        ax.set_xlabel('x', fontsize=11)
        ax.set_ylabel('y', fontsize=11)
        ax.set_zlabel('Z', fontsize=11)
        return fig

    def plot_both(self):
        """
        Plot dataset and wire to verify the work.

        Returns:
            matplotlib.figure: a graph
        """
        fig = plt.figure(figsize=(10, 7))
        ax = plt.axes(projection='3d')
        ax.scatter(self.df.x, self.df.y, self.df.z, c='b', alpha=0.01)

        for label in range(max(self.labels)+1):
            ax.plot(
                self.predictions[label].x,
                self.predictions[label].y,
                self.predictions[label].z,
                c=colors[label])

        ax.set_title("Wire plot", fontsize=13)
        ax.set_xlabel('x', fontsize=11)
        ax.set_ylabel('y', fontsize=11)
        ax.set_zlabel('Z', fontsize=11)
        return fig
