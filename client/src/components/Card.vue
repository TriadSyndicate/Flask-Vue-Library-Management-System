<template lang="">
<div :class="class">
    <a href="#">
        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{title}}</h5>
    </a>
    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{description}}</p>

</div>
</template>
<script>
export default {
    props: {
        class: String,
        title: String,
        description: String,
    }

}
</script>
<style lang="">
    
</style>