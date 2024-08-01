import React, { useState } from 'react';
import { registerUser, loginUser } from '../services/api';

const AuthComponent = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isRegister, setIsRegister] = useState(true);
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (isRegister) {
        const data = await registerUser(username, password);
        setMessage('Registration successful!');
      } else {
        const data = await loginUser(username, password);
        setMessage('Login successful!');
      }
    } catch (error) {
      setMessage(error.msg || 'Something went wrong');
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    setMessage('Logged out successfully');
  };

  return (
    <div>
      <h2>{isRegister ? 'Register' : 'Login'}</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
        </div>
        <div>
          <label>Password:</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <button type="submit">{isRegister ? 'Register' : 'Login'}</button>
      </form>
      <button onClick={() => setIsRegister(!isRegister)}>
        {isRegister ? 'Switch to Login' : 'Switch to Register'}
      </button>
      <button onClick={handleLogout}>Logout</button>
      <p>{message}</p>
    </div>
  );
};

export default AuthComponent;
