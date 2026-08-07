---
name: Nicholas Moffett — Portfolio
description: Personal portfolio proving a CRE+AI builder ships real work, for recruiters scanning fast
colors:
  paper: "#f1ece4"
  paper-deep: "#e9e2d6"
  ink: "#0e0e0c"
  ink-soft: "#2a2a26"
  muted: "#6b6862"
  line: "#c9c2b6"
  surface: "#fbf8f2"
  accent: "#ff3d2e"
  accent-soft: "#ff7a6a"
typography:
  display:
    fontFamily: "Instrument Serif, serif"
    fontSize: "clamp(3rem, 9vw, 9rem)"
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Instrument Serif, serif"
    fontSize: "clamp(2rem, 3.5vw, 2.8rem)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "-0.03em"
  body:
    fontFamily: "Inter, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "0.7rem"
    fontWeight: 500
    letterSpacing: "0.12em"
rounded:
  sm: "10px"
  md: "14px"
  lg: "20px"
  pill: "999px"
  circle: "50%"
spacing:
  section-y: "5.5rem"
  gap-sm: "0.5rem"
  gap-md: "1.5rem"
  gap-lg: "3rem"
components:
  btn-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    rounded: "{rounded.pill}"
    padding: "0.9rem 1.8rem"
  btn-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0.9rem 1.8rem"
  org-link:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.circle}"
---

# Design System: Nicholas Moffett — Portfolio

## 1. Overview

**Creative North Star: "The Builder's Notebook"**

This is a working builder's site, not an agency case-study template dressed up as one. The page reads like it was made by someone who ships product — real links to real projects, real numbers where they're true and corrected the moment they weren't (scholairly's signup count got walked back mid-session when the "100+ active users" line didn't hold up), and a first-person voice throughout. Density is scannable-first: a recruiter gets the headline facts in one pass, and everything past that is opt-in (click to expand a role, click a project tab, hover an org).

The system explicitly rejects generic AI-portfolio energy: template case-study copy ("The Problem / The Solution / The Impact" written in third person about someone else), decoration that doesn't carry information, and uniform reflexes applied to every section regardless of whether that section earns them. Where this system currently sits closest to a known AI-default (a cream/near-black/single-coral palette is a common 2026 AI-generated look) that was a deliberate choice made early in the project, not an oversight — the burden shifts to everything layered on top of that base actually being specific to Nicholas rather than templated.

**Key Characteristics:**
- Warm paper background, near-black ink, exactly one accent color used sparingly
- Serif display type for identity/headlines, monospace for data/labels/timestamps, sans for body prose
- One signature interactive moment per section rather than uniform motion applied everywhere (kinetic hero name, magnetic-hover project rows, floating org cluster in Involvement, drag-scroll Off Hours carousel)
- Everything clickable actually goes somewhere real: live projects, real GitHub repos, real org pages — nothing is a dead-end mockup link

## 2. Colors

A tight three-role system: one warm neutral family (paper → ink), one accent used at low frequency, nothing else.

### Primary
- **Electric Coral** (#ff3d2e): The single accent. Used for italic emphasis words in headlines, the one active nav-link underline, hover-state links, and the scroll-progress bar. Never used as a background fill of any real size.

### Neutral
- **Paper** (#f1ece4): Page background.
- **Paper Deep** (#e9e2d6): Slightly deeper neutral for nested surfaces (nav rail in Projects, involvement-label areas) — not a card background, a subtle depth cue.
- **Surface** (#fbf8f2): Lightest neutral, used for panels that sit "above" the page (project detail panel, org-photo backing, tooltips).
- **Ink** (#0e0e0c): Primary text, headline color, primary button fill.
- **Ink Soft** (#2a2a26): Body copy — slightly softer than pure ink so long paragraphs don't compete with headline weight.
- **Muted** (#6b6862): Labels, timestamps, secondary metadata, eyebrow text.
- **Line** (#c9c2b6): Hairline dividers and borders. Always 1px, never used decoratively at heavier weights.

### Named Rules
**The One Accent Rule.** Coral appears on at most one element per viewport at rest (an italic word, an active state, a hover). It is never a section background, never a card fill, never more than ~5% of any given screen's surface area.

## 3. Typography

**Display Font:** Instrument Serif (with Georgia, serif fallback)
**Body Font:** Inter (with system-ui, sans-serif fallback)
**Label/Mono Font:** JetBrains Mono (with monospace fallback)

**Character:** A classic serif/sans/mono three-way split — serif carries personality and scale, sans carries readability at length, mono signals "this is data, not prose" (timestamps, role labels, tech-stack tags, eyebrow numbers). The pairing is intentionally conservative; the personality lives in motion and interaction, not in an unusual type choice.

### Hierarchy
- **Display** (400 weight, clamp(3rem, 9vw, 9rem), line-height 0.95): Hero name only. Italic sub-word in coral for the one emphasized term.
- **Headline** (400 weight, clamp(2rem, 3.5vw, 2.8rem), line-height 1): Section titles ("Selected experience.", "What I've built."). Same italic-accent-word pattern as the hero, reused deliberately as a system-wide rule rather than a one-off hero trick.
- **Title** (500 weight, ~1.6rem, Instrument Serif): Row-level titles inside lists (a role title, a project nav name).
- **Body** (400 weight, 1rem–1.05rem, line-height 1.6–1.7, Inter): Prose paragraphs. Capped implicitly by the grid column width, not an explicit ch value — worth tightening if any paragraph runs past ~75ch on wide viewports.
- **Label** (500 weight, 0.6–0.8rem, JetBrains Mono, uppercase, 0.05–0.15em tracking): Section eyebrows, role/date metadata, org-orb captions, tech-stack chips.

### Named Rules
**The Serif-Rise Rule.** Every headline (hero and section) uses the same mask-reveal-on-scroll treatment: the line sits behind an invisible clip and rises into place. One mechanism, reused consistently, rather than a different entrance animation per section.

## 4. Elevation

Flat by default — the whole system leans on hairline borders (`--line`) and the paper/surface/paper-deep three-step neutral ramp to convey depth, not shadows. Shadow appears only as a **response to interaction** (hover lift on a card, an active project panel, an org-orb hover), never as a resting decoration.

### Shadow Vocabulary
- **Resting card** (`box-shadow: 0 10px 26px -12px rgba(14,14,12,0.28)`): Default state for the org-photo circles and any raised element at rest — deliberately soft and close, not a floating-card look.
- **Hover lift** (`box-shadow: 0 16px 34px -14px rgba(14,14,12,0.35)`): Interaction response, slightly larger blur/spread than resting.
- **Off Hours cards**: no shadow at rest (`0 0 0 0 rgba(0,0,0,0)`), gains `0 20px 36px -14px rgba(0,0,0,0.4)` on hover only.

### Named Rules
**The No-Rest-Shadow Rule.** If an element has a shadow while nothing is hovering, selected, or dragging it, that's a bug, not a style choice. (This rule exists because it was violated and fixed once already this project — `.off-card` briefly carried both a hover `transform` and a shadow that conflicted with a `mask-image` ancestor and clipped incorrectly; the fix was moving all card-level feedback to box-shadow only, never transform, on that specific component.)

## 5. Components

### Buttons
- **Shape:** Full pill (`border-radius: 999px`)
- **Primary:** Ink background, paper text, `0.9rem 1.8rem` padding
- **Ghost:** Transparent, ink border, ink text
- **Hover:** Primary inverts to paper-bg/ink-text; both variants get a magnetic cursor-follow pull (`translate(x*0.18, y*0.25)`) rather than a color-only hover

### Org / Project Links
- **Shape:** Circle photo (`border-radius: 50%`), pill-shaped external "Visit ↗" affordance elsewhere in Projects
- **Style:** Surface-color backing behind the photo, resting shadow per Elevation, magnetic hover (pull + 1.06 scale) rather than a static hover state
- **Distinctive behavior:** The Involvement section's six org links float in a slow idle wobble (hexagonal cluster, ~185px ring radius) via a lightweight rAF loop, gated to only run while the section is in viewport and skipped entirely under `prefers-reduced-motion`. Two of the six carry an additional hover tooltip (paper card, coral arrow-bullet, `z-index` promoted on hover so it never renders under a neighboring orb's label).

### Cards / Containers
- **Corner style:** 10–20px radius depending on size (never full-pill except true pill buttons/tags)
- **Background:** Surface or paper-deep, never a third arbitrary tone
- **Shadow strategy:** Resting = none or minimal; hover = the lift value above
- **Border:** 1px `--line` hairline where a container needs definition instead of shadow

### Navigation
- Fixed top bar, transparent-to-solid on scroll. Active section indicated by a coral underline (`::after` width transition), driven by an IntersectionObserver scroll-spy rather than manual click-state only.

### Signature Component: Kinetic Hero Title
The hero name (`Nicholas` / italic coral `Moffett`) uses a two-line masked reveal on load: each line sits in an `overflow: hidden` box, inner span at `translateY(110%)`, animating to `0` with a staggered delay between lines. This exact mechanism is reused for every section headline on scroll-into-view, making it a system rule rather than a hero-only flourish.

## 6. Do's and Don'ts

### Do:
- **Do** keep coral to one instance per viewport at rest — the One Accent Rule.
- **Do** reuse the mask-reveal rise for any new headline; don't invent a second entrance animation.
- **Do** keep every clickable element pointed at something real (a live URL, a real repo, a real org page) — never a placeholder `#` or a "coming soon" that isn't labeled as such.
- **Do** gate any new continuous animation (rAF loops, idle motion) behind an `IntersectionObserver` so it only runs in view, and behind `prefers-reduced-motion` so it has a static fallback.
- **Do** write project/experience copy in first person ("I built X because Y"), matching the About section's established voice.

### Don't:
- **Don't** add a numbered eyebrow ("01 — About", "02 — Work"...) to a *new* section without checking first — the site already carries this pattern on every major section, which is itself flagged in PRODUCT.md as sitting close to a known AI-generated-portfolio default. Adding more of them compounds the tell rather than being neutral.
- **Don't** apply `transform` directly to `.off-card` — the mask-image ancestor + border-radius + overflow:hidden combination breaks corner clipping. Scope any hover motion to a child element instead (this was a real, twice-recurring bug).
- **Don't** use `border-left`/`border-right` as a colored accent stripe anywhere.
- **Don't** pair a 1px border with a wide (≥16px blur) drop shadow on the same element — pick one.
- **Don't** write case-study-template copy ("The Problem: Users struggled with X. The Solution: We built Y.") in third person about Nicholas's own work — this already happened once (StackingPlanner/scholairly project copy) and was rewritten into first person after review.
- **Don't** assert a specific number, user count, or achievement without checking it against a real source first — this project has a standing incident history here (AKPsi budget figures, YMCA "five summers," scholairly "100+ active users") and treats it as a hard rule, not a style preference.
