import numpy as np
import pandas as pd
# Read the data. Data is already loaded in the variable `path` use the `delimeter = ';'`.
df = pd.read_csv(path, delimiter=';')
print(df.head(20))

# Replace the `unknown` values with the `Nan` and check the value count of missing values and drop the missing rows
df = df.replace('unknown', np.nan)

print(df.isnull().sum())  # Check null values

df.dropna(inplace=True)
print(df.isnull().sum())  # After null rows dropped

# Replace the column name from `loan` to `previous_loan_status` and `y` to `loan_status` 
df.rename(columns={'loan':'previous_loan_status', 'y':'loan_status'}, inplace=True)
print(df.head())

# Find out the information of the `job` column.

# How many different variants or types of job are there?
print(df['job'].nunique())    # count or number of unique

#Total different types of job
print(df['job'].unique())      # will display unique values

# Counts for different types of `job`
print(df['job'].value_counts()) # display unique values with respective counts

# Check the `loan_status`  approval rate by `job`
print(df.groupby('job')['loan_status'].value_counts(normalize=True)) 


# Check the percentage of loan approved by `education`
print(df[df['loan_status']=='yes']['education'].value_counts(normalize=True)) 

# Check the percentage of loan approved by `previous loan status`
print(df[df['loan_status']=='yes']['previous_loan_status'].value_counts(normalize=True)) 

# Create a pivot table between `loan_status` and `marital ` with values form `age`
table = df.pivot_table(values='age', index='marital', columns=['loan_status'])
print(table) 

# Loan status based on marital status whose status is married
print(df[df['marital']== 'married']['loan_status'].value_counts())

#Create a  Dataframes 
branch_1 = { 'customer_id' : ['101', '102', '103', '104'],
             'first_name' : ['Ayushi', 'Sudevi', 'Piyali', 'Saiesha'],
             'last_name' : ['Patra', 'Sau', 'Pal', 'Panda']}


branch_2 = { 'customer_id' : ['106', '107', '108', '109'],
             'first_name' : ['Anupam', 'Animesh', 'Sourav', 'Anshuman'],
             'last_name' : ['Panigrahi', 'Jaadav', 'Pal', 'Panda']}

# Create a dataframe `df_branch_1` where keys are `'customer_id','first_name','last_name'` you can take any value 
df_branch_1 = pd.DataFrame(branch_1, columns=['customer_id', 'first_name', 'last_name'])
print(df_branch_1) 

# Create a dataframe `df_branch_2` where keys are `'customer_id','first_name','last_name'` you can take any value
df_branch_2 = pd.DataFrame(branch_2, columns=['customer_id', 'first_name', 'last_name'])
print(df_branch_2) 

# Create a dataframe `df_credit_score` where keys are `'customer_id','score'` you can take any value
credit_score = {
        'customer_id': ['101', '102', '103', '104', '105', '107', '108', '109', '110', '111'],
        'score': [513, 675, 165, 961, 1080, 1654, 415, 900, 610, 1116]}
df_credit_score = pd.DataFrame(credit_score, columns = ['customer_id','score'])
print(df_credit_score)

# Concatenate the dataframe `df_branch_1` and `df_branch_2` along the rows
df_new = pd.concat([df_branch_1, df_branch_2])
print(df_new)

# Merge two dataframes `df_new` and `df_credit_score` with both the left and right dataframes using the `customer_id` key
print(pd.merge(df_new, df_credit_score, left_on='customer_id', right_on='customer_id'))


