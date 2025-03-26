const HealthCareRecord = artifacts.require("HealthCareRecord");

module.exports = function (deployer) {
  deployer.deploy(HealthCareRecord);
};