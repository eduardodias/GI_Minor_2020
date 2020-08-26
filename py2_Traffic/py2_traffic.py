###############################################################################################
# This is the auxiliary file for the practical assignment to learn python for API´s.          #
# Prepared by the Spatial Information Laboratory - Vrije Universiteit Amsterdam               #
# Simeon Nedkov, Chris Lucas, Maurice de Kleijn, Devi Brands                                  #
###############################################################################################

# For this assignment we do not provide as much hints compared to the previous ones. Now it is foremost up to you.
# It is your task to create a script that generates a shapefile with information about traffic
# from the excelsheet you downloaded for april 2019 (15/04 - 19/04) and april 2020 (13/04 - 17/04) from https://dexter.ndwcloud.nu/opendata
# the shapefile should contain the following fields:
# ID 	X_coord 	Y_coord 	vehicles_2019 	vehicles_2020

# to create this file you will need the following modules 
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Consult the documentation of these libraries in order to write your code.

# The first step is to extract the data from the excelsheet(s) into a dataframe
# Next you will need to create geometries from the coordinates 
# Finally you will need to export it to a shape file (have a look at the luchtmeetnet exercises and the first pratical assignment)
