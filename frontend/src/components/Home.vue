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
      <div id="grid-back">
        <!-- TODO: turn the home page into a feed -->
        <h1>queer_code home page</h1>
        <div class="row">
          <div style="list-style-type:none" v-for="a in articles" v-bind:key="a.id">
            <div class="col-sm-3">
              <div class="article-unit">
                <h3>{{ a.title }}</h3>
                <h5>By: {{ a.author }}</h5>
                <p>{{ a.content }}</p>
                <span>Published on {{ a.created_date }}</span>
              </div>
            </div>
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
#grid-back {
  background-image: radial-gradient(#d9dbdb, 1px, transparent 0);
  background-size: 40px 40px;
  background-position: -19px -19px;
}

.row {
  background-image: linear-gradient(-225deg, #e3fdf5 0%, #ffe6fa 100%);
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.home {
  background-image: linear-gradient(-225deg, #e3fdf5 0%, #ffe6fa 100%);
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
/* 
.article-unit {
  width: 10rem;
} */

h1 {
  font-weight: 700;
  margin-top: 3rem;
  margin-bottom: 3rem;
}
</style>
