<script setup lang="ts">
import Card from 'primevue/card';
import { onMounted } from 'vue';
import axios from 'axios';
import { ref } from 'vue';
import {CarModelMock} from '../../Models/CarModel';

const carList = ref<CarModelMock[]>();

const getCarList = () => {
    axios.get('http://localhost:8000/cars')
    .then(response => {
        console.log(response.data);
        carList.value = response.data;
    })
    .catch(error => {
        console.log(error);
    });
}
onMounted(() => {
    getCarList();
})
</script>
<template>
    <div class="text-center">
    <h1>Flota de Vehiculos</h1>
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
</template>