#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_wkt_multiline.py
Description:   This code create a wkt multi lines from points
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [50, 51, 52, 53]
longitudes = [100, 110, 120, 130]
elevation = 0

#Create multilines
multi_lines = ogr.Geometry(ogr.wkbMultiLineString)

#Create first line
line_1 = ogr.Geometry(ogr.wkbLineString)
line_1.AddPoint(longitudes[0], latitudes[0], elevation)
line_1.AddPoint(longitudes[1], latitudes[1], elevation)
multi_lines.AddGeometry(line_1)

#Create second line
line_2 = ogr.Geometry(ogr.wkbLineString)
line_2.AddPoint(longitudes[2], latitudes[2], elevation)
line_2.AddPoint(longitudes[3], latitudes[3], elevation)
multi_lines.AddGeometry(line_2)

multi_lines.ExportToWkt()
print multi_lines
