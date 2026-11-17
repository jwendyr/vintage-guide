import sys,os;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from setara import S as SETARA
#!/usr/bin/env python3
"""Regenerate dist/ from ../items.json (+ ../img). Uses only data present; no invented items."""
import json, shutil, pathlib, re
from PIL import Image
H=pathlib.Path(__file__).resolve().parent; V=H.parent
items=[]
if (V/'items.json').exists():
    d=json.load(open(V/'items.json')); items=d.get('items',d) if isinstance(d,dict) else d
items=[dict(i) for i in items if isinstance(i,dict)]
out=H/'dist'
if out.exists(): shutil.rmtree(out)
(out/'img'/'t').mkdir(parents=True)
def put(f,dst,mx=1200,tn=True):
    """copy f into dist dir dst, resized to mx; also make 300px thumb in dist/img/t. returns (main,thumb) names"""
    nm=f.stem+'.jpg' if f.suffix.lower() not in ('.jpg','.jpeg','.webp') else f.name
    try:
        im=Image.open(f); im.load()
        if im.mode not in ('RGB','L'): im=im.convert('RGB')
        if max(im.size)>mx: im.thumbnail((mx,mx))
        im.save(dst/nm,quality=84,optimize=True)
        if tn:
            t=im.copy(); t.thumbnail((300,300)); t.save(out/'img'/'t'/nm,quality=80)
    except Exception as ex:
        print('img err',f,ex); shutil.copy2(f,dst/f.name); nm=f.name
    return nm

for i in items:
  for k in ('top_sale_image','iconic_image'):
    p=i.get(k)
    if p and not str(p).startswith('http'):
        f=pathlib.Path(p); f=f if f.is_absolute() else V/f
        if f.exists(): nm=put(f,out/'img'); i[k]='/img/'+nm; i[k+'_t']='/img/t/'+nm
        else: i.pop(k); print('missing image',f)
  for t in i.get('spot_tips') or []:
    f=pathlib.Path(t.get('image') or '')
    if t.get('image') and f.exists(): nm=put(f,out/'img'); t['image']='/img/t/'+nm
    elif t.get('image'): print('missing spot',f); t.pop('image')
combos=json.load(open(V/'combos.json')) if (V/'combos.json').exists() else []
(out/'img'/'combos').mkdir(exist_ok=True)
for c in combos:
    f=V/c.get('image','')
    if c.get('image') and f.is_file(): nm=put(f,out/'img'/'combos',1600,False); c['image']='/img/combos/'+nm
    else: c.pop('image',None)

BYI={i['id']:i for i in items}
def num(x):
    try: return float(x)
    except: return None
for c in combos:
    rows=[];tt=tn=tn_cmp=tt_cmp=0;gaps=[]
    for id in c.get('items',[]):
        i=BYI.get(id)
        if not i: continue
        rec=str(i.get('rec') or '');nb=rec.lower().startswith('beli baru')
        ne=num(i.get('new_equiv'));tp=num(i.get('target_price'))
        basis='baru';nv=ne
        if nv is None and id in SETARA: nv=SETARA[id][1];basis='setara baru'
        if nv is None and num(i.get('replica_price')) is not None: nv=num(i.get('replica_price'));basis='replika'
        if nv is None and (num(i.get('price_low')) or num(i.get('price_high'))): nv=num(i.get('price_low')) or num(i.get('price_high'));basis='pasar'
        th=(ne if ne is not None else tp) if nb else tp
        if th is None: gaps.append(i.get('name'))
        if nv is None: gaps.append(i.get('name')+' (harga baru)')
        rows.append({'id':id,'name':i.get('name'),'mode':'Beli baru' if nb else 'Thrift','thrift':th,'new':nv,'basis':basis})
        if th is not None: tt+=th
        if nv is not None: tn+=nv
        if th is not None and nv is not None: tt_cmp+=th; tn_cmp+=nv
    am=[];amt=0
    for a in c.get('amenities') or []:
        m=re.search(r'(±)?\$\s?([\d,]+(?:\.\d+)?)',a)
        v=float(m.group(2).replace(',','')) if m else None
        am.append({'t':re.sub(r'\s*\(±?\$[^)]*\)','',a),'v':v,'est':bool(m and m.group(1))})
        amt+=v or 0
    sm=[(BYI[x].get('name'),num(BYI[x].get('new_equiv')) or num(BYI[x].get('price_low'))) for x in c.get('smart') or [] if x in BYI]
    c['price']={'rows':rows,'thrift':round(tt),'new':round(tn),'save':round(100*(1-tt_cmp/tn_cmp)) if tn_cmp else None,
      'amen':round(amt),'amen_n':len(am),'amen_est':any(a['est'] for a in am),'amen_rows':am,'smart':round(sum(v or 0 for _,v in sm)),'smart_n':len(sm),'gaps':gaps}
data=json.dumps(items,ensure_ascii=False).replace('</','<\\/')
html=(H/'template.html').read_text().replace('__CSS__',(H/'review-base.css').read_text()).replace('__DATA__',data).replace('__COMBOS__',json.dumps(combos,ensure_ascii=False).replace('</','<\\/')).replace('__COUNT__',str(len(items)))
(out/'index.html').write_text(html)
(out/'_headers').write_text("/img/*\n  Cache-Control: public, max-age=604800\n")
print(f"built dist/ with {len(items)} items, {len(list((out/'img').iterdir()))} images")

# --- Total per rumah (Nov 2026) ---
FAM={'Craftsman Terang':'Craftsman','Craftsman × MCM':'Craftsman'}
def pick(fam,room,tier):
    cs=[c for c in combos if FAM.get(c.get('profile'),c.get('profile'))==fam and c['room']==room and c['tier']==tier]
    cs.sort(key=lambda c:0 if c.get('profile')=='Craftsman Terang' else 1)
    return cs[0] if cs else None
TIERS=['hemat','menengah','premium']
def house(fam,bd,ba):
    rooms=['Ruang Tamu','Ruang Makan','Dapur']+['Kamar Mandi']*ba
    if bd>=2: rooms+=['Ruang Kerja']+['Kamar Tidur']*(bd-1)
    else: rooms+=['Kamar Tidur']*bd
    out={};miss=set()
    for t in TIERS:
        s=0
        for r in rooms:
            c=pick(fam,r,t)
            if not c: miss.add(f'{r} ({t})');continue
            s+=c['price']['thrift']+c['price']['amen']
        out[t]=s
    return out,sorted(miss)
STD=[('2 kamar / 1 KM',2,1),('3 kamar / 1 KM',3,1),('3 kamar / 2 KM',3,2),('4 kamar / 2 KM',4,2)]
REAL=json.load(open(V/'house-counts.json')) if (V/'house-counts.json').exists() else []
def row(lbl,bd,ba):
    v,m=house('Craftsman',bd,ba)
    return f"<tr><td>{lbl}</td>"+''.join(f"<td>${v[t]:,}</td>" for t in TIERS)+"</tr>"
HT=('<section id="rumah" class="cbx" style="margin:12px 0"><h2 class="sh">🏠 Total per rumah</h2>'
 '<p class="cbi">Estimasi isi satu rumah untuk 2 orang (gaya Craftsman). Kamar 1 = Ruang Kerja; tiap rumah punya Ruang Tamu, Ruang Makan, Dapur, Kamar Mandi sesuai jumlahnya, sisanya Kamar Tidur. Total = harga target thrift/beli baru per kombo + amenities (sebagian estimasi). Belum termasuk Entry, hardware, smart home, ongkir & pajak.</p>'
 '<div style="overflow-x:auto"><table style="border-collapse:collapse;width:100%;font-size:14px"><thead><tr><th style="text-align:left">Rumah</th><th>Hemat</th><th>Menengah</th><th>Premium</th></tr></thead><tbody>'
 +''.join(row(l,b,a) for l,b,a in STD)
 +''.join(row(f"{r['label']} ({r['bd']}bd/{r['ba']}ba{' estimasi' if r.get('est') else ''})"+(f" <small>{r['note']}</small>" if r.get('note') else ''),r['bd'],r['ba']) for r in REAL)
 +'</tbody></table></div><p class="cbi" style="font-size:12px">Profil Ralph Lauren & Hollywood Regency belum lengkap per ruangan, jadi belum dihitung per rumah.</p></section>')
p=out/'index.html';p.write_text(p.read_text().replace('<section id="cmb">',HT+'<section id="cmb">',1))
json.dump({'std':{l:house('Craftsman',b,a) for l,b,a in STD},'real':[dict(r,tot=house('Craftsman',r['bd'],r['ba'])) for r in REAL],
 'rl':house('Alfredo Paredes / Ralph Lauren',3,1),'hr':house('Hollywood Regency',3,1)},open(H/'house-totals.json','w'),ensure_ascii=False,indent=1)
