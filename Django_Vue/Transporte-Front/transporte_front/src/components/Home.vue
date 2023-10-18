<script setup lang="ts">
import Card from 'primevue/card';
import Menubar from 'primevue/menubar';
import {ref} from 'vue';
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
    <div class="home">
        <div class="card z-2">
        <Menubar :model="items" />
    </div> 
    <div class="grid">
        <div v-for="car in carList" class="col-3 text-center flex justify-content-center align-items-center">
            <Card class="carCards" style="width: 15em;" @click="showCard">
                <template #header>
                    <img src="./assets/icons8-car-100.png" style="height: 3rem;"/>
                </template>
                <template #content >
                    <div class="flex justify-content-between cardIndividual" style="background-color: #35062e;">
                        <span><strong>Marca:</strong></span>
                        <span><strong>{{car.brand}}</strong></span>
                    </div>
                    <div class="flex justify-content-between cardIndividual" style="background-color: #CD6688;">
                        <span><strong>Modelo:</strong></span>
                        <span><strong>{{car.model}}</strong></span>
                    </div>
                    <div class="flex justify-content-between cardIndividual" style="background-color: #35062e;">
                        <span><strong>Valor:</strong></span>
                        <span><strong>{{formatCurrency(car.value) ?? '-'}}</strong></span>
                    </div>
                    <div class="flex justify-content-between cardIndividual" style="background-color: #CD6688;">
                        <span><strong>Color:</strong></span>
                        <span><strong>{{toUpperCase(car.licencePlate)}}</strong></span>
                    </div>
                </template>
            </Card>
        </div>
    </div>
    </div>
</template>
<style>
</style>