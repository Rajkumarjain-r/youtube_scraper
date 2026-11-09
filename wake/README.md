# Wake (prototype v4: rocket, aliens, missions and hangar)

An endless one-tap game. Slingshot your rocket from star to star, keep it fuelled, and stay ahead of the alien saucer.

Run it: open `index.html` in any modern browser. Tap / click / Space to release; keys 1–4 for boosters.

## In a run
- **Tap** to leave orbit along the dotted line. The label on the target star previews the result: `+6 fuel · ×3 · ◉8`, `EMPTY`, `DRAINS`, `MISS · drift`, `LASSO ×2`, `SNAG −8`.
- **Fuel** drains constantly. Stars' dots are fuel cells; landing refuels. Same-colour landings build a **chain** (×2…×8) that multiplies fuel and score.
- **Coins** sit as an arc on part of each star's orbit. Circling longer collects more but burns fuel. Clearing a whole arc pays +10 bonus coins.
- **Lasso**: cross your exhaust trail around unused stars to take them all at once.
- **The alien saucer** sits as close as your fuel is low. Mistakes (drift, snag, red dwarf, black hole) cost fuel; a second mistake within 4 s makes the tractor beam lunge for double. Warm-up (first 20 jumps): half cost, no lunges.
- **Pickups** on the paths between stars: JET (autopilot, no burn), MAG (pulls coins), 2× (double score), SHLD (blocks one mistake).
- **Pace**: first 20 jumps at 80% speed, then +6% every 20 jumps (cap 1.8×).
- **Game over** when fuel hits 0 ("Abducted!"). **Second Wind** costs 1 ◆ shard, once per run.

## Between runs (saved in the browser)
- **Missions**: 3 at a time, mostly "in one run". Finishing a set gives +1 permanent score multiplier (cap ×30), +1 ◆ and +250 ◉. Targets get harder every 2 sets.
- **Hangar**:
  - Rockets (cosmetic, each with its own exhaust trail): Pathfinder (free), Ember 1,500, Aurora 3,000, Phantom 4,500, Gold Rush 8,000.
  - Upgrades (5 levels: 300 / 700 / 1,500 / 3,000 / 6,000): Comet Jet, Magnet, 2× Score duration, Bigger tank (starting fuel).
  - Boosters: Flare 400, Lens 400, Rewind 500, Nova 700. Booster counts persist; +1 random booster per rocket level in a run.
- **Daily reward**: 7-day streak (100, 200, 300, 1 ◆, 500, 800, 1,500 + one of each booster). Missing a day resets the streak.
- Real-money coin packs are not implemented.

All balance numbers live in `T`, `UPG`, `BOOST`, `ROCKETS`, `DAILY` and `MISSIONS` at the top of the script.
