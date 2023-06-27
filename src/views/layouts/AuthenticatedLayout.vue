<template lang="">
    <div class="relative">  
      <Navbar/>
      <AsideBar/>
      <div class="absolute top-7 right-0 left-0 bottom-0 bg-white border-gray-200 dark:bg-gray-900">
         <slot/>
      </div>
      
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import AsideBar from '@/components/AsideBar.vue';
export default {
   components: {
      Navbar,
      AsideBar
   },
   mounted() {
      var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
      var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

      // Change the icons inside the button based on previous settings
      if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
         themeToggleLightIcon.classList.remove('hidden');
      } else {
         themeToggleDarkIcon.classList.remove('hidden');
      }

      var themeToggleBtn = document.getElementById('theme-toggle');

      themeToggleBtn.addEventListener('click', function () {

         // toggle icons inside button
         themeToggleDarkIcon.classList.toggle('hidden');
         themeToggleLightIcon.classList.toggle('hidden');

         // if set via local storage previously
         if (localStorage.getItem('color-theme')) {
            if (localStorage.getItem('color-theme') === 'light') {
               document.documentElement.classList.add('dark');
               localStorage.setItem('color-theme', 'dark');
            } else {
               document.documentElement.classList.remove('dark');
               localStorage.setItem('color-theme', 'light');
            }

            // if NOT set via local storage previously
         } else {
            if (document.documentElement.classList.contains('dark')) {
               document.documentElement.classList.remove('dark');
               localStorage.setItem('color-theme', 'light');
            } else {
               document.documentElement.classList.add('dark');
               localStorage.setItem('color-theme', 'dark');
            }
         }

      });
   },
}
</script>
<style lang="">
    
</style>