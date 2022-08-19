<template>
    <div>
        <div v-if="post" style="color: var(--bs-indigo)">
            <h1 class="text-primary">{{post.title}}</h1>
            <h3 class="bg-success">{{post.intro}}</h3>
            <img v-if="post.image_thumbnail" :src="axios_root_url + post.image_thumbnail.url" :width="post.image_thumbnail.width" :height="post.image_thumbnail.height">
            <span v-for="block in post.body" :key="block.id">
                <div v-if="block.type == 'heading'" class="text-danger">
                    <h2>{{ block.value }}</h2>
                </div>
                <div v-else-if="block.type == 'image'">
                    <h2>image: {{block.value }}</h2>
                </div>
                <div v-else-if="block.type == 'paragraph'">
                    <p v-html="block.value"></p>
                </div>
            </span>
        </div>

    </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'PostItem',
  data(){
    return {
      post: null,
      axios_root_url: axios.defaults.baseURL,
      errors: null
    }
  },
  methods: {
      getBlogPost() {
          axios
          .get('/api/v2/pages/?type=blog.BlogPage&fields=intro,body,image_thumbnail')
          .then(response => {
              let posts = response.data.items
              let post = {}
              for (let idx in posts){
                  post = posts[idx]
                  if (post.meta.slug == this.$route.params.slug){
                      this.post = post
                  }
              }
          })
          .catch(error => {
              this.errors = error
          }
          )
      }
  },
  mounted(){
      this.getBlogPost()
  }
}
</script>