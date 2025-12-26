<template>
  <div class="min-h-screen flex items-center justify-center bg-bg-main p-4">
    <div class="max-w-md w-full bg-bg-card rounded-2xl shadow-xl p-8 border border-border-soft">
      
      <div class="text-center mb-8">
        <div class="inline-flex items-center justify-center h-16 w-16 rounded-full bg-brand-primary/10 text-brand-primary mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
          </svg>
        </div>
        <h2 class="text-3xl font-bold text-white">Skate Analytics</h2>
        <p class="text-slate-500 text-sm mt-2">Acceso al panel de control</p>
      </div>
      
      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-slate-300 mb-1">Usuario</label>
          <input 
            v-model="username" 
            name="username" 
            type="text" 
            autocomplete="username" 
            required 
            class="input-field w-full" 
            placeholder="Tu usuario"
          >
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-300 mb-1">Contraseña</label>
          <input 
            v-model="password" 
            name="password" 
            type="password" 
            autocomplete="current-password"
            required 
            class="input-field w-full" 
            placeholder="••••••••"
          >
        </div>

        <button 
          type="submit" 
          :disabled="loading" 
          class="btn-primary w-full disabled:opacity-50 py-3 font-bold shadow-lg shadow-brand-primary/20 active:scale-[0.98] transition-transform"
        >
          {{ loading ? 'Conectando...' : 'Iniciar Sesión' }}
        </button>
      </form>
      
      <p v-if="error" class="mt-6 text-sm text-red-400 text-center bg-red-500/10 p-3 rounded-lg border border-red-500/20">
        {{ error }}
      </p>
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
const loading = ref(false);
const router = useRouter();

const handleLogin = async () => {
  loading.value = true;
  error.value = '';
  
  try {
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
    error.value = 'Usuario o contraseña incorrectos.';
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>