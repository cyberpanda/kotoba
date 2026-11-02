import json,sys,time
from playwright.sync_api import sync_playwright
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL=sys.argv[1] if len(sys.argv)>1 else 'file://'+os.path.join(ROOT,'dist','standalone','kotoba.html')
SHOTS=os.path.join(ROOT,'dist','qa');os.makedirs(SHOTS,exist_ok=True)
VIEWS=['home','path','learn','read','build','play','kana','gram']
GAMES=['pics','challenge','runner','bonsai','breathe','rpg']
VPS={'phone':dict(viewport={'width':390,'height':844},device_scale_factor=3,is_mobile=True,has_touch=True),'tablet':dict(viewport={'width':820,'height':1180},is_mobile=True,has_touch=True),'desktop':dict(viewport={'width':1440,'height':900})}
CHK=r'''()=>{const out={};const W=innerWidth;out.hscroll=document.scrollingElement.scrollWidth>W+1?document.scrollingElement.scrollWidth:0;
const vis=e=>{const r=e.getBoundingClientRect();const cs=getComputedStyle(e);return r.width>0&&r.height>0&&cs.visibility!=="hidden"&&cs.display!=="none"&&+cs.opacity>0.05};
const name=e=>(e.getAttribute("aria-label")||e.title||e.textContent||"").trim()||(e.querySelector("img[alt]")&&e.querySelector("img").alt);
const btns=[...document.querySelectorAll("button,a[href],[role=button],input,select")].filter(e=>vis(e)&&!e.closest("#ksp"));
out.noname=btns.filter(e=>!name(e)&&e.type!=="range"&&e.type!=="checkbox"&&e.tagName!=="SELECT").map(e=>e.outerHTML.slice(0,90)).slice(0,8);
out.small=btns.filter(e=>{const r=e.getBoundingClientRect();return(r.width<28||r.height<28)&&e.type!=="checkbox"&&e.type!=="range"}).map(e=>(e.id||e.className||e.tagName)+":"+Math.round(e.getBoundingClientRect().width)+"x"+Math.round(e.getBoundingClientRect().height)).slice(0,12);
out.offscreen=[...document.querySelectorAll("#main *")].filter(e=>{const r=e.getBoundingClientRect();return vis(e)&&r.right>W+2&&r.width<W&&!e.closest("[style*=overflow],.hs,.scroller")&&getComputedStyle(e.parentElement).overflowX==="visible"}).map(e=>(e.className||e.tagName)+"@"+Math.round(e.getBoundingClientRect().right)).slice(0,6);
const lum=c=>{const m=c.match(/[\d.]+/g);if(!m)return null;const [r,g,b]=m.slice(0,3).map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return{L:.2126*r+.7152*g+.0722*b,a:m[3]===undefined?1:+m[3]}};
const bgOf=e=>{for(;e;e=e.parentElement){const c=getComputedStyle(e).backgroundColor;const l=lum(c);if(l&&l.a>.9)return l.L;if(getComputedStyle(e).backgroundImage!=="none")return null}return lum(getComputedStyle(document.body).backgroundColor).L};
const low=[];document.querySelectorAll("#main *,header *,nav *").forEach(e=>{if(!vis(e)||![...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim().length>1))return;const cs=getComputedStyle(e);if(cs.backgroundClip==="text"||cs.webkitTextFillColor==="transparent"||cs.color.includes("0, 0, 0, 0"))return;const f=lum(cs.color),b=bgOf(e);if(!f||b==null)return;const r=(Math.max(f.L,b)+.05)/(Math.min(f.L,b)+.05);const big=parseFloat(cs.fontSize)>=18.6||(parseFloat(cs.fontSize)>=14&&+cs.fontWeight>=700);if(r<(big?3:4.5)&&f.a>.9)low.push(e.tagName+"."+(e.className+"").slice(0,20)+" '"+e.textContent.trim().slice(0,18)+"' "+r.toFixed(2))});out.contrast=low.slice(0,10);out.ncontrast=low.length;
out.imgnoalt=[...document.querySelectorAll("img")].filter(i=>!i.hasAttribute("alt")).length;
return out}'''
res={'errors':{},'views':{},'games':{},'flow':{},'perf':{}}
with sync_playwright() as p:
  b=p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
  for vpn,vp in VPS.items():
    for th in ['dark','light']:
      ctx=b.new_context(**vp);pg=ctx.new_page();er=[]
      pg.on('pageerror',lambda e:er.append('PE '+str(e)[:160]))
      pg.on('console',lambda m:m.type=='error' and er.append('CE '+m.text[:160]))
      pg.add_init_script("localStorage.setItem('nj_welcome','1');localStorage.setItem('nj_tour','1');localStorage.setItem('nj_cfg',JSON.stringify({theme:'%s',thU:1,th2:1,th3:1,lang:'de'}))"%th)
      t0=time.time();pg.goto(URL);pg.wait_for_timeout(3200);res['perf'][vpn+th]=round(time.time()-t0,2)
      for v in VIEWS:
        try:pg.evaluate(f"go('{v}')");pg.wait_for_timeout(700);res['views'][f'{vpn}/{th}/{v}']=pg.evaluate(CHK);pg.screenshot(path=SHOTS+f'/{vpn}_{th}_{v}.png',full_page=False)
        except Exception as e:res['views'][f'{vpn}/{th}/{v}']={'ex':str(e)[:150]}
      if th=='dark':
        for g in GAMES:
          try:pg.evaluate(f"go('home');{g}()");pg.wait_for_timeout(1500);res['games'][f'{vpn}/{g}']=pg.evaluate(CHK);pg.screenshot(path=SHOTS+f'/{vpn}_g_{g}.png')
          except Exception as e:res['games'][f'{vpn}/{g}']={'ex':str(e)[:150]}
        try:pg.evaluate("go('home')");pg.click('#tMusic');pg.wait_for_timeout(500);res['views'][f'{vpn}/menu']=pg.evaluate(CHK);pg.screenshot(path=SHOTS+f'/{vpn}_menu.png');pg.click('#mpx')
        except Exception as e:res['views'][f'{vpn}/menu']={'ex':str(e)[:150]}
        try:
          pg.evaluate("go('home')");pg.wait_for_timeout(300);pg.click('#go');pg.wait_for_timeout(800);pg.screenshot(path=SHOTS+f'/{vpn}_session.png');res['views'][f'{vpn}/session']=pg.evaluate(CHK)
        except Exception as e:res['views'][f'{vpn}/session']={'ex':str(e)[:150]}
      res['errors'][vpn+th]=list(dict.fromkeys(er))[:12];ctx.close()
  ctx=b.new_context(**VPS['phone']);pg=ctx.new_page();er=[];pg.on('pageerror',lambda e:er.append(str(e)[:150]))
  pg.goto(URL);pg.wait_for_timeout(2900);pg.click('#kgo');pg.wait_for_timeout(3600);pg.click('#kgo');pg.wait_for_timeout(900)
  res['flow']['welcome_open']=pg.evaluate("!!document.querySelector('#wdlg:not([hidden])')");pg.screenshot(path=SHOTS+'/flow_welcome.png')
  btn=pg.query_selector('#wdlg button:has-text("ohne"),#wdlg button:has-text("without")')
  res['flow']['skipbtn']=bool(btn)
  if btn:btn.click();pg.wait_for_timeout(900)
  res['flow']['tour']=pg.evaluate("!!document.getElementById('ktour')");pg.screenshot(path=SHOTS+'/flow_tour.png')
  n=0
  while pg.query_selector('#ktour .ktnx') and n<20:pg.click('#ktour .ktnx');pg.wait_for_timeout(500);n+=1
  res['flow']['tour_steps']=n;res['flow']['errs']=er
  b.close()
json.dump(res,open(SHOTS+'/res.json','w'),indent=1,ensure_ascii=False)
bad=[k for k,v in res['errors'].items() if v]+[k for k,v in {**res['views'],**res['games']}.items() if 'ex' in v or v.get('hscroll')]+([] if res['flow'].get('tour_steps',0)>0 and not res['flow'].get('errs') else ['flow'])
print('QA', 'FAILED: '+', '.join(bad) if bad else 'passed', '– report:', SHOTS+'/res.json')
sys.exit(1 if bad else 0)
