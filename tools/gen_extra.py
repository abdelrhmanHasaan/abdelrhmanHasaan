import html, random
random.seed(11)
esc=html.escape
FONT = "'Segoe UI',Ubuntu,'Helvetica Neue',Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"

def dedupe(pts):
    d={}
    for k,v in pts: d[round(min(k,1),4)]=v
    ks=sorted(d); return ";".join(str(k) for k in ks), ";".join(str(d[k]) for k in ks)

# ---------- terminal ----------
def terminal():
    W,H=900,250
    lines=[("$ ","whoami","#e2e8f0",True),
           ("→ ","Abdelrahman Hassan · AI Engineer · Giza, Egypt","#38bdf8",False),
           ("$ ","cat stack.txt","#e2e8f0",True),
           ("→ ","LangGraph · RAG · FastAPI · Redis · PostgreSQL · Ollama","#a78bfa",False),
           ("$ ","./status.sh","#e2e8f0",True),
           ("● ","open to freelance & full-time AI roles","#4ade80",False)]
    cw=8.6; dur=18
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Terminal intro">
<defs><linearGradient id="tb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0a0f1e"/><stop offset="1" stop-color="#111827"/></linearGradient>
<linearGradient id="tl" x1="0" x2="1"><stop offset="0" stop-color="#38bdf8"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#f472b6"/><animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0" dur="5s" repeatCount="indefinite"/></linearGradient></defs>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#tb)" stroke="url(#tl)" stroke-width="1.6"/>
<circle cx="26" cy="24" r="6" fill="#ff5f56"/><circle cx="46" cy="24" r="6" fill="#ffbd2e"/><circle cx="66" cy="24" r="6" fill="#27c93f"/>
<text x="{W/2}" y="28" text-anchor="middle" font-family="{MONO}" font-size="12" fill="#64748b">abdelrahman@ai-engineer: ~</text>
<line x1="1" y1="42" x2="{W-1}" y2="42" stroke="#1e293b"/>
'''
    y=74; start=0.02
    per=[len(a)+len(b) for a,b,_,_ in lines]
    cur_t=start
    for i,(pre,txt,col,cmd) in enumerate(lines):
        n=per[i]; d=(0.030 if cmd else 0.022)*(n/20)+0.02
        d=min(d,0.09)
        t0=cur_t; t1=t0+d
        pts=[(0,0),(t0,0)]
        for k in range(1,n+1): pts.append((t0+(t1-t0)*k/n, round(k*cw+4,1)))
        pts.append((0.95,0)); pts.append((1,0))
        kts,vs=dedupe(pts)
        cur_t=t1+0.03
        s+=f'''<clipPath id="cl{i}"><rect x="24" y="{y-18}" width="0" height="26"><animate attributeName="width" values="{vs}" keyTimes="{kts}" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/></rect></clipPath>
<text x="24" y="{y}" font-family="{MONO}" font-size="14.5" clip-path="url(#cl{i})"><tspan fill="#4ade80">{esc(pre)}</tspan><tspan fill="{col}">{esc(txt)}</tspan></text>
'''
        y+=26 if cmd else 36
    last_y=74+26*3+36*3-36+0
    tf=cur_t-0.03
    pts=[(0,0),(tf,0)]; t=tf; v=1
    while t<0.94:
        pts.append((t,v)); t+=0.025; v=1-v
    pts+= [(0.95,0),(1,0)]
    kts,vs=dedupe(pts)
    cx=24+per[-1]*cw+8
    s+=f'<rect x="{cx:.0f}" y="{last_y-14}" width="9" height="18" fill="#e2e8f0" opacity="0"><animate attributeName="opacity" values="{vs}" keyTimes="{kts}" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/></rect>'
    s+="</svg>"
    # place cursor after last line roughly
    open('../assets/terminal.svg','w',encoding='utf-8').write(s)

# ---------- stats counters ----------
def stats():
    W,H=900,130
    tiles=[("3.5","",["0","1","2","3","3.5"],"YEARS BUILDING AI","#38bdf8"),
           ("6","",["0","1","2","3","4","5","6"],"FLAGSHIP PROJECTS","#a78bfa"),
           ("110","+",["0","20","40","60","80","100","110"],"AUTOMATED TESTS","#34d399"),
           ("13","",["0","3","6","9","11","13"],"LLM PROVIDERS WIRED","#f472b6")]
    tw=204; gap=(W-4*tw)/3
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Key numbers">'
    dur=9
    for i,(val,suf,frames,label,col) in enumerate(tiles):
        x=i*(tw+gap); n=len(frames); seg=0.07
        s+=f'''<g transform="translate({x:.0f},0)"><rect x="1" y="1" width="{tw-2}" height="{H-2}" rx="14" fill="#0f172a" stroke="{col}" stroke-opacity=".7" stroke-width="1.5"/>
<circle cx="52" cy="58" r="30" fill="none" stroke="{col}" stroke-opacity=".15" stroke-width="6"/>
<circle cx="52" cy="58" r="30" fill="none" stroke="{col}" stroke-width="6" stroke-linecap="round" transform="rotate(-90 52 58)" stroke-dasharray="0 189"><animate attributeName="stroke-dasharray" values="0 189;189 189;189 189;0 189" keyTimes="0;.45;.93;1" dur="{dur}s" repeatCount="indefinite"/></circle>
'''
        for j,f in enumerate(frames):
            b=[j*seg for _ in range(1)][0]; nxt=(j+1)*seg if j<n-1 else 0.94
            pts=[(0,0),(b,0),(b,1),(nxt,0),(1,0)]
            if j==0: pts=[(0,1),(nxt,0),(1,0)]
            kts,vs=dedupe(pts)
            s+=f'<text x="98" y="68" font-family="{FONT}" font-size="38" font-weight="800" fill="{col}" opacity="0">{f}{suf if j==n-1 else ""}<animate attributeName="opacity" values="{vs}" keyTimes="{kts}" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/></text>'
        s+=f'<text x="{tw/2}" y="112" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="#94a3b8" letter-spacing="1.2">{label}</text></g>'
    s+='</svg>'
    open('../assets/stats.svg','w',encoding='utf-8').write(s)

# ---------- timeline ----------
def timeline():
    W,H=900,330
    cols=[("APR – DEC 2023","LLM Engineer","Product MasterZ · Contract",["LoRA fine-tuning on curated datasets","Models served via REST APIs","Prompt optimisation + evaluation"],"#38bdf8"),
          ("FEB 2024 → PRESENT","AI Engineer · Freelance","Healthcare · Travel · Education · SaaS",["LangGraph + RAG multi-agent systems","Local 4-bit LLMs + provider failover","FastAPI · Redis Lua · Oracle Cloud"],"#a78bfa"),
          ("IN PROGRESS","B.Sc. Artificial Intelligence","Helwan University · Cairo",["ML · Deep Learning · NLP · Vision","LLMs · Cloud · Databases","IBM AI/ML + NVIDIA certified"],"#f472b6")]
    cwid=280; xs=[20,310,600]
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Experience timeline">
<path d="M40 52 H860" stroke="#1e293b" stroke-width="4" stroke-linecap="round"/>
<path d="M40 52 H860" stroke="url(#tg)" stroke-width="4" stroke-linecap="round" stroke-dasharray="820" stroke-dashoffset="820"><animate attributeName="stroke-dashoffset" values="820;0;0;820" keyTimes="0;.18;.92;1" dur="14s" repeatCount="indefinite"/></path>
<defs><linearGradient id="tg" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="860" y2="0"><stop offset="0" stop-color="#38bdf8"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#f472b6"/></linearGradient></defs>
'''
    for i,(when,role,org,bul,c) in enumerate(cols):
        x=xs[i]; cx=x+cwid/2; d=0.04+i*0.1
        def pop(vals_op,begin_f): 
            return kt(begin_f)
        def kt(b): 
            pts=[(0,0),(b,0),(b+0.05,1),(0.92,1),(0.97,0),(1,0)]; return dedupe(pts)
        kts,op=kt(d+0.08)
        s+=f'''<g><circle cx="{cx}" cy="52" r="11" fill="#0b1020" stroke="{c}" stroke-width="3" opacity="0"><animate attributeName="opacity" values="{op}" keyTimes="{kts}" dur="14s" repeatCount="indefinite"/></circle>
<circle cx="{cx}" cy="52" r="11" fill="none" stroke="{c}" stroke-width="2" opacity="0"><animate attributeName="r" values="11;26" dur="2.4s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0" dur="2.4s" repeatCount="indefinite"/></circle>
<g opacity="0"><animate attributeName="opacity" values="{op}" keyTimes="{kts}" dur="14s" repeatCount="indefinite"/>
<animateTransform attributeName="transform" type="translate" values="0 18;0 18;0 0;0 0;0 0" keyTimes="0;{max(d+0.08-0.0001,0):.4f};{d+0.15:.4f};.92;1" dur="14s" repeatCount="indefinite"/>
<rect x="{x}" y="88" width="{cwid}" height="226" rx="14" fill="#0f172a" stroke="{c}" stroke-opacity=".75" stroke-width="1.5"/>
<rect x="{x}" y="88" width="{cwid}" height="5" rx="2.5" fill="{c}"/>
<text x="{x+18}" y="122" font-family="{MONO}" font-size="12" fill="{c}" letter-spacing="1.5">{esc(when)}</text>
<text x="{x+18}" y="152" font-family="{FONT}" font-size="19" font-weight="700" fill="#f1f5f9">{esc(role)}</text>
<text x="{x+18}" y="174" font-family="{FONT}" font-size="12.5" fill="#94a3b8">{esc(org)}</text>
<line x1="{x+18}" y1="190" x2="{x+cwid-18}" y2="190" stroke="#1e293b"/>
'''
        for k,b in enumerate(bul):
            yy=218+k*30
            s+=f'<circle cx="{x+24}" cy="{yy-4}" r="3.2" fill="{c}"/><text x="{x+38}" y="{yy}" font-family="{FONT}" font-size="12.5" fill="#cbd5e1">{esc(b)}</text>'
        s+='</g></g>'
    s+='</svg>'
    open('../assets/timeline.svg','w',encoding='utf-8').write(s)

# ---------- voice tutor ----------
def voice():
    W,H=900,230
    names=[("Whisper STT","speech → text","#38bdf8"),("13B LLM · 4-bit","streaming tokens","#a78bfa"),("RAG","course knowledge","#34d399"),("TTS","text → speech","#fb923c"),("React + avatar","live audio stream","#f472b6")]
    xs=[90,270,450,630,810]; y=92
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Real-time Arabic AI voice tutor pipeline">
<rect width="{W}" height="{H}" rx="16" fill="#0b1020"/>
<text x="30" y="32" font-family="{FONT}" font-size="14" font-weight="700" fill="#94a3b8" letter-spacing="3">REAL-TIME ARABIC AI VOICE TUTOR · FULL-DUPLEX · FULLY LOCAL</text>
<rect x="{W-146}" y="16" width="116" height="24" rx="12" fill="#fb923c" opacity=".16"/><circle cx="{W-130}" cy="28" r="4" fill="#fb923c"><animate attributeName="opacity" values="1;.2;1" dur="1.4s" repeatCount="indefinite"/></circle>
<text x="{W-120}" y="32" font-family="{MONO}" font-size="11" fill="#fb923c">IN PROGRESS</text>
<path d="M{xs[0]} {y} L{xs[4]} {y}" stroke="#334155" stroke-width="2" stroke-dasharray="5 6"><animate attributeName="stroke-dashoffset" values="0;-22" dur="1s" repeatCount="indefinite"/></path>
<circle r="6" fill="#fff"><animate attributeName="cx" values="{xs[0]};{xs[1]};{xs[2]};{xs[3]};{xs[4]}" dur="4.5s" repeatCount="indefinite"/><animate attributeName="cy" values="{y};{y};{y};{y};{y}" dur="4.5s" repeatCount="indefinite"/><animate attributeName="fill" values="{';'.join(n[2] for n in names)}" dur="4.5s" repeatCount="indefinite"/></circle>
<circle r="6" fill="#fff" opacity=".7"><animate attributeName="cx" values="{xs[4]};{xs[3]};{xs[2]};{xs[1]};{xs[0]}" dur="4.5s" begin="2.2s" repeatCount="indefinite"/><animate attributeName="cy" values="{y+44};{y+44};{y+44};{y+44};{y+44}" dur="4.5s" begin="2.2s" repeatCount="indefinite"/></circle>
<path d="M{xs[0]} {y+44} L{xs[4]} {y+44}" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="3 7"/>
'''
    for i,(n,sub,c) in enumerate(names):
        x=xs[i]
        s+=f'''<rect x="{x-66}" y="{y-34}" width="132" height="68" rx="14" fill="#111a33" stroke="{c}" stroke-width="1.6"/>
<text x="{x}" y="{y-4}" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="700" fill="#f1f5f9">{esc(n)}</text>
<text x="{x}" y="{y+16}" text-anchor="middle" font-family="{FONT}" font-size="10.5" fill="#94a3b8">{esc(sub)}</text>'''
    # equalizer
    base=212; n=60; x0=60; step=(W-120)/n
    for k in range(n):
        h=[random.randint(6,34) for _ in range(5)]; h.append(h[0])
        dur=round(random.uniform(.7,1.6),2)
        col=["#38bdf8","#a78bfa","#f472b6"][k*3//n]
        ys=";".join(str(base-v) for v in h); hs=";".join(str(v) for v in h)
        s+=f'<rect x="{x0+k*step:.1f}" y="{base-h[0]}" width="{step*0.55:.1f}" height="{h[0]}" rx="2" fill="{col}" opacity=".85"><animate attributeName="y" values="{ys}" dur="{dur}s" repeatCount="indefinite"/><animate attributeName="height" values="{hs}" dur="{dur}s" repeatCount="indefinite"/></rect>'
    s+='</svg>'
    open('../assets/voice.svg','w',encoding='utf-8').write(s)

# ---------- skills ----------
def skills():
    W=900
    cats=[("AGENTIC AI & LLMs","#a78bfa",["LangGraph","LangChain","RAG","Tool Calling","Structured Outputs","LoRA","Ollama · GGUF","LLM Routing & Failover","Hallucination Audits"]),
          ("BACKEND & APIs","#38bdf8",["FastAPI","Flask","Node / Express","REST","WebSockets","SSE","Celery","JWT"]),
          ("DATA & STORAGE","#34d399",["PostgreSQL","Redis (Lua)","SQLAlchemy","Alembic","FAISS","ChromaDB","Pinecone","Pandas"]),
          ("FRONTEND & TESTING","#f472b6",["React","Next.js","TypeScript","Playwright","Bruno"]),
          ("DEVOPS & ML","#fb923c",["Docker","Linux","Oracle Cloud","PyTorch","TensorFlow","scikit-learn","Transformers"])]
    body=""; y=14; idx=0
    for name,c,items in cats:
        body+=f'<text x="20" y="{y+19}" font-family="{MONO}" font-size="11.5" fill="{c}" letter-spacing="1.5">{esc(name)}</text>'
        x=200; ry=y
        for it in items:
            w=len(it)*7.3+24
            if x+w>W-10: x=200; ry+=38
            dly=idx*0.12; idx+=1
            body+=f'''<g transform="translate({x:.0f},{ry})" opacity="0"><animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{min(dly/16,.5):.3f};{min(dly/16+.04,.54):.3f};1" dur="16s" repeatCount="indefinite"/>
<rect width="{w:.0f}" height="28" rx="14" fill="{c}" opacity=".13" stroke="{c}" stroke-opacity=".55"/>
<rect width="{w:.0f}" height="28" rx="14" fill="{c}" opacity="0"><animate attributeName="opacity" values="0;.28;0;0" keyTimes="0;.04;.1;1" dur="{4+idx%5}s" begin="{(idx%9)*0.5}s" repeatCount="indefinite"/></rect>
<text x="{w/2:.0f}" y="19" text-anchor="middle" font-family="{FONT}" font-size="12.5" fill="{c}">{esc(it)}</text></g>'''
            x+=w+8
        y=ry+54
    H=y
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Technical skills">{body}</svg>'
    open('../assets/skills.svg','w',encoding='utf-8').write(s)

# ---------- divider ----------
def divider():
    W=900
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="26" viewBox="0 0 {W} 26"><defs><linearGradient id="d" x1="0" x2="1"><stop offset="0" stop-color="#38bdf8" stop-opacity="0"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#f472b6" stop-opacity="0"/></linearGradient>
<radialGradient id="g"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#a78bfa" stop-opacity="0"/></radialGradient></defs>
<rect x="0" y="12" width="{W}" height="2" fill="url(#d)"/>
<circle r="9" cy="13" fill="url(#g)"><animate attributeName="cx" values="0;{W};0" dur="7s" repeatCount="indefinite"/></circle>
<g transform="translate({W/2},13)"><rect x="-5" y="-5" width="10" height="10" fill="#a78bfa" transform="rotate(45)"><animateTransform attributeName="transform" type="rotate" values="45;405" dur="6s" repeatCount="indefinite"/></rect></g></svg>'''
    open('../assets/divider.svg','w',encoding='utf-8').write(s)

terminal(); stats(); timeline(); voice(); skills(); divider()
print("extra ok")
