<template lang="">
    <div>
        <AuthenticatedLayout>
            <router-view></router-view>
        </AuthenticatedLayout>
    </div>
</template>
<script>
import AuthenticatedLayout from '../layouts/AuthenticatedLayout.vue';
import { RouterView } from 'vue-router';
export default {
    components: {
        AuthenticatedLayout,
        RouterView,
    },
}
</script>
<style lang="">
    
</style>