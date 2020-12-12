import vue from "vue";
import vuex from "vuex";
import axios from "axios";
import router from "../router/index";
var baseUrl = "http://127.0.0.1:8000/";

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
  state: {
    communities: [],
    articles: [],
    profiles: [],
  },
  mutations: {},
  getters: {},
  actions: {
    getCommunities({ commit, dispatch }, payload) {
      axios
        .get(baseUrl + "communities/")
        .then((response) => {
          this.state.communities = response.data;
          // console.log(this.state.communities);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getArticles({ commit, dispatch }, payload) {
      axios
        .get(baseUrl + "articles/")
        .then((response) => {
          this.state.articles = response.data;
          console.log(this.state.articles);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getActiveUser({ commit, dispatch }, payload) {
      axios.get(baseUrl + "users/").then((response) => {
        this.state.user = response.data;
        console.log(this.state.users);
      });
    },
    getUserRegistrationForm({commit, dispatch}, payload) {
      axios.get(baseUrl + "register/").then((response) => {
        console.log("Here is the user registration page")
      })
      .catch((err) => {
        console.log(err);
        });
    }
  },
  methods: {}
});
