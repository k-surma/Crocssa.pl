<script setup>
import { ref, onMounted } from "vue";
import api from "../api"

const props = defineProps({ profile: Object, onSwipe: Function });
const x = ref(0);
const handle = (e) => {
  x.value = e.deltaX;
};
const end = () => {
  if (x.value > 150) props.onSwipe("like");
  else if (x.value < -150) props.onSwipe("skip");
  x.value = 0;
};
</script>

<template>
  <div
    class="w-80 h-96 bg-white rounded-xl shadow-lg p-4 select-none"
    @pointermove="handle"
    @pointerup="end"
    :style="{ transform: `translateX(${x}px)` }"
  >
    <img :src="profile.image" class="w-full h-60 object-cover rounded-lg mb-2" />
    <h3 class="text-xl font-bold">{{ profile.name }}, {{ profile.age }}</h3>
    <p class="text-sm">{{ profile.description }}</p>
  </div>
</template>
