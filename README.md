# Data-Wrangling
Data Wrangling using Python

This repository contains Python code that performs data-wrangling applications using pandas, numpy and matplotlib.

The input data is formatted in some number of horizontally-repeating blocks such that the data in any column c corresponds to the data in column c mod 156.

The output csv file has 256 columns, and now is formatted to be just one table or dataset.

I have written two different pieces of code that will solve this problem.  Both read and write the csv files into and from a pandas dataframe. The first piece of code, however, uses list data structures to restructure the data, and the second uses numpy arrays which is more efficient.
