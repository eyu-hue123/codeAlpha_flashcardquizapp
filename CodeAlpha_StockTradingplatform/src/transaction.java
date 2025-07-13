import java.util.Date;

public class Transaction {
    String symbol;
    int qty;
    boolean isBuy;
    Date timestamp;

    public Transaction(String symbol, int qty, boolean isBuy) {
        this.symbol = symbol;
        this.qty = qty;
        this.isBuy = isBuy;
        this.timestamp = new Date();
    }

    public String toString() {
        return (isBuy ? "Buy" : "Sell") + " " + qty + " x " + symbol + " @ " + timestamp;
    }
}
