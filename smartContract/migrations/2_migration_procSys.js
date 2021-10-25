const Migrations = artifacts.require("procurement");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
};

