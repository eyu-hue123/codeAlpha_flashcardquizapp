 
pragma solidity ^0.8.0;

contract SimpleStorage {
    int public value; // Public variable to store value

    // Set initial value (optional constructor)
    constructor() {
        value = 0;
    }

    // Increase the stored value
    function increment() public {
        value += 1;
    }

    // Decrease the stored value
    function decrement() public {
        value -= 1;
    }

    // Get current value (optional, since 'value' is public)
    function getValue() public view returns (int) {
        return value;
    }
}