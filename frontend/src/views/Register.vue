<script setup>
import { ref } from "vue";
import api from "../api";           // ← instancja z baseURL i tokenem
import { useRouter } from "vue-router";

const name      = ref("");
const age       = ref(null);
const email     = ref("");
const password  = ref("");
const errorMsg  = ref("");
const router    = useRouter();

const submit = async () => {
  errorMsg.value = "";
  try {
    await api.post("/api/auth/register", {     // ← tu było axios.post
      name: name.value,
      email: email.value,
      password: password.value,
      age: age.value,
    });
    router.push("/login");
  } catch (e) {
    errorMsg.value =
      e.response?.data?.msg || "Nie udało się zarejestrować.";
  }
};
</script>

<template>
  <div class="h-screen flex flex-col items-center justify-center gap-3">
    <h1 class="text-2xl font-bold">Rejestracja</h1>

    <input v-model="name" placeholder="Imię" class="input"/>
    <input v-model="age" placeholder="Wiek" type="number" class="input"/>
    <input v-model="email" placeholder="Email" type="email" class="input"/>
    <input v-model="password" placeholder="Hasło" type="password" class="input"/>

    <button @click="submit" class="btn-primary">Zarejestruj</button>
    <p v-if="errorMsg" class="text-red-600">{{ errorMsg }}</p>
  </div>
</template>

<style scoped>
.input {
  @apply border px-3 py-2 rounded w-64;
}

.btn-primary {
  @apply bg-green-500 text-white px-6 py-2 rounded;
}
</style>
