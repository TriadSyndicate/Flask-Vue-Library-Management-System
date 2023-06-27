<template lang="">
<dialog id="addMember-modal" tabindex="-1"  class="fixed top-0 bg-transparent left-0 right-0 bottom-0 z-[100] w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full container mx-auto">
    <div class="relative w-full max-w-md max-h-full mx-auto my-auto">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <button type="button" @click="closeModal" class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-800 dark:hover:text-white">
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                <span class="sr-only">Close modal</span>
            </button>
            <div class="px-6 py-6 lg:px-8">
                <h3 class="mb-4 text-3xl font-medium underline underline-offset-8 decoration-double decoration-green-500 text-gray-900 dark:text-white">Add New Member</h3>
                <div v-show="success" class="p-4 mb-4 text-sm text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400" role="alert">
                    <span class="font-medium">Successfully Added Member!</span>
                </div>
                <div v-show="failed" class="p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400" role="alert">
                    <span class="font-medium">Failed to Add Member!</span>
                </div>
                <form class="space-y-6" action="#">
                    <div>
                        <label for="names" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Full Names</label>
                        <input type="text" v-model="names" name="names" id="names" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="Kobe Beef" required>
                    </div>
                    <div>
                        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email</label>
                        <input type="email" v-model="email" name="email" id="password" placeholder="email@user.com" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required>
                    </div>
                    <div>
                        <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Phone Number</label>
                        <input type="tel" name="phone" v-model="phone" id="phone" placeholder="+254 700 000 000" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required>
                    </div>
                    <!-- <div class="flex justify-between">
                        <div class="flex items-start">
                            <div class="flex items-center h-5">
                                <input id="remember" type="checkbox" value="" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-600 dark:border-gray-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800" required>
                            </div>
                            <label for="remember" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Remember me</label>
                        </div>
                        <a href="#" class="text-sm text-blue-700 hover:underline dark:text-blue-500">Lost Password?</a>
                    </div> -->
                    <button @submit.prevent type="button" @click="addMember" class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-blue-800">Add Member</button>
                    <!-- <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
                        Not registered? <a href="#" class="text-blue-700 hover:underline dark:text-blue-500">Create account</a>
                    </div> -->
                </form>
            </div>
        </div>
    </div>
</dialog> 
</template>
<script>
export default {
    data() {
        return {
            "names": "",
            "email": "",
            "phone": "",
            success: false,
            failed: false
        }
    },
    methods: {
        openModal() {
            document.getElementById('addMember-modal').showModal();
        },
        closeModal() {
            document.getElementById('addMember-modal').close();
        },
        addMember() {
            this.$http.post('http://localhost:5000/api/v1/members', {
                "name": this.names,
                "email": this.email,
                "phone": this.phone
            }).then((response) => {
                console.log(response.status);
                if(response.status == 201)
                {
                    this.success = true;
                }else if(response.status == 200 && response.data.msg == "Member already exists"){
                    console.log("Failed")
                    this.failed = true;
                }
            }, (error) => {
                // console.log(error);
            });
        }
    }
}
</script>
<style lang="">
    
</style>