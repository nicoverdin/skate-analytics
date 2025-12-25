<template>
  <div class="min-h-screen flex items-center justify-center bg-bg-main p-4">
    <div class="max-w-md w-full bg-bg-card rounded-2xl shadow-xl p-8 border border-border-soft">
      <h2 class="text-3xl font-bold text-center text-white mb-8">Skate Analytics</h2>
      
      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-slate-300 mb-1">Usuario</label>
          <input v-model="username" name="username" type="text" required class="input-field" placeholder="Tu usuario">
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-300 mb-1">Contraseña</label>
          <input v-model="password" name="password" type="password" required class="input-field" placeholder="••••••••">
        </div>

        <button 
          type="submit" 
          :disabled="loading" 
          class="btn-primary w-full disabled:opacity-50"
        >
          {{ loading ? 'Entrando...' : 'Iniciar Sesión' }}
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

    const userResponse = await api.get('/api/auth/user/'); 
    localStorage.setItem('is_staff', userResponse.data.is_staff);

    router.push('/');
  } catch (err) {
    error.value = 'Credenciales incorrectas o error de conexión';
    console.error(err);
  }
};
</script>