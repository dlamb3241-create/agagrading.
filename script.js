
const ROTATE_MS = 5000;
function getDominantColor(imgEl, cb){
  const canvas=document.createElement('canvas');
  const ctx=canvas.getContext('2d',{willReadFrequently:true});
  const w=canvas.width=24, h=canvas.height=24;
  try{
    ctx.drawImage(imgEl,0,0,w,h);
    const d=ctx.getImageData(0,0,w,h).data;
    let r=0,g=0,b=0,n=0;
    for(let i=0;i<d.length;i+=4){
      const rr=d[i],gg=d[i+1],bb=d[i+2],aa=d[i+3];
      if(aa<220) continue;
      if(rr+gg+bb<100) continue;
      r+=rr; g+=gg; b+=bb; n++;
    }
    if(!n) return cb('#16a34a');
    r=Math.round(r/n); g=Math.round(g/n); b=Math.round(b/n);
    cb(`rgb(${r}, ${g}, ${b})`);
  }catch(e){ cb('#16a34a'); }
}
function showIndex(i){
  const imgs=[...document.querySelectorAll('.hero img')];
  imgs.forEach(el=>el.classList.remove('visible'));
  const next=imgs[i%imgs.length];
  next.classList.add('visible');
  getDominantColor(next, c=> document.documentElement.style.setProperty('--accent', c));
}
function startRotation(){
  const imgs=[...document.querySelectorAll('.hero img')];
  if(!imgs.length) return;
  let i=0; showIndex(i);
  setInterval(()=>{ i=(i+1)%imgs.length; showIndex(i); }, ROTATE_MS);
}
document.addEventListener('DOMContentLoaded', ()=>{
  const y=document.getElementById('year'); if(y) y.textContent=new Date().getFullYear();
  startRotation();
});
