<template>
  <div class="p-8">
    <div class="max-w-5xl mx-auto">
      <header class="mb-8 flex justify-between items-center">
        <div>
          <h1 class="text-3xl font-bold text-white">Rollart 2026 Catalog</h1>
          <p class="text-slate-400">Manage base values, extra points, and QOE scales</p>
        </div>
        <button v-if="isAdmin" @click="showForm = !showForm" class="btn-primary">
          {{ showForm ? 'Close Form' : '+ Add Element' }}
        </button>
      </header>

      <div v-if="showForm" class="card-skate mb-8 border-brand-primary/30">
        <form @submit.prevent="createElement" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div>
              <label class="block text-xs font-semibold text-slate-500 uppercase mb-1">Element Type</label>
              <select v-model="form.name" required class="input-field">
                <option value="Tr">Traveling</option>
                <option value="ASq">Art Seq</option>
                <option value="DSSq">Dance Step Seq</option>
                <option value="FoSq">Foot Seq</option>
                <option value="ClSq">Cluster Sequence</option>
                <option value="ChStS">Choreo Step Seq</option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-semibold text-slate-500 uppercase mb-1">Level (0-5)</label>
              <input v-model.number="form.level" type="number" min="0" max="5" class="input-field" required>
            </div>
            <div>
              <label class="block text-xs font-semibold text-slate-500 uppercase mb-1">Base Value</label>
              <input v-model="form.base_score" type="number" step="0.01" class="input-field" required>
            </div>
            <div>
              <label class="block text-xs font-semibold text-brand-primary uppercase mb-1">Extra Points (%)</label>
              <input v-model="form.extra_points" type="number" step="0.01" class="input-field" placeholder="e.g., 0.5">
            </div>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 bg-bg-main p-4 rounded-lg">
            <div>
              <label class="block text-xs font-semibold text-brand-primary uppercase mb-1">QOE +1 / -1</label>
              <input v-model="form.qoe_1" type="number" step="0.01" class="input-field" placeholder="e.g., 0.5">
            </div>
            <div>
              <label class="block text-xs font-semibold text-brand-primary uppercase mb-1">QOE +2 / -2</label>
              <input v-model="form.qoe_2" type="number" step="0.01" class="input-field" placeholder="e.g., 1.0">
            </div>
            <div>
              <label class="block text-xs font-semibold text-brand-primary uppercase mb-1">QOE +3 / -3</label>
              <input v-model="form.qoe_3" type="number" step="0.01" class="input-field" placeholder="e.g., 1.5">
            </div>
          </div>

          <div class="flex justify-end">
            <button type="submit" class="btn-primary px-12">Save to Catalog</button>
          </div>
        </form>
      </div>

      <div class="mb-6">
        <div class="relative max-w-md">
          <span class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <svg 
              xmlns="http://www.w3.org/2000/svg" 
              class="h-5 w-5 text-brand-primary" 
              fill="none" 
              viewBox="0 0 24 24" 
              stroke="currentColor"
            >
              <path 
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="2.5" 
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" 
              />
            </svg>
          </span>
          <input 
            v-model="searchQuery"
            type="text" 
            placeholder="Search by code (e.g., 4Tr)..."
            class="input-field pl-10 w-full focus:border-brand-primary transition-colors"
          >
        </div>
      </div>

      <div class="card-skate overflow-x-auto">
        <table class="w-full text-left">
          <thead class="text-slate-500 text-sm uppercase tracking-wider border-b border-border-soft">
            <tr>
              <th class="p-4">Code</th>
              <th class="p-4">Base</th>
              <th class="p-4">Extra</th>
              <th class="p-4">Total</th>
              <th class="p-4 text-center">Q1</th>
              <th class="p-4 text-center">Q2</th>
              <th class="p-4 text-center">Q3</th>
              <th v-if="isAdmin" class="p-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/5">
            <tr v-for="el in filteredElements" :key="el.id" class="hover:bg-white/5 transition">
              <td class="p-4 font-mono font-bold text-brand-primary">{{ el.code }} </td>
              <td class="p-4 text-slate-400">{{ el.base_score }} </td>
              <td class="p-4 text-slate-400">{{ el.extra_points || '0.00' }} </td>
              <td class="p-4 text-white font-semibold">{{ el.total_score }} </td>
              <td class="p-4 text-center text-slate-400">{{ el.qoe_1 }} </td>
              <td class="p-4 text-center text-slate-400">{{ el.qoe_2 }} </td>
              <td class="p-4 text-center text-slate-400">{{ el.qoe_3 }} </td>
              <td v-if="isAdmin" class="p-4 text-right">
                <button @click="deleteElement(el.id)" class="text-red-400 hover:text-red-300 text-sm">Delete</button>
              </td>
            </tr>
            <tr v-if="filteredElements.length === 0">
              <td colspan="8" class="p-8 text-center text-slate-500 italic">
                No elements found matching "{{ searchQuery }}"
              </td>
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

// Lógica de filtrado reactiva
const filteredElements = computed(() => {
  const query = searchQuery.value.toLowerCase().trim();
  if (!query) return elements.value;

  return elements.value.filter(el => {
    return el.code.toLowerCase().includes(query) || 
           el.name.toLowerCase().includes(query);
  });
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
    form.value = { 
      name: 'Tr', 
      level: 0, 
      base_score: 0, 
      extra_points: 0, 
      qoe_1: 0, 
      qoe_2: 0, 
      qoe_3: 0 
    };
    showForm.value = false;
    await fetchElements();
  } catch (error) {
    alert("Error saving element. Please check that the code is unique.");
  }
};

const deleteElement = async (id) => {
  if (confirm("Are you sure you want to remove this element from the catalog?")) {
    try {
      await api.delete(`/api/elements/${id}/`);
      await fetchElements();
    } catch (error) {
      console.error("Error deleting element:", error);
    }
  }
};

onMounted(fetchElements);
</script>