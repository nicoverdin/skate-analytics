<template>
  <div class="p-4 md:p-8 min-h-screen pb-20">
    <div class="max-w-6xl mx-auto">
      
      <header class="flex flex-col md:flex-row justify-between items-start md:items-end gap-6 mb-8">
        <div>
          <div class="flex items-center gap-2 mb-1">
            <span class="h-2 w-2 rounded-full bg-brand-primary animate-pulse"></span>
            <span class="text-brand-primary text-[10px] md:text-xs font-black uppercase tracking-[0.2em]">Base de Datos</span>
          </div>
          <h1 class="text-3xl md:text-4xl font-black tracking-tighter uppercase italic text-white">Historial Técnico</h1>
          <p class="text-slate-500 text-xs md:text-sm font-medium mt-1">Registro completo de evaluaciones.</p>
        </div>
        
        <div v-if="isAdmin" class="w-full md:w-72 relative group">
          <label class="absolute -top-2.5 left-3 bg-bg-main px-2 text-[10px] font-black text-brand-primary uppercase tracking-widest z-10">
            Filtrar por Atleta
          </label>
          <div class="relative">
            <select v-model="selectedSkaterId" class="w-full bg-slate-900/80 border border-white/10 rounded-xl h-12 pl-4 pr-10 text-sm font-bold text-white focus:border-brand-primary focus:ring-1 focus:ring-brand-primary outline-none appearance-none transition-all cursor-pointer hover:border-white/20">
              <option value="">Ver todos los perfiles</option>
              <option v-for="s in skaters" :key="s.id" :value="s.id">
                {{ s.name }}
              </option>
            </select>
            <div class="absolute right-4 top-3.5 text-slate-500 pointer-events-none group-hover:text-brand-primary transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </div>
          </div>
        </div>
      </header>

      <div class="md:hidden space-y-4">
        <div v-for="res in filteredResults" :key="`mob-${res.id}`" 
             class="bg-slate-800 border border-white/5 rounded-2xl p-5 relative overflow-hidden shadow-sm group">
          
          <div class="absolute left-0 top-0 bottom-0 w-1.5" :class="res.qoe_given >= 0 ? 'bg-green-500/50' : 'bg-red-500/50'"></div>

          <div class="flex justify-between items-start mb-4 pl-3">
            <div>
              <div class="text-[10px] font-bold uppercase tracking-wider text-slate-500 mb-1 flex items-center gap-2">
                {{ formatDate(res.date) }}
                <button v-if="isAdmin && res.skater_details" 
                        @click.stop="goToSkater(res.skater)"
                        class="text-brand-primary bg-brand-primary/10 px-2 py-0.5 rounded border border-brand-primary/20 hover:bg-brand-primary hover:text-bg-main transition-colors">
                  {{ res.skater_details.name }}
                </button>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-2xl font-black text-white italic tracking-tighter leading-none">
                  {{ res.element_details?.code }}
                </span>
                <span class="text-xs text-slate-400 font-medium">
                  {{ res.element_details?.name }}
                </span>
              </div>
            </div>
            
            <div class="text-right">
              <span class="block text-3xl font-black text-white tracking-tighter tabular-nums drop-shadow-lg">
                {{ Number(res.total_score).toFixed(2) }}
              </span>
              <span class="text-[9px] text-slate-500 uppercase font-bold tracking-wider">Puntos</span>
            </div>
          </div>

          <div class="flex justify-between items-center pt-3 border-t border-white/5 pl-3">
            <div class="flex items-center gap-2 bg-slate-900/50 px-3 py-1.5 rounded-lg border border-white/5">
              <span class="text-[10px] font-bold text-slate-500 uppercase">QOE</span>
              <span :class="valColor(res.qoe_given)" class="text-sm font-mono font-black">
                 {{ res.qoe_given > 0 ? '+' : '' }}{{ res.qoe_given }}
              </span>
            </div>

            <button v-if="isAdmin" @click="deleteResult(res.id)" 
                    class="text-slate-500 hover:text-red-400 p-2 transition-colors active:scale-95">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
        </div>

        <div v-if="filteredResults.length === 0" class="text-center p-12 bg-slate-800/20 rounded-2xl border border-white/5 border-dashed">
          <p class="text-slate-500 text-sm italic">No hay registros con estos filtros.</p>
        </div>
      </div>

      <div class="hidden md:block bg-slate-800 rounded-2xl border border-white/5 overflow-hidden shadow-xl">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead class="bg-black/20 text-slate-400 text-[10px] uppercase font-black tracking-widest border-b border-white/5">
              <tr>
                <th v-if="isAdmin" class="p-5">Patinador</th>
                <th class="p-5">Elemento</th>
                <th class="p-5 text-center">Ejecución (QOE)</th>
                <th class="p-5 text-center">Score</th>
                <th class="p-5 text-right">Fecha</th>
                <th v-if="isAdmin" class="p-5 text-right">Acción</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-white/5">
              <tr v-for="res in filteredResults" :key="res.id" class="group hover:bg-white/[0.02] transition-colors">
                
                <td v-if="isAdmin" class="p-5">
                  <div @click="goToSkater(res.skater)" class="flex items-center gap-3 cursor-pointer group/skater">
                    <div class="h-8 w-8 rounded-full bg-slate-700 flex items-center justify-center text-[10px] font-bold text-brand-primary border border-white/5 group-hover/skater:border-brand-primary transition-colors">
                      {{ res.skater_details?.name.charAt(0) }}
                    </div>
                    <span class="font-bold text-sm text-slate-200 group-hover/skater:text-brand-primary transition-colors">
                      {{ res.skater_details?.name }}
                    </span>
                  </div>
                </td>

                <td class="p-5">
                  <div class="flex flex-col">
                    <span class="text-white font-black text-lg tracking-tight">{{ res.element_details?.code }}</span>
                    <span class="text-slate-500 text-[10px] uppercase font-bold tracking-tight">{{ res.element_details?.name }}</span>
                  </div>
                </td>

                <td class="p-5 text-center">
                  <span :class="valColor(res.qoe_given)" class="font-mono font-black text-lg">
                    {{ res.qoe_given > 0 ? '+' : '' }}{{ res.qoe_given }}
                  </span>
                </td>

                <td class="p-5 text-center">
                  <span class="text-2xl font-black text-white tracking-tighter tabular-nums">
                    {{ Number(res.total_score).toFixed(2) }}
                  </span>
                </td>

                <td class="p-5 text-right">
                  <div class="flex flex-col items-end">
                    <span class="text-slate-300 font-mono text-xs uppercase">{{ formatDate(res.date).split(',')[0] }}</span>
                    <span class="text-slate-600 text-[10px] font-bold uppercase">{{ formatDate(res.date).split(',')[1] }}</span>
                  </div>
                </td>

                <td v-if="isAdmin" class="p-5 text-right">
                  <button 
                    @click="deleteResult(res.id)" 
                    class="text-slate-500 hover:text-red-500 p-2 transition-colors duration-300"
                    title="Eliminar registro"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                    </svg>
                  </button>
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
import { useRouter } from 'vue-router';
import api from '../api/axios';

const router = useRouter();
const results = ref([]);
const skaters = ref([]);
const selectedSkaterId = ref('');
const isAdmin = localStorage.getItem('is_staff') === 'true';

const goToSkater = (id) => {
  if (id) {
    router.push(`/skaters/${id}`);
  }
};

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
  if (!confirm('¿Eliminar este registro permanentemente?')) return;

  try {
    await api.delete(`/api/results/${id}/`);
    results.value = results.value.filter(r => r.id !== id);
  } catch (error) {
    console.error("Error al eliminar:", error);
    alert("Hubo un error al eliminar.");
  }
};

const valColor = (val) => {
  if (val > 0) return 'text-green-400 drop-shadow-sm';
  if (val < 0) return 'text-red-400 drop-shadow-sm';
  return 'text-slate-500';
};

const formatDate = (d) => new Date(d).toLocaleString('es-ES', { 
  day: '2-digit', month: '2-digit', year: '2-digit', hour: '2-digit', minute: '2-digit' 
});

onMounted(fetchInitialData);
</script>