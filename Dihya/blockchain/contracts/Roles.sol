// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity ^0.8.20;

/**
 * @title Roles
 * @dev Gestion des rôles (RBAC) pour Dihya, extensible, sécurisé, RGPD-ready
 */
import "@openzeppelin/contracts/access/AccessControl.sol";

contract Roles is AccessControl {
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    bytes32 public constant USER_ROLE = keccak256("USER_ROLE");
    bytes32 public constant AUDITOR_ROLE = keccak256("AUDITOR_ROLE");

    constructor() {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(ADMIN_ROLE, msg.sender);
    }

    function addUser(address user) public onlyRole(ADMIN_ROLE) {
        grantRole(USER_ROLE, user);
    }
    function addAuditor(address auditor) public onlyRole(ADMIN_ROLE) {
        grantRole(AUDITOR_ROLE, auditor);
    }
}
