<script setup lang="ts">
import Card from 'primevue/card';
import Menubar from 'primevue/menubar';
import {ref} from 'vue';

</script>
<template>
    <div class="grid">
        <div class="home">
            <h1>Bienvenido a la Administracion de Viajes Escolares</h1>
        </div>
    </div>
</template>
<style>
.home{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    background-color: #35062e;
    color: white;
    font-size: 3rem;
    font-weight: bold;
}

.home h1{
    text-align: center;
}

@media (max-width: 768px) {
    .home h1{
        font-size: 2.5rem;
    }
}
</style>