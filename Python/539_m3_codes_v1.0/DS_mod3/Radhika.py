import numpy as np
import seaborn as sns
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import cross_val_predict
from sklearn.cross_validation import train_test_split

import linear_regression
lr = linear_regression
import warnings
file ='C:\\Users\\adhyapakss\\PycharmProjects\\DS_mod3\\boston-dataset.csv'
bos = pd.read_csv(file)
bos1 = pd.DataFrame(bos)
prices = bos1['MV']
features = bos1.drop("MV", axis=1)
minimum_price = prices.min()

'''y= bos1
predicted=cross_val_predict(lr,bos1.data,y,cv=10)
ax=plt.subplot()
ax.scatter(y,predicted,edgecolors=(0,0,0))
ax.plot([y.min(),y.max()],[y.min(),y.max()], 'k--',lw=4)
ax.set_xlabel('measured')
ax.set_ylabel('predicted')
plt.show()'''

#print(bos1)
#print(bos1.head(6))
boston = bos1.values
x = boston[:,5]
y = boston[:,4]
plt.scatter(x,y)
plt.ylabel("Zone(Price)")
plt.xlabel("CrimeRate")
plt.show()
boston.keys()
'''correlations = bos1.corr()

sns.heatmap(correlations,cmap='coolwarm', vmin=-1, vmax= 1, annot=True,)
plt.tight_layout()
plt.show()'''
'''print("target =", ",".join(str(k) for k in bos1.target[0:5]),"...", ",".join(str(k) for k in bos1.target[-5:]))
bos1.columns = bos1.feature_names
bos1.head()
bos1['PRICE']= bos1.target
bos1.head()
x = bos1.drop('PRICE', axis=1)
y = bos1['PRICE']
lm = linear_regression()
lm
assert isinstance(y, object)
lm.fit(x,y)
linear_regression(copy_x=True, fit_intercept=True, n_jobs=1, normalize=False)
print("Estimated intercept coeff: ", lm.intercept_)
print("Number of coeff:", len(lm.coef_))
print("coeffs =", lm.coef_)
lm.predict(x)[0:10]
plt.scatter(bos1.PRICE, lm.predict())

#print("Estimated intercept coeff:" lm.intercept_)'''
'''x_train, x_test, y_train, y_test = sklearn.cross_validation.train_test_split(x,y, test_size =0.33, random_state = 5)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
plt.show()'''