const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slide');

let index = 0;

function slide() {
    slides[index].style.opacity = 0;
    index = (index + 1) % slides.length;
    slides[index].style.opacity = 1;
}

setInterval(slide, 5000); // Change slide every 5 seconds
