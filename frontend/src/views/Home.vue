<script setup>
import { ref, onMounted } from "vue";
import SwipeCard from "../components/SwipeCard.vue";
import axios from "axios";
const profiles = ref([]);

onMounted(async () => {
  const r = await axios.get("/api/users/recommendations");
  profiles.value = r.data;
});

const swipe = async (direction) => {
  const profile = profiles.value.shift();
  if (direction === "like") await axios.post(`/api/matches/${profile.id}`);
};
</script>

<template>
  <div class="flex items-center justify-center h-screen">
    <SwipeCard
      v-if="profiles[0]"
      :profile="profiles[0]"
      :on-swipe="swipe"
    />
    <p v-else>Brak kandydatów, wróć później 🙂</p>
  </div>
</template>
