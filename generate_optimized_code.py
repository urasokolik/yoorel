import re

YADISK_TOKEN = 'y0__wgBENifibMHGPSXTyCN697bGe2931gbhKuY-LYTbVLSkQayxVIy'

# Read index.html
with open('c:/Work/index.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# Remove the mock alert openOrderModalWithFormat from index.html
base_html = re.sub(
    r'// Modal Trigger Simulation.*?const startBtn = document\.getElementById\(\'heroStartBtn\'\);.*?</script>',
    '</script>',
    base_html,
    flags=re.DOTALL
)

# 1. Update font in .spread-name and carousel styles in base_html
old_spread_name_css = """.spread-name {
      font-family: "Cormorant Garamond", serif;
      font-size: 20px;
      font-weight: 700;
      color: var(--accent-dark);
    }"""

new_spread_name_css = """.spread-name {
      font-family: -apple-system, BlinkMacSystemFont, "Plus Jakarta Sans", "SF Pro Text", sans-serif;
      font-size: 16.5px;
      font-weight: 600;
      letter-spacing: -0.01em;
      color: var(--text-primary);
    }"""

if old_spread_name_css in base_html:
    base_html = base_html.replace(old_spread_name_css, new_spread_name_css)
    print("Replaced .spread-name CSS")
else:
    print("Warning: old_spread_name_css not found")

# Replace spread tag CSS
old_spread_tag_css = """.spread-tag {
      font-size: 12px;
      font-weight: 600;
      color: var(--accent-warm);
      background: var(--accent-subtle);
      padding: 4px 10px;
      border-radius: var(--radius-full);
    }"""

new_spread_tag_css = """.spread-tag {
      font-size: 12px;
      font-weight: 500;
      color: #8a4827;
      background: rgba(184, 98, 59, 0.08);
      border: 1px solid rgba(184, 98, 59, 0.16);
      padding: 3px 9px;
      border-radius: 6px;
      white-space: nowrap;
    }"""

if old_spread_tag_css in base_html:
    base_html = base_html.replace(old_spread_tag_css, new_spread_tag_css)
    print("Replaced .spread-tag CSS")

# Add GPU optimization and controls to carousel
old_track_css = """.spreads-track {
      display: flex;
      gap: 24px;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      padding: 20px 8px 40px;
      scrollbar-width: none;
      -ms-overflow-style: none;
    }"""

new_track_css = """.spreads-slider-wrap {
      max-width: 1240px;
      margin: 0 auto;
      position: relative;
    }

    .spreads-track {
      display: flex;
      gap: 24px;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      padding: 20px 8px 30px;
      scrollbar-width: none;
      -ms-overflow-style: none;
      -webkit-overflow-scrolling: touch;
      scroll-behavior: smooth;
      will-change: scroll-position;
      transform: translateZ(0);
    }

    .spread-card {
      flex: 0 0 clamp(320px, 45vw, 540px);
      scroll-snap-align: center;
      background: var(--bg-surface);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-medium);
      box-shadow: 0 6px 20px rgba(35, 25, 20, 0.06);
      overflow: hidden;
      position: relative;
      will-change: transform;
      transform: translateZ(0);
      transition: transform 0.25s var(--ease-spring), box-shadow 0.25s ease, border-color 0.25s ease;
    }

    .spread-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 32px rgba(35, 25, 20, 0.1);
      border-color: var(--border-accent);
    }

    .spread-img-wrap {
      position: relative;
      width: 100%;
      height: 340px;
      background: #eae2d7;
      overflow: hidden;
    }

    /* Subtle spine crease simulating physical book center */
    .spread-img-wrap::after {
      content: "";
      position: absolute;
      top: 0; bottom: 0; left: 49%; width: 2%;
      background: linear-gradient(to right, transparent, rgba(0, 0, 0, 0.08) 50%, transparent);
      pointer-events: none;
    }

    .spread-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    /* Carousel navigation controls */
    .spreads-controls {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 16px;
      margin-top: 10px;
    }

    .spread-nav-btn {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #ffffff;
      border: 1px solid rgba(60, 45, 35, 0.14);
      box-shadow: 0 2px 8px rgba(35, 25, 20, 0.06);
      color: #3d322a;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .spread-nav-btn:hover {
      background: #fbf8f5;
      border-color: var(--accent-warm);
      color: var(--accent-warm);
      transform: scale(1.05);
    }

    .spread-nav-btn:active {
      transform: scale(0.95);
    }"""

if old_track_css in base_html:
    base_html = base_html.replace(old_track_css, new_track_css)
    print("Replaced spreads track & card CSS")

# Replace img markup in cards to include .spread-img-wrap
base_html = re.sub(
    r'<div class="spread-card">\s*<img src="([^"]+)" alt="([^"]+)" class="spread-img">',
    r'<div class="spread-card">\n            <div class="spread-img-wrap"><img src="\1" alt="\2" class="spread-img"></div>',
    base_html
)

# Insert carousel controls into spreads-slider-wrap
old_spreads_closing = """        </div>
      </div>
    </section>

    <!-- THE 4-STEP PROCESS"""

new_spreads_closing = """        </div>

        <div class="spreads-controls">
          <button type="button" class="spread-nav-btn" id="spreadPrevBtn" aria-label="Предыдущий разворот">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
          </button>
          <button type="button" class="spread-nav-btn" id="spreadNextBtn" aria-label="Следующий разворот">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>
          </button>
        </div>
      </div>
    </section>

    <!-- THE 4-STEP PROCESS"""

if old_spreads_closing in base_html:
    base_html = base_html.replace(old_spreads_closing, new_spreads_closing)
    print("Added carousel navigation buttons")

# Add Tilda Cart Icon styling fix
cart_fix_css = """
    /* -------------------------------------------------------------
       TILDA ST100 CART ICON REFINEMENT & SIZING FIX
       ------------------------------------------------------------- */
    .t706__carticon-img {
      box-sizing: content-box !important;
      stroke: #2a211b !important;
      display: block !important;
      margin: 0 auto !important;
    }
    .t706__carticon-img path {
      stroke: #2a211b !important;
      stroke-width: 2.2px !important;
    }
    .t706__carticon-imgwrap {
      background: rgba(255, 255, 255, 0.95) !important;
      backdrop-filter: blur(20px) !important;
      -webkit-backdrop-filter: blur(20px) !important;
      border: 1px solid rgba(60, 45, 35, 0.12) !important;
      box-shadow: 0 10px 30px rgba(35, 25, 20, 0.15) !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .t706__carticon-imgwrap:hover {
      transform: scale(1.08) !important;
    }
    .t706__carticon-counter {
      background-color: #b8623b !important;
      color: #ffffff !important;
      font-family: -apple-system, BlinkMacSystemFont, "Plus Jakarta Sans", sans-serif !important;
      font-weight: 700 !important;
      font-size: 13px !important;
      box-shadow: 0 2px 8px rgba(184, 98, 59, 0.45) !important;
      border: 2px solid #ffffff !important;
    }
"""

base_html = base_html.replace('</style>', cart_fix_css + '\n  </style>')
print("Injected cart_fix_css")

# Save base_html
with open('c:/Work/index_optimized.html', 'w', encoding='utf-8') as f:
    f.write(base_html)

print("Saved c:/Work/index_optimized.html")
