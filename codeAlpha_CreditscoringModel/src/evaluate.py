import pickle
from preprocess import prepare_data
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

X_train, X_test, y_train, y_test = prepare_data("data/credit_data.csv")

lr = pickle.load(open("logistic_model.pkl", "rb"))
rf = pickle.load(open("rf_model.pkl", "rb"))

def evaluate(model, name):
    y_pred = model.predict(X_test)
    print(f"\n📍 {name} Evaluation:")
    print(classification_report(y_test, y_pred))
    print(f"ROC-AUC: {roc_auc_score(y_test, model.predict_proba(X_test)[:,1])}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")

evaluate(lr, "Logistic Regression")
evaluate(rf, "Random Forest")
