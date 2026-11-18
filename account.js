/* DoraPDF accounts + Assignment Helper (assignments & presentations) (talks to the dorapdf-api worker) */
(function(){
const TK='dora_tok';
let TOKEN=null,USER=null,CFG=null,MODE='assignment',lastSlides=null,pending=null;
try{TOKEN=localStorage.getItem(TK)}catch(e){}
const setTok=t=>{TOKEN=t;try{t?localStorage.setItem(TK,t):localStorage.removeItem(TK)}catch(e){}};

async function call(path,opt={}){const headers={'Content-Type':'application/json',...(opt.headers||{})};if(TOKEN)headers.Authorization='Bearer '+TOKEN;
  let r;try{r=await fetch(API+path,{...opt,headers})}catch(e){throw new Error('Could not reach the server. Check your internet and try again.')}
  let j={};try{j=await r.json()}catch(e){}
  if(j.user){USER=j.user;paint()}
  if(r.status===401){if(j.code==='other-device')toast('⚠️ '+j.error);setTok(null);USER=null;paint();const e=new Error(j.error||'Please sign in');e.code='login';throw e}
  if(!r.ok){const e=new Error(j.error||('Something went wrong ('+r.status+')'));e.code=j.code;throw e}
  return j}
async function config(){if(CFG)return CFG;try{CFG=await (await fetch(API+'/config')).json()}catch(e){CFG={googleClientId:'',pay:{},pkr:{pro:1699,max:5299},country:''}}paintPrices();return CFG}
const isPK=()=>((USER&&USER.country)||(CFG&&CFG.country))==='PK';

/* ---------- modals ---------- */
function modal(title,body,cls){closeModal();const w=h('div',{class:'dp-wrap',id:'acModal',onclick:e=>{if(e.target===w)closeModal()}});
  const p=h('div',{class:'dp '+(cls||''),role:'dialog','aria-label':title},h('div',{class:'dp-top'},h('div',{style:'font:800 18px Unbounded,sans-serif'},title),h('button',{class:'dp-x','aria-label':'Close',onclick:closeModal},'×')));
  p.append(body);w.append(p);document.body.append(w);document.body.classList.add('dp-lock');return p}
function closeModal(){const m=document.getElementById('acModal');if(m)m.remove();if(!document.querySelector('.dp-wrap'))document.body.classList.remove('dp-lock')}

async function loginModal(reason){const cfg=await config();const slot=h('div',{style:'display:flex;justify-content:center;margin:18px 0 8px;min-height:44px'});
  const body=h('div',{},h('p',{class:'dp-sub',style:'font-size:14px'},reason||'Sign in to start your 3-day free trial of the Assignment Helper: 3 assignment drafts and 3 presentations.'),slot,
    h('p',{class:'dp-sub',style:'font-size:12px;text-align:center'},'Only verified Google accounts. One account works on one device at a time. By continuing you agree to our ',h('a',{href:'/terms/',style:'color:var(--pink2)'},'Terms'),' and ',h('a',{href:'/privacy/',style:'color:var(--pink2)'},'Privacy policy'),'.'));
  modal('Sign in to DoraPDF',body);
  if(!cfg.googleClientId){slot.append(h('p',{class:'dp-sub'},'Sign-in is being set up. Please try again soon.'));return}
  try{await loadScript('https://accounts.google.com/gsi/client');google.accounts.id.initialize({client_id:cfg.googleClientId,callback:onCred,ux_mode:'popup',auto_select:false,itp_support:true});
    google.accounts.id.renderButton(slot,{theme:'filled_black',size:'large',shape:'pill',text:'continue_with',width:280})}catch(e){slot.append(h('p',{class:'dp-sub'},'Could not load Google sign-in. Disable ad-blockers and try again.'))}}
async function onCred(resp){loadScript('https://accounts.google.com/gsi/client').catch(()=>{});try{const j=await call('/auth/google',{method:'POST',body:JSON.stringify({credential:resp.credential})});setTok(j.token);USER=j.user;paint();closeModal();toast('Welcome, '+(USER.name||USER.email).split(' ')[0]+' ✦');
    if(pending){const f=pending;pending=null;f()}}catch(e){toast('⚠️ '+e.message)}}

const PN={trial:'Free trial',pro:'Pro',max:'Max',none:'No active plan'};
const dt=t=>t?new Date(t).toLocaleDateString(undefined,{day:'numeric',month:'short',year:'numeric'}):'';
function accountModal(){if(!USER)return loginModal();const u=USER;const left=u.fairUse?'Unlimited (fair use: '+u.assignLeft+' left today)':null;
  const body=h('div',{class:'acm'},
    h('div',{style:'display:flex;align-items:center;gap:12px;margin-bottom:10px'},u.picture?h('img',{src:u.picture,referrerpolicy:'no-referrer',style:'width:46px;height:46px;border-radius:50%'}):null,h('div',{},h('div',{style:'font-weight:700'},u.name||''),h('div',{class:'dp-sub'},u.email))),
    h('div',{class:'row'},h('span',{},'Plan'),h('b',{},PN[u.plan]||u.plan)),
    u.endsAt?h('div',{class:'row'},h('span',{},u.plan==='trial'?'Trial ends':'Renews / ends'),h('b',{},dt(u.endsAt))):null,
    h('div',{class:'row'},h('span',{},'Assignments left'),h('b',{},left||String(u.assignLeft))),
    h('div',{class:'row'},h('span',{},'Presentations left'),h('b',{},left?'Same as above':String(u.slidesLeft))),
    (u.docs&&u.docs.length)?h('div',{style:'margin-top:14px'},h('div',{class:'dp-lbl'},'My documents (Google Drive)'),...u.docs.slice(0,10).map(d=>h('a',{href:d.link,target:'_blank',rel:'noopener',class:'row',style:'text-decoration:none;color:inherit'},h('span',{},(d.type==='slides'?'📊 ':'📝 ')+d.t),h('b',{},dt(d.at))))):h('p',{class:'dp-sub',style:'margin-top:12px'},'Documents you save to Google Drive will be listed here.'),
    h('div',{style:'display:flex;gap:10px;margin-top:16px;flex-wrap:wrap'},
      u.plan!=='max'?h('button',{class:'btn btn-p',onclick:()=>{closeModal();location.hash='pricing'}},'Upgrade'):null,
      h('button',{class:'btn btn-g',onclick:async()=>{try{await call('/auth/logout',{method:'POST'})}catch(e){}setTok(null);USER=null;paint();closeModal();toast('Signed out')}},'Sign out')));
  modal('Your account',body)}

/* ---------- checkout ---------- */
async function checkout(plan){const cfg=await config();if(!USER){pending=()=>checkout(plan);return loginModal('Sign in first, then choose how to pay.')}
  const P=cfg.plans&&cfg.plans[plan]||{usd:plan==='pro'?6:19};const pk=isPK();const pkr=(cfg.pkr||{})[plan];
  const methods=pk?[['jazzcash','🟥','JazzCash'],['easypaisa','🟩','Easypaisa'],['nayapay','🟧','NayaPay'],['card','💳','Card / international (USD)']]:[['card','💳','Card (Visa / Mastercard)']];
  let sel=methods[0][0];const area=h('div');const box=h('div',{class:'paybox'});
  const draw=()=>{box.innerHTML='';methods.forEach(([k,i,n])=>box.append(h('button',{class:'payopt'+(sel===k?' on':''),onclick:()=>{sel=k;draw()}},h('i',{},i),n)));area.innerHTML='';
    if(sel==='card'){area.append(h('p',{class:'dp-sub',style:'font-size:14px'},'International card payments are opening very soon. For now email ',h('a',{href:'mailto:hello@dorapdf.com',style:'color:var(--pink2)'},'hello@dorapdf.com'),' and we will send you a payment link.'));return}
    const acc=(cfg.pay||{})[sel];if(!acc){area.append(h('p',{class:'dp-sub',style:'font-size:14px'},'This payment method is opening soon. Please pick another or email hello@dorapdf.com.'));return}
    const txn=h('input',{class:'dp-in',style:'border:1px solid #2c2236;border-radius:12px;padding:12px;width:100%;box-sizing:border-box',placeholder:'Transaction ID (TID)'});
    const send=h('button',{class:'btn btn-p',style:'width:100%;justify-content:center;margin-top:12px',onclick:async()=>{if(!txn.value.trim())return toast('⚠️ Enter the transaction ID');send.disabled=true;
      try{const j=await call('/pay/claim',{method:'POST',body:JSON.stringify({plan,method:sel,txn:txn.value.trim(),amount:'PKR '+pkr})});closeModal();toast('✦ '+j.message)}catch(e){toast('⚠️ '+e.message)}send.disabled=false}},'I have paid ✦');
    area.append(h('ol',{class:'dp-sub',style:'font-size:14px;line-height:1.7;padding-left:18px'},h('li',{},'Open your ',h('b',{},methods.find(m=>m[0]===sel)[2]),' app'),h('li',{},'Send ',h('b',{},'Rs '+(+pkr).toLocaleString()),' to: ',h('b',{style:'color:#fff'},acc)),h('li',{},'Paste the transaction ID below')),txn,send,
      h('p',{class:'dp-sub',style:'font-size:12px;margin-top:10px'},'Your plan is switched on after we confirm the payment (usually within a few hours). It renews monthly: pay again each month to continue.'))};
  draw();
  modal((plan==='pro'?'Pro':'Max')+' plan',h('div',{},h('div',{style:'font:800 30px Unbounded,sans-serif'},h('s',{class:'was'},'$'+(P.was||'')),' $'+P.usd,h('small',{style:'font:500 14px Space Grotesk,sans-serif;color:#9a90a6'},' /month'+(pk&&pkr?' · Rs '+(+pkr).toLocaleString():''))),
    h('p',{class:'dp-sub'},plan==='pro'?'6 assignments + 6 presentations every month':'Unlimited assignments and presentations (fair use 30/day)'),h('div',{class:'dp-lbl',style:'margin-top:14px'},'Pay with'),box,area))}


/* ---------- Google Drive (drive.file: only files DoraPDF creates) ---------- */
let driveTok=null,driveExp=0;
function driveAuth(){return new Promise((ok,no)=>{if(driveTok&&Date.now()<driveExp)return ok(driveTok);if(!(window.google&&google.accounts&&google.accounts.oauth2)||!CFG||!CFG.googleClientId)return no(new Error('Google Drive is still loading, try again'));
  const c=google.accounts.oauth2.initTokenClient({client_id:CFG.googleClientId,scope:'https://www.googleapis.com/auth/drive.file',login_hint:USER&&USER.email||'',callback:r=>{if(r&&r.access_token){driveTok=r.access_token;driveExp=Date.now()+((r.expires_in||3600)-120)*1000;ok(driveTok)}else no(new Error('Google Drive permission was not given'))},error_callback:()=>no(new Error('Google Drive permission was not given'))});
  c.requestAccessToken({prompt:driveTok?'':'consent'})})}
async function gd(path,opt={}){const r=await fetch('https://www.googleapis.com'+path,{...opt,headers:{Authorization:'Bearer '+driveTok,...(opt.headers||{})}});if(r.status===401){driveTok=null;throw new Error('Google Drive session expired, press Save to Drive again')}if(!r.ok)throw new Error('Google Drive error ('+r.status+')');return r.json()}
async function driveUpload(blob,name,type){await driveAuth();
  let q=encodeURIComponent("name='DoraPDF' and mimeType='application/vnd.google-apps.folder' and trashed=false");let f=(await gd('/drive/v3/files?fields=files(id)&q='+q)).files||[];
  let folder=f[0]&&f[0].id;if(!folder)folder=(await gd('/drive/v3/files?fields=id',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:'DoraPDF',mimeType:'application/vnd.google-apps.folder'})})).id;
  const meta={name,parents:[folder]};const fd=new FormData();fd.append('metadata',new Blob([JSON.stringify(meta)],{type:'application/json'}));fd.append('file',blob);
  const res=await gd('/upload/drive/v3/files?uploadType=multipart&fields=id,webViewLink',{method:'POST',body:fd});
  try{await call('/docs/add',{method:'POST',body:JSON.stringify({title:name,type,link:res.webViewLink})})}catch(e){}
  return res.webViewLink}
async function currentFile(){/* build the current document without downloading it */const real=window.saveFile;let got=null;window.saveFile=(n,b)=>{got={name:n,blob:b}};
  try{if(lastSlides&&!lastDoc){got={name:(lastSlides.title||'presentation').replace(/[^\w\- ]+/g,'').slice(0,60).trim()+'.pptx',blob:await buildPptx(lastSlides)}}else if(lastDoc)await realDocx()}finally{window.saveFile=real}return got}
let realDocx=null;
async function saveToDrive(auto){const b=$q('#driveBtn');try{if(!auto&&!(driveTok&&Date.now()<driveExp))await driveAuth();b&&(b.disabled=true,b.textContent='Saving…');const f=await currentFile();if(!f)throw new Error('Create a document first');
    const link=await driveUpload(f.blob,f.name,lastSlides&&!lastDoc?'slides':'assignment');toast('✦ Saved to Google Drive › DoraPDF');if(b){b.textContent='Open in Drive ↗';b.disabled=false;b.onclick=()=>window.open(link,'_blank','noopener')}}
  catch(e){toast('⚠️ '+e.message);if(b){b.disabled=false;b.textContent='Save to Drive';b.onclick=()=>saveToDrive(false)}}}

/* ---------- paint ---------- */
function paint(){const b=document.getElementById('acctBtn');if(b){b.innerHTML='';if(USER){if(USER.picture)b.append(h('img',{src:USER.picture,referrerpolicy:'no-referrer',alt:''}));b.append(h('span',{class:'nm'},(USER.name||USER.email).split(' ')[0]))}else b.textContent='Sign in'}
  const t=document.getElementById('trialTxt');if(t){if(!USER)t.innerHTML='3-day free trial · sign in with Google';else if(USER.plan==='none')t.innerHTML='Trial <b>ended</b> · upgrade to continue';
    else t.innerHTML=`<b>${PN[USER.plan]}</b> · ${USER.fairUse?USER.assignLeft+' left today':USER.assignLeft+' assignments, '+USER.slidesLeft+' presentations left'}`}}
function paintPrices(){if(!CFG)return;document.querySelectorAll('.pkr').forEach(e=>{const v=(CFG.pkr||{})[e.dataset.plan];e.textContent=isPK()&&v?'≈ Rs '+(+v).toLocaleString()+' /month · JazzCash, Easypaisa, NayaPay':'Monthly subscription'})}

/* ---------- AI form ---------- */
const $q=s=>document.querySelector(s);
function setMode(m){MODE=m;document.querySelectorAll('#gType button').forEach(b=>b.classList.toggle('on',b.dataset.v===m));
  $q('#lenWrap').style.display=m==='assignment'?'':'none';$q('#slWrap').style.display=m==='slides'?'':'none';
  const cite=$q('#gCite');if(cite)cite.closest('.field').style.display=m==='assignment'?'':'none';
  $q('#docxBtn').textContent=m==='assignment'?'Download .docx':'Download .pptx'}
document.querySelectorAll('#gType button').forEach(b=>b.addEventListener('click',()=>setMode(b.dataset.v)));

function renderSlides(d){let html='<div class="slide-prev">';html+=`<div class="sl t"><h4>${esc(d.title||'')}</h4><div>${esc(d.subtitle||'')}</div></div>`;
  (d.slides||[]).forEach((s,i)=>{if(i===0&&/title/i.test(s.title||'')&&!(s.bullets||[]).length)return;html+=`<div class="sl"><h4>${esc(s.title||'')}</h4><ul>${(s.bullets||[]).map(b=>`<li>${esc(b)}</li>`).join('')}</ul>${s.image&&refDataUrl?`<img src="${refDataUrl}" style="position:absolute;right:14px;bottom:14px;width:30%;border-radius:8px">`:s.img?`<img src="${esc(s.img.src)}" onerror="this.remove()" style="position:absolute;right:14px;bottom:14px;width:32%;max-height:70%;object-fit:cover;border-radius:8px">`:''}<span class="n">${i+1}</span></div>`});
  $q('#paper').innerHTML=html+'</div>';$q('#paper').style.display='block';$q('#outEmpty').style.display='none';$q('#copyBtn').disabled=false;$q('#docxBtn').disabled=false;$q('#outTag').textContent=(d.slides||[]).length+' slides · '+$q('#gLevel').value}

async function buildPptx(d){await loadScript(CDN.pptx);const pp=new PptxGenJS();pp.layout='LAYOUT_WIDE';pp.title=d.title||'Presentation';
  const PINK=themeColor(),VIO='3A1D5C',FONT='Arial';const bgMode=$q('#gBg')?$q('#gBg').value:'none';const LIGHT=bgMode==='tint';const DARK=LIGHT?'FFFFFF':'0E0B13';const TXT=LIGHT?'222222':'F3EEF7';let BGIMG=null;if(bgMode==='image'&&$q('#gBgImg').files[0]){const im=await loadImg($q('#gBgImg').files[0]);const c=drawTo(im,1920,'#000');BGIMG=c.toDataURL('image/jpeg',.85)}let img=null,iw=0,ih=0;
  if(refFile){const im=await loadImg(refFile);const c=drawTo(im,1600,'#fff');img=c.toDataURL('image/jpeg',.9);iw=c.width;ih=c.height}
  const t=pp.addSlide();if(BGIMG){t.background={data:BGIMG};t.addShape(pp.ShapeType.rect,{x:0,y:0,w:13.33,h:7.5,fill:{color:'000000',transparency:45}})}else{t.background={color:PINK};t.addShape(pp.ShapeType.rect,{x:0,y:0,w:13.33,h:7.5,fill:{color:'000000',transparency:75}})}
  t.addText(d.title||'',{x:.8,y:2.3,w:11.7,h:1.6,fontFace:FONT,fontSize:40,bold:true,color:'FFFFFF'});t.addText(d.subtitle||'',{x:.8,y:3.9,w:11.7,h:.8,fontFace:FONT,fontSize:20,color:'FFFFFF'});
  const name=$q('#gName').value.trim(),course=$q('#gCourse').value.trim();if(name||course)t.addText([name,course].filter(Boolean).join(' · '),{x:.8,y:5.6,w:11.7,h:.5,fontFace:FONT,fontSize:14,color:'FFFFFF'});
  const SL=d.slides||[];for(let i=0;i<SL.length;i++){const s=SL[i];if(i===0&&!(s.bullets||[]).length)continue;const sl=pp.addSlide();if(BGIMG){sl.background={data:BGIMG};sl.addShape(pp.ShapeType.rect,{x:0,y:0,w:13.33,h:7.5,fill:{color:'0E0B13',transparency:18}})}else sl.background={color:DARK};if(LIGHT)sl.addShape(pp.ShapeType.rect,{x:0,y:0,w:13.33,h:7.5,fill:{color:PINK,transparency:93}});sl.addShape(pp.ShapeType.rect,{x:0,y:0,w:.18,h:7.5,fill:{color:PINK}});
    sl.addText(s.title||'',{x:.6,y:.4,w:12,h:.9,fontFace:FONT,fontSize:28,bold:true,color:PINK});
    let sImg=null,siw=0,sih=0;if(!(s.image&&img)&&s.img){try{const r=await imgForDoc(s.img.src,1400);if(r){sImg=r.c.toDataURL('image/jpeg',.88);siw=r.c.width;sih=r.c.height}}catch(e){}}
    const hasImg=(s.image&&img)||sImg;const bw=hasImg?7:12;
    sl.addText((s.bullets||[]).map(b=>({text:b,options:{bullet:{code:'25CF'},paraSpaceAfter:10}})),{x:.7,y:1.5,w:bw,h:5.2,fontFace:FONT,fontSize:20,color:(LIGHT&&!BGIMG)?TXT:'F3EEF7',valign:'top'});
    if(hasImg){const D=(s.image&&img)?img:sImg,IW=(s.image&&img)?iw:siw,IH=(s.image&&img)?ih:sih;const maxW=4.9,maxH=4.4;let w=maxW,hh=w*IH/IW;if(hh>maxH){hh=maxH;w=hh*IW/IH}sl.addImage({data:D,x:8+(maxW-w)/2,y:1.6,w,h:hh});if(sImg&&D===sImg&&s.img.credit)sl.addText('Image: '+s.img.credit,{x:8,y:1.65+hh,w:4.9,h:.35,fontFace:FONT,fontSize:9,color:'9A90A6',align:'center'})}
    sl.addText('dorapdf.com',{x:11.2,y:7,w:2,h:.35,fontFace:FONT,fontSize:10,color:'9A90A6',align:'right'});if(s.notes)sl.addNotes(s.notes)}
  if(img&&!(d.slides||[]).some(s=>s.image)){const sl=pp.addSlide();sl.background={color:LIGHT?'FFFFFF':'0E0B13'};sl.addText('Figure',{x:.6,y:.4,w:12,h:.9,fontFace:FONT,fontSize:28,bold:true,color:PINK});let w=11,hh=w*ih/iw;if(hh>5.6){hh=5.6;w=hh*iw/ih}sl.addImage({data:img,x:(13.33-w)/2,y:1.5,w,h:hh})}
  return pp.write({outputType:'blob'})}

async function generate(){const topic=$q('#gTopic').value.trim();if(!topic){toast('⚠️ Enter a topic');return}
  if(!TOKEN){pending=generate;return loginModal()}
  const wantDrive=!!($q('#gDrive')&&$q('#gDrive').checked);if(wantDrive&&!(driveTok&&Date.now()<driveExp)){driveAuth().catch(e=>toast('⚠️ '+e.message+'. You can still download the file.'))}
  const btn=$q('#genBtn');btn.disabled=true;btn.textContent=MODE==='assignment'?'Writing your assignment…':'Designing your slides…';$q('#pay').classList.remove('on');
  $q('#paper').style.display='none';$q('#outEmpty').style.display='grid';$q('#outEmpty').innerHTML='<div><div class="thinking"><i></i><i></i><i></i></div><p id="genStat">Researching the topic…</p></div>';
  const stats=MODE==='assignment'?['Researching the topic…','Building the outline…','Writing sections…','Formatting references…']:['Researching the topic…','Planning the slides…','Writing bullet points…','Adding speaker notes…'];let si=0;const st=setInterval(()=>{si=(si+1)%stats.length;const el=document.getElementById('genStat');if(el)el.textContent=stats[si]},3000);
  const body={topic,subject:$q('#gSubject').value,level:$q('#gLevel').value,cite:$q('#gCite').value,language:$q('#gLang').value,extra:$q('#gExtra').value,length:+$q('#gLen').value,slides:+$q('#gSlides').value,hasImage:!!refFile,autoImages:!!($q('#gAutoImg')&&$q('#gAutoImg').checked)};
  try{const j=await call(MODE==='assignment'?'/ai/assignment':'/ai/slides',{method:'POST',body:JSON.stringify(body)});
    if(MODE==='assignment'){lastSlides=null;lastDoc=j.doc;renderDoc(j.doc)}else{lastDoc=null;lastSlides=j.doc;renderSlides(j.doc)}
    if(typeof sDone==='function')sDone();toast((MODE==='assignment'?'Assignment':'Presentation')+' ready ✦');const db=$q('#driveBtn');if(db){db.disabled=false;db.textContent='Save to Drive';db.onclick=()=>saveToDrive(false)}
    if(wantDrive){for(let i=0;i<60&&!(driveTok&&Date.now()<driveExp);i++)await new Promise(r=>setTimeout(r,500));if(driveTok)saveToDrive(true)}}
  catch(e){if(e.code==='login'){pending=generate;loginModal()}else if(e.code==='upgrade'){$q('#payMsg').textContent=e.message;$q('#pay').classList.add('on');$q('#outEmpty').innerHTML='<div><div style="font-size:36px">🔒</div><p style="margin-top:8px">'+esc(e.message)+'</p></div>'}
    else $q('#outEmpty').innerHTML='<div><div style="font-size:36px">⚠️</div><p style="margin-top:8px">'+esc(e.message)+'</p></div>'}
  clearInterval(st);btn.disabled=false;btn.textContent='✦ Generate again'}

const form=$q('#genForm');if(form)form.addEventListener('submit',e=>{e.preventDefault();generate()});
const dBtn=$q('#docxBtn');if(dBtn){const orig=dBtn.onclick;realDocx=orig;dBtn.onclick=async()=>{if(MODE==='slides'||lastSlides&&!lastDoc){if(!lastSlides)return;dBtn.disabled=true;try{const b=await buildPptx(lastSlides);saveFile((lastSlides.title||'presentation').replace(/[^\w\- ]+/g,'').slice(0,60).trim()+'.pptx',b)}catch(e){toast('⚠️ Could not build the PowerPoint')}dBtn.disabled=false;return}return orig&&orig()}}
const cBtn=$q('#copyBtn');if(cBtn){const o2=cBtn.onclick;cBtn.onclick=async()=>{if(lastSlides&&!lastDoc){const t=[lastSlides.title,'',...(lastSlides.slides||[]).map(s=>s.title+'\n'+(s.bullets||[]).map(b=>'• '+b).join('\n'))].join('\n\n');try{await navigator.clipboard.writeText(t);toast('Copied ✓')}catch(e){}return}return o2&&o2()}}

document.getElementById('acctBtn')&&document.getElementById('acctBtn').addEventListener('click',()=>USER?accountModal():loginModal());
document.querySelectorAll('.plan-btn').forEach(b=>b.addEventListener('click',()=>{const p=b.dataset.plan;if(p==='trial'){if(USER){location.hash='gen'}else{pending=()=>{location.hash='gen'};loginModal()}}else checkout(p)}));
if(form)setMode('assignment');
paint();
if(TOKEN){call('/me').catch(()=>{});config().then(c=>{if(c.googleClientId)loadScript('https://accounts.google.com/gsi/client').catch(()=>{})})}
if(document.querySelector('.pkr'))config();
window.DoraAccount={loginModal,accountModal,checkout};
})();
