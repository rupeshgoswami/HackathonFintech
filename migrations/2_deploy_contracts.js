const Stablecoin = artifacts.require("Stablecoin");

module.exports = function(deployer) {
    deployer.deploy(Stablecoin, 1000000);  // Initial supply of 1,000,000 tokens
};
