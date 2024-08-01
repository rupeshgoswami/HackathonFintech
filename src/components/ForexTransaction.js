// frontend/src/components/ForexTransaction.js
import React, { useState } from 'react';
import axios from 'axios';

const ForexTransaction = () => {
    const [amount, setAmount] = useState('');
    const [message, setMessage] = useState('');

    const handleBuy = async () => {
        try {
            const response = await axios.post('/api/forex/buy', { amount });
            setMessage(response.data);
        } catch (error) {
            setMessage(error.response.data);
        }
    };

    const handleSell = async () => {
        try {
            const response = await axios.post('/api/forex/sell', { amount });
            setMessage(response.data);
        } catch (error) {
            setMessage(error.response.data);
        }
    };

    return (
        <div>
            <h2>Forex Transactions</h2>
            <input
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                placeholder="Amount"
            />
            <button onClick={handleBuy}>Buy Stablecoin</button>
            <button onClick={handleSell}>Sell Stablecoin</button>
            <p>{message}</p>
        </div>
    );
};

export default ForexTransaction;