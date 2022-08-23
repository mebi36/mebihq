import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import '@marcoschulte/vue3-progress/dist/index'
import { Vue3ProgressPlugin } from '@marcoschulte/vue3-progress'
import 'bootstrap'

createApp(App)
.use(Vue3ProgressPlugin)
.use(router)
.mount('#app')
