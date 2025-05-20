import { createRouter, createWebHistory, type NavigationGuardNext, type RouteLocationNormalized } from 'vue-router';
import Home from '../pages/Home.vue';
import Login from '../pages/Login.vue';
import Ports from '../pages/Ports.vue';
import { isAuthenticated } from '../utils/auth';
import Signup from '../pages/Signup.vue'; 

const routes = [
   { path: '/', name: 'Home', component: Home },
   { path: '/login', name: 'Login', component: Login },
   {
       path: '/ports',
       name: 'Ports',
       beforeEnter: (_to: RouteLocationNormalized, _from: RouteLocationNormalized, next: NavigationGuardNext) => {
           if (!isAuthenticated()) {
               next('/login');
           } else {
               next();
           }
       },
       component: Ports,
   },
   {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
];

const router = createRouter({
   history: createWebHistory(),
   routes,
});

export default router;
