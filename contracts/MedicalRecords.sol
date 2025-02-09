// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MedicalRecords {
    struct FileMetadata {
        string cid;  // Encrypted file stored in IPFS
        address owner;
        mapping(address => bool) accessList;
    }

    mapping(address => FileMetadata[]) public patientFiles;

    function uploadFile(string memory _cid) public {
        patientFiles[msg.sender].push(FileMetadata({cid: _cid, owner: msg.sender}));
    }

    function grantAccess(address _doctor, uint index) public {
        patientFiles[msg.sender][index].accessList[_doctor] = true;
    }

    function getFileMetadata(address _patient, uint index) public view returns (string memory) {
        require(patientFiles[_patient][index].accessList[msg.sender], "Access Denied");
        return patientFiles[_patient][index].cid;
    }
}
