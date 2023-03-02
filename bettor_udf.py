#from pyspark.sql.functions import udf
#from pyspark.sql.types import StringType, DateType

def convert(x):     
    return x.replace(' ', '_')
    
def keyconverter(obj, convert):
    """
    Recursively goes through the dictionary obj and replaces keys with the convert function.
    """
    if isinstance(obj, (str, int, float)):
        return obj
    if isinstance(obj, dict):
        new = obj.__class__()
        for k, v in obj.items():
            new[convert(k)] = keyconverter(v, convert)
    elif isinstance(obj, (list, set, tuple)):
        new = obj.__class__(keyconverter(v, convert) for v in obj)
    else:
        return obj
    return new

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        fdate = start_date + timedelta(n)

# UDF for matching dict keys with db keys -- replaces spaces with underscore
#fillspace = udf(lambda x: key_converter(x, convert), StringType())

# UDF for iterating over days between a date range#
#daterange = udf(lambda y: daterange, DateType())

