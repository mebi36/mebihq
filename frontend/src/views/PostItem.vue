<template>
    <div class="m-3 p-5">
        <div class="text-start" v-if="post">
            <h1 class="text-center mb-5">{{post.title}}</h1>
            <div class="bg-white bg-opacity-10 p-5 mb-5">
                <p class="lead">{{post.intro}}</p>
            </div>
            <div class="text-center">
                <img v-if="post.image_thumbnail" :src="axios_root_url + post.image_thumbnail.url" :width="post.image_thumbnail.width" :height="post.image_thumbnail.height">
            </div>
            <span v-for="block in post.body" :key="block.id">
                <div class="text-warning mb-2" v-if="block.type == 'heading'">
                    <h4>{{ block.value }}</h4>
                </div>
                <div class="text-center mb-2" v-else-if="block.type == 'image'">
                    <figure>
                        <img class="img-fluid" :src="block.value.file" :alt="block.value.title" style="max-height: 300px;">
                        <figcaption class="figure-caption text-warning">{{block.value.title}}</figcaption>
                    </figure>                    
                </div>
                <div class="mb-2" v-else-if="block.type == 'paragraph'">
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