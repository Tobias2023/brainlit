import pytest
from brainlit.utils.ngl_pipeline import NeuroglancerSession
from brainlit.preprocessing.features import *
import numpy as np
import pandas as pd
from cloudvolume import CloudVolume
from cloudvolume.lib import Bbox

URL = "s3://mouse-light-viz/precomputed_volumes/brain1"


def test_neighborhood():
    nbr = neighborhood.NeighborhoodFeatures(
        url=URL, size=[1, 1, 1], offset=[15, 15, 15]
    )
    df_nbr = nbr.fit([2, 7], 5)
    assert df_nbr.shape == (20, 4)  # 5on, 5off for each swc
    assert not df_nbr.empty


def test_linear_features():
    lin = linear_features.LinearFeatures(url=URL, size=[1, 1, 1], offset=[15, 15, 15])
    df_lin = lin.fit([2, 7], 5)
    assert df_lin.shape == (20, 4)
    assert not df_lin.empty