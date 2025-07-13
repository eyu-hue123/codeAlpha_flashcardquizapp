public class Reservation {
    String customerName;
    Room room;

    public Reservation(String name, Room room) {
        this.customerName = name;
        this.room = room;
    }

    public String toString() {
        return "Customer: " + customerName + " | Room: " + room.type + " | $" + room.price;
    }
}
