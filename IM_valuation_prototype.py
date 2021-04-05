
import pandas as pd
from sklearn import preprocessing

df = pd.read_excel("PATH")

columns = [' Model', 'Hours', 'Year', 'Gross Price', 'Currency',"encoded"]

label_encoder = preprocessing.LabelEncoder() # encodes non-numerical data into numerical values
label_encoder.fit(df[" Model"])
label_encoder.transform(df[" Model"])

df["encoded"] = label_encoder.transform(df[" Model"]) # appends a new column for the new numerical data

X = df.drop(columns=["Currency"," Model","Gross Price"])
y  = df["Gross Price"]

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X,y)

while True:

    model_input = input("please enter the model of your vehicle: ")
    index = df[df[" Model"] == model_input].index[0]
    b = df["encoded"][index]

    hours = input("please enter how many hours your vehicle has been operating: ")
    year = input("please enter the model year of your vehicle: ")

    prediction = model.predict([[hours,year,b]])
    print("the estimated value for your",model_input,"is:",prediction,"TRY")






