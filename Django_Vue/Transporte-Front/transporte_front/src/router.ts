import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Home from './components/Home.vue';
import CarList from './components/Views/Car/CarList.vue';
import Login from './components/Login.vue';
import NewCar from './components/Views/Car/NewCar.vue';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/carList',
    component: CarList
  },
  {
    path: '/newCar',
    component: NewCar
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
