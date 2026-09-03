# import csv

# with open("students.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in file:
#         print(row)


# import pandas as pd 

# df = pd.read_csv("students.csv")

# print(df)

import pandas as pd 

df1= pd.read_csv("student1.csv")
df2= pd.read_csv("student2.csv")

merged_df= pd.concat([df1,df2],ignore_index=True)

print(merged_df)

merged_df.to_csv("merged.csv",index=False)