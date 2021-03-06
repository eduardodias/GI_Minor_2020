##############################################################################################
# This is the auxiliary file for the practical assignment to learn python for API´s.          #
# Prepared by the Spatial Information Laboratory - Vrije Universiteit Amsterdam               #
# Simeon Nedkov, Chris Lucas, Maurice de Kleijn, Devi Brands                                  #
###############################################################################################

# In this practical assignment we want you to create a csv file containing the locations of every station
# For this practical assignment you need to use a couple of modules. Most of them have already appeared in the exercises.
# A couple of them are new and will be introduced when you need to use them.

import requests
import datetime
import pandas as pd


# STEP 1: As first step we want you to start a pandas DataFrame
# REMOVE THE HASHTAG IN THE NEXT LINE AND FINISH THE LINE
#df = 



# STEP 2: Now start a list to save each found station number to
# Write your code below:


# STEP 3: To retrieve data from all stations we need to get all the station numbers.
# In the API documentation (https://api-docs.luchtmeetnet.nl/#intro) find the URL to retrieve station numbers.
# Check how many pages there are and create a loop which goes from 1 to the total number of pages.
# Inside the loop retrieve the stations data of that page.
# Loop over that data.
# Save the station numbers to the earlier created list.
# Write your code below:





# STEP 4 Now save the list in a column of the DataFrame
# Write your code below:



# STEP 5: Now that we have a list of all stations we want you to add the station coordinates to it. First start the list. 
# Write your code below:

# Next you need to look in the API documentation for the url to retrieve information of a station.
# Loop over all station numbers found previously and use the url to retrieve information of each station.
# Look in the data of a station where to find the coordinates.
# Save each station's coordinates.
# note: the coordinates returned by the API are in the wrong order (at least for the shapely Point class which we will use later)
# You can reverse a list as such:  some_list[::-1]
# Write your code below:

# Now save the coordinate list to a column in the DataFrame
# Write your code below:

################################################################################################ 
## At this point this version of the practical assignment differs from the initial assignment ##
################################################################################################ 
# Step 6 Save the DataFrame containing the station numbers and coordiates to a csv
# Look at https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html
# REMOVE THE HASHTAG IN THE NEXT LINE AND FINISH THE LINE
# df.to_csv('stations.csv')

# In the csv your coordinates are showed in one field. In order to split these there are multiple options. You can either code this by using split https://www.w3schools.com/python/python_strings.asp
# which should obviously be done before Step 6. Another option is to load in into Excel and use LEFT and RIGHT statements to copy the data into a new collumn, after which you add the new file to your GIS.
