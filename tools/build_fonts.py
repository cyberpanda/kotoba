"""Re-subset the bundled fonts to the characters used in src/index.html.
Needs: pip install fonttools; Noto Sans/Serif CJK (fonts-noto-cjk) and DejaVu Sans Mono installed.
Run after adding new kanji/kana to the source: python3 tools/build_fonts.py"""
import re,base64,io,subprocess,os,sys
from fontTools.ttLib import TTCollection,TTFont
from fontTools import subset
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC=open(os.path.join(ROOT,'src','index.html'),encoding='utf-8').read()
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
D=os.path.join(ROOT,'src','fonts')+os.sep
build(pick('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc','Noto Sans CJK JP'),"Kotoba Sans","Regular",D+'KotobaSans-Regular.woff')
build(pick('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc','Noto Sans CJK JP'),"Kotoba Sans","Bold",D+'KotobaSans-Bold.woff')
build(pick('/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc','Noto Serif CJK JP'),"Kotoba Serif","Bold",D+'KotobaSerif-Bold.woff')
build(TTFont('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'),"Kotoba Mono","Regular",D+'KotobaMono-Regular.woff')
print('fonts written to',D)
