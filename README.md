# Surfs_Up
Module 9: Advanced Data Storage and Retrieval (__Challenge__)

## Overview
Client needs information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

## Process
1. Create a databse connection.
2. Retrieve temperatures for the month of June and December from the __hawaii.sqlite__ database, __measurement__ table, using the __SQLAlchemy__ `.filter(extract())` method.
3. Convert monthly results into lists.
4. Convert lists to __Pandas__ `DataFrame`.
5. Then use the `DataFrame` `.describe()` method to obtain statics for each of the month.
6. Create the  analysis about our findings.

## Resources
* Data Source: hawaii.sqlite __SQLite__ database.
* Language:
  - Python 3.9.7
* Libraries:
  - Pandas
  - SQLAlchemy

* Development tools: 
  - Jupyter Notebook 6.4.6
  - Visual Code 1.62.3; just to edit README.md file.

## Results
![Months Comparison](/Resources/ComparedStatistics.png)

1. There are a total of 183 more temperature records for June than for the month Decemeber.
2. Min temperature for June is 9 degress higher than in December.
3. Max temperature for June is 2 degrees higher than in December.

## Summary

![Store Front](/Resources/StoreFront.png)

After comparing temperatures statistics for the months of June and Decemeber, we found that the area would be perfect to stablish the business, high and low temperatures differences would not limit them to have the store open thorught the entire year selling ice creams and shakes and surfing.


