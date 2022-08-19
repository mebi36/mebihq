<template>
<div>
  <div class="progress sticky-top" style="height: 0.2rem;">
    <div class="progress-bar progress-bar-animated bg-primary" style="width: 50%;" role="progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
  </div>
  <div class="parent_block bg-dark text-white">
    
    <div class="parent_block bg-primary bg-opacity-10">
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
              <li class="nav-item"><router-link class="nav-link" to="/about">About</router-link></li>
            </ul>
          </div>
        </nav>
      </div>
      
      <div style="min-height:75vh;">
        <router-view></router-view>
      </div>
      <div class="footer-bottom border-top p-5">
        <div class="text-center">
          &copy;<span class="ms-2"><strong>MebiHQ 2022</strong></span>
        </div>
      </div>
    </div>
  </div>  
</div>
</template>

<script>
import { BIconList } from 'bootstrap-icons-vue'
import axios from 'axios'
export default {
  name: 'App',
  components: {BIconList},
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
    min-height: 100vh;
    max-width: 100vw;
    overflow-x:none;
}
</style>
