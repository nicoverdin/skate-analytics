import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/skaters',
    name: 'Skaters',
    component: () => import('../views/SkatersList.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/skaters/add',
    name: 'AddSkater',
    component: () => import('../views/AddSkater.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/results/add',
    name: 'RegisterResult',
    component: () => import('../views/RegisterResult.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/catalog',
    name: 'CatalogManager',
    component: () => import('../views/CatalogManager.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/results',
    name: 'ResultsList',
    component: () => import('../views/ResultsList.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/skaters/:id',
    name: 'SkaterDetail',
    component: () => import('../views/SkaterDetail.vue'),
    meta: { requiresAuth: true }
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access_token');
  
  // Si la ruta requiere auth y no hay token
  if (to.meta.requiresAuth && !token) {
    next({ name: 'Login' });
  } 
  // Si ya estás logueado e intentas ir al Login, mándalo al Dashboard
  else if (to.name === 'Login' && token) {
    next({ name: 'Dashboard' });
  }
  // En cualquier otro caso, permite la navegación
  else {
    next();
  }
});

export default router