<template>
<div>
  
  <div class="parent_block bg-dark text-white">
    <div class="parent_block bg-primary bg-opacity-10">
      <div>
        <NavBar />
      </div>
      
      <div style="min-height:75vh;">
        <router-view></router-view>
      </div>
      <div class="footer-bottom border-top p-3">
        <div class="text-center">
          &copy;<span class="ms-2"><strong>MebiHQ 2022</strong></span>
        </div>
      </div>
    </div>
  </div>  
</div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import axios from 'axios'
export default {
  name: 'App',
  components: { NavBar },
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
  },
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

.parent_block a {
  color: #29B6F6;
}

.parent_block a:hover {
  color: #01579B;
  text-decoration: none;
}
</style>
