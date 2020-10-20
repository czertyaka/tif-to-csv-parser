#!/usr/bin/python3

import rasterio
import csv

ds = rasterio.open('ozersk_elevation.tif')
band1 = ds.read(1)

with open('landscape.csv', 'w', newline='') as csvfile:
    wrtr = csv.writer(csvfile, delimiter = ';',
                      quotechar = '\"', quoting = csv.QUOTE_ALL)
    wrtr.writerow(['Longitude', 'Latitude', 'Elevation', 'Landscape type'])

    for i in range(ds.height):
        for j in range(1, ds.width, 2):
            lat, lon = ds.xy(i, j)
            elev = band1[i][j]
            wrtr.writerow([lon, lat, elev, ''])