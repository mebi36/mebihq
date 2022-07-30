<template>
    <div>
        <div v-if="post">
            <h1>{{post.title}}</h1>
            <h3>{{post.intro}}</h3>
            <p v-html="post.body"></p>
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
      errors: null
    }
  },
  methods: {
      getBlogPost() {
          axios
          .get('/api/v2/pages/?type=blog.BlogPage&fields=intro,body')
          .then(response => {
              let posts = response.data.items
              let post = {}
              console.log("this is posts: ")
              console.log(posts)
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