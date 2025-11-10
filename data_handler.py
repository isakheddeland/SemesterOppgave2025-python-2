import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def load_data(filename='data/NedborX.csv'):
    df = pd.read_csv(filename)
    ns = df['Nedbor']
    X = df[['X', 'Y', 'Month']]
    return df, X, ns

def create_poly_model(X, ns, degree=3):
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, ns)
    return model, poly, X_poly
