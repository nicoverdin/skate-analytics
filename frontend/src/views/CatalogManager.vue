<template>
  <div class="p-4 md:p-8 text-white min-h-screen pb-20">
    <div class="max-w-6xl mx-auto">
      
      <header class="mb-6 md:mb-8 flex flex-col md:flex-row justify-between items-start md:items-end gap-4 md:gap-6">
        <div class="w-full md:w-auto">
          <div class="flex items-center gap-2 mb-1">
            <span class="h-2 w-2 rounded-full bg-brand-primary animate-pulse"></span>
            <span class="text-brand-primary text-[10px] md:text-xs font-black uppercase tracking-[0.2em]">Configuración Técnica</span>
          </div>
          <h1 class="text-3xl md:text-4xl font-black tracking-tighter uppercase italic">Catálogo SOV</h1>
          <p class="text-slate-500 text-xs md:text-sm font-medium mt-1">Base de datos de elementos y puntuaciones.</p>
        </div>
        
        <button v-if="isAdmin" @click="showForm = !showForm" 
                class="w-full md:w-auto btn-primary flex justify-center items-center gap-2 group px-6 py-3 shadow-lg shadow-brand-primary/10">
          <span class="text-xl font-bold transition-transform duration-300" :class="{ 'rotate-45': showForm }">+</span>
          {{ showForm ? 'Cerrar Panel' : 'Añadir Elemento' }}
        </button>
      </header>

      <transition name="slide-fade">
        <div v-if="showForm" class="mb-8 bg-slate-800/80 backdrop-blur-md border border-brand-primary/30 rounded-2xl p-4 md:p-6 shadow-2xl relative overflow-hidden">
          <div class="absolute top-0 right-0 w-64 h-64 bg-brand-primary/5 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2 pointer-events-none"></div>

          <h2 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-brand-primary" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z" clip-rule="evenodd" />
            </svg>
            Nuevo Elemento Técnico
          </h2>

          <form @submit.prevent="createElement" class="space-y-4 md:space-y-6 relative z-10">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
              <div class="col-span-2 md:col-span-1 space-y-1">
                <label class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Tipo</label>
                <div class="relative">
                  <select v-model="form.name" required class="w-full bg-slate-900/80 border border-white/10 rounded-lg h-10 px-3 text-sm font-bold focus:border-brand-primary focus:ring-1 focus:ring-brand-primary outline-none appearance-none">
                    <option value="Tr">Traveling (Tr)</option>
                    <option value="ASq">Art Seq (ASq)</option>
                    <option value="DSSq">Dance Step (DSSq)</option>
                    <option value="FoSq">Foot Seq (FoSq)</option>
                    <option value="ClSq">Cluster (ClSq)</option>
                    <option value="ChStS">Choreo Step (ChStS)</option>
                  </select>
                  <div class="absolute right-3 top-2.5 pointer-events-none text-slate-500">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                  </div>
                </div>
              </div>
              <div class="space-y-1">
                <label class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Nivel</label>
                <input v-model.number="form.level" type="number" min="0" max="6" class="input-modern text-center font-mono" required placeholder="0-6">
              </div>
              <div class="space-y-1">
                <label class="text-[10px] uppercase font-bold text-brand-primary tracking-wider">Base (BV)</label>
                <input v-model="form.base_score" type="number" step="0.01" class="input-modern text-center font-bold text-brand-primary border-brand-primary/30 focus:border-brand-primary" required>
              </div>
              <div class="space-y-1">
                <label class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Extra</label>
                <input v-model="form.extra_points" type="number" step="0.01" class="input-modern text-center font-mono text-slate-300" placeholder="0.00">
              </div>
            </div>
            
            <div class="bg-black/20 rounded-xl p-4 border border-white/5">
              <label class="text-[10px] uppercase font-bold text-slate-500 tracking-widest mb-3 block">Escala de Ejecución (QOE)</label>
              <div class="grid grid-cols-3 gap-4">
                <div class="space-y-1">
                  <span class="block text-center text-xs font-mono text-slate-400 mb-1">Q1</span>
                  <input v-model="form.qoe_1" type="number" step="0.01" class="input-modern text-center bg-slate-900" placeholder="0.00">
                </div>
                <div class="space-y-1">
                  <span class="block text-center text-xs font-mono text-slate-400 mb-1">Q2</span>
                  <input v-model="form.qoe_2" type="number" step="0.01" class="input-modern text-center bg-slate-900" placeholder="0.00">
                </div>
                <div class="space-y-1">
                  <span class="block text-center text-xs font-mono text-slate-400 mb-1">Q3</span>
                  <input v-model="form.qoe_3" type="number" step="0.01" class="input-modern text-center bg-slate-900" placeholder="0.00">
                </div>
              </div>
            </div>

            <button type="submit" class="w-full btn-primary py-3 font-bold uppercase tracking-widest text-sm shadow-lg hover:shadow-brand-primary/20 transition-all">
              Guardar en Catálogo
            </button>
          </form>
        </div>
      </transition>

      <div class="flex flex-col gap-6">
        <div class="relative w-full group">
          <input v-model="searchQuery" type="text" placeholder="Buscar por código (ej: Tr Level 1)..."
                 class="w-full bg-slate-800/50 border border-white/10 rounded-xl pl-12 h-12 text-sm text-white placeholder-slate-500 focus:border-brand-primary focus:ring-1 focus:ring-brand-primary transition-all outline-none">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 absolute left-4 top-3.5 text-slate-500 group-focus-within:text-brand-primary transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>

        <div class="md:hidden grid grid-cols-1 gap-3">
          <div v-for="el in filteredElements" :key="`mobile-${el.id}`" 
               class="bg-slate-800 border border-white/5 rounded-2xl p-4 shadow-sm relative overflow-hidden group">
            
            <div class="absolute left-0 top-0 bottom-0 w-1" :class="getLevelColor(el.level)"></div>

            <div class="flex justify-between items-start mb-3 pl-2">
              <div>
                 <div class="flex items-center gap-2">
                   <span class="text-xl font-black text-white tracking-tight">{{ el.code }}</span>
                   <span v-if="Number(el.extra_points) > 0" class="px-1.5 py-0.5 rounded text-[10px] font-bold bg-green-500/20 text-green-400 border border-green-500/30">
                     +{{ el.extra_points }}
                   </span>
                 </div>
                 <span class="text-[10px] text-slate-400 font-medium uppercase tracking-wide">Base: {{ Number(el.base_score).toFixed(2) }}</span>
              </div>
              
              <div class="text-right">
                <span class="block text-3xl font-black text-white tracking-tighter leading-none drop-shadow-lg">
                  {{ Number(el.total_score || 0).toFixed(2) }}
                </span>
                <span class="text-[9px] text-brand-primary font-bold uppercase tracking-wider">Valor SOV</span>
              </div>
            </div>

            <div class="grid grid-cols-3 gap-px bg-white/5 rounded-lg overflow-hidden border border-white/5 ml-2">
              <div class="p-1.5 text-center bg-slate-900/50">
                <div class="text-[8px] text-slate-500 uppercase font-bold">Q1</div>
                <div class="text-xs font-mono font-bold text-slate-300">{{ el.qoe_1 }}</div>
              </div>
              <div class="p-1.5 text-center bg-slate-900/50">
                <div class="text-[8px] text-slate-500 uppercase font-bold">Q2</div>
                <div class="text-xs font-mono font-bold text-slate-300">{{ el.qoe_2 }}</div>
              </div>
              <div class="p-1.5 text-center bg-slate-900/50">
                <div class="text-[8px] text-slate-500 uppercase font-bold">Q3</div>
                <div class="text-xs font-mono font-bold text-slate-300">{{ el.qoe_3 }}</div>
              </div>
            </div>

            <button v-if="isAdmin" @click="deleteElement(el.id)" 
                    class="absolute top-4 right-4 text-slate-600 hover:text-red-500 transition-colors p-2 -mr-2 -mt-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
        </div>

        <div class="hidden md:block bg-slate-800 rounded-2xl border border-white/5 overflow-hidden shadow-xl">
          <table class="w-full text-left border-collapse">
            <thead class="bg-black/20 text-slate-400 text-[10px] uppercase font-black tracking-widest border-b border-white/5">
              <tr>
                <th class="p-5">Código</th>
                <th class="p-5">Nivel</th>
                <th class="p-5">Base (BV)</th>
                <th class="p-5">Extra</th>
                <th class="p-5 text-right">Total SOV</th>
                <th class="p-5 text-center bg-white/[0.02]">Q1</th>
                <th class="p-5 text-center bg-white/[0.02]">Q2</th>
                <th class="p-5 text-center bg-white/[0.02]">Q3</th>
                <th v-if="isAdmin" class="p-5 text-right">Acciones</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-white/5">
              <tr v-for="el in filteredElements" :key="el.id" class="group hover:bg-white/[0.02] transition-colors">
                <td class="p-5">
                  <span class="font-bold text-white text-lg">{{ el.code }}</span>
                  <div class="text-xs text-slate-500">{{ el.name }}</div>
                </td>
                <td class="p-5">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded bg-slate-700 text-xs font-bold text-white">
                    {{ el.level }}
                  </span>
                </td>
                <td class="p-5 font-mono text-slate-300">{{ Number(el.base_score).toFixed(2) }}</td>
                <td class="p-5 font-mono text-slate-500">
                    <span v-if="Number(el.extra_points) > 0" class="text-green-400">+{{ el.extra_points }}</span>
                    <span v-else>--</span>
                </td>
                <td class="p-5 text-right">
                  <span class="text-xl font-black text-brand-primary tracking-tight">{{ Number(el.total_score).toFixed(2) }}</span>
                </td>
                <td class="p-5 text-center font-mono text-sm bg-white/[0.01]">{{ el.qoe_1 }}</td>
                <td class="p-5 text-center font-mono text-sm bg-white/[0.01]">{{ el.qoe_2 }}</td>
                <td class="p-5 text-center font-mono text-sm bg-white/[0.01]">{{ el.qoe_3 }}</td>
                <td v-if="isAdmin" class="p-5 text-right">
                  <button @click="deleteElement(el.id)" class="text-slate-500 hover:text-red-500 transition-colors p-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                    </svg>
                  </button>
                </td>
              </tr>
              <tr v-if="filteredElements.length === 0">
                <td :colspan="isAdmin ? 9 : 8" class="p-12 text-center text-slate-500 italic">
                  No se encontraron elementos que coincidan con tu búsqueda.
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
.input-modern {
  @apply w-full bg-slate-900/80 border border-white/10 rounded-lg h-10 px-3 text-sm text-white placeholder-slate-600 focus:border-brand-primary focus:ring-1 focus:ring-brand-primary outline-none transition-all;
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}
.slide-fade-leave-active {
  transition: all 0.2s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}
</style>

<script setup>
import { ref, computed, onMounted } from 'vue';
import api from '../api/axios';

const elements = ref([]);
const showForm = ref(false);
const searchQuery = ref('');
const isAdmin = localStorage.getItem('is_staff') === 'true';

const form = ref({
  name: 'Tr',
  level: 0,
  base_score: 0,
  extra_points: 0,
  qoe_1: 0,
  qoe_2: 0,
  qoe_3: 0
});

// Helper for UI colors
const getLevelColor = (level) => {
    if (level >= 4) return 'bg-brand-primary';
    if (level >= 2) return 'bg-blue-400';
    return 'bg-slate-500';
};

const filteredElements = computed(() => {
  const query = searchQuery.value.toLowerCase().trim();
  if (!query) return elements.value;
  return elements.value.filter(el => el.code.toLowerCase().includes(query) || el.name.toLowerCase().includes(query));
});

const fetchElements = async () => {
  try {
    const res = await api.get('/api/elements/');
    elements.value = res.data;
  } catch (error) {
    console.error("Error fetching elements:", error);
  }
};

const createElement = async () => {
  try {
    await api.post('/api/elements/', form.value);
    const lastType = form.value.name;
    form.value = { name: lastType, level: 0, base_score: 0, extra_points: 0, qoe_1: 0, qoe_2: 0, qoe_3: 0 };
    await fetchElements();
    alert("¡Elemento añadido!"); 
  } catch (error) {
    alert("Error al guardar. Revisa la consola.");
    console.error(error);
  }
};

const deleteElement = async (id) => {
  if (confirm("¿Estás seguro de eliminar este elemento?")) {
    try {
      await api.delete(`/api/elements/${id}/`);
      await fetchElements();
    } catch (error) {
      console.error("Error al borrar:", error);
    }
  }
};

onMounted(fetchElements);
</script>