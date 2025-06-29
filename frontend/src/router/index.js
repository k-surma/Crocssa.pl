import { createRouter, createWebHistory } from "vue-router";
import Home      from "../views/Home.vue";
import Login     from "../views/Login.vue";
import Register  from "../views/Register.vue";
import ChatRoom  from "../views/ChatRoom.vue";
import Profile from "../views/Profile.vue";
export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/",        component: Home },
    { path: "/login",   component: Login },
    { path: "/register",component: Register },
    { path: "/chat/:id",component: ChatRoom, props: true },
    { path: "/profile", component: Profile },
  ],
});
