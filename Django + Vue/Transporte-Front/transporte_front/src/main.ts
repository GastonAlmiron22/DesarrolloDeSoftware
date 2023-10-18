import { createApp } from 'vue'
import '/node_modules/primeflex/primeflex.css'
import 'primevue/resources/themes/md-dark-indigo/theme.css'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import router from './router';
createApp(App).use(PrimeVue).use(router).mount('#app')
        
