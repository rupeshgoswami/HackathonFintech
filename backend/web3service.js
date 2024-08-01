// backend/web3Service.js
const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'); // Replace with your Infura project ID or local Ethereum node

const contractABI = [/* Your contract ABI here */];
const contractAddress = 'YOUR_CONTRACT_ADDRESS'; // Replace with your contract address
const forexContract = new web3.eth.Contract(contractABI, contractAddress);

module.exports = { web3, forexContract };
