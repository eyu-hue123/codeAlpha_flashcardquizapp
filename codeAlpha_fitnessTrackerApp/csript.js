const form = document.getElementById("fitnessForm");
const stepsSummary = document.getElementById("stepsSummary");
const caloriesSummary = document.getElementById("caloriesSummary");
const workoutSummary = document.getElementById("workoutSummary");

let fitnessData = JSON.parse(localStorage.getItem("fitnessData")) || {
  steps: 0,
  calories: 0,
  workout: 0
};

function updateSummary() {
  stepsSummary.textContent = Steps: ${fitnessData.steps};
  caloriesSummary.textContent = Calories: ${fitnessData.calories};
  workoutSummary.textContent = Workout Time: ${fitnessData.workout} min;
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  
  const steps = parseInt(document.getElementById("steps").value);
  const calories = parseInt(document.getElementById("calories").value);
  const workout = parseInt(document.getElementById("workout").value);

  fitnessData.steps += steps;
  fitnessData.calories += calories;
  fitnessData.workout += workout;

  localStorage.setItem("fitnessData", JSON.stringify(fitnessData));
  updateSummary();

  form.reset();
});

updateSummary();