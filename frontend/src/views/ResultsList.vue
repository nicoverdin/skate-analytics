<template>
  <div class="p-8 text-white min-h-screen">
    <div class="max-w-6xl mx-auto">
      <header class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 mb-12">
        <div class="flex items-center gap-4">
          <div class="h-12 w-1.5 bg-brand-primary rounded-full shadow-[0_0_15px_rgba(244,244,245,0.3)]"></div>
          <div>
            <h1 class="text-4xl font-black tracking-tighter uppercase italic">Analytics</h1>
            <p class="text-slate-500 font-medium text-sm">Registro histórico de rendimiento técnico</p>
          </div>
        </div>
        
        <div v-if="isAdmin" class="w-full md:w-72 relative group">
          <label class="absolute -top-2 left-3 bg-bg-main px-2 text-[10px] font-black text-brand-primary uppercase tracking-widest z-10">
            Filtrar Atleta
          </label>
          <div class="relative">
            <select v-model="selectedSkaterId" class="input-field pl-10 h-12 appearance-none cursor-pointer hover:border-brand-primary transition-colors">
              <option value="">Todos los perfiles</option>
              <option v-for="s in skaters" :key="s.id" :value="s.id">
                {{ s.name }}
              </option>
            </select>
            <div class="absolute left-3 top-3.5 text-slate-500 group-hover:text-brand-primary transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
          </div>
        </div>
      </header>

      <div class="card-skate !p-0 overflow-hidden border-white/5 shadow-2xl">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead class="bg-slate-800/50 text-slate-400 text-[10px] uppercase font-black tracking-[0.2em] border-b border-white/5">
              <tr>
                <th v-if="isAdmin" class="p-5">Patinador</th>
                <th class="p-5">Elemento Técnico</th>
                <th class="p-5 text-center">Grado Ejecución (QOE)</th>
                <th class="p-5 text-center">Score Final</th>
                <th class="p-5 text-right">Timestamp</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-white/5">
              <tr v-for="res in filteredResults" :key="res.id" class="group hover:bg-brand-primary/[0.02] transition-all">
                <td v-if="isAdmin" class="p-5">
                  <div class="flex items-center gap-3">
                    <div class="h-8 w-8 rounded-full bg-slate-800 flex items-center justify-center text-[10px] font-bold text-brand-primary border border-white/5">
                      {{ res.skater_details?.name.charAt(0) }}
                    </div>
                    <span class="font-bold text-sm text-slate-200">{{ res.skater_details?.name }}</span>
                  </div>
                </td>
                <td class="p-5">
                  <div class="flex flex-col">
                    <span class="text-brand-primary font-mono font-black text-base">{{ res.element_details?.code }}</span>
                    <span class="text-slate-500 text-[10px] uppercase font-bold tracking-tighter leading-none">{{ res.element_details?.name }}</span>
                  </div>
                </td>
                <td class="p-5 text-center">
                  <div class="inline-flex items-center justify-center h-8 w-12 rounded-lg bg-slate-900 border border-white/5 shadow-inner">
                    <span :class="valColor(res.qoe_given)" class="font-mono font-black">
                      {{ res.qoe_given > 0 ? '+' : '' }}{{ res.qoe_given }}
                    </span>
                  </div>
                </td>
                <td class="p-5 text-center">
                  <span class="text-2xl font-black text-white tracking-tighter tabular-nums">
                    {{ res.total_score.toFixed(2) }}
                  </span>
                </td>
                <td class="p-5 text-right">
                  <div class="flex flex-col items-end">
                    <span class="text-slate-300 font-mono text-sm uppercase">{{ formatDate(res.date).split(',')[0] }}</span>
                    <span class="text-slate-600 text-[10px] font-bold uppercase">{{ formatDate(res.date).split(',')[1] }}</span>
                  </div>
                </td>
              </tr>
              <tr v-if="filteredResults.length === 0">
                <td colspan="5" class="p-20 text-center text-slate-600 italic font-medium">
                  No se han encontrado registros técnicos para este filtro.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
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
  try {
    const [resResults, resSkaters] = await Promise.all([
      api.get('/api/results/'),
      isAdmin ? api.get('/api/skaters/') : Promise.resolve({ data: [] })
    ]);
    results.value = resResults.data;
    skaters.value = resSkaters.data;
  } catch (error) {
    console.error("Error cargando historial:", error);
  }
};

const filteredResults = computed(() => {
  if (!selectedSkaterId.value) return results.value;
  return results.value.filter(r => r.skater === parseInt(selectedSkaterId.value));
});

const valColor = (val) => {
  if (val > 0) return 'text-green-400 drop-shadow-[0_0_8px_rgba(74,222,128,0.3)]';
  if (val < 0) return 'text-red-400 drop-shadow-[0_0_8px_rgba(248,113,113,0.3)]';
  return 'text-slate-500';
};

const formatDate = (d) => new Date(d).toLocaleString('es-ES', { 
  day: '2-digit', month: '2-digit', year: '2-digit', hour: '2-digit', minute: '2-digit' 
});

onMounted(fetchInitialData);
</script>