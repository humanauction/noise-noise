// Track flipped state and loop state
const flippedCards = new Set();
const loopStates = {};

function flipCard(color) {
    const controls = document.getElementById(`controls-${color}`);
    const indicator = document.getElementById(`indicator-${color}`);

    if (flippedCards.has(color)) {
        // Flip back to title view
        controls.classList.remove("show");
        controls.classList.add("hidden");
        indicator.classList.remove("hide");
        flippedCards.delete(color);
    } else {
        // Flip to controls view
        controls.classList.remove("hidden");
        controls.classList.add("show");
        indicator.classList.add("hide");
        flippedCards.add(color);
    }
}

function play(color) {
    const audio = document.getElementById(`audio-${color}`);
    audio.play().catch((e) => console.log("Audio play failed:", e));
}

function pause(color) {
    const audio = document.getElementById(`audio-${color}`);
    audio.pause();
}

function toggleLoop(color) {
    const audio = document.getElementById(`audio-${color}`);
    const loopBtn = document.getElementById(`loop-btn-${color}`);

    audio.loop = !audio.loop;
    loopStates[color] = audio.loop;

    // Update button appearance
    if (audio.loop) {
        loopBtn.classList.add("btn-active");
    } else {
        loopBtn.classList.remove("btn-active");
    }
}

function setVolume(color, volume) {
    const audio = document.getElementById(`audio-${color}`);
    audio.volume = volume;
}

// Initialize volume for all audio elements when page loads
document.addEventListener("DOMContentLoaded", function () {
    const colors = [
        "white",
        "pink",
        "red",
        "blue",
        "purple",
        "yellow",
        "brown",
        "green",
    ];
    colors.forEach((color) => {
        setVolume(color, 0.5);
    });
});
