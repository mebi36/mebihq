<template>
<div>
  <div class="progress sticky-top" style="height: 0.3rem;">
    <div class="progress-bar progress-bar-animated bg-primary" style="width: 50%;" role="progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
  </div>
  <div class="parent_block bg-dark text-white">
    
    <div class="parent_block bg-primary bg-opacity-10 position-relative">
      <div>
        <nav class="navbar navbar-dark navbar-expand-md sticky-top border-bottom px-3">
          <h1 class="logo navbar-brand text-white">MebiHQ</h1>
          <div class="navbar-collapse justify-content-end" id="navmenu">
          <ul class="navbar-nav">
            <li class="nav-item"><router-link class="nav-link" to="/">Home</router-link></li>
            <li class="nav-item"><router-link class="nav-link" to="/posts">Blog</router-link></li>
            <li class="nav-item"><router-link class="nav-link" to="/about">About</router-link></li>
          </ul>
          </div>
        </nav>
      </div>
      
      <router-view></router-view>
      <div class="container footer-bottom position-absolute bottom-0 start-50 translate-middle">
        <div class="text-center">
          &copy;<span class="ms-2"><strong>MebiHQ 2022</strong></span>
        </div>
      </div>
    </div>
  </div>  
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data(){
    return {
      posts: {},
    }
  },
  mounted(){
    axios
    .get('http://localhost:8009/api/v2/pages/4')
    .then(response => (this.posts = response.data))
    .catch(error => {
      if(error.response) {
        console.log(error.response)
      }
    })
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
.parent_block {
    height: 100vh;
    max-width: 100vw;
    overflow-x:none;
}
</style>
