<template>
  <div class="p-8">
    <div class="max-w-6xl mx-auto">
      <header class="mb-12">
        <h1 class="text-4xl font-bold text-white mb-2">Resumen General</h1>
        <p class="text-slate-400">Bienvenido de nuevo. Aquí tienes el estado de tu club.</p>
      </header>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        <div class="card-skate flex flex-col justify-between h-40">
          <span class="text-slate-400 text-sm font-medium uppercase tracking-wider">Total Patinadores</span>
          <div class="flex items-end justify-between">
            <span class="text-5xl font-bold text-white">12</span>
            <router-link to="/skaters" class="text-brand-primary text-sm hover:underline">Ver todos</router-link>
          </div>
        </div>

        <div class="card-skate flex flex-col justify-between h-40 border-l-4 border-l-brand-primary">
          <span class="text-slate-400 text-sm font-medium uppercase tracking-wider">Competiciones</span>
          <div class="flex items-end">
            <span class="text-5xl font-bold text-white">3</span>
            <span class="ml-3 text-slate-500 text-sm pb-2">este mes</span>
          </div>
        </div>

        <div class="card-skate flex flex-col justify-between h-40">
          <span class="text-slate-400 text-sm font-medium uppercase tracking-wider">Rendimiento Medio</span>
          <div class="flex items-end">
            <span class="text-5xl font-bold text-white text-brand-primary">8.4</span>
            <span class="ml-2 text-slate-500 text-sm pb-2">/ 10</span>
          </div>
        </div>
      </div>

      <section>
        <h2 class="text-xl font-semibold text-white mb-6">Acciones Rápidas</h2>
        <div class="flex gap-4">
          <button class="btn-primary">Añadir Nuevo Patinador</button>
          <button class="px-6 py-2 border border-border-soft rounded-lg hover:bg-white/5 transition">Configurar Temporada</button>
        </div>
      </section>
    </div>
  </div>
</template>