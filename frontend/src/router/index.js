import { createWebHistory, createRouter } from "vue-router"

import PostItem from "@/views/PostItem.vue"
import PostListing from "@/views/PostListing.vue"
import Home from "@/views/Home.vue"
import Resume from "@/views/Resume.vue"
import NProgress from "nprogress"
const routes = [
    {
        path: "/",
        name: "Home",
        component: Home
    },
    {
        path: "/posts",
        name: "Blog Posts",
        component: PostListing,
    },
    {
        path: "/resume",
        name: "Resume",
        component: Resume,
    },
    {
        path: "/post/:slug",
        name: "Post",
        component: PostItem,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeResolve((to) => {
    if(to.name){
        NProgress.start()
    }
    return true
})
router.afterEach(() => {
    NProgress.done()
})

export default router