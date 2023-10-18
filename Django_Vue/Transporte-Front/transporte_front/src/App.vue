<script setup lang="ts">
import Card from 'primevue/card';
import {CarModelMock} from './components/Models/CarModel.ts'
import { onMounted, ref } from "vue";
import Menubar from 'primevue/menubar';
import 'primeicons/primeicons.css';
import axios from 'axios';
import router from './router.ts';

const formatCurrency = (value: number) => {
    return value.toLocaleString('es-CL', { style: 'currency', currency: 'CLP' });
}

const toUpperCase = (value: string) => {
    return value.toUpperCase();
}

const showCard = () => {
    
}


const items = ref([
    {
        label: 'Coches',
        icon: 'pi pi-fw pi-car',
        items: [
            {
                label: 'Nuevo Coche',
                icon: 'pi pi-fw pi-plus',
               
            },
            {
                label: 'Flota',
                icon: 'pi pi-fw pi-list'
            }
        ]
    },
    {
        label: 'Escuelas',
        icon: 'pi pi-fw pi-home',
        items: [
            {
                label: 'Nueva Escuela',
                icon: 'pi pi-fw pi-plus',
               
            },
            {
                label: 'Instituciones',
                icon: 'pi pi-fw pi-list'
            }
        ]
    },
    {
        label: 'Clientes',
        icon: 'pi pi-fw pi-user',
        items: [
            {
                label: 'Nuevo Cliente',
                icon: 'pi pi-fw pi-user-plus'
            },
            {
                label: 'Listado',
                icon: 'pi pi-fw pi-list',
            }
        ]
    },
    {
        label: 'Viajes',
        icon: 'pi pi-fw pi-calendar',
        items: [
            {
                label: 'Esta semana',
                icon: 'pi pi-fw pi-calendar-plus'
            },
            {
                label: 'Nuevo Viaje',
                icon: 'pi pi-fw pi-plus'
            },
            {
                label: 'Historial',
                icon: 'pi pi-fw pi-list'
            }
        ]
    },
    {
        label: 'Condutores',
        icon: 'pi pi-fw pi-users',
        items: [
            {
                label: 'Nuevo Conductor',
                icon: 'pi pi-fw pi-user-plus'
            },
            {
                label: 'Listado',
                icon: 'pi pi-fw pi-list'
            }
        ]
    },
    {
        label: 'Salir',
        icon: 'pi pi-fw pi-power-off'
    }
]);


</script>

<template>
    <router-view></router-view>
    <div class="card z-2">
        <Menubar :model="items" />
    </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
h1{
  color: #ffff;
}

.cardIndividual{
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
    width: 100%;
}
.carCards{
  background-color: #15041d;
}

.carCards:hover::before{
    transform: scale(1.1);
  box-shadow: 0 0 15px #ffee10;
}
.carCards:hover{
    background-color: rgb(144, 115, 156); 
    width: 20em;
    height: 15em;
}

.p-card .p-card-body {
    padding: 0.4rem;
}
</style>
