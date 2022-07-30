<template>
<div>
  <div>
    <router-link to="/posts">Posts</router-link>|
    <router-link to="/">Home</router-link>

  </div>
<h1 class="text-danger">Headless Blog Posts</h1>
<router-view></router-view>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data(){
    return {
      posts: {}
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
  margin-top: 60px;
}
</style>
