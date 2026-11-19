/* ===== IMAGE TOOLS ===== */
(function(){
const T=d=>tool({cat:'image',file:true,...d});

async function pdfToImages(r,fmt){const sc=U.sel([['1.5','Normal (screen)'],['2.5','High (print)'],['4','Ultra']],{value:'2.5'});
  fileTool(r,{accept:'.pdf,application/pdf',opts:()=>U.row(U.field('Quality',sc)),go:async(fs,{out,prog})=>{const doc=await pdfDoc(fs[0]);const ext=fmt==='jpeg'?'jpg':'png';const outs=[];
    for(let p=1;p<=doc.numPages;p++){const c=await renderPage(doc,p,+sc.value);outs.push({n:`${base(fs[0].name)}-page${p}.${ext}`,b:await canvasBlob(c,'image/'+fmt,.93)});prog(p/doc.numPages*.9)}
    if(outs.length>1){await loadScript(CDN.jszip);const z=new JSZip();outs.forEach(o=>z.file(o.n,o.b));out.add(base(fs[0].name)+'-images.zip',await z.generateAsync({type:'blob'}),`All ${outs.length} pages (.zip)`)}outs.slice(0,15).forEach(o=>out.add(o.n,o.b))}})}
T({name:'PDF to JPG Converter',id:'pdf-to-jpg',pop:4,ic:'img',kw:'pdf to image picture',desc:'Export every PDF page as a sharp JPG image',run(r){pdfToImages(r,'jpeg')}});
T({name:'PDF to PNG',id:'pdf-to-png',ic:'img',kw:'pdf to image',desc:'Export PDF pages as lossless PNG images',run(r){pdfToImages(r,'png')}});
T({name:'Illustrator to PNG',id:'illustrator-to-png',kw:'ai adobe',desc:'Convert Adobe Illustrator .ai files to PNG',note:'Works with .ai files saved with PDF compatibility (the default in Illustrator).',run(r){fileTool(r,{accept:'.ai,application/postscript,application/pdf',go:async(fs,{out})=>{let doc;try{doc=await pdfDoc(fs[0])}catch(e){throw new Error('This .ai file was saved without PDF compatibility')}const c=await renderPage(doc,1,3);out.add(base(fs[0].name)+'.png',await canvasBlob(c,'image/png'))}})}});

T({name:'Image Compressor',id:'image-compressor',pop:9,kw:'compress reduce jpg png size',desc:'Shrink image file size while keeping quality',run(r){const q=U.sel([['0.82','Light'],['0.68','Balanced'],['0.5','Strong']],{value:'0.68'});const mw=U.sel([['0','Original size'],['2560','Max 2560px'],['1920','Max 1920px'],['1280','Max 1280px'],['800','Max 800px']],{value:'1920'});
  fileTool(r,{accept:'image/*',multi:true,opts:()=>U.row(U.field('Strength',q),U.field('Resize',mw)),btn:'Compress ✦',go:async(fs,{out,prog})=>{for(let i=0;i<fs.length;i++){const im=await imgFromFile(fs[i]);const png=/png/.test(fs[i].type);const c=drawTo(im,+mw.value,png?null:'#fff');const b=await canvasBlob(c,png?'image/webp':'image/jpeg',+q.value);const ext=png?'webp':'jpg';const n=`${base(fs[i].name)}-small.${ext}`;out.add(n,b,`${n} · ${Math.max(0,Math.round(100-b.size/fs[i].size*100))}% smaller`);prog((i+1)/fs.length)}}})}});

T({name:'GIF Maker',id:'gif-maker',kw:'animation animated',desc:'Turn a set of images into an animated GIF',run(r){const d=U.num(500);const w=U.sel([['320','320px'],['480','480px'],['640','640px']],{value:'480'});const loop=U.chk('Loop forever',true);
  fileTool(r,{accept:'image/*',multi:true,hint:'Add 2+ images — they play in this order',opts:()=>U.row(U.field('Frame delay (ms)',d),U.field('Width',w),loop),btn:'Make GIF ✦',go:async(fs,{out,prog,extra})=>{if(fs.length<2)throw new Error('Add at least 2 images');const {GIFEncoder,quantize,applyPalette}=await import(CDN.gifenc);const ims=[];for(const f of fs)ims.push(await imgFromFile(f));
    const W=+w.value,H=Math.round(W*ims[0].naturalHeight/ims[0].naturalWidth);const g=GIFEncoder();const c=canvasOf(W,H),x=c.getContext('2d',{willReadFrequently:true});
    ims.forEach((im,i)=>{x.fillStyle='#fff';x.fillRect(0,0,W,H);const s=Math.min(W/im.naturalWidth,H/im.naturalHeight);x.drawImage(im,(W-im.naturalWidth*s)/2,(H-im.naturalHeight*s)/2,im.naturalWidth*s,im.naturalHeight*s);const data=x.getImageData(0,0,W,H).data;const pal=quantize(data,256);g.writeFrame(applyPalette(data,pal),W,H,{palette:pal,delay:+d.value||500,repeat:loop.input.checked?0:-1});prog((i+1)/ims.length*.9)});
    g.finish();const b=new Blob([g.bytes()],{type:'image/gif'});out.add('animation.gif',b);extra.append(h('div',{class:'prev'},h('img',{src:URL.createObjectURL(b)})))}})}});

const conv=(name,id,to,accept,desc,kw,pop)=>T({name,id,desc,kw,pop,ic:'conv',run(r){imgConvertTool(r,{to,accept})}});
conv('HEIC to JPG Converter','heic-to-jpg','jpeg','.heic,.heif,image/heic,image/heif','Convert iPhone HEIC photos to JPG','iphone apple photo',10);
conv('HEIC to PNG Converter','heic-to-png','png','.heic,.heif,image/heic,image/heif','Convert iPhone HEIC photos to PNG','iphone apple');
conv('WebP to JPG Converter','webp-to-jpg','jpeg','image/webp','Convert WebP images to JPG');
conv('JPG to PNG Converter','jpg-to-png','png','image/jpeg','Convert JPG images to transparent-ready PNG','',11);
conv('AVIF to JPG Converter','avif-to-jpg','jpeg','image/avif,.avif','Convert AVIF images to JPG');
conv('AVIF to PNG Converter','avif-to-png','png','image/avif,.avif','Convert AVIF images to PNG');
conv('JPEG to PNG Converter','jpeg-to-png','png','image/jpeg','Convert JPEG photos to PNG');
conv('PNG to JPG Converter','png-to-jpg','jpeg','image/png','Convert PNG images to smaller JPG files');
conv('PNG to WebP Converter','png-to-webp','webp','image/png','Convert PNG to modern WebP format','web fast');
conv('WebP to PNG Converter','webp-to-png','png','image/webp','Convert WebP images to PNG');
T({name:'SVG to PNG Converter',id:'svg-to-png',ic:'conv',desc:'Render SVG vector files as PNG at any size',run(r){const sc=U.sel([['1','1x'],['2','2x'],['4','4x'],['8','8x']],{value:'2'});fileTool(r,{accept:'image/svg+xml,.svg',multi:true,opts:()=>U.row(U.field('Scale',sc)),go:async(fs,{out,prog})=>{for(let i=0;i<fs.length;i++){const im=await loadImg(fs[i]);const w=(im.naturalWidth||512)*sc.value,hh=(im.naturalHeight||512)*sc.value;const c=canvasOf(w,hh);c.getContext('2d').drawImage(im,0,0,w,hh);out.add(base(fs[i].name)+'.png',await canvasBlob(c,'image/png'));prog((i+1)/fs.length)}}})}});

async function traceSvg(f,detail){await loadScript(CDN.tracer);const im=await imgFromFile(f);const c=drawTo(im,800);const id=c.getContext('2d').getImageData(0,0,c.width,c.height);const o={hi:{numberofcolors:32,ltres:.5,qtres:.5,pathomit:4},mid:{numberofcolors:16,pathomit:8},lo:{numberofcolors:8,pathomit:16,blurradius:2}}[detail];return ImageTracer.imagedataToSVG(id,o)}
const svgT=(name,id,accept,desc)=>T({name,id,desc,kw:'vector trace',ic:'conv',run(r){const det=U.sel([['hi','High detail'],['mid','Balanced'],['lo','Simple / logo']],{value:'mid'});fileTool(r,{accept,opts:()=>U.row(U.field('Detail',det)),btn:'Vectorize ✦',go:async(fs,{out,extra,prog})=>{prog(.3);const svg=await traceSvg(fs[0],det.value);const b=textBlob(svg,'image/svg+xml');out.add(base(fs[0].name)+'.svg',b);extra.append(h('div',{class:'prev'},h('img',{src:URL.createObjectURL(b)})))}})}});
svgT('PNG to SVG Converter','png-to-svg','image/png','Trace PNG images into scalable SVG vectors');
svgT('WebP to SVG Converter','webp-to-svg','image/webp','Trace WebP images into SVG vectors');

T({name:'GPS Photo Stamper',id:'gps-photo-stamper',kw:'location geotag timestamp',desc:'Stamp location, date & time onto your photos',run(r){const addr=U.inp({placeholder:'Address or place name (optional)'});const lat=U.inp({placeholder:'Latitude'}),lon=U.inp({placeholder:'Longitude'}),dt=U.inp({type:'datetime-local'});const pv=h('div',{class:'prev'});let file=null,img=null;
  async function stamp(){if(!img)return;const c=drawTo(img,2400);const x=c.getContext('2d');const W=c.width,H=c.height,bh=Math.round(H*.16),fs=Math.round(bh/5);x.fillStyle='rgba(0,0,0,.55)';x.fillRect(0,H-bh,W,bh);x.fillStyle='#fff';x.font=`600 ${fs*1.15}px Arial`;let y=H-bh+fs*1.5;const lines=[addr.value,lat.value&&lon.value?`Lat ${(+lat.value).toFixed(6)}°  Long ${(+lon.value).toFixed(6)}°`:'',dt.value?new Date(dt.value).toLocaleString('en-GB',{dateStyle:'full',timeStyle:'short'}):''].filter(Boolean);lines.forEach((l,i)=>{x.font=`${i?400:600} ${fs*(i?1:1.15)}px Arial`;x.fillText(l,fs,y);y+=fs*1.45});pv.innerHTML='';pv.append(c);return c}
  U.drop(r,{accept:'image/*',onFiles:async fs=>{file=fs[0];img=await imgFromFile(file);try{await loadScript(CDN.exifr);const g=await exifr.gps(file);if(g){lat.value=g.latitude;lon.value=g.longitude}const ex=await exifr.parse(file,['DateTimeOriginal']);const d=ex&&ex.DateTimeOriginal?new Date(ex.DateTimeOriginal):new Date(file.lastModified);dt.value=new Date(d-d.getTimezoneOffset()*6e4).toISOString().slice(0,16)}catch(e){}stamp()}});
  [addr,lat,lon,dt].forEach(e=>e.addEventListener('input',stamp));r.append(U.row(U.field('Place',addr)),U.row(U.field('Latitude',lat),U.field('Longitude',lon),U.field('Date & time',dt)),pv,U.btn('Download stamped photo ✦',async()=>{const c=await stamp();if(!c)return toast('Upload a photo first');saveFile(base(file.name)+'-stamped.jpg',await canvasBlob(c,'image/jpeg',.93))}))}});

T({name:'Image Color Picker',id:'image-color-picker',kw:'eyedropper hex rgb palette',desc:'Click any pixel to get HEX, RGB and HSL codes',file:false,run(r){const pv=h('div',{class:'prev',style:'cursor:crosshair'});const res=U.res(h('div'));const pal=h('div',{style:'display:flex;gap:8px;flex-wrap:wrap;margin-top:12px'});
  const sw=(hex)=>h('button',{style:`width:54px;height:54px;border-radius:12px;background:${hex};border:1px solid var(--line)`,title:hex,onclick:()=>copyText(hex)});
  U.drop(r,{accept:'image/*',onFiles:async fs=>{const im=await imgFromFile(fs[0]);const c=drawTo(im,1600);const x=c.getContext('2d',{willReadFrequently:true});pv.innerHTML='';pv.append(c);c.style.width='100%';
    c.onclick=e=>{const b=c.getBoundingClientRect();const px=x.getImageData((e.clientX-b.left)*c.width/b.width|0,(e.clientY-b.top)*c.height/b.height|0,1,1).data;const hex='#'+[px[0],px[1],px[2]].map(v=>v.toString(16).padStart(2,'0')).join('');const [hh,s,l]=rgb2hsl(px[0],px[1],px[2]);res.set([['HEX',hex.toUpperCase(),true],['RGB',`rgb(${px[0]}, ${px[1]}, ${px[2]})`],['HSL',`hsl(${hh}, ${s}%, ${l}%)`]]);res.el.firstChild.style.background=`linear-gradient(135deg,${hex},${hex}88)`;copyText(hex.toUpperCase())};
    const sm=drawTo(im,60);const d=sm.getContext('2d').getImageData(0,0,sm.width,sm.height).data;const cnt={};for(let i=0;i<d.length;i+=4){const k=[d[i]>>5,d[i+1]>>5,d[i+2]>>5].join();cnt[k]=(cnt[k]||0)+1}pal.innerHTML='';Object.entries(cnt).sort((a,b)=>b[1]-a[1]).slice(0,8).forEach(([k])=>{const v=k.split(',').map(n=>(n*32+16).toString(16).padStart(2,'0'));pal.append(sw('#'+v.join('')))})}});
  r.append(pv,res.el,h('p',{class:'note'},'Dominant colors (click to copy):'),pal)}});
window.rgb2hsl=(r,g,b)=>{r/=255;g/=255;b/=255;const mx=Math.max(r,g,b),mn=Math.min(r,g,b);let hh=0,s=0;const l=(mx+mn)/2;if(mx!==mn){const d=mx-mn;s=l>.5?d/(2-mx-mn):d/(mx+mn);hh=mx===r?(g-b)/d+(g<b?6:0):mx===g?(b-r)/d+2:(r-g)/d+4;hh*=60}return[Math.round(hh),Math.round(s*100),Math.round(l*100)]};

T({name:'Image Flipper',id:'image-flipper',kw:'mirror rotate',desc:'Flip images horizontally or vertically, or rotate them',run(r){const op=U.sel([['h','Flip horizontal (mirror)'],['v','Flip vertical'],['r90','Rotate 90° right'],['r270','Rotate 90° left'],['r180','Rotate 180°']]);
  fileTool(r,{accept:'image/*',multi:true,opts:()=>U.row(U.field('Action',op)),btn:'Apply ✦',go:async(fs,{out,prog,extra})=>{for(let i=0;i<fs.length;i++){const im=await imgFromFile(fs[i]);const w=im.naturalWidth,hh=im.naturalHeight;const rot=op.value.startsWith('r')&&op.value!=='r180';const c=canvasOf(rot?hh:w,rot?w:hh);const x=c.getContext('2d');x.translate(c.width/2,c.height/2);
    if(op.value==='h')x.scale(-1,1);if(op.value==='v')x.scale(1,-1);if(op.value==='r90')x.rotate(Math.PI/2);if(op.value==='r270')x.rotate(-Math.PI/2);if(op.value==='r180')x.rotate(Math.PI);x.drawImage(im,-w/2,-hh/2);const png=/png/.test(fs[i].type);const b=await canvasBlob(c,png?'image/png':'image/jpeg',.95);out.add(base(fs[i].name)+'-edited.'+(png?'png':'jpg'),b);if(i===0)extra.append(h('div',{class:'prev'},h('img',{src:URL.createObjectURL(b)})));prog((i+1)/fs.length)}}})}});

T({name:'Image Resizer',id:'image-resizer',pop:12,kw:'resize dimensions scale pixels',desc:'Resize images to exact pixels or by percentage',run(r){const mode=U.sel([['px','By pixels'],['pct','By percentage']]);const w=U.num(1080),hh=U.num(''),pct=U.num(50);const keep=U.chk('Keep aspect ratio',true);const fmt=U.sel([['same','Same format'],['jpeg','JPG'],['png','PNG'],['webp','WebP']]);
  fileTool(r,{accept:'image/*',multi:true,opts:()=>[U.row(U.field('Mode',mode),U.field('Width (px)',w),U.field('Height (px)',hh),U.field('Percent %',pct)),U.row(keep,U.field('Output',fmt))],btn:'Resize ✦',go:async(fs,{out,prog})=>{for(let i=0;i<fs.length;i++){const im=await imgFromFile(fs[i]);let W,H;const iw=im.naturalWidth,ih=im.naturalHeight;
    if(mode.value==='pct'){W=iw*pct.value/100;H=ih*pct.value/100}else{W=+w.value||0;H=+hh.value||0;if(keep.input.checked){if(W&&!H)H=ih*W/iw;else if(H&&!W)W=iw*H/ih;else if(W&&H){const s=Math.min(W/iw,H/ih);W=iw*s;H=ih*s}}if(!W)W=iw;if(!H)H=ih}
    W=Math.max(1,Math.round(W));H=Math.max(1,Math.round(H));const c=canvasOf(W,H);const x=c.getContext('2d');x.imageSmoothingQuality='high';let f=fmt.value==='same'?(fs[i].type.split('/')[1]||'png'):fmt.value;if(!['jpeg','png','webp'].includes(f))f='png';if(f==='jpeg'){x.fillStyle='#fff';x.fillRect(0,0,W,H)}x.drawImage(im,0,0,W,H);out.add(`${base(fs[i].name)}-${W}x${H}.${extOf(f)}`,await canvasBlob(c,'image/'+f,.92));prog((i+1)/fs.length)}}})}});

T({name:'LinkedIn Photo Frame Editor',id:'linkedin-photo-frame',kw:'open to work hiring profile picture',desc:'Add an #OPENTOWORK style frame to your profile photo',run(r){const txt=U.inp({value:'#OPENTOWORK'});const col=U.inp({type:'color',value:'#ff2e88'});const pv=h('div',{class:'prev'});let img=null;
  function draw(){if(!img)return;const S=800,c=canvasOf(S,S),x=c.getContext('2d');x.save();x.beginPath();x.arc(S/2,S/2,S/2,0,Math.PI*2);x.clip();const s=Math.max(S/img.naturalWidth,S/img.naturalHeight);x.drawImage(img,(S-img.naturalWidth*s)/2,(S-img.naturalHeight*s)/2,img.naturalWidth*s,img.naturalHeight*s);x.restore();
    x.lineWidth=S*.1;x.strokeStyle=col.value;x.lineCap='round';x.beginPath();x.arc(S/2,S/2,S/2-S*.05,Math.PI*.62,Math.PI*1.18);x.stroke();
    x.save();x.fillStyle='#fff';x.font=`bold ${S*.052}px Arial`;x.textAlign='center';x.textBaseline='middle';const t=txt.value.toUpperCase(),R=S/2-S*.05;const total=Math.PI*.5;const step=total/Math.max(1,t.length);for(let i=0;i<t.length;i++){const a=Math.PI*1.15-step*(i+.5);x.save();x.translate(S/2+R*Math.cos(a),S/2+R*Math.sin(a));x.rotate(a-Math.PI/2);x.fillText(t[i],0,0);x.restore()}x.restore();pv.innerHTML='';pv.append(c);return c}
  U.drop(r,{accept:'image/*',onFiles:async fs=>{img=await imgFromFile(fs[0]);draw()}});[txt,col].forEach(e=>e.addEventListener('input',draw));r.append(U.row(U.field('Banner text',txt),U.field('Color',col)),pv,U.btn('Download PNG ✦',async()=>{const c=draw();if(!c)return toast('Upload a photo first');saveFile('profile-frame.png',await canvasBlob(c,'image/png'))}))}});

T({name:'Image Background Remover',id:'image-background-remover',pop:13,ic:'bg',kw:'remove bg transparent cutout png',desc:'Remove image backgrounds in HD with AI',long:'Cut out people, products and objects automatically. The AI runs inside your browser, so your photo never leaves your device.',
 note:'🔒 Processed on your device. Quick mode downloads a ≈13 MB AI model once. HD mode downloads ≈115 MB once and needs a modern browser with GPU (WebGPU); without it we use Quick mode.',
 run(r){const mode=U.sel([['quick','⚡ Quick — people & portraits'],['hd','✨ HD — any object (GPU)']]);const bgc=U.sel([['none','Transparent'],['#ffffff','White'],['#000000','Black'],['#ff2e88','Pink'],['#f3f0f7','Light grey']]);
  fileTool(r,{accept:'image/*,.heic,.heif',opts:()=>U.row(U.field('Mode',mode),U.field('Background',bgc)),btn:'Remove background ✦',go:async(fs,{out,prog,extra})=>{const f=fs[0];const im=await imgFromFile(f);
    const c=drawTo(im,2000);const W=c.width,H=c.height;const id=c.getContext('2d').getImageData(0,0,W,H);
    let m=mode.value;if(m==='hd'&&!(navigator.gpu&&await navigator.gpu.requestAdapter().catch(()=>null))){toast('No GPU acceleration in this browser — using Quick mode');m='quick'}
    let mask;try{mask=await bgMask(m,id,prog)}catch(e){console.error(e);if(m==='hd'){toast('HD model could not run here — using Quick mode');mask=await bgMask('quick',id,prog)}else throw new Error('AI model could not load. Check your internet and try again.')}
    for(let i=0;i<W*H;i++)id.data[i*4+3]=Math.round(id.data[i*4+3]*mask[i]/255);
    const o=canvasOf(W,H);const ox=o.getContext('2d');if(bgc.value!=='none'){ox.fillStyle=bgc.value;ox.fillRect(0,0,W,H);const t=canvasOf(W,H);t.getContext('2d').putImageData(id,0,0);ox.drawImage(t,0,0)}else ox.putImageData(id,0,0);
    const blob=await canvasBlob(o,'image/png');out.add(base(f.name)+'-no-bg.png',blob,`${base(f.name)}-no-bg.png · ${W}×${H}`);
    extra.append(compare(c.toDataURL('image/jpeg',.9),URL.createObjectURL(blob)),h('p',{class:'note'},'Drag the slider to compare before and after.'))}})}});
let bgW=null,bgSeq=0;const bgJobs={};
function bgWorker(){if(bgW)return bgW;const code=`let T,M={};const TJ='https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.7.1';
onmessage=async e=>{const {id,model,dtype,dev,w,h,data}=e.data;try{if(!T){T=await import(TJ);T.env.allowLocalModels=false}
if(!M[model]){const p=x=>{if(x.status==='progress'&&x.total>1e6)postMessage({id,prog:x.progress/100})};M[model]={m:await T.AutoModel.from_pretrained(model,{dtype,device:dev,progress_callback:p}),p:await T.AutoProcessor.from_pretrained(model)}}
const {m,p}=M[model];const img=new T.RawImage(new Uint8ClampedArray(data),w,h,4);const {pixel_values}=await p(img.rgb());const inName=m.sessions.model.inputNames[0];const out=await m({[inName]:pixel_values});
let t=out[Object.keys(out)[0]][0];if(/BiRefNet/.test(model))t=t.sigmoid();const mk=await T.RawImage.fromTensor(t.mul(255).to('uint8')).resize(w,h);const a=new Uint8Array(mk.data);postMessage({id,mask:a},[a.buffer])}catch(err){postMessage({id,err:String(err&&err.message||err)})}}`;
  bgW=new Worker(URL.createObjectURL(new Blob([code],{type:'text/javascript'})),{type:'module'});bgW.onmessage=e=>{const j=bgJobs[e.data.id];if(!j)return;if(e.data.prog!=null)return j.prog&&j.prog(.05+e.data.prog*.6);delete bgJobs[e.data.id];e.data.err?j.no(new Error(e.data.err)):j.ok(e.data.mask)};
  bgW.onerror=e=>{Object.values(bgJobs).forEach(j=>j.no(new Error('worker')));for(const k in bgJobs)delete bgJobs[k];bgW=null};return bgW}
function bgMask(mode,id,prog){const w=bgWorker();const n=++bgSeq;const cfg=mode==='hd'?{model:'onnx-community/BiRefNet_lite-ONNX',dtype:'fp16',dev:'webgpu'}:{model:'Xenova/modnet',dtype:'fp16',dev:'wasm'};
  return new Promise((ok,no)=>{bgJobs[n]={ok,no,prog};const d=id.data.slice().buffer;w.postMessage({id:n,...cfg,w:id.width,h:id.height,data:d},[d])})}

T({name:'Image to Text Converter',id:'image-to-text',pop:14,kw:'ocr extract text photo copy text from image picture to text',desc:'Extract text from images with AI OCR',long:'Pull the text out of photos, screenshots and scans. Pick the language, then copy the text or download it.',
 note:'🔒 Processed on your device. The text-recognition model downloads once per language (≈ 2–10 MB).',
 run(r){const lang=ocrLangSel();const box=h('textarea',{class:'uin',rows:12,style:'width:100%;margin-top:14px;display:none',placeholder:'Text will appear here'});
  fileTool(r,{accept:'image/*,.heic,.heif',multi:true,opts:()=>U.row(U.field('Language',lang)),btn:'Extract text ✦',go:async(fs,{out,prog,extra})=>{let all='';
    for(let i=0;i<fs.length;i++){const im=await imgFromFile(fs[i]);const c=drawTo(im,3000,'#fff');const d=await ocrRun(c,lang.value,p=>prog((i+p)/fs.length*.95));all+=(fs.length>1?`--- ${fs[i].name} ---\n`:'')+d.text.trim()+'\n\n'}
    all=all.trim();if(!all)throw new Error('No readable text found in this image.');box.value=all;box.style.display='block';
    out.add(base(fs[0].name)+'.txt',new Blob([all],{type:'text/plain'}),'Text file (.txt)');
    extra.append(box,h('button',{class:'btn ghost',style:'margin-top:10px',onclick:()=>{navigator.clipboard.writeText(box.value).then(()=>toast('Copied ✦'))}},'Copy text'))}})}});
T({name:'Compress GIF',id:'compress-gif',kw:'reduce gif size smaller animated gif optimizer',desc:'Reduce animated GIF file size',long:'Make big animated GIFs smaller by lowering colours, size or frame count, while keeping the animation.',
 run(r){const col=U.sel([['128','128 colours (best look)'],['64','64 colours (balanced)'],['32','32 colours (smallest)']],{value:'64'});const sc=U.sel([['1','Keep size'],['0.75','75% size'],['0.5','50% size']],{value:'1'});const skip=U.sel([['1','Keep all frames'],['2','Every 2nd frame']],{value:'1'});
  fileTool(r,{accept:'.gif,image/gif',opts:()=>U.row(U.field('Colours',col),U.field('Size',sc),U.field('Frames',skip)),btn:'Compress GIF ✦',go:async(fs,{out,prog,extra})=>{const f=fs[0];
    const {parseGIF,decompressFrames}=await import('https://cdn.jsdelivr.net/npm/gifuct-js@2.1.2/+esm');const {GIFEncoder,quantize,applyPalette}=await import(CDN.gifenc);
    const gif=parseGIF(await f.arrayBuffer());const frames=decompressFrames(gif,true);if(!frames.length)throw new Error('Could not read this GIF');
    const GW=gif.lsd.width,GH=gif.lsd.height;const k=+sc.value,W=Math.max(1,Math.round(GW*k)),H=Math.max(1,Math.round(GH*k));const st=+skip.value;
    const full=canvasOf(GW,GH),fx=full.getContext('2d',{willReadFrequently:true});const patch=canvasOf(1,1),px=patch.getContext('2d');const outC=canvasOf(W,H),ox=outC.getContext('2d',{willReadFrequently:true});
    const g=GIFEncoder();let prevImg=null;
    for(let i=0;i<frames.length;i++){const fr=frames[i];const d=fr.dims;if(fr.disposalType===3)prevImg=fx.getImageData(0,0,GW,GH);
      patch.width=d.width;patch.height=d.height;const pid=px.createImageData(d.width,d.height);pid.data.set(fr.patch);px.putImageData(pid,0,0);fx.drawImage(patch,d.left,d.top);
      if(i%st===0){ox.clearRect(0,0,W,H);ox.drawImage(full,0,0,W,H);const data=ox.getImageData(0,0,W,H).data;const pal=quantize(data,+col.value,{format:'rgba4444',oneBitAlpha:true});const idx=applyPalette(data,pal,'rgba4444');
        const tr=pal.findIndex(p=>p[3]===0);g.writeFrame(idx,W,H,{palette:pal,delay:(fr.delay||100)*st,transparent:tr>=0,transparentIndex:tr>=0?tr:0})}
      if(fr.disposalType===2)fx.clearRect(d.left,d.top,d.width,d.height);else if(fr.disposalType===3&&prevImg)fx.putImageData(prevImg,0,0);
      prog(i/frames.length*.95);if(i%5===0)await new Promise(r=>setTimeout(r))}
    g.finish();const blob=new Blob([g.bytes()],{type:'image/gif'});const pct=Math.round((1-blob.size/f.size)*100);
    out.add(base(f.name)+'-compressed.gif',blob,`${base(f.name)}-compressed.gif · ${pct>0?pct+'% smaller':'no smaller — try fewer colours or 50% size'}`);extra.append(h('img',{src:URL.createObjectURL(blob),style:'max-width:100%;margin-top:14px;border-radius:12px'}))}})}});
T({name:'Web to PNG',id:'web-to-png',file:false,kw:'website screenshot full page capture',desc:'Take a full screenshot of any website',run(r){const u=urlInput();const dev=U.sel([['1440','Desktop (1440px)'],['1024','Laptop (1024px)'],['768','Tablet (768px)'],['390','Phone (390px)']]);const full=U.chk('Full page',true);const out=U.out(r);const prev=h('div');
  const b=h('button',{class:'btn',style:'width:100%;margin-top:12px',onclick:async()=>{const v=u.value.trim();if(!v)return toast('⚠️ Enter a web address');b.disabled=true;b.textContent='Taking screenshot…';out.clear();prev.innerHTML='';
    try{const res=await apiFetch(`/shot?url=${encodeURIComponent(v)}&w=${dev.value}&full=${full.querySelector('input').checked?1:0}`);const bl=await res.blob();let host='website';try{host=new URL(/^https?:/.test(v)?v:'https://'+v).hostname}catch(e){}out.add(host+'.png',bl);prev.append(h('img',{src:URL.createObjectURL(bl),style:'max-width:100%;margin-top:14px;border-radius:12px;border:1px solid var(--line)'}));toast('Done ✦')}catch(e){toast('⚠️ '+friendlyErr(e))}b.disabled=false;b.textContent='Take screenshot ✦'}},'Take screenshot ✦');
  r.append(U.field('Website address',u),U.row(U.field('Device',dev),full),b,out.el,prev)}});
async function odfToImages(r,fmt){fileTool(r,{accept:'.odt,.odp,.ods,.odg,application/vnd.oasis.opendocument.text,application/vnd.oasis.opendocument.presentation,application/vnd.oasis.opendocument.graphics',go:async(fs,{out,prog})=>{const f=fs[0];await loadScript(CDN.jszip);const z=await JSZip.loadAsync(f);
  const ext=fmt==='jpeg'?'jpg':'png';const thumb=z.file('Thumbnails/thumbnail.png');const xml=z.file('content.xml')?await z.file('content.xml').async('string'):'';
  const dom=new DOMParser().parseFromString(xml,'application/xml');const blocks=[...dom.getElementsByTagNameNS('*','h'),...dom.getElementsByTagNameNS('*','p')].sort((a,b)=>a.compareDocumentPosition(b)&2?1:-1).map(e=>({h:e.localName==='h',t:e.textContent.trim()})).filter(b=>b.t);
  const imgs=[];for(const name of Object.keys(z.files))if(/^Pictures\/.+\.(png|jpe?g|gif|svg)$/i.test(name))imgs.push(name);
  if(!blocks.length&&!imgs.length&&!thumb)throw new Error('Nothing to convert in this file');
  const W=1240,M=90;const pages=[];let c=null,x=null,y=0;const np=()=>{c=canvasOf(W,1754);x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,W,1754);y=M;pages.push(c)};np();
  const wrap=(t,font,size,lh)=>{x.font=`${font} ${size}px Arial`;x.fillStyle='#111';const words=t.split(/\s+/);let line='';for(const w of words){const test=line?line+' '+w:w;if(x.measureText(test).width>W-2*M&&line){if(y+lh>1754-M)np(),x.font=`${font} ${size}px Arial`,x.fillStyle='#111';x.fillText(line,M,y+size);y+=lh;line=w}else line=test}if(line){if(y+lh>1754-M)np(),x.font=`${font} ${size}px Arial`,x.fillStyle='#111';x.fillText(line,M,y+size);y+=lh}y+=size*.6};
  blocks.forEach(b=>b.h?wrap(b.t,'bold',38,50):wrap(b.t,'',26,38));
  for(const n of imgs.slice(0,20)){try{const bl=await z.file(n).async('blob');const im=await imgFromFile(new File([bl],n));const sw=Math.min(W-2*M,im.naturalWidth),sh=sw*im.naturalHeight/im.naturalWidth;if(y+sh>1754-M)np();x.drawImage(im,M,y,sw,sh);y+=sh+30}catch(e){}}
  if(!blocks.length&&!imgs.length&&thumb){const im=await imgFromFile(new File([await thumb.async('blob')],'t.png'));pages[0]=drawTo(im,1240,'#fff')}
  const used=pages.filter((p,i)=>i===0||p);for(let i=0;i<used.length;i++){out.add(`${base(f.name)}${used.length>1?'-page'+(i+1):''}.${ext}`,await canvasBlob(used[i],'image/'+fmt,.92));prog((i+1)/used.length)}}})}
T({name:'ODF to JPG Converter',id:'odf-to-jpg',kw:'odt odp opendocument to image',desc:'Convert OpenDocument files to JPG images',run(r){odfToImages(r,'jpeg')}});
T({name:'ODF to PNG',id:'odf-to-png',kw:'odt odp opendocument to image',desc:'Convert OpenDocument files to PNG images',run(r){odfToImages(r,'png')}});
})();

/* ===== AI IMAGE UPSCALER + OBJECT REMOVER ===== */
(function(){
Object.assign(CDN,{
  tf:'https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.22.0/dist/tf.min.js',
  upscaler:'https://cdn.jsdelivr.net/npm/upscaler@1.0.0/dist/browser/umd/upscaler.min.js',
  esr2:'https://cdn.jsdelivr.net/npm/@upscalerjs/esrgan-slim@1.0.0/dist/umd/models/esrgan-slim/src/x2/index.min.js',
  esr4:'https://cdn.jsdelivr.net/npm/@upscalerjs/esrgan-slim@1.0.0/dist/umd/models/esrgan-slim/src/x4/index.min.js',
  opencv:'https://cdn.jsdelivr.net/npm/@techstark/opencv-js@4.10.0-release.1/dist/opencv.js'
});
const T=d=>tool({cat:'image',file:true,...d});
function compare(before,after){/* before/after slider */const wrap=h('div',{style:'position:relative;margin-top:16px;border-radius:16px;overflow:hidden;border:1px solid var(--line);background:repeating-conic-gradient(#1a1520 0 25%,#120e17 0 50%) 0 0/20px 20px;user-select:none;touch-action:none'});
  const a=h('img',{src:after,style:'display:block;width:100%'});const bw=h('div',{style:'position:absolute;inset:0;width:50%;overflow:hidden;border-right:3px solid #fff;box-shadow:0 0 20px #ff2e88'});const b=h('img',{src:before,style:'display:block;height:100%;width:auto;max-width:none;image-rendering:auto'});bw.append(b);
  const lab=(t,s)=>h('span',{style:`position:absolute;top:12px;${s};padding:6px 12px;border-radius:99px;background:#000a;color:#fff;font-size:12px;font-weight:600`},t);
  const knob=h('div',{style:'position:absolute;top:50%;left:50%;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;background:linear-gradient(135deg,#ff2e88,#9b3cff);display:grid;place-items:center;color:#fff;font-weight:900;box-shadow:0 0 24px #ff2e88;pointer-events:none'},'⇆');
  wrap.append(a,bw,lab('Before','left:12px'),lab('After','right:12px'),knob);
  const set=x=>{const r=wrap.getBoundingClientRect();const p=Math.max(0,Math.min(1,(x-r.left)/r.width));bw.style.width=p*100+'%';knob.style.left=p*100+'%'};
  const fit=()=>{b.style.height=wrap.getBoundingClientRect().height+'px';b.style.width=wrap.getBoundingClientRect().width+'px'};a.onload=fit;addEventListener('resize',fit);
  let dn=false;wrap.onpointerdown=e=>{dn=true;wrap.setPointerCapture(e.pointerId);set(e.clientX)};wrap.onpointermove=e=>dn&&set(e.clientX);wrap.onpointerup=()=>dn=false;return wrap}
function dataUrlToCanvas(u){return new Promise((ok,no)=>{const im=new Image();im.onload=()=>{const c=canvasOf(im.width,im.height);c.getContext('2d').drawImage(im,0,0);ok(c)};im.onerror=no;im.src=u})}
function classicUpscale(im,scale,sharp){let c=drawTo(im);let s=1;while(s<scale){const n=canvasOf(c.width*2,c.height*2),x=n.getContext('2d');x.imageSmoothingEnabled=true;x.imageSmoothingQuality='high';x.drawImage(c,0,0,n.width,n.height);c=n;s*=2}
  if(sharp>0){const W=c.width,H=c.height;const bl=canvasOf(W,H),bx=bl.getContext('2d');bx.filter=`blur(${Math.max(1,scale*.6)}px)`;bx.drawImage(c,0,0);const x=c.getContext('2d');const o=x.getImageData(0,0,W,H),b=bx.getImageData(0,0,W,H),d=o.data,e=b.data;for(let i=0;i<d.length;i+=4){d[i]+= (d[i]-e[i])*sharp;d[i+1]+=(d[i+1]-e[i+1])*sharp;d[i+2]+=(d[i+2]-e[i+2])*sharp}x.putImageData(o,0,0)}return c}
let upscalers={};
async function aiUpscale(im,scale,prog){await loadScript(CDN.tf);await loadScript(CDN.upscaler);await loadScript(scale===4?CDN.esr4:CDN.esr2);
  const key='x'+scale;if(!upscalers[key]){const base=scale===4?window.ESRGANSlim4x:window.ESRGANSlim2x;upscalers[key]=new Upscaler({model:{...base,path:`https://cdn.jsdelivr.net/npm/@upscalerjs/esrgan-slim@1.0.0/models/x${scale}/model.json`}})}
  try{await tf.ready()}catch(e){}const be=(window.tf&&tf.getBackend&&tf.getBackend())||'cpu';const src=drawTo(im);if(!/webgl|webgpu/.test(be)&&src.width*src.height>250000)throw new Error('no-gpu');const out=await upscalers[key].upscale(src,{output:'base64',patchSize:128,padding:6,progress:p=>prog(.1+p*.85)});return dataUrlToCanvas(out)}

T({name:'AI Image Upscaler',id:'image-upscaler',pop:12.5,kw:'upscale enlarge enhance hd 4k increase resolution sharpen photo quality',desc:'Upscale photos 2× or 4× with AI — bigger, sharper, HD',long:'Make small or blurry images bigger and sharper. Our AI model rebuilds detail as it enlarges your photo 2× or 4×, all inside your browser.',
 note:'🔒 Processed on your device. The AI model (≈ 2 MB) downloads once; on slower phones large images can take a minute. Use Fast mode for very large images.',
 run(r){const scale=U.sel([['2','2× (double size)'],['4','4× (HD boost)']]);const mode=U.sel([['ai','✨ AI — best quality'],['fast','⚡ Fast — classic + sharpen']]);
  fileTool(r,{accept:'image/*,.heic,.heif',opts:()=>U.row(U.field('Upscale',scale),U.field('Mode',mode)),btn:'Upscale ✦',go:async(fs,{out,prog,extra})=>{const f=fs[0];const im=await imgFromFile(f);const s=+scale.value;let c;const longSide=Math.max(im.naturalWidth,im.naturalHeight);
    if(mode.value==='ai'){if(longSide*s>6000)throw new Error(`Image is too large for AI ${s}× (max output ~6000px). Try 2× or Fast mode.`);
      try{prog(.05);c=await aiUpscale(im,s,prog)}catch(e){console.error(e);toast(e.message==='no-gpu'?'Your browser has no GPU acceleration — used Fast mode for this large image':'AI unavailable on this device — used Fast mode');c=classicUpscale(im,s,.8)}}
    else c=classicUpscale(im,s,.8);
    const blob=await canvasBlob(c,'image/png');out.add(`${base(f.name)}-${s}x.png`,blob,`${base(f.name)}-${s}x.png · ${c.width}×${c.height}`);
    const small=drawTo(im);extra.append(compare(small.toDataURL('image/jpeg',.9),URL.createObjectURL(blob)),h('p',{class:'note'},'Drag the slider to compare before and after.'))}})}});

let cvW=null,cvWarm=null;
function cvWorker(){if(cvW)return cvW;const code=`let ready=null;
function init(){if(!ready)ready=new Promise((res,rej)=>{try{importScripts(${JSON.stringify(CDN.opencv)});const c=self.cv;const done=()=>res({cv:c});if(c.Mat)done();else{c.onRuntimeInitialized=done;const t=setInterval(()=>{if(c.Mat){clearInterval(t);done()}},100)}}catch(e){rej(e)}});return ready}
onmessage=async e=>{const d=e.data;try{const {cv}=await init();if(d.warm){postMessage({id:d.id,ok:1});return}const src=cv.matFromImageData(d.img);const rgb=new cv.Mat();cv.cvtColor(src,rgb,cv.COLOR_RGBA2RGB);const m=new cv.Mat(d.h,d.w,cv.CV_8U);m.data.set(d.mask);const k=new cv.Mat();const ks=Math.max(7,(d.dil|0)*2+1);const ker=cv.getStructuringElement(cv.MORPH_ELLIPSE,new cv.Size(ks,ks));cv.dilate(m,k,ker);const dst=new cv.Mat();cv.inpaint(rgb,k,dst,d.rad,d.ns?cv.INPAINT_NS:cv.INPAINT_TELEA);const out=new cv.Mat();cv.cvtColor(dst,out,cv.COLOR_RGB2RGBA);const res=new ImageData(new Uint8ClampedArray(out.data),d.w,d.h);const km=new Uint8Array(k.data);[src,rgb,m,k,ker,dst,out].forEach(x=>x.delete());postMessage({id:d.id,res,km},[res.data.buffer,km.buffer])}catch(err){postMessage({id:d.id,err:String(err&&err.message||err)})}}`;
  cvW=new Worker(URL.createObjectURL(new Blob([code],{type:'text/javascript'})));return cvW}
function cvCall(msg,timeout=90000){const w=cvWorker();return new Promise((ok,no)=>{const id=Math.random();const t=setTimeout(()=>no(new Error('Timed out — try a smaller brush area')),timeout);w.addEventListener('message',function f(e){if(e.data.id!==id)return;w.removeEventListener('message',f);clearTimeout(t);e.data.err?no(new Error(e.data.err)):ok(e.data)});w.postMessage({...msg,id},msg.img?[msg.img.data.buffer]:[])})}
function cvPreload(){if(!cvWarm)cvWarm=cvCall({warm:1}).catch(e=>{cvWarm=null;throw e});return cvWarm}

/* smooth "membrane" fill: solves the hole from its border so gradients and flat colours blend perfectly */
function harmonicFill(id,km,w,h){const d=id.data;const idx=[];for(let i=0;i<w*h;i++)if(km[i])idx.push(i);if(!idx.length)return;
  const f=[new Float32Array(w*h),new Float32Array(w*h),new Float32Array(w*h)];for(let i=0;i<w*h;i++){f[0][i]=d[i*4];f[1][i]=d[i*4+1];f[2][i]=d[i*4+2]}
  const it=Math.min(1500,Math.max(200,Math.round(Math.sqrt(idx.length)*6)));
  for(let n=0;n<it;n++)for(const i of idx){const x=i%w,y=(i-x)/w;let c=0,a=0,b=0,g=0;
    if(x>0){c++;a+=f[0][i-1];b+=f[1][i-1];g+=f[2][i-1]}if(x<w-1){c++;a+=f[0][i+1];b+=f[1][i+1];g+=f[2][i+1]}if(y>0){c++;a+=f[0][i-w];b+=f[1][i-w];g+=f[2][i-w]}if(y<h-1){c++;a+=f[0][i+w];b+=f[1][i+w];g+=f[2][i+w]}
    f[0][i]=a/c;f[1][i]=b/c;f[2][i]=g/c}
  for(const i of idx){d[i*4]=f[0][i];d[i*4+1]=f[1][i];d[i*4+2]=f[2][i]}}
function borderStd(id,km,w,h){const d=id.data;let n=0,s=[0,0,0],q=[0,0,0];for(let y=1;y<h-1;y++)for(let x=1;x<w-1;x++){const i=y*w+x;if(km[i])continue;if(km[i-1]||km[i+1]||km[i-w]||km[i+w]){for(let c=0;c<3;c++){const v=d[i*4+c];s[c]+=v;q[c]+=v*v}n++}}
  if(!n)return 0;let t=0;for(let c=0;c<3;c++){const m=s[c]/n;t+=Math.sqrt(Math.max(0,q[c]/n-m*m))}return t/3}
function featherInto(orig,res,km,w,h){/* soften the seam: 2px blend ring outside the hole */const o=orig.data,r=res.data;
  for(let y=1;y<h-1;y++)for(let x=1;x<w-1;x++){const i=y*w+x;if(km[i])continue;let nb=km[i-1]||km[i+1]||km[i-w]||km[i+w];if(!nb)continue;for(let c=0;c<3;c++)r[i*4+c]=(o[i*4+c]*.5+r[i*4+c]*.5)}}
function removerRun(r){let base0=null,work=null,mask=null,hist=[];const brush=h('input',{class:'uin',type:'range',min:6,max:120,value:34});const meth=U.sel([['auto','✨ Auto (recommended)'],['smooth','Smooth fill (logos, skin, sky, flat colours)'],['telea','Texture (busy photos)'],['ns','Lines & edges']]);
  const stage=h('div',{style:'position:relative;margin:16px auto 0;width:fit-content;max-width:100%;display:none;border-radius:16px;overflow:hidden;border:1px solid var(--line);touch-action:none;cursor:crosshair'});const view=canvasOf(10,10),ov=canvasOf(10,10);view.style.cssText='display:block;max-width:100%;max-height:70vh';ov.style.cssText='position:absolute;inset:0;width:100%;height:100%;opacity:.55';stage.append(view,ov);
  const cur=h('div',{style:'position:absolute;border:2px solid #fff;border-radius:50%;pointer-events:none;box-shadow:0 0 0 2px #ff2e88;display:none;transform:translate(-50%,-50%)'});stage.append(cur);
  const draw=()=>{view.getContext('2d').drawImage(work,0,0)};
  U.drop(r,{accept:'image/*,.heic,.heif',onFiles:async fs=>{const im=await imgFromFile(fs[0]);work=drawTo(im,1400);base0=fs[0].name;[view,ov].forEach(c=>{c.width=work.width;c.height=work.height});mask=ov.getContext('2d');mask.clearRect(0,0,ov.width,ov.height);hist=[];draw();stage.style.display='block';cvPreload().catch(()=>{})}});
  let dn=false,last=null;const pt=e=>{const b=ov.getBoundingClientRect();return[(e.clientX-b.left)*ov.width/b.width,(e.clientY-b.top)*ov.height/b.height]};
  const stroke=(p)=>{const k=ov.width/ov.getBoundingClientRect().width;mask.strokeStyle=mask.fillStyle='#ff2e88';mask.lineCap='round';mask.lineJoin='round';mask.lineWidth=brush.value*k;mask.beginPath();if(last){mask.moveTo(...last);mask.lineTo(...p);mask.stroke()}else{mask.arc(p[0],p[1],brush.value*k/2,0,7);mask.fill()}last=p};
  stage.onpointerdown=e=>{if(!work)return;dn=true;stage.setPointerCapture(e.pointerId);last=null;stroke(pt(e))};
  stage.onpointermove=e=>{const b=stage.getBoundingClientRect();cur.style.display='block';cur.style.left=(e.clientX-b.left)+'px';cur.style.top=(e.clientY-b.top)+'px';cur.style.width=cur.style.height=brush.value+'px';if(dn)stroke(pt(e))};
  stage.onpointerup=()=>{dn=false;last=null};stage.onpointerleave=()=>{cur.style.display='none'};
  const remove=async e=>{if(!work)return toast('Upload an image first');const b=e.currentTarget;b.disabled=true;const t=b.textContent;b.textContent='Removing…';
    try{const W=ov.width,Hh=ov.height;const md=mask.getImageData(0,0,W,Hh).data;let x0=1e9,y0=1e9,x1=-1,y1=-1;
      for(let y=0;y<Hh;y++)for(let x=0;x<W;x++){if(md[(y*W+x)*4+3]>20){if(x<x0)x0=x;if(x>x1)x1=x;if(y<y0)y0=y;if(y>y1)y1=y}}
      if(x1<0)throw new Error('Brush over the object you want to remove first');
      const pad=Math.round(Math.max(40,(x1-x0+y1-y0)*.35));x0=Math.max(0,x0-pad);y0=Math.max(0,y0-pad);x1=Math.min(W-1,x1+pad);y1=Math.min(Hh-1,y1+pad);const w=x1-x0+1,hh=y1-y0+1;
      const img=work.getContext('2d').getImageData(x0,y0,w,hh);const mm=new Uint8Array(w*hh);const mr=mask.getImageData(x0,y0,w,hh).data;for(let j=0;j<w*hh;j++)mm[j]=mr[j*4+3]>20?255:0;
      b.textContent='Loading engine…';await cvPreload();b.textContent='Removing…';
      const k2=ov.width/ov.getBoundingClientRect().width;const r2=await cvCall({img,mask:mm,w,h:hh,rad:Math.min(10,Math.max(3,Math.round(brush.value/5))),ns:meth.value==='ns',dil:Math.max(3,Math.round(brush.value*k2/6))});
      let mode=meth.value;if(mode==='auto')mode=borderStd(img,r2.km,w,hh)<22?'smooth':'telea';if(mode==='smooth')harmonicFill(r2.res,r2.km,w,hh);featherInto(img,r2.res,r2.km,w,hh);
      hist.push(drawTo(work));if(hist.length>15)hist.shift();const outc=drawTo(work);outc.getContext('2d').putImageData(r2.res,x0,y0);work=outc;
      mask.clearRect(0,0,W,Hh);draw();sDone();toast('Removed ✦ Brush again to clean up more')}
    catch(err){console.error(err);toast('⚠️ '+friendlyErr(err))}b.disabled=false;b.textContent=t};
  r.append(U.row(U.field('Brush size',brush),U.field('Fill style',meth)),stage,U.row(U.btn('Remove object ✦',remove),U.btn('Undo',()=>{if(hist.length){work=hist.pop();draw()}else mask&&mask.clearRect(0,0,ov.width,ov.height)},'btn btn-g'),U.btn('Clear brush',()=>mask&&mask.clearRect(0,0,ov.width,ov.height),'btn btn-g'),
    U.btn('Download PNG',async()=>{if(!work)return;saveFile(base(base0||'image')+'-clean.png',await canvasBlob(work,'image/png'))},'btn btn-g')),
    h('p',{class:'note'},'Tip: brush slightly beyond the edges of the object. Works best on small–medium objects, text, people in the background and blemishes. Repeat for a cleaner result.'))}
T({name:'Watermark Eraser',id:'watermark-eraser',kw:'remove watermark logo text date stamp',desc:'Brush over a watermark, logo or date stamp to erase it',note:'Only remove watermarks from images you own or have permission to edit.',run:removerRun});
T({name:'Object Remover',id:'object-remover',pop:13.6,kw:'remove object person text erase magic eraser cleanup photo',desc:'Brush over any object, person or text — and make it disappear',long:'Select unwanted objects, people, text or blemishes with a brush and remove them from your photo in one click.',run:removerRun});
})();
