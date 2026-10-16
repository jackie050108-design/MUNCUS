document.querySelector('.burger')?.addEventListener('click',()=>document.querySelector('nav.main').classList.toggle('open'));
document.querySelectorAll('[data-year]').forEach(e=>e.textContent=new Date().getFullYear());
