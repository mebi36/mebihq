import { createApp } from 'vue'
import App from './App.vue'
// import axios from 'axios'
import router from './router'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import '@marcoschulte/vue3-progress/dist/index'
import { Vue3ProgressPlugin } from '@marcoschulte/vue3-progress'
import 'bootstrap'

// axios.defaults.baseURL = 'http://localhost:8009'
createApp(App)
.use(Vue3ProgressPlugin)
.use(router)
.mount('#app')
