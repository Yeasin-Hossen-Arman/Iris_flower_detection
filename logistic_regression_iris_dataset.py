# -*- coding: utf-8 -*-
"""Logistic_Regression_iris_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lWM3XxxHQ1wXKT3ONhlGXHIrivTC2WlY

#Logistic Regression
##iris dataset
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

df.head()

df['species'].unique()

df=df[df['species'] != 'setosa']

df.head()

df['species']=df['species'].map({'versicolor':0,'virginica':1})

df.head()

#df= df.drop['species',axis =1]
#df=df.drop['species',axis = 1]

"""#split dataset into independent and dependent feature"""

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X.head()

y.head()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()

from sklearn.model_selection import GridSearchCV

parameter = {'penalty':['l1','l2','l2','elasticnet'], 'C':[1,2,3,4,5,6,8,10,20,40,50],'max_iter':[100,200,300]}

classifier_regression = GridSearchCV(classifier,param_grid= parameter,scoring='accuracy',cv=5)

classifier_regression.fit(X_train,y_train)

print(classifier_regression.best_params_)

print(classifier_regression.best_score_)

y = classifier_regression.predict(X_test)

print(y)

print(y_test)

from sklearn.metrics import accuracy_score,classification_report

score= accuracy_score(y,y_test)

print(score)

print(classification_report(y,y_test))

