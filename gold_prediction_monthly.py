
import pandas as pd

df = pd.read_csv("/Users/selimpolat/Desktop/monthly.csv")

X = df.drop(columns="Price")
y = df["Price"].astype(int)

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X,y)

prediction = model.predict([[200706]])
print(prediction)
