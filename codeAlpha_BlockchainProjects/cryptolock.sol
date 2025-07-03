 
pragma solidity ^0.8.0;

contract CryptoLock {
    struct Lock {
        uint amount;
        uint unlockTime;
    }

    mapping(address => Lock) public locks;

    // Deposit ETH and set unlock time (in seconds from now)
    function lockFunds(uint durationInSeconds) public payable {
        require(msg.value > 0, "Send some ETH");
        require(locks[msg.sender].amount == 0, "You already locked funds");

        locks[msg.sender] = Lock(msg.value, block.timestamp + durationInSeconds);
    }

    // Check when user can withdraw
    function getUnlockTime(address user) public view returns (uint) {
        return locks[user].unlockTime;
    }

    // Withdraw ETH after unlock time
    function withdraw() public {
        Lock memory userLock = locks[msg.sender];
        require(userLock.amount > 0, "No funds locked");
        require(block.timestamp >= userLock.unlockTime, "Funds are still locked");

        uint amount = userLock.amount;
        locks[msg.sender].amount = 0; // prevent re-entrancy

        payable(msg.sender).transfer(amount);
    }

    // Check locked amount
    function getLockedAmount(address user) public view returns (uint) {
        return locks[user].amount;
    }
}