<template>
  <div class="min-h-screen flex items-center justify-center bg-slate-900 p-4">
    <div class="max-w-md w-full bg-slate-800 rounded-2xl shadow-xl p-8 border border-slate-700">
      <h2 class="text-3xl font-bold text-center text-white mb-8">Skate Analytics</h2>
      
      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-slate-300">Usuario</label>
          <input v-model="username" type="text" required 
            class="mt-1 block w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none transition"
            placeholder="Introduce tu usuario">
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-300">Contraseña</label>
          <input v-model="password" type="password" required 
            class="mt-1 block w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none transition"
            placeholder="••••••••">
        </div>

        <button type="submit" 
          class="w-full py-3 px-4 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-lg shadow-md transition duration-200 ease-in-out transform hover:-translate-y-1">
          Iniciar Sesión
        </button>
      </form>
      
      <p v-if="error" class="mt-4 text-sm text-red-400 text-center">{{ error }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import api from '../api/axios';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const error = ref('');
const router = useRouter();

const handleLogin = async () => {
  try {
    error.value = '';
    const response = await api.post('/api/auth/login/', {
      username: username.value,
      password: password.value
    });
    
    localStorage.setItem('access_token', response.data.access);
    localStorage.setItem('refresh_token', response.data.refresh);
    
    router.push('/');
  } catch (err) {
    error.value = 'Credenciales incorrectas o error de conexión';
    console.error(err);
  }
};
</script>