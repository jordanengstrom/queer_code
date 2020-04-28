import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/components/Home";
import Communities from "@/components/Communities.vue";
import Careers from "@/components/Careers";
import Overflow from "@/components/Overflow";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/communities",
    name: "Communities",
    component: Communities
  },
  {
    path: "/overflow",
    name: "Overflow",
    component: Overflow
  },
  {
    path: "/careers",
    name: "Careers",
    component: Careers
  }
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
