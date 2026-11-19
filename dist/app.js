
/* ===== EDIT YOUR SOCIAL LINKS HERE ===== */
const SOCIAL={instagram:'https://www.instagram.com/dorapdf.official/',facebook:'https://www.facebook.com/share/1A6nYCu3bz/',tiktok:'',youtube:'',pinterest:'https://pin.it/56yYCL0yL',x:'',linkedin:''};
document.querySelectorAll('.soc').forEach(a=>{const u=SOCIAL[a.dataset.soc];if(u)a.href=u;else a.classList.add('off')});
if(!Object.values(SOCIAL).some(Boolean))document.querySelectorAll('.soc').forEach(a=>a.classList.remove('off'));
/* ---------- helpers ---------- */
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const toast=(t)=>{const e=$('#toast');e.textContent=t;e.classList.add('on');clearTimeout(e._t);e._t=setTimeout(()=>e.classList.remove('on'),2600)};
const libs={};
const NPM_MAP={'jspdf':['jspdf','dist/jspdf.umd.min.js'],'pdf-lib':['pdf-lib','dist/pdf-lib.min.js'],'jszip':['jszip','dist/jszip.min.js'],'xlsx':['xlsx','dist/xlsx.full.min.js'],'mammoth':['mammoth','mammoth.browser.min.js'],'marked':['marked','marked.min.js'],'qrcodejs':['qrcodejs','qrcode.min.js'],'jsbarcode':['jsbarcode','dist/JsBarcode.all.min.js'],'html2canvas':['html2canvas','dist/html2canvas.min.js']};
function mirrors(src){const out=[src];let m=src.match(/cdnjs\.cloudflare\.com\/ajax\/libs\/([^/]+)\/([^/]+)\/(.+)$/);
  if(m){const [,lib,ver,file]=m;if(lib==='pdf.js'){out.push(`https://cdn.jsdelivr.net/npm/pdfjs-dist@${ver}/build/${file}`,`https://unpkg.com/pdfjs-dist@${ver}/build/${file}`)}else if(NPM_MAP[lib]){const [p,f]=NPM_MAP[lib];out.push(`https://cdn.jsdelivr.net/npm/${p}@${ver}/${f}`,`https://unpkg.com/${p}@${ver}/${f}`)}}
  else if((m=src.match(/cdn\.jsdelivr\.net\/npm\/(.+)$/))&&!/\+esm/.test(src))out.push('https://unpkg.com/'+m[1]);
  const SELF={'jspdf':'/vendor/jspdf.umd.min.js'};for(const k in SELF)if(src.includes('/'+k+'/')||src.includes('/'+k+'@'))out.push(SELF[k]);
  return out}
function loadOne(u){return new Promise((ok,no)=>{const s=document.createElement('script');s.src=u;s.async=true;s.onload=()=>ok(u);s.onerror=()=>{s.remove();no(new Error('net'))};document.head.appendChild(s)})}
function loadScript(src){return libs[src]||(libs[src]=(async()=>{for(const u of mirrors(src)){for(let t=0;t<2;t++){try{await loadOne(u);libs.__used=libs.__used||{};libs.__used[src]=u;return}catch(e){}}}delete libs[src];throw new Error('DORA_LOAD')})())}
function friendlyErr(e){const m=(e&&e.message)||'';if(m==='DORA_LOAD'||/^load https?:/.test(m)||/Failed to fetch|NetworkError|Load failed/i.test(m))return 'Couldn’t load part of this tool. Check your internet, or pause your ad-blocker for dorapdf.com, then try again.';if(/out of memory|allocation|Array buffer/i.test(m))return 'This file is too big for your device’s memory. Try fewer or smaller files at a time.';if(/password|encrypt/i.test(m))return 'This PDF is password-protected. Unlock it first with Unlock PDF.';if(!m||m.length>140||/https?:\/\/|undefined|null|TypeError|ReferenceError|is not a function|Cannot read/i.test(m))return 'Something went wrong with this file. Try another file, or refresh the page and try again.';return m}
const CDN={
  jspdf:'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js',
  pdf:'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js',
  pdfw:'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js',
  xlsx:'https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js',
  mammoth:'https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.6.0/mammoth.browser.min.js',
  jszip:'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js'
};
async function loadPdf(){await loadScript(CDN.pdfw);await loadScript(CDN.pdf);pdfjsLib.GlobalWorkerOptions.workerSrc=(libs.__used&&libs.__used[CDN.pdfw])||CDN.pdfw;return pdfjsLib}
const hasClaude=()=>window.claude&&typeof window.claude.use==='function';
let dlNS=null, sampleNS=null;
if(hasClaude()){claude.use('downloads').then(d=>dlNS=d).catch(()=>{});}
async function saveFile(name,blob){
  if(dlNS){try{await dlNS.save({filename:name,data:blob});toast('Saved ✓ '+name);return}catch(e){if(e&&e.code==='declined'){toast('Download cancelled');return}}}
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(a.href),4000);toast('Downloading '+name);
  try{setTimeout(revAsk,900)}catch(e){}
}
const base=n=>n.replace(/\.[^.]+$/,'');
const readAB=f=>f.arrayBuffer();
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

/* ---------- SFX (WebAudio) ---------- */
let actx=null, sfxOn=true;
try{sfxOn=localStorage.getItem('tv_sfx')!=='0'}catch(e){}
function ac(){if(!actx){try{actx=new (window.AudioContext||window.webkitAudioContext)()}catch(e){}}if(actx&&actx.state==='suspended')actx.resume().catch(()=>{});return actx}
function tone(f1,f2,dur,vol,type='sine'){if(!sfxOn||!actx||actx.state!=='running')return;const t=actx.currentTime,o=actx.createOscillator(),g=actx.createGain();o.type=type;o.frequency.setValueAtTime(f1,t);o.frequency.exponentialRampToValueAtTime(f2,t+dur);g.gain.setValueAtTime(0,t);g.gain.linearRampToValueAtTime(vol,t+.008);g.gain.exponentialRampToValueAtTime(.0001,t+dur);o.connect(g).connect(actx.destination);o.start(t);o.stop(t+dur+.02)}
const sHover=()=>tone(1800,2400,.045,.018,'sine');
const sClick=()=>{tone(520,980,.09,.05,'triangle');setTimeout(()=>tone(980,1400,.07,.03,'sine'),45)};
const sDone=()=>{[660,880,1320].forEach((f,i)=>setTimeout(()=>tone(f,f*1.01,.18,.04,'sine'),i*90))};
document.addEventListener('pointerdown',()=>ac(),{capture:true});
document.addEventListener('mouseover',e=>{const t=e.target.closest('[data-sfx],.tool');if(t&&t!==document._lastHover){document._lastHover=t;sHover()}});
document.addEventListener('click',e=>{if(e.target.closest('[data-sfx],.tool'))sClick()});
function paintSfx(){$('#sfxBtn').classList.toggle('off',!sfxOn);$('#wave').style.display=sfxOn?'':'none'}
$('#sfxBtn').onclick=()=>{sfxOn=!sfxOn;try{localStorage.setItem('tv_sfx',sfxOn?'1':'0')}catch(e){}paintSfx();toast(sfxOn?'Sound on 🔊':'Sound off')};
$('#themeBtn').onclick=()=>{const r=document.documentElement;const t=r.dataset.theme==='light'?'dark':'light';r.dataset.theme=t;try{localStorage.setItem('dp_theme',t)}catch(e){}toast(t==='light'?'☀️ Light mode':'🌙 Dark mode')};
paintSfx();

/* ---------- motion ---------- */
window.addEventListener('load',()=>setTimeout(()=>$('#loader').classList.add('done'),700));
setTimeout(()=>$('#loader').classList.add('done'),3000);
const dot=$('#dot'),glow=$('#glow');
let mx=innerWidth/2,my=innerHeight/2,gx=mx,gy=my;
addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;dot.style.left=mx+'px';dot.style.top=my+'px';
  const m=$('#mascotIn');const dx=(mx/innerWidth-.5),dy=(my/innerHeight-.5);m.style.transform=`rotateY(${dx*18}deg) rotateX(${-dy*14}deg) translate(${dx*20}px,${dy*14}px)`;
  const eyes=document.getElementById('eyes');if(eyes)eyes.setAttribute('transform',`translate(${dx*14} ${dy*8})`);
});
(function loop(){gx+=(mx-gx)*.08;gy+=(my-gy)*.08;glow.style.left=gx+'px';glow.style.top=gy+'px';requestAnimationFrame(loop)})();
document.addEventListener('mouseover',e=>dot.classList.toggle('big',!!e.target.closest('a,button,.tool,label')));
$('#mascot').style.perspective='800px';
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.15});
function observe(){$$('.reveal:not(.in)').forEach(el=>io.observe(el))}
addEventListener('scroll',()=>{const y=scrollY;$('.bigword').style.transform=`translateX(-50%) translateY(${y*.35}px)`;const p=$('#phone');const r=p.getBoundingClientRect();p.style.transform=`translateY(${Math.max(-30,Math.min(30,(r.top-innerHeight/2)*-.06))}px)`},{passive:true});
// phone typing
const titles=['Climate Change & Agriculture','Artificial Intelligence in Healthcare','The French Revolution','Photosynthesis Explained'];
(function typer(i=0,j=0,del=false){const el=$('#ptitle'),t=titles[i];el.textContent=t.slice(0,j);if(!del&&j<t.length)return setTimeout(()=>typer(i,j+1),70);if(!del)return setTimeout(()=>typer(i,j,true),1600);if(j>0)return setTimeout(()=>typer(i,j-1,true),30);typer((i+1)%titles.length,0,false)})();

const IC={
 word:'<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Z"/><path d="M14 3v6h6M8 13l1.5 5 2.5-4 2.5 4 1.5-5"/>',
 xls:'<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Z"/><path d="M14 3v6h6M8 12h8v6H8zM12 12v6M8 15h8"/>',
 img:'<rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="9" cy="9" r="2"/><path d="m21 15-5-5L5 21"/>',
 pdf:'<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Z"/><path d="M14 3v6h6"/><text x="7" y="18" font-size="6" fill="#fff" stroke="none" font-family="sans-serif" font-weight="700">PDF</text>',
 bg:'<path d="M12 3a9 9 0 1 0 0 18"/><path d="M12 3v18" stroke-dasharray="2 2"/><circle cx="12" cy="10" r="3"/><path d="M7 18c1-2.5 3-3.5 5-3.5"/>',
 conv:'<path d="M4 7h13l-3-3M20 17H7l3 3"/>'
};
/* ---------- TOOL FRAMEWORK ---------- */
Object.assign(CDN,{
  pdflib:'https://cdnjs.cloudflare.com/ajax/libs/pdf-lib/1.17.1/pdf-lib.min.js',
  h2c:'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js',
  marked:'https://cdnjs.cloudflare.com/ajax/libs/marked/4.3.0/marked.min.js',
  pptx:'https://cdn.jsdelivr.net/npm/pptxgenjs@3.12.0/dist/pptxgen.bundle.js',
  qr:'https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js',
  barcode:'https://cdnjs.cloudflare.com/ajax/libs/jsbarcode/3.11.6/JsBarcode.all.min.js',
  heic:'https://cdn.jsdelivr.net/npm/heic2any@0.0.4/dist/heic2any.min.js',
  exifr:'https://cdn.jsdelivr.net/npm/exifr@7.1.3/dist/full.umd.js',
  tracer:'https://cdn.jsdelivr.net/npm/imagetracerjs@1.2.6/imagetracer_v1.2.6.js',
  gifenc:'https://cdn.jsdelivr.net/npm/gifenc@1.0.3/dist/gifenc.esm.js'
});
const h=(tag,a={},...kids)=>{const e=document.createElement(tag);for(const k in a){const v=a[k];if(v===false||v==null)continue;if(k==='class')e.className=v;else if(k==='style')e.style.cssText=v;else if(k.startsWith('on')&&typeof v==='function')e.addEventListener(k.slice(2),v);else if(k==='html')e.innerHTML=v;else if(k==='value')e.value=v;else if(k==='checked')e.checked=!!v;else e.setAttribute(k,v===true?'':v)}kids.flat(9).forEach(c=>{if(c==null||c===false)return;e.append(c.nodeType?c:document.createTextNode(String(c)))});return e};
const fmtN=(n,d=2)=>isFinite(n)?Number(n).toLocaleString('en-US',{maximumFractionDigits:d}):'—';
const money=(n,cur='')=>isFinite(n)?cur+Number(n).toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2}):'—';
const sz=b=>b>1048576?(b/1048576).toFixed(2)+' MB':(b/1024).toFixed(1)+' KB';
async function copyText(t){try{await navigator.clipboard.writeText(t);toast('Copied ✓')}catch(e){toast('Copy blocked — select the text and copy')}}
const textBlob=(t,type='text/plain')=>new Blob([t],{type});

const U={
  row:(...k)=>h('div',{class:'urow'},...k),
  field:(label,el,cls='')=>h('label',{class:'ufield '+cls},h('span',{},label),el),
  inp:(a={})=>h('input',{class:'uin',...a}),
  num:(v,a={})=>h('input',{class:'uin',type:'number',step:'any',value:v,...a}),
  sel:(opts,a={})=>{const s=h('select',{class:'uin',...a},...opts.map(o=>Array.isArray(o)?h('option',{value:o[0]},o[1]):h('option',{value:o},o)));if(a.value!=null)s.value=a.value;return s},
  ta:(a={})=>h('textarea',{class:'uin uta',...a}),
  chk:(label,on=false)=>{const i=h('input',{type:'checkbox',checked:on});const l=h('label',{class:'ucheck'},i,label);l.input=i;return l},
  btn:(t,fn,cls='btn btn-p')=>h('button',{class:cls,'data-sfx':'',type:'button',onclick:fn},t),
  copy:get=>U.btn('Copy',()=>copyText(typeof get==='function'?get():get.value),'btn btn-g'),
  res(root){const r=h('div',{class:'res'});root.append(r);return{el:r,set(items){r.innerHTML='';items.forEach(([l,v,big])=>r.append(h('div',{class:'rcard'+(big?' big':'')},h('small',{},l),h('b',{},v))))}}},
  prog(root){const b=h('div',{class:'prog'},h('i'));root.append(b);return p=>{b.style.display='block';b.firstChild.style.width=Math.round(Math.min(1,p)*100)+'%'}},
  out(root){const l=h('div',{class:'flist'});root.append(l);return{el:l,clear(){l.innerHTML=''},add(name,blob,label){l.append(h('div',{class:'fitem'},h('span',{},'✅ '+(label||name)+' · '+sz(blob.size)),h('button',{class:'dl','data-sfx':'',onclick:()=>saveFile(name,blob)},'Download')))}}},
  drop(root,{accept='*',multi=false,hint='',onFiles}){const inp=h('input',{type:'file',accept,hidden:true,multiple:multi});const d=h('label',{class:'drop','data-sfx':''},inp,h('div',{html:'<svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#ff2e88" stroke-width="1.6"><path d="M12 16V4m0 0-4 4m4-4 4 4"/><path d="M4 16v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2"/></svg>'}),h('div',{class:'big'},multi?'Drop files here':'Drop a file here'),h('small',{},hint||'or click to choose'));
    ['dragenter','dragover'].forEach(ev=>d.addEventListener(ev,e=>{e.preventDefault();d.classList.add('over')}));['dragleave','drop'].forEach(ev=>d.addEventListener(ev,e=>{e.preventDefault();d.classList.remove('over')}));
    d.addEventListener('drop',e=>onFiles([...e.dataTransfer.files]));inp.onchange=()=>{onFiles([...inp.files]);inp.value=''};root.append(d);return d}
};

/* pattern: file tool */
function fileTool(root,{accept='*',multi=false,hint,opts,go,btn='Convert now ✦',auto=false,list=true}){
  let files=[];const optBox=h('div');const lst=h('div',{class:'flist'});
  U.drop(root,{accept,multi,hint,onFiles:fs=>{files=multi?files.concat(fs):fs.slice(0,1);paint();if(auto&&files.length)run()}});
  if(opts){const o=opts();(Array.isArray(o)?o:[o]).forEach(x=>x&&optBox.append(x))}
  root.append(optBox,lst);
  const b=U.btn(btn,()=>run());b.style.cssText='width:100%;justify-content:center;display:none';root.append(b);
  const setP=U.prog(root);const out=U.out(root);const extra=h('div');root.append(extra);
  function paint(){lst.innerHTML='';if(list)files.forEach((f,i)=>lst.append(h('div',{class:'fitem'},h('span',{},'📄 '+f.name),h('small',{style:'color:var(--mute)'},sz(f.size)),multi?h('button',{class:'rm',onclick:()=>{files.splice(i,1);paint()}},'✕'):null)));b.style.display=files.length&&!auto?'flex':'none'}
  async function run(){if(!files.length)return;b.disabled=true;const t=b.textContent;b.textContent='Working…';out.clear();extra.innerHTML='';setP(.05);
    try{await go(files,{out,prog:setP,extra});setP(1);sDone();toast('Done ✦')}catch(e){console.error(e);toast('⚠️ '+friendlyErr(e))}
    b.disabled=false;b.textContent=t}
  return{get files(){return files}}
}
/* pattern: text in -> text out */
function textTool(root,{fn,opts,ph='Type or paste text here…',live=true,outPh='Result',dl}){
  const o=opts?opts():[];const optRow=U.row(...(Array.isArray(o)?o:[o]));
  const a=U.ta({placeholder:ph}),b=U.ta({placeholder:outPh,readonly:true});
  const run=()=>{try{b.value=a.value?fn(a.value):''}catch(e){b.value='⚠️ '+e.message}};
  root.append(o.length?optRow:'',h('div',{class:'urow'},U.field('Input',a,'full')),live?'':U.btn('Convert ✦',run),h('div',{class:'urow'},U.field('Output',b,'full')),U.row(U.copy(()=>b.value),U.btn('Clear',()=>{a.value='';b.value=''},'btn btn-g'),dl?U.btn('Download',()=>b.value&&saveFile(dl,textBlob(b.value)),'btn btn-g'):null));
  if(live){a.addEventListener('input',run);optRow.addEventListener('input',run);optRow.addEventListener('change',run)}
  return{a,b,run};
}
/* pattern: calculator */
function calcTool(root,{fields,calc,note}){
  const els={};const row=h('div',{class:'urow'});
  fields.forEach(f=>{let el;if(f.o)el=U.sel(f.o,{value:f.v});else el=U.inp({type:f.t||'number',step:'any',value:f.v??''});els[f.k]=el;row.append(U.field(f.l,el,f.full?'full':''))});
  root.append(row);const r=U.res(root);if(note)root.append(h('p',{class:'note'},note));
  const run=()=>{const v={};for(const k in els){const f=fields.find(x=>x.k===k);v[k]=(f.t&&f.t!=='number')||f.o?els[k].value:parseFloat(els[k].value)}try{r.set(calc(v))}catch(e){r.set([['Error',e.message]])}};
  row.addEventListener('input',run);row.addEventListener('change',run);run();return{els,run}
}
/* pattern: generator */
function genTool(root,{opts,gen,btn='Generate ✦',mono=true,rows=8}){
  const o=opts?opts():[];root.append(U.row(...o));const out=U.ta({readonly:true,rows});if(!mono)out.style.fontFamily='inherit';
  const run=()=>{out.value=gen()};root.append(U.row(U.btn(btn,run),U.copy(()=>out.value)),h('div',{class:'urow'},U.field('Result',out,'full')));run();return{run,out}
}

/* image helpers for tools */
function canvasOf(w,h2){const c=document.createElement('canvas');c.width=w;c.height=h2;return c}
async function imgFromFile(f){if(/heic|heif/i.test(f.type)||/\.hei[cf]$/i.test(f.name)){await loadScript(CDN.heic);const b=await heic2any({blob:f,toType:'image/png'});return loadImg(Array.isArray(b)?b[0]:b)}return loadImg(f)}
const extOf=t=>({jpeg:'jpg','image/jpeg':'jpg',png:'png','image/png':'png',webp:'webp','image/webp':'webp'})[t]||t;
function imgConvertTool(root,{to,accept='image/*',bg}){fileTool(root,{accept,multi:true,opts:()=>to==='jpeg'||to==='webp'?[U.row(U.field('Quality',h('input',{class:'uin',type:'range',min:40,max:100,value:92,id:'q_'+to})))]:null,
  go:async(fs,{out,prog})=>{for(let i=0;i<fs.length;i++){const im=await imgFromFile(fs[i]);const c=drawTo(im,0,to==='jpeg'?'#fff':bg);const q=($('#q_'+to)||{value:92}).value/100;out.add(base(fs[i].name)+'.'+extOf(to),await canvasBlob(c,'image/'+to,q));prog((i+1)/fs.length)}}})}
async function pdfDoc(file,password){const lib=await loadPdf();return lib.getDocument({data:await readAB(file),password}).promise}
async function renderPage(doc,n,scale=2){const pg=await doc.getPage(n);const vp=pg.getViewport({scale});const c=canvasOf(vp.width,vp.height);const x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,c.width,c.height);await pg.render({canvasContext:x,viewport:vp,intent:'print'}).promise;return c}
async function pdfLib(){await loadScript(CDN.pdflib);return PDFLib}
function parseRanges(s,max){const out=new Set();String(s).split(',').map(x=>x.trim()).filter(Boolean).forEach(p=>{const m=p.match(/^(\d+)\s*-\s*(\d+)$/);if(m){for(let i=+m[1];i<=+m[2];i++)if(i>=1&&i<=max)out.add(i)}else if(/^\d+$/.test(p)&&+p>=1&&+p<=max)out.add(+p)});return[...out].sort((a,b)=>a-b)}
async function canvasesToPdf(cs,opts={}){await loadScript(CDN.jspdf);const {jsPDF}=window.jspdf;let doc=null;for(const c of cs){const w=c.width,hh=c.height,o=w>hh?'l':'p';const fmt=[w*.75,hh*.75];if(!doc)doc=new jsPDF({orientation:o,unit:'pt',format:fmt,...opts});else doc.addPage(fmt,o);doc.addImage(c.toDataURL('image/jpeg',opts.q||.9),'JPEG',0,0,fmt[0],fmt[1])}return doc.output('blob')}
async function htmlToPdf(html,name){await loadScript(CDN.jspdf);await loadScript(CDN.h2c);const box=h('div',{style:'position:fixed;left:-10000px;top:0;width:794px;padding:56px;background:#fff;color:#111;font:14px/1.6 Georgia,serif',html});box.querySelectorAll('img').forEach(i=>i.style.maxWidth='100%');box.querySelectorAll('table').forEach(t=>{t.style.borderCollapse='collapse';t.querySelectorAll('td,th').forEach(c=>c.style.cssText='border:1px solid #ccc;padding:4px 6px')});document.body.append(box);
  try{const c=await html2canvas(box,{scale:2,backgroundColor:'#fff'});const pageH=Math.round(c.width*297/210);const pages=[];for(let y=0;y<c.height;y+=pageH){const p=canvasOf(c.width,Math.min(pageH,c.height-y));p.getContext('2d').drawImage(c,0,-y);const full=canvasOf(c.width,pageH);const fx=full.getContext('2d');fx.fillStyle='#fff';fx.fillRect(0,0,full.width,full.height);fx.drawImage(p,0,0);pages.push(full)}
  await loadScript(CDN.jspdf);const {jsPDF}=window.jspdf;const doc=new jsPDF({unit:'mm',format:'a4'});pages.forEach((p,i)=>{if(i)doc.addPage();doc.addImage(p.toDataURL('image/jpeg',.92),'JPEG',0,0,210,297)});return doc.output('blob')}finally{box.remove()}}
async function textToPdf(title,text){await loadScript(CDN.jspdf);const {jsPDF}=window.jspdf;const doc=new jsPDF({unit:'pt',format:'a4'});const M=56,W=595-2*M;let y=M;doc.setFont('helvetica','bold');doc.setFontSize(16);if(title){doc.splitTextToSize(title,W).forEach(l=>{doc.text(l,M,y);y+=22});y+=8}doc.setFont('helvetica','normal');doc.setFontSize(11);
  String(text).replace(/\r/g,'').split('\n').forEach(par=>{const lines=par.trim()?doc.splitTextToSize(par,W):[''];lines.forEach(l=>{if(y>842-M){doc.addPage();y=M}doc.text(l,M,y);y+=15});y+=3});return doc.output('blob')}

/* registry + UI */
const CATS=[['popular','🔥 Most used'],['all','All'],['pdf','PDF & Documents'],['image','Image & Media'],['ai','AI Tools'],['design','Designer Tools'],['dev','Developer Tools'],['text','Text Tools'],['business','Business & Office'],['calc','Calculators & Units'],['fun','Fun & Games']];
const CATN={pdf:'PDF & Document Tools',image:'Image & Media Tools',ai:'AI Tools',design:'Designer Tools',dev:'Developer Tools',text:'Text Tools',business:'Business & Office Tools',calc:'Calculators & Unit Converters',fun:'Fun & Games',convert:'Converters',pro:'Professional'};
const GROUPS={"pdf-to-word":"pdf","pdf-merger":"pdf","pdf-compressor":"pdf","url-to-pdf":"pdf","pdf-image-watermark":"pdf","pdf-text-watermark":"pdf","pdf-editor":"pdf","unlock-pdf":"pdf","protect-pdf":"pdf","images-to-pdf":"pdf","png-to-pdf":"pdf","heic-to-pdf":"pdf","pdf-to-markdown":"pdf","pdf-to-txt":"pdf","highlight-pdf":"pdf","word-to-pdf":"pdf","docx-to-pdf":"pdf","sign-pdf":"pdf","markdown-to-pdf":"pdf","pdf-image-extractor":"pdf","rotate-pdf":"pdf","delete-pdf-pages":"pdf","redact-pdf":"pdf","epub-to-pdf":"pdf","email-to-pdf":"pdf","odf-to-pdf":"pdf","pdf-to-excel":"pdf","pdf-to-powerpoint":"pdf","pdf-splitter":"pdf","pptx-to-pdf":"pdf","pdf-ocr":"pdf","scan-to-pdf":"pdf","pdf-to-jpg":"pdf","pdf-to-png":"pdf","odf-to-jpg":"pdf","odf-to-png":"pdf","zip-extractor":"pdf","csv-to-json":"pdf","illustrator-to-png":"image","image-compressor":"image","gif-maker":"image","heic-to-jpg":"image","heic-to-png":"image","webp-to-jpg":"image","jpg-to-png":"image","avif-to-jpg":"image","avif-to-png":"image","jpeg-to-png":"image","png-to-jpg":"image","png-to-webp":"image","webp-to-png":"image","svg-to-png":"image","png-to-svg":"image","webp-to-svg":"image","gps-photo-stamper":"image","image-flipper":"image","image-resizer":"image","compress-gif":"image","video-compressor":"image","tab-audio-recorder":"image","image-background-remover":"ai","image-to-text":"ai","image-upscaler":"ai","watermark-eraser":"ai","object-remover":"ai","image-color-picker":"design","color-palette-generator":"design","color-code-converter":"design","css-gradient-generator":"design","box-shadow-generator":"design","mesh-gradient-generator":"design","glassmorphism-generator":"design","linkedin-photo-frame":"design","youtube-thumbnail":"design","ascii-art":"design","web-to-png":"design","password-generator":"dev","uuid-generator":"dev","json-validator":"dev","regex-tester":"dev","base64":"dev","url-encoder":"dev","jwt-decoder":"dev","sql-formatter":"dev","binary-to-text":"dev","url-breakpoint-preview":"dev","open-graph-checker":"dev","lorem-ipsum":"dev","word-counter":"text","text-formatter":"text","text-replace":"text","unicode-text-generator":"text","glitch-text":"text","invisible-character":"text","leetspeak":"text","morse-code":"text","braille-translator":"text","wingdings-translator":"text","numbers-to-words":"text","roman-numerals":"text","mocking-text":"text","text-to-emoji":"text","upside-down-text":"text","vaporwave-text":"text","word-unscrambler":"text","qr-code-generator":"business","barcode-generator":"business","invoice-generator":"business","receipt-generator":"business","resume-builder":"business","email-signature":"business","email-subject-preview":"business","tweet-previewer":"business","link-shortener":"business","pomodoro-timer":"business","currency-converter":"business","celsius-to-fahrenheit":"calc","liters-to-gallons":"calc","miles-to-km":"calc","km-to-miles":"calc","ounces-to-grams":"calc","hours-to-minutes":"calc","cm-to-m":"calc","feet-to-cm":"calc","feet-to-meter":"calc","feet-to-miles":"calc","foot-to-inch":"calc","inch-to-cm":"calc","inch-to-mm":"calc","inches-to-feet":"calc","lbs-to-kg":"calc","meter-to-inch":"calc","meters-to-miles":"calc","ml-to-oz":"calc","mortgage-calculator":"calc","loan-calculator":"calc","interest-calculator":"calc","investment-calculator":"calc","retirement-calculator":"calc","paycheck-calculator":"calc","salary-calculator":"calc","sales-tax-calculator":"calc","tip-calculator":"calc","discount-calculator":"calc","commission-calculator":"calc","profit-margin-calculator":"calc","roi-calculator":"calc","percentage-calculator":"calc","fraction-calculator":"calc","random-number-generator":"calc","calorie-calculator":"calc","bmi-calculator":"calc","due-date-calculator":"calc","gpa-calculator":"calc","countdown-timer":"calc","days-until":"calc","date-to-age":"calc","time-zone-converter":"calc","2048-game":"fun","typewriter-simulator":"fun","hacker-typer":"fun"};
const ICONS={pdf:IC.pdf,image:IC.img,convert:IC.conv,calc:'<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M8 6h8M8 11h2M12 11h2M16 11h0M8 15h2M12 15h2M8 19h2M12 19h4"/>',pro:'<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>',fun:'<circle cx="12" cy="12" r="9"/><path d="M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/>',word:IC.word,xls:IC.xls,img:IC.img,bg:IC.bg,conv:IC.conv};
const REAL=/(^|\.)dorapdf\.com$/.test(location.hostname);
const TV={list:[],cat:'popular',q:'',
  add(t){t.id=t.id||t.name.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');if(t.soon)return;if(!t.ic)t.ic=t.cat;t.cat=GROUPS[t.id]||t.cat;this.list.push(t)},
  card(t){const ic=ICONS[t.ic]||ICONS[t.cat];const el=h('a',{class:'tool','data-id':t.id,href:t.soon?'#t-'+t.id:'/'+t.id+'/',html:`<div class="ti"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6">${ic}</svg></div><h3>${esc(t.name)}</h3><p>${esc(t.desc)}</p><span class="go">↗</span><span class="cat">${CATN[t.cat]}</span>${t.soon?'<span class="soon">Coming soon</span>':''}`});
    el.addEventListener('mousemove',e=>{const r=el.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;el.style.setProperty('--mx',x+'px');el.style.setProperty('--my',y+'px');el.style.transform=`perspective(700px) rotateX(${(y/r.height-.5)*-6}deg) rotateY(${(x/r.width-.5)*6}deg) translateY(-4px)`});
    el.addEventListener('mouseleave',()=>el.style.transform='');el.addEventListener('click',e=>{if(!REAL||t.soon){e.preventDefault();location.hash='t-'+t.id}});return el},
  paint(){const q=this.q.trim().toLowerCase();const g=$('#toolGrid');g.innerHTML='';let list=this.list;
    const pop=this.list.filter(t=>t.pop).sort((a,b)=>a.pop-b.pop);
    $('#popWrap').style.display=(!q&&this.cat==='popular')?'':'none';
    if(!q&&this.cat==='popular'){$('#popGrid').innerHTML='';pop.forEach(t=>$('#popGrid').append(this.card(t)));$('#allH').textContent='All tools';}
    if(q){const words=q.split(/\s+/);list=list.filter(t=>{const s=(t.name+' '+t.desc+' '+(t.kw||'')+' '+t.cat).toLowerCase();return words.every(w=>s.includes(w))});$('#allH').textContent=list.length+' result'+(list.length===1?'':'s')}
    else if(this.cat!=='popular'&&this.cat!=='all'){list=list.filter(t=>t.cat===this.cat);$('#allH').textContent=CATN[this.cat]+' ('+list.length+')'}
    else if(this.cat==='all')$('#allH').textContent='All tools ('+list.length+')';
    const show=(!q&&this.cat==='popular')?list.filter(t=>!t.pop):list;
    const limit=(!q&&this.cat==='popular'&&!this.more)?12:9999;
    show.slice(0,limit).forEach(t=>g.append(this.card(t)));
    if(show.length>limit){const m=U.btn(`Show all ${this.list.length} tools ↓`,()=>{this.more=true;this.paint()},'btn btn-g morebtn');g.after(m);this._m=m}else if(this._m){this._m.remove();this._m=null}
    if(this._m&&show.length<=limit){this._m.remove();this._m=null}
    $('#tCount').textContent=this.list.length+' tools'},
  open(id){const t=this.list.find(x=>x.id===id);if(!t)return this.close();window.CUR_TOOL=t;
    const keep=window.TOOL_LANG&&window.TOOL_PAGE===t.id;if(!keep){$('#tCrumb').textContent=CATN[t.cat];$('#tpTitle').textContent=t.name;$('#tpDesc').textContent=t.long||t.desc;}
    if(!keep)document.title=t.name+' — Free Online | DoraPDF';const md=document.querySelector('meta[name=description]');if(md&&!keep)md.content=`Free online ${t.name}. ${t.desc}. No sign-up, works in your browser.`;
    const box=$('#tpBox');box.innerHTML='';$('#tpNote').textContent=t.note||(t.file?'🔒 Your files are processed on your device and never uploaded.':'');
    if(t.soon){box.append(h('div',{class:'soonbox'},h('div',{class:'em'},'🚀'),h('h3',{style:'font-size:20px;margin:10px 0 6px'},t.name+' is coming soon'),h('p',{style:'color:var(--mute)'},t.soonWhy||'This tool goes live when the site launches. Meanwhile, try the related tools below!')))}
    else{try{t.run(box)}catch(e){console.error(e);box.append(h('p',{},'⚠️ '+friendlyErr(e)))}}
    try{revRender(t)}catch(e){}
    const rel=$('#tpRel');rel.innerHTML='';this.list.filter(x=>x.cat===t.cat&&x.id!==t.id&&!x.soon).sort(()=>Math.random()-.5).slice(0,4).forEach(x=>rel.append(this.card(x)));
    $('#tpage').classList.add('on');$('#tpage').scrollTop=0;if(!window.TOOL_PAGE)document.body.style.overflow='hidden'},
  close(){$('#tpage').classList.remove('on');document.body.style.overflow='';document.title='DoraPDF — Free File Tools & Assignment Helper'},
  route(){const m=location.hash.match(/^#t-([a-z0-9-]+)$/);if(m)this.open(m[1]);else if(window.TOOL_PAGE)this.open(window.TOOL_PAGE);else this.close()},
  boot(){const c=$('#chips');CATS.forEach(([k,l])=>c.append(h('button',{class:'chip'+(k===this.cat?' on':''),'data-sfx':'',onclick:e=>{this.cat=k;this.more=k!=='popular';$$('.chip').forEach(x=>x.classList.remove('on'));e.currentTarget.classList.add('on');this.paint()}},l)));
    $('#tSearch').addEventListener('input',e=>{this.q=e.target.value;this.paint()});
    $('#tBack').onclick=()=>{if(window.TOOL_PAGE&&REAL)location.href='/#tools';else location.hash='tools'};addEventListener('hashchange',()=>this.route());
    this.paint();this.route();
    $('#mq').innerHTML=[...this.list.filter(t=>t.pop),...this.list.filter(t=>t.pop)].map(t=>`<span>${esc(t.name)}</span>`).join('');observe()}
};
const tool=t=>TV.add(t);

/* image helpers */
function loadImg(file){return new Promise((ok,no)=>{const u=URL.createObjectURL(file),im=new Image();im.onload=()=>ok(im);im.onerror=()=>no(new Error('not an image: '+file.name));im.src=u})}
function canvasBlob(c,type,q){return new Promise(ok=>c.toBlob(ok,type,q))}
function drawTo(im,maxW=0,bg){let w=im.naturalWidth||im.width,h=im.naturalHeight||im.height;if(maxW&&w>maxW){h=Math.round(h*maxW/w);w=maxW}const c=document.createElement('canvas');c.width=w;c.height=h;const x=c.getContext('2d');if(bg){x.fillStyle=bg;x.fillRect(0,0,w,h)}x.drawImage(im,0,0,w,h);return c}

/* pdf text extraction -> rows */
async function pdfRows(file,onp){
  const lib=await loadPdf();const doc=await lib.getDocument({data:await readAB(file)}).promise;const pages=[];
  for(let p=1;p<=doc.numPages;p++){
    const pg=await doc.getPage(p);const tc=await pg.getTextContent();const rows=[];
    tc.items.filter(i=>i.str&&i.str.trim()).forEach(it=>{const y=it.transform[5],x=it.transform[4],h=Math.abs(it.transform[3])||10;let r=rows.find(r=>Math.abs(r.y-y)<h*.5);if(!r){r={y,h,items:[]};rows.push(r)}r.items.push({x,w:it.width,s:it.str,h})});
    rows.sort((a,b)=>b.y-a.y);rows.forEach(r=>r.items.sort((a,b)=>a.x-b.x));pages.push(rows);onp&&onp(p/doc.numPages);
  }
  return pages;
}
function rowText(r){let out='',prevEnd=null;r.items.forEach(i=>{if(prevEnd!==null){const gap=i.x-prevEnd;out+=gap>i.h*.25?' ':''}out+=i.s;prevEnd=i.x+i.w});return out.replace(/\s+/g,' ').trim()}
function rowCells(r){const cells=[];let curCell=null,prevEnd=null;r.items.forEach(i=>{if(curCell===null||i.x-prevEnd>i.h*1.6){curCell={s:i.s};cells.push(curCell)}else{curCell.s+=(i.x-prevEnd>i.h*.25?' ':'')+i.s}prevEnd=i.x+i.w});return cells.map(c=>{const t=c.s.trim();const n=t.replace(/,/g,'');return /^-?\d+(\.\d+)?$/.test(n)?Number(n):t})}

/* minimal docx writer */
const xe=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
function para(text,o={}){const rpr=`<w:rPr><w:rFonts w:ascii="${o.font||'Calibri'}" w:hAnsi="${o.font||'Calibri'}"/>${o.b?'<w:b/>':''}${o.i?'<w:i/>':''}${o.color?`<w:color w:val="${o.color}"/>`:''}<w:sz w:val="${(o.size||11)*2}"/></w:rPr>`;const ppr=`<w:pPr>${o.center?'<w:jc w:val="center"/>':o.justify?'<w:jc w:val="both"/>':''}<w:spacing w:after="${o.after??120}" w:line="${o.line||276}" w:lineRule="auto"/>${o.indent?'<w:ind w:left="360" w:hanging="360"/>':''}</w:pPr>`;return `<w:p>${ppr}<w:r>${rpr}<w:t xml:space="preserve">${xe(text)}</w:t></w:r></w:p>`}
const pageBreak='<w:p><w:r><w:br w:type="page"/></w:r></w:p>';
async function makeDocx(bodyXml,images=[],sect,opt={}){
  await loadScript(CDN.jszip);const z=new JSZip();
  z.file('[Content_Types].xml',`<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Default Extension="png" ContentType="image/png"/><Default Extension="jpeg" ContentType="image/jpeg"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>${opt.header?'<Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>':''}</Types>`);
  z.file('_rels/.rels',`<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>`);
  z.file('word/_rels/document.xml.rels',`<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">${images.map((im,i)=>`<Relationship Id="img${i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/img${i}.${im.ext}"/>`).join('')}${opt.header?'<Relationship Id="hdr1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>':''}</Relationships>`);
  if(opt.header){z.file('word/header1.xml',`<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">${opt.header.xml}</w:hdr>`);z.file('word/_rels/header1.xml.rels',`<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="bg1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/bg1.${opt.header.ext}"/></Relationships>`);z.file('word/media/bg1.'+opt.header.ext,opt.header.data)}
  images.forEach((im,i)=>z.file(`word/media/img${i}.${im.ext}`,im.data));
  z.file('word/document.xml',`<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><w:body>${bodyXml}${sect||('<w:sectPr>'+(opt.header?'<w:headerReference w:type="default" r:id="hdr1"/>':'')+'<w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/></w:sectPr>')}</w:body></w:document>`);
  return z.generateAsync({type:'blob',mimeType:'application/vnd.openxmlformats-officedocument.wordprocessingml.document'});
}



/* DoraPDF API (Cloudflare worker on api.dorapdf.com) */
const API='https://dorapdf-api.asadch3602.workers.dev';


/* ---------- rate-after-download popup ---------- */
function revAsk(){const t=window.CUR_TOOL;if(!t||document.querySelector('.revm'))return;
  let st={};try{st=JSON.parse(localStorage.getItem('dora_rev')||'{}')}catch(e){}
  if(st[t.id]==='done'||(st[t.id]&&Date.now()-st[t.id]<3*864e5))return;
  const save=v=>{st[t.id]=v;try{localStorage.setItem('dora_rev',JSON.stringify(st))}catch(e){}};
  let pick=0;const sb=h('div',{class:'stars',role:'radiogroup','aria-label':'Your rating'});const paint=v=>[...sb.children].forEach((b,i)=>b.classList.toggle('on',i<v));
  const ta=h('textarea',{maxlength:'400',placeholder:'Tell others how it went (optional)',style:'display:none'});const send=h('button',{class:'send',type:'button',style:'display:none;width:100%'},'Submit rating');
  for(let i=1;i<=5;i++){const b=h('button',{type:'button',role:'radio','aria-label':i+' star'+(i>1?'s':'')},'★');b.onmouseenter=()=>paint(i);b.onmouseleave=()=>paint(pick);b.onclick=()=>{pick=i;paint(i);ta.style.display='block';send.style.display='block';try{sfx&&sfx('tap')}catch(e){}};sb.append(b)}
  const close=()=>{m.remove();document.removeEventListener('keydown',esc)};const esc=e=>{if(e.key==='Escape'){save(Date.now());close()}};
  const box=h('div',{class:'box',role:'dialog','aria-modal':'true','aria-label':'Rate this tool'},
    h('button',{class:'x',type:'button','aria-label':'Close'},'✕'),
    h('div',{class:'lbl',style:'font:500 11px/1 ui-monospace,monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--pink2)'},'Your file is downloading'),
    h('h3',{},'How was '+t.name+'?'),h('p',{},'One tap helps other people find tools that work.'),sb,ta,send,
    h('button',{class:'later',type:'button'},'Maybe later'));
  const m=h('div',{class:'revm rev'},box);
  box.querySelector('.x').onclick=()=>{save(Date.now());close()};box.querySelector('.later').onclick=()=>{save(Date.now());close()};
  m.onclick=e=>{if(e.target===m){save(Date.now());close()}};document.addEventListener('keydown',esc);
  send.onclick=async()=>{send.disabled=true;send.textContent='Sending…';
    try{const r=await fetch(API+'/reviews',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({tool:t.id,stars:pick,text:ta.value.trim(),name:''})});const j=await r.json().catch(()=>({}));if(!r.ok&&r.status!==429)throw new Error(j.error||'Could not send');
      save('done');box.replaceChildren(h('div',{style:'font-size:46px;color:#ff2e88'},'✦'),h('h3',{},'Thank you!'),h('p',{},ta.value.trim()?'Your rating is counted. Your review shows after a quick check.':'Your rating is counted.'));setTimeout(close,1800);try{revRender(t)}catch(e){}}
    catch(e){toast('⚠️ '+friendlyErr(e));send.disabled=false;send.textContent='Submit rating'}};
  document.body.append(m);setTimeout(()=>sb.firstChild&&sb.firstChild.focus(),50)}
/* ---------- tool reviews (real users only) ---------- */
async function revRender(t){const box=$('#tpRev');if(!box)return;box.innerHTML='';let data={avg:0,n:0,items:[]};
  try{const r=await fetch(API+'/reviews?tool='+encodeURIComponent(t.id));if(r.ok)data=await r.json()}catch(e){}
  if($('#tpRev')!==box||(window.TV&&TV.cur&&TV.cur.id&&TV.cur.id!==t.id))return;
  const starTxt=v=>'★★★★★'.slice(0,Math.round(v))+'☆☆☆☆☆'.slice(0,5-Math.round(v));
  const left=h('div',{},h('div',{class:'lbl'},'Rated by users'),
    data.n?h('div',{},h('div',{class:'big'},data.avg.toFixed(1)),h('div',{class:'sm'},starTxt(data.avg)),h('p',{style:'margin:8px 0 0;color:var(--mute);font-size:14px'},`${data.n} rating${data.n>1?'s':''} for ${t.name}`))
      :h('div',{},h('div',{class:'big'},'—'),h('p',{style:'margin:8px 0 0;color:var(--mute);font-size:14px'},'No ratings yet. Be the first to rate this tool.')),
    ...(data.items||[]).slice(0,3).map(it=>h('div',{class:'item'},h('div',{},h('b',{},it.name||'DoraPDF user'),' ',h('span',{class:'sm',style:'font-size:12px'},starTxt(it.s))),h('div',{style:'margin-top:4px'},it.t),h('span',{},it.d||''))));
  let pick=0;const sb=h('div',{class:'stars',role:'radiogroup','aria-label':'Your rating'});
  const paint=v=>[...sb.children].forEach((b,i)=>b.classList.toggle('on',i<v));
  for(let i=1;i<=5;i++){const b=h('button',{type:'button',role:'radio','aria-label':i+' star'+(i>1?'s':'')},'★');b.onmouseenter=()=>paint(i);b.onmouseleave=()=>paint(pick);b.onclick=()=>{pick=i;paint(i);try{sfx&&sfx('tap')}catch(e){}};sb.append(b)}
  const ta=h('textarea',{maxlength:'400',placeholder:'What did you use it for? Did it work well? (optional)'}),nm=h('input',{maxlength:'40',placeholder:'Your name (optional)'});
  const send=h('button',{class:'send',type:'button'},'Submit rating');
  const right=h('div',{},h('div',{class:'lbl'},'Rate this tool'),h('div',{style:'margin-top:12px'},sb),ta,nm,send,h('p',{style:'margin:10px 0 0;color:var(--mute);font-size:12px'},'Only real ratings. Written reviews appear after a quick check.'));
  send.onclick=async()=>{if(!pick){toast('Tap the stars to rate first');return}send.disabled=true;send.textContent='Sending…';
    try{const r=await fetch(API+'/reviews',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({tool:t.id,stars:pick,text:ta.value.trim(),name:nm.value.trim()})});const j=await r.json().catch(()=>({}));
      if(!r.ok)throw new Error(j.error||'Could not send');try{const st=JSON.parse(localStorage.getItem('dora_rev')||'{}');st[t.id]='done';localStorage.setItem('dora_rev',JSON.stringify(st))}catch(e){}right.replaceChildren(h('div',{class:'lbl'},'Thank you'),h('div',{class:'big',style:'font-size:44px'},'✦'),h('p',{style:'color:var(--mute)'},ta.value.trim()?'Your rating is counted. Your review will show after a quick check.':'Your rating is counted.'))}
    catch(e){toast('⚠️ '+friendlyErr(e));send.disabled=false;send.textContent='Submit rating'}};
  box.append(h('section',{class:'rev','aria-label':'Ratings and reviews'},left,right))}
async function apiFetch(path,opt={}){let r;try{r=await fetch(API+path,opt)}catch(e){throw new Error('This tool is being connected to our server. Please try again soon.')}
  if(!r.ok){let m='Something went wrong ('+r.status+')';try{m=(await r.json()).error||m}catch(e){}throw new Error(m)}return r}
function urlInput(ph){return h('input',{class:'uin',type:'url',inputmode:'url',placeholder:ph||'https://example.com',style:'width:100%'})}
/* OCR (tesseract.js, runs in its own worker) */
const OCR_LANGS=[['eng','English'],['urd','Urdu'],['ara','Arabic'],['hin','Hindi'],['spa','Spanish'],['fra','French'],['deu','German'],['por','Portuguese'],['ita','Italian'],['tur','Turkish'],['ind','Indonesian'],['rus','Russian'],['chi_sim','Chinese (Simplified)']];
function ocrLangSel(){return U.sel(OCR_LANGS,{value:'eng'})}
let ocrW=null,ocrWLang=null,ocrProg=null;
async function ocrRun(img,lang,onp){await loadScript('https://cdn.jsdelivr.net/npm/tesseract.js@5.1.1/dist/tesseract.min.js');ocrProg=onp;
  if(!ocrW||ocrWLang!==lang){if(ocrW){try{await ocrW.terminate()}catch(e){}}ocrW=await Tesseract.createWorker(lang,1,{logger:m=>{if(m.status==='recognizing text'&&ocrProg)ocrProg(m.progress)}});ocrWLang=lang}
  const {data}=await ocrW.recognize(img);return data}
/* PDF -> DOCX keeping the original layout: page background (text removed) + editable positioned text */
const PUA={'':'•','':'▪','':'➢','':'❖','':'✓','':'➔','':'•','':'●','':'■','':'➢','':'➤'};
function pdfFontInfo(name){name=String(name||'').replace(/^[A-Z]{6}\+/,'');const bold=/bold|black|heavy|semibold|demi/i.test(name),ital=/italic|oblique/i.test(name);
  let b=name.split(/[-,]/)[0].replace(/(PSMT|PS|MT)$/,'').replace(/(Bold|Italic|Regular|Oblique)+$/,'');
  const map={TimesNewRoman:'Times New Roman',Times:'Times New Roman',Arial:'Arial',Helvetica:'Arial',ArialNarrow:'Arial Narrow',Calibri:'Calibri',CalibriLight:'Calibri Light',Cambria:'Cambria',CenturyGothic:'Century Gothic',Georgia:'Georgia',Verdana:'Verdana',Tahoma:'Tahoma',Garamond:'Garamond',BookAntiqua:'Book Antiqua',Courier:'Courier New',CourierNew:'Courier New',Symbol:'Symbol',SegoeUI:'Segoe UI',TrebuchetMS:'Trebuchet MS',Trebuchet:'Trebuchet MS',Aptos:'Aptos',Roboto:'Roboto',OpenSans:'Open Sans',Montserrat:'Montserrat',Poppins:'Poppins',Lato:'Lato'};
  let fam=map[b]||b.replace(/([a-z])([A-Z])/g,'$1 $2').trim();if(!fam||/^(sans-serif|serif|monospace|g_d\d+)/i.test(fam)||/^f\d+$/i.test(fam))fam='Calibri';return{fam,bold,ital}}
async function pdfLayoutDocx(file,prog){
  const doc=await pdfDoc(file);const SC=2;const images=[];let body='';let any=false;const n=doc.numPages;
  const pt2tw=v=>Math.round(v*20),pt2emu=v=>Math.round(v*12700);
  for(let p=1;p<=n;p++){
    const pg=await doc.getPage(p);const v1=pg.getViewport({scale:1}),vp=pg.getViewport({scale:SC});
    const c=canvasOf(Math.ceil(vp.width),Math.ceil(vp.height));const x=c.getContext('2d',{willReadFrequently:true});x.fillStyle='#fff';x.fillRect(0,0,c.width,c.height);
    await pg.render({canvasContext:x,viewport:vp,intent:'print'}).promise;
    const tc=await pg.getTextContent();const W=c.width,H=c.height;const px=x.getImageData(0,0,W,H).data;
    const at=(X,Y)=>{X=Math.max(0,Math.min(W-1,X|0));Y=Math.max(0,Math.min(H-1,Y|0));const i=(Y*W+X)*4;return[px[i],px[i+1],px[i+2]]};
    const items=[];
    for(const it of tc.items){if(!it.str||!it.str.trim())continue;const t=pdfjsLib.Util.transform(v1.transform,it.transform);const fh=Math.hypot(t[2],t[3]);if(fh<2)continue;
      if(Math.abs(t[1])>fh*.02||Math.abs(t[2])>fh*.02)continue; /* rotated text stays in the picture */
      const st=tc.styles[it.fontName]||{};const asc=st.ascent||.85,des=st.descent||-.22;const w=Math.max(it.width,fh*.3);
      const L=t[4],B=t[5],T=B-fh*asc,Bo=B-fh*des;let fo=null;try{fo=pg.commonObjs.get(it.fontName)}catch(e){}
      const fi=pdfFontInfo((fo&&fo.name)||st.fontFamily);
      /* colours: background = median of the box border, ink = pixel farthest from it */
      const x0=(L*SC)-2,y0=(T*SC)-2,x1=(L+w)*SC+2,y1=Bo*SC+2;const bord=[];for(let k=0;k<=12;k++){const fx=x0+(x1-x0)*k/12,fy=y0+(y1-y0)*k/12;bord.push(at(fx,y0),at(fx,y1),at(x0,fy),at(x1,fy))}
      const med=i=>bord.map(q=>q[i]).sort((a,b)=>a-b)[bord.length>>1];const bg=[med(0),med(1),med(2)];
      let ink=[0,0,0],best=-1;for(let yy=Math.max(0,y0+2|0);yy<Math.min(H,y1-2);yy+=1)for(let xx=Math.max(0,x0+2|0);xx<Math.min(W,x1-2);xx+=2){const q=at(xx,yy);const d=Math.abs(q[0]-bg[0])+Math.abs(q[1]-bg[1])+Math.abs(q[2]-bg[2]);if(d>best){best=d;ink=q}}
      const hex=a=>a.map(v=>v.toString(16).padStart(2,'0')).join('');
      let str=it.str.replace(/[-]/g,ch=>PUA[ch]||'•');
      items.push({s:str,L,R:L+w,T,Bo,B,fh,fi,col:best<60?'000000':hex(ink),bg,box:[x0,y0,x1,y1]});any=true}
    /* remove the original text from the picture */
    items.forEach(i=>{x.fillStyle=`rgb(${i.bg[0]},${i.bg[1]},${i.bg[2]})`;x.fillRect(i.box[0],i.box[1],i.box[2]-i.box[0],i.box[3]-i.box[1])});
    /* group into lines */
    items.sort((a,b)=>Math.abs(a.B-b.B)<Math.min(a.fh,b.fh)*.35?a.L-b.L:a.B-b.B);
    const lines=[];items.forEach(i=>{const l=lines[lines.length-1];if(l&&Math.abs(l.B-i.B)<Math.min(l.fh,i.fh)*.35&&i.L-l.R<Math.max(l.fh,i.fh)*1.1&&i.L>l.R-i.fh*.6){l.items.push(i);l.R=Math.max(l.R,i.R);l.T=Math.min(l.T,i.T);l.Bo=Math.max(l.Bo,i.Bo);l.fh=Math.max(l.fh,i.fh)}else lines.push({items:[i],L:i.L,R:i.R,T:i.T,Bo:i.Bo,B:i.B,fh:i.fh})});
    /* page picture behind the text */
    const blob=await canvasBlob(c,'image/jpeg',.88);const ix=images.length;images.push({ext:'jpeg',data:blob});
    const cx=pt2emu(v1.width),cy=pt2emu(v1.height),did=ix+1;
    body+=`<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="20" w:lineRule="exact"/></w:pPr><w:r><w:drawing><wp:anchor distT="0" distB="0" distL="0" distR="0" simplePos="0" relativeHeight="0" behindDoc="1" locked="1" layoutInCell="1" allowOverlap="1"><wp:simplePos x="0" y="0"/><wp:positionH relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionH><wp:positionV relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionV><wp:extent cx="${cx}" cy="${cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:wrapNone/><wp:docPr id="${did}" name="Page ${p}"/><wp:cNvGraphicFramePr/><a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic><pic:nvPicPr><pic:cNvPr id="${did}" name="page${p}"/><pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip r:embed="img${ix}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="${cx}" cy="${cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:anchor></w:drawing></w:r></w:p>`;
    lines.forEach(l=>{let runs='',prevR=null;l.items.forEach(i=>{let s=i.s;if(prevR!==null&&i.L-prevR>i.fh*.18&&!/^\s/.test(s)&&!/\s$/.test(runs.slice(-40)))s=' '+s;prevR=i.R;
        const f=i.fi.fam;runs+=`<w:r><w:rPr><w:rFonts w:ascii="${xe(f)}" w:hAnsi="${xe(f)}" w:cs="${xe(f)}"/>${i.fi.bold?'<w:b/>':''}${i.fi.ital?'<w:i/>':''}${i.col!=='000000'?`<w:color w:val="${i.col}"/>`:''}<w:sz w:val="${Math.max(2,Math.round(i.fh*2))}"/></w:rPr><w:t xml:space="preserve">${xe(s)}</w:t></w:r>`});
      const wTw=pt2tw((l.R-l.L)*1.15+l.fh*.6),hTw=pt2tw(l.Bo-l.T);
      body+=`<w:p><w:pPr><w:framePr w:w="${wTw}" w:h="${hTw}" w:hRule="atLeast" w:wrap="around" w:vAnchor="page" w:hAnchor="page" w:x="${pt2tw(l.L)}" w:y="${pt2tw(l.T)}"/><w:spacing w:before="0" w:after="0" w:line="${pt2tw(l.Bo-l.T)}" w:lineRule="exact"/><w:ind w:left="0" w:right="0"/></w:pPr>${runs}</w:p>`});
    const sect=`<w:sectPr><w:pgSz w:w="${pt2tw(v1.width)}" w:h="${pt2tw(v1.height)}"/><w:pgMar w:top="0" w:right="0" w:bottom="0" w:left="0" w:header="0" w:footer="0" w:gutter="0"/></w:sectPr>`;
    if(p<n)body+=`<w:p><w:pPr><w:spacing w:after="0" w:line="20" w:lineRule="exact"/>${sect}</w:pPr></w:p>`;else body+=`\u0000${sect}`;
    prog&&prog(p/n*.9)}
  if(!any)throw new Error('No text found — this PDF looks scanned (image only).');
  const [b,sect]=body.split('\u0000');return makeDocx(b,images,sect)}

function imgPara(i,wPx,hPx){const maxW=5486400*.75;let cx=wPx*9525,cy=hPx*9525;if(cx>maxW){cy=Math.round(cy*maxW/cx);cx=maxW}return `<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:drawing><wp:inline><wp:extent cx="${cx}" cy="${cy}"/><wp:docPr id="${i+1}" name="Figure ${i+1}"/><a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic><pic:nvPicPr><pic:cNvPr id="${i+1}" name="img${i}"/><pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip r:embed="img${i}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="${cx}" cy="${cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>`}


/* ---------- AI assignment ---------- */
const TRIAL_DAYS=3;const LAUNCHING=false;
function trialState(){let s=null;try{s=localStorage.getItem('tv_trial')}catch(e){}if(!s)return{started:false,left:TRIAL_DAYS};const left=TRIAL_DAYS-(Date.now()-+s)/864e5;return{started:true,left}}
function paintTrial(){const t=trialState();$('#trialTxt').innerHTML=t.started?(t.left>0?`Trial: <b>${Math.ceil(t.left)} day${Math.ceil(t.left)>1?'s':''} left</b>`:'Trial <b>ended</b>'):`Free trial: <b>${TRIAL_DAYS} days</b>`;$('#pay').classList.toggle('on',t.started&&t.left<=0)}

let refFile=null, refDataUrl=null, lastDoc=null;
$('#gImg').onchange=e=>{refFile=e.target.files[0]||null;if(refFile){const u=URL.createObjectURL(refFile);refDataUrl=u;$('#refTxt').innerHTML=`<span style="display:flex;align-items:center;gap:10px"><img src="${u}"> ${esc(refFile.name)}</span>`}};
function renderDoc(d){
  const name=$('#gName').value.trim(),course=$('#gCourse').value.trim();
  let h=`<h1>${esc(d.title)}</h1><div class="sub">${esc(d.subtitle||'')}${name||course?'<br>'+esc([name,course].filter(Boolean).join(' · ')):''}</div>`;
  let figDone=false,fig=0;const cap=s=>esc(String(s.heading||'').replace(/^\d+\.?\s*/,''));
  d.sections.forEach(s=>{h+=`<h2>${esc(s.heading)}</h2>`;(s.paragraphs||[]).forEach((p,i)=>{h+=`<p>${esc(p)}</p>`;
    if(i===0&&s.figure&&refDataUrl&&!figDone){figDone=true;fig++;h+=`<div class="figure"><img src="${refDataUrl}"><i>Figure ${fig}. ${cap(s)}</i></div>`}
    if(i===0&&s.img){fig++;h+=`<div class="figure"><img src="${esc(s.img.src)}" loading="lazy" onerror="this.parentNode.remove()"><i>Figure ${fig}. ${cap(s)}</i><small style="display:block;font-size:10.5px;color:#8a7a92">Image: ${esc(s.img.credit||'')}</small></div>`}});
    if(s.bullets&&s.bullets.length)h+='<ul>'+s.bullets.map(b=>`<li>${esc(b)}</li>`).join('')+'</ul>'});
  if(refDataUrl&&!figDone){fig++;h+=`<div class="figure"><img src="${refDataUrl}"><i>Figure ${fig}. Reference image</i></div>`}
  if(d.references&&d.references.length)h+=`<h2>References</h2><ol class="refs">${d.references.map(r=>`<li>${esc(r)}</li>`).join('')}</ol><p style="font-size:11.5px;color:#8a7a92;margin-top:16px">Tip: double-check each reference before submitting.</p>`;
  $('#paper').innerHTML=h;$('#paper').style.display='block';$('#outEmpty').style.display='none';
  $('#copyBtn').disabled=false;$('#docxBtn').disabled=false;$('#outTag').textContent=$('#gCite').value+' · '+$('#gLevel').value;
}

/* assignment theme helpers */
let lastFile=null;
function themeColor(){const t=$('#gTheme');if(!t)return '9C0F55';return (t.value==='custom'?$('#gColor').value.replace('#',''):t.value).toUpperCase()}
async function bgCanvas(w,h){const mode=$('#gBg')?$('#gBg').value:'none';if(mode==='none')return null;const c=canvasOf(w,h),x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,w,h);
  if(mode==='image'&&$('#gBgImg').files[0]){const im=await loadImg($('#gBgImg').files[0]);const r=Math.max(w/im.naturalWidth,h/im.naturalHeight);const iw=im.naturalWidth*r,ih=im.naturalHeight*r;x.globalAlpha=.16;x.drawImage(im,(w-iw)/2,(h-ih)/2,iw,ih);x.globalAlpha=1}
  else{const col='#'+themeColor();const g=x.createLinearGradient(0,0,w,h);g.addColorStop(0,col+'14');g.addColorStop(1,col+'05');x.fillStyle=g;x.fillRect(0,0,w,h);x.fillStyle=col+'2a';x.fillRect(0,0,w,Math.round(h*.012))}
  return c}
async function docBackground(){const c=await bgCanvas(1240,1754);if(!c)return null;const b=await canvasBlob(c,'image/jpeg',.85);const cx=7560310,cy=10692130;
  return {ext:'jpeg',data:await b.arrayBuffer(),xml:`<w:p><w:r><w:drawing><wp:anchor distT="0" distB="0" distL="0" distR="0" simplePos="0" relativeHeight="0" behindDoc="1" locked="1" layoutInCell="1" allowOverlap="1"><wp:simplePos x="0" y="0"/><wp:positionH relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionH><wp:positionV relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionV><wp:extent cx="${cx}" cy="${cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:wrapNone/><wp:docPr id="900" name="Background"/><wp:cNvGraphicFramePr/><a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic><pic:nvPicPr><pic:cNvPr id="900" name="bg"/><pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip r:embed="bg1"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="${cx}" cy="${cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:anchor></w:drawing></w:r></w:p>`}}
$('#gTheme')&&$('#gTheme').addEventListener('change',e=>{$('#gColor').style.display=e.target.value==='custom'?'block':'none'});
$('#gBg')&&$('#gBg').addEventListener('change',e=>{$('#bgImgWrap').style.display=e.target.value==='image'?'block':'none'});
$('#gBgImg')&&($('#gBgImg').onchange=e=>{const f=e.target.files[0];if(f)$('#bgImgTxt').textContent='✓ '+f.name});
async function imgForDoc(src,max){try{const b=await (await fetch(src)).blob();const im=await loadImg(new File([b],'i'));const c=drawTo(im,max||1400,'#fff');return {c,blob:await canvasBlob(c,'image/jpeg',.9)}}catch(e){return null}}
function docText(d){let t=d.title+'\n'+(d.subtitle||'')+'\n\n';d.sections.forEach(s=>{t+=s.heading+'\n\n'+(s.paragraphs||[]).join('\n\n')+'\n';if(s.bullets&&s.bullets.length)t+=s.bullets.map(b=>'• '+b).join('\n')+'\n';t+='\n'});if(d.references&&d.references.length)t+='References\n'+d.references.map((r,i)=>`${i+1}. ${r}`).join('\n');return t}
$('#copyBtn').onclick=async()=>{if(!lastDoc)return;try{await navigator.clipboard.writeText(docText(lastDoc));toast('Copied to clipboard ✓')}catch(e){toast('Copy blocked — select the text instead')}};
$('#docxBtn').onclick=async()=>{
  if(!lastDoc)return;const d=lastDoc;const name=$('#gName').value.trim(),course=$('#gCourse').value.trim();const btn=$('#docxBtn');btn.disabled=true;
  try{
  const T=themeColor();const F={font:'Times New Roman'};let body=para(d.title,{...F,size:20,b:true,center:true,color:T,after:80})+para(d.subtitle||'',{...F,size:12,i:true,center:true,color:'555555',after:name||course?60:360});
  if(name||course)body+=para([name,course].filter(Boolean).join(' · '),{...F,size:12,center:true,after:360});
  const images=[];const addImg=async(src,file)=>{let r=null;if(file){const im=await loadImg(file);const c=drawTo(im,1400,'#fff');r={c,blob:await canvasBlob(c,'image/jpeg',.9)}}else r=await imgForDoc(src);if(!r)return '';const i=images.length;images.push({ext:'jpeg',data:await r.blob.arrayBuffer()});return imgPara(i,r.c.width,r.c.height)};
  let refXml='';if(refFile)refXml=await addImg(null,refFile);
  let figDone=false,fig=0;const cap=s=>s.heading.replace(/^\d+\.?\s*/,'');
  for(const s of d.sections){body+=para(s.heading,{...F,size:14,b:true,color:T,after:120});const ps=s.paragraphs||[];
    for(let i=0;i<ps.length;i++){body+=para(ps[i],{...F,size:12,justify:true,line:360,after:160});
      if(i===0&&s.figure&&refXml&&!figDone){figDone=true;fig++;body+=refXml+para(`Figure ${fig}. `+cap(s),{...F,size:10,i:true,center:true})}
      if(i===0&&s.img){const x=await addImg(s.img.src);if(x){fig++;body+=x+para(`Figure ${fig}. `+cap(s),{...F,size:10,i:true,center:true,after:20})+para('Image: '+(s.img.credit||''),{...F,size:8,center:true,color:'777777',after:160})}}}
    (s.bullets||[]).forEach(b=>body+=para('•  '+b,{...F,size:12,indent:true,after:60}))}
  if(refXml&&!figDone){fig++;body+=refXml+para(`Figure ${fig}. Reference image`,{...F,size:10,i:true,center:true})}
  if(d.references&&d.references.length){body+=para('References',{...F,size:14,b:true,color:T});d.references.forEach(r=>body+=para(r,{...F,size:12,indent:true,after:100}))}
  const bg=await docBackground();const blob=await makeDocx(body,images,null,bg?{header:bg}:{});lastFile={blob,name:(d.title||'assignment').replace(/[^\w\- ]+/g,'').slice(0,60).trim()+'.docx'};
  saveFile((d.title||'assignment').replace(/[^\w\- ]+/g,'').slice(0,60).trim()+'.docx',blob);
  }catch(e){console.error(e);toast('⚠️ Could not build the Word file')}btn.disabled=false;
};
