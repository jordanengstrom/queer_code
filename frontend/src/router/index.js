import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/components/Home";
import Communities from "@/components/Communities";
import Careers from "@/components/Careers";

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
    path: "/careers",
    name: "Careers",
    component: Careers
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
