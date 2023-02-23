import pandas as pd
df = pd.read_csv(r'Pandas\california_housing_train.csv')

print(df.head(n=10))

print(df.shape)

print(df.dtypes)

print(df.columns)

print(df.isnull())

print(df.isnull().sum())

print(df["totalRooms"])

print(df[df["medianIncome"] < 2] ['medianHouseValue'])

print(df[(df["housingMedianAge"] < 20) & (df["medianHouseValue"] > 70000)])

print(df[df['housingMedianAge'] < 20] ['totalRooms'])

print(df["medianHouseValue"].max())

print(df['medianHouseValue'].min())

print(df[df["housingMedianAge"] < 20] ["totalRooms"])

print(df[(df["medianHouseValue"].max()) & (df["medianIncome"] == 3.1250)])

print(df[("population")].max() & (df[("medianHouseValue")].min()))




