<template>
    <div class="content-section">
      <h2>Register</h2>
        <form method="POST">
          <div class="row">
            <div class="col">
              <label for="email-field">Email</label>
              <input type="text" id="email-field" class="form-control" placeholder="Email">
            </div>
            <div class="col">
              <label for="password-field">Password</label>
              <input type="password" id="password-field" class="form-control" placeholder="Password">
            </div>
          </div>
        </form>
<!--        <div class="border-top pt-3">-->
<!--            <small class="text-muted">-->
<!--                Already have an account? <a class="ml-2" href="{% url 'login' %}">Sign In</a>-->
<!--            </small>-->
<!--        </div>-->
    </div>
</template>

<script>
export default {
name: "Register"
}
</script>

<style scoped>

</style>