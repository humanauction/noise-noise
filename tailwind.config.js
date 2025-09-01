module.exports = {
    content: [
        "./templates/**/*.html",
        "./static/**/*.js",
        "./selector/templates/**/*.html",
        "./accounts/templates/**/*.html",
    ],
    theme: {
        extend: {},
    },
    plugins: [require("daisyui")],
};
