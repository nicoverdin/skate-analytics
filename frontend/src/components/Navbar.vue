<template>
  <nav class="bg-bg-card border-b border-border-soft fixed top-0 left-0 w-full z-50 pt-[env(safe-area-inset-top)] transition-all duration-300 shadow-lg shadow-black/20">
    
    <div class="px-4 py-3 md:px-8 md:py-4">
      <div class="max-w-6xl mx-auto flex justify-between items-center">
        
        <div 
          @click="navigate('/')" 
          class="cursor-pointer text-lg md:text-xl font-bold text-white hover:text-brand-primary transition-colors flex items-center gap-2"
        >
          Skate Analytics <span class="text-[10px] md:text-xs font-mono text-slate-500 italic">v1.0</span>
        </div>

        <button @click="toggleMenu" class="md:hidden text-slate-400 hover:text-white focus:outline-none p-1">
          <svg v-if="!isMenuOpen" xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>

        <div class="hidden md:flex items-center space-x-8">
          <button @click="navigate('/')" :class="getDesktopClass('/')">Inicio</button>
          
          <button v-if="!isAdmin && selfId" @click="navigate(`/skaters/${selfId}`)" :class="getDesktopClass(`/skaters/${selfId}`)">
            Mi Rendimiento
          </button>
          
          <button v-if="isAdmin" @click="navigate('/skaters')" :class="getDesktopClass('/skaters')">
            Patinadores
          </button>
          
          <button @click="navigate('/results')" :class="getDesktopClass('/results')">
            Resultados
          </button>
          
          <button @click="navigate('/catalog')" :class="getDesktopClass('/catalog')">
            Catálogo SOV
          </button>
          
          <button @click="handleLogout" class="ml-4 px-4 py-1.5 text-sm border border-red-500/30 text-red-400 rounded-md hover:bg-red-500/10 transition">
            Cerrar Sesión
          </button>
        </div>
      </div>

      <div v-show="isMenuOpen" class="md:hidden mt-4 border-t border-border-soft pt-4 flex flex-col space-y-4 pb-4 animate-fade-in">
          <button @click="navigate('/')" :class="getMobileClass('/')">
            Inicio
          </button>
          
          <button v-if="!isAdmin && selfId" @click="navigate(`/skaters/${selfId}`)" :class="getMobileClass(`/skaters/${selfId}`)">
            Mi Rendimiento
          </button>
          
          <button v-if="isAdmin" @click="navigate('/skaters')" :class="getMobileClass('/skaters')">
            Patinadores
          </button>
          
          <button @click="navigate('/results')" :class="getMobileClass('/results')">
            Resultados
          </button>
          
          <button @click="navigate('/catalog')" :class="getMobileClass('/catalog')">
            Catálogo SOV
          </button>
          
          <button @click="handleLogout" class="w-full text-left block text-base font-medium transition-colors px-3 py-2 rounded text-red-400 hover:text-red-300 border-t border-white/5 pt-4 mt-2">
            Cerrar Sesión
          </button>
      </div>
    </div>
  </nav>
  
  <div class="h-[70px] md:h-[80px] w-full bg-bg-main"></div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import api from '../api/axios';

const router = useRouter();
const route = useRoute();
const isAdmin = localStorage.getItem('is_staff') === 'true';
const selfId = ref(null);
const isMenuOpen = ref(false);

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const navigate = (path) => {
  isMenuOpen.value = false;
  router.push(path);
};

const baseDesktop = "text-sm font-medium transition-colors";
const activeDesktop = "text-brand-primary font-bold";
const inactiveDesktop = "text-slate-400 hover:text-brand-primary";

const getDesktopClass = (path) => {
  return route.path === path ? `${baseDesktop} ${activeDesktop}` : `${baseDesktop} ${inactiveDesktop}`;
};

const baseMobile = "block text-base font-medium transition-colors px-3 py-2 rounded text-left w-full";
const activeMobile = "text-brand-primary font-bold bg-white/5";
const inactiveMobile = "text-slate-300 hover:text-brand-primary hover:bg-white/5";

const getMobileClass = (path) => {
  return route.path === path ? `${baseMobile} ${activeMobile}` : `${baseMobile} ${inactiveMobile}`;
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
      if (localStorage.getItem('is_staff') !== 'true') {
        const myProfile = skatersRes.data.find(s => String(s.user) === String(currentUserId));
        if (myProfile) selfId.value = myProfile.id;
      }
    }
  } catch (error) {
    if (error.response && error.response.status === 401) console.warn("Sesión expirada.");
  }
});
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.2s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>