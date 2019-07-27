# --------------
import numpy as np
import pandas as pd
# Read the data. Data is already loaded in the variable `path` use the `delimeter = ';'`.
df = pd.read_csv(path, delimiter=';')
# print(df.head(20))

# Replace the `unknown` values with the `Nan` and check the value count of missing values and drop the missing rows
# print(df.isnull().values.any())
# df = df.apply({'unknown': 'Nan'}.get) 
# print(df.value_counts())
# Replace the column name from `loan` to `previous_loan_status` and `y` to `loan_status` 
df = df.rename(columns={'loan':'previous_loan_status', 'y':'loan_status'})

# Find out the information of the `job` column.
# print(df['job'].value_counts())
# Check the `loan_status`  approval rate by `job`

# Check the percentage of loan approved by `education`

# Check the percentage of loan approved by `previous loan status`

# Create a pivot table between `loan_status` and `marital ` with values form `age`

# Loan status based on marital status whose status is married

#Create a  Dataframes 

# Create a dataframe `df_branch_1` where keys are `'customer_id','first_name','last_name'` you can take any value 

# Create a dataframe `df_branch_2` where keys are `'customer_id','first_name','last_name'` you can take any value

# Create a dataframe `df_credit_score` where keys are `'customer_id','score'` you can take any value

# Concatenate the dataframe `df_branch_1` and `df_branch_2` along the rows

# Merge two dataframes `df_new` and `df_credit_score` with both the left and right dataframes using the `customer_id` key



