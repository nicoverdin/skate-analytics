<template>
  <div class="p-8 text-white min-h-screen">
    <div class="max-w-6xl mx-auto">
      <header class="mb-10 flex flex-col md:flex-row justify-between items-start md:items-end gap-6">
        <div>
          <div class="flex items-center gap-2 mb-1">
            <span class="h-2 w-2 rounded-full bg-brand-primary animate-pulse"></span>
            <span class="text-brand-primary text-xs font-black uppercase tracking-[0.2em]">Configuración Técnica</span>
          </div>
          <h1 class="text-4xl font-black tracking-tighter uppercase italic">Catálogo SOV 2026</h1>
          <p class="text-slate-500 text-sm font-medium">Gestión de valores base y escalas de ejecución Rollart.</p>
        </div>
        <button v-if="isAdmin" @click="showForm = !showForm" 
                class="btn-primary flex items-center gap-2 group px-8">
          <span class="text-xl transition-transform group-hover:rotate-90">{{ showForm ? '×' : '+' }}</span>
          {{ showForm ? 'Cerrar Panel' : 'Añadir Elemento' }}
        </button>
      </header>

      <transition name="fade">
        <div v-if="showForm" class="card-skate mb-10 border-brand-primary/20 bg-slate-900/50 backdrop-blur-xl shadow-2xl">
          <form @submit.prevent="createElement" class="space-y-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
              <div class="space-y-1">
                <label class="label-style">Tipo de Elemento</label>
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
                <label class="label-style">Nivel (0-5)</label>
                <input v-model.number="form.level" type="number" min="0" max="5" class="input-field font-mono" required>
              </div>
              <div class="space-y-1">
                <label class="label-style text-brand-primary">Valor Base (BV)</label>
                <input v-model="form.base_score" type="number" step="0.01" class="input-field border-brand-primary/30 font-bold" required>
              </div>
              <div class="space-y-1">
                <label class="label-style text-brand-primary">Extra Points</label>
                <input v-model="form.extra_points" type="number" step="0.01" class="input-field border-brand-primary/30 font-mono" placeholder="0.50">
              </div>
            </div>
            
            <div class="bg-bg-main/50 p-6 rounded-2xl border border-white/5">
              <div class="flex items-center gap-2 mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-slate-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                <span class="text-[10px] font-black uppercase text-slate-500 tracking-widest">Escala de Incrementos QOE</span>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="space-y-1">
                  <label class="label-style !text-slate-600">QOE Nivel 1 (±)</label>
                  <input v-model="form.qoe_1" type="number" step="0.01" class="input-field text-center" placeholder="0.00">
                </div>
                <div class="space-y-1">
                  <label class="label-style !text-slate-600">QOE Nivel 2 (±)</label>
                  <input v-model="form.qoe_2" type="number" step="0.01" class="input-field text-center" placeholder="0.00">
                </div>
                <div class="space-y-1">
                  <label class="label-style !text-slate-600">QOE Nivel 3 (±)</label>
                  <input v-model="form.qoe_3" type="number" step="0.01" class="input-field text-center" placeholder="0.00">
                </div>
              </div>
            </div>

            <div class="flex justify-end pt-2">
              <button type="submit" class="btn-primary px-16 py-3 shadow-lg shadow-brand-primary/20">
                Sincronizar con Catálogo
              </button>
            </div>
          </form>
        </div>
      </transition>

      <div class="flex flex-col gap-6">
        <div class="relative w-full max-w-md group">
          <input v-model="searchQuery" type="text" placeholder="Buscar por código (ej: 3Tr)..."
                 class="input-field pl-12 h-12 border-white/10 group-hover:border-brand-primary transition-all">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 absolute left-4 top-3.5 text-slate-600 group-hover:text-brand-primary transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>

        <div class="card-skate !p-0 overflow-hidden shadow-2xl">
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