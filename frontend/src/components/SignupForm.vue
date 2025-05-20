<template>
  <div class="signup-container">
    <h2>Créer un utilisateur</h2>
    <form @submit.prevent="submitForm" novalidate>
      <div class="form-group">
        <label for="username">Nom d'utilisateur</label>
        <input
          id="username"
          type="text"
          v-model="username"
          required
          placeholder="Entrez votre nom d'utilisateur"
          autocomplete="username"
        />
      </div>

      <div class="form-group">
        <label for="email">Email</label>
        <input
          id="email"
          type="email"
          v-model="email"
          required
          placeholder="Entrez votre adresse email"
          autocomplete="email"
        />
      </div>

      <div class="form-group">
        <label for="password">Mot de passe</label>
        <input
          id="password"
          type="password"
          v-model="password"
          required
          placeholder="Entrez un mot de passe sécurisé"
          autocomplete="new-password"
        />
      </div>

      <button type="submit" :disabled="loading">
        <span v-if="loading">Création en cours...</span>
        <span v-else>Créer</span>
      </button>
    </form>

    <p v-if="error" class="error-message">{{ error }}</p>
    <p v-if="success" class="success-message">Utilisateur créé avec succès !</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '../utils/api'  // <-- Import your axios instance here

const username = ref('')
const email = ref('')
const password = ref('')

const error = ref('')
const success = ref(false)
const loading = ref(false)

const submitForm = async () => {
  error.value = ''
  success.value = false
  loading.value = true

  try {
    await api.post('/users/', {
      username: username.value,
      email: email.value,
      password: password.value
    })
    success.value = true
    username.value = ''
    email.value = ''
    password.value = ''
  } catch (err) {
    if (err.response && err.response.data && err.response.data.detail) {
      error.value = err.response.data.detail
    } else {
      error.value = "Une erreur est survenue."
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* Keep your existing styles */
.signup-container {
  max-width: 400px;
  margin: 2rem auto;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgb(0 0 0 / 0.1);
  background-color: #fff;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
}

h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #2e7d32;
}

.form-group {
  margin-bottom: 1.25rem;
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #555;
}

input {
  padding: 0.6rem 0.8rem;
  border: 1.5px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

input:focus {
  border-color: #2e7d32;
  outline: none;
  box-shadow: 0 0 4px #81c784;
}

button {
  width: 100%;
  padding: 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
  background-color: #2e7d32;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:disabled {
  background-color: #a5d6a7;
  cursor: not-allowed;
}

button:hover:not(:disabled) {
  background-color: #27632a;
}

.error-message {
  margin-top: 1rem;
  color: #d32f2f;
  font-weight: 600;
  text-align: center;
}

.success-message {
  margin-top: 1rem;
  color: #388e3c;
  font-weight: 600;
  text-align: center;
}

@media (max-width: 480px) {
  .signup-container {
    margin: 1rem;
    padding: 1.5rem;
  }
}
</style>
