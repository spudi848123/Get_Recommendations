# Assumptions: 
# 1) Ignore nulls when reading the file
# 2) The tests may run on python 3 only
import collections, csv 
import os, sys
from fletch_logger import logger

class FieldRecommend(object):
    """load fname as a CSV into a data structure for get_recommendations"""
    def __init__(self, fname):
        # Initiate a dictionary to contain the data from the field_recommendations.csv. 
        # The first row elements are the keys. A list of remaining elements in the csv are the values for each corresponding key
        # For ex. dict[column1_heading]=[column1_value1, column1_value2, column1_value3.....]
        FRLogger = logger('field_recommendations_')
        out = {}
        with open(fname, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            FRLogger.log_it("Read the csv file into a dictionary")
            # Collect the header row names into a list and remove blanks or null header names
            fieldnames = [i for i in reader.fieldnames if i]
            FRLogger.log_it("Collect the header names")
            # Iterate through the rows in the csv and exclude nulls or blanks in the column values
            FRLogger.log_it("Iterate through the rows in the csv and exclude nulls or blanks in the column values")
            for row in reader:
                for fieldname in fieldnames:
                    if fieldname in out and row[fieldname]:
                        out[fieldname].append(row[fieldname])
                    elif row[fieldname]:
                        out[fieldname]=[row[fieldname]]
    
        self.out = out
        self.fieldnames = fieldnames
    
    def get_recommendations(self, field, value):
        # return a list of recommendations for field
        # where value has been substituted for "[value]" in each recommendation
        # example: get_recommendations("Authentication.dest", "127.0.0.1")
        # the first element in the list should be "Logins from host 127.0.0.1 by action"
        res = list(map(lambda recmdtns: str.replace(recmdtns, "[value]", value), self.out[field]))
        return res

    def get_fieldnames(self):
        # Return a list of header names or field names
        fieldnames = self.fieldnames
        return fieldnames
