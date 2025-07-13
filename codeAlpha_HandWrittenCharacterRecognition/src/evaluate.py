from tensorflow.keras.models import load_model
from preprocess import load_mnist
from sklearn.metrics import classification_report

model = load_model("digit_model.h5")
x_train, y_train, x_test, y_test = load_mnist()
y_pred = model.predict(x_test).argmax(axis=1)

print(classification_report(y_test, y_pred))
