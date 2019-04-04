import Vue from 'vue';
import * as  Bootstrap from 'bootstrap';
import 'bootstrap/dist/css/bootstrap.css';

Vue.use(Bootstrap);

import Header from '../components/layouts/Header.vue';

const app = new Vue({
    el: '.app',
    components: {
        'nav-bar': Header
    },
    data: function() {
        return {
            message: 'Hello Vue.js!'
        }
    }
})