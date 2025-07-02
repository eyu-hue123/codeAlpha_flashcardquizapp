#include <iostream>
#include <fstream> // for file handling
#include <string>
using namespace std;

// Register a new user
void registerUser() {
    string username, password;

    cout << "==== Register ====" << endl;
    cout << "Enter a new username: ";
    cin >> username;
    cout << "Enter a new password: ";
    cin >> password;

    // Save username and password to file
    ofstream file(username + ".txt"); // create file named username.txt
    file << username << endl << password;
    file.close();

    cout << " Registration successful!\n\n";
}

// Login existing user
bool loginUser() {
    string username, password;
    string savedUser, savedPass;

    cout << "==== Login ====" << endl;
    cout << "Enter username: ";
    cin >> username;
    cout << "Enter password: ";
    cin >> password;

    ifstream file(username + ".txt"); // read from file
    if (!file) {
        cout << " User not found.\n";
        return false;
    }

    getline(file, savedUser);
    getline(file, savedPass);
    file.close();

    if (username == savedUser && password == savedPass) {
        cout << " Login successful!\n\n";
        return true;
    } else {
        cout << "Incorrect password.\n";
        return false;
    }
}

int main() {
    int choice;

    cout << "==== Welcome to Login System ====\n";
    cout << "1. Register\n";
    cout << "2. Login\n";
    cout << "Enter your choice (1 or 2): ";
    cin >> choice;

    if (choice == 1) {
        registerUser();
    } else if (choice == 2) {
        loginUser();
    } else {
        cout << " Invalid choice.\n";
    }

    return 0;
}
