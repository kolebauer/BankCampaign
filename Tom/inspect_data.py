import pandas as pd

campaign = pd.read_csv("bank.csv")


print("Here is the head \n", campaign.head())

print("Here is the describe \n", campaign.describe())

print("Here is the y value count", campaign['y'].value_counts())

