// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;
pragma experimental ABIEncoderV2; // ✅ Enable experimental ABIEncoderV2

contract HealthCareRecord {
    address public owner;

    struct Record {
        uint256 recordID;
        string patientName;
        string diagnosis;
        string treatment;
        uint256 timestamp;
    }

    mapping(uint256 => Record[]) private patientRecords;
    mapping(address => bool) private AuthorisedProvider;
    uint256[] private patientIDs;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier onlyAuth() {
        require(AuthorisedProvider[msg.sender], "Only authorized providers can call this function");
        _;
    }

    // ✅ Explicitly mark constructor as `public`
    constructor() public {
        owner = msg.sender;
    }

    function getOwner() public view returns (address) {
        return owner;
    }

    function authorizeProvider(address provider) public onlyOwner {
        AuthorisedProvider[provider] = true;
    }

    function revokeProvider(address provider) public onlyOwner {
        AuthorisedProvider[provider] = false;
    }

    function addRecord(uint256 patientID, string memory patientName, string memory diagnosis, string memory treatment) 
        public onlyAuth 
    {
        require(patientID != 0, "Patient ID cannot be zero");
        
        if (patientRecords[patientID].length == 0) {
            patientIDs.push(patientID);
        }
        
        uint256 recordID = patientRecords[patientID].length + 1;
        patientRecords[patientID].push(Record(recordID, patientName, diagnosis, treatment, block.timestamp));
    }

    // ✅ Enable returning a struct array using ABIEncoderV2
    function getPatientRecords(uint256 patientID) public view onlyAuth returns (Record[] memory) {
        return patientRecords[patientID];
    }

    function getAllRecords() public view onlyAuth returns (Record[] memory) {
        uint256 totalRecords = 0;
        for (uint256 i = 0; i < patientIDs.length; i++) {
            totalRecords += patientRecords[patientIDs[i]].length;
        }
        
        Record[] memory allRecords = new Record[](totalRecords);
        uint256 index = 0;
        for (uint256 i = 0; i < patientIDs.length; i++) {
            uint256 id = patientIDs[i];
            for (uint256 j = 0; j < patientRecords[id].length; j++) {
                allRecords[index] = patientRecords[id][j];
                index++;
            }
        }

        return allRecords;
    }
}
