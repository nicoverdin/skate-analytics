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
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('access_token');

  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'Login' });
  }

  else if (to.name === 'Login' && isAuthenticated) {
    next({ name: 'Home' });
  }

  else {
    next();
  }
});

export default router