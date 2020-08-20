# Practical Assignment 2 - py2 Traffic data

## Introduction

In the previous practical assignment you have learned how to get data from air measurement stations. For this practical assignment we are going to combine data about the air quality and combine is with traffcic data. We want you to look at a couple of measurement stations and see whether you can find a relationship between the number of cars and the air quality. 

##Trafic data
Information about traffic can be obtained from different sources. Many of this data is not available as open data. You will often need to sign an agreement or buy a licence. Whenever you have such an agreement you will often get a api_key which you need to include in your script and provides access to the API in the same way as Luchtmeetnet. For many of these data sources you can create a free account which offer limited but still very useful functionalities. Good platform that you could use to get traffic information from are:

 - [HERE](https://www.developer.here.com/documentation/traffic/dev_guide/topics/what-is.html) 
 - [TOMTOM](https://developer.tomtom.com/)
 - [Flitsmeister](https://www.flitsmeister.nl/fcd.html) 

And remember, these APIs have a lot of data. They have live data and historical datasets going back a couple of years. Working with these very large datasets is really considered Big Data analytics. Another thing that is interesting to notice is that the data these sources offer is obtained from the users that use their devices and apps. In some cases  such commerical parties thus know more about our traffic behaviour than the government. Interesting times, right?   

Information about traffic on the Dutch highways is available at the [National Data Warehouse for Traffic Information (NDW)](https://www.ndw.nu/en/). This data is not collected through users that use a certain app or that installed a certain sensor on their vehicle, but works the other way around. NDW data is foremost obtained through external sensors like cameras, rubber tubes or loop detectors. Like the data sources above also NDW is not fully open data. 

They do offer a very useful open data tool with which you can generate an excel sheet with the number of vehicles for certain period. 

https://dexter.ndwcloud.nu/opendata

This tool is limited to 10 stations per download, so whenever you are interested in a small area this can be very useful. The excelsheet is however not formatted in the way that you can easily use it in a GIS. For this practical assignment it is your task to convert the data into usable GIS data. Some steps could have easily been done manually as well, but imagine you would want to include multiple time series in your analysis. Not only would it be very error sensitive to manually convert all data, it would also be very labor intensive.





