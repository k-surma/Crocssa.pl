<script setup>
import { ref, onMounted } from "vue";
import SwipeCard from "../components/SwipeCard.vue";
import { useAuthStore } from "../store";
import { useRouter } from "vue-router";
import api from "../api";

const auth = useAuthStore();
const router = useRouter();
const profiles = ref([]);

onMounted(async () => {
  if (!auth.token) {            // ⬅ kiedy ktoś wylogowany wejdzie na /
    router.push("/login");
    return;
  }
  const { data } = await api.get("/api/users/recommendations");
  profiles.value = data;
});

const swipe = async (direction) => {
  const profile = profiles.value.shift();
  if (direction === "like") await api.post(`/api/matches/${profile.id}`);
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
