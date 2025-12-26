<template>
  <div class="p-8">
    <div class="max-w-2xl mx-auto">
      <header class="mb-8">
        <router-link to="/" class="text-brand-primary text-sm hover:underline flex items-center mb-4">
          ← Volver al Panel
        </router-link>
        <h1 class="text-3xl font-bold text-white">Registrar Elemento</h1>
      </header>

      <div class="card-skate">
        <form @submit.prevent="saveResult" class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-slate-300 mb-2">Patinador</label>
            <select v-model="form.skater" required class="input-field">
              <option value="" disabled>Selecciona un patinador</option>
              <option v-for="s in skaters" :key="s.id" :value="s.id">{{ s.name }}</option>
            </select>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-slate-300 mb-2">Elemento</label>
              <select v-model="selectedElementName" @change="handleElementChange" required class="input-field">
                <option value="" disabled>Elemento</option>
                <option v-for="name in uniqueElementNames" :key="name" :value="name">
                  {{ name }}
                </option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-slate-300 mb-2">Nivel</label>
              <select 
                v-model="selectedLevel" 
                :disabled="!selectedElementName" 
                required 
                class="input-field"
              >
                <option value="" disabled>Dificultad</option>
                <option v-for="lvl in availableLevels" :key="lvl" :value="lvl">
                  {{ getLevelLabel(lvl) }}
                </option>
              </select>
            </div>
          </div>

          <transition name="fade">
            <div v-if="isTraveling" class="bg-brand-primary/10 p-4 rounded-xl border border-brand-primary/20">
              <label class="block text-sm font-bold text-brand-primary mb-2">
                Traveling Extra Score
              </label>
              <div class="grid grid-cols-3 sm:grid-cols-6 gap-2">
                <button 
                  v-for="score in [0, 1.0, 1.1, 1.3, 1.7, 2.0]" 
                  :key="score"
                  type="button"
                  @click="form.extra_points = score"
                  :class="[
                    'py-2 px-1 rounded-lg text-sm font-bold transition-all border',
                    form.extra_points === score 
                      ? 'bg-brand-primary text-bg-main border-brand-primary shadow-lg scale-105' 
                      : 'bg-bg-input text-slate-400 border-border-soft hover:bg-slate-700'
                  ]"
                >
                  {{ score === 0 ? 'Nada' : '+' + score.toFixed(1) }}
                </button>
              </div>
            </div>
          </transition>
          <div>
            <label class="block text-sm font-medium text-slate-300 mb-4 text-center">
              Calidad de Ejecución (QOE)
            </label>
            <div class="flex justify-between gap-2 overflow-x-auto pb-2">
              <button 
                v-for="val in [-3, -2, -1, 0, 1, 2, 3]" 
                :key="val"
                type="button"
                @click="form.qoe_given = val"
                :class="[
                  'flex-1 min-w-[40px] py-3 rounded-lg font-bold transition-all border',
                  form.qoe_given === val 
                    ? 'bg-brand-primary text-bg-main border-brand-primary scale-110 shadow-lg' 
                    : 'bg-bg-input text-slate-400 border-border-soft hover:bg-slate-600'
                ]"
              >
                {{ val > 0 ? '+' + val : val }}
              </button>
            </div>
          </div>

          <div v-if="currentElement" class="bg-bg-main p-6 rounded-xl border border-border-soft space-y-2 text-center shadow-inner">
            <p class="text-slate-500 text-xs uppercase tracking-widest font-semibold">Cálculo Estimado (Rollart 2026)</p>
            <div class="flex justify-center items-baseline gap-2">
              <span class="text-4xl font-mono font-bold text-brand-primary">
                {{ (parseFloat(currentElement.base_score) + form.extra_points + getQoeImpact()).toFixed(2) }}
              </span>
              <span class="text-slate-400">Puntos</span>
            </div>
            <p class="text-slate-500 text-xs italic">
              Base: {{ currentElement.base_score }} 
              <span v-if="form.extra_points > 0" class="text-brand-primary font-bold">
                 + Extra: {{ form.extra_points.toFixed(1) }}
              </span>
              | QOE: {{ getQoeImpact() > 0 ? '+' : '' }}{{ getQoeImpact() }}
            </p>
          </div>

          <button 
            type="submit" 
            :disabled="!currentElement" 
            class="btn-primary w-full py-4 text-lg font-bold uppercase tracking-wider disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Guardar Resultado
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import api from '../api/axios';
import { useRouter } from 'vue-router';

const router = useRouter();
const skaters = ref([]);
const elements = ref([]);

const selectedElementName = ref('');
const selectedLevel = ref('');

const form = ref({
  skater: '',
  element: '',
  qoe_given: 0,
  notes: '',
  is_program: false
});

const isTraveling = computed(() => {
  return selectedElementName.value === 'Tr';
});

const handleElementChange = () => {
  if (!isTraveling.value) {
    form.value.extra_points = 0;
  }
};

onMounted(async () => {
  try {
    const [sRes, eRes] = await Promise.all([
      api.get('/api/skaters/'),
      api.get('/api/elements/')
    ]);
    skaters.value = sRes.data;
    elements.value = eRes.data;
  } catch (error) {
    console.error("Error cargando datos:", error);
  }
});

const uniqueElementNames = computed(() => {
  const names = elements.value.map(el => el.name);
  return [...new Set(names)].sort();
});

const availableLevels = computed(() => {
  if (!selectedElementName.value) return [];
  
  const allLevels = elements.value
    .filter(el => el.name === selectedElementName.value)
    .map(el => el.level);

  return [...new Set(allLevels)].sort((a, b) => a - b);
});

const getLevelLabel = (lvl) => {
  const map = {
    0: 'NL (No Level)',
    1: 'B (Base)',
    2: 'Nivel 1',
    3: 'Nivel 2',
    4: 'Nivel 3',
    5: 'Nivel 4'
  };
  return map[lvl] || `Lvl ${lvl}`;
};

const currentElement = computed(() => {
  return elements.value.find(el => 
    el.name === selectedElementName.value && 
    el.level == selectedLevel.value &&
    el.extra_points == form.value.extra_points
  );
});

const getQoeImpact = () => {
  if (!currentElement.value) return 0;
  const val = form.value.qoe_given;
  if (val === 0) return 0;
  
  const absVal = Math.abs(val);
  const impact = parseFloat(currentElement.value[`qoe_${absVal}`] || 0);
  
  return val > 0 ? impact : -impact;
};

const saveResult = async () => {
  if (!currentElement.value) return;
  
  try {
    form.value.element = currentElement.value.id;
    await api.post('/api/results/', form.value);
    router.push('/');
  } catch (error) {
    alert("Error al guardar el resultado.");
    console.error(error);
  }
};
</script>

<style scoped>
/* Pequeña animación para que aparezca suave el panel de extra score */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>