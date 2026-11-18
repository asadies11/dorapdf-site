/* DoraPDF: drop-on-Dora, smart tool panel, keep-going chips, Explore search */
(function(){
const ACC={"pdf-to-word":".pdf,application/pdf","pdf-merger":".pdf,application/pdf","pdf-compressor":".pdf,application/pdf","pdf-image-watermark":".pdf,application/pdf","pdf-text-watermark":".pdf,application/pdf","pdf-editor":".pdf,application/pdf","unlock-pdf":".pdf,application/pdf","protect-pdf":".pdf,application/pdf","images-to-pdf":"image/*,.heic,.heif","png-to-pdf":"image/png","heic-to-pdf":".heic,.heif,image/heic,image/heif","pdf-to-markdown":".pdf,application/pdf","pdf-to-txt":".pdf,application/pdf","highlight-pdf":".pdf,application/pdf","word-to-pdf":".docx","docx-to-pdf":".docx","sign-pdf":".pdf,application/pdf","markdown-to-pdf":".md,.markdown,.txt","pdf-image-extractor":".pdf,application/pdf","rotate-pdf":".pdf,application/pdf","delete-pdf-pages":".pdf,application/pdf","redact-pdf":".pdf,application/pdf","epub-to-pdf":".epub","email-to-pdf":".eml,message/rfc822","odf-to-pdf":".odt","pdf-to-excel":".pdf,application/pdf","pdf-to-powerpoint":".pdf,application/pdf","pdf-splitter":".pdf,application/pdf","pptx-to-pdf":".pptx","pdf-ocr":".pdf,application/pdf","scan-to-pdf":"image/*","pdf-to-jpg":".pdf,application/pdf","pdf-to-png":".pdf,application/pdf","illustrator-to-png":".ai,application/postscript,application/pdf","image-compressor":"image/*","gif-maker":"image/*","heic-to-jpg":".heic,.heif,image/heic,image/heif","heic-to-png":".heic,.heif,image/heic,image/heif","webp-to-jpg":"image/webp","jpg-to-png":"image/jpeg","avif-to-jpg":"image/avif,.avif","avif-to-png":"image/avif,.avif","jpeg-to-png":"image/jpeg","png-to-jpg":"image/png","png-to-webp":"image/png","webp-to-png":"image/webp","svg-to-png":"image/svg+xml,.svg","png-to-svg":"image/png","webp-to-svg":"image/webp","gps-photo-stamper":"image/*","image-color-picker":"image/*","image-flipper":"image/*","image-resizer":"image/*","linkedin-photo-frame":"image/*","image-background-remover":"image/*,.heic,.heif","image-to-text":"image/*,.heic,.heif","compress-gif":".gif,image/gif","odf-to-jpg":".odt,.odp,.ods,.odg,application/vnd.oasis.opendocument.text,application/vnd.oasis.opendocument.presentation,application/vnd.oasis.opendocument.graphics","odf-to-png":".odt,.odp,.ods,.odg,application/vnd.oasis.opendocument.text,application/vnd.oasis.opendocument.presentation,application/vnd.oasis.opendocument.graphics","image-upscaler":"image/*,.heic,.heif","watermark-eraser":"image/*,.heic,.heif","object-remover":"image/*,.heic,.heif","base64":"*","zip-extractor":".zip,application/zip","video-compressor":"video/*","ascii-art":"image/*"};
const BEST={pdf:'pdf-to-word',image:'images-to-pdf',png:'images-to-pdf',jpg:'images-to-pdf',webp:'webp-to-jpg',avif:'avif-to-jpg',svg:'svg-to-png',heic:'heic-to-jpg',docx:'word-to-pdf',pptx:'pptx-to-pdf',epub:'epub-to-pdf',eml:'email-to-pdf',odt:'odf-to-pdf',md:'markdown-to-pdf',zip:'zip-extractor',video:'video-compressor',ai:'illustrator-to-png'};
const KN={pdf:'PDF file',image:'Image',png:'PNG image',jpg:'JPG image',webp:'WebP image',avif:'AVIF image',svg:'SVG image',heic:'HEIC photo',docx:'Word document',pptx:'PowerPoint file',epub:'eBook',eml:'Email file',odt:'OpenDocument text',md:'Markdown file',zip:'ZIP archive',video:'Video',ai:'Illustrator file',other:'File'};
const MIME={pdf:'application/pdf',png:'image/png',jpg:'image/jpeg',jpeg:'image/jpeg',webp:'image/webp',gif:'image/gif',svg:'image/svg+xml',avif:'image/avif',docx:'application/vnd.openxmlformats-officedocument.wordprocessingml.document',pptx:'application/vnd.openxmlformats-officedocument.presentationml.presentation',xlsx:'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',zip:'application/zip',mp4:'video/mp4',webm:'video/webm',txt:'text/plain',md:'text/markdown'};
const ext=f=>(f.name.split('.').pop()||'').toLowerCase();
function kind(f){const e=ext(f),t=(f.type||'').toLowerCase();
  if(e==='pdf'||t==='application/pdf')return 'pdf';if(e==='heic'||e==='heif')return 'heic';if(e==='svg')return 'svg';if(e==='png')return 'png';if(e==='jpg'||e==='jpeg')return 'jpg';if(e==='webp')return 'webp';if(e==='avif')return 'avif';
  if(t.startsWith('image/'))return 'image';if(e==='docx')return 'docx';if(e==='pptx')return 'pptx';if(e==='epub')return 'epub';if(e==='eml')return 'eml';if(e==='odt')return 'odt';if(e==='md'||e==='markdown')return 'md';if(e==='zip')return 'zip';if(e==='ai')return 'ai';if(t.startsWith('video/'))return 'video';return 'other'}
function fits(id,f){const a=ACC[id];if(!a)return false;const n=f.name.toLowerCase(),t=(f.type||'').toLowerCase();
  return a.split(',').map(s=>s.trim().toLowerCase()).some(s=>s==='*'?false:s.startsWith('.')?n.endsWith(s):s.endsWith('/*')?t.startsWith(s.slice(0,-1)):t===s)}
const live=()=>TV.list.filter(t=>!t.soon);
const tool=id=>TV.list.find(t=>t.id===id);
const fitList=(f,skip)=>{const k=kind(f);const b=BEST[k];return live().filter(t=>t.id!==skip&&fits(t.id,f)).sort((x,y)=>(y.id===b)-(x.id===b)||(x.pop||99)-(y.pop||99))};
const sz=b=>b<1024?b+' B':b<1048576?(b/1024).toFixed(1)+' KB':(b/1048576).toFixed(1)+' MB';
const D=window.DORA={pending:null,last:null,kind,fits,
  use(id,files){D.pending=files;D.closeAll();if(location.hash==='#t-'+id)TV.open(id);else location.hash='t-'+id},
  closeAll(){document.querySelectorAll('.dp-wrap').forEach(e=>e.remove());document.body.classList.remove('dp-lock')},
  chip(t,files,extra){return h('button',{class:'dpchip'+(extra||''),'data-sfx':'',onclick:()=>D.use(t.id,files)},t.name)},
  exploreChip(files){return h('button',{class:'dpchip ex','data-sfx':'',onclick:()=>D.explore(files)},'🔎 Explore →')},
  panel(files){const f=files[0];D.last=f;const k=kind(f);const list=fitList(f);const bestId=BEST[k];const best=list.find(t=>t.id===bestId)||list[0];
    D.closeAll();const w=h('div',{class:'dp-wrap',onclick:e=>{if(e.target===w)D.closeAll()}});
    const p=h('div',{class:'dp',role:'dialog','aria-label':'Choose a tool'});
    p.append(h('div',{class:'dp-top'},h('div',{class:'dp-ic'},(ext(f)||'file').slice(0,4).toUpperCase()),h('div',{style:'min-width:0'},h('div',{class:'dp-nm'},files.length>1?files.length+' files · '+f.name+' …':f.name),h('div',{class:'dp-sub'},KN[k]+' · '+sz(f.size)+' · Dora is ready')),h('button',{class:'dp-x','aria-label':'Close',onclick:()=>D.closeAll()},'×')));
    if(best){p.append(h('div',{class:'dp-lbl'},'Best match'),h('button',{class:'dp-best','data-sfx':'',onclick:()=>D.use(best.id,files)},h('span',{},best.name),h('small',{},best.desc),h('b',{},'→')));
      const rest=list.filter(t=>t!==best).slice(0,14);p.append(h('div',{class:'dp-lbl'},'Or do something else with it'));const c=h('div',{class:'dp-chips'});rest.forEach(t=>c.append(D.chip(t,files)));c.append(D.exploreChip(files));p.append(c)}
    else{p.append(h('p',{class:'dp-sub',style:'margin:6px 0 14px'},'Dora does not have a direct tool for this file type yet. Search all tools:'));p.append(h('div',{class:'dp-chips'},D.exploreChip(files)))}
    p.append(h('div',{class:'dp-foot'},'🔒 Your file stays in your browser. Pick any tool, no re-upload.'));
    w.append(p);document.body.append(w);document.body.classList.add('dp-lock')},
  explore(files){const f=files&&files[0];D.closeAll();const w=h('div',{class:'dp-wrap',onclick:e=>{if(e.target===w)D.closeAll()}});
    const inp=h('input',{class:'dp-in',type:'search',placeholder:'Search 160+ tools, e.g. image to word','aria-label':'Search tools'});
    const res=h('div',{class:'dp-res'});let items=[],sel=0;
    const paint=()=>{const q=inp.value.trim().toLowerCase();const words=q.split(/\s+/).filter(Boolean);
      items=live().filter(t=>{const s=(t.name+' '+t.desc+' '+(t.kw||'')+' '+t.cat).toLowerCase();return words.every(x=>s.includes(x))});
      if(f)items.sort((a,b)=>fits(b.id,f)-fits(a.id,f));items=items.slice(0,30);sel=Math.min(sel,Math.max(0,items.length-1));res.innerHTML='';
      if(!items.length)res.append(h('div',{class:'dp-sub',style:'padding:14px;text-align:center'},'No tool found. Try another word.'));
      items.forEach((t,i)=>{const ok=f&&fits(t.id,f);res.append(h('button',{class:'dp-r'+(i===sel?' on':''),onclick:()=>go(t),onmouseenter:()=>{sel=i;[...res.children].forEach((c,j)=>c.classList.toggle('on',j===i))}},h('div',{},h('div',{class:'dp-rt'},t.name),h('div',{class:'dp-rd'},t.desc)),ok?h('span',{class:'dp-tag'},'Works with your file'):null))})};
    const go=t=>{if(f&&fits(t.id,f))D.use(t.id,files);else{D.pending=null;D.closeAll();location.hash='t-'+t.id}};
    inp.addEventListener('input',()=>{sel=0;paint()});
    inp.addEventListener('keydown',e=>{if(e.key==='ArrowDown'){sel=Math.min(items.length-1,sel+1);paint();e.preventDefault()}else if(e.key==='ArrowUp'){sel=Math.max(0,sel-1);paint();e.preventDefault()}else if(e.key==='Enter'&&items[sel])go(items[sel]);else if(e.key==='Escape')D.closeAll()});
    const p=h('div',{class:'dp sp'},h('div',{class:'dp-bar'},h('span',{},'🔎'),inp,h('button',{class:'dp-x','aria-label':'Close',onclick:()=>D.closeAll()},'×')));
    if(f)p.append(h('div',{class:'dp-ft'},'Using your file: ',h('b',{},f.name),' · tools that fit it come first'));
    p.append(res,h('div',{class:'dp-foot',style:'justify-content:center'},'↑↓ to move · Enter to open'));
    w.append(p);document.body.append(w);document.body.classList.add('dp-lock');paint();setTimeout(()=>inp.focus(),30)},
  keep(listEl,blob,name,curId){try{const f=new File([blob],name,{type:blob.type||MIME[(name.split('.').pop()||'').toLowerCase()]||''});D.last=f;let k=listEl.parentNode.querySelector('.dp-keep');if(!k){k=h('div',{class:'dp-keep'});listEl.after(k)}
    const list=fitList(f,curId).slice(0,12);k.innerHTML='';k.append(h('h4',{},'Keep going with this file'),h('p',{},name+' · same file, no re-upload. Pick the next tool.'));const c=h('div',{class:'dp-chips'});list.forEach(t=>c.append(D.chip(t,[f])));c.append(D.exploreChip([f]));k.append(c)}catch(e){console.warn(e)}}
};
/* hand pending file(s) to the tool that just opened */
const _open=TV.open.bind(TV);TV.open=function(id){D.cur=id;_open(id);if(!D.pending)return;const files=D.pending;D.pending=null;
  setTimeout(()=>{const inp=document.querySelector('#tpBox input[type=file]');if(!inp)return;const dt=new DataTransfer();(inp.multiple?files:files.slice(0,1)).forEach(x=>dt.items.add(x));inp.files=dt.files;inp.dispatchEvent(new Event('change',{bubbles:true}))},80)};
/* keep-going chips after an output appears */
const _out=U.out;U.out=function(root){const o=_out(root);const add=o.add;o.add=function(name,blob,label){add.call(o,name,blob,label);D.keep(o.el,blob,name,D.cur)};const clr=o.clear;o.clear=function(){clr.call(o);const k=o.el.parentNode&&o.el.parentNode.querySelector('.dp-keep');if(k)k.remove()};return o};
/* hero: drop on Dora */
const hero=document.querySelector('.hero'),mas=document.getElementById('mascot');
if(hero&&mas){const tag=h('span',{class:'dz-tag'},'⬇ Drop your file on Dora');mas.append(tag);
  const fi=h('input',{type:'file',hidden:true,multiple:true,'aria-label':'Choose a file'});mas.append(fi);
  mas.setAttribute('role','button');mas.setAttribute('tabindex','0');mas.setAttribute('aria-label','Drop a file on Dora or click to choose one');mas.style.cursor='pointer';
  mas.addEventListener('click',()=>fi.click());mas.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();fi.click()}});
  fi.onchange=()=>{const fs=[...fi.files];fi.value='';if(fs.length)D.panel(fs)};
  let dc=0;const on=v=>{hero.classList.toggle('dz-on',v);tag.textContent=v?'Drop it! 👇':'⬇ Drop your file on Dora'};
  hero.addEventListener('dragenter',e=>{if(![...(e.dataTransfer.types||[])].includes('Files'))return;e.preventDefault();dc++;on(true)});
  hero.addEventListener('dragover',e=>{if([...(e.dataTransfer.types||[])].includes('Files'))e.preventDefault()});
  hero.addEventListener('dragleave',()=>{if(--dc<=0){dc=0;on(false)}});
  hero.addEventListener('drop',e=>{e.preventDefault();dc=0;on(false);const fs=[...e.dataTransfer.files];if(fs.length)D.panel(fs)});
}
/* stop the browser from opening a file dropped outside a drop zone */
addEventListener('dragover',e=>{if([...(e.dataTransfer.types||[])].includes('Files'))e.preventDefault()});
addEventListener('drop',e=>{if(!e.defaultPrevented)e.preventDefault()});
addEventListener('keydown',e=>{if(e.key==='Escape')D.closeAll()});
})();
