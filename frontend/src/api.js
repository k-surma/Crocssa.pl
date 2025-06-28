import axios from "axios";

/* 1) odczytujemy zmienną środowiskową z Vite
   (patrz frontend/.env.example → VITE_API_BASE=http://localhost:5000) */
axios.defaults.baseURL =
  import.meta.env.VITE_API_BASE || "http://localhost:5000";

/* 2) jeżeli jest token w localStorage, dołącz go automatycznie */
const token = localStorage.getItem("jwt");
if (token) axios.defaults.headers.common.Authorization = `Bearer ${token}`;

export default axios;      // będziemy importować w komponentach
