<script setup lang="ts">
import { ref } from 'vue'
import Button from 'primevue/button';
import Card from 'primevue/card';

defineProps<{ msg: string }>()

const count = ref(0)
</script>

<template>
  <h1>{{ msg }}</h1>
  
    <div class="col-md-6 col-12">
      <Card class="cardbox">
        <template #title>Card Title</template>
        <template #content>
          <Button class="btn btn-primary" @click="count++">count is {{ count }}</Button>
        </template>
      </Card>
    </div>
    <p>
      Edit
      <Code>components/HelloWorld.vue</Code> to test HMR
    </p>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/vuejs/language-tools" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
.cardbox{
  margin: 50px;
  transition-duration: 1s;
  justify-content: center;
  align-items: center;
}
.cardbox:hover{
  transform: scale(1.01);
  box-shadow: 0 10px 20px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.06);
  transition-duration: 1s;
  color: rgb(174, 140, 140);
  stroke-width: 23%;
  background: linear-gradient(146deg, rgba(227, 12, 12, 0.3) 3%, rgba(182, 70, 70, 0) 100%);
}
</style>
