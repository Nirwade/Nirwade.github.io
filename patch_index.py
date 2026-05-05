"""
patch_index.py
Run from your project root (where index.html lives):
    python patch_index.py

Makes three targeted changes to index.html:
  1. Tech stack subtitle — new text
  2. Run section — shorter setup steps
  3. CTA block — adds PDF download button next to Request a demo
"""

from pathlib import Path

f = Path("index.html")
if not f.exists():
    print("ERROR: index.html not found. Run this from your project root.")
    exit(1)

content = f.read_text()
original = content
changes = []

# ── 1. TECH STACK SUBTITLE ─────────────────────────────────────
OLD_TS = '<h2 class="display">All open source.<br><em>Fully local.</em></h2>\n  <p class="section-sub">End-to-end retail AI with zero external dependencies. Local inference, local data, local everything.</p>'

NEW_TS = '<h2 class="display">Built on open-source tools.<br><em>Designed for production.</em></h2>\n  <p class="section-sub">LightGBM demand forecasting, Random Forest phantom detection, LLaMA 3.2 language interface, and a 10-page Streamlit dashboard — all running on a single machine with no cloud dependencies.</p>'

if OLD_TS in content:
    content = content.replace(OLD_TS, NEW_TS)
    changes.append("Tech stack subtitle updated")
else:
    print("WARN: tech stack subtitle pattern not found — skipping")

# ── 2. SHORTER SETUP STEPS ─────────────────────────────────────
OLD_RUN = '''  <h2 class="display">From zero to running<br>in <em>five commands.</em></h2>

  <div class="two-col">
    <div>
      <h3 style="font-size:16px;font-weight:700;margin-bottom:16px">1 — Clone and set up</h3>
      <div class="code-block">
        <div class="cm"># Clone the repository</div>
        <div class="cmd">git clone https://github.com/Nirwade/HyperShefl_Retail-AI-project</div>
        <div class="cmd">cd retail-ai-project</div>
        <div style="height:10px"></div>
        <div class="cm"># Create conda environment</div>
        <div class="cmd">conda create -n retail-ai python=3.10</div>
        <div class="cmd">conda activate retail-ai</div>
        <div class="cmd">pip install -r requirements.txt</div>
        <div style="height:10px"></div>
        <div class="cm"># Set up sample data so dashboard boots immediately</div>
        <div class="hl">python scripts/setup_sample_data.py</div>
        <div style="height:10px"></div>
        <div class="cm"># Install Ollama and pull the model</div>
        <div class="cmd">brew install ollama</div>
        <div class="hl">ollama pull llama3.2:3b</div>
        <div class="hl">ollama serve</div>
      </div>
    </div>
    <div>
      <h3 style="font-size:16px;font-weight:700;margin-bottom:16px">2 — Launch both interfaces</h3>
      <div class="code-block">
        <div class="cm"># 10-page AI dashboard</div>
        <div class="hl">python -m streamlit run streamlit_app/app.py \\</div>
        <div class="hl">  --server.port 8511</div>
        <div style="height:12px"></div>
        <div class="cm"># Standalone conversational AI</div>
        <div class="hl">python -m streamlit run streamlit_app/llm_chat.py \\</div>
        <div class="hl">  --server.port 8501</div>
        <div style="height:12px"></div>
        <div class="cm"># Regenerate analytics layer (optional)</div>
        <div class="cmd">python src/analytics.py</div>
        <div class="cmd">python src/pipeline.py</div>
      </div>
      <div class="port-row">
        <div class="port"><div class="port-title">Dashboard</div><div class="port-url">localhost:8511</div><div class="port-desc">10 pages · AI per page · live alerts</div></div>
        <div class="port"><div class="port-title">AI Chat</div><div class="port-url">localhost:8501</div><div class="port-desc">8 tools · conversational · morning briefing</div></div>
      </div>
    </div>
  </div>'''

NEW_RUN = '''  <h2 class="display">Clone. Install.<br><em>Run.</em></h2>

  <div class="two-col">
    <div>
      <h3 style="font-size:16px;font-weight:700;margin-bottom:16px">Setup</h3>
      <div class="code-block">
        <div class="hl">git clone https://github.com/Nirwade/HyperShelf_Retail-AI-project</div>
        <div class="cmd">cd HyperShelf_Retail-AI-project</div>
        <div style="height:8px"></div>
        <div class="cmd">conda create -n retail-ai python=3.10</div>
        <div class="cmd">conda activate retail-ai</div>
        <div class="cmd">pip install -r requirements.txt</div>
        <div style="height:8px"></div>
        <div class="hl">python scripts/setup_sample_data.py</div>
        <div style="height:8px"></div>
        <div class="cmd">ollama pull llama3.2:3b &amp;&amp; ollama serve</div>
      </div>
    </div>
    <div>
      <h3 style="font-size:16px;font-weight:700;margin-bottom:16px">Launch</h3>
      <div class="code-block">
        <div class="cm"># Dashboard — 10 pages with AI</div>
        <div class="hl">python -m streamlit run streamlit_app/app.py --server.port 8511</div>
        <div style="height:10px"></div>
        <div class="cm"># Standalone AI chat</div>
        <div class="hl">python -m streamlit run streamlit_app/llm_chat.py --server.port 8501</div>
      </div>
      <div class="port-row">
        <div class="port"><div class="port-title">Dashboard</div><div class="port-url">localhost:8511</div><div class="port-desc">10 pages · AI per page · live alerts</div></div>
        <div class="port"><div class="port-title">AI Chat</div><div class="port-url">localhost:8501</div><div class="port-desc">8 tools · conversational · morning briefing</div></div>
      </div>
    </div>
  </div>'''

if OLD_RUN in content:
    content = content.replace(OLD_RUN, NEW_RUN)
    changes.append("Setup steps shortened")
else:
    print("WARN: run section pattern not found — skipping")

# ── 3. CTA BLOCK — add PDF button next to demo button ──────────
PDF_ID = "1kjMY1-n3ypg3aj90gEZbuxcInV5fZKrL"
PDF_URL = f"https://drive.google.com/file/d/{PDF_ID}/view?usp=sharing"

OLD_CTA = '''  <div class="cta-block">
    <div class="cta-text"><h3>Want to see it live?</h3><p>The full system requires the processed data files and Ollama running locally. Request a demo session to walk through all 10 pages and both AI interfaces with real retail data.</p></div>
    <a class="cta-btn" href="mailto:?subject=HyperShelf DemandSense v2 — Demo Request">Request a demo →</a>
  </div>'''

NEW_CTA = f'''  <div class="cta-block">
    <div class="cta-text"><h3>Want to see it live?</h3><p>Request a demo session to walk through all 10 pages and both AI interfaces. Or download the full project book for the complete methodology.</p></div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;">
      <a class="cta-btn" href="mailto:?subject=HyperShelf DemandSense v2 — Demo Request">Request a demo →</a>
      <a class="cta-btn" href="{PDF_URL}" target="_blank" rel="noopener" style="border-color:var(--amber);color:var(--amber);">Project Book ↓</a>
    </div>
  </div>'''

if OLD_CTA in content:
    content = content.replace(OLD_CTA, NEW_CTA)
    changes.append("PDF download button added to CTA block")
else:
    print("WARN: CTA block pattern not found — skipping")
    # Try to find it
    cta_idx = content.find('cta-block')
    # find the closing div
    idx = content.find('<div class="cta-block">', cta_idx+100)
    print(f"  CTA div found at: {idx}")
    print(f"  Context: {repr(content[idx:idx+300])}")

# ── SAVE ───────────────────────────────────────────────────────
if changes:
    f.write_text(content)
    print("\nDone. Changes applied:")
    for c in changes:
        print(f"  + {c}")
    print(f"\nTotal: {len(changes)}/3 changes applied")
    if len(changes) < 3:
        print("Run again and check WARN messages above for any skipped patches.")
else:
    print("No changes applied. Check WARN messages above.")