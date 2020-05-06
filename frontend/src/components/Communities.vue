<template>
  <div class="comms">
    <Navbar></Navbar>
    <div class="container-fluid">
      <div class="row" id="grid-back">
        <div class="col-sm-12">
          <h1>&#127752; Find your people, or branch out! &#129412;</h1>
        </div>
      </div>
      <div class="row community-row">
        <div class="col-sm-3 comm-card card" v-for="c in communities" v-bind:key="c.id">
          <h3>{{ c.name }}</h3>
          <h5>{{ c.description }}</h5>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>
 
<script>
import Navbar from "./Navbar";
import Footer from "./Footer";

export default {
  name: "Communities",

  data() {
    return {};
  },

  components: {
    Navbar,
    Footer
  },

  mounted() {
    this.$store.dispatch("getCommunities");
  },

  computed: {
    communities() {
      return this.$store.state.communities;
    }
  }
};
</script>

<style scoped>
.comms {
  background-image: linear-gradient(-225deg, #e3fdf5 0%, #ffe6fa 100%);
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.comm-card {
  width: 10rem;
  margin: 1.5rem 2.5rem 1.5rem 2.5rem;
}

.community-row {
  justify-content: space-around;
}

#grid-back {
  background-image: radial-gradient(#d9dbdb, 1px, transparent 0);
  background-size: 40px 40px;
  background-position: -19px -19px;
}

h1 {
  font-weight: 700;
  margin-top: 3rem;
  margin-bottom: 3rem;
}
</style>
