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
        <router-link v-if="!isAdmin" :to="`/skaters/${selfId}`" class="nav-link" active-class="text-brand-primary font-bold">
          Mi Rendimiento
        </router-link>
        <router-link v-if="isAdmin" to="/skaters" class="nav-link" active-class="text-brand-primary font-bold">
          Patinadores
        </router-link>
        <router-link to="/results" class="nav-link" active-class="text-brand-primary font-bold">
          Resultados
        </router-link>
        <router-link to="/catalog" class="nav-link" active-class="text-brand-primary font-bold">
          Catálogo SOV
        </router-link>
        
        <button @click="handleLogout" class="ml-4 px-4 py-1.5 text-sm border border-red-500/30 text-red-400 rounded-md hover:bg-red-500/10 transition">
          Cerrar Sesión
        </button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '../api/axios';

const router = useRouter();
const isAdmin = localStorage.getItem('is_staff') === 'true';
const selfId = ref(null);

const getUserIdFromToken = (token) => {
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload).user_id;
  } catch (e) {
    return null;
  }
};

const handleLogout = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  router.push('/login');
};

onMounted(async () => {
  const token = localStorage.getItem('access_token');
  
  if (!token) return;

  try {
    const currentUserId = getUserIdFromToken(token);
    
    if (currentUserId) {
      const skatersRes = await api.get('/api/skaters/');
      
      const isAdmin = localStorage.getItem('is_staff') === 'true';

      if (!isAdmin) {
        const myProfile = skatersRes.data.find(s => String(s.user) === String(currentUserId));
        if (myProfile) {
          selfId.value = myProfile.id;
          console.log("Perfil encontrado. Skater ID:", selfId.value);
        }
      }
    }
  } catch (error) {
    if (error.response && error.response.status === 401) {
      console.warn("Sesión expirada en Navbar. No redirigir aquí para evitar bucles.");
    } else {
      console.error("Error en Navbar:", error);
    }
  }
});
</script>

<style scoped>
@reference "../style.css";

.nav-link {
  @apply text-sm font-medium text-slate-400 hover:text-brand-primary transition-colors;
}
</style>