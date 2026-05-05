"""
patch_index_v2.py
Run from your project root:
    python patch_index_v2.py

Adds a Project Information block just above the footer.
"""
from pathlib import Path

f = Path("index.html")
if not f.exists():
    print("ERROR: index.html not found.")
    exit(1)

content = f.read_text()

PROJECT_INFO_HTML = '''
<section style="background:var(--bg2);padding:56px 48px;border-top:1px solid var(--border);">
  <div class="section-eyebrow">Project information</div>
  <h2 class="display" style="font-size:clamp(28px,4vw,44px);margin-bottom:32px">Version 1 &amp; 2 — <em>All Access Links</em></h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;">

    <div>
      <div style="font-family:\'IBM Plex Mono\',monospace;font-size:10px;color:var(--gray);letter-spacing:0.12em;text-transform:uppercase;margin-bottom:12px;">Version 1 — Original Team Dashboard</div>
      <div style="display:flex;flex-direction:column;gap:8px;">
        <div style="background:var(--bg);border:1px solid var(--border);border-left:3px solid var(--gray);padding:12px 16px;">
          <div style="font-size:10px;color:var(--gray);font-family:\'IBM Plex Mono\',monospace;margin-bottom:3px;">DASHBOARD URL</div>
          <div style="font-family:\'IBM Plex Mono\',monospace;font-size:12px;color:var(--white);">http://localhost:8050</div>
          <div style="font-size:11px;color:var(--gray);margin-top:3px;">Requires app_dashboard.py to be running</div>
        </div>
        <div style="background:var(--bg);border:1px solid var(--border);border-left:3px solid var(--gray);padding:12px 16px;">
          <div style="font-size:10px;color:var(--gray);font-family:\'IBM Plex Mono\',monospace;margin-bottom:3px;">CODE REPOSITORY</div>
          <div style="font-family:\'IBM Plex Mono\',monospace;font-size:12px;color:var(--white);">GitHub — HyperShelf</div>
          <div style="font-size:11px;color:var(--gray);margin-top:3px;">Private repository — team access required</div>
        </div>
        <div style="background:var(--bg);border:1px solid var(--border);border-left:3px solid var(--gray);padding:12px 16px;">
          <div style="font-size:10px;color:var(--gray);font-family:\'IBM Plex Mono\',monospace;margin-bottom:3px;">DOCUMENT VERSION</div>
          <div style="font-family:\'IBM Plex Mono\',monospace;font-size:12px;color:var(--white);">Version 1.0 Final — April 2026</div>
        </div>
      </div>
    </div>

    <div>
      <div style="font-family:\'IBM Plex Mono\',monospace;font-size:10px;color:var(--teal2);letter-spacing:0.12em;text-transform:uppercase;margin-bottom:12px;">Version 2 — DemandSense v2 (This Project)</div>
      <div style="display:flex;flex-direction:column;gap:8px;">
        <div style="background:var(--bg);border:1px solid var(--border);border-left:3px solid var(--teal);padding:12px 16px;">
          <div style="font-size:10px;color:var(--teal2);font-family:\'IBM Plex Mono\',monospace;margin-bottom:3px;">PORTFOLIO WEBSITE</div>
          <a href="https://nirwade.github.io" style="font-family:\'IBM Plex Mono\',monospace;font-size:12px;color:var(--teal2);text-decoration:none;">nirwade.github.io</a>
          <div style="font-size:11px;color:var(--gray);margin-top:3px;">Live — interactive showcase with demos</div>
        </div>
        <div style="background:var(--bg);border:1px solid var(--border);border-left:3px solid var(--teal);padding:12px 16px;">
          <div style="font-size:10px;color:var(--teal2);font-family:\'IBM Plex Mono\',monospace;margin-bottom:3px;">DASHBOARD URL</div>
          <div style="font-family:\'IBM Plex Mono\',monospace;font-size:12px;color:var(--white);">http://localhost:8511</div>
          <div style="font-size:11px;color:var(--gray);margin-top:3px;">10-page AI dashboard — requires Streamlit and data files</div>
        </div>
        <div style="background:var(--bg);border:1px solid var(--border);border-left:3px solid var(--teal);padding:12px 16px;">
          <div style="font-size:10px;color:var(--teal2);font-family:\'IBM Plex Mono\',monospace;margin-bottom:3px;">CODE REPOSITORY</div>
          <a href="https://github.com/Nirwade/HyperShelf_Retail-AI-project" style="font-family:\'IBM Plex Mono\',monospace;font-size:12px;color:var(--teal2);text-decoration:none;">github.com/Nirwade/HyperShelf_Retail-AI-project</a>
          <div style="font-size:11px;color:var(--gray);margin-top:3px;">Public — full source code with README and sample data</div>
        </div>
        <div style="background:var(--bg);border:1px solid var(--border);border-left:3px solid var(--teal);padding:12px 16px;">
          <div style="font-size:10px;color:var(--teal2);font-family:\'IBM Plex Mono\',monospace;margin-bottom:3px;">DOCUMENT VERSION</div>
          <div style="font-family:\'IBM Plex Mono\',monospace;font-size:12px;color:var(--white);">Version 2.0 Final — May 2026</div>
          <div style="font-size:11px;color:var(--gray);margin-top:3px;">Nexus Team 2 · University at Buffalo · Globant AI Studios</div>
        </div>
      </div>
    </div>

  </div>
</section>

'''

TARGET = '\n<footer>'
if TARGET in content:
    content = content.replace(TARGET, PROJECT_INFO_HTML + '<footer>', 1)
    f.write_text(content)
    print("Done — Project Information block added just above footer.")
else:
    print("ERROR: Could not find footer tag. No changes made.")
