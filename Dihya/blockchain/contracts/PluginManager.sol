// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity ^0.8.20;

/**
 * @title PluginManager
 * @dev Gestion des plugins métiers, extensible, sécurisé, RGPD-ready
 */
import "@openzeppelin/contracts/access/Ownable.sol";

contract PluginManager is Ownable {
    mapping(string => address) public plugins;
    event PluginAdded(string name, address indexed plugin);
    event PluginRemoved(string name);

    function addPlugin(string memory name, address plugin) public onlyOwner {
        plugins[name] = plugin;
        emit PluginAdded(name, plugin);
    }
    function removePlugin(string memory name) public onlyOwner {
        delete plugins[name];
        emit PluginRemoved(name);
    }
}
