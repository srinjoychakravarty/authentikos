// contract at https://rinkeby.etherscan.io/address/0xC3737aF68f5471a2607C996525993a8E9AF1862F

pragma solidity ^0.4.19;
pragma experimental ABIEncoderV2;

import "github.com/Arachnid/solidity-stringutils/strings.sol";

contract Authentikos {

    struct Agency {
        address ethIdentity;
        bool exists;
    }

    struct Article {
        string agencyChecksum;
        string contentHash;
    }

    address private contractOwner;
    mapping (string => Agency) agencies;
    mapping (string => Article) articles;
    using strings for *;
    string private agencyStrings;
    uint16 private agencyCount;

    modifier onlyOwner() {
      require(msg.sender == contractOwner, "Only contract owner can call this function");
      _;
    }

    function Authentikos() public {
      contractOwner = msg.sender;
      agencyCount = 0;
    }

    function stringConcat(string s1, string s2, string s3) internal returns(string) {
        var s0 = s1.toSlice().concat(s2.toSlice());
        agencyStrings = s0.toSlice().concat(s3.toSlice());
    }

    function setAgency(string _checksum, address _ethIdentity) public onlyOwner {
        var agency = agencies[_checksum];
        bool isNew = agency.exists;
        require(isNew == false, "News agency domain already registered");
        agency.ethIdentity = _ethIdentity;
        agency.exists = true;
        agencyCount += 1;
        stringConcat(agencyStrings, " ", _checksum);
    }

    function getContractOwner() view public returns (address) {
        return contractOwner;
    }

    function getOneAgency(string _checksum) view public returns (address) {
        return (agencies[_checksum].ethIdentity);
    }

    function getAllAgencies() view public returns (string) {
        return agencyStrings;
    }

    function getAgencyCount() view public returns (uint) {
        return agencyCount;
    }
}
