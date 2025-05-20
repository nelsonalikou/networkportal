import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;  // for Vite
// const API_BASE_URL = process.env.VUE_APP_API_BASE_URL; // for Vue CLI

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

api.interceptors.request.use((config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export default api;
