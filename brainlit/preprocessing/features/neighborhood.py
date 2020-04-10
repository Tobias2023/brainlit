import numpy as np
import brainlit
from brainlit.preprocessing import preprocess, image_process
from scipy import ndimage as ndi
from pathlib import Path
import pandas as pd
from itertools import product

from .base import BaseFeatures


class NeighborhoodFeatures(BaseFeatures):
    """
    Computes features based off neighborhood properties.
    """

    def __init__(self, url, size=[1, 1, 1], offset=[15, 15, 15]):
        super().__init__(url=url, size=size, offset=offset)

    def _convert_to_features(self, img, include_neighborhood=None):
        """
        Computes features from image data by flattening the image.

        Parameters
        ----------
        img : ndarray
            Image data.

        include_neighborhood : boolean
            Argument is ignored.

        Returns
        -------
        features : dict
            Feature data generated by flattening the image.
        """
        return dict(enumerate(img.flatten()))
