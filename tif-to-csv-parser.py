#!/usr/bin/python3

import rasterio
from rasterio.enums import Resampling
import rasterio.crs
import numpy
import csv
import sys

help_str = "Usage:\n\t./tif-to-csv-parser.py <your_file>.tif <resolution>"

if len(sys.argv) > 3:
    print("Too much arguments")
    print(help)
    quit(1)

if len(sys.argv) == 1:
    print("Too few arguments")
    print(help)
    quit(1)

if str(sys.argv[1]) == "--help" or str(sys.argv[1]) == "-h":
    print(help)
    quit(0)

src_filename = str(sys.argv[1])
rsmpld_filename = "rsmpld_" + src_filename
csv_filename = src_filename.replace("tif", "csv")

resolution = int(sys.argv[2])

print('Running resampling...')

# open source file, read and resample
src_ds = rasterio.open(src_filename)
data = src_ds.read(
    out_shape = (src_ds.count, resolution, resolution),
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
        width = resolution,
        height = resolution,
        transform = transform
    )

    # open and write
    with rasterio.open(rsmpld_filename, 'w', **profile) as rsmpld_ds:
        rsmpld_ds.write(data)

print('Resampling is done.')

print('Running parsing...')

# open source file and read data
ds = rasterio.open(rsmpld_filename)
data = ds.read(1)
epsg_format = ds.crs.to_dict().get('init')

# parse to csv
with open(csv_filename, 'w', newline='') as csvfile:

    wrtr = csv.writer(csvfile, delimiter = ';',
                      quotechar = '\"', quoting = csv.QUOTE_ALL)
    wrtr.writerow(['Latitude ' + epsg_format, 'Longitude ' + epsg_format, 'Parameter'])

    for i in range(ds.height):
        for j in range(ds.width):
            lat, lon = ds.xy(i, j)
            param = data[i][j]
            wrtr.writerow([lon, lat, param])

print('Parsing is done.')
quit()