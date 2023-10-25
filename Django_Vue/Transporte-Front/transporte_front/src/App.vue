<script setup lang="ts">
import Card from 'primevue/card';
import {CarModelMock} from './components/Models/CarModel.ts'
import { onMounted, ref } from "vue";
import Menubar from 'primevue/menubar';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import 'primeicons/primeicons.css';
import axios from 'axios';
import router from './router.ts';

const isUserLogged = ref(false);
const visible = ref(false);

const items = ref([
    {
        label: 'Inicio',
        icon: 'pi pi-fw pi-home',
        route: '/'
    },
    {
        label: 'Coches',
        icon: 'pi pi-fw pi-car',
        items: [
            {
                label: 'Nuevo Coche',
                icon: 'pi pi-fw pi-plus',
                route: 'newCar'
            },
            {
                label: 'Flota',
                icon: 'pi pi-fw pi-list',
                route: '/carList'
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
        icon: 'pi pi-fw pi-power-off',
        visible: isUserLogged.value
    },
    {
        label: 'Iniciar Sesión',
        icon: 'pi pi-fw pi-sign-in',
        route: '/login',
        visible: !isUserLogged.value
    }
]);

const goToRoute = (event: any) => {
    router.push('/carList');
}
</script>

<template>
    <div class="card z-2 menubar">
        <Menubar :model="items">
            <template #item="{ label, item, props, root, hasSubmenu }">
                <router-link v-if="item.route" v-slot="routerProps" :to="item.route" custom>
                    <a :href="routerProps.href" v-bind="props.action" @click="routerProps.navigate">
                        <span v-bind="props.icon" />
                        <span v-bind="props.label">{{ label }}</span>
                    </a>
                </router-link>
                <a v-else :href="item.url" :target="item.target" v-bind="props.action">
                    <span v-bind="props.icon" />
                    <span v-bind="props.label">{{ label }}</span>
                    <span :class="[hasSubmenu && (root ? 'pi pi-fw pi-angle-down' : 'pi pi-fw pi-angle-right')]" v-bind="props.submenuicon" />
                </a>
            </template>
        </Menubar>
    </div>
    <router-view></router-view>
    <Dialog v-model:visible="visible" header="Nuevo conductor" :style="{ width: '50vw' }" :modal="true" :draggable="false">
    <p class="m-0">
        <span class="p-float-label">
            <InputText id="float-input" type="text"/>
            <label for="float-input">Marca</label>
        </span>
    </p>
    <template #footer>
        <span class="flex justify-content-between">
            <Button label="No" class=""/>
            <Button label="Yes" icon="pi pi-check"/>
        </span>
    </template>
    </Dialog>
</template>

<style scoped>

.menubar{
    position: sticky;
    top: 0;
    width: 100%;
    z-index: 0;
}
.modal{
    background-color: #771ea0;
    color: #ffff;
}
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
