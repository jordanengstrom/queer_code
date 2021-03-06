import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/components/Home";
import Communities from "@/components/Communities";
import Jobs from "@/components/Jobs";
import Overflow from "@/components/Overflow";
import Register from "@/components/Register";

Vue.use(VueRouter);

const routes = [
  {
    path: "/home",
    name: "Home",
    component: Home
  },
  {
    path: "/communities/",
    name: "Communities",
    component: Communities
  },
  {
    path: "/overflow/",
    name: "Overflow",
    component: Overflow
  },
  {
    path: "/jobs/",
    name: "Jobs",
    component: Jobs
  },
  {
    path: "/register/",
    name: "Register",
    component: Register
  }
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
