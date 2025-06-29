<script setup>
import {ref, onMounted} from "vue";
import {useRouter} from "vue-router";
import {useAuthStore} from "../store";
import api from "../api";
import ImageUploader from "../components/ImageUploader.vue";

const router = useRouter();
const auth = useAuthStore();
if (!auth.token) router.push("/login");

const loading = ref(true);
const editMode = ref(false);
const saved = ref(false);

const profile = ref({id: null, name: "", age: "", email: "", image: "", description: ""});
const form = ref({name: "", age: "", image: "", description: ""});

/* ── pobranie profilu ─────────────────────────────────────────────── */
onMounted(async () => {
  const {data} = await api.get("/api/users/me");
  profile.value = {...data};          // do podglądu
  Object.assign(form.value, data);      // do edycji
  loading.value = false;
});

/* ── zapis edycji ─────────────────────────────────────────────────── */
const save = async () => {
  await api.put("/api/users/me", form.value);
  Object.assign(profile.value, form.value); // odśwież podgląd
  editMode.value = false;
  saved.value = true;
  setTimeout(() => (saved.value = false), 2000);
};
</script>

<template>
  <div class="max-w-md mx-auto mt-8">
    <h2 class="text-2xl font-bold mb-4">Mój profil</h2>

    <!--  LOADING  -->
    <p v-if="loading" class="text-gray-500">Ładowanie…</p>

    <!--  TRYB PODGLĄDU  -->
    <div v-else-if="!editMode" class="space-y-4">
      <img v-if="profile.image" :src="profile.image" class="w-48 rounded-xl mx-auto"/>
      <p><b>Imię:</b> {{ profile.name }}</p>
      <p><b>Wiek:</b> {{ profile.age || "—" }}</p>
      <p><b>Email:</b> {{ profile.email }}</p>
      <p><b>Opis:</b><br/> {{ profile.description || "—" }}</p>

      <button @click="editMode=true" class="btn-primary mt-2">Edytuj</button>
    </div>

    <!--  TRYB EDYCJI  -->
    <div v-else class="space-y-4">
      <label class="block">Imię
        <input v-model="form.name" class="input"/>
      </label>

      <label class="block">Wiek
        <input type="number" v-model="form.age" class="input"/>
      </label>

      <label class="block">Zdjęcie crocsów
        <ImageUploader v-model="form.image"/>
      </label>

      <label class="block">Opis
        <textarea v-model="form.description" class="input h-24"/>
      </label>

      <div class="flex gap-3">
        <button @click="save" class="btn-primary">Zapisz</button>
        <button @click="editMode=false" class="btn-secondary">Anuluj</button>
      </div>

      <p v-if="saved" class="text-green-600">✓ Zapisano!</p>
    </div>
  </div>
</template>

<style scoped>
.input {
  @apply border px-3 py-2 rounded w-full;
}

.btn-primary {
  @apply bg-primary hover:bg-primary-dark text-white px-6 py-2 rounded;
}

.btn-secondary {
  @apply bg-gray-300 hover:bg-gray-400 text-gray-800 px-6 py-2 rounded;
}
</style>
