<template>
    <div>
        <nav class="navbar navbar-dark navbar-expand-md sticky-top border-bottom px-3">
          <router-link class="navbar-brand" to="/"><h1 class="logo navbar-brand text-white">MebiHQ</h1></router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navmenu">
            <BIconList class="navbar-toggle-icon h1 text-white" />
          </button>
          <div class="collapse navbar-collapse justify-content-end" id="navmenu">
            <ul class="navbar-nav">
              <li class="nav-item"><router-link class="nav-link" to="/">Home</router-link></li>
              <li class="nav-item"><router-link class="nav-link" to="/posts">Blog</router-link></li>
              <li class="nav-item"><router-link class="nav-link" to="/resume">Resume</router-link></li>
            </ul>
          </div>
        </nav>
    </div>
</template>

<script>
import { BIconList } from 'bootstrap-icons-vue'
export default {
    name: 'NavBar',
    components: {BIconList}
}
</script>

<style scoped>
.navbar {
  padding: 0;
}

.navbar a,
.navbar a:focus {
  display: flex;
  align-items: center;
  font-size: 15px;
  color: #ffffff;
}

.navbar a i,
.navbar a:focus i {
  font-size: 12px;
  line-height: 0;
  margin-left: 5px;
}

.navbar a:hover,
.navbar .active,
.navbar .router-link-active,
.navbar .active:focus,
.navbar .router-link-active:focus,
.navbar li:hover>a {
  color: #eeeeee;
  font-weight: bold;
  background: rgba(255, 255, 255, 0.3);
}
.navbar .navbar-brand,
.navbar .navbar-brand:hover,
 .navbar .navbar-brand:focus,
 .navbar .navbar-brand:active{
    color: #fff;
    background:none;
}

.navbar .dropdown-menu {
    background: #343a40;
}
.navbar-toggle-icon {
    color:#ffffff;
}
.navbar-toggle-icon:focus {
    border-color: #69f0ae;
}
</style>
