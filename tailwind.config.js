/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.html",
        "./static/**/*.js",
        "./**/templates/**/*.html",
        "./selector/templates/**/*.html",
        "./accounts/templates/**/*.html",
    ],
    theme: {
        screens: {
            sm: "640px",
            md: "768px",
            lg: "1024px",
            xl: "1280px",
        },
        extend: {},
    },
    plugins: [require("daisyui")],
};
