let display = document.getElementById('display');
function press(val) {
  display.value += val;
}
function calculate() {
  try {
    display.value = eval(display.value);
  } catch (e) {
    alert('Invalid Expression');
  }
}
function clearDisplay() {
  display.value = '';
}
