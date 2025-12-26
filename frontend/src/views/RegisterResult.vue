<template>
  <div class="p-4 md:p-8 min-h-screen pb-20">
    <div class="max-w-2xl mx-auto">
      
      <header class="mb-6 md:mb-8">
        <button 
          @click="goBack" 
          class="text-brand-primary text-sm hover:underline flex items-center mb-4 bg-transparent border-none p-0 cursor-pointer"
        >
          ← Volver al Panel
        </button>
        <h1 class="text-2xl md:text-3xl font-bold text-white">Registrar Elemento</h1>
      </header>

      <div class="card-skate">
        <form @submit.prevent="saveResult" class="space-y-6">
          
          <div>
            <label class="block text-sm font-medium text-slate-300 mb-2">Patinador</label>
            <div class="relative">
              <select v-model="form.skater" required class="input-field appearance-none">
                <option value="" disabled>Selecciona un atleta...</option>
                <option v-for="s in skaters" :key="s.id" :value="s.id">{{ s.name }}</option>
              </select>
              <div class="absolute right-3 top-3.5 pointer-events-none text-slate-500">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
              </div>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-slate-300 mb-2">Elemento</label>
              <div class="relative">
                <select v-model="selectedElementName" @change="handleElementChange" required class="input-field appearance-none">
                  <option value="" disabled>Tipo...</option>
                  <option v-for="name in uniqueElementNames" :key="name" :value="name">
                    {{ name }}
                  </option>
                </select>
                <div class="absolute right-2 top-3.5 pointer-events-none text-slate-500">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
                </div>
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-slate-300 mb-2">Nivel</label>
              <div class="relative">
                <select 
                  v-model="selectedLevel" 
                  :disabled="!selectedElementName" 
                  required 
                  class="input-field appearance-none disabled:opacity-50"
                >
                  <option value="" disabled>Dificultad...</option>
                  <option v-for="lvl in availableLevels" :key="lvl" :value="lvl">
                    {{ getLevelLabel(lvl) }}
                  </option>
                </select>
                <div class="absolute right-2 top-3.5 pointer-events-none text-slate-500">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
                </div>
              </div>
            </div>
          </div>

          <transition name="fade">
            <div v-if="isTraveling" class="bg-brand-primary/5 p-4 rounded-xl border border-brand-primary/20">
              <label class="block text-xs font-bold text-brand-primary uppercase tracking-wider mb-3">
                Traveling Extra Score
              </label>
              <div class="grid grid-cols-3 sm:grid-cols-6 gap-2">
                <button 
                  v-for="score in [0, 1.0, 1.1, 1.3, 1.7, 2.0]" 
                  :key="score"
                  type="button"
                  @click="form.extra_points = score"
                  :class="[
                    'py-2.5 px-1 rounded-lg text-xs md:text-sm font-bold transition-all border',
                    form.extra_points === score 
                      ? 'bg-brand-primary text-bg-main border-brand-primary shadow-lg scale-105' 
                      : 'bg-slate-800 text-slate-400 border-white/10 hover:bg-slate-700'
                  ]"
                >
                  {{ score === 0 ? 'Base' : '+' + score.toFixed(1) }}
                </button>
              </div>
            </div>
          </transition>

          <div>
            <label class="block text-sm font-medium text-slate-300 mb-3 text-center">
              Calidad de Ejecución (QOE)
            </label>
            <div class="flex justify-between gap-2 overflow-x-auto pb-2 touch-pan-x snap-x">
              <button 
                v-for="val in [-3, -2, -1, 0, 1, 2, 3]" 
                :key="val"
                type="button"
                @click="form.qoe_given = val"
                :class="[
                  'snap-center flex-1 min-w-[44px] py-3 rounded-xl font-bold transition-all border text-sm md:text-base',
                  form.qoe_given === val 
                    ? 'bg-brand-primary text-bg-main border-brand-primary scale-105 shadow-brand-primary/20 shadow-lg ring-2 ring-brand-primary/30' 
                    : 'bg-slate-800 text-slate-400 border-white/10 hover:bg-slate-700'
                ]"
              >
                {{ val > 0 ? '+' + val : val }}
              </button>
            </div>
          </div>

          <transition name="fade">
            <div v-if="currentElement" class="bg-gradient-to-br from-slate-800 to-slate-900 p-6 rounded-2xl border border-white/10 text-center relative overflow-hidden group">
              
              <div class="absolute top-0 left-0 w-full h-1 bg-brand-primary"></div>

              <p class="text-slate-500 text-[10px] uppercase tracking-widest font-bold mb-2">Cálculo en Tiempo Real</p>
              
              <div class="flex justify-center items-baseline gap-2 mb-2">
                <span class="text-5xl font-mono font-black text-white tracking-tighter drop-shadow-xl">
                  {{ (parseFloat(currentElement.base_score) + form.extra_points + getQoeImpact()).toFixed(2) }}
                </span>
                <span class="text-xs font-bold text-brand-primary uppercase">Pts</span>
              </div>
              
              <div class="inline-flex items-center gap-2 bg-black/20 px-3 py-1 rounded-full text-[10px] text-slate-400 border border-white/5">
                <span>Base: <b class="text-white">{{ currentElement.base_score }}</b></span>
                <span class="text-slate-600">|</span>
                <span v-if="form.extra_points > 0" class="text-green-400 font-bold">
                   Extra: +{{ form.extra_points.toFixed(1) }}
                </span>
                <span v-else>No Extra</span>
                <span class="text-slate-600">|</span>
                <span>QOE: <b :class="getQoeImpact() >= 0 ? 'text-green-400' : 'text-red-400'">
                  {{ getQoeImpact() > 0 ? '+' : '' }}{{ getQoeImpact() }}
                </b></span>
              </div>
            </div>
          </transition>

          <button 
            type="submit" 
            :disabled="!currentElement" 
            class="btn-primary w-full py-4 text-base md:text-lg font-black uppercase tracking-widest shadow-xl shadow-brand-primary/10 disabled:opacity-50 disabled:shadow-none disabled:cursor-not-allowed active:scale-[0.98] transition-all"
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
  extra_points: 0,
  qoe_given: 0,
  notes: '',
  is_program: false
});

const goBack = () => {
  router.push('/');
};

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
    0: 'Base (Lvl 0)',
    1: 'Nivel 1',
    2: 'Nivel 2',
    3: 'Nivel 3',
    4: 'Nivel 4',
    5: 'Nivel 5',
    6: 'Nivel 6'
  };
  return map[lvl] || `Nivel ${lvl}`;
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
    // IMPORTANTE: Aquí mandamos el ID del elemento base que encontramos
    form.value.element = currentElement.value.id;
    
    
    await api.post('/api/results/', form.value);
    
    router.push('/');
  } catch (error) {
    alert("Error al guardar el resultado. Revisa que todos los campos estén completos.");
    console.error(error);
  }
};
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>