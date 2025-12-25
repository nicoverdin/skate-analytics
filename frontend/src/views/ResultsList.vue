<template>
  <div class="p-8 text-white">
    <div class="max-w-6xl mx-auto">
      <header class="flex justify-between items-end mb-8">
        <div>
          <h1 class="text-3xl font-bold mb-2">Historial de Resultados</h1>
          <p class="text-slate-400">Consulta y filtra el rendimiento técnico</p>
        </div>
        
        <div v-if="isAdmin" class="w-64">
          <label class="block text-xs font-semibold text-slate-500 uppercase mb-1">Filtrar por Patinador</label>
          <select v-model="selectedSkaterId" class="input-field">
            <option value="">Todos los patinadores</option>
            <option v-for="s in skaters" :key="s.id" :value="s.id">
              {{ s.name }}
            </option>
          </select>
        </div>
      </header>

      <div class="card-skate overflow-hidden">
        <table class="w-full text-left">
          <thead class="bg-bg-main text-slate-500 text-xs uppercase tracking-wider">
            <tr>
              <th v-if="isAdmin" class="p-4">Patinador</th>
              <th class="p-4">Elemento</th>
              <th class="p-4 text-center">QOE</th>
              <th class="p-4 text-center">Puntos</th>
              <th class="p-4">Fecha</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/5">
            <tr v-for="res in filteredResults" :key="res.id" class="hover:bg-white/5 transition">
              <td v-if="isAdmin" class="p-4 font-medium">{{ res.skater_details?.name }}</td>
              <td class="p-4">
                <span class="text-brand-primary font-mono font-bold">{{ res.element_details?.code }}</span>
                <span class="ml-2 text-slate-500 text-sm">{{ res.element_details?.name }}</span>
              </td>
              <td class="p-4 text-center">
                <span :class="valColor(res.qoe_given)" class="font-bold">
                  {{ res.qoe_given > 0 ? '+' : '' }}{{ res.qoe_given }}
                </span>
              </td>
              <td class="p-4 text-center font-mono font-bold text-lg">{{ res.total_score }}</td>
              <td class="p-4 text-slate-500 text-sm">{{ formatDate(res.date_created) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import api from '../api/axios';

const results = ref([]);
const skaters = ref([]);
const selectedSkaterId = ref('');
const isAdmin = localStorage.getItem('is_staff') === 'true';

const fetchInitialData = async () => {
  const [resResults, resSkaters] = await Promise.all([
    api.get('/api/results/'),
    isAdmin ? api.get('/api/skaters/') : Promise.resolve({ data: [] })
  ]);
  results.value = resResults.data;
  skaters.value = resSkaters.data;
};

// Lógica de filtrado reactivo
const filteredResults = computed(() => {
  if (!selectedSkaterId.value) return results.value;
  return results.value.filter(r => r.skater === parseInt(selectedSkaterId.value));
});

const valColor = (val) => {
  if (val > 0) return 'text-green-400';
  if (val < 0) return 'text-red-400';
  return 'text-slate-500';
};

const formatDate = (d) => new Date(d).toLocaleDateString('es-ES', { 
  day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' 
});

onMounted(fetchInitialData);
</script>