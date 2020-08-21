# Practical Assignment 2 - py2 Traffic data

## Introduction

In the previous practical assignment you have learned how to get data from air measurement stations. For this practical assignment we are going to combine data about the air quality with traffcic data. We want you to look at a couple of measurement stations and see whether you can find a relationship between the number of cars and the air quality. But let us first have a look at available traffic data.  

## Traffic data

Information about traffic can be obtained from different sources. Many of this data is not available as open data. You will often need to sign an agreement or buy a licence. Whenever you have such an agreement you will often get a api_key which you need to include in your script and provides access to the API in the same way as Luchtmeetnet. For many of these data sources you can create a free account which offer limited but still very useful functionalities. Good platform that you could use to get traffic information from are:

 - [HERE](https://www.developer.here.com/documentation/traffic/dev_guide/topics/what-is.html) 
 - [TOMTOM](https://developer.tomtom.com/)
 - [Flitsmeister](https://www.flitsmeister.nl/fcd.html) 

And remember, these APIs have a lot of data. They have live data and historical datasets going back a couple of years. Working with these very large datasets is really considered Big Data analytics. Another thing that is interesting to notice is that the data these sources offer is obtained from the users that use their devices and apps. In some cases  such commerical parties thus know more about our traffic behaviour than the government. Interesting times, right?   

Information about traffic on the Dutch highways is available at the [National Data Warehouse for Traffic Information (NDW)](https://www.ndw.nu/en/). This data is not collected through users that use a certain app or that installed a certain sensor on their vehicle, but works the other way around. NDW data is foremost obtained through external sensors like cameras, rubber tubes or loop detectors. Like the data sources above also NDW is not fully open data. 

They do offer a very useful open data tool with which you can generate an excel sheet with the number of vehicles for certain period. 

https://dexter.ndwcloud.nu/opendata

This tool is limited to 10 stations per download, so whenever you are interested in a small area this can be very useful. The excelsheet is however not structured in the way that you can easily use it in a GIS. For this practical assignment it is your task to convert the data into usable GIS data. Some steps could have easily been done manually as well, but imagine you would want to include multiple time series in your analysis. Not only would it be very error sensitive to manually convert all data, it would also be very labor intensive.

## Python to read and write Excel files
One of the main purposes for which you will use python is to preprocess you data before performing an analysis. A huge advantage of scripting data processing steps is that it remains transparant what you exactly did, thus reproducable by other researcher. There are multiple modules that allow you to proces (read and write) data from excel sheets. The most popular is [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html), but older alternatives like [openpyxl](https://openpyxl.readthedocs.io/en/stable/) or [xlrd](https://xlrd.readthedocs.io/en/latest/) are still useful. For this practical assignment we want you to work with [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html).

To install the `pandas` module open a Anaconda prompt (`Start Menu` -> `Anaconda` -> `Anaconda Prompt`) in administrator mode (right click -> More -> Run as administrator) and enter the following command:

    `conda install pandas`

    press `Enter` to execute it.

However, since pandas is very commonly used it is very likely you already installed it or that is was automatically installed when you installed Anaconda.


# Practical Assignment

In order to see the effect of traffic on the air quality we are going to compare the traffic and air quality measurements from April 2019 and April 2020 for the southern part of highway A10 near to the Vrije Universiteit. Since that Netherlands was in lockdown due to the COVID-19 virus in April 2020, we expect that there was less traffic which might have let to a better air quality. It is up to you to find out! 

## Traffic data
To get your data go to: https://dexter.ndwcloud.nu/opendata

For the first excelsheet we want you to fill in `15-04-2019` for `Begindatum` (startdate) and `19-04-2019` for `Einddatum` (Enddate). Select you measureng stations by clicking on `Locatieselectie aanpassen` go to `Klembord` and paste the following in `Selectie uit klembord`:

```python
RWS01_MONIBAS_0100vwb0183ra
RWS01_MONIBAS_0100vwb0199ra
RWS01_MONIBAS_0100vwc0175ra
RWS01_MONIBAS_0101hrl0160ra
RWS01_MONIBAS_0101hrl0166ra
RWS01_MONIBAS_0101hrl0175ra
RWS01_MONIBAS_0101hrl0186ra
RWS01_MONIBAS_0101hrl0205ra
RWS01_MONIBAS_0101hrr0171ra
RWS01_MONIBAS_0101hrr0209ra
```

Now click on `+Toevoegen` and confirm by clicking on `Bevestigen`. For `Naam` `2019`, fill in your email adress, check the `Ik ben geen robot` (I am not a robot) box and click at `Aanvraag starten`. Wait a bit and the download will be ready. 

Once you downloaded the 2019 sheet go to the proces a second time (you might have to refresh by pressing `F5`) but now change the `Begindatum` to `13-04-2020` and the `Einddatum` to `17-04-2020` and fill in for `Name` `2020`. 

When you open the excel sheet you will notice that the data is structured, but not in a way is can easily be intgrated into your GIS. Restructuring the data can be done manually, but is error sensitive and not easily reproducable. Since you are trained as researchers we want you to not modify the downloaded data, but instead generate a new datafile without touching the orginal data. Whenever publishing a academic report you can accompany it with your data processing scripts (which most researchers currently publish on platforms like GIThub: the platform where this practical assignment is published on as well). 

For this practical assignment we want you to create a shapefile `traffic_april_1920.shp`file with the following collumns. 

| ID | X_coord | Y_coord | vehicles_2019 | vehicles_2020 |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| RWS01_MONIBAS_0100vwb0183ra | 52.3396955| 4.8836328 |  13956.1 | 5816.5 |
| RWS01_MONIBAS_0100vwb0199ra | 52.3389098| 4.8604215 |  20715.5 | 9487.2 |
| ... | ... | ... | ... | ... |

**ID** represents the unique ID of the sensor and can be found on either the `2019.xlsx`or `2020.xlsx` excel files on sheet `overzicht` cells `B7:B16` this collumn must be stored as string / text.

**X_Coord** represents the Longitude of the sensor and can be found either the `2019.xlsx`or `2020.xlsx` excel files on sheet `overzicht` cells `D7:D16`. This collumn must be stored as float or double in order for your GIS to be recognized as number.

**Y_Coord** represents the Latitude of the sensor and can be found either the `2019.xlsx`or `2020.xlsx` excel files on sheet `overzicht` cells `E7:E16`. This collumn must be stored as float or double in order for your GIS to be recognized as number.

**vehicles_2019** are the total number of cars that passed this sensor for the predefined period. These figures can be found in `2019.xlsx` on the `intensiteit` sheet in the different cells that provide `Totaal` under the collumn `intensiteit`. For sensor `RWS01_MONIBAS_0100vwb0183ra` this is cell B30 fo sensor `RWS01_MONIBAS_0100vwb0199ra` this is `B67` for `RWS01_MONIBAS_0100vwc0175ra` this is `B104` (do you see the pattern?).

**vehicles_2020** are the total number of cars that passed this sensor for the predefined period. These figures can be found in `2020.xlsx` on the `intensiteit` sheet in the different cells that provide `Totaal` under the collumn `intensiteit`. For sensor `RWS01_MONIBAS_0100vwb0183ra` this is cell `B30` fo sensor `RWS01_MONIBAS_0100vwb0199ra` this is `B67` for `RWS01_MONIBAS_0100vwc0175ra` this is `B104` (do you see the pattern?).

Not it is up to you to do this. Go through the documentation of [pandas] and in particular have a look at this [tutorial](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write) . In order to export the data as a shapefile have a look at the previous assignment and geopandas.

To help you a bit we have prepared [py2_traffic.py](URL) in which we included some tips on how to create your script. 

## Air Quality data

In order to see which stations are near to the traffic sensors we want you to add the traffic shapefile and the measurement stations from the previous practical assignment to your GIS (if you want you can also done using buffer analysis using **arcpy** or **geopandas**, however let´s take it easy for the moment). Now select the ten air quality measurement stations which are nearest to the traffic sensors and modify your script from the previous assignment to get the data for the periods in **April 2019** and **April 2020** for which you generated the traffic dataset. Make sure to now also include average measurements for all other chemical components. 

Name you this script: `py2_air_april_1920.py`. 

Create a shapefile named `air_q_april_1920.shp` containing the following table structure.

| ID_AQ | X_coord | Y_coord | PM25 | PM10 | NO | etc. | 
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| ... | ... | ... | ... | ... |... | ... |

## Comparing the Air Quality and Traffic
Now that you created two shape files we want you to compare April 2019 with April 2020. Although various statistical methods exist and obviously interpolation and distance decay functionalities should be included to analyse this in a more robust academic manner, we want you to just explore the data and compare the figures visually. Answer the following questions:

1. What do you see when you compare the air quality of April 2019 with April 2020.
2. How would you interpret these results in relation to the amount of traffic? What conclusions would you draw from your explorative analysis?
3. What other information would you require to analyse the relationship between air quality and traffic?

Save your answers in a file named `py2_answers.txt`

## Submit the following

Create a .zip file containing the following files 

- `py2_traffic.py` which contains the script with which you modify the traffic data into a useable shapefile.
- the generated shapefile `traffic_april_1920.shp`
- `py2_air_april_1920.py`
- the generated shapefile `air_q_april_1920.shp`
- `py2_answers.txt`

Submit this zip to Canvas **before the 16th of September 23:59**. 
