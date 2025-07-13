public class ChatBot {
    private ResponseEngine engine;

    public ChatBot() {
        this.engine = new ResponseEngine();
    }

    public String reply(String input) {
        return engine.generateResponse(input);
    }
}
