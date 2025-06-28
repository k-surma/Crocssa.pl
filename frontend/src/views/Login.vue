<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../store";

const email    = ref("");
const password = ref("");
const errorMsg = ref("");
const router   = useRouter();
const auth     = useAuthStore();

const submit = async () => {
  errorMsg.value = "";
  try {
    await auth.login(email.value, password.value);   // zapis tokenu
    router.push("/");                                // ✅ na Home
  } catch {
    errorMsg.value = "Błędny login lub hasło.";
  }
};
</script>

<template>
  <div class="h-screen flex flex-col items-center justify-center gap-4">
    <h1 class="text-2xl font-bold">Logowanie</h1>
    <input v-model="email" type="email" placeholder="Email" class="input"/>
    <input v-model="password" type="password" placeholder="Hasło" class="input"/>
    <button @click="submit" class="btn-primary">Zaloguj</button>
    <p v-if="errorMsg" class="text-red-600">{{ errorMsg }}</p>
  </div>
</template>

<style scoped>
.input {
  @apply border px-3 py-2 rounded w-64;
}

.btn-primary {
  @apply bg-blue-500 text-white px-6 py-2 rounded;
}
</style>
