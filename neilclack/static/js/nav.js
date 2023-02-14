function toggleNav() {
    var x = document.getElementById("nav-links");
    x.className = x.className === 'hide-nav' ? 'show-nav' : 'hide-nav';

    var body = document.querySelector('body');
    body.style.overflow = body.style.overflow === '' ? 'hidden' : '';
} 