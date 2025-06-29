import { createApp } from "vue";
import { createPinia } from "pinia";
import router from "./router";
import App from "./App.vue";
import "./style.css";
import api from "./api";          // <-- ważne!

/* jeśli token był w localStorage, dołącz nagłówek przed startem app-ki */
const stored = localStorage.getItem("jwt");
if (stored)
  api.defaults.headers.common.Authorization = `Bearer ${stored}`;

createApp(App).use(createPinia()).use(router).mount("#app");
