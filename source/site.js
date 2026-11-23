/* Resilient Collaborative · shared behaviour for every page */
(()=>{
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const C={ink:'#151515',brick:'#B5452B',paper:'#F4F2EE',mist:'#D8DEE1'};
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)), P=(t,a,b)=>cl((t-a)/(b-a));
const eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2, eqo=x=>1-Math.pow(1-x,5), lerp=(a,b,x)=>a+(b-a)*x;
const mix=(a,b,x)=>{const h=c=>[1,3,5].map(i=>parseInt(c.substr(i,2),16));const A=h(a),B=h(b);return`rgb(${A.map((v,i)=>Math.round(lerp(v,B[i],x))).join(',')})`};

/* the ring: six segments, accent at one o'clock, lifted */
function ring(svg,ink=C.ink,acc=C.brick){
  svg.setAttribute('viewBox','0 0 100 100');
  svg.innerHTML=`<g transform="translate(50 50) scale(0.84) translate(-50 -50)"><g transform="rotate(-84 50 50)" fill="none" stroke-width="22">
    <circle cx="50" cy="50" r="39" stroke="${ink}" stroke-dasharray="0 40.84 32 8.84 32 8.84 32 8.84 32 8.84 32 8.84"/></g>
    <g class="acc" transform="translate(3.7 -6.55)"><g transform="rotate(-84 50 50)" fill="none" stroke-width="22"><circle cx="50" cy="50" r="39" stroke="${acc}" stroke-dasharray="32 213.04"/></g></g></g>`;
}
$$('svg[data-ring]').forEach(s=>ring(s,s.dataset.ring==='light'?C.paper:C.ink));

/* practice icons: one segment per practice lights up */
$$('svg[data-seg]').forEach(s=>{const i=+s.dataset.seg;s.setAttribute('viewBox','0 0 100 100');
  s.innerHTML=`<g transform="translate(50 50) scale(0.84) translate(-50 -50)"><g transform="rotate(-84 50 50)" fill="none" stroke-width="22">${[0,1,2,3,4,5].map(k=>`<circle class="${k===i?'on':''}" cx="50" cy="50" r="39" stroke="${k===i?C.ink:C.mist}" stroke-dasharray="32 213.04" stroke-dashoffset="${-40.84*k}"/>`).join('')}</g></g>`});

/* home hero: the logo builds itself */
const hero=$('#heroRing');
if(hero){
  hero.innerHTML=`<g transform="translate(50 50) scale(0.84) translate(-50 -50)"><g transform="rotate(-84 50 50)" fill="none"><circle id="hR" cx="50" cy="50" r="39" stroke="${C.ink}"/><g id="hAG"><circle id="hA" cx="50" cy="50" r="39" stroke="${C.ink}"/></g></g></g>`;
  const hR=$('#hR'),hA=$('#hA'),hAG=$('#hAG'),a=23.5*Math.PI/180;
  const draw=t=>{const d=eio(P(t,.2,1.5)),th=eio(P(t,1.4,2.3)),gap=8.84*eio(P(t,2.4,3.2)),dash=40.84-gap,sw=lerp(.7,22,th);
    if(gap<=.001){hR.setAttribute('stroke-dasharray',`${(245.04*d+(d>=1?2:0)).toFixed(2)} 300`);hA.style.opacity=0}
    else{hR.setAttribute('stroke-dasharray',`0 40.84 ${Array(5).fill(`${dash.toFixed(2)} ${gap.toFixed(2)}`).join(' ')}`);hA.style.opacity=1}
    hR.setAttribute('stroke-width',sw);hA.setAttribute('stroke-width',sw);
    hA.setAttribute('stroke-dasharray',`${dash.toFixed(2)} ${(245.04-dash).toFixed(2)}`);
    hA.setAttribute('stroke',mix(C.ink,C.brick,eio(P(t,3.2,3.7))));
    const L=9*eqo(P(t,3.4,4.4));hAG.setAttribute('transform',`translate(${(Math.cos(a)*L).toFixed(2)} ${(Math.sin(a)*L).toFixed(2)})`)};
  if(reduce)draw(9);else{const t0=performance.now();const loop=n=>{const t=(n-t0)/1000;draw(t);if(t<4.6)requestAnimationFrame(loop)};requestAnimationFrame(loop)}
  const mk=hero.parentElement;
  mk.addEventListener('pointerenter',()=>{if(reduce)return;hAG.style.transition='transform .6s cubic-bezier(.2,.8,.2,1)';hAG.setAttribute('transform',`translate(${(Math.cos(a)*14).toFixed(2)} ${(Math.sin(a)*14).toFixed(2)})`)});
  mk.addEventListener('pointerleave',()=>hAG.setAttribute('transform',`translate(${(Math.cos(a)*9).toFixed(2)} ${(Math.sin(a)*9).toFixed(2)})`));
}

/* contours: loose loops on canvas, drifting slowly */
function blob(ctx,cx,cy,r,seed,ex,ey,ph){const n=18,p=[];
  for(let k=0;k<n;k++){const t=2*Math.PI*k/n;const rr=r*(1+.08*Math.sin(3*t+seed+ph)+.05*Math.sin(5*t+seed*1.7-ph*.6)+.02*Math.sin(7*t+seed*.4));p.push([cx+rr*Math.cos(t)*ex,cy+rr*Math.sin(t)*ey])}
  ctx.beginPath();ctx.moveTo(p[0][0],p[0][1]);
  for(let i=0;i<n;i++){const A=p[(i-1+n)%n],B=p[i],Cc=p[(i+1)%n],D=p[(i+2)%n];ctx.bezierCurveTo(B[0]+(Cc[0]-A[0])/6,B[1]+(Cc[1]-A[1])/6,Cc[0]-(D[0]-B[0])/6,Cc[1]-(D[1]-B[1])/6,Cc[0],Cc[1])}
  ctx.closePath();ctx.stroke()}
$$('canvas[data-topo]').forEach(cv=>{
  const o=JSON.parse(cv.dataset.topo);const ctx=cv.getContext('2d');let w=0,h=0;
  const size=()=>{const r=cv.getBoundingClientRect(),d=Math.min(devicePixelRatio||1,2);w=r.width;h=r.height;cv.width=w*d;cv.height=h*d;ctx.setTransform(d,0,0,d,0,0)};
  const draw=t=>{ctx.clearRect(0,0,w,h);const s=Math.max(w,h);
    for(let i=0;i<o.n;i++){const acc=i===o.acc;ctx.strokeStyle=acc?C.brick:o.c;ctx.globalAlpha=acc?.55:o.a;ctx.lineWidth=acc?1.6:1;
      blob(ctx,w*o.x+i*s*.006,h*o.y+i*s*.004,s*.06+i*s*.045,o.s+i*.9,1.25+.05*i,.8,t*.00012)}};
  size();addEventListener('resize',()=>{size();draw(performance.now())});
  let vis=true;new IntersectionObserver(e=>{vis=e[0].isIntersecting}).observe(cv);
  if(reduce){draw(0);return}
  const loop=n=>{if(vis)draw(n);requestAnimationFrame(loop)};requestAnimationFrame(loop);
});

/* the one free line on the statement band draws as it comes into view */
$$('svg.line path').forEach(p=>{p.setAttribute('pathLength','1');p.style.strokeDasharray='1 1';p.style.strokeDashoffset=reduce?'0':'1';
  if(!reduce)new IntersectionObserver((e,o)=>{if(e[0].isIntersecting){p.style.transition='stroke-dashoffset 2.4s cubic-bezier(.65,0,.35,1)';p.style.strokeDashoffset='0';o.disconnect()}},{threshold:.4}).observe(p.closest('section'))});

/* the way we work: each stage lights in turn while on screen */
const method=$('.approach4');
if(method){const items=[...method.children];let cur=0,timer=null;
  const set=k=>{cur=k;items.forEach((li,i)=>li.classList.toggle('on',i===k))};set(0);
  items.forEach((li,i)=>{li.addEventListener('mouseenter',()=>{clearInterval(timer);timer=null;set(i)})});
  if(!reduce)new IntersectionObserver(e=>{if(e[0].isIntersecting&&!timer)timer=setInterval(()=>set((cur+1)%items.length),2800);else if(!e[0].isIntersecting){clearInterval(timer);timer=null}},{threshold:.4}).observe(method)}

/* work filters */
const fl=$('.filters');
if(fl){fl.addEventListener('click',e=>{const b=e.target.closest('.filter');if(!b)return;
  fl.querySelectorAll('.filter').forEach(x=>x.setAttribute('aria-pressed',x===b));
  const f=b.dataset.f;$$('.grid .card').forEach(c=>{c.hidden=!(f==='all'||c.dataset.tags.split(' ').includes(f))})})}

/* header, menu, copy email */
const header=$('header.site');
addEventListener('scroll',()=>header.classList.toggle('scrolled',scrollY>8),{passive:true});
const mb=$('.menu-btn');mb&&mb.addEventListener('click',()=>{const o=header.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
$$('[data-copy]').forEach(btn=>btn.addEventListener('click',async()=>{const src=$(btn.dataset.copy),ok=btn.parentElement.querySelector('.ok');
  try{await navigator.clipboard.writeText(src.textContent);ok.textContent='Copied.'}catch(_){const r=document.createRange();r.selectNodeContents(src);const s=getSelection();s.removeAllRanges();s.addRange(r);ok.textContent='Selected. Press Ctrl+C or ⌘C.'}}));

/* reveal below-the-fold blocks */
if(!reduce){const vh=innerHeight;const rvs=$$('.rv').filter(el=>el.getBoundingClientRect().top>vh*.92);
  rvs.forEach(el=>el.classList.add('pre'));
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){const el=e.target;const sib=[...el.parentElement.children].filter(x=>x.classList.contains('rv'));el.style.transitionDelay=(Math.max(0,sib.indexOf(el))%3*90)+'ms';el.classList.remove('pre');io.unobserve(el)}}),{threshold:.1});
  rvs.forEach(el=>io.observe(el))}
})();
