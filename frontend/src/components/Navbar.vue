<template>
  <nav class="bg-bg-card border-b border-border-soft px-8 py-4">
    <div class="max-w-6xl mx-auto flex justify-between items-center">
      <router-link to="/" class="text-xl font-bold text-white hover:text-brand-primary transition-colors">
        Skate Analytics <span class="text-xs font-mono text-slate-500 italic">v1.0</span>
      </router-link>

      <div class="flex items-center space-x-8">
        <router-link to="/" class="nav-link" active-class="text-brand-primary font-bold">
          Inicio
        </router-link>
        <router-link to="/skaters" class="nav-link" active-class="text-brand-primary font-bold">
          Patinadores
        </router-link>
        
        <button @click="handleLogout" class="ml-4 px-4 py-1.5 text-sm border border-red-500/30 text-red-400 rounded-md hover:bg-red-500/10 transition">
          Cerrar Sesión
        </button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const handleLogout = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  router.push('/login');
};
</script>

<style scoped>
@reference "../style.css";

.nav-link {
  @apply text-sm font-medium text-slate-400 hover:text-brand-primary transition-colors;
}
</style>