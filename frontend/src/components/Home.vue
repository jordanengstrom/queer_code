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
  <!-- TODO: Put a disco ball somewhere -->

  <div class="home">
    <Navbar></Navbar>
    <div>
      <!-- TODO: turn the home page into a feed -->
      <h1>queer_code home page</h1>
      <div>
        <h3>Orci Nulla Pellentesque Dignissim Enim</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dictumst quisque sagittis purus sit amet volutpat consequat. Suscipit adipiscing bibendum est ultricies integer. Hendrerit gravida rutrum quisque non. Porttitor rhoncus dolor purus non enim praesent elementum. Amet purus gravida quis blandit. Ut placerat orci nulla pellentesque dignissim enim sit amet venenatis. Lectus magna fringilla urna porttitor rhoncus dolor purus. Et ligula ullamcorper malesuada proin. Sociis natoque penatibus et magnis dis parturient montes nascetur. Consectetur lorem donec massa sapien faucibus et molestie ac. Et egestas quis ipsum suspendisse ultrices gravida dictum fusce ut. Tincidunt ornare massa eget egestas purus viverra accumsan. Turpis nunc eget lorem dolor.</p>
      </div>
      <div>
        <h3>Sed Turpis Tincidunt id Aliquet</h3>
        <p>Volutpat odio facilisis mauris sit amet massa vitae. Quis viverra nibh cras pulvinar mattis nunc sed. Scelerisque in dictum non consectetur a. Ornare arcu dui vivamus arcu felis bibendum. Venenatis lectus magna fringilla urna. Est placerat in egestas erat imperdiet sed. Est sit amet facilisis magna etiam. Facilisis leo vel fringilla est. Vitae aliquet nec ullamcorper sit. Quis commodo odio aenean sed adipiscing diam donec adipiscing. Semper viverra nam libero justo laoreet sit. In egestas erat imperdiet sed euismod nisi porta lorem mollis. Vitae purus faucibus ornare suspendisse sed nisi. Mattis nunc sed blandit libero volutpat. Sit amet cursus sit amet dictum sit amet justo.</p>
      </div>
      <div>
        <h3>Diam Donec Adipiscing Tristique Risus</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dictumst quisque sagittis purus sit amet volutpat consequat. Suscipit adipiscing bibendum est ultricies integer. Hendrerit gravida rutrum quisque non. Porttitor rhoncus dolor purus non enim praesent elementum. Amet purus gravida quis blandit. Ut placerat orci nulla pellentesque dignissim enim sit amet venenatis. Lectus magna fringilla urna porttitor rhoncus dolor purus. Et ligula ullamcorper malesuada proin. Sociis natoque penatibus et magnis dis parturient montes nascetur. Consectetur lorem donec massa sapien faucibus et molestie ac. Et egestas quis ipsum suspendisse ultrices gravida dictum fusce ut. Tincidunt ornare massa eget egestas purus viverra accumsan. Turpis nunc eget lorem dolor.</p>
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
  }
};
</script>

<style scoped>
h1 {
  font-weight: 700;
  margin-top: 3rem;
  margin-bottom: 3rem;
}

.home {
  /* https://webgradients.com/ */
  /* background-image: linear-gradient(to top, #a8edea 0%, #fed6e3 100%);
  height: 100vh;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover; */
  background-image: linear-gradient(-225deg, #e3fdf5 0%, #ffe6fa 100%);
  height: 100vh;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
