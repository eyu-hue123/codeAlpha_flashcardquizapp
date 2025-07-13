public class IntentTrainer {
    public String detectIntent(String input) {
        if (input.contains("hi") || input.contains("hello")) return "greeting";
        if (input.contains("how") || input.contains("what")) return "faq";
        if (input.contains("bye") || input.contains("exit")) return "farewell";
        return "unknown";
    }
}
