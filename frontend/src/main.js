import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

axios.defaults.baseURL = 'http://localhost:8009'
createApp(App)
.use(router)
.mount('#app')
