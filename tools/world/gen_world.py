import json
def G(w,h,fill='.',border='P'):
    g=[[fill]*w for _ in range(h)]
    if border:
        for x in range(w): g[0][x]=border; g[h-1][x]=border
        for y in range(h): g[y][0]=border; g[y][w-1]=border
    return g
def H(g,y,x0,x1,c='='):
    for x in range(x0,x1+1): g[y][x]=c
def V(g,x,y0,y1,c='='):
    for y in range(y0,y1+1): g[y][x]=c
def Rc(g,x0,y0,x1,y1,c):
    for y in range(y0,y1+1):
        for x in range(x0,x1+1): g[y][x]=c
def Pt(g,pts,c):
    for x,y in pts: g[y][x]=c
def S(g): return [''.join(r) for r in g]
def station_top(g,back,fwd,sb,sf):
    w=len(g[0])
    H(g,0,0,w-1,'R');H(g,1,0,w-1,'V');H(g,2,0,w-1,'l');H(g,3,0,w-1,'l')
    if back is not None: g[1][back]='Y'; g[2][back-1]=sb
    if fwd is not None: g[1][fwd]='Y'; g[2][fwd+1]=sf
A=[]
def add(**k): A.append(k)
def rail(g,y,cross=()):
    W=len(g[0]);H_=len(g)
    for x in range(W):
        g[y][x]='Z' if (g[y][x] in '=qr' or x in cross) else 'R'
    if y+1==H_-1 and all(c=='P' for c in g[y+1]): g[y+1]=['.']*W
    zs=[x for x in range(W) if g[y][x]=='Z']
    for x in zs:
        for nx in (x-1,x+1):
            if 0<nx<W-1 and g[y][nx]=='R':
                g[y][nx]='Z'
                for ny in (y-1,y+1):
                    if 0<=ny<H_ and g[ny][nx] in '.,TPJ' and g[ny][x] in '=qkX': g[ny][nx]=g[ny][x] if g[ny][x] in '=qk' else '='

# ---------- Kapitel 1: ふるさと ----------
g=G(24,16)
H(g,12,2,22);g[12][23]='X';V(g,13,5,12);H(g,5,4,13);V(g,4,5,6);V(g,7,10,12);V(g,18,5,12);H(g,5,18,20)
Rc(g,15,7,20,10,'~');Rc(g,16,6,19,6,'~');Rc(g,2,13,6,14,',');Rc(g,9,1,12,2,',')
Pt(g,[(2,2),(21,2),(2,8),(9,9),(21,13),(11,14),(1,10),(22,8),(14,2),(6,8)],'T')
rail(g,14);add(id='mura',rail=[14],ch=0,s='spring',n=['村','Mura','Heimat · Das Dorf','Home · The village'],m=S(g),
 o=[['minka',3,3,{'door':1,'nc':'#2a5fc9'}],['minka',15,2,{'th':1}],['machiya',6,8,{'sign':'おみせ','nc':'#2f9e4f'}],['torii',12,13]],
 npc=[['oba',9,6],['kid',5,11],['shop',7,10],['guard',22,11]],it=[['hana',10,1,'flower']],
 ex=[[23,12,'machi',1,8,['oba','kid','shop']],[4,4,'ie',5,7,[]]],start=[7,12])
g=G(12,9,'f','W');Rc(g,2,3,9,5,'t');Rc(g,4,4,7,4,'b');Pt(g,[(1,1),(2,1),(9,1),(10,1)],'j');g[8][5]='D'
add(id='ie',ch=0,s='in',n=['家','Ie','Heimat · Opas Haus','Home · Grandpa’s house'],m=S(g),npc=[['ojii',3,4]],ex=[[5,8,'mura',4,5,[]]])
g=G(24,16)
H(g,8,1,22);g[8][0]='X';V(g,12,1,14);g[0][12]='X';H(g,4,14,21);V(g,18,4,8);V(g,4,5,8);H(g,12,2,10);V(g,6,8,12);H(g,13,13,21);V(g,20,8,13)
Pt(g,[(1,13),(10,14),(22,6),(22,14),(9,2),(15,10),(1,4)],'T');Rc(g,8,10,10,11,',')
rail(g,1);add(id='machi',rail=[1],ch=0,s='spring',n=['町','Machi','Heimat · Die Stadt','Home · The town'],m=S(g),
 o=[['school',2,2],['station',16,2,{'door':1}],['minka',2,9],['minka',7,9,{}],['machiya',15,10,{'sign':'ねこカフェ','nc':'#e98fb0'}]],
 npc=[['sensei',5,6],['eki',15,5],['nekolady',14,13],['guard2',13,2]],it=[['neko',22,12,'cat']],
 ex=[[0,8,'mura',22,12,[]],[12,0,'yama',9,12,['eki','nekolady','sensei']],[18,3,'eki',7,10,[]]])
g=G(18,14,'.','M');V(g,9,4,12,'q');g[13][9]='X';Rc(g,2,9,4,10,'~');Rc(g,13,9,15,10,'~');Pt(g,[(7,4),(11,4),(7,8),(11,8)],'s');Pt(g,[(2,3),(15,3),(3,6),(14,6)],'T');Pt(g,[(1,12),(16,12),(2,1),(15,1)],'P')
add(id='yama',ch=0,s='spring',n=['山','Yama','Heimat · Bergschrein','Home · Mountain shrine'],m=S(g),o=[['shrine',7,1],['torii',8,6]],
 npc=[['monk',5,7],['fox',13,7],['shrine',10,4]],ex=[[9,13,'machi',12,1,[]]])
g=G(16,12,'k',None);H(g,0,0,15,'F');H(g,1,0,15,'R');H(g,2,0,15,'V');g[2][7]='Y';H(g,3,0,15,'l');H(g,4,0,15,'l');g[3][8]='2';H(g,5,0,15,'F');g[5][6]='I';g[5][7]='l';g[5][8]='I';H(g,11,0,15,'F');g[11][7]='X';Pt(g,[(2,7),(3,7)],'b');Pt(g,[(12,7),(13,7)],'v')
add(id='eki',ch=0,s='spring',city=1,n=['駅','Eki','Heimat · Bahnhof','Home · Station'],m=S(g),npc=[['kaisatsu',5,6]],
 ex=[[7,11,'machi',18,4,[]],[7,2,'tokyoin',4,2,['kaisatsu']]])

# ---------- Kapitel 2: 東京 ----------
g=G(24,14,'k',None);H(g,1,0,23,'R');H(g,2,0,6,'R');H(g,2,17,23,'R');H(g,0,0,23,'W');g[7][0]='X';g[7][23]='X';H(g,13,0,23,'k');g[13][3]='X';Rc(g,11,9,13,10,'~');Pt(g,[(9,6),(14,6),(11,12),(12,12)],'b');Pt(g,[(2,5),(21,5),(6,4),(17,4)],'v');Pt(g,[(5,9),(16,9),(1,12),(22,12),(1,4),(22,4),(10,11),(14,11),(16,12)],'T');Pt(g,[(10,4),(13,4),(3,9),(20,7),(11,8),(14,8)],'s');Pt(g,[(21,11)],'U')
add(id='tokyo',ch=1,s='spring',city=1,n=['丸の内','Marunouchi','Tokio · Bahnhofsvorplatz','Tokyo · Station plaza'],rail=[1],m=S(g),o=[['tokyoeki',7,1,{'door':1}],['kanban',21,12,{'t':'タクシー'}],['kanban',1,10,{'t':'バス'}]],
 npc=[],ex=[[8,2,'tokyoin',12,10,[]],[12,2,'tokyoin',12,10,[]],[15,2,'tokyoin',12,10,[]],[0,7,'shibuya',22,4,['annai']],[23,7,'asakusa',1,12,['annai']],[3,13,'akiba',11,1,['annai']]])
g=G(24,20,'k',None);Rc(g,0,6,23,9,'a');Rc(g,10,0,13,5,'a');Rc(g,10,10,13,19,'a');g[0][8]='X';g[4][23]='X';g[19][20]='X';Pt(g,[(17,11),(1,15),(6,15)],'T');rail(g,17,cross=(10,11,12,13))
add(id='shibuya',rail=[17],via=[15,19,1.3],under=[[19,17],[20,17],[21,17]],ch=1,s='spring',city=1,n=['渋谷','Shibuya','Tokio · Shibuya-Kreuzung','Tokyo · Shibuya Crossing'],m=S(g),
 o=[['scramble',6,3],['sky',0,1,{'hg':60}],['screen',2,1],['neonb',5,2,{'sign':'カラオケ','k':0}],['screen',14,1],['neonb',17,2,{'sign':'ゲーム','k':1}],['round',19,1],['sky',22,1,{'hg':70}],['shibueki',1,12],['metro',21,12],['dsign',23,15,{'t':'東京タワー','d':1,'sm':1}],['neonb',16,15,{'sign':'カフェ','k':2,'hg':18}]],
 npc=[['hachiko',7,15],['mika',17,12]],ex=[[23,4,'tokyo',1,7,[]],[8,0,'shinjuku',11,12,[]],[20,19,'tower',10,1,[]]])
g=G(24,14,'k',None);Rc(g,0,7,23,8,'a');H(g,13,0,23,'F');g[13][11]='X';g[12][11]='k';Pt(g,[(2,10),(21,10),(8,10),(15,10)],'T');Pt(g,[(6,11),(17,11)],'v')
add(id='shinjuku',ch=1,s='spring',city=1,n=['新宿','Shinjuku','Tokio · Hochhäuser','Tokyo · Skyscrapers'],m=S(g),
 o=[['zebra',10,7],['sky',0,2,{'hg':90}],['sky',2,2,{'hg':110,'c':'#556688'}],['ramen',5,4],['metro',19,9],['tocho',8,2],['kanban',4,9,{'t':'交番'}],['kanban',17,9,{'t':'駐車場'}],['neonb',13,4,{'sign':'ほんや','k':2}],['sky',15,2,{'hg':120}],['sky',17,2,{'hg':95,'c':'#556688'}],['neonb',19,4,{'sign':'くすり','k':3}],['sky',21,2,{'hg':85}],['sky',0,11,{'hg':40}],['sky',22,11,{'hg':40}]],
 npc=[['salary',14,9]],ex=[[11,13,'shibuya',8,1,[]],[6,5,'ramen',5,7,[]]])
g=G(12,9,'f','W');H(g,2,2,9,'j');H(g,4,2,8,'b');Pt(g,[(3,6),(4,6),(7,6),(8,6)],'b');g[8][5]='D'
add(id='ramen',ch=1,s='in',n=['ラーメン屋','Rāmen-ya','Tokio · Ramen-Laden','Tokyo · Ramen shop'],m=S(g),npc=[['ramen',6,3]],ex=[[5,8,'shinjuku',6,6,[]]])
g=G(24,16);V(g,11,4,14);V(g,12,4,14);H(g,12,0,11);g[12][0]='X';Pt(g,[(9,7),(9,9),(14,7),(14,9),(8,7),(8,9),(15,7),(15,9)],'y');Pt(g,[(10,4),(13,4)],'s');Pt(g,[(2,3),(4,6),(20,8),(22,4),(3,14),(20,14),(6,10),(17,12)],'T')
add(id='asakusa',ch=1,s='spring',n=['浅草','Asakusa','Tokio · Tempelviertel','Tokyo · Temple district'],m=S(g),
 o=[['temple',8,1],['pagoda',17,2],['kaminari',10,11],['metro',2,10],['skytree',20,1],['kanban',4,4,{'t':'せんべい'}],['kanban',16,5,{'t':'人力車'}]],npc=[['kimono',7,8],['omikuji',14,5]],ex=[[0,12,'tokyo',22,7,[]]])
g=G(24,14,'k',None);Rc(g,0,7,23,8,'a');g[0][11]='X';g[7][23]='X';Pt(g,[(4,10),(19,10)],'v')
rail(g,13);add(id='akiba',rail=[13],ch=1,s='spring',city=1,n=['秋葉原','Akihabara','Tokio · Elektronikviertel','Tokyo · Electric Town'],m=S(g),
 o=[['neonb',0,0,{'sign':'ゲーム','k':0,'hg':50}],['animeb',2,0],['konbini',5,2],['metro',9,9],['neonb',13,0,{'sign':'でんき','k':2,'hg':70}],['neonb',15,0,{'sign':'カメラ','k':3,'hg':55}],['neonb',17,0,{'sign':'パソコン','k':0,'hg':65}],['neonb',19,0,{'sign':'まんが','k':1,'hg':45}],['neonb',21,0,{'sign':'カフェ','k':2,'hg':50}],['neonb',0,12,{'sign':'おもちゃ','k':3}],['neonb',2,12,{'k':1}],['neonb',6,11,{'sign':'ゲーム','k':0}],['animeb',14,11],['kanban',8,4,{'t':'免税'}],['neonb',16,11,{'sign':'レトロ','k':3}],['neonb',20,11,{'k':0}]],
 npc=[['otaku',16,5]],ex=[[11,0,'tokyo',3,12,[]],[6,3,'konbini',5,7,[]],[23,7,'ueno',1,8,[]]])
g=G(12,9,'c','W');H(g,1,1,10,'j');Pt(g,[(3,3),(3,4),(6,3),(6,4)],'j');Pt(g,[(9,3),(9,4)],'v');H(g,6,1,3,'b');g[8][5]='D'
add(id='konbini',ch=1,s='in',n=['コンビニ','Konbini','Tokio · Konbini','Tokyo · Convenience store'],m=S(g),npc=[['konbini',2,7]],it=[['sumaho',8,5,'phone']],ex=[[5,8,'akiba',6,4,[]]])
g=G(24,16);H(g,8,0,22);g[8][0]='X';V(g,12,4,14);Rc(g,15,10,20,13,'~');Rc(g,3,10,7,13,'F');Rc(g,4,11,6,12,'.');H(g,13,12,14)
for p in [(2,3),(4,3),(19,3),(21,3),(2,6),(21,6),(9,12),(14,6),(10,6),(22,11),(1,14),(22,14)]: g[p[1]][p[0]]='T'
rail(g,14);add(id='ueno',rail=[14],ch=1,s='spring',n=['上野','Ueno','Tokio · Ueno-Park','Tokyo · Ueno Park'],m=S(g),o=[['museum',9,1],['metro',19,5]],
 npc=[['ueno',8,11],['panda',5,11]],ex=[[0,8,'akiba',22,7,[]]])
g=G(20,16);V(g,10,1,13);g[0][10]='X';H(g,13,2,18);Rc(g,5,7,14,12,'k');Pt(g,[(5,7),(14,7),(5,12),(14,12)],',');Pt(g,[(6,12),(13,12)],'b');Pt(g,[(4,8),(15,8)],'s');Pt(g,[(3,3),(16,3),(2,6),(17,6),(6,4),(13,4),(2,10),(17,10),(4,14),(15,14)],'T');g[13][19]='X'
add(id='tower',ch=1,s='spring',n=['東京タワー','Tōkyō Tawā','Tokio · Tokyo Tower','Tokyo · Tokyo Tower'],m=S(g),o=[['ttower',8,10],['metro',2,14]],
 npc=[['tower',12,12]],ex=[[10,0,'shibuya',20,18,[]],[19,13,'odaiba',1,4,[]]])

# ---------- Kapitel 3: 夏の海 ----------
g=G(24,14,'.',None);station_top(g,4,19,'2','4');H(g,4,0,23,'=');Rc(g,0,5,23,6,'.');Rc(g,0,7,23,9,'n');Rc(g,0,10,23,13,'~');g[5][0]='X';g[5][23]='X';V(g,0,4,6,'=');V(g,23,4,6,'=');g[4][0]='=';g[4][23]='='
Pt(g,[(2,7),(9,7),(15,7),(22,7)],'p');Pt(g,[(6,8),(18,8)],'U');Pt(g,[(3,5),(12,5),(20,5)],'T')
g[5][0]='X';g[5][23]='X'
add(id='umi',ch=2,s='summer',n=['海','Umi','Sommer · Am Meer','Summer · The beach'],m=S(g),o=[['lighthouse',21,9],['machiya',8,4,{'sign':'かき氷','nc':'#7fb8d9'}]] if False else [['lighthouse',21,9]],
 npc=[['ryoshi',16,8],['suika',5,8]],ex=[[4,1,'tokyoin',19,2,[]],[19,1,'kyoto',4,2,['matsuri']],[23,5,'matsuri',1,10,[]],[0,5,'miyajima',22,6,[]]])
g=G(20,14);V(g,9,4,12,'q');V(g,10,4,12,'q');H(g,10,0,9,'q');g[10][0]='X';Pt(g,[(5,6),(5,8),(14,6),(14,8),(4,6),(4,8),(15,6),(15,8)],'y');Pt(g,[(7,4),(12,4),(7,11),(12,11)],'s');Pt(g,[(2,3),(17,3),(2,12),(17,12)],'T')
add(id='matsuri',ch=2,s='summer',night=1,fw=1,n=['夏祭り','Natsu-matsuri','Sommer · Sommerfest','Summer · Summer festival'],m=S(g),o=[['shrine',7,0],['torii',8,7],['yagura',15,10]],
 npc=[['yatai',6,7],['matsuri',11,4]],ex=[[0,10,'umi',22,5,[]]])
g=G(24,14,'.',None);Rc(g,0,0,23,1,'P');Rc(g,0,2,23,6,'.');Rc(g,0,7,23,8,'n');Rc(g,0,9,23,13,'~');H(g,6,1,23,'q');g[6][23]='X';V(g,6,9,12,'r');H(g,12,6,13,'r');V(g,6,7,8,'q');Pt(g,[(3,3),(9,3),(15,3),(20,3),(2,5)],'T')
add(id='miyajima',ch=2,s='summer',n=['宮島','Miyajima','Sommer · Insel Miyajima','Summer · Miyajima island'],m=S(g),o=[['shrine',9,2],['ftorii',14,11]],
 npc=[['itsuku',12,7],['deer1',4,4],['deer2',18,5]],ex=[[23,6,'umi',1,5,[]]])

# ---------- Kapitel 4: 古都 ----------
g=G(24,16,'.',None);station_top(g,4,19,'3','5');Rc(g,0,4,23,15,'.');H(g,4,0,23,'q');V(g,11,4,15,'q');g[15][11]='X';H(g,10,11,22,'q');g[10][23]='X';Rc(g,2,8,8,12,'~');V(g,4,13,15,'.')
Pt(g,[(1,6),(9,6),(14,6),(21,6),(1,14),(20,14),(15,14),(9,14),(22,8)],'T');Pt(g,[(13,8),(17,8)],'s');H(g,13,12,19,'q');V(g,19,13,15,'q');g[15][19]='X';g[4][0]='X'
add(id='kyoto',ch=3,s='autumn',n=['京都','Kyōto','Kyoto & Nara · Kyoto','Kyoto & Nara · Kyoto'],m=S(g),o=[['kinkaku',3,8],['ryokan',15,5,{'door':1}],['kanban',22,9,{'t':'三年坂'}],['kanban',20,15,{'t':'稲荷'}],['kanban',2,6,{'t':'嵐山'}],['kanban',12,14,{'t':'奈良'}]],
 npc=[['tera',13,9],['maiko',9,12]],it=[['momiji',17,12,'leaf']],ex=[[4,1,'umi',19,2,[]],[19,1,'osaka',4,2,['okami','daibutsu']],[16,6,'ryokan',5,7,[]],[23,10,'sannenzaka',1,15,[]],[19,15,'inari',1,22,[]],[11,15,'nara',11,1,[]],[0,4,'arashiyama',22,7,[]]])
g=G(24,14,'Q','P');Rc(g,1,6,22,8,'q');Rc(g,1,5,22,5,'F');Rc(g,1,9,22,9,'F');g[7][23]='X';g[6][23]='P';g[8][23]='P';Pt(g,[(4,6),(12,8),(19,6)],',');Pt(g,[(7,6),(16,8)],'s')
BB=[]
add(id='arashiyama',ch=3,s='autumn',n=['嵐山','Arashiyama','Kyoto & Nara · Bambuswald','Kyoto & Nara · Bamboo grove'],m=S(g),o=[['kanban',21,6,{'t':'竹林の小径'}]],
 npc=[],ex=[[23,7,'kyoto',1,4,[]]],
 sp=[[10,5,["{竹|たけ}が{風|かぜ}でさらさら{鳴|な}る。","take ga kaze de sarasara naru.","Der Bambus rauscht im Wind.","The bamboo rustles in the wind."],0],[15,9,["{竹|たけ}の{根元|ねもと}に５０{円|えん}！","take no nemoto ni gojū-en!","Am Bambusfuß: 50 Yen!","At the bamboo's foot: 50 yen!"],1]],
 fl=[["fl_arashi_0",9,6,"#555","#2b2b48",["{人力車|じんりきしゃ}で{竹林|ちくりん}をどうぞ！","jinrikisha de chikurin o dōzo!","Mit der Rikscha durch den Bambuswald!","Ride through the bamboo by rickshaw!"],"{車夫|しゃふ}","shafu"],["fl_arashi_1",14,8,"#1e1e24","#c8325a",["{着物|きもの}で{写真|しゃしん}を{撮|と}りたいな。","kimono de shashin o toritai na.","Ich will im Kimono Fotos machen.","I want photos in a kimono."],"{観光客|かんこうきゃく}","kankōkyaku"]])
g=G(24,18,'.','P');Pt(g,[(11,y) for y in range(4,18)]+[(12,y) for y in range(4,18)],'q');Pt(g,[(10,y) for y in range(9,14)]+[(13,y) for y in range(5,9)],'q');Rc(g,9,9,14,10,'q');H(g,15,0,10,'q');g[15][0]='X';Pt(g,[(9,8),(14,8),(9,12),(14,14)],'s');Pt(g,[(3,4),(20,3),(2,2),(21,12),(5,16),(18,16),(4,9),(19,8)],'T');Pt(g,[(16,11),(9,14),(17,16)],',');Rc(g,9,1,14,5,'P');Pt(g,[(10,6),(13,6)],'T')
KS=[('八ツ橋','#b5651d'),('抹茶','#4f7a3a'),('着物','#a8324a'),('扇子','#6b4f9a'),('清水焼','#2f6f9a'),('甘味','#c46a2a'),('湯豆腐','#7a6a4a'),('団子','#c0503a'),('かんざし','#b0446a'),('和傘','#9a2a2a')]
POS=[(2,3),(6,4),(17,3),(20,6),(5,9),(16,9),(6,12),(15,13),(1,12),(19,12)]
SO=[['machiya',x,y,{'sign':KS[i][0],'nc':KS[i][1]}] for i,(x,y) in enumerate(POS)]
add(id='sannenzaka',ch=3,s='autumn',n=['三年坂','Sannenzaka','Kyoto & Nara · Higashiyama','Kyoto & Nara · Higashiyama'],m=S(g),o=[['pagoda',11,7]]+SO,
 npc=[],ex=[[0,15,'kyoto',22,10,[]]],
 sp=[[9,7,["{八坂|やさか}の{塔|とう}：{高|たか}さ４６メートル。","Yasaka no tō: takasa yonjūroku mētoru.","Yasaka-Pagode: 46 Meter hoch.","Yasaka Pagoda: 46 metres tall."],0],[13,16,["{石畳|いしだたみ}の{下|した}に５{円玉|えんだま}！","ishidatami no shita ni go-en-dama!","Unter dem Pflaster: eine 5-Yen-Münze!","Under the paving: a 5-yen coin!"],1],[3,15,["{三年坂|さんねんざか}で{転|ころ}ぶと…{気|き}をつけて！","Sannenzaka de korobu to… ki o tsukete!","Wer am Sannenzaka stolpert… pass auf!","Trip on Sannenzaka and… be careful!"],0]],
 fl=[["fl_sannen_0",12,11,"#1e1e24","#c8325a",["{着物|きもの}で{散歩|さんぽ}、たのしい！","kimono de sanpo, tanoshii!","Im Kimono spazieren macht Spaß!","Walking in a kimono is fun!"],"{着物|きもの}の{人|ひと}","kimono no hito"],["fl_sannen_1",10,10,"#3a2a20","#5a7ac8",["{写真|しゃしん}をとってもいいですか。","shashin o totte mo ii desu ka.","Darf ich ein Foto machen?","May I take a photo?"],"{観光客|かんこうきゃく}","kankōkyaku"],["fl_sannen_2",12,14,"#1e1e24","#e0a020",["{八ツ橋|やつはし}、{一|ひと}つどうぞ。","yatsuhashi, hitotsu dōzo.","Ein Yatsuhashi, bitte sehr.","Have a yatsuhashi."],"{店員|てんいん}","ten'in"],["fl_sannen_3",4,15,"#1e1e24","#7a3a8a",["{下駄|げた}の{音|おと}がいいね。","geta no oto ga ii ne.","Schön, das Klacken der Geta.","I love the sound of geta."],"{着物|きもの}の{人|ひと}","kimono no hito"],["fl_sannen_4",13,12,"#555","#2f6f4a",["{人力車|じんりきしゃ}、{乗|の}りませんか。","jinrikisha, norimasen ka.","Eine Rikscha-Fahrt?","Want a rickshaw ride?"],"{車夫|しゃふ}","shafu"]])
g=G(12,9,'f','W');Rc(g,1,1,4,3,'t');Pt(g,[(2,2),(3,2)],'b');g[1][5]='j';Rc(g,7,1,10,3,'o');g[8][5]='D'
add(id='ryokan',ch=3,s='in',n=['旅館','Ryokan','Kyoto & Nara · Onsen-Gasthaus','Kyoto & Nara · Hot-spring inn'],m=S(g),npc=[['okami',3,5]],ex=[[5,8,'kyoto',16,7,[]]])
g=G(16,24,'.','P');V(g,7,15,21,'G');V(g,8,15,21,'G');H(g,22,0,8,'q');g[22][0]='X';Rc(g,5,12,10,14,'q');H(g,14,1,4,'M');H(g,14,11,14,'M');V(g,7,7,11,'G');V(g,8,7,11,'G');H(g,6,1,5,'M');H(g,6,10,14,'M');Rc(g,4,4,11,6,'q');Pt(g,[(4,14),(11,14)],'s');Pt(g,[(3,5),(12,5)],'s');Pt(g,[(2,3),(13,3),(3,9),(12,9),(2,17),(13,17),(4,20),(11,18),(2,11),(13,11)],'T');Rc(g,11,20,14,21,'J');Rc(g,1,20,2,21,'J');V(g,6,7,11,'P');V(g,9,7,11,'P');V(g,6,15,20,'P');V(g,9,15,20,'P')
add(id='inari',ch=3,s='autumn',n=['伏見稲荷','Fushimi Inari','Kyoto & Nara · Tausend Torii','Kyoto & Nara · Thousand torii'],m=S(g),o=[['shrine',5,1],['fox',5,12],['fox',10,12],['fox',6,4],['fox',9,4]],
 npc=[['inari',10,5]],ex=[[0,22,'kyoto',19,14,[]]])
g=G(24,14);V(g,11,4,12,'q');V(g,12,4,12,'q');g[0][11]='X';V(g,11,0,3,'q');Pt(g,[(2,3),(21,3),(3,8),(20,8),(2,12),(21,12),(7,11),(16,11)],'T');Pt(g,[(10,4),(13,4)],'s')
g[0][11]='X'
add(id='nara',ch=3,s='autumn',n=['奈良','Nara','Kyoto & Nara · Nara','Kyoto & Nara · Nara'],m=S(g),o=[['todaiji',8,1]] if False else [['todaiji',2,1]],
 npc=[['daibutsu',9,5],['senbei',15,8],['shika',6,9],['deer3',18,6],['deer4',4,12],['deer5',8,11],['deer6',21,11],['deer7',20,9],['deer8',3,7],['deer9',14,6]],ex=[[11,0,'kyoto',11,14,[]]])

# ---------- Kapitel 5: 大阪 ----------
g=G(24,14,'k',None);station_top(g,4,19,'4','6');Rc(g,0,4,23,8,'k');Rc(g,0,9,23,10,'~');Rc(g,11,9,12,10,'r');Rc(g,0,11,23,13,'k');g[6][23]='X';Pt(g,[(3,5),(4,5),(18,13),(19,13)],'y');Pt(g,[(8,13),(14,5)],'v')
add(id='osaka',ch=4,s='autumn',city=1,night=1,n=['道頓堀','Dōtonbori','Osaka · Dōtonbori','Osaka · Dōtonbori'],m=S(g),
 o=[['neonb',0,12,{'sign':'たこやき','k':0,'hg':40}],['neonb',2,12,{'sign':'くいだおれ','k':1,'hg':60}],['neonb',5,12,{'sign':'おこのみ','k':2,'hg':50}],['neonb',14,12,{'sign':'ラーメン','k':3,'hg':55}],['neonb',21,12,{'sign':'ゲーム','k':0,'hg':45}]],
 npc=[['kuidaore',9,6]],ex=[[4,1,'kyoto',19,2,[]],[19,1,'sapporo',4,2,['shiro']],[23,6,'osakajo',1,12,[]]])
g=G(24,16);Rc(g,3,1,20,11,'~');Rc(g,5,2,18,9,'.');Rc(g,11,10,12,11,'r');Rc(g,11,12,12,13,'q');H(g,12,0,11,'=');g[12][0]='X';V(g,11,7,9,'q');V(g,12,7,9,'q');Rc(g,7,6,16,6,'q');Pt(g,[(6,3),(17,3),(6,8),(17,8)],'T');Pt(g,[(10,7),(13,7)],'s');Pt(g,[(7,8),(8,8),(15,8),(16,8)],',');Pt(g,[(1,3),(22,3),(2,14),(21,14),(6,13),(17,13),(22,8),(1,8)],'T');Pt(g,[(15,13),(8,13)],',')
rail(g,14);add(id='osakajo',rail=[14],ch=4,s='autumn',n=['大阪城','Ōsaka-jō','Osaka · Burg Osaka','Osaka · Osaka Castle'],m=S(g),o=[['castle',9,3]],
 npc=[['shiro',14,12]],ex=[[0,12,'osaka',22,6,[]]])

# ---------- Kapitel 6: 北海道 ----------
g=G(24,14,'.',None);station_top(g,4,19,'5','7');Rc(g,0,4,23,13,'.');H(g,4,0,23,'=');V(g,11,4,13);H(g,8,11,22);g[8][23]='X';Pt(g,[(1,6),(22,6),(1,12),(22,12),(8,12),(15,12)],'T');Pt(g,[(6,11),(17,11)],'w')
add(id='sapporo',ch=5,s='winter',n=['札幌','Sapporo','Hokkaido · Sapporo','Hokkaido · Sapporo'],m=S(g),o=[['clock',3,5],['snowsc',15,9],['snowsc',4,10]],
 npc=[['tokei',8,7]],ex=[[4,1,'osaka',19,2,[]],[19,1,'gogome',4,15,['kami']],[23,8,'yukimura',1,8,[]]])
g=G(24,14);H(g,8,0,22);g[8][0]='X';H(g,6,15,22);g[6][23]='X';V(g,15,6,8);Rc(g,16,9,20,11,'~');V(g,5,5,8);V(g,11,5,8);Pt(g,[(2,11),(8,11),(13,12),(22,11),(2,2),(21,2)],'T');Pt(g,[(14,10)],'w')
rail(g,12);add(id='yukimura',rail=[12],ch=5,s='winter',n=['雪村','Yukimura','Hokkaido · Schneedorf','Hokkaido · Snow village'],m=S(g),o=[['minka',4,3,{'th':1}],['minka',10,3,{'th':1}],['minka',16,2,{}]],
 npc=[['yukiko',13,10]],ex=[[0,8,'sapporo',22,8,[]],[23,6,'yukiyama',1,8,['yukiko']]])
g=G(16,14,'.','M');V(g,7,4,12,'q');V(g,8,4,12,'q');H(g,8,0,7,'q');g[8][0]='X';Pt(g,[(5,4),(10,4)],'s');Pt(g,[(3,6),(12,6),(3,11),(12,11)],'P')
add(id='yukiyama',ch=5,s='winter',n=['雪山','Yukiyama','Hokkaido · Schneegipfel','Hokkaido · Snowy peak'],m=S(g),o=[['shrine',5,1],['torii',6,7]],
 npc=[['kami',9,4]],ex=[[0,8,'yukimura',22,6,[]]])

# ---------- Kapitel 7: 富士山 ----------
g=G(24,18,'.',None);Rc(g,0,0,23,4,'P');Rc(g,0,5,3,7,'P');Rc(g,20,5,23,7,'P');H(g,13,0,23,'=');H(g,14,0,23,'l');H(g,15,0,23,'l');H(g,16,0,23,'V');g[16][4]='Y';g[16][19]='Y';g[15][20]='3';H(g,17,0,23,'R');g[15][3]='6';V(g,12,8,12,'q');H(g,10,4,19,'q');V(g,4,10,13,'q');Pt(g,[(1,9),(22,9),(1,12),(22,12),(8,11),(16,11)],'P');Pt(g,[(11,8),(14,8)],'s');Pt(g,[(6,12),(18,12)],'b')
add(id='gogome',ch=6,s='summer',n=['五合目','Gogōme','Fuji · 5. Station','Fuji · 5th station'],m=S(g),o=[['fujimt',4,5],['torii',11,7],['hut',15,8]],
 npc=[['goraiko',9,10]],ex=[[4,16,'sapporo',19,2,[]],[19,16,'kanazawa',4,2,['fuji']],[12,7,'fujisan',12,13,[]]])
g=G(24,16,'u','M');H(g,5,7,18,'q');H(g,13,7,18,'q');V(g,7,5,13,'q');V(g,18,5,13,'q');V(g,12,13,14,'q');g[15][12]='X';V(g,12,3,4,'q');Pt(g,[(5,12),(20,8),(16,14),(3,7)],'M');Pt(g,[(10,4),(14,4)],'s')
add(id='fujisan',ch=6,s='summer',tint='rgba(255,170,90,.10)',n=['富士山頂','Fuji-sanchō','Fuji · Gipfel','Fuji · Summit'],m=S(g),o=[['fujibg',0,0,{'w':24,'dawn':1}],['torii',11,3],['crater',8,6]],
 npc=[['fuji',19,6]],ex=[[12,15,'gogome',12,8,[]]])

# ---------- Tokio: Hafen Odaiba ----------
g=G(24,14,'k',None);Rc(g,0,9,23,13,'~');H(g,8,0,23,'F');Rc(g,0,0,23,1,'k');H(g,4,0,23,'=');V(g,12,2,7,'=');g[4][0]='X';V(g,20,8,10,'r');V(g,19,9,10,'F');V(g,21,9,10,'F');g[11][19]='F';g[11][20]='F';g[11][21]='F';Pt(g,[(3,6),(8,6),(16,6),(21,6),(2,2),(21,2)],'T');Pt(g,[(6,7),(18,7)],'b');Pt(g,[(10,7)],'s')
add(id='odaiba',ch=1,s='spring',city=1,n=['お台場','Odaiba','Tokio · Hafen Odaiba','Tokyo · Odaiba harbour'],m=S(g),
 o=[['rbridge',0,12,{'w':24}],['ferris',17,1],['ship',4,9],['metro',5,2],['kanban',9,2,{'t':'うみ'}]],
 npc=[['minato',12,6]],it=[['kaizu',20,10,'map']],ex=[[0,4,'tower',18,13,[]]],sp=[[6,7,["ベンチから{海|うみ}が{見|み}える。","benchi kara umi ga mieru.","Von der Bank sieht man das Meer.","You can see the sea from the bench."],0],[10,7,["{灯台|とうだい}のあかり。","tōdai no akari.","Licht vom Leuchtturm.","Lighthouse light."],0]],
 fl=[["fl_odaiba_a1",3,7,"#3a2a20","#5a7a4a",["{今日|きょう}はアジが{釣|つ}れたよ。","kyō wa aji ga tsureta yo.","Heute habe ich Stöcker gefangen.","I caught horse mackerel today."],"{釣|つ}り{人|びと}","tsuribito"],["fl_odaiba_a2",22,7,"#555","#2a5fc9",["しーっ、{魚|さかな}が{逃|に}げる！","shī, sakana ga nigeru!","Psst, die Fische fliehen!","Shh, the fish will flee!"],"{釣|つ}り{人|びと}","tsuribito"],["fl_odaiba_0",8,5,"#3a2a20","#5fa8e8",["{観覧車|かんらんしゃ}に{乗|の}りたい！","kanransha ni noritai!","Ich will aufs Riesenrad!","I want to ride the Ferris wheel!"],"{子|こ}ども","kodomo"]])

# ---------- Kapitel 8-12: 西へ ----------
def city(id,ch,s,n,o,npc,ex,extra=None,city_=0,sp=None,fl=None,fill='.'):
    g=G(24,14,fill,None);station_top(g,4,19 if ex.get('fwd') else None,'1','3' if ex.get('fwd') else None)
    Rc(g,0,4,23,13,fill);H(g,8,1,22,'k' if city_ else '=');V(g,4,4,8,'k' if city_ else '=');V(g,19,4,8,'k' if city_ else '=')
    if extra: extra(g)
    E=[[4,1,ex['back'][0],ex['back'][1],ex['back'][2],[]]]
    if ex.get('fwd'): E.append([19,1,ex['fwd'][0],4,2,ex['fwd'][1]])
    add(id=id,ch=ch,s=s,city=city_,n=n,m=S(g),o=o,npc=npc,ex=E,sp=sp or [],fl=fl or [])
def kz(g):
    Rc(g,6,5,13,7,'~');Pt(g,[(9,5),(10,7),(6,7),(13,5)],'.');Pt(g,[(8,6),(9,6),(10,6),(11,6)],'q');Pt(g,[(2,5),(15,5),(17,7),(21,5),(1,7),(14,7),(5,5)],'T');Pt(g,[(16,6),(3,6),(18,5),(22,7)],',');Pt(g,[(7,4),(12,4)],'s');Rc(g,8,9,15,12,'.');Rc(g,7,9,7,13,'~');Rc(g,16,9,16,13,'~');Rc(g,7,13,16,13,'~');Pt(g,[(3,11),(20,11),(5,13),(19,13)],'T')
city('kanazawa',7,'spring',['金沢','Kanazawa','Kanazawa · Kenroku-en','Kanazawa · Kenroku-en'],[['castle',9,9,{'nd':1}],['kotoji',14,6],['kanban',17,9,{'t':'金沢城'}],['kanban',5,4,{'t':'兼六園'}]],[['kinpaku',3,7]],{'back':('gogome',19,15),'fwd':('hiroshima',['kinpaku'])},kz,
 sp=[[16,6,["{琴柱灯籠|ことじとうろう}：{兼六園|けんろくえん}のシンボル。","kotoji-tōrō: Kenroku-en no shinboru.","Kotoji-Laterne: Symbol des Kenroku-en.","Kotoji lantern: symbol of Kenroku-en."],0],[6,9,["{金沢城|かなざわじょう}：{白|しろ}い{壁|かべ}と{鉛瓦|なまりがわら}。","Kanazawa-jō: shiroi kabe to namarigawara.","Burg Kanazawa: weiße Wände und Bleiziegel.","Kanazawa Castle: white walls and lead tiles."],0]],
 fl=[["fl_kanazawa_0",18,6,"#555","#7a5c99",["{金箔|きんぱく}アイス、たべた？","kinpaku aisu, tabeta?","Schon Blattgold-Eis gegessen?","Have you tried gold-leaf ice cream?"],"{観光客|かんこうきゃく}","kankōkyaku"],["fl_kanazawa_1",16,4,"#1e1e24","#e98fb0",["{桜|さくら}がきれい！","sakura ga kirei!","Die Kirschblüten sind schön!","The cherry blossoms are pretty!"],"{観光客|かんこうきゃく}","kankōkyaku"]])
def hs(g):
    Rc(g,0,11,23,13,'~');Rc(g,9,11,10,13,'r');Pt(g,[(2,6),(21,6),(6,10),(16,10)],'T');Pt(g,[(14,7)],'s')
city('hiroshima',8,'summer',['広島','Hiroshima','Hiroshima · Friedenspark','Hiroshima · Peace Park'],[['gdome',6,5],['kanban',16,5,{'t':'お好み焼'}]],[['heiwa',13,6]],{'back':('kanazawa',19,2),'fwd':('fukuoka',['heiwa'])},hs,
 sp=[[14,7,["{平和|へいわ}の{灯|ひ}。ずっと{燃|も}えている。","heiwa no hi. zutto moete iru.","Die Flamme des Friedens brennt immer.","The Flame of Peace keeps burning."],0]],
 fl=[["fl_hiroshima_0",17,9,"#3a2a20","#e8665a",["お{好|この}み{焼|や}き、{広島風|ひろしまふう}がいちばん！","okonomiyaki, hiroshima-fū ga ichiban!","Okonomiyaki nach Hiroshima-Art ist die beste!","Hiroshima-style okonomiyaki is the best!"],"{店員|てんいん}","ten'in"]])
def fk(g):
    Pt(g,[(2,11),(21,11),(2,6)],'T');Pt(g,[(8,10),(9,10),(14,10),(15,10)],'y')
city('fukuoka',9,'summer',['福岡','Fukuoka','Fukuoka · Hakata','Fukuoka · Hakata'],[['ftower',20,5],['kanban',7,5,{'t':'屋台'}],['kanban',12,10,{'t':'ラーメン'}]],[['yatai2',11,10]],{'back':('hiroshima',19,2),'fwd':('nagasaki',['yatai2'])},fk,city_=1,fill='k',
 sp=[[8,10,["{屋台|やたい}：とんこつラーメンのいいにおい。","yatai: tonkotsu rāmen no ii nioi.","Straßenstand: Duft von Tonkotsu-Ramen.","Food stall: smell of tonkotsu ramen."],0],[15,10,["{屋台|やたい}のいすの{下|した}に１０{円|えん}！","yatai no isu no shita ni jū-en!","Unter dem Hocker: 10 Yen!","Under the stool: 10 yen!"],1]],
 fl=[["fl_fukuoka_0",17,7,"#1e1e24","#2b3f6a",["{博多|はかた}は{夜|よる}がたのしいよ。","Hakata wa yoru ga tanoshii yo.","Hakata ist nachts toll.","Hakata is fun at night."],"サラリーマン","sararīman"]])
def ng(g):
    Rc(g,15,4,16,13,'~');g[8][15]='r';g[8][16]='r';Pt(g,[(2,6),(21,6),(6,10),(19,11)],'T');Pt(g,[(18,6),(8,6)],'s')
city('nagasaki',10,'autumn',['長崎','Nagasaki','Nagasaki · Brillenbrücke','Nagasaki · Spectacles Bridge'],[['megane',14,8],['dejima',6,4],['kanban',12,5,{'t':'カステラ'}]],[['kasutera',10,7]],{'back':('fukuoka',19,2),'fwd':('okinawa',['kasutera'])},ng,
 sp=[[18,6,["ランタンフェスティバルのちょうちん。","rantan fesutibaru no chōchin.","Laterne vom Laternenfest.","A lantern from the Lantern Festival."],0]],
 fl=[["fl_nagasaki_0",18,9,"#555","#c8323d",["カステラ、ひとつどうぞ！","kasutera, hitotsu dōzo!","Ein Stück Castella, bitte sehr!","Have a piece of castella!"],"お{店|みせ}の{人|ひと}","omise no hito"]])
def ok(g):
    Rc(g,0,10,23,10,'n');Rc(g,0,11,23,13,'~');Pt(g,[(2,6),(21,6),(6,9),(17,9)],'y');Pt(g,[(10,6),(13,6)],'s')
city('okinawa',11,'summer',['沖縄','Okinawa','Okinawa · Shuri & Strand','Okinawa · Shuri & beach'],[['shurei',10,4],['kanban',16,5,{'t':'めんそーれ'}]],[['shisa',12,8]],{'back':('nagasaki',19,2)},ok,
 sp=[[10,6,["シーサー：{家|いえ}をまもる{守|まも}り{神|がみ}。","shīsā: ie o mamoru mamorigami.","Shīsā: Schutzgeist des Hauses.","Shisa: guardian of the house."],0],[13,6,["シーサーの{口|くち}は{開|あ}いている。もう一つは{閉|と}じている。","shīsā no kuchi wa aite iru. mō hitotsu wa tojite iru.","Ein Shīsā hat den Mund offen, der andere geschlossen.","One shisa's mouth is open, the other is closed."],0]],
 fl=[["fl_okinawa_0",18,9,"#3a2a20","#5fe3ff",["めんそーれ！{沖縄|おきなわ}へようこそ！","mensōre! Okinawa e yōkoso!","Mensōre! Willkommen in Okinawa!","Mensōre! Welcome to Okinawa!"],"{島|しま}の{人|ひと}","shima no hito"]])


def footprint(a):
    m=[list(r) for r in a['m']]
    global SOLD
    SOL={'minka':(3,2,["###","#D#"]),'machiya':(3,2,["###","#D#"]),'school':(5,3,None),'station':(5,2,["#####","##D##"]),'shrine':(5,3,None),'temple':(7,3,None),'pagoda':(2,2,None),'torii':(3,1,["#.#"]),'kaminari':(4,1,["#..#"]),'ttower':(4,2,["#..#","#..#"]),'sky':(2,2,None),'neonb':(2,2,None),'screen':(3,2,None),'tokyoeki':(10,2,["##########","#D###D##D#"]),'konbini':(4,2,["####","#D##"]),'ramen':(3,2,["###","#D#"]),'museum':(6,2,None),'castle':(6,4,None),'kinkaku':(4,3,None),'todaiji':(8,3,None),'ftorii':(4,1,None),'lighthouse':(1,1,None),'clock':(3,2,None),'snowsc':(3,2,None),'hut':(4,2,None),'ryokan':(4,2,["####","#D##"]),'yagura':(2,2,None),'fox':(1,1,None),'fujibg':(16,3,None),'scramble':(12,10,['.'*12]*10),'round':(3,2,None),'shibueki':(8,2,['########','###D####']),'metro':(2,1,None),'fujimt':(16,2,None),'dsign':(1,1,None),'crater':(10,7,None),'rbridge':(24,2,['.'*24,'.'*24]),'ferris':(4,3,None),'ship':(5,2,None),'kanban':(1,1,None),'kotoji':(2,1,None),'gdome':(4,3,None),'ftower':(2,2,None),'megane':(4,2,['....','....']),'dejima':(4,2,None),'shurei':(4,2,['#..#','#..#']),'skytree':(2,2,None),'tocho':(4,3,None),'animeb':(2,2,None),'zebra':(3,2,['...','...']),'canopy':(1,1,['.']),'bamboo':(1,1,None),'fishbox':(1,1,None)}
    SOLD=SOL
    for o in a.get('o',[]):
        w,h,sol=SOL[o[0]]
        if o[0]=='fujibg': w=o[3]['w']
        sol=sol or ['#'*w]*h
        door=len(o)>3 and o[3].get('door')
        dr=len(o)>3 and o[3].get('dr')
        if o[0] in('ramen','konbini'): door=True
        for dy in range(h):
            for dx in range(w):
                c=sol[dy][dx];X=o[1]+dx;Y=o[2]+dy
                if dr and [dx,dy]==dr: c='D';door=True
                if Y>=len(m) or X>=len(m[0]): continue
                if c=='#' or (c=='D' and not door): m[Y][X]='B'
                elif c=='D': m[Y][X]='D'
    return [''.join(r) for r in m]
def deco(aid,objs):
    a=[b for b in A if b['id']==aid][0];m=[list(r) for r in a['m']];Hh,Ww=len(m),len(m[0])
    busy={(n[1],n[2]) for n in a.get('npc',[])}|{(i[1],i[2]) for i in a.get('it',[])}|{(p[0],p[1]) for p in a.get('sp',[])}|{(f[1],f[2]) for f in a.get('fl',[])}|{(e[0],e[1]) for e in a['ex']}
    busy|={(e[0]+dx,e[1]+dy) for e in a['ex'] for dx in range(-2,3) for dy in range(-2,3)}
    for o in a.get('o',[]):
        sl=SOLD.get(o[0]) if 'SOLD' in globals() else None
        if sl and sl[2]:
            for dy,r in enumerate(sl[2]):
                for dx,c in enumerate(r):
                    if c=='D': busy.add((o[1]+dx,o[2]+dy+1))
    fp=footprint(a)
    for o in objs:
        if o[0]=='sky' and len(o)<4: o.append({'hg':10+((o[1]*7+o[2]*3)%3)*6,'c':['#5a6a88','#6b7a8f','#7a6a62'][(o[1]+o[2])%3]})
        k,x,y=o[0],o[1],o[2];w,h,sol=SOLD[k];sol=sol or ['#'*w]*h
        dd=[(x+dx,y+dy+1) for dy in range(h) for dx in range(w) if sol[dy][dx]=='D' and (k in('konbini','ramen','machiya','minka') or (len(o)>3 and o[3].get('door')))]
        cells=[(x+dx,y+dy) for dy in range(h) for dx in range(w)]+dd
        ok=all(0<=cx<Ww and 0<=cy<Hh-1 and fp[cy][cx] in ('.,PTyk' if a.get('city') else '.,PTy') and (cx,cy) not in busy for cx,cy in cells[:w*h])
        ok=ok and all(cy<Hh and fp[cy][cx] in '.,=qkPT' and (cx,cy) not in busy for cx,cy in dd)
        if not ok: print('skip',aid,o);continue
        for cx,cy in dd:
            if fp[cy][cx] in 'PT': m[cy][cx]='k' if a.get('city') else '='
        for cx,cy in cells[:w*h]: m[cy][cx]='k' if a.get('city') else '.'
        a['m']=[''.join(r) for r in m];a['o'].append(o);fp=footprint(a);busy|=set(dd)
def MS(s,c,d=0): return {'sign':s,'nc':c}
deco('kyoto',[['machiya',12,5,MS('茶','#4f7a3a')],['machiya',19,5,MS('扇子','#6b4f9a')],['machiya',5,13,MS('豆腐','#7a6a4a')],['machiya',13,11,MS('京菓子','#b0446a')]])
deco('nara',[['machiya',14,9,MS('せんべい','#b5651d')],['machiya',17,9,MS('奈良漬','#5a7a2a')],['machiya',5,6,MS('墨','#2b2b33')]])
deco('kanazawa',[['machiya',1,9,MS('茶屋','#a8324a',1)],['machiya',19,9,MS('金箔','#c89a2a')],['machiya',15,5,MS('九谷焼','#2f6f9a')],['machiya',13,5,MS('和菓子','#c46a2a')]])
deco('hiroshima',[['machiya',1,5,MS('もみじ饅頭','#c0503a')],['machiya',11,5,MS('牡蠣','#5a7ac8')],['machiya',20,5,MS('お好み焼','#d33',1)]])
deco('fukuoka',[['machiya',1,9,MS('明太子','#c0503a')],['machiya',20,9,MS('うどん','#7a6a4a')],['machiya',5,5,MS('博多織','#6b4f9a')],['machiya',15,5,MS('屋台','#c46a2a')]])
deco('nagasaki',[['machiya',1,9,MS('ちゃんぽん','#c8323d')],['machiya',10,9,MS('中華街','#d33')],['machiya',20,9,MS('べっこう','#b5651d')]])
deco('okinawa',[['minka',1,6,{'nc':'#c8503a'}],['minka',20,6,{'nc':'#c8503a'}],['machiya',6,6,MS('ちんすこう','#e0a020')]])
deco('sapporo',[['machiya',12,5,MS('ラーメン','#c0503a',1)],['machiya',19,9,MS('かに','#d33')],['machiya',6,5,MS('とうきび','#e0a020')]])

deco('yukimura',[['minka',19,3,{'th':1}]])
deco('tokyo',[['sky',4,5],['sky',7,5],['sky',15,5],['sky',18,5],['konbini',7,8],['ramen',18,10],['sky',21,10],['sky',0,9],['kanban',6,8,{'t':'丸の内'}]])
deco('asakusa',[['machiya',4,5,MS('人形焼','#c0503a')],['machiya',17,7,MS('扇子','#6b4f9a')],['machiya',17,9,MS('手ぬぐい','#2f6f9a')],['machiya',6,12,MS('天ぷら','#c46a2a')],['machiya',14,12,MS('もんじゃ','#7a6a4a')],['machiya',4,9,MS('せんべい','#a8324a')]])
deco('ueno',[['machiya',2,4,MS('甘味','#c46a2a')],['machiya',5,4,MS('アメ横','#d33',1)],['machiya',15,4,MS('果物','#4f7a3a')],['machiya',8,9,MS('みやげ','#2f6f9a')],['machiya',16,6,MS('カフェ','#7a5c99')]])
deco('tower',[['machiya',2,11,MS('そば','#7a6a4a',1)],['machiya',14,1,MS('みやげ','#c0503a')],['machiya',3,1,MS('喫茶','#4f7a3a')],['sky',16,11]])
deco('odaiba',[['machiya',15,5,MS('魚屋','#2f6f9a')],['sky',0,0],['sky',2,0],['sky',7,0],['sky',10,0],['sky',14,0],['konbini',13,5],['sky',21,0]])
deco('akiba',[['sky',22,0],['ramen',2,9],['sky',11,2],['sky',14,2],['sky',17,2],['sky',20,2],['konbini',10,11],['sky',22,9]])
deco('shinjuku',[['sky',2,11],['sky',20,11],['konbini',8,11]])
deco('shibuya',[['sky',0,13],['konbini',15,13]])
for a in A:
    if a.get('s')=='in': continue
    m=[list(r) for r in a['m']];H_=len(m);W_=len(m[0]);new=[]
    for e in a['ex']:
        x,y=e[0],e[1]
        if m[y][x]!='X': continue
        if x in(0,W_-1): along=[(x,y-1),(x,y+1)];inw=(1 if x==0 else -1,0)
        elif y in(0,H_-1): along=[(x-1,y),(x+1,y)];inw=(0,1 if y==0 else -1)
        else: continue
        pathc='k' if a.get('city') else ('q' if m[y+inw[1]][x+inw[0]]=='q' else '=')
        for (ax,ay) in along:
            if not(0<=ax<W_ and 0<=ay<H_): continue
            if m[ay][ax] in 'RVYZ~l': continue
            m[ay][ax]='X';ix,iy=ax+inw[0],ay+inw[1]
            if m[iy][ix] in 'PTFMJ.,': m[iy][ix]=pathc
            new.append([ax,ay]+e[2:])
    a['ex']+=new;a['m']=[''.join(r) for r in m]

DOORS={'school':(2,2),'shrine':(2,2),'temple':(3,2),'todaiji':(3,2),'museum':(2,1),'castle':(2,3),'hut':(1,1),'clock':(1,1),'minka':(1,1),'machiya':(1,1),'shibueki':(3,1)}
INNM={'school':['学校','Gakkō','Schule','School'],'shrine':['本殿','Honden','Schreinhalle','Shrine hall'],'temple':['お寺','Otera','Tempelhalle','Temple hall'],'todaiji':['大仏殿','Daibutsuden','Halle des Buddha','Great Buddha hall'],'museum':['博物館','Hakubutsukan','Museum','Museum'],'castle':['天守','Tenshu','Burgturm','Castle keep'],'hut':['小屋','Koya','Hütte','Hut'],'clock':['時計台','Tokeidai','Uhrturm','Clock tower'],'minka':['家','Ie','Haus','House'],'machiya':['店','Mise','Laden','Shop'],'shibueki':['ハチ公口','Hachikō-guchi','Hachikō-Ausgang','Hachikō exit']}
def interior(k):
    g=G(12,9,'f','W')
    if k=='school':
        for y in (3,5):
            for x in (2,4,7,9): g[y][x]='b'
        Pt(g,[(1,1),(2,1),(3,1)],'j');Pt(g,[(9,1),(10,1)],'j')
    elif k in('shrine','temple','todaiji','castle'):
        Rc(g,2,2,9,5,'t');Pt(g,[(2,1),(9,1)],'s');g[1][5]='r';g[1][6]='r'
    elif k=='museum':
        Pt(g,[(1,1),(3,1),(5,1),(7,1),(9,1),(10,1)],'j');Pt(g,[(3,4),(8,4)],'s')
    elif k=='shibueki':
        Pt(g,[(3,4),(5,4),(7,4),(9,4)],'b');Pt(g,[(1,1),(2,1),(9,1),(10,1)],'j');g[5][10]='t'
    elif k=='machiya':
        Pt(g,[(1,1),(2,1),(3,1),(8,1),(9,1),(10,1)],'j');Rc(g,4,3,7,3,'b');Pt(g,[(2,5),(9,5)],'b')
    else:
        Rc(g,3,3,8,5,'t');Rc(g,5,4,6,4,'b');Pt(g,[(1,1),(10,1),(2,1)],'j')
    g[8][5]='D'
    return S(g)
NEWIN=[]
for a in list(A):
    if a.get('s')=='in': continue
    m=[list(r) for r in a['m']]
    for i,o in enumerate(a.get('o',[])):
        k=o[0]
        if k not in DOORS: continue
        if len(o)>3 and (o[3].get('door') or o[3].get('dr') or o[3].get('nd')): continue
        if k=='minka' and a['id']=='mura': pass
        dx,dy=DOORS[k];X,Y=o[1]+dx,o[2]+dy;fy=Y+1
        if fy>=len(m) or Y>=len(m): continue
        if any(e[0]==X and e[1]==fy for e in a['ex']) or any(n[1]==X and n[2]==fy for n in a.get('npc',[])) or any(t[1]==X and t[2]==fy for t in a.get('it',[])): continue
        if m[fy][X] in 'RVYZ~WM': continue
        if m[fy][X] in 'PTJ.,': m[fy][X]='k' if a.get('city') else '='
        nid=f"{a['id']}_{k}{i}"
        if len(o)<4: o.append({})
        o[3]['dr']=[dx,dy]
        nm=INNM[k];an=a['n']
        NEWIN.append(dict(id=nid,ch=a['ch'],s='in',gen=1,n=[nm[0],nm[1],an[2].split(' · ')[0]+' · '+nm[2],an[3].split(' · ')[0]+' · '+nm[3]],m=interior(k),npc=[],ex=[[5,8,a['id'],X,fy,[]]]))
        a['ex'].append([X,Y,nid,5,7,[]])
    a['m']=[''.join(r) for r in m]
for a in NEWIN:
    if a['id'].startswith('odaiba_machiya'):
        a['o']=[['fishbox',x,y,{'v':(x+y)%4}] for (x,y) in [(2,3),(3,3),(4,3),(7,3),(8,3),(9,3),(2,5),(3,5),(8,5),(9,5)]];a['n']=['魚市場','Uoichiba','Tokio · Fischmarkt','Tokyo · Fish market']
A+=NEWIN
g=G(24,12,'k',None);station_top(g,4,19,'1','3');H(g,5,0,23,'F');g[5][10]='I';g[5][11]='l';g[5][12]='l';g[5][13]='I';H(g,11,0,23,'F');g[11][12]='X';Pt(g,[(3,8),(4,8),(19,8),(20,8)],'b');Pt(g,[(1,7),(22,7),(2,7),(21,7)],'v');Pt(g,[(7,6),(8,6),(15,6),(16,6)],'I');Pt(g,[(7,9),(16,9)],'y')
A.append(dict(id='tokyoin',ch=1,s='spring',city=1,n=['東京駅','Tōkyō-eki','Tokio · Hauptbahnhof','Tokyo · Central Station'],m=S(g),o=[['kanban',5,6,{'t':'丸の内口'}],['kanban',18,6,{'t':'きっぷ'}]],npc=[['annai',12,7]],it=[],ex=[[4,1,'eki',7,3,[]],[19,1,'umi',4,2,['tower']],[12,11,'tokyo',12,3,[]]]))

for a in A:
    if a.get('s')=='in' or a['id'] in ('eki',): continue
    m=a['m']
    for ry in range(len(m)-1):
        if 'Y' in m[ry] and ry+1<len(m) and m[ry+1].count('l')>len(m[0])//2:
            a.setdefault('o',[]).insert(0,['canopy',0,ry+1,{'w':len(m[0]),'t':a['n'][0],'c':'#2a5fc9' if a['ch']>=1 else '#2f9e4f'}]);break
        if 'Y' in m[ry] and ry>0 and m[ry-1].count('l')>len(m[0])//2:
            a.setdefault('o',[]).insert(0,['canopy',0,ry-1,{'w':len(m[0]),'t':a['n'][0],'c':'#2a5fc9' if a['ch']>=1 else '#2f9e4f'}]);break
import os
HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,'interiors.py')).read())
apply(A)
ids=[a['id'] for a in A]
WALK=set(".,=qnkazlYcftXDGrLuZ")
err=[]
for a in A:
    w=len(a['m'][0])
    for r in a['m']:
        if len(r)!=w: err.append(a['id']+' width')
    if a['id'] in('ramen','konbini'):
        for o in a.get('o',[]): pass
for a in A:
    for o in a.get('o',[]):
        if o[0] in ('ramen','konbini'):
            if len(o)<4: o.append({})
            o[3]['door']=1
fm={a['id']:footprint(a) for a in A}
for a in A: a['ex']=[e for e in a['ex'] if fm[a['id']][e[1]][e[0]]!='B']

def reach(a,m):
    Hh,Ww=len(m),len(m[0]);st=[tuple(a['start'])] if a.get('start') else []
    st+=[(e[0],e[1]) for e in a['ex'] if m[e[1]][e[0]]!='D']
    seen=set(st);q=list(st)
    while q:
        x,y=q.pop()
        for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny=x+dx,y+dy
            if 0<=nx<Ww and 0<=ny<Hh and (nx,ny) not in seen and m[ny][nx] in WALK: seen.add((nx,ny));q.append((nx,ny))
    return seen
DROP=[]
for a in A:
    if a.get('s')=='in': continue
    for e in [e for e in a['ex'] if e[2].startswith(a['id']+'_')]:
        m=[list(r) for r in fm[a['id']]];Hh,Ww=len(m),len(m[0]);fx,fy=e[0],e[1]+1
        R_=reach(a,m)
        if (fx,fy) in R_: continue
        prev={(fx,fy):None};q=[(fx,fy)];hit=None
        while q and not hit:
            x,y=q.pop(0)
            for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny=x+dx,y+dy
                if not(1<=nx<Ww-1 and 1<=ny<Hh-1) or (nx,ny) in prev: continue
                if (nx,ny) in R_: prev[(nx,ny)]=(x,y);hit=(nx,ny);break
                if m[ny][nx] in 'PTJ.,=qkn':prev[(nx,ny)]=(x,y);q.append((nx,ny))
        if not hit: DROP.append(e);continue
        p=prev[hit];pc='k' if a.get('city') else '='
        mm=[list(r) for r in a['m']]
        while p:
            if mm[p[1]][p[0]] in 'PTJ.,': mm[p[1]][p[0]]=pc
            p=prev[p]
        a['m']=[''.join(r) for r in mm];fm[a['id']]=footprint(a)
print('DROP',[(e[2]) for e in DROP])
for a in A:
    m=fm[a['id']]
    for e in a['ex']:
        x,y,t,tx,ty,gt=e
        if t not in ids: err.append(a['id']+' bad target '+t);continue
        if m[y][x] not in WALK: err.append(f"{a['id']} exit tile {x},{y} '{m[y][x]}'")
        tm=fm[t]
        if not (0<=ty<len(tm) and 0<=tx<len(tm[0])): err.append(f"{a['id']}->{t} arrival out of map");continue
        if tm[ty][tx] not in WALK: err.append(f"{a['id']}->{t} arrival {tx},{ty} '{tm[ty][tx]}'")
        T=[b for b in A if b['id']==t][0]
        if any(f[0]==tx and f[1]==ty for f in T['ex']): err.append(f"{a['id']}->{t} arrival on exit")
    for n in a.get('npc',[]):
        c=m[n[2]][n[1]]
        if c not in WALK and c not in 'tb': err.append(f"{a['id']} npc {n[0]} on '{c}'")
    for i in a.get('it',[]):
        if m[i[2]][i[1]] not in WALK: err.append(f"{a['id']} item {i[0]} on '{m[i[2]][i[1]]}'")
print('\n'.join(err) or 'OK',len(A))
for a in A:
    for e in a['ex']: e[2]=ids.index(e[2])
    a['npc']=[[n[0],n[1],n[2],None,'',''] for n in a.get('npc',[])]
NAMES={'minato':['{船長|せんちょう}','senchō'],'kinpaku':['{職人|しょくにん}','shokunin'],'heiwa':['ガイドさん','gaido-san'],'yatai2':['{大将|たいしょう}','taishō'],'kasutera':['{菓子|かし}{職人|しょくにん}','kashi shokunin'],'shisa':['おじい','ojī'],'oba':['おばあさん','obāsan'],'kid':['たろう','Tarō'],'shop':['{店員|てんいん}','ten’in'],'guard':['{門番|もんばん}','monban'],'eki':['{駅員|えきいん}','ekiin'],'nekolady':['{山田|やまだ}さん','Yamada-san'],'sensei':['{先生|せんせい}','sensei'],'guard2':['{門番|もんばん}','monban'],'monk':['お{坊|ぼう}さん','obōsan'],'fox':['きつね','kitsune'],'shrine':['{神主|かんぬし}','kannushi'],'ojii':['おじいさん','ojīsan'],'kaisatsu':['{駅員|えきいん}','ekiin'],'annai':['{案内係|あんないがかり}','annaigakari'],'hachiko':['ハチ{公|こう}','Hachikō'],'mika':['ミカ','Mika'],'salary':['{会社員|かいしゃいん}','kaishain'],'ramen':['{大将|たいしょう}','taishō'],'kimono':['{着物屋|きものや}さん','kimonoya-san'],'omikuji':['{巫女|みこ}さん','miko-san'],'otaku':['ケン','Ken'],'konbini':['{店員|てんいん}','ten’in'],'ueno':['{飼育員|しいくいん}','shiikuin'],'panda':['パンダ','panda'],'tower':['スタッフ','sutaffu'],'ryoshi':['{漁師|りょうし}','ryōshi'],'suika':['ゆうた','Yūta'],'yatai':['{屋台|やたい}の{人|ひと}','yatai no hito'],'matsuri':['{法被|はっぴ}の{人|ひと}','happi no hito'],'itsuku':['{案内人|あんないにん}','annainin'],'deer1':['{鹿|しか}','shika'],'deer2':['{鹿|しか}','shika'],'deer3':['{鹿|しか}','shika'],'deer4':['{鹿|しか}','shika'],'deer5':['{鹿|しか}','shika'],'deer6':['{鹿|しか}','shika'],'deer7':['{鹿|しか}','shika'],'deer8':['{鹿|しか}','shika'],'deer9':['{鹿|しか}','shika'],'tera':['お{坊|ぼう}さん','obōsan'],'maiko':['{舞妓|まいこ}さん','maiko-san'],'okami':['{女将|おかみ}さん','okami-san'],'inari':['お{稲荷|いなり}さん','oinari-san'],'daibutsu':['お{坊|ぼう}さん','obōsan'],'senbei':['せんべい{屋|や}','senbei-ya'],'shika':['{鹿|しか}','shika'],'kuidaore':['{料理人|りょうりにん}','ryōrinin'],'shiro':['{城|しろ}の{案内人|あんないにん}','shiro no annainin'],'tokei':['ガイド','gaido'],'yukiko':['ゆきこ','Yukiko'],'kami':['{山|やま}の{神様|かみさま}','yama no kamisama'],'goraiko':['{山|やま}ガイド','yama gaido'],'fuji':['{神主|かんぬし}','kannushi']}
for a in A:
    for n in a['npc']:
        if n[0] not in NAMES: print('NO NAME',n[0])
        n[4],n[5]=NAMES.get(n[0],['?','?'])
W=json.dumps(A,ensure_ascii=False)
open(os.path.join(HERE,'rpg3_world.json'),'w').write(W)
import re
SRC=os.path.join(HERE,'..','..','src','index.html')
t=open(SRC).read()
t2=re.sub(r'const W3DATA=.*?;\n',lambda m:'const W3DATA='+W+';\n',t,count=1,flags=re.S)
open(SRC,'w').write(t2)
print('world embedded:',len(A),'areas')
for a in A:
    if a['id'] in ('mura','tokyo','asakusa','kyoto','osakajo'):
        print(a['id']);print('\n'.join(fm[a['id']]))
