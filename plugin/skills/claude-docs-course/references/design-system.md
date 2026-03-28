# Design System Reference — Obsidian & Amber

Complete CSS design tokens for the course. Copy this entire `:root` block into the course HTML. The theme is a refined dark aesthetic — deep obsidian backgrounds with warm amber accents that create an atmosphere of focused discovery. Serif display headings give editorial elegance; clean sans-serif body text ensures readability. Grain textures and subtle glow effects add depth without distraction.

## Table of Contents
1. [Color Palette](#color-palette)
2. [Typography](#typography)
3. [Spacing & Layout](#spacing--layout)
4. [Shadows & Depth](#shadows--depth)
5. [Animations & Transitions](#animations--transitions)
6. [Navigation & Progress](#navigation--progress)
7. [Module Structure](#module-structure)
8. [Responsive Breakpoints](#responsive-breakpoints)
9. [Scrollbar & Background](#scrollbar--background)
10. [Grain & Atmosphere](#grain--atmosphere)

---

## Color Palette

```css
:root {
  /* --- BACKGROUNDS ---
     Deep obsidian with a subtle warm-navy undertone. Never pure black.
     The slight blue-purple tint gives depth and avoids a "dead screen" feel. */
  --color-bg:             #0D0D16;       /* primary — deep obsidian */
  --color-bg-warm:        #12121E;       /* alternating modules — slightly lifted */
  --color-bg-code:        #08080F;       /* code blocks — near-black, inky */
  --color-text:           #E8E0D4;       /* warm cream — primary text */
  --color-text-secondary: #9A9088;       /* warm muted — body text */
  --color-text-muted:     #5C5852;       /* dark muted — labels, timestamps */
  --color-border:         #2A2840;       /* subtle dark border */
  --color-border-light:   #1E1C32;       /* even subtler border */
  --color-surface:        #161624;       /* card surfaces — elevated from bg */
  --color-surface-warm:   #1C1A28;       /* warm card surface — for translations */

  /* --- ACCENT: Amber ---
     Warm amber-gold evokes lamplight, discovery, illumination.
     This is the signature color — used sparingly for maximum impact. */
  --color-accent:         #F0A050;       /* amber gold */
  --color-accent-hover:   #E88A30;       /* deeper amber on hover */
  --color-accent-light:   rgba(240, 160, 80, 0.08);  /* subtle amber wash */
  --color-accent-muted:   #C09060;       /* desaturated amber for less emphasis */
  --color-accent-glow:    rgba(240, 160, 80, 0.25);  /* glow effect around interactives */

  /* --- SEMANTIC --- */
  --color-success:        #50C8A0;       /* bright mint-teal */
  --color-success-light:  rgba(80, 200, 160, 0.08);
  --color-error:          #F06060;       /* warm red */
  --color-error-light:    rgba(240, 96, 96, 0.08);
  --color-info:           #60A0E0;       /* soft blue */
  --color-info-light:     rgba(96, 160, 224, 0.08);

  /* --- ACTOR COLORS (assign to protocol conversation actors) ---
     Chosen for contrast against dark backgrounds and against each other.
     Each actor should be instantly recognizable by color alone. */
  --color-actor-1:        #F0A050;       /* amber — Client App */
  --color-actor-2:        #50C8A0;       /* teal — API Gateway */
  --color-actor-3:        #C080E0;       /* soft violet — Claude Model */
  --color-actor-4:        #E0C060;       /* warm gold — Cache / Tool */
  --color-actor-5:        #60B0E0;       /* sky blue — User */
}
```

**Rules:**
- Even-numbered modules use `--color-bg`, odd-numbered use `--color-bg-warm` (alternating creates depth rhythm)
- Actor colors must be distinct from each other and pass a contrast test against `--color-surface`
- Code blocks always use `--color-bg-code` — darker than everything else to visually recede
- The amber accent should be used for CTAs, active states, and highlights — never for large background areas
- Interactive elements get a subtle `box-shadow: 0 0 20px var(--color-accent-glow)` on hover/focus

---

## Typography

```css
:root {
  /* --- FONTS ---
     Display: Instrument Serif — sharp, elegant serifs with editorial character.
     Creates immediate visual identity on dark backgrounds. The contrast between
     serif headings and sans body text is the signature of this theme.
     Body: Outfit — modern, clean, slightly rounded terminals. Excellent legibility
     at all sizes on dark backgrounds.
     Mono: JetBrains Mono — developer standard, clear character distinction. */
  --font-display:  'Instrument Serif', Georgia, 'Times New Roman', serif;
  --font-body:     'Outfit', -apple-system, sans-serif;
  --font-mono:     'JetBrains Mono', 'Fira Code', 'Consolas', monospace;

  /* --- TYPE SCALE (1.25 ratio) --- */
  --text-xs:   0.75rem;    /* 12px — labels, badges */
  --text-sm:   0.875rem;   /* 14px — secondary text, code */
  --text-base: 1rem;       /* 16px — body text */
  --text-lg:   1.125rem;   /* 18px — lead paragraphs */
  --text-xl:   1.25rem;    /* 20px — screen headings */
  --text-2xl:  1.5rem;     /* 24px — sub-module titles */
  --text-3xl:  1.875rem;   /* 30px — module subtitles */
  --text-4xl:  2.25rem;    /* 36px — module titles */
  --text-5xl:  3rem;       /* 48px — hero text */
  --text-6xl:  3.75rem;    /* 60px — module numbers */

  /* --- LINE HEIGHTS --- */
  --leading-tight:  1.15;  /* headings */
  --leading-snug:   1.3;   /* subheadings */
  --leading-normal: 1.6;   /* body text */
  --leading-loose:  1.8;   /* relaxed reading */
}
```

**Google Fonts link (put in `<head>`):**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

**Rules:**
- Module numbers: `--text-6xl`, font-display, italic, `--color-accent` with 20% opacity
- Module titles: `--text-4xl` or `--text-5xl`, font-display, normal weight (serifs carry their own weight — no bold needed)
- Screen headings: `--text-xl` or `--text-2xl`, font-display
- Body text: `--text-base` or `--text-lg`, font-body, weight 400, `--leading-normal`
- Code: `--text-sm`, font-mono
- Labels/badges: `--text-xs`, font-body, weight 600, uppercase, letter-spacing 0.08em
- The serif display font should NEVER be used below `--text-xl` — below that, use font-body

---

## Spacing & Layout

```css
:root {
  --space-1:  0.25rem;   /* 4px */
  --space-2:  0.5rem;    /* 8px */
  --space-3:  0.75rem;   /* 12px */
  --space-4:  1rem;      /* 16px */
  --space-5:  1.25rem;   /* 20px */
  --space-6:  1.5rem;    /* 24px */
  --space-8:  2rem;      /* 32px */
  --space-10: 2.5rem;    /* 40px */
  --space-12: 3rem;      /* 48px */
  --space-16: 4rem;      /* 64px */
  --space-20: 5rem;      /* 80px */
  --space-24: 6rem;      /* 96px */

  --content-width:     800px;   /* standard reading width */
  --content-width-wide: 1000px; /* for side-by-side layouts */
  --nav-height:        52px;
  --radius-sm:  6px;
  --radius-md:  10px;
  --radius-lg:  14px;
  --radius-xl:  20px;
  --radius-full: 9999px;
}
```

**Module layout:**
```css
.module {
  min-height: 100dvh;       /* fallback: 100vh */
  scroll-snap-align: start;
  padding: var(--space-16) var(--space-6);
  padding-top: calc(var(--nav-height) + var(--space-12));
  position: relative;        /* for grain overlay pseudo-element */
}
.module-content {
  max-width: var(--content-width);
  margin: 0 auto;
}
```

---

## Shadows & Depth

```css
:root {
  /* On dark backgrounds, shadows use near-black with slight blue tint
     to maintain the obsidian atmosphere. Glow effects use the accent color. */
  --shadow-sm:  0 1px 3px rgba(0, 0, 8, 0.3);
  --shadow-md:  0 4px 16px rgba(0, 0, 8, 0.4);
  --shadow-lg:  0 8px 32px rgba(0, 0, 8, 0.5);
  --shadow-xl:  0 16px 48px rgba(0, 0, 8, 0.6);
  --shadow-glow: 0 0 24px var(--color-accent-glow);    /* amber glow for interactives */
  --shadow-inner: inset 0 1px 0 rgba(255, 255, 255, 0.04);  /* subtle top-edge highlight */
}
```

**Card depth pattern:**
```css
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md), var(--shadow-inner);
  transition: box-shadow var(--duration-normal) var(--ease-out),
              border-color var(--duration-normal) var(--ease-out);
}
.card:hover {
  border-color: var(--color-accent-muted);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
}
```

Never use pure black `rgba(0,0,0,...)` for shadows — always use the blue-tinted `rgba(0,0,8,...)` to maintain the obsidian atmosphere.

---

## Animations & Transitions

```css
:root {
  --ease-out:    cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);   /* subtle overshoot */
  --duration-fast:   150ms;
  --duration-normal: 300ms;
  --duration-slow:   500ms;
  --duration-reveal: 700ms;
  --stagger-delay:   100ms;
}
```

**Scroll-triggered reveal pattern:**
```css
.animate-in {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity var(--duration-reveal) var(--ease-out),
              transform var(--duration-reveal) var(--ease-out);
}
.animate-in.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger children */
.stagger-children > .animate-in {
  transition-delay: calc(var(--stagger-index, 0) * var(--stagger-delay));
}
```

**Amber glow pulse (for interactive elements awaiting interaction):**
```css
@keyframes glowPulse {
  0%, 100% { box-shadow: 0 0 16px rgba(240, 160, 80, 0.1); }
  50%      { box-shadow: 0 0 28px rgba(240, 160, 80, 0.2); }
}
.interactive-hint {
  animation: glowPulse 3s var(--ease-in-out) infinite;
}
```

**JS setup for stagger:**
```javascript
document.querySelectorAll('.stagger-children').forEach(parent => {
  Array.from(parent.children).forEach((child, i) => {
    child.style.setProperty('--stagger-index', i);
  });
});
```

**Intersection Observer (trigger reveals):**
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target); // animate only once
    }
  });
}, { rootMargin: '0px 0px -10% 0px', threshold: 0.1 });

document.querySelectorAll('.animate-in').forEach(el => observer.observe(el));
```

---

## Navigation & Progress

**HTML structure:**
```html
<nav class="nav">
  <div class="progress-bar" role="progressbar" aria-valuenow="0"></div>
  <div class="nav-inner">
    <span class="nav-title">Course Title</span>
    <div class="nav-dots">
      <button class="nav-dot" data-target="module-1" data-tooltip="Module 1 Name"
              role="tab" aria-label="Module 1"></button>
      <!-- one per module -->
    </div>
  </div>
</nav>
```

**Nav styling:**
```css
.nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  background: rgba(13, 13, 22, 0.85);
  backdrop-filter: blur(16px) saturate(1.2);
  -webkit-backdrop-filter: blur(16px) saturate(1.2);
  border-bottom: 1px solid var(--color-border-light);
  height: var(--nav-height);
}
.nav-inner {
  max-width: var(--content-width-wide);
  margin: 0 auto;
  padding: 0 var(--space-6);
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.nav-title {
  font-family: var(--font-display);
  font-size: var(--text-base);
  color: var(--color-text);
  letter-spacing: -0.01em;
}
.progress-bar {
  position: absolute;
  bottom: 0; left: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--color-accent), var(--color-accent-hover));
  transition: width 100ms linear;
  box-shadow: 0 0 8px var(--color-accent-glow);
}
```

**Nav dot states:**
```css
.nav-dot {
  width: 10px; height: 10px;
  border-radius: 50%;
  border: 1.5px solid var(--color-text-muted);
  background: transparent;
  cursor: pointer;
  transition: all var(--duration-normal) var(--ease-out);
  padding: 0;
}
.nav-dot.active {
  border-color: var(--color-accent);
  background: var(--color-accent);
  box-shadow: 0 0 10px var(--color-accent-glow);
  transform: scale(1.15);
}
.nav-dot.visited {
  border-color: var(--color-accent-muted);
  background: var(--color-accent-muted);
}
```

**Progress bar (JS):**
```javascript
function updateProgressBar() {
  const scrollTop = window.scrollY;
  const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
  const progress = (scrollTop / scrollHeight) * 100;
  progressBar.style.width = progress + '%';
}
window.addEventListener('scroll', () => {
  requestAnimationFrame(updateProgressBar);
}, { passive: true });
```

**Keyboard navigation:**
```javascript
document.addEventListener('keydown', (e) => {
  if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;
  if (e.key === 'ArrowDown' || e.key === 'ArrowRight') { nextModule(); e.preventDefault(); }
  if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') { prevModule(); e.preventDefault(); }
});
```

---

## Module Structure

**HTML template for each module:**
```html
<section class="module" id="module-N">
  <div class="module-content">
    <header class="module-header animate-in">
      <span class="module-number">0N</span>
      <h1 class="module-title">Module Title</h1>
      <p class="module-subtitle">One-line description of what this module teaches</p>
    </header>

    <div class="module-body">
      <section class="screen animate-in">
        <h2 class="screen-heading">Screen Title</h2>
        <p>Content...</p>
        <!-- Interactive elements, code translations, etc. -->
      </section>

      <section class="screen animate-in">
        <!-- Next screen -->
      </section>
    </div>
  </div>
</section>
```

**Module number styling:**
```css
.module-number {
  font-family: var(--font-display);
  font-style: italic;
  font-size: var(--text-6xl);
  color: var(--color-accent);
  opacity: 0.15;
  line-height: 1;
  display: block;
  margin-bottom: var(--space-2);
}
.module-title {
  font-family: var(--font-display);
  font-size: var(--text-5xl);
  color: var(--color-text);
  line-height: var(--leading-tight);
  margin-bottom: var(--space-3);
  letter-spacing: -0.02em;
}
.module-subtitle {
  font-family: var(--font-body);
  font-size: var(--text-lg);
  color: var(--color-text-secondary);
  line-height: var(--leading-snug);
  max-width: 540px;
}
.screen-heading {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  color: var(--color-text);
  margin-bottom: var(--space-4);
}
```

**Alternating module backgrounds:**
```css
.module:nth-child(odd)  { background: var(--color-bg); }
.module:nth-child(even) { background: var(--color-bg-warm); }
```

---

## Responsive Breakpoints

```css
/* Tablet */
@media (max-width: 768px) {
  :root {
    --text-4xl: 1.875rem;
    --text-5xl: 2.25rem;
    --text-6xl: 3rem;
  }
  .translation-block { grid-template-columns: 1fr; } /* stack code/english */
  .pattern-cards { grid-template-columns: 1fr 1fr; }
}

/* Mobile */
@media (max-width: 480px) {
  :root {
    --text-4xl: 1.5rem;
    --text-5xl: 1.875rem;
    --text-6xl: 2.25rem;
  }
  .module { padding: var(--space-8) var(--space-4); }
  .pattern-cards { grid-template-columns: 1fr; }
  .flow-steps { flex-direction: column; }
  .flow-arrow { transform: rotate(90deg); }
}
```

---

## Scrollbar & Background

```css
/* Custom scrollbar — thin, ambient */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: var(--color-border);
  border-radius: var(--radius-full);
}
::-webkit-scrollbar-thumb:hover {
  background: var(--color-accent-muted);
}

/* Atmospheric background — subtle amber radial at top, fading out */
body {
  background: var(--color-bg);
  background-image:
    radial-gradient(ellipse at 30% 0%, rgba(240, 160, 80, 0.04) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 100%, rgba(192, 128, 224, 0.02) 0%, transparent 40%);
}

/* Page scroll setup */
html {
  scroll-snap-type: y proximity;
  scroll-behavior: smooth;
}
```

---

## Grain & Atmosphere

The grain overlay is the signature texture of this theme. It adds analog warmth to the digital dark surface — like looking through a vintage lens or at a printed page under lamplight.

**CSS grain overlay (apply to body or individual modules):**
```css
body::after {
  content: '';
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.035;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 256px 256px;
}
```

**Module separator — geometric line accent:**
```css
.module + .module::before {
  content: '';
  display: block;
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--color-accent-muted), transparent);
}
```

**Glass-morphism pattern for elevated surfaces:**
```css
.glass {
  background: rgba(22, 22, 36, 0.6);
  backdrop-filter: blur(12px) saturate(1.1);
  -webkit-backdrop-filter: blur(12px) saturate(1.1);
  border: 1px solid rgba(255, 255, 255, 0.04);
  box-shadow: var(--shadow-md), var(--shadow-inner);
}
```

---

## Code Block Globals

All code blocks in the course — whether inside translation blocks, standalone snippets, or quiz challenges — must wrap text and never show a horizontal scrollbar. This is a teaching tool, not an IDE.

```css
pre, code {
  white-space: pre-wrap;       /* wrap long lines */
  word-break: break-word;      /* break mid-word if absolutely needed */
  overflow-x: hidden;          /* no horizontal scrollbar — ever */
}
/* Hide scrollbars on code containers */
.translation-code::-webkit-scrollbar,
pre::-webkit-scrollbar {
  display: none;
}
```

Code snippets must be **exact copies** from the official documentation — never modified, trimmed, or simplified. Choose naturally short (5-15 line) examples that illustrate the concept well.

---

## Syntax Highlighting (Amber Night)

Custom syntax theme designed for the `--color-bg-code` (#08080F) background. Warm tones dominate, with cool accents for contrast. Every color must be instantly readable against the near-black code background.

```css
.code-keyword  { color: #F0A050; }  /* amber — keywords carry the theme color */
.code-string   { color: #A6E3A1; }  /* soft green — strings stay calm */
.code-function { color: #60B0E0; }  /* sky blue — function names pop */
.code-comment  { color: #4A4A58; }  /* muted slate — comments recede */
.code-number   { color: #F0C080; }  /* warm peach — numbers glow gently */
.code-property { color: #E8E0D4; }  /* cream — object keys match body text */
.code-operator { color: #50C8A0; }  /* teal — operators are structural */
.code-tag      { color: #E08080; }  /* muted rose — HTML tags */
.code-attr     { color: #C080E0; }  /* soft violet — HTML attributes */
.code-value    { color: #A6E3A1; }  /* soft green — attribute values */
```

The amber keyword color (`#F0A050`) ties code to the overall theme accent, creating visual cohesion between the UI and the code examples.
