import java.util.*;

public class Main {
    public static void main(String[] args) {
        HotelSystem hotel = new HotelSystem();
        Scanner sc = new Scanner(System.in);
        System.out.println("🏨 Welcome to CodeAlpha Hotel Booking");

        while (true) {
            System.out.println("\n📋 Menu:");
            System.out.println("1. View Rooms");
            System.out.println("2. Book Room");
            System.out.println("3. Cancel Booking");
            System.out.println("4. View Reservations");
            System.out.println("0. Exit");
            System.out.print("Choose: ");
            int option = sc.nextInt();
            sc.nextLine();

            switch (option) {
                case 1:
                    hotel.showRooms(); break;
                case 2:
                    System.out.print("Enter name: ");
                    String name = sc.nextLine();
                    System.out.print("Enter room type: ");
                    String type = sc.nextLine();
                    if (hotel.bookRoom(type, name)) {
                        System.out.println("✅ Booking confirmed!");
                    } else {
                        System.out.println("❌ Room unavailable.");
                    }
                    break;
                case 3:
                    System.out.print("Enter your name to cancel: ");
                    String cancelName = sc.nextLine();
                    if (hotel.cancelReservation(cancelName)) {
                        System.out.println("✅ Reservation cancelled.");
                    } else {
                        System.out.println("❌ No booking found.");
                    }
                    break;
                case 4:
                    hotel.viewBookings(); break;
                case 0:
                    System.out.println("👋 Goodbye!");
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}
