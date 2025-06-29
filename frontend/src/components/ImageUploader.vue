<script setup>
import { ref } from "vue";
import api from "../api";

const modelValue = defineModel();         // v-model (Vue 3.4)
const progress   = ref(0);

const choose = async (e) => {
  const file = e.target.files[0];
  if (!file) return;

  const form = new FormData();
  form.append("file", file);

  progress.value = 0;
  const r = await api.post("/api/upload", form, {
    onUploadProgress: ev => progress.value = Math.round(ev.progress * 100),
    headers: { "Content-Type": "multipart/form-data" }
  });
  modelValue.value = r.data.url;          // ← ustawia URL w rodzicu
};
</script>

<template>
  <div class="space-y-2">
    <input type="file" accept="image/*" @change="choose" />
    <div v-if="progress && progress<100" class="text-sm">Wysyłanie… {{progress}} %</div>
    <img v-if="modelValue" :src="modelValue" class="w-48 rounded-lg"/>
  </div>
</template>
