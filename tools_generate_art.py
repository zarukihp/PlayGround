from pathlib import Path
import cairosvg, math
ROOT=Path(__file__).parent
BG=ROOT/'renpy_project/game/images/bg'; CH=ROOT/'renpy_project/game/images/chars'; CG=ROOT/'renpy_project/game/images/cg'; WEB=ROOT/'assets/images'
for p in (BG,CH,CG,WEB): p.mkdir(parents=True,exist_ok=True)
# Original illustrated environments: layered gradients, architectural silhouettes, rain and light.
scenes={
'alley':('Callejón de los faroles','#10172d','#714b70','rain'),
'university':('Universidad Arco Norte','#18304b','#b88e79','campus'),
'police':('Comisaría central','#1d2639','#748398','office'),
'apartment':('Habitación 604','#1c1934','#745178','window'),
'tv':('Estudio Prisma','#211a3a','#b97886','studio'),
'rooftop':('Azotea del distrito','#1b2944','#bd7180','rooftop'),
'cafe':('Cafetería Nube','#263348','#d8a876','cafe'),
'interrogation':('Sala de interrogatorio 3','#151d31','#667993','room'),
}
def bg_svg(key,title,c1,c2,kind):
    extra=''
    if kind=='rain':
        extra='<path d="M0 500 L1280 460 1280 720 0 720Z" fill="#17182a"/><path d="M0 610 L1280 570" stroke="#b6c4df" opacity=".18" stroke-width="3"/><g opacity=".35" stroke="#a9bfe5" stroke-width="2">'+''.join(f'<path d="M{x} 80 l-55 130"/>' for x in range(50,1300,95))+'</g><g fill="#f2bd76">'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" opacity=".7"/>' for x,y,r in [(190,320,26),(480,265,14),(1020,350,34),(1160,210,11)])+'</g>'
    elif kind=='campus':
        extra='<path d="M0 520 L1280 500 1280 720 0 720Z" fill="#344454"/><path d="M120 275 L640 115 1160 275Z" fill="#28344c"/><rect x="170" y="275" width="940" height="280" fill="#425267"/><path d="M150 275h980" stroke="#dfb38c" stroke-width="10"/><g fill="#202b42">'+''.join(f'<rect x="{x}" y="{y}" width="105" height="110" rx="8"/>' for x in range(220,1080,180) for y in (325,445))+'</g><g fill="#f8d39b" opacity=".6">'+''.join(f'<rect x="{x}" y="{y}" width="88" height="90"/>' for x in range(228,1080,180) for y in (334,454))+'</g>'
    elif kind=='office':
        extra='<rect y="570" width="1280" height="150" fill="#252c3e"/><path d="M80 160h1120v430H80Z" fill="#27364c" stroke="#7c879d" stroke-width="5"/><g fill="#172437" stroke="#8391aa" stroke-width="4">'+''.join(f'<rect x="{x}" y="210" width="190" height="145"/>' for x in (125,350,575,800,1025))+'</g><g fill="#9eb2c7" opacity=".3">'+''.join(f'<path d="M{x} 215v135" stroke="#d5deeb" stroke-width="3"/>' for x in (220,445,670,895,1120))+'</g><rect x="420" y="460" width="440" height="175" rx="10" fill="#684d46"/><rect x="450" y="480" width="380" height="120" fill="#a16f57"/>'
    elif kind=='window':
        extra='<rect x="760" y="80" width="400" height="430" fill="#1c3150" stroke="#d0bed6" stroke-width="12"/><path d="M960 80v430M760 295h400" stroke="#d0bed6" stroke-width="8"/><g fill="#f5cb83">'+''.join(f'<rect x="{x}" y="{y}" width="18" height="34" opacity="{op}"/>' for x,y,op in [(800,150,.8),(900,190,.4),(1040,130,.65),(1090,355,.7),(825,365,.35)])+'</g><rect y="570" width="1280" height="150" fill="#271e35"/><path d="M160 580h420v20H160Z" fill="#bb8d71"/>'
    elif kind=='studio':
        extra='<rect y="560" width="1280" height="160" fill="#1a1830"/><path d="M110 100h1060v430H110Z" fill="#2a2344" stroke="#ed8ca2" stroke-width="5"/><g fill="#f08ba2" opacity=".75">'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x,y,r in [(185,160,20),(1080,190,30),(250,460,13),(1030,420,17)])+'</g><path d="M370 520 Q640 410 910 520v60H370Z" fill="#68455d"/><rect x="470" y="365" width="340" height="140" rx="18" fill="#d67491"/>'
    elif kind=='rooftop':
        extra='<path d="M0 460h1280v260H0Z" fill="#20283d"/><path d="M0 300 L230 180 380 295 600 100 840 290 1010 160 1280 320v200H0Z" fill="#293954"/><g fill="#f8c783">'+''.join(f'<rect x="{x}" y="{y}" width="17" height="30" opacity=".72"/>' for x,y in [(100,360),(275,330),(425,380),(620,230),(700,290),(880,350),(1050,250),(1150,400)])+'</g><path d="M0 530h1280" stroke="#d18393" stroke-width="5" opacity=".65"/>'
    elif kind=='cafe':
        extra='<rect y="490" width="1280" height="230" fill="#62463f"/><path d="M95 105h1090v370H95Z" fill="#33485c"/><g stroke="#e1bd92" stroke-width="7">'+''.join(f'<path d="M{x} 110v360"/>' for x in (350,620,890))+'</g><g fill="#f6d69d" opacity=".55">'+''.join(f'<rect x="{x}" y="135" width="210" height="300"/>' for x in (120,375,645,915))+'</g><path d="M270 525h740v40H270Z" fill="#b27c5b"/><path d="M360 565v155m550-155v155" stroke="#49363c" stroke-width="24"/>'
    else:
        extra='<rect x="85" y="90" width="1110" height="540" rx="22" fill="#202a3f" stroke="#8190a7" stroke-width="6"/><rect x="180" y="180" width="920" height="315" fill="#10192a"/><circle cx="640" cy="335" r="120" fill="#687890" opacity=".12"/><rect x="520" y="565" width="240" height="35" fill="#b8c5d5"/><path d="M560 600v120m160-120v120" stroke="#9ca9bb" stroke-width="12"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720"><defs><linearGradient id="g" x2="0" y2="1"><stop stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient><radialGradient id="glow"><stop stop-color="#f3bb91" stop-opacity=".42"/><stop offset="1" stop-color="#f3bb91" stop-opacity="0"/></radialGradient></defs><rect width="1280" height="720" fill="url(#g)"/><ellipse cx="690" cy="255" rx="540" ry="360" fill="url(#glow)"/>{extra}<path d="M0 700 Q300 665 650 700 T1280 690" stroke="#efd4c0" opacity=".12" fill="none" stroke-width="5"/><text x="45" y="65" fill="#fff" opacity=".18" font-family="sans-serif" font-size="20" letter-spacing="7">{title.upper()}</text></svg>'''
for name,(title,c1,c2,kind) in scenes.items():
    svg=bg_svg(name,title,c1,c2,kind)
    for dest in [BG/f'{name}.png',WEB/f'bg_{name}.png']:
        cairosvg.svg2png(bytestring=svg.encode(),write_to=str(dest),output_width=1280,output_height=720)

# Static anime-inspired portraits, transparent, expression variants are separate still files.
people={
'noa':('#202641','#293c69','#e9b08d','#15213b','#75d2e8','Noa'),
'iris':('#30344a','#152331','#f0c4a4','#202637','#afd7e7','Iris'),
'nera':('#211b35','#412645','#d9a38e','#171326','#de9dc2','Nera'),
'vela':('#d486a4','#8e456d','#f3c7ac','#49334d','#8ce3dc','Vela'),
'chief':('#303947','#5a463f','#dea98c','#252a36','#e9c58f','Ciro'),
}
expressions=['neutral','smile','tense','anger','fear','surprise','sad','suspicious']
def char_svg(name,palette,exp):
    hair,coat,skin,hair2,eye,label=palette
    mouth={'neutral':'M270 410 Q300 415 330 410','smile':'M268 405 Q300 440 334 405','tense':'M270 418 Q300 405 332 418','anger':'M270 414 Q300 394 334 414','fear':'M278 412 Q300 429 322 412','surprise':'M282 410 Q300 431 318 410','sad':'M270 426 Q300 395 334 426','suspicious':'M270 415 Q298 406 330 419'}[exp]
    brow={'neutral':'M220 288l58 6m42 0 58-6','smile':'M220 291l58 4m42 4 58-4','tense':'M220 305l58-14m42-2 58 16','anger':'M220 311l58-20m42 0 58 20','fear':'M220 278l58 10m42 0 58-10','surprise':'M220 270l58 8m42 0 58-8','sad':'M220 284l58 12m42-2 58-12','suspicious':'M220 300l58-9m42 2 58 9'}[exp]
    eyes='<ellipse cx="258" cy="338" rx="21" ry="27" fill="#fff"/><ellipse cx="342" cy="338" rx="21" ry="27" fill="#fff"/><ellipse cx="258" cy="342" rx="12" ry="18" fill="'+eye+'"/><ellipse cx="342" cy="342" rx="12" ry="18" fill="'+eye+'"/><circle cx="262" cy="338" r="5" fill="#fff"/><circle cx="346" cy="338" r="5" fill="#fff"/>'
    if name=='nera':
        hairshape='<path d="M176 340 Q135 90 300 62 Q490 75 430 360 L402 238 388 462 350 284 300 474 267 278 225 452 214 250Z" fill="'+hair+'" stroke="#131522" stroke-width="10"/><path d="M188 163Q300 72 420 166L383 210Q302 163 212 210Z" fill="'+hair2+'" opacity=".65"/>'
    elif name=='vela':
        hairshape='<path d="M177 340 Q145 100 300 65 Q455 90 423 360L400 236 385 420 355 277 317 441 275 274 230 425 214 245Z" fill="'+hair+'" stroke="#57344e" stroke-width="10"/><path d="M204 185Q290 70 395 180" fill="none" stroke="#ffd4e5" stroke-width="16" opacity=".8"/>'
    else:
        hairshape='<path d="M176 340 Q145 91 300 61 Q455 73 424 355 L400 236 383 439 350 277 315 452 275 270 230 421 214 245Z" fill="'+hair+'" stroke="#111827" stroke-width="10"/><path d="M193 196Q260 99 385 152" fill="none" stroke="'+hair2+'" stroke-width="13" opacity=".75"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="900" viewBox="0 0 600 900"><g stroke-linejoin="round"><path d="M65 900Q90 605 215 555L300 525 385 555Q520 610 545 900Z" fill="{coat}" stroke="#111725" stroke-width="12"/><path d="M230 570l70 145 70-145-70-48Z" fill="#eee3db"/><path d="M266 640l34 45 34-45-34-48Z" fill="#d88d9c"/><path d="M235 192Q300 132 365 192V402Q365 470 300 480Q235 470 235 402Z" fill="{skin}" stroke="#201c2b" stroke-width="9"/><path d="M229 380Q192 343 207 280M370 380Q407 343 392 280" fill="none" stroke="#201c2b" stroke-width="11"/>{hairshape}<path d="{brow}" stroke="#3b2932" stroke-width="9" stroke-linecap="round" fill="none"/>{eyes}<path d="M300 346l-9 37 15 2" stroke="#b87972" stroke-width="5" fill="none"/><path d="{mouth}" stroke="#8c4c58" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M204 392Q220 496 300 510Q380 496 396 392V435Q380 515 300 528Q220 515 204 435Z" fill="{hair}" opacity=".96"/><path d="M225 278Q250 250 277 270M323 270Q355 246 380 276" fill="none" stroke="{hair}" stroke-width="25" stroke-linecap="round"/><path d="M244 355q-9 7-18 0m149 0q-9 7-18 0" stroke="#bf7277" stroke-width="4" opacity=".55"/></g><text x="300" y="860" text-anchor="middle" fill="#ffffff" opacity=".55" font-family="sans-serif" font-size="18" letter-spacing="6">{label.upper()} · {exp.upper()}</text></svg>'''
for name,palette in people.items():
    for exp in expressions:
        svg=char_svg(name,palette,exp)
        for dest in [CH/f'{name}_{exp}.png',WEB/f'{name}_{exp}.png']:
            cairosvg.svg2png(bytestring=svg.encode(),write_to=str(dest),output_width=600,output_height=900)
# Key still CGs: stylized composite panels with character-shaped silhouette implied by moonlit profile.
for key,bgname,caption,accent in [('discovery','alley','LA PRIMERA PÁGINA','#edc784'),('revelation','rooftop','EL NOMBRE QUE FALTA','#d68ea4'),('lastpage','apartment','NINGUNA TINTA ES ETERNA','#80d7d1')]:
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720"><image href="../bg/{bgname}.png" width="1280" height="720"/><rect width="1280" height="720" fill="#101421" opacity=".27"/><path d="M655 720Q675 450 780 370Q732 218 844 135Q958 65 1040 182Q1102 276 1040 377Q1170 440 1208 720Z" fill="#121728" stroke="{accent}" stroke-opacity=".6" stroke-width="5"/><path d="M785 328Q850 247 961 304" fill="none" stroke="{accent}" stroke-width="6" opacity=".75"/><rect x="90" y="500" width="490" height="5" fill="{accent}" opacity=".8"/><text x="90" y="570" font-family="sans-serif" font-size="22" letter-spacing="8" fill="{accent}">CHRONICLE OF ASH</text><text x="90" y="625" font-family="sans-serif" font-size="40" letter-spacing="6" fill="#fff">{caption}</text></svg>'''
    # Replace relative external image with embedded data URI.
    source=(BG/f'{bgname}.png').read_bytes(); import base64
    uri='data:image/png;base64,'+base64.b64encode(source).decode()
    svg=svg.replace(f'../bg/{bgname}.png',uri)
    cairosvg.svg2png(bytestring=svg.encode(),write_to=str(CG/f'{key}.png'),output_width=1280,output_height=720)
    cairosvg.svg2png(bytestring=svg.encode(),write_to=str(WEB/f'cg_{key}.png'),output_width=1280,output_height=720)
print('Art generated: 8 backgrounds, 40 static expressions, 3 CGs')
