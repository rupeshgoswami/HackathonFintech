import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000/api',
});

export const registerUser = async (username, password) => {
  try {
    const response = await api.post('/auth/register', { username, password });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const loginUser = async (username, password) => {
  try {
    const response = await api.post('/auth/login', { username, password });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};
