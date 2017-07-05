
# f θ (X)= θT X, where θ is the parameter we wish to calculate and X is the column vector of features or independent variables.
import pandas as pd
import numpy as np

#you don’t need to bother about the following. It just #transforms the data from original source into matrix

Df = pd.read_csv( "../baseball.csv")
Df1 = df.head(14)

# We are just taking 6 features to calculate θ.
X = Df1[[‘RS’, ‘RA’, ‘W’, ‘OBP’,'SLG','BA']]
Y=Df1['OOBP']

#Converting X to matrix
X = np.asmatrix(X)

#taking transpose of X and assigning it to x
x= np.transpose(X)

#finding multiplication
T= x.dot(X)

#inverse of T - provided it is invertible otherwise we use pseudoinverse
inv=np.linalg.inv(T)

#calculating θ
theta=(inv.dot(X.T)).dot(Y)