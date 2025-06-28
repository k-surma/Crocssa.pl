<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const name = ref("");
const email = ref("");
const password = ref("");
const age = ref(null);
const router = useRouter();

const submit = async () => {
  await axios.post("/api/auth/register", {
    name: name.value,
    email: email.value,
    password: password.value,
    age: age.value,
  });
  router.push("/login");
};
</script>

<template>
  <div class="h-screen flex flex-col items-center justify-center gap-3">
    <h1 class="text-2xl font-bold">Rejestracja</h1>
    <input v-model="name" type="text" placeholder="Imię" class="border px-3 py-2 rounded w-64" />
    <input v-model="age" type="number" placeholder="Wiek" class="border px-3 py-2 rounded w-64" />
    <input v-model="email" type="email" placeholder="Email" class="border px-3 py-2 rounded w-64" />
    <input v-model="password" type="password" placeholder="Hasło" class="border px-3 py-2 rounded w-64" />
    <button @click="submit" class="bg-green-500 text-white px-6 py-2 rounded">Zarejestruj</button>
  </div>
</template>
