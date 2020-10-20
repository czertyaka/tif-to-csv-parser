# GeoTIFF Parser

Takes file with geospatial data in .tif format and parses it into .csv-file

## Script steps

1. Resamples data from source file to 601x601 grid and saves it in new .tif-file.
2. Parses data (longitude, latitude, band parameter) from resampled .tif-file to .csv-file.

## Warnings

Script meant for datasets with `dataset.count == 1`. For multidiband datasets it will only parse data from first band I guess.

## Depenencirs

`python3`. `rasterio`, `numpy`, `csv` python libraries