#include <iostream>
#include <iomanip> // For setting decimal places
using namespace std;

int main() {
    int numCourses;
    float grade, credit;
    float totalCredits = 0, totalGradePoints = 0;

    cout << "===== CGPA Calculator =====" << endl;
    cout << "Enter the number of courses: ";
    cin >> numCourses;

    // Loop through each course
    for (int i = 1; i <= numCourses; ++i) {
        cout << "\nCourse " << i << ":" << endl;

        cout << "  Enter grade (e.g. 4.0, 3.7): ";
        cin >> grade;

        cout << "  Enter credit hours: ";
        cin >> credit;

        totalCredits += credit;
        totalGradePoints += grade * credit;
    }

    if (totalCredits == 0) {
        cout << "\nError: Total credit hours is zero. CGPA cannot be calculated." << endl;
    } else {
        float cgpa = totalGradePoints / totalCredits;
        cout << fixed << setprecision(2); // show 2 decimal places
        cout << "\n✅ Your CGPA is: " << cgpa << endl;
    }

    return 0;
}
