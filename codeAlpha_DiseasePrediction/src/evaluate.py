import pickle
from preprocess import load_data
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

X_train, X_test, y_train, y_test = load_data("data/medical_data.csv", "target")

rf = pickle.load(open("rf_model.pkl", "rb"))
xgb = pickle.load(open("xgb_model.pkl", "rb"))

def evaluate(model, name):
    y_pred = model.predict(X_test)
    print(f"\n📊 {name} Results:")
    print(classification_report(y_test, y_pred))
    print(f"ROC-AUC: {roc_auc_score(y_test, model.predict_proba(X_test)[:,1])}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")

evaluate(rf, "Random Forest")
evaluate(xgb, "XGBoost")
