import React from 'react';
import {BrowserRouter as Router,Route,Switch} from 'react-router-dom'
import AuthComponent from './components/AuthComponent';
import Dashboard from './components/Dashboard';
import Wallet from './components/Wallet';
import Forex from './components/Forex';
import History from './components/History';
import ForexTransaction from './components/ForexTransaction'
import PrivateRoute from './components/PrivateRoute';
function App() {
  return (
    <Router>
    <div className="App">
      <Switch>
        <Route exact path="/" component={AuthComponent} />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/wallet" component={Wallet} />
        <Route path="/forex" component={Forex} />
        <Route path="/history" component={History} />
        <Route path="/forextransaction" component={ForexTransaction} />
      </Switch>
    </div>
  </Router>
  );
}

export default App;