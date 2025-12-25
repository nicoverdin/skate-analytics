<template>
  <div class="p-8 text-white">
    <div class="max-w-6xl mx-auto" v-if="skater">
      <header class="flex justify-between items-center mb-10">
        <div>
          <h1 class="text-4xl font-bold mb-2">{{ skater.name }}</h1>
          <p class="text-slate-400">ID de Patinador: {{ skater.id }}</p>
        </div>
        <div class="bg-bg-card border border-border-soft px-6 py-3 rounded-2xl">
          <span class="text-slate-500 text-sm block">Puntuación Media Total</span>
          <span class="text-3xl font-mono font-bold text-brand-primary">{{ skater.average_score }}</span>
        </div>
      </header>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div class="space-y-4">
          <h3 class="text-lg font-semibold mb-4 text-slate-300">Análisis por Elemento</h3>
          <div v-for="stat in elementStats" :key="stat.element__name" 
               class="flex justify-between items-center p-4 bg-bg-card border border-border-soft rounded-xl">
            <span class="font-bold text-slate-200">{{ stat.element__name }}</span>
            <span class="font-mono text-brand-primary bg-bg-main px-3 py-1 rounded-lg">
              {{ stat.average.toFixed(2) }}
            </span>
          </div>
          
          <div class="relative overflow-hidden p-6 bg-blue-500/5 border border-blue-500/20 rounded-3xl group transition-all hover:bg-blue-500/10">
            <div class="absolute -right-6 -bottom-6 text-blue-500/10 transition-transform group-hover:scale-125 duration-700">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-24 w-24" fill="currentColor" viewBox="0 0 24 24">
                <path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6C8.29 12.42 7 10.78 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.78-1.29 3.42-3.15 4.1z"/>
                </svg>
            </div>
            
            <div class="relative z-10">
                <div class="flex items-center gap-2 mb-2">
                <span class="flex h-2 w-2 rounded-full bg-blue-400 animate-pulse"></span>
                <span class="text-blue-400 text-[10px] font-black uppercase tracking-widest">Sugerencia del Sistema</span>
                </div>
                <h4 class="text-white font-bold text-xl mb-1 italic tracking-tight">
                Prioridad Técnica: <span class="text-blue-400">{{ recommendedElement }}</span>
                </h4>
                <p class="text-sm text-slate-400 max-w-md leading-relaxed">
                Basado en el rendimiento actual, se detecta una oportunidad de mejora significativa reforzando este elemento en las próximas sesiones.
                </p>
            </div>
          </div>
        </div>

        <div class="card-skate flex items-center justify-center p-8 min-h-[400px]">
          <Radar v-if="chartData.labels.length > 0" :data="chartData" :options="chartOptions" />
          <div v-else class="text-slate-500">No hay suficientes datos para el gráfico</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import api from '../api/axios';
import { Radar } from 'vue-chartjs';
import { Chart as ChartJS, RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend } from 'chart.js';

ChartJS.register(RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend);

const route = useRoute();
const skater = ref(null);
const elementStats = ref([]);

const chartData = computed(() => ({
  labels: elementStats.value.map(s => s.element__name),
  datasets: [{
    label: 'Promedio Técnico',
    data: elementStats.value.map(s => s.average),
    backgroundColor: 'rgba(244, 244, 245, 0.2)',
    borderColor: '#f4f4f5',
    pointBackgroundColor: '#f4f4f5',
    borderWidth: 2
  }]
}));

const chartOptions = {
  scales: {
    r: {
      angleLines: { color: '#3f3f46' },
      grid: { color: '#3f3f46' },
      pointLabels: { color: '#94a3b8', font: { size: 12 } },
      ticks: { display: false }
    }
  },
  plugins: { legend: { display: false } }
};

const recommendedElement = computed(() => {
  if (elementStats.value.length === 0) return '---';
  return elementStats.value.reduce((prev, curr) => prev.average < curr.average ? prev : curr).element__name;
});

onMounted(async () => {
  const id = route.params.id;
  const [skaterRes, statsRes] = await Promise.all([
    api.get(`/api/skaters/${id}/`),
    api.get(`/api/skaters/${id}/stats/`)
  ]);
  skater.value = skaterRes.data;
  elementStats.value = statsRes.data;
});
</script>