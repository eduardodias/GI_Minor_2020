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




https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write









