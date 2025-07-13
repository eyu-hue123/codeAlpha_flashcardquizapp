import java.util.ArrayList;

public class Student {
    String name;
    ArrayList<Integer> grades;

    public Student(String name) {
        this.name = name;
        this.grades = new ArrayList<>();
    }

    public void addGrade(int grade) {
        grades.add(grade);
    }

    public double getAverage() {
        return grades.stream().mapToInt(Integer::intValue).average().orElse(0.0);
    }

    public int getHighest() {
        return grades.stream().mapToInt(Integer::intValue).max().orElse(0);
    }

    public int getLowest() {
        return grades.stream().mapToInt(Integer::intValue).min().orElse(0);
    }
}
