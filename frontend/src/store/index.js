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
  state: {},
  mutations: {},
  getters: {},
  actions: {
    getCommunities({ commit, dispatch }, payload) {
      baseAPI.get("communities/").then((response) => {
        console.log(response);
      });
    }
    //     this.community = response.data;
    //     this.loading = false;
    //   .catch((err) => {
    //     this.loading = false;
    //     console.log(err);
    //   });
  },
  //   getCommunity: function(id) {
  //     this.loading = true;
  //     this.$http
  //       .get(`/api/community/${id}/`)
  //       .then((response) => {
  //         this.currentCommunity = response.data;
  //         this.loading = false;
  //       })
  //       .catch((err) => {
  //         this.loading = false;
  //         console.log(err);
  //       });
  //   }
  // },
  methods: {}
});
