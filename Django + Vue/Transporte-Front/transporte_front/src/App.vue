<script setup lang="ts">
import Card from 'primevue/card';
import {CarList} from './components/Models/CarModel.ts'
import { ref } from "vue";
import Menubar from 'primevue/menubar';
import 'primeicons/primeicons.css';

const carList = CarList();

interface Car {
  color: string;
}

const items = ref([
    {
        label: 'Coches',
        icon: 'pi pi-fw pi-car',
        items: [
            {
                label: 'New',
                icon: 'pi pi-fw pi-plus',
                items: [
                    {
                        label: 'Bookmark',
                        icon: 'pi pi-fw pi-bookmark'
                    },
                    {
                        label: 'Video',
                        icon: 'pi pi-fw pi-video'
                    }
                ]
            },
            {
                label: 'Delete',
                icon: 'pi pi-fw pi-trash'
            },
            {
                separator: true
            },
            {
                label: 'Export',
                icon: 'pi pi-fw pi-external-link'
            }
        ]
    },
    {
        label: 'Editar',
        icon: 'pi pi-fw pi-pencil',
        items: [
            {
                label: 'Left',
                icon: 'pi pi-fw pi-align-left'
            },
            {
                label: 'Right',
                icon: 'pi pi-fw pi-align-right'
            },
            {
                label: 'Center',
                icon: 'pi pi-fw pi-align-center'
            },
            {
                label: 'Justify',
                icon: 'pi pi-fw pi-align-justify'
            }
        ]
    },
    {
        label: 'Clientes',
        icon: 'pi pi-fw pi-user',
        items: [
            {
                label: 'New',
                icon: 'pi pi-fw pi-user-plus'
            },
            {
                label: 'Delete',
                icon: 'pi pi-fw pi-user-minus'
            },
            {
                label: 'Search',
                icon: 'pi pi-fw pi-users',
                items: [
                    {
                        label: 'Filter',
                        icon: 'pi pi-fw pi-filter',
                        items: [
                            {
                                label: 'Print',
                                icon: 'pi pi-fw pi-print'
                            }
                        ]
                    },
                    {
                        icon: 'pi pi-fw pi-bars',
                        label: 'List'
                    }
                ]
            }
        ]
    },
    {
        label: 'Viajes',
        icon: 'pi pi-fw pi-calendar',
        items: [
            {
                label: 'Edit',
                icon: 'pi pi-fw pi-pencil',
                items: [
                    {
                        label: 'Save',
                        icon: 'pi pi-fw pi-calendar-plus'
                    },
                    {
                        label: 'Delete',
                        icon: 'pi pi-fw pi-calendar-minus'
                    }
                ]
            },
            {
                label: 'Archieve',
                icon: 'pi pi-fw pi-calendar-times',
                items: [
                    {
                        label: 'Remove',
                        icon: 'pi pi-fw pi-calendar-minus'
                    }
                ]
            }
        ]
    },
    {
        label: 'Quit',
        icon: 'pi pi-fw pi-power-off'
    }
]);
</script>

<template>
  <div class="card z-2">
        <Menubar :model="items" />
    </div>
  <div class="text-center">
    <h1>Listado de Autos</h1>
  </div>  
  <div class="grid">
    <div v-for="car in carList">
      <div class="col-12 text-center">
          <Card style="width: 15em; background-color: #917fb8;">
            <template #header>
                <img src="./assets/icons8-car-100.png" style="height: 3rem;"/>
            </template>
            <template #content>
              <p><strong>Marca:</strong></p>
              <p>{{car.brand}}</p>
              <p>
                <strong>
                  Modelo: {{car.name}}
                </strong>
              </p>
              <p>
                <strong>
                  Año: {{car.year}}
                </strong>
              </p>
              <p>
                <strong>
                  Color: {{car.color}}
                </strong>
              </p>
            </template>
        </Card>
      </div>
    </div>
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
</style>
