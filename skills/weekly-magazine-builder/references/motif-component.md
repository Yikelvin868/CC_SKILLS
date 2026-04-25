# Motif component — generative SVG identity

A magazine's motif is its single most recognizable visual element. It must be programmatically generated (not a static logo file) so it can vary across covers and contexts while remaining recognizable.

## Design principles for any motif

**Recognizable at three scales.** It must work as:
- 22px favicon / masthead mini icon
- 60-200px in-page card visual
- 400-600px cover centerpiece

If a motif only works at one scale, it's not a motif — it's an illustration.

**Programmatically parameterizable.** Generate the SVG from a builder function with these typical parameters:
- `size` (px)
- `seed` (deterministic variation)
- `accentColor` (override for per-issue or per-section variation)
- `complexity` (number of rings / spokes / nodes)
- `label` (text rendered in center)

**Symbolically tied to the publisher.** For a biometrics company, the iris. For a navigation tool, a compass. For a writing community, a fountain pen nib. For a network company, a constellation. The motif must answer "what does this brand look at every day?"

**Absorbs the brand color as accent, not as fill.** The motif itself is mostly grayscale (or muted versions of the brand color); the brand color shows up as a single accent — a ring, a dot, a highlight. Using brand color as the dominant fill makes the motif feel branded; using it as accent makes the motif feel printed.

**Animatable.** At minimum, an awakening / reveal animation for the cover. Optional: subtle ambient motion (slow rotation, breathing, mouse-follow).

## Reference implementation: iris.js (HOMSH)

For HOMSH's biometrics weekly, the motif is the iris (the colored ring around the pupil). The component file is `~240 lines` and exports:

```javascript
// site/js/motif.js (or iris.js for HOMSH)

const TAU = Math.PI * 2;

/**
 * Generate full motif SVG string.
 */
export function buildIris({
  size = 360,
  accentColor = "#E60012",
  ringColor = "#26262F",
  ringColorSoft = "#1F1F2B",
  pupilColor = "#0A0A0F",
  labelColor = "#F4F0E8",
  label = "",
  labelSub = "",
  rings = 8,
  spokes = 28,
  seed = 1,
  accent = "dashed",   // "dashed" | "solid" | "none"
  animated = false,
} = {}) {
  // ... build concentric rings
  // ... build radial spokes (outer)
  // ... build short spokes (middle layer for texture)
  // ... build accent ring (red, dashed)
  // ... build pupil with optional center label

  return `<svg ...>...</svg>`;
}

/**
 * Mini version for masthead, favicon, etc.
 */
export function buildMiniIris({ size = 24, color = "#E60012" } = {}) {
  return `<svg viewBox="0 0 ${size} ${size}" ...>
    <circle cx="..." r="${c-0.5}" fill="none" stroke="currentColor" stroke-width="0.75" opacity="0.4"/>
    <circle cx="..." r="${c*0.68}" fill="none" stroke="currentColor" stroke-width="0.5" opacity="0.6"/>
    <circle cx="..." r="${c*0.35}" fill="${color}"/>
    <circle cx="..." r="${c*0.12}" fill="#0A0A0F"/>
  </svg>`;
}

/**
 * Animated reveal — cover entrance sequence.
 * Phases:
 *   0-100ms:   nothing visible
 *   100-400ms: pupil fades in
 *   400-1200ms: rings fade in from inner to outer
 *   800-1200ms: spokes draw outward
 *   1400-1800ms: accent ring + short spokes
 *   1800-2200ms: center label fades in
 */
export function playIrisReveal(container, irisOpts = {}) {
  // inject SVG, hide all elements, schedule timed appearances via setTimeout
}

/**
 * Mouse-follow eye effect (cover only).
 * Pupil and label translate up to maxOffset px toward cursor.
 * Outer rings translate -depth (small inverse) for parallax depth.
 */
export function trackPupil(container, maxOffset = 12) {
  // attach mousemove listener with rAF throttling
}

/**
 * Pseudo-random for seeded variation.
 */
function pseudoRand(n) {
  const x = Math.sin(n * 12.9898 + 78.233) * 43758.5453;
  return x - Math.floor(x);
}
```

## Adapting the iris pattern to other motifs

The iris is a **concentric + radial** motif. Many other motifs share this structure or can be reframed into it:

- **Sun / star** → concentric rings + rays = same code, different defaults
- **Lens / aperture** → polygonal blades arranged radially
- **Compass** → 4 cardinal arrows + concentric degree marks
- **Network graph** → nodes at radial positions + edges
- **Wave / spectrum** → horizontal lines at frequencies, no rings — different code, same builder pattern

If the motif is fundamentally not concentric (e.g., a single bird, a fountain pen nib, a bookmark), the principles still apply: build a function that generates the SVG with parameters; provide mini and full variants; provide an animated entrance.

## Pitfalls to avoid

**Don't make the motif too literal.** A literal eye for a biometrics company looks generic; an abstracted iris with concentric rings is a motif. A literal book for a publisher looks generic; an abstracted spine with margin marks is a motif.

**Don't use too much color.** A motif with 5 colors is decoration. A motif with 1-2 colors (mostly grayscale + single accent) is identity.

**Don't skip the seed parameter.** You'll want to vary the motif slightly per issue (rotation angle, accent color, ring count) and the seed makes that controllable and reproducible.

**Don't forget the favicon.** Generate a 32×32 PNG version of the mini motif and use it as the site favicon. Browsers and search engines will display it — the motif is your visual signature there too.

## Where the motif appears

- Homepage hero (full reveal animation)
- Issue cover (full, smaller, often with label inside pupil/center)
- Issue card on homepage (medium, hover-rotates)
- Masthead (mini, fixed)
- 404 page (mini, decorative)
- "Next Week" preview (half-revealed, suggests mystery)
- Each deep article's breadcrumb area (mini)
- Favicon (32px PNG export)

The repetition is the point. The same motif at different scales and contexts trains the reader's eye to recognize the magazine in 0.1 seconds.
