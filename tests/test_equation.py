"""Module to test the equation file."""
import numpy as np

import wire_detect.equation as eq


def test_plan():
    assert eq.plan(1, 2, 3) == 5


def test_catenary2d():
    assert np.round(eq.catenary2d(1, 2, 3, 4), 6) == 3.125652


def test_catenary3d():
    assert np.round(eq.catenary3d(1, 2, 3, 4, 5, 6), 6) == 4.152835


def test_rotate():
    x, y = eq.rotate(1, 2, 3) 
    assert np.round(x, 6) == 0.966529
    assert np.round(y, 6) == 2.016388


def test_rmse():
    assert np.round(eq.rmse(
        np.array([-1.8315895449468216, -1.8301816526460877]),
        np.array(
            [-1.8302488415643627, 1.826984999062111])), 6) == 2.586008
