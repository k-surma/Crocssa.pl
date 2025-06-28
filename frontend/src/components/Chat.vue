<script setup>
import { ref, onMounted } from "vue";
import { useSocket } from "../store";
const props = defineProps({ room: String });
const socketStore = useSocket();
const msgs = ref([]);
const text = ref("");

onMounted(() => {
  socketStore.connect();
  socketStore.socket.emit("join", { room: props.room, sid: socketStore.socket.id });
  socketStore.socket.on("message", (m) => msgs.value.push(m));
});

const send = () => {
  socketStore.socket.emit("message", { room: props.room, body: text.value });
  text.value = "";
};
</script>

<template>
  <div class="flex flex-col h-full">
    <div class="flex-1 overflow-y-auto p-2">
      <div v-for="m in msgs" :key="m.id" class="mb-1">{{ m.body }}</div>
    </div>
    <div class="flex p-2">
      <input v-model="text" class="flex-1 border rounded-l px-2" @keyup.enter="send" />
      <button class="bg-blue-500 text-white px-4 rounded-r" @click="send">Wyślij</button>
    </div>
  </div>
</template>
