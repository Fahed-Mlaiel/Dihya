// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity ^0.8.20;

/**
 * @title Payment
 * @dev Paiements souverains, auditables, RGPD-ready, extensibles (multi-token)
 */
import "@openzeppelin/contracts/access/Ownable.sol";

contract Payment is Ownable {
    event PaymentSent(address indexed from, address indexed to, uint256 amount);
    function sendPayment(address to) public payable {
        require(msg.value > 0, "Montant nul");
        payable(to).transfer(msg.value);
        emit PaymentSent(msg.sender, to, msg.value);
    }
}
