import { defineStore } from "pinia";
import { io } from "socket.io-client";
import axios from "../api";

export const useAuthStore = defineStore("auth", {
  state: () => ({ token: null, user: null }),
  actions: {
    async login(email, password) {
      const r = await axios.post("/api/auth/login", { email, password });
      this.token = r.data.access_token;
      axios.defaults.headers.common.Authorization = `Bearer ${this.token}`;
    },
  },
});

export const useSocket = defineStore("socket", {
  state: () => ({ socket: null }),
  actions: {
    connect() {
      this.socket = io("http://localhost:5000");
    },
  },
});
