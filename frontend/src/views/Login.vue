<script setup>
import { ref } from "vue";
import { useAuthStore } from "../store";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const auth = useAuthStore();
const router = useRouter();

const submit = async () => {
  await auth.login(email.value, password.value);
  router.push("/");
};
</script>

<template>
  <div class="h-screen flex flex-col items-center justify-center gap-4">
    <h1 class="text-2xl font-bold">Logowanie</h1>
    <input v-model="email" type="email" placeholder="Email" class="border px-3 py-2 rounded w-64" />
    <input v-model="password" type="password" placeholder="Hasło" class="border px-3 py-2 rounded w-64" />
    <button @click="submit" class="bg-blue-500 text-white px-6 py-2 rounded">Zaloguj</button>
  </div>
</template>
