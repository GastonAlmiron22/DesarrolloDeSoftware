<script setup lang="ts">
import { ref } from "vue";
import InputText from "primevue/inputtext";
import Button from "primevue/button";
import ProgressSpinner from 'primevue/progressspinner';
import { onMounted } from "vue";
const user = ref<UserModel>({});
const showProgressSpinner = ref(false);

const login = () => {
  console.log(user);
};

const goToBottom = () => {
  window.scrollTo(0, document.body.scrollHeight);
};



onMounted(() => {
    goToBottom();
});

interface UserModel {
  username: string;
  password: string;
}
</script>

<template>
  <div class="grid">
    <div class="login">
      <div class="col-6">
        <div class="p-fluid">
            <div class="text-center carLoginImg">
                <img src="../assets/icons8-car-100.png  " alt="">
            </div>
          <h1>Iniciar Sesión</h1>
          <div>
            <label for="username">Usuario</label>
            <InputText id="username" v-model="user.username" />
          </div>
          <div class="mt-2">
            <label for="password">Contraseña</label>
            <InputText id="password" v-model="user.password" />
          </div>
          <div class="mt-2">
            <Button label="Ingresar" @click="login" />
          </div>
        </div>
      </div>
    </div>
    <div class="card flex justify-content-center">
    </div>
    </div>
</template>
<style>
.carLoginImg{
    margin-bottom: 2rem;
    width: 100%;
    height: 100%;
    display: block;
    margin-left: auto;
    margin-right: auto;
}

.login {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
  background-color: #170214;
  color: white;

  font-weight: bold;
}
.Spinner{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100vh;
    background-color: #170214;
    color: white;
    font-weight: bold;
}
</style>
