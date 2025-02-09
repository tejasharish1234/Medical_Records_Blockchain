from web3 import Web3

# Connect to Ethereum blockchain (Ganache RPC)
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Smart contract ABI and address
contract_address = "0x0fC5025C764cE34df352757e82f7B5c4Df39A836"

contract_abi = [
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "string",
				"name": "patientName",
				"type": "string"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "grantee",
				"type": "address"
			}
		],
		"name": "AccessGranted",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "string",
				"name": "patientName",
				"type": "string"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "grantee",
				"type": "address"
			}
		],
		"name": "AccessRevoked",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_patientName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_recordData",
				"type": "string"
			}
		],
		"name": "addRecord",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_patientName",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_grantee",
				"type": "address"
			}
		],
		"name": "authorizeAccess",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "recordId",
				"type": "uint256"
			},
			{
				"indexed": True,
				"internalType": "string",
				"name": "patientName",
				"type": "string"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "creator",
				"type": "address"
			}
		],
		"name": "RecordAdded",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "recordId",
				"type": "uint256"
			},
			{
				"indexed": True,
				"internalType": "string",
				"name": "patientName",
				"type": "string"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "updater",
				"type": "address"
			}
		],
		"name": "RecordUpdated",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_patientName",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_grantee",
				"type": "address"
			}
		],
		"name": "revokeAccess",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_recordId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_newRecordData",
				"type": "string"
			}
		],
		"name": "updateRecord",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_recordId",
				"type": "uint256"
			}
		],
		"name": "getRecordById",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "recordId",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "patientName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "recordData",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					},
					{
						"internalType": "address",
						"name": "creator",
						"type": "address"
					}
				],
				"internalType": "struct MedicalRecords.MedicalRecord",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_patientName",
				"type": "string"
			}
		],
		"name": "getRecords",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "recordId",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "patientName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "recordData",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					},
					{
						"internalType": "address",
						"name": "creator",
						"type": "address"
					}
				],
				"internalType": "struct MedicalRecords.MedicalRecord[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "nextRecordId",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]  # Paste your compiled contract ABI here


# Create a contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Function to add a medical record (adjusting for correct function names from ABI)
def add_medical_record(patient_name, record_data, sender_address, sender_private_key):
    txn = contract.functions.addRecord(patient_name, record_data).build_transaction({
        'from': sender_address,
        'gas': 2000000,
        'nonce': web3.eth.get_transaction_count(sender_address),
        'gasPrice': web3.to_wei('10', 'gwei')  # Set gas price
    })

    signed_txn = web3.eth.account.sign_transaction(txn, sender_private_key)
    txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

    print("Transaction sent! Hash:", txn_hash.hex())

# Example Usage
sender_address = "0x92a4c358462d06c7B7212Db6912F79a5CB5372A4"
sender_private_key = "0x7b8afd0a9ad3d8f74878b288c3ceb62d84cc7356f3f07b9edefc284a8a639335"  # ⚠️ DO NOT HARDCODE THIS IN REAL PROJECTS!

# Call function
add_medical_record("John Doe", "Diagnosed with flu.", sender_address, sender_private_key)
