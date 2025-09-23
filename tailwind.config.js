module.exports = {
  content: [
    "./selector/templates/**/*.html",
    "./templates/**/*.html",
    "./accounts/templates/**/*.html",
    "./static/**/*.js",
    "./static/**/*.css",
    "./theme/static_src/src/**/*.{html,js,css}",
    "./theme/static_src/src/**/*.{html,js,css}",
  ],
  safelist:['bg-white', 'bg-pink-500', 'bg-red-500', 'bg-blue-500', 
    'bg-purple-500', 'bg-yellow-500', 'bg-yellow-900', 'bg-green-500',
    'text-white', 'text-black',
    'btn', 'btn-primary', 'btn-warning', 'btn-secondary', 'btn-active', 'btn-outline',],

  plugins: [require("daisyui")],
};
