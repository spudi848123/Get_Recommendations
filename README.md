# Get Recommendations
## Description
The job returns a list recommendations for field where value has been substituted for "[value]" in each recommendation example: get_recommendations("Authentication.dest", "127.0.0.1") the first element in the list should be "Logins from host 127.0.0.1 by action"

## Assumptions made: 
1) Filter out nulls when reading the csv file
2) The tests may run on python 3 only
3) Assumed the values that need to be substituted and are passed as a list
4) The number of values correspond to the number of fieldnames to get the recommendations based on the *field_recommendations.csv*


## Getting Started
1) Clone the repository
2) Browse to the root of the project
3) Ensure that the following csv files are in the root directory
    - csv file with the recommendations data
    - mock csv file for the unit tests *mock_rec.csv*
4) Run the unit tests
    > python -m unittest tests.field_recommend_test
5) Run the job using the below command
    > python .\src\get_recommendations.py
6) This will create a log file in the root directory with the name `field_recommendations_*date_time*.log`