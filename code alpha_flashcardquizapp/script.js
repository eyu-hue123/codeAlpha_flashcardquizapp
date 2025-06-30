let flashcards = [
  { question: "What is HTML?", answer: "HyperText Markup Language" },
  { question: "What is CSS?", answer: "Cascading Style Sheets" },
  { question: "What is JavaScript?", answer: "Programming language for the web" }
];

let currentIndex = 0;
let showingAnswer = false;

const cardText = document.getElementById('cardText');
const toggleBtn = document.getElementById('toggleAnswer');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const addBtn = document.getElementById('addBtn');
const editBtn = document.getElementById('editBtn');
const deleteBtn = document.getElementById('deleteBtn');

function showCard() {
  const card = flashcards[currentIndex];
  cardText.textContent = showingAnswer ? card.answer : card.question;
  toggleBtn.textContent = showingAnswer ? "Show Question" : "Show Answer";
}

toggleBtn.onclick = () => {
  showingAnswer = !showingAnswer;
  showCard();
};

prevBtn.onclick = () => {
  if (currentIndex > 0) {
    currentIndex--;
    showingAnswer = false;
    showCard();
  }
};

nextBtn.onclick = () => {
  if (currentIndex < flashcards.length - 1) {
    currentIndex++;
    showingAnswer = false;
    showCard();
  }
};

addBtn.onclick = () => {
  const q = document.getElementById('questionInput').value;
  const a = document.getElementById('answerInput').value;
  if (q && a) {
    flashcards.push({ question: q, answer: a });
    currentIndex = flashcards.length - 1;
    showingAnswer = false;
    showCard();
  }
};

editBtn.onclick = () => {
  const q = document.getElementById('questionInput').value;
  const a = document.getElementById('answerInput').value;
  if (q && a) {
    flashcards[currentIndex] = { question: q, answer: a };
    showingAnswer = false;
    showCard();
  }
};

deleteBtn.onclick = () => {
  flashcards.splice(currentIndex, 1);
  if (currentIndex >= flashcards.length) currentIndex = flashcards.length - 1;
  showingAnswer = false;
  showCard();
};

showCard();