<template>
  <div class="p-4 md:p-8 text-white min-h-screen pb-20">
    <div class="max-w-6xl mx-auto">
      
      <header class="mb-8 flex flex-col md:flex-row justify-between items-start md:items-end gap-6">
        <div>
          <div class="flex items-center gap-2 mb-1">
            <span class="h-2 w-2 rounded-full bg-brand-primary animate-pulse"></span>
            <span class="text-brand-primary text-[10px] md:text-xs font-black uppercase tracking-[0.2em]">Configuración Técnica</span>
          </div>
          <h1 class="text-3xl md:text-4xl font-black tracking-tighter uppercase italic">Catálogo SOV 2026</h1>
          <p class="text-slate-500 text-xs md:text-sm font-medium mt-1">Gestión de valores base y escalas de ejecución.</p>
        </div>
        
        <button v-if="isAdmin" @click="showForm = !showForm" 
                class="w-full md:w-auto btn-primary flex justify-center items-center gap-2 group px-6 py-3">
          <span class="text-xl transition-transform group-hover:rotate-90">{{ showForm ? '×' : '+' }}</span>
          {{ showForm ? 'Cerrar Panel' : 'Añadir Elemento' }}
        </button>
      </header>

      <transition name="fade">
        <div v-if="showForm" class="card-skate mb-10 border-brand-primary/20 bg-slate-900/50 backdrop-blur-xl shadow-2xl">
          <form @submit.prevent="createElement" class="space-y-6 md:space-y-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
              <div class="space-y-1 col-span-2 md:col-span-1">
                <label class="label-style">Tipo</label>
                <select v-model="form.name" required class="input-field font-bold">
                  <option value="Tr">Traveling (Tr)</option>
                  <option value="ASq">Art Seq (ASq)</option>
                  <option value="DSSq">Dance Step Seq (DSSq)</option>
                  <option value="FoSq">Foot Seq (FoSq)</option>
                  <option value="ClSq">Cluster Sequence (ClSq)</option>
                  <option value="ChStS">Choreo Step Seq (ChStS)</option>
                </select>
              </div>
              <div class="space-y-1">
                <label class="label-style">Nivel</label>
                <input v-model.number="form.level" type="number" min="0" max="5" class="input-field font-mono text-center" required>
              </div>
              <div class="space-y-1">
                <label class="label-style text-brand-primary">Base (BV)</label>
                <input v-model="form.base_score" type="number" step="0.01" class="input-field border-brand-primary/30 font-bold text-center" required>
              </div>
              <div class="space-y-1">
                <label class="label-style text-brand-primary">Extra</label>
                <input v-model="form.extra_points" type="number" step="0.01" class="input-field border-brand-primary/30 font-mono text-center" placeholder="0.50">
              </div>
            </div>
            
            <div class="bg-bg-main/50 p-4 md:p-6 rounded-2xl border border-white/5">
              <div class="flex items-center gap-2 mb-4">
                <span class="text-[10px] font-black uppercase text-slate-500 tracking-widest">Escala QOE</span>
              </div>
              <div class="grid grid-cols-3 gap-3 md:gap-6">
                <div class="space-y-1">
                  <label class="label-style text-[10px] text-center block">Q1</label>
                  <input v-model="form.qoe_1" type="number" step="0.01" class="input-field text-center px-1" placeholder="0.00">
                </div>
                <div class="space-y-1">
                  <label class="label-style text-[10px] text-center block">Q2</label>
                  <input v-model="form.qoe_2" type="number" step="0.01" class="input-field text-center px-1" placeholder="0.00">
                </div>
                <div class="space-y-1">
                  <label class="label-style text-[10px] text-center block">Q3</label>
                  <input v-model="form.qoe_3" type="number" step="0.01" class="input-field text-center px-1" placeholder="0.00">
                </div>
              </div>
            </div>

            <div class="flex justify-end pt-2">
              <button type="submit" class="w-full md:w-auto btn-primary px-8 py-3 shadow-lg shadow-brand-primary/20">
                Guardar
              </button>
            </div>
          </form>
        </div>
      </transition>

      <div class="flex flex-col gap-6">
        <div class="relative w-full group">
          <input v-model="searchQuery" type="text" placeholder="Buscar código..."
                 class="input-field pl-10 md:pl-12 h-12 border-white/10 group-hover:border-brand-primary transition-all text-sm md:text-base">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 absolute left-3 md:left-4 top-3.5 text-slate-600 group-hover:text-brand-primary transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>

        <div class="md:hidden grid grid-cols-1 gap-4">
          <div v-for="el in filteredElements" :key="`mobile-${el.id}`" 
               class="bg-slate-800/40 border border-white/5 rounded-xl p-4 active:scale-[0.99] transition-transform">
            
            <div class="flex justify-between items-start mb-4">
              <div>
                 <span class="bg-brand-primary/10 text-brand-primary px-3 py-1 rounded text-sm font-mono font-black border border-brand-primary/20 inline-block mb-1">
                    {{ el.code }}
                 </span>
                 <div class="text-[10px] text-slate-500 uppercase font-bold tracking-wider">SOV TOTAL</div>
              </div>
              <div class="text-right">
                <span class="block text-2xl font-black text-white tracking-tighter leading-none">
                  {{ Number(el.total_score || 0).toFixed(2) }}
                </span>
                <span v-if="Number(el.extra_points) > 0" class="text-[10px] text-green-400 font-mono">
                  +{{ el.extra_points }} Extra
                </span>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-2 mb-4">
              <div class="bg-black/20 rounded p-2 text-center border border-white/5">
                <div class="text-[9px] text-slate-500 uppercase">Base Score</div>
                <div class="font-mono text-slate-300">{{ Number(el.base_score || 0).toFixed(2) }}</div>
              </div>
              <div class="bg-black/20 rounded p-2 flex justify-between items-center px-4 border border-white/5 col-span-2">
                <div class="text-center">
                  <div class="text-[9px] text-slate-500">Q1</div>
                  <div class="font-mono text-xs text-slate-400">{{ el.qoe_1 }}</div>
                </div>
                <div class="h-4 w-px bg-white/10"></div>
                <div class="text-center">
                  <div class="text-[9px] text-slate-500">Q2</div>
                  <div class="font-mono text-xs text-slate-400">{{ el.qoe_2 }}</div>
                </div>
                <div class="h-4 w-px bg-white/10"></div>
                <div class="text-center">
                  <div class="text-[9px] text-slate-500">Q3</div>
                  <div class="font-mono text-xs text-slate-400">{{ el.qoe_3 }}</div>
                </div>
              </div>
            </div>

            <button v-if="isAdmin" @click="deleteElement(el.id)" 
                    class="w-full py-2 bg-red-500/10 text-red-400 rounded-lg text-xs font-bold uppercase tracking-widest hover:bg-red-500/20 transition">
              Eliminar Entrada
            </button>
          </div>
        </div>

        <div class="hidden md:block card-skate !p-0 overflow-hidden shadow-2xl">
          <table class="w-full text-left">
            <thead class="bg-slate-800/50 text-slate-500 text-[10px] uppercase font-black tracking-widest border-b border-white/5">
              <tr>
                <th class="p-5">Código</th>
                <th class="p-5">Base Score</th>
                <th class="p-5">Extra</th>
                <th class="p-5">Total SOV</th>
                <th class="p-5 text-center">Q1</th>
                <th class="p-5 text-center">Q2</th>
                <th class="p-5 text-center">Q3</th>
                <th v-if="isAdmin" class="p-5 text-right">Acción</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-white/5">
              <tr v-for="el in filteredElements" :key="el.id" class="group hover:bg-white/[0.02] transition-all">
                <td class="p-5">
                  <span class="bg-brand-primary/10 text-brand-primary px-3 py-1 rounded-lg font-mono font-black border border-brand-primary/20">
                    {{ el.code }}
                  </span>
                </td>
                <td class="p-5 text-slate-400 font-mono italic">
                  {{ Number(el.base_score || 0).toFixed(2) }}
                </td>
                <td class="p-5 text-slate-500 font-mono">{{ el.extra_points || '0.00' }}</td>
                <td class="p-5">
                  <span class="text-white font-black text-lg tracking-tighter tabular-nums">
                    {{ Number(el.total_score || 0).toFixed(2) }}
                  </span>
                </td>
                <td class="p-5 text-center text-slate-500 font-mono text-sm">{{ el.qoe_1 }}</td>
                <td class="p-5 text-center text-slate-500 font-mono text-sm">{{ el.qoe_2 }}</td>
                <td class="p-5 text-center text-slate-500 font-mono text-sm">{{ el.qoe_3 }}</td>
                <td v-if="isAdmin" class="p-5 text-right">
                  <button @click="deleteElement(el.id)" class="bg-red-500/10 hover:bg-red-500 text-red-500 hover:text-white p-2 rounded-lg transition-all duration-300">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
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

<style scoped>
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease, transform 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; transform: translateY(-10px); }
</style>

<script setup>
import { ref, computed, onMounted } from 'vue';
import api from '../api/axios';

const elements = ref([]);
const showForm = ref(false);
const searchQuery = ref('');

const form = ref({
  name: 'Tr',
  level: 0,
  base_score: 0,
  extra_points: 0,
  qoe_1: 0,
  qoe_2: 0,
  qoe_3: 0
});

const isAdmin = localStorage.getItem('is_staff') === 'true';

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
    form.value = { name: 'Tr', level: 0, base_score: 0, extra_points: 0, qoe_1: 0, qoe_2: 0, qoe_3: 0 };
    showForm.value = false;
    await fetchElements();
  } catch (error) {
    alert("Error al guardar. Verifica que el código sea único (Nivel + Nombre).");
  }
};

const deleteElement = async (id) => {
  if (confirm("¿Estás seguro de eliminar este elemento del catálogo oficial?")) {
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