// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity ^0.8.20;

/**
 * @title Project
 * @dev Gestion de projet souverain, modulaire, extensible, sécurisé, RGPD-ready
 */
import "@openzeppelin/contracts/access/Ownable.sol";

contract Project is Ownable {
    string public name;
    address public admin;
    event ProjectCreated(string name, address indexed admin);
    event ProjectUpdated(string name);

    constructor(string memory _name) {
        name = _name;
        admin = msg.sender;
        emit ProjectCreated(_name, msg.sender);
    }

    function updateName(string memory _name) public onlyOwner {
        name = _name;
        emit ProjectUpdated(_name);
    }
}
