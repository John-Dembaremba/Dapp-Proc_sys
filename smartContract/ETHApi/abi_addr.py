import json


def get_addr():
  contract_addr = '0xaD6dd7eDBF298CEfF176db1DbB02638Dc70f1637'
  return contract_addr

def get_abi():
    json_data = """
      [{
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "job_id",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "price_unity",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "total_price",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "zimraITF263",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "praz",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "validity",
          "type": "string"
        }
      ],
      "name": "Bidders",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "product_type",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "product",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "requirements",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "date",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "delivery_period",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "job",
          "type": "uint256"
        }
      ],
      "name": "Jobs",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "job_id",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "price_unity",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "total_price",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "zimraITF263",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "praz",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "validity",
          "type": "string"
        }
      ],
      "name": "Winner",
      "type": "event"
    },
    {
      "inputs": [],
      "name": "job_id",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "supplier",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "job_id",
          "type": "uint256"
        },
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "price_unit",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "total_price",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "zimraITF263",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "praz",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "validity",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "transaction",
      "outputs": [
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "product_type",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "product",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "requirements",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "date",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "delivery_period",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "job",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "user",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_productType",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_product",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_req",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_date",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_del",
          "type": "string"
        }
      ],
      "name": "addTransaction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_job",
          "type": "uint256"
        },
        {
          "internalType": "string",
          "name": "_supNm",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "unit_price",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "total_price",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_zimraITF263",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_praz",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_validity",
          "type": "string"
        }
      ],
      "name": "addSuppliers",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_id",
          "type": "uint256"
        }
      ],
      "name": "setJob_id",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_job",
          "type": "uint256"
        },
        {
          "internalType": "string",
          "name": "_supNm",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "unit_price",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "total_price",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_zimraITF263",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_praz",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_validity",
          "type": "string"
        }
      ],
      "name": "award_bider",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }]
  """
    abi = json.loads(json_data)
    return abi




































