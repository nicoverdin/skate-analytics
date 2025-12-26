<template>
  <div class="p-4 md:p-8 text-white min-h-screen pb-20">
    <div class="max-w-6xl mx-auto">
      
      <header class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 mb-8 md:mb-12">
        <div class="flex items-center gap-4">
          <div class="h-10 w-1 md:h-12 md:w-1.5 bg-brand-primary rounded-full shadow-[0_0_15px_rgba(244,244,245,0.3)]"></div>
          <div>
            <h1 class="text-3xl md:text-4xl font-black tracking-tighter uppercase italic">Analytics</h1>
            <p class="text-slate-500 font-medium text-xs md:text-sm">Registro histórico de rendimiento</p>
          </div>
        </div>
        
        <div v-if="isAdmin" class="w-full md:w-72 relative group">
          <label class="absolute -top-2 left-3 bg-bg-main px-2 text-[10px] font-black text-brand-primary uppercase tracking-widest z-10">
            Filtrar Atleta
          </label>
          <div class="relative">
            <select v-model="selectedSkaterId" class="input-field pl-10 h-12 appearance-none cursor-pointer hover:border-brand-primary transition-colors text-sm">
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

      <div class="md:hidden space-y-4">
        <div v-for="res in filteredResults" :key="`mob-${res.id}`" 
             class="bg-slate-800/40 border border-white/5 rounded-xl p-5 relative overflow-hidden">
          
          <div class="flex justify-between items-start mb-3 text-[10px] uppercase font-bold tracking-wider text-slate-500">
            <span>{{ formatDate(res.date) }}</span>
            <span v-if="isAdmin && res.skater_details" class="text-brand-primary bg-brand-primary/10 px-2 py-0.5 rounded border border-brand-primary/20">
              {{ res.skater_details.name }}
            </span>
          </div>

          <div class="flex justify-between items-center mb-4">
            <div>
              <span class="text-2xl font-black text-white italic tracking-tighter block leading-none mb-1">
                {{ res.element_details?.code }}
              </span>
              <span class="text-xs text-slate-400 font-medium block">
                {{ res.element_details?.name }}
              </span>
            </div>
            <div class="text-right">
              <span class="block text-3xl font-black text-white tracking-tighter tabular-nums text-shadow-glow">
                {{ res.total_score.toFixed(2) }}
              </span>
              <span class="text-[10px] text-slate-500 uppercase">Total Points</span>
            </div>
          </div>

          <div class="flex justify-between items-center pt-3 border-t border-white/5">
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-bold text-slate-500 uppercase">QOE:</span>
              <span :class="valColor(res.qoe_given)" class="text-sm font-mono font-black bg-slate-900 px-2 py-0.5 rounded border border-white/5">
                 {{ res.qoe_given > 0 ? '+' : '' }}{{ res.qoe_given }}
              </span>
            </div>

            <button v-if="isAdmin" @click="deleteResult(res.id)" 
                    class="text-red-400 bg-red-500/10 px-3 py-1.5 rounded-lg text-xs font-bold uppercase hover:bg-red-500 hover:text-white transition-colors">
              Eliminar
            </button>
          </div>
        </div>

        <div v-if="filteredResults.length === 0" class="text-center p-10 text-slate-500 text-sm italic">
          No hay registros para mostrar.
        </div>
      </div>

      <div class="hidden md:block card-skate !p-0 overflow-hidden border-white/5 shadow-2xl">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead class="bg-slate-800/50 text-slate-400 text-[10px] uppercase font-black tracking-[0.2em] border-b border-white/5">
              <tr>
                <th v-if="isAdmin" class="p-5">Patinador</th>
                <th class="p-5">Elemento Técnico</th>
                <th class="p-5 text-center">Grado Ejecución (QOE)</th>
                <th class="p-5 text-center">Score Final</th>
                <th class="p-5 text-right">Timestamp</th>
                <th v-if="isAdmin" class="p-5 text-right">Acción</th>
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
                <td v-if="isAdmin" class="p-5 text-right">
                  <button 
                    @click="deleteResult(res.id)" 
                    class="bg-red-500/10 hover:bg-red-500 text-red-500 hover:text-white p-2 rounded-lg transition-all duration-300 group/del"
                    title="Eliminar registro"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                    </svg>
                  </button>
                </td>
              </tr>
              <tr v-if="filteredResults.length === 0">
                <td :colspan="isAdmin ? 6 : 4" class="p-20 text-center text-slate-600 italic font-medium">
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

<style scoped>
.text-shadow-glow {
  text-shadow: 0 0 20px rgba(255,255,255,0.1);
}
</style>

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

const deleteResult = async (id) => {
  if (!confirm('¿Estás seguro de que deseas eliminar este registro técnico? Esta acción es irreversible.')) {
    return;
  }

  try {
    await api.delete(`/api/results/${id}/`);
    results.value = results.value.filter(r => r.id !== id);
  } catch (error) {
    console.error("Error al eliminar el resultado:", error);
    alert("Hubo un error al intentar eliminar el registro.");
  }
};

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