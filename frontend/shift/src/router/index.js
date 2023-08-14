import { createRouter, createWebHistory } from 'vue-router'
// import HomeComponent from '@/components/HomeComponent.vue'
import LoginComponent from '@/components/LoginComponent.vue'
import ScheduleComponent from '@/components/ScheduleComponent.vue'
// import App from '@/App.vue'

const routes = [
//   { path: '/', component: App },
  { path: '/login', component: LoginComponent },
  { path: '/schedule', component: ScheduleComponent },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router