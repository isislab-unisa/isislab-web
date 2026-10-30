"""Optional Chromium smoke test: pip install playwright; playwright install chromium.
Run from any folder: python scripts/test_physics.py
"""
from pathlib import Path
from shutil import which
from playwright.sync_api import sync_playwright
root = Path(__file__).resolve().parents[1]
html = (root / 'preview.html').read_text(encoding='utf8')
with sync_playwright() as p:
    local_chromium = which("chromium") or which("chromium-browser")
    browser = p.chromium.launch(headless=True, executable_path=local_chromium, args=["--no-sandbox"] if local_chromium else [])
    desktop = browser.new_page(viewport={'width': 1440, 'height': 900})
    errors = []
    desktop.on('pageerror', lambda e: errors.append(str(e)))
    desktop.set_content(html, wait_until='load')
    desktop.wait_for_timeout(400)
    assert desktop.evaluate("typeof window.ISISLabPhysics") == 'object'
    before = desktop.evaluate('ISISLabPhysics.snapshot()')
    desktop.wait_for_timeout(1800)
    after = desktop.evaluate('ISISLabPhysics.snapshot()')
    travel = [((a['x']-b['x'])**2+(a['y']-b['y'])**2)**.5 for a,b in zip(before,after)]
    assert sum(d>15 for d in travel) >= 10, travel
    info = desktop.evaluate('ISISLabPhysics.stats()')
    assert info['frames'] > 40 and info['collisions'] > 0 and info['running'], info
    touch_context = browser.new_context(viewport={'width':390,'height':844}, has_touch=True,is_mobile=True)
    touch = touch_context.new_page()
    touch.on('pageerror', lambda e: errors.append(str(e)))
    touch.set_content(html, wait_until='load')
    touch.wait_for_timeout(300)
    balls = touch.evaluate('ISISLabPhysics.snapshot()')
    position = touch.locator('[data-physics-hero]').bounding_box()
    candidate = max((i for i,b in enumerate(balls) if b['y']>600),key=lambda i:balls[i]['r'])
    b = balls[candidate]
    touch.touchscreen.tap(position['x']+b['x'],position['y']+b['y'])
    changed = touch.evaluate('(i)=>ISISLabPhysics.snapshot()[i]', candidate)
    delta=((changed['vx']-b['vx'])**2+(changed['vy']-b['vy'])**2)**.5
    assert delta > 4, delta
    assert not errors, errors
    print(f'PASS: {sum(d>15 for d in travel)} moving orbs, '
          f'{info["frames"]} frames, {info["collisions"]} collisions, '
          f'touch speed delta {delta:.1f} pixels/frame')
    browser.close()
