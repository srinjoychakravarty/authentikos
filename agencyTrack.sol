// contract at https://rinkeby.etherscan.io/address/

pragma solidity ^0.4.19;
pragma experimental ABIEncoderV2;

import "github.com/Arachnid/solidity-stringutils/strings.sol";

contract Authentikos {

    struct Agency {
        address ethIdentity;
    }

    address public contractOwner;
    mapping (string => Agency) agencies;
    using strings for *;
    string private agencyStrings;
    uint16 public agencyCount;

    modifier onlyOwner() {
      require(msg.sender == contractOwner);
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

    function setAgency(string _address, address _ethIdentity) public {
        var agency = agencies[_address];
        agency.ethIdentity = _ethIdentity;
        agencyCount += 1;
        stringConcat(agencyStrings, " ", _address);
    }

    function getAgency(string _address) view public returns (address) {
        return (agencies[_address].ethIdentity);
    }

    function getAgencies() view public returns (string) {
        return agencyStrings;
    }

    function countAgencies() view public returns (uint) {
        return agencyCount;
    }
}
