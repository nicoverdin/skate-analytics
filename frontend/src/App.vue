<template>
  <div class="min-h-screen flex flex-col">
    <Navbar v-if="route.name !== 'Login'" />
    
    <main class="flex-grow">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue';
import { useRoute } from 'vue-router';

const route = useRoute();
</script>