# Wake (prototype v5: rocket, mothership, missions and hangar)

An endless one-tap game. Slingshot your rocket from star to star, keep it fuelled, and stay ahead of the alien mothership.

Run it: open `index.html` in any modern browser. Tap / click / Space to release; keys 1–4 for boosters.

## In a run
- **Tap** to leave orbit along the dotted line. Stars no longer bend your flight, so the line is exactly where you go (only black holes pull, marked PULL!). If the preview names a star, you land on it. Stars are spaced so their catch rings never overlap (rings grow at most 1.25× during a run), and when you tap, any star whose ring you're already inside is ignored until you've left it, so a tap never snaps you back to a neighbour.
   The label on the target star previews the result: `+6 fuel · ×3 · ◉8`, `EMPTY`, `DRAINS`, `MISS · drift`, `LASSO ×2`, `SNAG −8`.
- **Fuel** drains constantly. Stars' dots are fuel cells; landing refuels. Same-colour landings build a **chain** (×2…×8) that multiplies fuel and score.
- **Coins** sit as an arc on part of each star's orbit. Circling longer collects more but burns fuel. Clearing a whole arc pays +10 bonus coins.
- **Lasso**: cross your exhaust trail around unused stars to take them all at once. Crossing your trail is otherwise harmless (no snag penalty).
- **The alien mothership** (a dome spanning the whole screen, with a tracking eye and tractor beam) only shows up when you slip, like the chaser in a runner game. After any mistake (drift or black hole) it swoops in and **hunts you for 6 s** ("ALIENS!" timer). Another mistake while it hunts makes the tractor beam lunge for double cost. Play clean and it gives up ("SHAKEN OFF"). It also appears whenever fuel is below 20%. Warm-up (first 20 jumps): half cost, no lunges.
- **Engine burn**: when a black hole is pulling you or you're drifting, tap to burn (−4 fuel) toward the nearest safe star. If you sit in a pull for 1.8 s the rocket auto-ejects. Looping around a black hole never counts as a snag or a drift.
- **Pickups** sit in the centre of about 1 in 8 stars: JET (autopilot, no burn, rarest), MAG (pulls coins), 2× (double score), SHLD (blocks one mistake). Land on the star to collect it. The star's core shows the pickup with a glow and beacon ring, and the preview label adds `+JET`/`+MAG`/`+2×`/`+SHLD` when you're aiming at it.
- **Pace**: first 20 jumps at 80% speed, then +6% every 20 jumps (cap 1.8×).
- **Black holes** (sector 2+): never closer than 520 px to each other, so two can't wall off the path. JET flies straight through them (no pull, no hit). Gentle pull (0.45 strength, 1.8× reach), small core. A hit costs 10 fuel, throws you toward the nearest safe star and gives 1.5 s of protection, so one hit is one mistake. The preview marks holes on your path with PULL!
- **Game over** when fuel hits 0 ("Abducted!"). **Second Wind** costs 1 ◆ shard, once per run: you restart in orbit around the nearest safe star with 40 fuel, a cleared trail, the saucer pushed back and 3 s of protection.

## Between runs (saved in the browser)
- **Missions**: 3 at a time, mostly "in one run". Finishing a set gives +1 permanent score multiplier (cap ×30), +1 ◆ and +250 ◉. Targets get harder every 2 sets. Mission types: coins, chain, lasso, jumps, sector, pickups, clean landing streak, coin rings, score.
- **Hangar**:
  - Rockets (cosmetic, each with its own exhaust trail): Pathfinder (free), Ember 1,500, Aurora 3,000, Phantom 4,500, Gold Rush 8,000.
  - Upgrades (5 levels: 300 / 700 / 1,500 / 3,000 / 6,000): Comet Jet, Magnet, 2× Score duration, Bigger tank (starting fuel).
  - Boosters: Flare 400, Lens 400, Rewind 500, Nova 700. Booster counts persist; +1 random booster per rocket level in a run.
- **Daily reward**: 7-day streak (100, 200, 300, 1 ◆, 500, 800, 1,500 + one of each booster). Missing a day resets the streak.
- Real-money coin packs are not implemented.

All balance numbers live in `T`, `UPG`, `BOOST`, `ROCKETS`, `DAILY` and `MISSIONS` at the top of the script.

Removed: red dwarfs, the snag penalty for crossing your own trail, and trail close shaves (black-hole close shaves remain).
