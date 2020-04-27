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
  actions: {},
  methods: {
    getCommunities: function() {
      this.loading = true;
      this.$http
        .get("/api/community/")
        .then((response) => {
          this.community = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        });
    },
    getCommunity: function(id) {
      this.loading = true;
      this.$http
        .get(`/api/community/${id}/`)
        .then((response) => {
          this.currentCommunity = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        });
    }
  }
});
