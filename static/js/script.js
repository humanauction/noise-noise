document.addEventListener("DOMContentLoaded", function () {
    const select = document.getElementById("theme-select");
    if (select) {
        console.log("Theme select found");
        select.addEventListener("change", function () {
            console.log("Theme changed to:", select.value);
        });
    } else {
        console.log("Theme select NOT found");
    }
});

document.addEventListener("change", function (e) {
    if (
        e.target &&
        e.target.matches("select[data-choose-theme], [data-set-theme]")
    ) {
        var theme = document.documentElement.getAttribute("data-theme");
        document.body.setAttribute("data-theme", theme);
    }
});
