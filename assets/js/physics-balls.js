/**
 * ISISLab interactive research orbs.
 *
 * The HTML snapshot of the original WordPress theme references
 * `isislab_files/site.js`, but that JS file wasn't included in the export.
 * This is a self-contained replacement for Jekyll, reproducing the visible
 * translucent orbs and implementing true, ongoing motion and impulse transfer.
 *
 * Research fields: cyan = distributed computing; violet = collaborative
 * computing; green = visualization and interaction.
 */
(function () {
  'use strict';

  const COLORS = [[4, 200, 239], [147, 103, 249], [13, 192, 141]];
  // Initial positions / sizes measured against the supplied WordPress screenshot.
  const COMPOSITION = [
    [.033,.262,47,1],[.130,.266,54,2],[.260,.092,28,2],
    [.360,.169,56,1],[.390,.278,58,0],[.574,.254,67,0],
    [.633,.260,27,0],[.885,.355,40,0],[.875,.460,48,2],
    [.950,.540,22,0],[.780,.557,66,2],[.843,.689,77,0],
    [.842,.866,20,2],[.669,.595,30,0],[.578,.534,30,0],
    [.510,.633,25,1],[.302,.873,23,1],[.182,.874,99,1],
    [.127,.724,105,0],[.212,.627,86,0],[.047,.640,76,1],
    [.029,.469,35,0],[.056,.520,19,2],[.117,.524,29,0],
    [.225,.494,26,0],[.320,.572,29,2],[.733,.389,34,1]
  ];
  const clamp = (value, min, max) => Math.max(min, Math.min(max, value));
  const random = (a, b) => a + Math.random() * (b - a);
  const rgb = (color, alpha) => `rgba(${color[0]},${color[1]},${color[2]},${alpha})`;

  function init() {
    const layer = document.querySelector('[data-physics-hero]');
    if (!layer || layer.dataset.physicsInitialized === 'true') return;
    const hero = layer.closest('.lab-hero');
    const canvas = layer.querySelector('canvas');
    const ctx = canvas && canvas.getContext('2d', { alpha: true });
    if (!ctx || !hero) return;
    layer.dataset.physicsInitialized = 'true';

    let w = 0, h = 0, dpr = 1, balls = [], last = 0, raf = 0;
    let chosen = -1, dragging = null, pointerId = -1;
    let prior = { x: 0, y: 0, t: 0 };
    let previousVelocity = { x: 0, y: 0 };
    let frames = 0, collisions = 0;
    const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');

    function makeBalls() {
      const mobile = w < 700;
      const scale = mobile ? clamp(w / 1350, .28, .58) : clamp(w / 1657, .53, 1.17);
      balls = COMPOSITION.map(([relX, relY, radius, color], idx) => {
        // Keep most spheres below the text card on narrow displays.
        if (mobile) {
          if (radius > 42) {
            relX = .08 + ((relX * 2.71) % .84);
            relY = .75 + ((idx * .074) % .22);
          } else relY = .08 + ((relY * 2.8) % .86);
        }
        const r = Math.max(5, radius * scale);
        return {
          x: relX * w, y: relY * h, r, color,
          // Visible from the first frame: speed ~45–105 px / second at 60 Hz.
          vx: random(-1.60, 1.60), vy: random(-1.45, 1.45),
          mass: r * r, phase: idx * 1.37
        };
      });
      // Ensure every orb moves immediately, including occasional near-zero draws.
      for (const b of balls) if (Math.hypot(b.vx, b.vy) < .65) {
        const theta = random(0, Math.PI * 2);
        b.vx = Math.cos(theta) * 1.05;
        b.vy = Math.sin(theta) * 1.05;
      }
    }

    function sizeCanvas() {
      const bounds = layer.getBoundingClientRect();
      if (bounds.width < 5 || bounds.height < 5) return;
      const oldWidth = w, oldHeight = h;
      w = bounds.width; h = bounds.height;
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
      canvas.style.width = `${w}px`;
      canvas.style.height = `${h}px`;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      if (balls.length && oldWidth > 0 && oldHeight > 0 &&
          Math.abs(w / oldWidth - 1) < .18 && Math.abs(h / oldHeight - 1) < .18) {
        for (const b of balls) {
          b.x *= w / oldWidth; b.y *= h / oldHeight;
          b.r *= w / oldWidth; b.mass = b.r * b.r;
        }
      } else makeBalls();
      draw();
    }

    function bound(b) {
      // Slight clipping at the screen edges matches the original artwork.
      const margin = b.r * .35;
      if (b.x < margin) { b.x = margin; b.vx = Math.abs(b.vx) * .94; }
      if (b.x > w - margin) { b.x = w - margin; b.vx = -Math.abs(b.vx) * .94; }
      if (b.y < margin) { b.y = margin; b.vy = Math.abs(b.vy) * .94; }
      if (b.y > h - margin) { b.y = h - margin; b.vy = -Math.abs(b.vy) * .94; }
    }

    function impact(a, b) {
      const deltaX = b.x - a.x, deltaY = b.y - a.y;
      let distance = Math.hypot(deltaX, deltaY);
      const allowed = a.r + b.r;
      if (distance >= allowed) return;
      if (distance < .0001) distance = .0001;
      collisions++;
      const nx = deltaX / distance, ny = deltaY / distance;
      const inverseA = a === dragging ? 0 : 1 / a.mass;
      const inverseB = b === dragging ? 0 : 1 / b.mass;
      const total = inverseA + inverseB;
      if (!total) return;

      // Separate overlapping surfaces without excessive jitter.
      const correction = ((allowed - distance) * .75) / total;
      a.x -= nx * correction * inverseA;
      a.y -= ny * correction * inverseA;
      b.x += nx * correction * inverseB;
      b.y += ny * correction * inverseB;
      const relativeSpeed = (b.vx - a.vx) * nx + (b.vy - a.vy) * ny;
      if (relativeSpeed >= 0) return;
      const restitution = .93;
      const impulse = -(1 + restitution) * relativeSpeed / total;
      a.vx -= impulse * nx * inverseA;
      a.vy -= impulse * ny * inverseA;
      b.vx += impulse * nx * inverseB;
      b.vy += impulse * ny * inverseB;
    }

    function advance(milliseconds, now) {
      const dt = clamp(milliseconds / 16.6667, .25, 2.4);
      for (const b of balls) {
        if (b === dragging) continue;
        // Ambient drift persists instead of settling to an imperceptible speed.
        b.vx += Math.sin(now * .00048 + b.phase) * .007 * dt;
        b.vy += Math.cos(now * .00043 + b.phase) * .007 * dt;
        b.vx = clamp(b.vx * .9996, -17, 17);
        b.vy = clamp(b.vy * .9996, -17, 17);
        b.x += b.vx * dt; b.y += b.vy * dt;
        bound(b);
      }
      // Sequential bounces propagate energy from a touched ball to its neighbours.
      for (let iteration = 0; iteration < 3; iteration++) {
        for (let i = 0; i < balls.length; i++)
          for (let j = i + 1; j < balls.length; j++) impact(balls[i], balls[j]);
      }
      for (const b of balls) bound(b);
    }

    function paint(b) {
      const color = COLORS[b.color], x = b.x, y = b.y, r = b.r;
      ctx.save();
      ctx.globalAlpha = chosen === -1 || chosen === b.color ? 1 : .18;
      // Preserve the translucent luminous-ball appearance from the screenshot.
      const halo = ctx.createRadialGradient(x, y, r * .13, x, y, r * 1.72);
      halo.addColorStop(0, rgb(color, .23));
      halo.addColorStop(.56, rgb(color, .16));
      halo.addColorStop(1, rgb(color, 0));
      ctx.fillStyle = halo;
      ctx.beginPath(); ctx.arc(x, y, r * 1.72, 0, Math.PI * 2); ctx.fill();
      const glass = ctx.createRadialGradient(x - r * .27, y - r * .31, r * .02, x + r * .11, y + r * .11, r * 1.07);
      glass.addColorStop(0, 'rgba(255,255,255,.89)');
      glass.addColorStop(.12, rgb(color, .72));
      glass.addColorStop(.36, rgb(color, .57));
      glass.addColorStop(.71, rgb(color, .30));
      glass.addColorStop(.91, rgb(color, .13));
      glass.addColorStop(1, 'rgba(255,255,255,.12)');
      ctx.fillStyle = glass;
      ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = 'rgba(255,255,255,.74)';
      ctx.lineWidth = Math.max(.7, r * .011);
      ctx.beginPath(); ctx.arc(x, y, r - .5, 0, Math.PI * 2); ctx.stroke();
      const hx = x - r * .26, hy = y - r * .29;
      const light = ctx.createRadialGradient(hx, hy, 0, hx, hy, r * .23);
      light.addColorStop(0, 'rgba(255,255,255,1)');
      light.addColorStop(.24, 'rgba(255,255,255,.94)');
      light.addColorStop(.56, 'rgba(255,255,255,.53)');
      light.addColorStop(1, 'rgba(255,255,255,0)');
      ctx.fillStyle = light;
      ctx.beginPath(); ctx.arc(hx, hy, r * .23, 0, Math.PI * 2); ctx.fill();
      ctx.restore();
    }

    function draw() {
      ctx.clearRect(0, 0, w, h);
      for (const b of balls) paint(b);
    }

    function loop(now) {
      raf = 0;
      if (document.hidden) return;
      const dt = last ? Math.min(50, now - last) : 16.667;
      last = now;
      if (!reduceMotion.matches) advance(dt, now);
      draw(); frames++;
      raf = requestAnimationFrame(loop);
    }

    function start() {
      if (raf) cancelAnimationFrame(raf);
      last = 0;
      if (!document.hidden && w > 0 && h > 0) raf = requestAnimationFrame(loop);
    }

    function coords(event) {
      const rect = layer.getBoundingClientRect();
      return { x: event.clientX - rect.left, y: event.clientY - rect.top };
    }
    function underPoint(point) {
      return [...balls].reverse().find(b => Math.hypot(b.x - point.x, b.y - point.y) < b.r * 1.17);
    }
    function nudge(ball) {
      const angle = random(0, Math.PI * 2), magnitude = random(9, 15);
      ball.vx = clamp(ball.vx + Math.cos(angle) * magnitude, -17, 17);
      ball.vy = clamp(ball.vy + Math.sin(angle) * magnitude, -17, 17);
      // In reduced-motion mode, user-requested movement occurs in a single small step.
      if (reduceMotion.matches) { advance(16.667, performance.now()); draw(); }
      else start();
    }
    hero.addEventListener('pointerdown', event => {
      if (event.target.closest('a,button,input,select,textarea')) return;
      const point = coords(event), orb = underPoint(point);
      if (!orb) return;
      nudge(orb);
      if (event.pointerType === 'mouse' && event.button === 0) {
        dragging = orb;
        pointerId = event.pointerId;
        prior = { ...point, t: performance.now() };
        previousVelocity = { x: orb.vx, y: orb.vy };
        hero.setPointerCapture?.(event.pointerId);
      }
    });
    hero.addEventListener('pointermove', event => {
      if (!dragging || event.pointerId !== pointerId) return;
      const point = coords(event), t = performance.now();
      const elapsed = Math.max(10, t - prior.t);
      previousVelocity = {
        x: clamp((point.x - prior.x) * 16.667 / elapsed, -17, 17),
        y: clamp((point.y - prior.y) * 16.667 / elapsed, -17, 17)
      };
      prior = { ...point, t };
      dragging.x = point.x; dragging.y = point.y;
      dragging.vx = previousVelocity.x; dragging.vy = previousVelocity.y;
      draw();
    });
    function release(event) {
      if (!dragging || (event.pointerId !== undefined && event.pointerId !== pointerId)) return;
      dragging.vx = clamp(previousVelocity.x + random(-1.1, 1.1), -17, 17);
      dragging.vy = clamp(previousVelocity.y + random(-1.1, 1.1), -17, 17);
      dragging = null; pointerId = -1;
    }
    hero.addEventListener('pointerup', release);
    hero.addEventListener('pointercancel', release);
    hero.addEventListener('lostpointercapture', () => release({}));
    for (const control of document.querySelectorAll('[data-research-index]')) {
      control.addEventListener('pointerenter', () => { chosen = Number(control.dataset.researchIndex); draw(); });
      control.addEventListener('pointerleave', () => { chosen = -1; draw(); });
      control.addEventListener('focus', () => { chosen = Number(control.dataset.researchIndex); draw(); });
      control.addEventListener('blur', () => { chosen = -1; draw(); });
    }

    // Minimal read-only diagnostics make it possible to verify the motion in-browser.
    window.ISISLabPhysics = Object.freeze({
      snapshot: () => balls.map(b => ({x:b.x,y:b.y,r:b.r,vx:b.vx,vy:b.vy,field:b.color})),
      stats: () => ({ frames, collisions, running: !!raf, reducedMotion: reduceMotion.matches }),
      kickAt: (x, y) => { const b = underPoint({x,y}); if (b) nudge(b); return !!b; }
    });
    let resizeRequest = 0;
    window.addEventListener('resize', () => {
      cancelAnimationFrame(resizeRequest);
      resizeRequest = requestAnimationFrame(() => { sizeCanvas(); start(); });
    }, {passive:true});
    if ('ResizeObserver' in window) new ResizeObserver(() => {
      if (Math.abs(layer.clientWidth - w) > 2 || Math.abs(layer.clientHeight - h) > 2) {
        sizeCanvas(); start();
      }
    }).observe(layer);
    document.addEventListener('visibilitychange', start);
    window.addEventListener('pageshow', start);
    reduceMotion.addEventListener?.('change', start);
    sizeCanvas(); start();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, {once: true});
  else init();
})();
