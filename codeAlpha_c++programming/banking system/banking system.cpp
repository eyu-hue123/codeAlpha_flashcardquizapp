
class Account {
private:
    string = "owner";
    double balance;

public:
    Account(string ownerName) {
        owner = ownerName;
        balance = 0.0;
    }

    void deposit(double amount) {
        balance += amount;
    }

    bool withdraw(double amount) {
        if (amount > balance) return false;
        balance -= amount;
        return true;
    }

    void display() {
        cout << "Owner: " << owner << ", Balance: " << balance<<endl;
    }
};
