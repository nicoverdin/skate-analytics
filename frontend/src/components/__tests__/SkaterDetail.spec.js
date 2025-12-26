import { describe, it, expect, vi, beforeEach } from 'vitest';
import { mount } from '@vue/test-utils';
import SkaterDetail from '@/views/SkaterDetail.vue';
import { createRouter, createMemoryHistory } from 'vue-router';

vi.mock('@/api/axios', () => ({
  default: {
    get: vi.fn((url) => {
      if (url.includes('/stats/')) {
        return Promise.resolve({ 
          data: [{ element__name: 'Traveling', average: 5.5 }] 
        });
      }
      return Promise.resolve({ 
        data: { id: 1, name: 'Mabel', average_score: 8.25 } 
      });
    })
  }
}));

const router = createRouter({
  history: createMemoryHistory(),
  routes: [{ path: '/skaters/:id', component: SkaterDetail }]
});

describe('SkaterDetail.vue', () => {
  beforeEach(async () => {
    router.push('/skaters/1');
    await router.isReady();
  });

  it('debe renderizar el nombre y el promedio correctamente', async () => {
    const wrapper = mount(SkaterDetail, {
      global: {
        plugins: [router],
        stubs: ['Radar']
      }
    });

    await new Promise(resolve => setTimeout(resolve, 50));
    await wrapper.vm.$nextTick();

    expect(wrapper.text()).toContain('Mabel');
    
    expect(wrapper.text()).toContain('8.25');
  });

  it('debe calcular el elemento recomendado (el de menor puntuación)', async () => {
    const wrapper = mount(SkaterDetail, {
      global: {
        plugins: [router],
        stubs: ['Radar']
      }
    });

    await new Promise(resolve => setTimeout(resolve, 50));
    await wrapper.vm.$nextTick();

    expect(wrapper.text()).toContain('Volver a la lista MMabelPerfil Técnico y EstadísticasPromedio Global8.25PTS Desglose por Elemento Traveling5.50IA Insight Mejora Sugerida: Traveling Detectamos que este elemento tiene el promedio más bajo. Enfocarse aquí tendrá el mayor impacto en la puntuación global. Mapa de Competencias');
  });
});