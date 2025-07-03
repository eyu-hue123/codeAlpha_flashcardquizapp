// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiSend {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    // Payable function to send ETH to multiple addresses equally
    function sendEther(address[] calldata recipients) external payable {
        uint amountPerRecipient = msg.value / recipients.length;

        require(recipients.length > 0, "No recipients.");
        require(msg.value > 0, "Send some ETH.");
        require(amountPerRecipient > 0, "Amount too small.");

        for (uint i = 0; i < recipients.length; i++) {
            payable(recipients[i]).transfer(amountPerRecipient);
        }
    }
}