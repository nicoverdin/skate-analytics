<template>
  <div class="p-4 md:p-8 text-white min-h-screen pb-20">
    <div class="max-w-6xl mx-auto" v-if="skater">
      
      <header class="mb-8">
        <router-link to="/skaters" class="inline-flex items-center text-slate-500 hover:text-brand-primary text-xs font-bold uppercase tracking-wider mb-4 transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
          Volver a la lista
        </router-link>

        <div class="flex flex-col md:flex-row justify-between items-start md:items-end gap-6">
          <div>
            <div class="flex items-center gap-3 mb-2">
              <div class="h-10 w-10 md:h-12 md:w-12 rounded-full bg-slate-800 border border-white/10 flex items-center justify-center text-brand-primary font-black text-lg md:text-xl shadow-inner">
                {{ skater.name.charAt(0).toUpperCase() }}
              </div>
              <h1 class="text-3xl md:text-5xl font-black tracking-tighter uppercase italic">{{ skater.name }}</h1>
            </div>
            <p class="text-slate-500 text-xs md:text-sm font-medium pl-14">Perfil Técnico y Estadísticas</p>
          </div>
          
          <div class="w-full md:w-auto bg-slate-800/50 border border-white/5 px-6 py-4 rounded-2xl flex justify-between md:block items-center backdrop-blur-sm">
            <span class="text-slate-500 text-[10px] md:text-xs font-bold uppercase tracking-widest block md:mb-1">Promedio Global</span>
            <div class="flex items-baseline gap-2">
              <span class="text-3xl md:text-4xl font-mono font-black text-brand-primary tracking-tighter">{{ skater.average_score }}</span>
              <span class="text-slate-600 text-[10px] font-bold">PTS</span>
            </div>
          </div>
        </div>
      </header>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 md:gap-8">
        
        <div class="space-y-6 order-2 lg:order-1">
          
          <div class="bg-bg-card border border-border-soft rounded-2xl overflow-hidden p-1">
            <div class="px-4 py-3 border-b border-white/5 bg-slate-800/30">
              <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <span class="h-2 w-2 rounded-full bg-brand-primary"></span>
                Desglose por Elemento
              </h3>
            </div>
            <div class="divide-y divide-white/5 p-2">
              <div v-for="stat in elementStats" :key="stat.element__name" 
                   class="group flex justify-between items-center p-3 hover:bg-white/5 rounded-lg transition-colors">
                
                <div class="flex-1 mr-4">
                  <div class="flex justify-between mb-1">
                    <span class="font-bold text-sm text-slate-300">{{ stat.element__name }}</span>
                    <span class="font-mono text-xs font-bold text-white">{{ stat.average.toFixed(2) }}</span>
                  </div>
                  <div class="h-1.5 w-full bg-slate-800 rounded-full overflow-hidden">
                    <div class="h-full bg-slate-500 group-hover:bg-brand-primary transition-colors duration-300" 
                         :style="{ width: `${(stat.average / 10) * 100}%` }"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="relative overflow-hidden p-6 bg-gradient-to-br from-blue-900/20 to-slate-900/50 border border-blue-500/20 rounded-3xl group">
            <div class="absolute -right-6 -bottom-6 text-blue-500/10 transition-transform group-hover:scale-125 duration-700">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-32 w-32" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6C8.29 12.42 7 10.78 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.78-1.29 3.42-3.15 4.1z"/>
                </svg>
            </div>
            
            <div class="relative z-10">
                <div class="flex items-center gap-2 mb-3">
                  <span class="flex h-2 w-2 rounded-full bg-blue-400 animate-pulse"></span>
                  <span class="text-blue-400 text-[10px] font-black uppercase tracking-widest">IA Insight</span>
                </div>
                <h4 class="text-white font-bold text-lg md:text-xl mb-2 italic tracking-tight">
                  Mejora Sugerida: <span class="text-blue-400 border-b border-blue-400/30 pb-0.5">{{ recommendedElement }}</span>
                </h4>
                <p class="text-xs md:text-sm text-slate-400 leading-relaxed max-w-md">
                  Detectamos que este elemento tiene el promedio más bajo. Enfocarse aquí tendrá el mayor impacto en la puntuación global.
                </p>
            </div>
          </div>
        </div>

        <div class="order-1 lg:order-2">
          <div class="card-skate flex flex-col items-center justify-center p-4 md:p-8 min-h-[320px] md:min-h-[450px] relative">
            
            <h3 class="absolute top-4 left-6 text-xs font-bold text-slate-500 uppercase tracking-widest">Mapa de Competencias</h3>

            <div class="w-full h-[280px] md:h-[350px] flex items-center justify-center">
              <Radar v-if="chartData.labels.length > 0" :data="chartData" :options="chartOptions" />
              <div v-else class="text-slate-500 text-sm flex flex-col items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                Faltan datos para generar el gráfico
              </div>
            </div>
          </div>
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
    backgroundColor: 'rgba(234, 179, 8, 0.2)',
    borderColor: '#eab308',
    pointBackgroundColor: '#eab308',
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: '#eab308',
    borderWidth: 2
  }]
}));

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    r: {
      angleLines: { color: 'rgba(255, 255, 255, 0.1)' },
      grid: { color: 'rgba(255, 255, 255, 0.1)' },
      pointLabels: { 
        color: '#94a3b8', 
        font: { size: 10, family: "'JetBrains Mono', monospace" } // Fuente más pequeña para móvil
      },
      ticks: { display: false, backdropColor: 'transparent' }
    }
  },
  plugins: { 
    legend: { display: false },
    tooltip: {
      backgroundColor: 'rgba(15, 23, 42, 0.9)',
      titleColor: '#eab308',
      bodyColor: '#fff',
      padding: 10,
      cornerRadius: 8,
      displayColors: false
    }
  }
};

const recommendedElement = computed(() => {
  if (elementStats.value.length === 0) return '---';
  return elementStats.value.reduce((prev, curr) => prev.average < curr.average ? prev : curr).element__name;
});

onMounted(async () => {
  const id = route.params.id;
  try {
    const [skaterRes, statsRes] = await Promise.all([
      api.get(`/api/skaters/${id}/`),
      api.get(`/api/skaters/${id}/stats/`)
    ]);
    skater.value = skaterRes.data;
    elementStats.value = statsRes.data;
  } catch (e) {
    console.error(e);
  }
});
</script>