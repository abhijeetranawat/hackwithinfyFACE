import pandas as pd
data = pd.read_csv("C:/Users/abhijeet/Desktop/OrderList.csv")
# print(data)


# col=[]
# for cl in data.columns:
#     col.append(cl)
# print(col)


#data.fillna("NaN")

# print(data.tail(10).isna())

data.rename(columns={'Total Sale $': 'Sale'})


data.dropna()

print(data)