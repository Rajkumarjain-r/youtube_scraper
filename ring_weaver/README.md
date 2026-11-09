# Ring Weaver (prototype, merge version)

A machine at the bottom blows numbered bubbles (2, 4, 8 … up to 1M = 2^20). They float **up** and pile against the ceiling. Aim the launcher along the bottom and tap to release the next bubble. Two touching bubbles with the same number merge into one with double the value.

Run it: open `index.html` in any modern browser (mouse, touch, or ←/→ + Space). No build step.

## What makes it not just "merge game upside down"

1. **Ceiling outlets with orders.** Three pipes in the ceiling each ask for one exact number. Push a bubble with that number into the pipe to *ship* it: value × 4 points, and the space it took is free again. A wrong bubble resting under a pipe blocks it. New orders track your biggest bubble (biggest −2 … +1), so the goal becomes building the right number in the right place, not hoarding one giant bubble.
2. **Charge shot.** Tap = gentle puff (480 px/s). Hold up to 0.65 s = hard shot (up to 1750 px/s) that shoves the pile, to knock a bubble into a pipe or clear a blocker.

## Rules implemented

- Launched value is random: 2/4/8/16 (weights 40/30/20/10); 32 joins the pool once you've made a 256.
- Merge score = new bubble's value. Merges within 0.7 s of each other form a chain: +25% per step.
- Reaching 1M gives a one-time +1,000,000 bonus. 1M bubbles don't merge further.
- Lose condition: a settled bubble (older than 1.1 s) stays below the red line for 2 s.
- The machine's dial and the HUD bar show how far the pile has grown toward the line.

All balance numbers live in the `T` object at the top of the script.

The earlier "draw a strand through rings" version is in git history (commit before this one).
