import java.util.*;

public class TradingApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Stock> stocks = Arrays.asList(
            new Stock("AAPL", 150),
            new Stock("GOOGL", 125),
            new Stock("AMZN", 100)
        );

        User user = new User("Bereket", 1000);
        List<Transaction> history = new ArrayList<>();

        while (true) {
            System.out.println("\n📍 Stock Trading Menu");
            System.out.println("1. View Stocks");
            System.out.println("2. Buy Stock");
            System.out.println("3. Sell Stock");
            System.out.println("4. View Portfolio");
            System.out.println("5. View Transaction History");
            System.out.println("0. Exit");
            System.out.print("Choose option: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    stocks.forEach(s -> System.out.println(s));
                    break;
                case 2:
                    System.out.print("Enter symbol to buy: ");
                    String buySymbol = sc.next();
                    System.out.print("Qty: ");
                    int buyQty = sc.nextInt();
                    for (Stock s : stocks) {
                        if (s.symbol.equalsIgnoreCase(buySymbol)) {
                            if (user.buyStock(s, buyQty)) {
                                history.add(new Transaction(s.symbol, buyQty, true));
                                System.out.println("✅ Bought!");
                            } else {
                                System.out.println("❌ Insufficient funds.");
                            }
                        }
                    }
                    break;
                case 3:
                    System.out.print("Enter symbol to sell: ");
                    String sellSymbol = sc.next();
                    System.out.print("Qty: ");
                    int sellQty = sc.nextInt();
                    for (Stock s : stocks) {
                        if (s.symbol.equalsIgnoreCase(sellSymbol)) {
                            if (user.sellStock(s, sellQty)) {
                                history.add(new Transaction(s.symbol, sellQty, false));
                                System.out.println("✅ Sold!");
                            } else {
                                System.out.println("❌ Not enough shares.");
                            }
                        }
                    }
                    break;
                case 4:
                    user.showPortfolio();
                    break;
                case 5:
                    System.out.println("📜 Transactions:");
                    history.forEach(t -> System.out.println(t));
                    break;
                case 0:
                    System.out.println("👋 Goodbye!");
                    return;
                default:
                    System.out.println("Invalid option.");
            }
        }
    }
}
