const navSlide = () => {
    const burger = document.querySelector(".burger");
    const nav = document.querySelector(".nav-links");
    const navLinks = document.querySelectorAll(".nav-links li")
 
 
    burger.addEventListener("click", () => {
        // Togle burger
        nav.classList.toggle("nav-active");
 
        // Animation nav-links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = "";
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.2}s`;
            }
        });
        // Burger animation
        burger.classList.toggle("toggle");
    });
 }
 
 navSlide();
 
 // Buffer for animations during resizing the browser
 let resizeTimer;
 window.addEventListener("resize", () => {
    document.body.classList.add("resize-animation-stopper");
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        document.body.classList.remove("resize-animation-stopper");
    }, 400);
 });