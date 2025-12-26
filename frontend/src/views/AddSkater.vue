<template>
  <div class="p-4 md:p-8">
    <div class="max-w-2xl mx-auto">
      
      <header class="mb-6 md:mb-8">
        <button 
          @click="goBack" 
          class="text-brand-primary text-sm hover:underline flex items-center mb-4 bg-transparent border-none p-0 cursor-pointer"
        >
          ← Volver a la lista
        </button>
        <h1 class="text-2xl md:text-3xl font-bold text-white">Añadir Nuevo Patinador</h1>
      </header>

      <div class="card-skate">
        <form @submit.prevent="handleSubmit" class="space-y-5 md:space-y-6">
          <div>
            <label class="block text-sm font-medium text-slate-300 mb-1">Nombre Completo</label>
            <input v-model="form.name" type="text" required class="input-field" placeholder="Ej: Jane Doe">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-300 mb-1">Nombre de Usuario (Login)</label>
            <input v-model="form.username" type="text" required class="input-field" placeholder="ej: janeskate99">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-300 mb-1">Contraseña Temporal</label>
            <input v-model="form.password" type="password" required class="input-field" placeholder="••••••••">
            <p class="text-xs text-slate-500 mt-1">Dale esta clave al patinador para su primer acceso.</p>
          </div>
          
          <div v-if="error" class="bg-red-500/10 border border-red-500/20 text-red-400 text-sm p-3 rounded-lg">
            {{ error }}
          </div>

          <div class="flex gap-3 md:gap-4 pt-4">
            <button type="submit" :disabled="loading" class="btn-primary flex-grow justify-center">
              {{ loading ? 'Guardando...' : 'Guardar Patinador' }}
            </button>
            
            <button 
              type="button" 
              @click="goBack" 
              class="px-4 md:px-6 py-2 border border-border-soft rounded-lg text-slate-400 hover:bg-white/5 transition text-sm md:text-base"
            >
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import api from '../api/axios';

const router = useRouter();
const loading = ref(false);
const error = ref(null);

const form = ref({
  name: '',
  username: '',
  password: ''
});

const goBack = () => {
  router.push('/skaters');
};

const handleSubmit = async () => {
  loading.value = true;
  error.value = null;
  try {
    await api.post('/api/skaters/', form.value);
    router.push('/skaters');
  } catch (err) {
    error.value = "Hubo un error al guardar. Revisa los datos.";
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>