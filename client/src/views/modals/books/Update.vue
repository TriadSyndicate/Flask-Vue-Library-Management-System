<template lang="">
    <!-- Edit Book Drawer -->
    <dialog :id="dialogId" class="fixed top-0 right-0 z-40 w-full h-modal max-w-xs p-4 overflow-y-auto transition-transform translate-x-full bg-white dark:bg-gray-800" tabindex="-1" aria-labelledby="drawer-label" aria-hidden="true" >
        <h5 id="drawer-label" class="inline-flex items-center mb-6 text-sm font-semibold text-gray-500 uppercase dark:text-gray-400">Update Book: {{book.title}}</h5>
        <button @click="closeModal" type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 absolute top-2.5 right-2.5 inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white">
            <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
            <span class="sr-only">Close menu</span>
        </button>
        <form action="#">
            <div class="space-y-4">
                <div>
                    <label for="book_title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Book Title</label>
                    <input type="text" name="book_title" id="book_title" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" v-model="title" placeholder="Type Book name" required="">
                </div>
                <div>
                    <label for="book_genre" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Genre</label>
                    <select id="book_genre" v-model="book_genre" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                        <option v-for="genre in bookGenres" :value="genre">{{genre}}</option>
                        <option  :selected="book_genre">{{book_genre}}</option>
                        <!-- <option selected="">Flowbite</option>
                        <option value="RE">React</option>
                        <option value="AN">Angular</option>
                        <option value="VU">Vue JS</option> -->
                    </select>
                </div>
                <div>
                    <label for="quantity" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Quantity</label>
                    <input type="number" name="quantity" id="quantity" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" v-model="quantity" placeholder="$149" required="">
                </div>
                <div>
                    <label for="book_author" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Author</label>
                    <input type="text" name="book_author" id="book_author" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" v-model="author" placeholder="Type Book name" required="">
                </div>
                <div>
                    <label for="book_year" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Year</label>
                    <input type="text" name="book_year" id="book_year" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" v-model="year" placeholder="Type Book name" required="">
                </div>
                <!-- <div>
                    <label for="discount" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Discount</label>
                    <select id="discount" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                        <option selected="">No</option>
                        <option value="5">5%</option>
                        <option value="10">10%</option>
                        <option value="20">20%</option>
                        <option value="30">30%</option>
                        <option value="40">40%</option>
                        <option value="50">50%</option>
                    </select>
                </div> -->
            </div>
            <div class="bottom-0 left-0 flex justify-center w-full pb-4 mt-4 space-x-4 sm:absolute sm:px-4 sm:mt-0">
                <button type="submit" class="w-full justify-center text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                    Update
                </button>
                <button type="button" class="w-full justify-center text-red-600 inline-flex items-center hover:text-white border border-red-600 hover:bg-red-600 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:border-red-500 dark:text-red-500 dark:hover:text-white dark:hover:bg-red-600 dark:focus:ring-red-900">
                    <svg aria-hidden="true" class="w-5 h-5 mr-1 -ml-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
                    Delete
                </button>
            </div>
        </form>
    </dialog>
</template>
<script>
export default {
    data() {
        return {
            title: this.book.title,
            author: this.book.author,
            quantity: this.book.stats.quantity,
            year: this.book.year,
            book_genre: this.book.genre,
            bookGenres: [
                "Fiction",
                "Non-fiction",
                "Mystery",
                "Thriller",
                "Romance",
                "Science Fiction",
                "Fantasy",
                "Horror",
                "Historical Fiction",
                "Young Adult",
                "Children",
                "Poetry",
                "Biography",
                "Self-help",
                "Business"
            ]
        }
    },
    props: {
        book: {
            type: Object,
            required: true
        }
    },
    computed: {
        dialogId() {
            return `updateBook-${this.book._id}`
        }
    },
    methods: {
        closeModal() {
            document.getElementById(this.dialogId).close()
        }
    },
    mounted(){
    }
}
</script>
<style lang="">
    
</style>