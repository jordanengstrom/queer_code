// Ideas
// Pixelated triangle logo
// Get ideas from: Hackernoon, TechCrunch, Medium, Dev, etc.

<template>
  <!-- TODO: Monospace Font -->
  <!-- TODO: User Profiles -->
  <!-- TODO: User blog posts -->
  <!-- TODO: Discussion boards -->
  <!-- TODO: Join by invite only -->
  <!-- TODO: Ability to support markdown -->
  <!-- TODO: Careers page layout -->
  <!-- TODO: Sharing buttons for twitter, facebook, linkedin, email -->
  <!-- TODO: Live chats -->
  <!-- TODO: Mobile app version -->
  <!-- TODO: Resources for queer people -->
  <!-- TODO: Community outreach -->
  <!-- TODO: Alternative themes -->
  <!-- TODO: Put a disco ball somewhere -->
  <div class="home">
    <Navbar></Navbar>
    <div>
      <h1>queer_code home page</h1>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Navbar from "./Navbar";
import Footer from "./Footer";

export default {
  name: "Home",
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
h1 {
  font-weight: 700;
  margin-top: 3rem;
}

.home {
  /* https://webgradients.com/ */
  background-image: linear-gradient(to top, #a8edea 0%, #fed6e3 100%);
  height: 100vh;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
