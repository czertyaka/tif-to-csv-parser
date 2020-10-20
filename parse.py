#!/usr/bin/python3

import rasterio
import csv

# running resample script
import resample

print('Running parsing script...')

# open source file and read data
ds = rasterio.open('rsmpld_ozersk_elevation.tif')
band1 = ds.read(1)

# parse to csv
with open('landscape.csv', 'w', newline='') as csvfile:

    wrtr = csv.writer(csvfile, delimiter = ';',
                      quotechar = '\"', quoting = csv.QUOTE_ALL)
    wrtr.writerow(['Longitude', 'Latitude', 'Elevation', 'Landscape type'])

    for i in range(ds.height):
        for j in range(ds.width):
            lat, lon = ds.xy(i, j)
            elev = band1[i][j]
            wrtr.writerow([lon, lat, elev, ''])

print('Parsing is done.')
quit()