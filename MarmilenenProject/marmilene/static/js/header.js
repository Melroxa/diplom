document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('burger').addEventListener('click',
        function() {
            document.querySelector('.header__burger','.header__menu').classList.toggle('open');
            document.querySelector('.header__menu').classList.toggle('open');
            document.querySelector('body').classList.toggle('lock')
        })
})