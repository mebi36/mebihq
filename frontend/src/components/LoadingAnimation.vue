<template>
    <div class="spinner-grow text-secondary" role="status" v-if="visible">
        <span class="visually-hidden">Loading...</span>
    </div>
</template>

<script>
export default {
    name: 'LoadingAnimation',
    props: ["visible"]
}
</script>