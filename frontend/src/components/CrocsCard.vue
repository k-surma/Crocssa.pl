<script setup>
defineProps({
  profile: {
    type: Object,
    required: true,
    // spodziewamy się:
    // { id, image, name, model, color, size, holes, charms, description }
  },
});
</script>

<template>
  <div class="w-80 h-auto bg-white rounded-xl shadow-lg p-4">
    <img :src="profile.image" class="w-full h-56 object-cover rounded-lg mb-3" />
    <h3 class="text-xl font-bold mb-1">{{ profile.name }}</h3>
    <ul class="text-sm mb-2">
      <li><b>Model:</b> {{ profile.model }}</li>
      <li><b>Kolor:</b> {{ profile.color }}</li>
      <li><b>Rozmiar:</b> {{ profile.size }}</li>
      <li><b>Dziurki:</b> {{ profile.holes }}</li>
      <li><b>Ozdoby:</b> {{ profile.charms }}</li>
    </ul>
    <p class="text-sm">{{ profile.description }}</p>
  </div>
</template>
