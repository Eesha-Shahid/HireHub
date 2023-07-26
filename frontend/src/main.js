import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import Home from './views/Home.vue';
import Jobs from './views/Jobs.vue';

Vue.use(VueRouter);

const routes = [
    { path: '/', component: Home },
    { path: '/jobs', component: Jobs },
];

const router = new VueRouter({
    routes,
});

new Vue({
    router,
    render: (h) => h(App),
}).$mount('#app');
