import re,base64,io,subprocess,os,sys
from fontTools.ttLib import TTCollection,TTFont
from fontTools import subset
SRC=open('/home/claude/src.html').read()
chars=set(SRC)|set(chr(c) for c in range(0x20,0x7f))|set(chr(c) for c in range(0xa0,0x100))|set(chr(c) for c in range(0x3040,0x30ff))|set("ōūāīēŌŪĀĪĒ’‘“”–—…・「」『』、。！？〜ー※　")
text=''.join(sorted(c for c in chars if ord(c)>=0x20))
def pick(ttc,name):
    for f in TTCollection(ttc).fonts:
        if name in f['name'].getDebugName(1)+' '+(f['name'].getDebugName(4) or ''):return f
def build(font,fam,style,out):
    opts=subset.Options();opts.flavor='woff';opts.layout_features=['*'];opts.name_IDs=['*'];opts.notdef_outline=True;opts.desubroutinize=True
    ss=subset.Subsetter(opts);ss.populate(text=text);ss.subset(font)
    nm=font['name']
    for r in nm.names:
        if r.nameID in (1,16):r.string=fam
        elif r.nameID==4:r.string=f"{fam} {style}"
        elif r.nameID==6:r.string=(fam+"-"+style).replace(" ","")
    font.flavor='woff';font.save(out)
D='/home/claude/kotoba/fonts/'
build(pick('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc','Noto Sans CJK JP'),"Kotoba Sans","Regular",D+'KotobaSans-Regular.woff')
build(pick('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc','Noto Sans CJK JP'),"Kotoba Sans","Bold",D+'KotobaSans-Bold.woff')
build(pick('/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc','Noto Serif CJK JP'),"Kotoba Serif","Bold",D+'KotobaSerif-Bold.woff')
build(TTFont('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'),"Kotoba Mono","Regular",D+'KotobaMono-Regular.woff')
FF=[("Kotoba Sans",400,"KotobaSans-Regular.woff"),("Kotoba Sans",700,"KotobaSans-Bold.woff"),("Kotoba Serif",700,"KotobaSerif-Bold.woff"),("Kotoba Mono",400,"KotobaMono-Regular.woff")]
def css(inline):
    o=""
    for fam,w,f in FF:
        u=("data:font/woff;base64,"+base64.b64encode(open(D+f,'rb').read()).decode()) if inline else "fonts/"+f
        o+=f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:normal;font-display:swap;src:url("{u}") format("woff")}}'
        if w==700 and fam=="Kotoba Sans":o+=f'@font-face{{font-family:"{fam}";font-weight:600 900;font-style:normal;font-display:swap;src:url("{u}") format("woff")}}'
    if inline: pass
    return o
pub=SRC.replace('/*FONTS*/',css(True))
open('/home/claude/nihongo.html','w').write(pub)
body=SRC.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
h=open('/home/claude/kotoba/index.html').read();head=h[:h.index('<title>')]
head=re.sub(r'<link rel="preload"[^\n]*\n','',head)
pre=''.join(f'<link rel="preload" href="fonts/{f}" as="font" type="font/woff" crossorigin>\n' for _,_,f in FF[:1])
idx=head+pre+body.replace('/*FONTS*/',css(False)).replace('<div class="wrap" id="app">','</head>\n<body>\n<div class="wrap" id="app">',1).replace('</script>','</script>\n<script>if("serviceWorker"in navigator)addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}))</script>',1)+'\n</body>\n</html>\n'
open('/home/claude/kotoba/index.html','w').write(idx)
sa=head+body.replace('/*FONTS*/',css(True)).replace('<div class="wrap" id="app">','</head>\n<body>\n<div class="wrap" id="app">',1)+'\n</body>\n</html>\n'
sa='\n'.join(l for l in sa.split('\n') if 'icon.svg' not in l and 'manifest.webmanifest' not in l and 'serviceWorker' not in l)
pwa='<link rel="manifest" href="kotoba.webmanifest">\n<link rel="apple-touch-icon" href="kotoba-icon-180.png">\n'
sa=sa.replace('</head>',pwa+'</head>',1).replace('\n</body>','\n<script>if("serviceWorker"in navigator&&location.protocol.startsWith("http"))addEventListener("load",()=>navigator.serviceWorker.register("kotoba-sw.js",{scope:"./kotoba"}).catch(()=>{}))</script>\n</body>',1)
open('/home/claude/kotoba/site/kotoba.html','w').write(sa)
open('/home/claude/kotoba-standalone.html','w').write(sa)
for f in os.listdir(D):print(f,os.path.getsize(D+f)//1024,'KB')
print('standalone',len(sa)//1024,'KB')
