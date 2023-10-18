import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Home from './components/Home.vue';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: Home
  }
  // ... define más rutas según las necesidades de tu aplicación
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
