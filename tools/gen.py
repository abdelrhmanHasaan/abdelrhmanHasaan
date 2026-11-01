import html, math, random
random.seed(7)
FONT = "'Segoe UI',Ubuntu,'Helvetica Neue',Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"
esc = html.escape

# ---------------- HERO ----------------
def hero():
    W,H = 900,300
    lines = ["I turn LLMs into things that actually ship",
             "Multi-agent pipelines with critic-led hallucination audits",
             "Local 4-bit LLMs, multi-provider failover, real-time voice AI",
             "Ship the model. Then make it boring."]
    nodes = [(random.randint(40,860), random.randint(30,270)) for _ in range(26)]
    edges = []
    for i,a in enumerate(nodes):
        for j,b in enumerate(nodes):
            if j>i and math.dist(a,b) < 120: edges.append((a,b))
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Abdelrahman Hassan — AI Engineer">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#0b1020"><animate attributeName="stop-color" values="#0b1020;#120d2b;#08202b;#0b1020" dur="14s" repeatCount="indefinite"/></stop>
<stop offset="1" stop-color="#101828"><animate attributeName="stop-color" values="#101828;#1a1038;#0c2a33;#101828" dur="14s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="txt" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#38bdf8"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#f472b6"/>
<animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0;-1 0" dur="8s" repeatCount="indefinite"/>
</linearGradient>
<radialGradient id="glow"><stop offset="0" stop-color="#a78bfa" stop-opacity=".35"/><stop offset="1" stop-color="#a78bfa" stop-opacity="0"/></radialGradient>
<clipPath id="c"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#c)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<circle cx="150" cy="60" r="160" fill="url(#glow)"><animate attributeName="cx" values="150;700;150" dur="18s" repeatCount="indefinite"/></circle>
<circle cx="760" cy="250" r="140" fill="#38bdf8" opacity=".10"><animate attributeName="cy" values="250;60;250" dur="12s" repeatCount="indefinite"/></circle>
<g transform="translate(450,150) rotate(-8)" fill="none">
<ellipse rx="400" ry="105" stroke="#a78bfa" stroke-opacity=".22" stroke-dasharray="3 9"/>
<ellipse rx="310" ry="66" stroke="#38bdf8" stroke-opacity=".2" stroke-dasharray="3 9"/>
<circle r="5.5" fill="#38bdf8"><animateMotion dur="11s" repeatCount="indefinite" path="M-400 0 a400 105 0 1 1 800 0 a400 105 0 1 1 -800 0"/></circle>
<circle r="4.5" fill="#f472b6"><animateMotion dur="8s" repeatCount="indefinite" path="M310 0 a310 66 0 1 1 -620 0 a310 66 0 1 1 620 0"/></circle>
</g>
<g stroke="#7c8cff" stroke-width="1">'''
    for k,(a,b) in enumerate(edges):
        s += f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" opacity=".15"><animate attributeName="opacity" values=".06;.4;.06" dur="{3+k%5}s" begin="{(k%7)*0.4}s" repeatCount="indefinite"/></line>'
    s += '</g>'
    for k,(x,y) in enumerate(nodes):
        s += f'<circle cx="{x}" cy="{y}" r="2.6" fill="#c4b5fd"><animate attributeName="r" values="2;4;2" dur="{2.5+k%4}s" begin="{k*0.2}s" repeatCount="indefinite"/><animate attributeName="opacity" values=".4;1;.4" dur="{2.5+k%4}s" begin="{k*0.2}s" repeatCount="indefinite"/></circle>'
    s += f'''
<text x="{W/2}" y="104" text-anchor="middle" font-family="{FONT}" font-size="54" font-weight="800" fill="url(#txt)" letter-spacing="1">Abdelrahman Hassan</text>
<text x="{W/2}" y="140" text-anchor="middle" font-family="{MONO}" font-size="15" fill="#94a3b8" letter-spacing="6">AI ENGINEER  ·  LLM  ·  RAG  ·  AGENTIC SYSTEMS</text>
'''
    for i,t in enumerate(lines):
        st = i*0.25
        pts = [(0,0),(st,0),(st+.03,1),(st+.22,1),(st+.25,0),(1,0)]
        d = {}
        for kt,v in pts: d[round(min(kt,1),4)] = v
        kts = sorted(d); kt = ";".join(str(k) for k in kts); vs = ";".join(str(d[k]) for k in kts)
        s += f'<text x="{W/2}" y="208" text-anchor="middle" font-family="{FONT}" font-size="24" font-weight="600" fill="#e2e8f0" opacity="0">{esc(t)}<animate attributeName="opacity" values="{vs}" keyTimes="{kt}" dur="16s" repeatCount="indefinite"/></text>\n'
    s += f'''<rect x="{W/2-60}" y="232" width="120" height="3" rx="1.5" fill="#a78bfa"><animate attributeName="width" values="0;260;0" dur="4s" repeatCount="indefinite"/><animate attributeName="x" values="{W/2};{W/2-130};{W/2}" dur="4s" repeatCount="indefinite"/></rect>
<text x="{W/2}" y="272" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#64748b">B.Sc. AI @ Helwan University  ◆  Giza, Egypt  ◆  3.5 yrs building LLM systems</text>
</g></svg>'''
    open('../assets/hero.svg','w',encoding='utf-8').write(s)

# ---------------- CARDS ----------------
cards = [
 ("JobFidner","AI career assistant","CV parsing · job-match scoring 0–100","Tailored .docx CVs · cold emails · any LLM",["FastAPI","React","LiteLLM"],3,"#38bdf8"),
 ("ResearchMultiAgentSystem","5-agent research platform","Query in → sourced PDF/Markdown report out.","100% local (~6 GB VRAM) · critic-led audits",["LangGraph","ChromaDB","Ollama"],3,"#a78bfa"),
 ("SchemaForge v2","AI database architect","Figma-style PostgreSQL designer + AI architect","Drag ERDs · review AI cards · 1-click deploy",["React 19","FastAPI","PostgreSQL"],3,"#34d399"),
 ("ReplayLens","Flight recorder for AI agents","Record runs, replay them, and diff behaviour","(tools · meaning · cost) to catch regressions",["Python SDK","Redis","React"],1,"#fb923c"),
 ("wa-agent-sdk","WhatsApp AI agents, your number","Smart provider router, human-like batching,","anti-ban safety, tools, memory, campaigns",["Python","Baileys","Ollama"],1,"#4ade80"),
 ("DevMate","Production-grade coding agent","ReAct loop · policy layers · human approval ·","Lua token-bucket limiter · 3-tier memory",["FastAPI","Redis Lua","pgvector"],1,"#f472b6"),
]
def card(i,c):
    name,sub,l1,l2,tags,stars,col = c
    W,H = 430,178
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(name)}">
<defs>
<linearGradient id="g{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0f172a"/><stop offset="1" stop-color="#111827"/></linearGradient>
<linearGradient id="b{i}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{col}"/><stop offset=".5" stop-color="#ffffff" stop-opacity=".9"/><stop offset="1" stop-color="{col}"/>
<animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0" dur="3.5s" repeatCount="indefinite"/></linearGradient>
<clipPath id="k{i}"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14"/></clipPath>
</defs>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#g{i})" stroke="url(#b{i})" stroke-width="1.6"/>
<g clip-path="url(#k{i})">
<rect x="-80" y="-10" width="50" height="{H+20}" fill="#fff" opacity=".05" transform="skewX(-20)"><animate attributeName="x" values="-120;{W+60}" dur="5s" begin="{i*0.6}s" repeatCount="indefinite"/></rect>
<circle cx="{W-30}" cy="30" r="70" fill="{col}" opacity=".10"><animate attributeName="r" values="60;85;60" dur="5s" repeatCount="indefinite"/></circle>
<rect x="0" y="0" width="5" height="{H}" fill="{col}"/>
</g>
<circle cx="28" cy="34" r="5" fill="{col}"><animate attributeName="opacity" values="1;.25;1" dur="1.8s" repeatCount="indefinite"/></circle>
<text x="42" y="40" font-family="{FONT}" font-size="19" font-weight="700" fill="#f1f5f9">{esc(name)}</text>
<text x="26" y="64" font-family="{FONT}" font-size="12.5" font-weight="600" fill="{col}" letter-spacing=".5">{esc(sub.upper())}</text>
<text x="26" y="92" font-family="{FONT}" font-size="13" fill="#cbd5e1">{esc(l1)}</text>
<text x="26" y="111" font-family="{FONT}" font-size="13" fill="#cbd5e1">{esc(l2)}</text>
'''
    x = 26
    for t in tags:
        w = len(t)*7.2+18
        s += f'<rect x="{x}" y="132" width="{w:.0f}" height="24" rx="12" fill="{col}" opacity=".14"/><text x="{x+w/2:.0f}" y="148" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="{col}">{esc(t)}</text>'
        x += w+8
    s += f'<text x="{W-24}" y="148" text-anchor="end" font-family="{FONT}" font-size="13" fill="#facc15">★ {stars}</text></svg>'
    open(f'../assets/card-{i+1}.svg','w',encoding='utf-8').write(s)

# ---------------- PIPELINE ----------------
def pipeline():
    W,H = 900,230
    names = ["Planner","Scraper","Analyzer","Writer","Critic"]
    subs = ["keyword clusters","parallel crawl","dedupe · chunk · embed","RAG drafting","hallucination guard"]
    cols = ["#38bdf8","#818cf8","#a78bfa","#f472b6","#fb923c"]
    xs = [90,270,450,630,810]; y=96
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Five agent research pipeline with critic revision loop">
<rect width="{W}" height="{H}" rx="16" fill="#0b1020"/>
<text x="{W/2}" y="30" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="700" fill="#94a3b8" letter-spacing="3">RESEARCHMULTIAGENTSYSTEM · LIVE PIPELINE</text>
<path id="main" d="M{xs[0]} {y} L{xs[4]} {y}" stroke="#334155" stroke-width="2" stroke-dasharray="5 6"><animate attributeName="stroke-dashoffset" values="0;-22" dur="1s" repeatCount="indefinite"/></path>
<path id="loop" d="M{xs[4]} {y+36} C{xs[4]} 200 {xs[3]} 200 {xs[3]} {y+36}" fill="none" stroke="#fb923c" stroke-width="2" stroke-dasharray="5 5"><animate attributeName="stroke-dashoffset" values="0;-20" dur="1s" repeatCount="indefinite"/></path>
<text x="30" y="214" font-family="{MONO}" font-size="11.5" fill="#64748b">LangGraph · Llama 3.1 8B · Q4_K_M 4-bit · no external API</text>
<text x="{(xs[3]+xs[4])/2}" y="214" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="#fb923c">score &lt; 7 → revise with feedback</text>
'''
    s += f'''<circle r="7" fill="#fff" opacity=".95"><animate attributeName="cx" values="{xs[0]};{xs[1]};{xs[2]};{xs[3]};{xs[4]}" dur="5s" repeatCount="indefinite"/><animate attributeName="cy" values="{y};{y};{y};{y};{y}" dur="5s" repeatCount="indefinite"/><animate attributeName="fill" values="{';'.join(cols)}" dur="5s" repeatCount="indefinite"/></circle>
<circle r="5" fill="#fb923c"><animateMotion dur="2.5s" begin="0s" repeatCount="indefinite" path="M{xs[4]} {y+36} C{xs[4]} 200 {xs[3]} 200 {xs[3]} {y+36}"/><animate attributeName="opacity" values="0;1;1;0" dur="2.5s" repeatCount="indefinite"/></circle>'''
    for i,(n,sb,c,x) in enumerate(zip(names,subs,cols,xs)):
        s += f'''<g><rect x="{x-62}" y="{y-34}" width="124" height="68" rx="14" fill="#111a33" stroke="{c}" stroke-width="1.6"/>
<rect x="{x-62}" y="{y-34}" width="124" height="68" rx="14" fill="{c}" opacity="0"><animate attributeName="opacity" values="0;.22;0;0;0;0;0;0;0;0" dur="10s" begin="{i*1.0}s" repeatCount="indefinite"/></rect>
<text x="{x}" y="{y-4}" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="700" fill="#f1f5f9">{i+1}. {n}</text>
<text x="{x}" y="{y+16}" text-anchor="middle" font-family="{FONT}" font-size="10.5" fill="#94a3b8">{esc(sb)}</text></g>'''
    s += '</svg>'
    open('../assets/pipeline.svg','w',encoding='utf-8').write(s)

# ---------------- MARQUEE ----------------
def marquee():
    items = ["LangGraph","RAG","LoRA","Ollama","PyTorch","HuggingFace","FastAPI","LiteLLM","React","PostgreSQL","pgvector","Redis","Docker","Multi-Agent","Quantized LLMs","STT → LLM → TTS"]
    cols = ["#38bdf8","#a78bfa","#f472b6","#fb923c","#34d399","#facc15"]
    W,H = 900,56
    x=0; chips=""
    for i,t in enumerate(items):
        w = len(t)*9+36; c = cols[i%len(cols)]
        chips += f'<g transform="translate({x},10)"><rect width="{w}" height="36" rx="18" fill="{c}" opacity=".13" stroke="{c}" stroke-opacity=".6"/><text x="{w/2}" y="23" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{c}">{esc(t)}</text></g>'
        x += w+14
    total = x
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Tech stack">

<g><animateTransform attributeName="transform" type="translate" from="0 0" to="-{total} 0" dur="38s" repeatCount="indefinite"/>
{chips}<g transform="translate({total},0)">{chips}</g></g></svg>'''
    open('../assets/marquee.svg','w',encoding='utf-8').write(s)

hero()
for i,c in enumerate(cards): card(i,c)
pipeline(); marquee()
print("ok")
