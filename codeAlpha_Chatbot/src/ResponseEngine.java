public class ResponseEngine {
    private IntentTrainer trainer;

    public ResponseEngine() {
        trainer = new IntentTrainer();
    }

    public String generateResponse(String input) {
        String intent = trainer.detectIntent(input.toLowerCase());

        switch (intent) {
            case "greeting": return "Hey there! 👋 What can I help you with?";
            case "faq": return "I'm here to answer your Java-related questions!";
            case "farewell": return "Goodbye! Catch you later 👋";
            default: return "Hmm, I didn't understand that. Can you rephrase?";
        }
    }
}
