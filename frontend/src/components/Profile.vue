<template>
  <div>
    <h1>My Profile Page</h1>
  </div>
</template>


<script>
import Navbar from "./Navbar";
import Footer from "./Footer";

export default {
  name: "Profile",

  data() {
    return {};
  },

  components: {
    Navbar,
    Footer
  },

  mounted() {
    this.$store.dispatch("getActiveUser");
  }
};
</script>

<style scoped>
h1 {
  font-weight: 700;
  margin-top: 3rem;
  margin-bottom: 3rem;
}
</style>
