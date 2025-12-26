<template>
  <div class="h-full w-full flex flex-col overflow-hidden bg-bg-main relative">
    
    <Navbar v-if="route.name !== 'Login'" class="flex-none z-50" />
    
    <main class="flex-grow overflow-y-auto overflow-x-hidden scroll-smooth pb-0">
      
      <div class="w-full" style="height: calc(80px + env(safe-area-inset-top));"></div>
      
      <router-view />
      
      </main>
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue';
import { useRoute } from 'vue-router';

const route = useRoute();
</script>

<style>
/* Scroll nativo de iOS */
main {
  -webkit-overflow-scrolling: touch;
}
</style>
