

import dataDescription as dd

import pandas as pd

from sklearn import linear_model
from sklearn.preprocessing import normalize


# function returns model of Linear Regression with multiple features
def get_model(data):
    reg = linear_model.LinearRegression()
    x_train = data.loc[:, data.columns != 'SalePrice']
    x_train = normalize(x_train)
    y_train = data['SalePrice']
    reg.fit(x_train, y_train)
    return reg


# function returns predicted sales
def predict_output(reg, x_test):
    x_test = normalize(x_test)
    prediction = reg.predict(x_test)
    print(prediction)
    return prediction

# get predictions and save it to the datafram
def main():
    df_train, id_col_train = dd.get_train_dataframe() # train dataset
    df_to_predict, id_col_predict = dd.get_test_dataframe() # dataset to predict results
    reg = get_model(df_train)
    prediction = predict_output(reg, df_to_predict)

    df_out = pd.DataFrame(columns=['Id', 'SalePrice'])
    df_out['Id'] = id_col_predict['Id']
    df_out['SalePrice'] = prediction
    return df_out

df_out = main()
df_out.to_csv("submission_norm.csv", index=False)