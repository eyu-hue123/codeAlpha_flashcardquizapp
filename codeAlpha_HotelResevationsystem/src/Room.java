public class Room {
    String type;
    double price;
    boolean isBooked;

    public Room(String type, double price) {
        this.type = type;
        this.price = price;
        this.isBooked = false;
    }

    public boolean bookRoom() {
        if (!isBooked) {
            isBooked = true;
            return true;
        }
        return false;
    }

    public void cancelBooking() {
        isBooked = false;
    }

    public String toString() {
        return type + " - $" + price + " | " + (isBooked ? "Booked" : "Available");
    }
}
