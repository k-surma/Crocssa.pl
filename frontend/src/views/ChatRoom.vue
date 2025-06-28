<script setup>
import { onMounted } from "vue";
import { useRoute } from "vue-router";
import Chat from "../components/Chat.vue";
import { useSocket } from "../store";

const route = useRoute();
const matchId = route.params.id;          // :id z routera
const room = `match_${matchId}`;

const socketStore = useSocket();
onMounted(() => {
  if (!socketStore.socket) socketStore.connect();
});
</script>

<template>
  <div class="h-screen flex flex-col">
    <h2 class="text-xl font-bold p-4 shadow-md">Czat #{{ matchId }}</h2>
    <Chat :room="room" class="flex-1" />
  </div>
</template>
