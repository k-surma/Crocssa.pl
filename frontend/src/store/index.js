import { defineStore } from "pinia";
import { io }          from "socket.io-client";
import { useRouter }   from "vue-router";
import api             from "../api";     // <-- zamiast axios

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem("jwt") || null,
    user : null,
  }),

  actions: {
    /* LOGIN */
    async login(email, password) {
      const { data } = await api.post("/api/auth/login", { email, password });
      this.token = data.access_token;

      api.defaults.headers.common.Authorization = `Bearer ${this.token}`;
      localStorage.setItem("jwt", this.token);
    },

    /* LOGOUT */
    logout() {
      this.token = null;
      this.user  = null;
      localStorage.removeItem("jwt");
      delete api.defaults.headers.common.Authorization;
      useSocket().disconnect();
      useRouter().push("/login");      // przekierowanie
    },
  },
});

/* Socket-IO (bez zmian poza importem tokenu z localStorage) */
export const useSocket = defineStore("socket", {
  state: () => ({ socket: null }),
  actions: {
    connect() {
      if (!this.socket) {
        this.socket = io("http://localhost:5000", {
          auth: { token: localStorage.getItem("jwt") },
        });
      }
    },
    disconnect() {
      this.socket?.disconnect();
      this.socket = null;
    },
  },
});
