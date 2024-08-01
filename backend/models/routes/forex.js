// backend/routes/forex.js
const express = require('express');
const router = express.Router();
const { web3, forexContract } = require('../web3Service');

router.post('/buy', async (req, res) => {
    const { amount } = req.body;
    try {
        const accounts = await web3.eth.getAccounts();
        const receipt = await forexContract.methods.buyStablecoin(web3.utils.toWei(amount, 'ether')).send({
            from: accounts[0],
            value: web3.utils.toWei(amount, 'ether')
        });
        res.send(receipt);
    } catch (error) {
        res.status(500).send(error.toString());
    }
});

router.post('/sell', async (req, res) => {
    const { amount } = req.body;
    try {
        const accounts = await web3.eth.getAccounts();
        const receipt = await forexContract.methods.sellStablecoin(web3.utils.toWei(amount, 'ether')).send({
            from: accounts[0]
        });
        res.send(receipt);
    } catch (error) {
        res.status(500).send(error.toString());
    }
});

module.exports = router;
