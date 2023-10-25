<script setup lang="ts">
import Card from 'primevue/card';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import InputNumber from 'primevue/inputnumber';
import Calendar from 'primevue/calendar';
import Dropdown from 'primevue/dropdown';

import {computed, onMounted} from 'vue';
import {ref} from 'vue';
import router from '../../../router.ts';

const car = ref<Car>({}); //Car es una interface
const brands = ref<string[]>([])
const isFormValid = computed(() => {
    return car.value?.brand && car.value.model && car.value.price && car.value.saleDate;
})

const setBrands = () => {
    brands.value = [
        'Audi',
        'BMW',
        'Fiat',
        'Ford',
        'Honda',
        'Jaguar',
        'Mercedes',
        'Renault',
        'VW',
        'Volvo'
    ]
}

const goToHome = () => {
    router.push('/');
}

onMounted(() => {
    //Enviar al fondo de la pagina
    window.scrollTo(0, document.body.scrollHeight);
    setBrands();

})

interface Car{
    brand?: string;
    model?: string;
    price?: number;
    saleDate?: Date;
}
</script>
<template>
    <div class="grid justify-content-center mt-3 newCarCard">
        <div class="d-flex">
            <Card>
                <template #title>
                    <h3 class="text-center">Nuevo Coche</h3>
                </template>
                <template #content>
                    <Form>
                        <!--agrupar en 2 columnas los 4 campos en 2 y 2-->
                        <div class="p-fluid p-formgrid p-grid">
                            <div class="p-field p-col-12 p-md-6 mt-0">
                                <label for="brand">Marca</label>
                                <Dropdown id="brand" v-model="car.brand" :options="brands"  placeholder="Seleccione una marca" />
                            </div>
                            <div class="p-field p-col-12 p-md-6 mt-2">
                                <label for="model">Modelo</label>
                                <InputText id="model" v-model="car.model" />
                            </div>
                            <div class="p-field p-col-12 p-md-6 mt-2">
                                <label for="price">Precio</label>
                                <InputNumber id="price" v-model="car.price" />
                            </div>
                            <div class="p-field p-col-12 p-md-6 mt-2">
                                <label for="calendar">Fecha de Venta</label>
                                <Calendar id="calendar" v-model="car.saleDate" />
                            </div>
                        </div>
                    </Form>
                </template>
                <template #footer>
                    <div class="flex justify-content-between">
                        <Button severity="secondary" label="Guardar" icon="pi pi-save" :disabled="!isFormValid"/>
                        <Button label="Cancelar" severity="info"  icon="pi pi-times" @click="goToHome"/>
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>
<style>
.newCarCard{
    width: 100%;
}
</style>