// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PollingSystem {
    address public owner;
    uint public deadline;
    string[] public options;

    struct Voter {
        bool hasVoted;
        uint voteIndex;
    }

    mapping(address => Voter) public voters;
    mapping(uint => uint) public voteCounts;

    constructor(string[] memory _options, uint _durationInMinutes) {
        owner = msg.sender;
        options = _options;
        deadline = block.timestamp + (_durationInMinutes * 1 minutes);
    }

    // Vote for an option by index
    function vote(uint optionIndex) public {
        require(block.timestamp < deadline, "Voting has ended");
        require(!voters[msg.sender].hasVoted, "You already voted");
        require(optionIndex < options.length, "Invalid option");

        voters[msg.sender] = Voter(true, optionIndex);
        voteCounts[optionIndex]++;
    }

    // Get total votes for an option
    function getVoteCount(uint index) public view returns (uint) {
        return voteCounts[index];
    }

    // Get winning option (after deadline)
    function getWinningOption() public view returns (string memory winner, uint votes) {
        require(block.timestamp >= deadline, "Voting is still open");

        uint maxVotes = 0;
        uint winnerIndex = 0;

        for (uint i = 0; i < options.length; i++) {
            if (voteCounts[i] > maxVotes) {
                maxVotes = voteCounts[i];
                winnerIndex = i;
            }
        }

        return (options[winnerIndex], maxVotes);
    }

    // View all poll options
    function getOptions() public view returns (string[] memory) {
        return options;
    }
}