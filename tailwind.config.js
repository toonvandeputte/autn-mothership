/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.{html,jinja}"],
  theme: {
    extend : {
        backgroundImage: {
        },
        colors: {
        },
    },
  },
  plugins: [
    require('@tailwindcss/forms')
  ],
}
