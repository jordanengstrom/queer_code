<template>
  <div class="careers">
    <Navbar></Navbar>
    <div class="list">
      <!-- TODO: Create/read/update/delete job postings (submit for verification???)-->
      <!-- TODO: Search job postings -->
      <h1>Careers Page</h1>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Navbar from "./Navbar";
import Footer from "./Footer";

export default {
  name: "Careers",
  data() {
    return {};
  },
  components: {
    Navbar,
    Footer
  }
};
</script>

<style scoped>
.list {
  border: 2px black;
}

h1 {
  font-weight: 700;
  margin-top: 3rem;
}

.careers {
  background-image: linear-gradient(-225deg, #e3fdf5 0%, #ffe6fa 100%);
  height: 100vh;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
