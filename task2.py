import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv('housing_data.csv')

# importing the independent variables into x while excluding the dependent and unnecessary columns

x = data.drop(columns=['HouseID','Price_Lakhs'])

# now importing the dependent variable to y

y = data['Price_Lakhs']

# implementing one hot encoding to the independent data

x = pd.get_dummies(x, columns=['Location','House_Type'])

#dividing the data to train and test on

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#applying linear regression

model = LinearRegression()
model.fit(x_train,y_train)

yprediction = model.predict(x_test)

# comparing the predictions to the real values to see the accuracy of the predictions

comparison = pd.DataFrame({
    "real price": y_test.values,
    "prediction": yprediction
})

print(comparison.head())

# defining the accuraccy of the model through its r2 score

r2score = r2_score(y_test,yprediction)
print("R2 score:",r2score)

# while working i accidentally added a data leakage by writing
#"x = pd.get_dummies(data, columns=['Location','House_Type'])" in line 18
#which resulted in me getting a prefect r2 score which is fixed now