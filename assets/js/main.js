document.querySelector('.burger')?.addEventListener('click',()=>document.querySelector('nav.main').classList.toggle('open'));
document.querySelectorAll('[data-year]').forEach(e=>e.textContent=new Date().getFullYear());
document.querySelectorAll('.carousel').forEach(c=>{const t=c.querySelector('.track'),n=t.children.length,d=c.querySelector('.dots');let i=0;
for(let k=0;k<n;k++){const s=document.createElement('span');s.onclick=()=>go(k);d.appendChild(s)}
function go(k){i=(k+n)%n;t.style.transform=`translateX(-${i*100}%)`;[...d.children].forEach((s,j)=>s.classList.toggle('on',j===i))}
c.querySelector('.prev').onclick=()=>go(i-1);c.querySelector('.next').onclick=()=>go(i+1);go(0);const ms=+c.dataset.interval||4000;let timer=setInterval(()=>go(i+1),ms);
c.onmouseenter=()=>clearInterval(timer);c.onmouseleave=()=>timer=setInterval(()=>go(i+1),ms)});
