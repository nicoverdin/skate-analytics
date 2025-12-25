<template>
  <div class="p-8">
    <div class="max-w-6xl mx-auto">
      <header class="mb-8 flex justify-between items-center">
        <div>
          <h1 class="text-3xl font-bold text-white">
            {{ isAdmin ? 'Historial Global' : 'Mis Resultados' }}
          </h1>
          <p class="text-slate-400">Seguimiento de rendimiento Rollart 2026</p>
        </div>
        <router-link to="/results/add" class="btn-primary">
          + Nuevo Registro
        </router-link>
      </header>

      <div class="card-skate overflow-x-auto">
        <table class="w-full text-left">
          <thead class="text-slate-500 text-sm uppercase tracking-wider border-b border-border-soft">
            <tr>
              <th v-if="isAdmin" class="p-4">Patinador</th>
              <th class="p-4">Elemento</th>
              <th class="p-4 text-center">QOE</th>
              <th class="p-4 text-center">Total</th>
              <th class="p-4">Fecha</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/5">
            <tr v-for="res in results" :key="res.id" class="hover:bg-white/5 transition">
              <td v-if="isAdmin" class="p-4 text-white font-medium">
                {{ res.skater_details?.name }}
              </td>
              <td class="p-4">
                <div class="flex flex-col">
                  <span class="text-brand-primary font-mono font-bold">{{ res.element_details?.code }}</span>
                  <span class="text-xs text-slate-500">{{ res.element_details?.name }}</span>
                </div>
              </td>
              <td class="p-4 text-center">
                <span :class="qoeColor(res.score_given)" class="font-bold">
                  {{ res.score_given > 0 ? '+' : '' }}{{ res.qoe_given }}
                </span>
              </td>
              <td class="p-4 text-center text-white font-mono font-bold">
                {{ res.total_score }}
              </td>
              <td class="p-4 text-slate-500 text-sm">
                {{ formatDate(res.date_created) }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '../api/axios';

const results = ref([]);
const isAdmin = localStorage.getItem('is_staff') === 'true';

const fetchResults = async () => {
  const res = await api.get('/api/results/');
  results.value = res.data;
};

const qoeColor = (val) => {
  if (val > 0) return 'text-green-400';
  if (val < 0) return 'text-red-400';
  return 'text-slate-400';
};

const formatDate = (dateStr) => {
  return new Date(dateStr).toLocaleDateString('es-ES', {
    day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit'
  });
};

onMounted(fetchResults);
</script>