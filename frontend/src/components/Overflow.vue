<template>
  <div class="comms">
    <Navbar></Navbar>
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12">
          <h1>&#127752; Overflow section! &#129412;</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-1">size 1</div>
        <!-- Community ideas: languages, Data Science, DevOps, InfoSec, WebDev, Databases, Gaming, Non-tech discourse,  -->
        <div class="col-sm-10">size 10</div>
        <div class="col-sm-1">size 1</div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Navbar from "./Navbar";
import Footer from "./Footer";

export default {
  name: "Overflow",

  data() {
    return {};
  },

  components: {
    Navbar,
    Footer
  },

  mounted() {
    this.$store.dispatch("getCommunities");
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
.containter-fluid {
  display: flex;
  justify-content: center;
}
/* .row {
  border: 2px solid black;
} */
/* .col-sm-12, */
.col-sm-10,
.col-sm-1 {
  border: 2px solid black;
}

h1 {
  font-weight: 700;
  margin-top: 3rem;
  margin-bottom: 3rem;
}
</style>
