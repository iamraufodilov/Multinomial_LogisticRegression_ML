# importing libraries
from sklearn import datasets
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split

# loading data
my_data = datasets.load_digits()
X = my_data.data
y = my_data.target

# splitting data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# create model
MLReg = linear_model.LogisticRegression()

# train model
MLReg.fit(X_train, y_train)

# make prediction
y_pred = MLReg.predict(X_test)

# get accuracy
my_accuracy = metrics,accuracy_score((y_test, y_pred)*100)
print("our model has accuracy around: ", my_ccuracy)