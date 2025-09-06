module.exports = {
  content: [
    "./selector/templates/**/*.html",
    "./templates/**/*.html",
    "./accounts/templates/**/*.html",
    "./static/**/*.js",
    "./static/**/*.css"
  ],
  safelist: [
    "btn", "btn-primary", "btn-warning", "btn-secondary",
    "card", "card-body", "card-title", "card-actions",
    "sm:grid-cols-2", "md:grid-cols-3", "lg:grid-cols-4"
  ],
  plugins: [require("daisyui")],
};
