# Hawaiian Climate Analysis

![hawaii.jpg](SurfsUp/images/hawaii.jpg)

## Overview
This analysis is a climate analysis for Hawaii for those who are planning a vacation. This overview section will explain where to find all files that were used to conduct this analysis. All files are found within the SurfsUp folder. This folder contains a resources folder, an images folder, app.py, and climate.ipynb. The data folder will be broken down in the data section of this README. The images folder contains images used in this README. app.py is an app python file that is used to store the data. climate.ipynb is the main file for this analysis.

## Data 
Found within the Surfsup folder, there is a folder titled *resources*. Within this folder, there are two csv files and a sqlite file that are used in this analysis.

<ins>hawaii_measurements:<ins/>

The data in this file consists of the following variables:

* The station code (station).

* The date (date) ranging from the years 2010-2017.

* The precipitation in inches for that day (prcp).

* The tobs (tobs) which record the maximum temperature for that day.

<ins>hawaii_stations:<ins/>

The data in this file consists of the following variables:

* The station code (station).

* The name of each station (name)

* The location of each station split between latitude, longitude, and elevation (latitude), (longitude), (elevation). 

<ins>hawaii.sqlite<ins/>

This file is an sqlite file that was used to create tables of the previously mentioned csv files, this file will be used more in the analysis. 

## Analysis 
This analysis is split into two sections:

* Precipitation Analysis

* Staion Analysis

<ins>Precipitation Analysis:<ins/>

1. Find the most recent date in the dataset.

2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

3. Select only the "date" and "prcp" values.

4. Load the query results into a Pandas DataFrame. Explicitly set the column names.

5. Sort the DataFrame values by "date".

6. Plot the results by using the DataFrame plot method

7. Use Pandas to print the summary statistics for the precipitation data.

This plot and summary statistics can be found in climate.ipynb

<ins>Stations Analysis:<ins/>

1. Design a query to calculate the total number of stations in the dataset.

2. Design a query to find the most-active stations (that is, the stations that have the most rows).

3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

4. Design a query to get the previous 12 months of temperature observation (TOBS) data.

The histogram for the station analysis can be found in climate.ipynb

## App

The python app consists of 5 directories:

* precipitation

* stations

* tobs

* start

* start/end

The precipitation directory consists of a json file of the value of prcp and the date of that value

The station directory consists of a json file of the station id, station code, station name, and station location (lat, lon, and elevation).

The tobs directory consists of a json file of the date, and the tobs value of that date.

The start directory calculates a TMIN, TMAX, and TAVG depending on a specified start date.

The start/end directory calculates a TMIN, TMAX, and TAVG depending on a specified start and end date.

**For the final two directories, the start and end dates must be specified within the app code, otherwise the json file will return null for all values.**