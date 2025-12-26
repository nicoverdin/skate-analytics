<template>
  <nav class="bg-bg-card border-b border-border-soft px-4 py-3 md:px-8 md:py-4 sticky top-0 z-50">
    <div class="max-w-6xl mx-auto flex justify-between items-center">
      
      <router-link to="/" class="text-lg md:text-xl font-bold text-white hover:text-brand-primary transition-colors flex items-center gap-2">
        Skate Analytics <span class="text-[10px] md:text-xs font-mono text-slate-500 italic">v1.0</span>
      </router-link>

      <button @click="toggleMenu" class="md:hidden text-slate-400 hover:text-white focus:outline-none">
        <svg v-if="!isMenuOpen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <div class="hidden md:flex items-center space-x-8">
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

    <div v-show="isMenuOpen" class="md:hidden mt-4 border-t border-border-soft pt-4 flex flex-col space-y-4 pb-2 animate-fade-in">
        <router-link to="/" class="mobile-nav-link" active-class="text-brand-primary font-bold" @click="toggleMenu">
          Inicio
        </router-link>
        <router-link v-if="!isAdmin" :to="`/skaters/${selfId}`" class="mobile-nav-link" active-class="text-brand-primary font-bold" @click="toggleMenu">
          Mi Rendimiento
        </router-link>
        <router-link v-if="isAdmin" to="/skaters" class="mobile-nav-link" active-class="text-brand-primary font-bold" @click="toggleMenu">
          Patinadores
        </router-link>
        <router-link to="/results" class="mobile-nav-link" active-class="text-brand-primary font-bold" @click="toggleMenu">
          Resultados
        </router-link>
        <router-link to="/catalog" class="mobile-nav-link" active-class="text-brand-primary font-bold" @click="toggleMenu">
          Catálogo SOV
        </router-link>
        
        <button @click="handleLogout" class="w-full text-left mobile-nav-link text-red-400 hover:text-red-300">
          Cerrar Sesión
        </button>
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

const isMenuOpen = ref(false);

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

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
      // Recalcular admin por si acaso
      const isAdminCheck = localStorage.getItem('is_staff') === 'true';

      if (!isAdminCheck) {
        const myProfile = skatersRes.data.find(s => String(s.user) === String(currentUserId));
        if (myProfile) {
          selfId.value = myProfile.id;
        }
      }
    }
  } catch (error) {
    if (error.response && error.response.status === 401) {
      console.warn("Sesión expirada.");
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

.mobile-nav-link {
  @apply block text-base font-medium text-slate-300 hover:text-brand-primary transition-colors px-2 py-1 rounded hover:bg-white/5;
}

.animate-fade-in {
  animation: fadeIn 0.2s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>