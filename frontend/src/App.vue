<template>
  <div class="h-[100dvh] w-full flex flex-col overflow-hidden bg-bg-main relative">
    
    <Navbar v-if="route.name !== 'Login'" class="flex-none z-50" />
    
    <main class="flex-grow overflow-y-auto overflow-x-hidden scroll-smooth">
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
main {
  -webkit-overflow-scrolling: touch;
}
</style>