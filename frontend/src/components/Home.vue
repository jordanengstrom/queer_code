// Ideas
// Pixelated triangle logo
// Get ideas from: Hackernoon, TechCrunch, Medium, Dev, Reddit, Mastadon, etc.

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
  <!-- TODO: dark mode! -->
  <!-- TODO: Put a disco ball somew/here -->

  <div class="home">
    <Navbar></Navbar>
    <div class="container-fluid">
      <!-- TODO: turn the home page into a feed -->
      <div class="row row-margin-override">
        <div class="col-sm-12">
          <h1>queer_code home page</h1>
        </div>
      </div>
      <div class="row article-row row-margin-override">
        <div class="col-sm-5 card" v-for="a in articles" v-bind:key="a.id">
          <div class="article-unit">
            <h3>{{ a.title }}</h3>
            <h5>By: {{ a.author }}</h5>
            <p>{{ a.content }}</p>
            <span>Published on {{ a.created_date }}</span>
          </div>
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
  name: "Home",
  data() {
    return {};
  },
  components: {
    Navbar,
    Footer
  },

  mounted() {
    this.$store.dispatch("getArticles");
  },

  computed: {
    articles() {
      return this.$store.state.articles;
    }
  }
};
</script>

<style scoped>
.container-fluid {
  background-image: radial-gradient(#d9dbdb, 1px, transparent 0);
  background-size: 40px 40px;
  background-position: -19px -19px;
  background-size: 100%;
}

.home {
  background-image: linear-gradient(-225deg, #e3fdf5 0%, #ffe6fa 100%);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.article-unit {
  margin-top: 3rem;
  margin-bottom: 3rem;
  margin-left: 2rem;
  margin-right: 2rem;
}

/* Even though my rows are in a container-fluid, there is still extra 
whitespace that causes the horizontal scrollbar to show up in the browser. 
If this is removed, these two values will to Bootstraps default value of 
-15px */
.row-margin-override {
  margin-left: 0px;
  margin-right: 0px;
}

.article-row {
  justify-content: center;
}

h1 {
  font-weight: 700;
  margin-top: 3rem;
  margin-bottom: 3rem;
}
</style>
