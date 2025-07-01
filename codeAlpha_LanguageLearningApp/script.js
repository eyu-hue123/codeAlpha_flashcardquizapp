const flashcards = [
  { word: "Hello", translation: "Hola" },
  { word: "Thank you", translation: "Gracias" },
  { word: "Yes", translation: "Sí" },
  { word: "No", translation: "No" },
  { word: "Goodbye", translation: "Adiós" }
];

let currentIndex = 0;

const wordEl = document.getElementById("word");
const translationEl = document.getElementById("translation");
const showAnswerBtn = document.getElementById("showAnswer");
const nextBtn = document.getElementById("nextBtn");

function showCard() {
  const card = flashcards[currentIndex];
  wordEl.textContent = card.word;
  translationEl.textContent = card.translation;
  translationEl.classList.add("hidden");
}

showAnswerBtn.onclick = () => {
  translationEl.classList.remove("hidden");
};

nextBtn.onclick = () => {
  currentIndex = (currentIndex + 1) % flashcards.length;
  showCard();
};

showCard();


// ---------- QUIZ Section ----------
const quizQuestion = document.getElementById("quizQuestion");
const optionsContainer = document.getElementById("options");

function loadQuiz() {
  const card = flashcards[Math.floor(Math.random() * flashcards.length)];
  quizQuestion.textContent = What is the meaning of "${card.word}"?;

  let answers = [card.translation];
  while (answers.length < 3) {
    let random = flashcards[Math.floor(Math.random() * flashcards.length)].translation;
    if (!answers.includes(random)) {
      answers.push(random);
    }
  }

  answers = shuffleArray(answers);

  optionsContainer.innerHTML = "";
  answers.forEach(answer => {
    const btn = document.createElement("button");
    btn.textContent = answer;
    btn.onclick = () => {
      if (answer === card.translation) {
        alert("Correct!");
      } else {
        alert("Try again.");
      }
      loadQuiz();
    };
    optionsContainer.appendChild(btn);
  });
}

function shuffleArray(arr) {
  return arr.sort(() => Math.random() - 0.5);
}

loadQuiz();