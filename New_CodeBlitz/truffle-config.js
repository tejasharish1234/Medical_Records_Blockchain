module.exports = {
  networks: {
    development: {
      host: "127.0.0.1", // Localhost
      port: 7545, // Default Ganache port
      network_id: "*", // Match any network ID
      gas: 6721975, // Increase if needed
      gasPrice: 20000000000, // 20 gwei
    },
  },
  compilers: {
    solc: {
      version: "0.5.0", // Match your Solidity version
    },
  },
};
