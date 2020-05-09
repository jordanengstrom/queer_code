<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <!-- I removed this div because the navbar disappears when you open chrome dev tools -->
      <!-- <div class="collapse navbar-collapse" id="navbarText"> -->
      <div id="triangle"></div>
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <router-link :to="{name: 'Home'}">
            <span class="nav-link" href="#">{Home}</span>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{name: 'Communities'}">
            <span class="nav-link" href="#">{Communities}</span>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{name: 'Overflow'}">
            <span class="nav-link" href="#">{Overflow}</span>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{name: 'Jobs'}">
            <span class="nav-link" href="#">{Jobs}</span>
          </router-link>
        </li>
      </ul>
      <!-- </div> -->
      <div id="circle"></div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {};
  },

  mounted() {
    this.$store.dispatch("getUser");
  },

  computed: {
    articles() {
      return this.$store.state.user;
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=VT323&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap");

a:link {
  text-decoration: none;
}

a:visited {
  text-decoration: none;
}

a:hover {
  text-decoration: none;
}

a:active {
  text-decoration: none;
}

span {
  /* font-family: "VT323", monospace; */
  font-family: "Source Code Pro", monospace;
  font-size: 1.25rem;
}

#triangle {
  width: 0;
  height: 0;
  border-left: 50px solid transparent;
  border-right: 50px solid transparent;
  border-bottom: 100px solid #ffdde1;
  margin-right: 1rem;
}

#circle {
  width: 100px;
  height: 100px;
  background: #d9dbdb;
  border-radius: 50%;
}

li {
  transition: transform 0.2s;
}

/* li:hover {
  transform: scale(1.025);
  transform-origin: left top;
*/
</style>
