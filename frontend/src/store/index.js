import vue from "vue";
import vuex from "vuex";
import axios from "axios";
import router from "../router/index";

var baseUrl = "//localhost:3000/";

var auth = axios.create({
  baseURL: baseUrl + "auth/",
  withCredentials: true
});

var baseAPI = axios.create({
  baseURL: baseUrl,
  withCredentials: false
});

vue.use(vuex);

export default new vuex.Store({
  state: {},
  mutations: {},
  getters: {},
  actions: {
    getHome({ commit, dispatch }, payload) {
      baseAPI
        .get("/")
        .then((res) => {
          console.log("Successfully got 'Home'");
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }
});
