# Wake (prototype)

An endless one-tap game. You are a comet climbing through space; everything you fly leaves a permanent trail.

Run it: open `index.html` in any modern browser. Tap / click / Space.

## Rules

- **Orbit and release.** You orbit a star. Tap to leave along the tangent (the dotted line). The first star whose faint ring you enter catches you.
- **Your trail is permanent.** Crossing it kills you…
- **…unless the loop you close contains an unclaimed star.** Every star inside is claimed (100 × n² points) and the loop's trail is erased.
- **Full lap around a star** claims it (+25) and erases that lap.
- **The void rises** from below and speeds up over time. It also eats old trail.
- You also die by flying off the sides, or by flying free for more than 4.2 s.
- Score = distance climbed / 10 + claim points. Speed rises with distance.

All balance numbers live in the `T` object at the top of the script.
