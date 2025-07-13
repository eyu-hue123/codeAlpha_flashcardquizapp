import java.util.*;

public class GradeTracker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Student> students = new ArrayList<>();

        System.out.print("Enter number of students: ");
        int count = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < count; i++) {
            System.out.print("Student name: ");
            String name = scanner.nextLine();
            Student student = new Student(name);

            System.out.print("Enter number of grades for " + name + ": ");
            int numGrades = Integer.parseInt(scanner.nextLine());

            for (int j = 0; j < numGrades; j++) {
                System.out.print("Enter grade " + (j + 1) + ": ");
                int grade = Integer.parseInt(scanner.nextLine());
                student.addGrade(grade);
            }

            students.add(student);
        }

        System.out.println("\n📊 Grade Summary:");
        for (Student s : students) {
            System.out.printf("Student: %s | Avg: %.2f | Max: %d | Min: %d%n",
                s.name, s.getAverage(), s.getHighest(), s.getLowest());
        }
    }
}
