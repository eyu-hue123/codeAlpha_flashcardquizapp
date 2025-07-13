import java.util.*;

public class User {
    String name;
    double balance;
    Map<String, Integer> portfolio;

    public User(String name, double balance) {
        this.name = name;
        this.balance = balance;
        this.portfolio = new HashMap<>();
    }

    public boolean buyStock(Stock stock, int qty) {
        double cost = stock.price * qty;
        if (balance >= cost) {
            balance -= cost;
            portfolio.put(stock.symbol, portfolio.getOrDefault(stock.symbol, 0) + qty);
            return true;
        }
        return false;
    }

    public boolean sellStock(Stock stock, int qty) {
        int owned = portfolio.getOrDefault(stock.symbol, 0);
        if (owned >= qty) {
            balance += stock.price * qty;
            portfolio.put(stock.symbol, owned - qty);
            return true;
        }
        return false;
    }

    public void showPortfolio() {
        System.out.println("📦 Portfolio for " + name);
        for (String symbol : portfolio.keySet()) {
            System.out.println(symbol + " → " + portfolio.get(symbol) + " shares");
        }
        System.out.println("💰 Balance: $" + balance);
    }
}
