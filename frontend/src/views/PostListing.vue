<template>
<div class="m-5 p-5">
  <h1><span class="text-warning me-3"><BIconJournalCode /></span>Posts</h1>

  <LoadingAnimation :visible="loading_api" />
  <div v-if="posts && !(loading_api)">
    <div class="text-start pt-3" v-for="item in posts" v-bind:key="item.id">
        <div class="d-flex align-items-center">
        <router-link :to="postLink(item)">
        <h2>{{item.title}}</h2>
        </router-link>
        <span class="ms-2 text-muted"><BIconClock /></span>
        <span class="ms-1 text-warning fw-bold">{{timeSince(item.meta.first_published_at)}}</span>
        </div>
        <p>{{item.intro}}</p>
        <br>
        <p v-html="posts.body"></p>
    </div>
  </div>
  <div v-if="!(posts)">Service Unavailable</div>
</div>
</template>

<script>
import axios from 'axios'
import LoadingAnimation from '../components/LoadingAnimation.vue'
import { BIconClock, BIconJournalCode } from 'bootstrap-icons-vue'
import utils from '../utils'
export default {
  name: 'PostListing',
  components: { BIconClock, BIconJournalCode, LoadingAnimation },
  data(){
    return {
      posts: [],
      loading_api: false
    }
  },
  methods: {
      timeSince: utils.timeSince,
      postLink(post){
          return "/post/" + post.meta.slug
      }
  },
  mounted(){
    this.loading_api = true
    axios
    .get('/api/v2/pages/?type=blog.BlogPage&fields=intro')
    .then(response => (this.posts = response.data.items))
    .catch(error => {
      if(error.response) {
        console.log(error.response)
      }
    })
    this.loading_api = false
  }
}
</script>