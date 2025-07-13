from preprocess import prepare_data
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pickle

X_train, X_test, y_train, y_test = prepare_data("data/credit_data.csv")

lr = LogisticRegression(max_iter=1000)
rf = RandomForestClassifier(n_estimators=100)

lr.fit(X_train, y_train)
rf.fit(X_train, y_train)

pickle.dump(lr, open("logistic_model.pkl", "wb"))
pickle.dump(rf, open("rf_model.pkl", "wb"))

print("✅ Models trained and saved!")
