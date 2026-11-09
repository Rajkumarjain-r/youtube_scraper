# Wake (prototype v2: burning out)

An endless one-tap game. Your comet's **Light** is burning out. Hop from star to star to refuel and climb as far as you can before it goes dark.

Run it: open `index.html` in any modern browser. Tap / click / Space to release; keys 1–4 for boosters.

## Why each tap matters
- **Fuel.** Landing on a star absorbs its sparks (1–3 dots) into Light. Used stars turn grey.
- **Colour chain.** Same colour as your last star raises the chain (×2 … ×8): more Light (+35% per step) and more score. A different colour resets it.
- **Lasso.** Crossing your trail around unused stars absorbs them all at once (×1.5 Light bonus, score × stars).
- **Preview.** While orbiting, the dotted line shows exactly what this tap gets: `+6 light · ×3`, `EMPTY`, `DRAINS`, `MISS · drift`, `LASSO ×2` or `SNAG −8`.

## Mistakes are setbacks, not deaths
| Mistake | Cost |
|---|---|
| Miss | You drift (−5 Light/s) until the nearest star reels you in |
| Wrong colour | Chain resets |
| Crossing trail around nothing | Snag, −8 Light |
| Red dwarf (sector 2+) | Drains −7 Light/s while orbiting, breaks chain |
| Black hole core (sector 3+) | −15 Light, flung away |

## Growth and the end
- Light drains constantly: 1.6/s, +12% per comet level, +6% per sector.
- Absorbed Light fills XP. Each **comet level**: faster, bigger catch radius, hotter burn, +1 random booster.
- **Sectors** every 2,600 px: 2 red dwarfs, 3 black holes, 4 colour clusters, 5+ deep space.
- **Game over:** Light hits 0. Score = distance/10 + spark score. One **Second Wind** per run relights at 30%.

## Boosters (start with 2 each; +1 random per level)
| Booster | Effect |
|---|---|
| Flare | +50 Light instantly |
| Gravity Lens | Next 3 shots home onto a good star (prefers your chain colour) |
| Rewind | Undo the last tap: position, Light, chain and used stars restored |
| Supernova | Absorb every unused star within range and wipe the whole trail |

All balance numbers live in the `T` object at the top of the script.
