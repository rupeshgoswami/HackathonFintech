import React from 'react';
import { Link } from 'react-router-dom';


const Dashboard = () => {
  return (
    <div>
      <h2>Dashboard</h2>
      <nav>
        <ul>
          <li><Link to="/wallet">Wallet</Link></li>
          <li><Link to="/forex">Forex</Link></li>
          <li><Link to="/history">History</Link></li>
        </ul>
      </nav>
    </div>
  );
};

export default Dashboard;
