import pandas as pd
flights=pd.read_parquet('lesson-18/homework/flights/')
print(flights.info())
