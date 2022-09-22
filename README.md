# Get Recommendations
## Description
Given a CSV file with a multiple fields, return a list of recommendations for a each field and it's associated recommended value.
For example: get_recommendations("Authentication.dest", "127.0.0.1") the first element in the list should be "Logins from host 127.0.0.1 by action"

## Assumptions made: 
1) The result can be filtered of redundant elements in the list by using a *set*. I have created a list since the problem statement mentions a list should be returned 
2) "value" is the recommendation 
3) Filter out nulls when reading the csv file
4) The tests may run on python 3 only
5) Assumed the values that need to be substituted and are passed as a list
6) The number of values correspond to the number of fieldnames to get the recommendations based on the *field_recommendations.csv* 

## How to run
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

## How to scale
### As the data grows, we can scale up the job to process large data sets. Here are some options but are not limited to 
1) Use [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) to utilize parallel processing
2) Apache [Hadoop](https://aws.amazon.com/emr/details/hadoop/what-is-hadoop/#:~:text=Apache%20Hadoop%20is%20an%20open,datasets%20in%20parallel%20more%20quickly.) and Spark along with EMR 

## Questions and Concerns
Please contact me at spudi84@gmail.com for any questions or concerns
