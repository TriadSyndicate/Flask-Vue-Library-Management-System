/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
  darkMode: 'class', // or 'media' or 'class' or false
}

