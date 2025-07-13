import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ChatBot bot = new ChatBot();
        Scanner scanner = new Scanner(System.in);
        System.out.println("🤖 ChatBot is online. Type 'exit' to quit.");

        while (true) {
            System.out.print("You: ");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("exit")) {
                System.out.println("Bot: " + bot.reply("bye"));
                break;
            }

            System.out.println("Bot: " + bot.reply(input));
        }
    }
}
