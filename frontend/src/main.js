import Vue from 'vue';
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App.vue';
import VueMaterial from 'vue-material';
import VueMoment from "vue-moment";
import 'vue-material/dist/vue-material.min.css';
import 'vue-material/dist/theme/default.css';

Vue.use(VueAxios, axios);
Vue.use(VueMaterial);
Vue.use(VueMoment);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app')
