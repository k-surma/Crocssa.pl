<template>
  <header class="bg-purple-600 text-white px-4 py-3 shadow-md flex justify-between">
    <h1 class="text-xl font-semibold">Crocssa</h1>
    <nav class="space-x-4">
      <router-link v-if="!auth.token" to="/login">Logowanie</router-link>
      <router-link v-if="!auth.token" to="/register">Rejestracja</router-link>
      <button v-else @click="auth.logout()">Wyloguj</button>
    </nav>
  </header>

  <router-view />
</template>

<script setup>
import { useAuthStore } from "./store";
const auth = useAuthStore();
</script>
