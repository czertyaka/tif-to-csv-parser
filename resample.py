#!/usr/bin/python3

import rasterio
from rasterio.enums import Resampling
import numpy

print('Running resample script...')

# open source file, read and resample
src_ds = rasterio.open('ozersk_elevation.tif')
data = src_ds.read(
    out_shape = (src_ds.count, 601, 601),
    resampling = Resampling.bilinear
)

# scale image transform
transform = src_ds.transform * src_ds.transform.scale(
    (src_ds.width / data.shape[-1]),
    (src_ds.height / data.shape[-2])
)

# open target file and write resampled data
with rasterio.Env():
    
    # getting profile to open targer file and changing it
    profile = src_ds.profile
    profile.update(
        width = 601,
        transform = transform
    )

    # open and write
    with rasterio.open('rsmpld_ozersk_elevation.tif', 'w', **profile) as trgt_ds:
        trgt_ds.write(data)

print('Resampling is done.')