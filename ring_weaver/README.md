# Ring Weaver (prototype)

A machine puffs smoke rings. Hold and drag to draw one unbroken strand through them; lift to tie it off. Finished patterns vent boiler pressure and score points. Reach 100 psi and the machine overloads.

Run it: open `index.html` in any modern browser (mouse or touch). No build step, no dependencies.

## Rules implemented

| Pattern | Condition | Effect |
|---|---|---|
| Chain | 2+ rings threaded in one strand | `n² × 5` points |
| Harmony | all rings same colour, 3+ | ×2 |
| Weave | turns alternate L/R at each ring, 4+ | ×1.5 |
| Orbit | same turn direction at every ring, 4+ | ×1.5 |
| Loop | strand ends where it started, 3+ | ×1.5 |
| Double | same ring threaded twice | ×1.5 |
| Knot | strand crosses itself | +25% per crossing (max 4) |
| Combo | consecutive 2+ chains | +10% each (max +100%) |

Pressure vented per pattern: `min(55, (5 + 4n) × multiplier)`.

Mistakes / pressure sources:
- Passive build-up that ramps over time.
- Unthreaded ring drifts off the top: +3 psi.
- Ember ring (dark red, dashed) touched by the strand: strand snaps, +14 psi, combo reset.
- Strand length is capped (ink budget, ring around the cursor); running out auto-ties the strand.

All balance numbers live in the `T` object at the top of the script.
