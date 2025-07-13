from preprocess import load_data
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import pickle

X_train, X_test, y_train, y_test = load_data("data/medical_data.csv", "target")

rf = RandomForestClassifier()
xgb = XGBClassifier()

rf.fit(X_train, y_train)
xgb.fit(X_train, y_train)

pickle.dump(rf, open("rf_model.pkl", "wb"))
pickle.dump(xgb, open("xgb_model.pkl", "wb"))
print("✅ Models trained and saved.")
