/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'app/templates/*.html'
  ],
  theme: {
    extend: {
      backgroundImage: {
        'background': "[url(./images/background_1.jpeg)]"
      }
    },
  },
  plugins: [],
}
