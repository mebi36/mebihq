<template>
<div>
<div v-for="item in posts" v-bind:key="item.id">
    <router-link :to="postLink(item)">
    <h2>{{item.title}}</h2>
    </router-link>
    <p>{{item.intro}}</p>
    <br>
    <p v-html="posts.body"></p>
</div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'PostListing',
  data(){
    return {
      posts: []
    }
  },
  methods: {
      postLink(post){
          return "/post/" + post.id + "/" + post.meta.slug
      }
  },
  mounted(){
    axios
    .get('/api/v2/pages/?type=blog.BlogPage&fields=intro')
    .then(response => (this.posts = response.data.items))
    .catch(error => {
      if(error.response) {
        console.log(error.response)
      }
    })
  }
}
</script>