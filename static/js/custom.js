var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    loop: true,
    speed: 500,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
        hideOnClick: true,
        hiddenClass: 'my-button-hidden'
    },
    autoplay: {
        delay: 4000,
        disableOnInteraction: false,
    },
});


var swiper = new Swiper(".mySwiper2", {
    slidesPerView: 1,
    loop: true,
    speed: 500,
    autoplay: {
        delay: 4000,
        disableOnInteraction: false,
    },
});


window.addEventListener("scroll", () => {
    const navBar = document.querySelector(".navbar");
    const scrollHeight = window.pageYOffset;
    const navHeight = navBar.getBoundingClientRect().height;

    if (scrollHeight > navHeight) {
        navBar.classList.add("fix-nav");
    } else {
        navBar.classList.remove("fix-nav");
    }
});