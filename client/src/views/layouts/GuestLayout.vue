<template>
    <div class="min-h-screen flex flex-col sm:justify-center items-center pt-6 sm:pt-0 bg-gray-100 dark:bg-gray-900">
        <div>
            <a href="/home">
                <img src="@/assets/vue.svg" class="lg:w-36 fill-current text-gray-500" />
            </a>
        </div>

        <div
            class="w-full lg:max-w-md mt-6 px-6 py-4 bg-white dark:bg-gray-800 shadow-md overflow-hidden sm:rounded-lg"
        >
            <slot />
        </div>
    </div>
</template>