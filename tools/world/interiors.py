L=lambda j,r,de,en:[j,r,de,en]
HOME=dict(sp=[(1,1,L("{本棚|ほんだな}：{古|ふる}いアルバムがある。","hondana: furui arubamu ga aru.","Bücherregal: ein altes Fotoalbum.","Bookshelf: an old photo album.")),
 (5,4,L("こたつ。あたたかくて、{動|うご}きたくない…","kotatsu. atatakakute, ugokitakunai…","Kotatsu. So warm, man will nicht aufstehen…","Kotatsu. So warm you never want to leave…")),
 (10,1,L("ひきだしに１０{円|えん}を{見|み}つけた！","hikidashi ni jū-en o mitsuketa!","In der Schublade: 10 Yen gefunden!","Found 10 yen in a drawer!"),1)],
 fl=[(8,6,"#3a2a20","#7a9a5a",L("ゆっくりしていってね。お{茶|ちゃ}、どうぞ。","yukkuri shite itte ne. ocha, dōzo.","Mach es dir gemütlich. Tee?","Make yourself at home. Some tea?"),"お{母|かあ}さん","okāsan")])
SCHOOL=dict(sp=[(2,1,L("{黒板|こくばん}：「{今日|きょう}の{漢字|かんじ}：{山|やま}・{川|かわ}・{木|き}」","kokuban: kyō no kanji: yama, kawa, ki","Tafel: Kanji des Tages: 山 Berg, 川 Fluss, 木 Baum","Blackboard: today's kanji: 山 mountain, 川 river, 木 tree")),
 (2,3,L("つくえ。ノートに「あいうえお」と{書|か}いてある。","tsukue. nōto ni aiueo to kaite aru.","Pult. Im Heft steht „あいうえお“.","Desk. The notebook says あいうえお.")),
 (9,5,L("{机|つくえ}の{中|なか}にえんぴつを{見|み}つけた！","tsukue no naka ni enpitsu o mitsuketa!","Im Pult einen Bleistift gefunden!","Found a pencil in the desk!"),1),
 (9,1,L("{時間割|じかんわり}：１{時間目|じかんめ}は{国語|こくご}。","jikanwari: ichi-jikanme wa kokugo.","Stundenplan: 1. Stunde Japanisch.","Timetable: 1st period is Japanese."))],
 fl=[(6,4,"#1e1e24","#2b3f6a",L("{宿題|しゅくだい}、わすれちゃった…","shukudai, wasurechatta…","Hausaufgaben vergessen…","I forgot my homework…"),"{生徒|せいと}","seito")])
SHOP=dict(sp=[(1,1,L("{招|まね}き{猫|ねこ}が{手|て}をふっている。","maneki-neko ga te o futte iru.","Eine Winkekatze winkt.","A beckoning cat waves.")),
 (5,3,L("メニュー：コーヒー ３００{円|えん}、ケーキ ４００{円|えん}","menyū: kōhī 300 en, kēki 400 en","Karte: Kaffee 300 Yen, Kuchen 400 Yen","Menu: coffee 300 yen, cake 400 yen")),
 (10,1,L("{棚|たな}のうしろに５{円玉|えんだま}！ラッキー！","tana no ushiro ni go-en-dama! rakkī!","Hinterm Regal: eine 5-Yen-Münze! Glück!","Behind the shelf: a 5-yen coin! Lucky!"),1)],
 fl=[(8,5,"#555","#e98fb0",L("ねこがかわいい～！","neko ga kawaii~!","Die Katzen sind so süß!","The cats are so cute!"),"お{客|きゃく}さん","okyakusan")])
SHR=lambda what:dict(sp=[(5,1,L("おさいせん{箱|ばこ}。５{円|えん}を{入|い}れて、{手|て}を{合|あ}わせる。","osaisen-bako. go-en o irete, te o awaseru.","Opferkasten. 5 Yen hinein und die Hände falten.","Offering box. Put in 5 yen and put your hands together.")),
 (2,1,L("{灯籠|とうろう}にあかりがともっている。","tōrō ni akari ga tomotte iru.","In der Steinlaterne brennt ein Licht.","A light glows in the stone lantern.")),
 (9,1,what)],
 fl=[(3,6,"#555","#3a4a6a",L("しずかで、{気持|きも}ちがいいですね。","shizuka de, kimochi ga ii desu ne.","Ruhig hier, angenehm, nicht?","Quiet and peaceful here, isn't it?"),"{参拝客|さんぱいきゃく}","sanpaikyaku")])
OMI=L("おみくじ：「{大吉|だいきち}」！いいことがありそう。","omikuji: daikichi! ii koto ga arisō.","Omikuji: „großes Glück“! Klingt gut.","Omikuji: great blessing! Good things ahead.")
MUSEUM=dict(sp=[(1,1,L("{土器|どき}：{縄文時代|じょうもんじだい}のもの。","doki: jōmon-jidai no mono.","Tongefäß aus der Jōmon-Zeit.","Pottery from the Jōmon period.")),
 (5,1,L("{浮世絵|うきよえ}：{富士山|ふじさん}と{大|おお}きな{波|なみ}。","ukiyo-e: fujisan to ōkina nami.","Holzschnitt: Fuji und große Welle.","Woodblock print: Mt Fuji and a great wave.")),
 (3,4,L("{仏像|ぶつぞう}。{千年|せんねん}{以上前|いじょうまえ}のもの。","butsuzō. sennen ijō mae no mono.","Buddhastatue, über 1000 Jahre alt.","Buddha statue, over 1000 years old.")),
 (8,4,L("{恐竜|きょうりゅう}の{骨|ほね}！おおきい！","kyōryū no hone! ōkii!","Dinosaurierknochen! Riesig!","Dinosaur bones! Huge!"))],
 fl=[(6,6,"#2a2a2a","#2a5fc9",L("{写真|しゃしん}は だめですよ。","shashin wa dame desu yo.","Fotos sind nicht erlaubt.","No photos, please."),"{係員|かかりいん}","kakariin")])
CLOCK=dict(sp=[(1,1,L("{古|ふる}い{時計|とけい}の{歯車|はぐるま}。カチ、カチ…","furui tokei no haguruma. kachi kachi…","Zahnräder einer alten Uhr. Tick, tack…","Gears of an old clock. Tick, tock…")),
 (5,4,L("{札幌|さっぽろ}の{古|ふる}い{写真|しゃしん}。","sapporo no furui shashin.","Alte Fotos von Sapporo.","Old photos of Sapporo.")),(10,1,L("ストーブ。あたたかい！","sutōbu. atatakai!","Ein Ofen. Schön warm!","A stove. Nice and warm!"))],fl=[])
HUT=dict(sp=[(1,1,L("{登山|とざん}{地図|ちず}：{頂上|ちょうじょう}まで５{時間|じかん}。","tozan chizu: chōjō made go-jikan.","Wanderkarte: 5 Stunden bis zum Gipfel.","Trail map: 5 hours to the summit.")),
 (5,4,L("あたたかいうどんのにおい…","atatakai udon no nioi…","Duft von warmen Udon…","The smell of warm udon…")),(10,1,L("{金剛杖|こんごうづえ}に{焼印|やきいん}をおしてもらえる。","kongōzue ni yakiin o oshite moraeru.","Hier bekommt man einen Brandstempel auf den Wanderstab.","You can get your hiking stick branded here."))],
 fl=[(8,6,"#3a2a20","#d9502f",L("{日|ひ}の{出|で}を{見|み}に{行|い}くんだ！","hi no de o mi ni ikun da!","Ich will den Sonnenaufgang sehen!","I'm going to see the sunrise!"),"{登山客|とざんきゃく}","tozankyaku")])
NAMED={
'konbini':dict(sp=[(2,1,L("{冷|つめ}たい{飲|の}み{物|もの}：お{茶|ちゃ}、ジュース、{牛乳|ぎゅうにゅう}。","tsumetai nomimono: ocha, jūsu, gyūnyū.","Kalte Getränke: Tee, Saft, Milch.","Cold drinks: tea, juice, milk.")),
 (3,3,L("おにぎり：ツナマヨ、うめ、さけ。","onigiri: tsunamayo, ume, sake.","Onigiri: Thunfisch-Mayo, Pflaume, Lachs.","Onigiri: tuna mayo, plum, salmon.")),
 (6,3,L("お{弁当|べんとう}。「あたためますか？」","obentō. atatamemasu ka?","Bentō. „Soll ich es aufwärmen?“","Bentō. 'Shall I heat it up?'")),
 (3,4,L("お{菓子|かし}：ポッキー、おせんべい、グミ。","okashi: pokkī, osenbei, gumi.","Süßes: Pocky, Reiscracker, Gummis.","Snacks: Pocky, rice crackers, gummies.")),
 (6,4,L("{雑誌|ざっし}とマンガ。{立|た}ち{読|よ}みはだめ！","zasshi to manga. tachiyomi wa dame!","Zeitschriften und Manga. Kein Gratislesen!","Magazines and manga. No reading for free!")),
 (9,3,L("あったかいコーヒー １２０{円|えん}","attakai kōhī 120 en","Heißer Kaffee 120 Yen","Hot coffee 120 yen")),
 (9,4,L("ATMの{下|した}に１００{円|えん}{玉|だま}が{落|お}ちていた！","ATM no shita ni hyaku-en-dama ga ochite ita!","Unterm Automaten: 100 Yen gefunden!","Under the ATM: found a 100-yen coin!"),1),
 (1,6,L("レジ：「いらっしゃいませ！ポイントカードはお{持|も}ちですか？」","reji: irasshaimase! pointo kādo wa omochi desu ka?","Kasse: „Willkommen! Haben Sie eine Punktekarte?“","Register: 'Welcome! Do you have a point card?'"))],
 fl=[(7,6,"#1e1e24","#4f8fd6",L("{新|あたら}しいおにぎり、どれにしようかな…","atarashii onigiri, dore ni shiyō ka na…","Welches neue Onigiri nehm ich bloß…","Which new onigiri should I get…"),"お{客|きゃく}さん","okyakusan")]),
'ramen':dict(sp=[(2,2,L("{食券機|しょっけんき}：しょうゆラーメン ８００{円|えん}","shokkenki: shōyu rāmen 800 en","Ticketautomat: Shōyu-Ramen 800 Yen","Ticket machine: shōyu ramen 800 yen")),
 (8,2,L("スープの{鍋|なべ}。いいにおい！","sūpu no nabe. ii nioi!","Suppentopf. Riecht toll!","Soup pot. Smells great!")),
 (3,4,L("カウンター：はし、こしょう、にんにく。","kauntā: hashi, koshō, ninniku.","Theke: Stäbchen, Pfeffer, Knoblauch.","Counter: chopsticks, pepper, garlic.")),
 (8,6,L("テーブルの{下|した}に１０{円|えん}！","tēburu no shita ni jū-en!","Unterm Tisch: 10 Yen!","Under the table: 10 yen!"),1)],
 fl=[(5,5,"#555","#6b8f4a",L("ずるずる…おいしい！","zuruzuru… oishii!","Schlürf… lecker!","Slurp… delicious!"),"お{客|きゃく}さん","okyakusan")]),
'ryokan':dict(sp=[(2,2,L("{浴衣|ゆかた}がたたんである。","yukata ga tatande aru.","Ein gefalteter Yukata liegt bereit.","A folded yukata is ready.")),
 (3,2,L("お{茶|ちゃ}と{和菓子|わがし}。","ocha to wagashi.","Tee und japanische Süßigkeiten.","Tea and Japanese sweets.")),
 (5,1,L("{掛|か}け{軸|じく}：「{一期一会|いちごいちえ}」","kakejiku: ichigo ichie","Rollbild: „Einmalige Begegnung“","Hanging scroll: 'once in a lifetime'"))],
 fl=[(8,6,"#3a2a20","#7a5c99",L("{温泉|おんせん}、さいこうでした！","onsen, saikō deshita!","Das Onsen war super!","The hot spring was amazing!"),"お{客|きゃく}さん","okyakusan")]),
'ie':dict(sp=[(1,1,L("{仏壇|ぶつだん}。おばあちゃんの{写真|しゃしん}。","butsudan. obāchan no shashin.","Hausaltar mit Omas Foto.","Family altar with grandma's photo.")),
 (4,4,L("お{茶|ちゃ}とおせんべい。","ocha to osenbei.","Tee und Reiscracker.","Tea and rice crackers.")),
 (10,1,L("{棚|たな}の{上|うえ}に{古|ふる}いけん{玉|だま}。","tana no ue ni furui kendama.","Auf dem Regal ein altes Kendama.","An old kendama on the shelf."))],fl=[])}
GATE=dict(sp=[(2,3,L("{改札|かいさつ}：ICカードをタッチ。ピッ！","kaisatsu: IC kādo o tatchi. pi!","Ticketschranke: IC-Karte antippen. Piep!","Ticket gate: tap your IC card. Beep!")),
 (9,1,L("{路線図|ろせんず}：{山手線|やまのてせん}は{緑|みどり}。","rosenzu: Yamanote-sen wa midori.","Streckenplan: Die Yamanote-Linie ist grün.","Route map: the Yamanote Line is green.")),
 (1,1,L("ハチ{公|こう}の{写真|しゃしん}。「{待|ま}ち{合|あ}わせはハチ{公口|こうぐち}で」","Hachikō no shashin. machiawase wa Hachikō-guchi de.","Foto von Hachikō: „Treffpunkt am Hachikō-Ausgang.“","Photo of Hachikō: “Meet at the Hachikō exit.”")),
 (10,5,L("{切符|きっぷ}の{下|した}に１００{円|えん}！","kippu no shita ni hyaku-en!","Unter einem Ticket: 100 Yen!","Under a ticket: 100 yen!"),1)],
 fl=[(8,6,"#2b3448","#2b3448",L("いらっしゃいませ。{山手線|やまのてせん}は２{番線|ばんせん}です。","irasshaimase. Yamanote-sen wa ni-bansen desu.","Willkommen. Die Yamanote-Linie fährt von Gleis 2.","Welcome. The Yamanote Line is on track 2."),"{駅員|えきいん}","ekiin")])
FISH=dict(sp=[(2,3,L("{今日|きょう}のおすすめ：マグロ、サバ、イカ。","kyō no osusume: maguro, saba, ika.","Heute empfohlen: Thunfisch, Makrele, Tintenfisch.","Today's picks: tuna, mackerel, squid.")),(9,3,L("{氷|こおり}の{上|うえ}に{新鮮|しんせん}な{魚|さかな}。","kōri no ue ni shinsen na sakana.","Frischer Fisch auf Eis.","Fresh fish on ice."))],fl=[(5,5,"#2b2b33","#2f6f9a",L("いらっしゃい！サバ{一匹|いっぴき}３００{円|えん}だよ！","irasshai! saba ippiki sanbyaku-en da yo!","Willkommen! Eine Makrele 300 Yen!","Welcome! One mackerel, 300 yen!"),"{魚屋|さかなや}さん","sakanaya-san")])
KIND={'shibueki':GATE,'minka':HOME,'school':SCHOOL,'machiya':SHOP,'museum':MUSEUM,'clock':CLOCK,'hut':HUT,
 'shrine':SHR(OMI),'temple':SHR(L("{大|おお}きなお{香|こう}の{煙|けむり}。{頭|あたま}にかけるといいらしい。","ōkina okō no kemuri. atama ni kakeru to ii rashii.","Großer Räucherrauch – soll gut für den Kopf sein.","Incense smoke – said to make you smarter.")),
 'todaiji':SHR(L("{大仏|だいぶつ}さま：{高|たか}さ１５メートル！","daibutsu-sama: takasa jūgo mētoru!","Großer Buddha: 15 Meter hoch!","Great Buddha: 15 metres tall!")),
 'castle':SHR(L("{鎧|よろい}と{刀|かたな}の{展示|てんじ}。","yoroi to katana no tenji.","Ausstellung von Rüstungen und Schwertern.","Exhibition of armour and swords."))}
def apply(A):
  for a in A:
    if a.get('s')!='in':continue
    k=a['id'] if a['id'] in NAMED else None
    if not k and a.get('gen'):
      kind=a['id'].split('_',1)[1].rstrip('0123456789')
      d=KIND.get(kind)
    else: d=NAMED.get(k)
    if a['id'].startswith('odaiba_machiya'): d=FISH
    if not d: continue
    m=a['m'];sp=[];fl=[]
    for s in d['sp']:
      x,y=s[0],s[1]
      if m[y][x] in 'fctW' or m[y][x]=='D': continue
      sp.append([x,y,s[2],1 if len(s)>3 else 0])
    for i,f in enumerate(d['fl']):
      x,y=f[0],f[1]
      if m[y][x] not in 'fct' or any(n[1]==x and n[2]==y for n in a['npc']) or any(t[1]==x and t[2]==y for t in a.get('it',[])): continue
      fl.append([f"fl_{a['id']}_{i}",x,y,f[2],f[3],f[4],f[5],f[6]])
    a['sp']=sp;a['fl']=fl
