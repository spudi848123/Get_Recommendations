"""Import the field recommendations class"""
import field_recommend as FR
from fletch_logger import logger

# Assumed the values that need to be substituted are passed as a list. 
Values = ["127.0.0.1","127.0.0.1","r624340"]
def main():
    # Create an object with the FieldRecommend class
    FRLogger.log_it(f'Reading the file')
    FROBJ = FR.FieldRecommend('field_recommendations.csv')
    # Get the field names of the recommendations csv
    FR_FIELDNAMES=FROBJ.get_fieldnames()
    FRLogger.log_it("Iterating through the header names to get recommendations and "\
        "printing the result but not logging the actual data")
    for FN in FR_FIELDNAMES:
        FRLISTNAME = FN
        # Assuming the number of values correspond to the number of fieldnames to get the recommendations
        FRLISTNAME = FROBJ.get_recommendations(FN, Values[FR_FIELDNAMES.index(FN)])
        print("===========================================")
        print(f"{FN} values: {FRLISTNAME}")

FRLogger = logger()
try:
    if __name__ == '__main__':
        main()
except Exception as err:
    FRLogger.log_it(f"Error: {err}")
    raise