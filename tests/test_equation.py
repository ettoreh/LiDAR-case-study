"""Module to test the equation file."""
import numpy as np

import wire_detect.equation as eq


def test_plan():
    assert eq.plan(1, 2, 3) == 5


def test_catenary2d():
    assert eq.catenary2d(1, 2, 3, 4) == 3.1256523995182928


def test_catenary3d():
    assert eq.catenary3d(1, 2, 3, 4, 5, 6) == 4.15283476851212


def test_rotate():
    assert eq.rotate(1, 2, 3) == [0.9665293241812118, 2.016388123724649]


def test_rmse():
    assert eq.rmse(
        np.array([-1.8315895449468216, -1.8301816526460877]),
        np.array(
            [-1.8302488415643627, 1.826984999062111])) == 2.586007513122508
