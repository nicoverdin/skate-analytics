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
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('access_token');
  const isAdmin = localStorage.getItem('is_staff') === 'true';

  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'Login' });
  } 
  // Si la ruta requiere ser Admin y no lo es, lo mandamos al Home
  else if ((to.name === 'AddSkater' || to.name === 'RegisterResult') && !isAdmin) {
    next({ name: 'Home' });
  }
  else {
    next();
  }
});

export default router