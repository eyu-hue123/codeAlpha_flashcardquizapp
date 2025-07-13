import java.util.*;

public class HotelSystem {
    List<Room> rooms;
    List<Reservation> reservations;

    public HotelSystem() {
        rooms = new ArrayList<>();
        reservations = new ArrayList<>();
        rooms.add(new Room("Standard", 100));
        rooms.add(new Room("Deluxe", 200));
        rooms.add(new Room("Suite", 300));
    }

    public void showRooms() {
        rooms.forEach(r -> System.out.println(r));
    }

    public boolean bookRoom(String type, String name) {
        for (Room r : rooms) {
            if (r.type.equalsIgnoreCase(type) && !r.isBooked) {
                r.bookRoom();
                reservations.add(new Reservation(name, r));
                return true;
            }
        }
        return false;
    }

    public boolean cancelReservation(String name) {
        Iterator<Reservation> iter = reservations.iterator();
        while (iter.hasNext()) {
            Reservation res = iter.next();
            if (res.customerName.equalsIgnoreCase(name)) {
                res.room.cancelBooking();
                iter.remove();
                return true;
            }
        }
        return false;
    }

    public void viewBookings() {
        if (reservations.isEmpty()) {
            System.out.println("📭 No reservations found.");
        } else {
            reservations.forEach(res -> System.out.println(res));
        }
    }
}
