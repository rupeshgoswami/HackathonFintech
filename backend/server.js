const express = require('express');
const web3 = require('web3');
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');
const authRoutes = require('./models/routes/auth')
const forexRoutes = require('./models/routes/forex')

const app = express();
const port = process.env.PORT || 5000;
const web3 = new Web3('http://localhost:8545');
const Stablecoin = contract(StablecoinArtifact);
Stablecoin.setprovider(web3.currentProvider);

app.use(cors());
app.use('/api/auth',authRoutes);
app.use('/api/forex',forexRoutes)
app.use(bodyParser.json());
app.use(express.json());
// Database connection
app.post('/api/buy', async (req, res) => {
  const { amount } = req.body;
  const accounts = await web3.eth.getAccounts();
  try {
      const instance = await Stablecoin.deployed();
      const receipt = await instance.buyStablecoin({ from: accounts[0], value: web3.utils.toWei(amount, 'ether') });
      res.send(receipt);
  } catch (error) {
      res.status(500).send(error.toString());
  }
});

app.post('/api/sell', async (req, res) => {
  const { amount } = req.body;
  const accounts = await web3.eth.getAccounts();
  try {
      const instance = await Stablecoin.deployed();
      const receipt = await instance.sellStablecoin(web3.utils.toWei(amount, 'ether'), { from: accounts[0] });
      res.send(receipt);
  } catch (error) {
      res.status(500).send(error.toString());
  }
});

mongoose.connect('mongodb://localhost:27017/forex_system', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));
// Routes
// app.use('/api/auth', require('./routes/auth'));
app.use('/api/user', require('./models/routes/auth'));

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
