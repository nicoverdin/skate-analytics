<template>
  <div class="p-8">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-4xl font-bold text-white mb-4">Bienvenido a tu Panel</h1>
      <p class="text-slate-400 text-lg">Has iniciado sesión correctamente.</p>
      
      <div class="mt-8 bg-slate-800 p-6 rounded-xl border border-slate-700">
        <h3 class="text-xl font-semibold text-indigo-400 mb-2">Tu sesión actual:</h3>
        <code class="block bg-black p-4 rounded text-xs text-green-400 break-all">
          Token: {{ token.substring(0, 50) }}...
        </code>
      </div>

      <button @click="handleLogout" class="mt-6 text-red-400 hover:text-red-300 transition underline">
        Cerrar sesión
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();
const token = localStorage.getItem('access_token') || 'No encontrado';

const handleLogout = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  router.push('/login');
};
</script>