# Jim's Levels

86 Lode Runner levels I designed when I was 10 years old, playable in a browser.

**[▶ Play](https://jpivarski.github.io/jims-loderunner-levels/)**

The whole game is a single `index.html` — no build step, no libraries, no external
requests. Open it and press any key to start.

Every level begins frozen and unshaded, so you get to read the board and plan a
route before anything can reach you. That includes after you are caught: press a
key when you are ready.

<!-- COPY HERE -->

## Controls

Both control sets are live at the same time and are fully interchangeable, so you
can play left-handed, right-handed, or with a hand on each.

| Action | Left hand | Right hand | Arrows |
|---|---|---|---|
| move left | `A` | `J` | `←` |
| move right | `D` | `L` | `→` |
| climb up | `W` | `I` | `↑` |
| climb down | `S` | `K` | `↓` |
| shoot the block down-left | `Q` | `U` | — |
| shoot the block down-right | `E` | `O` | — |

`Space` pause · `R` restart the level · `[` `]` previous/next level ·
type a number then `Enter` to jump to a level · `M` mute ·
`T` switch between hold-to-move and latched (Apple II style) movement

## How it plays

Collect every chest on the screen. When the last one is gone, hidden ladders appear
and you escape out the top row. The border around the playfield is there so you can
tell whether a ladder actually reaches the top. Guards chase you; shoot a hole in a brick floor to
drop one in, and you can run across its head while it struggles. Holes fill back in
after a few seconds — and they will crush whatever is still standing in them,
including you.

Steel blocks cannot be shot. Some bricks are false and you fall straight through.
Lives are infinite and there is no score: the only goal is the next screen.

## About the levels

The levels came off a 34 KB file I wrote as a kid, in the Apple II layout: 224 bytes
per level holding 448 nibbles for a 28×16 grid, low nibble the left tile and high
nibble the right. 86 of the 151 available slots were filled. The decoded levels are
embedded in `index.html` as ASCII art, and 85 of the 86 re-encode byte-identically to
the original file. Two cells in level 16 held tile values that do not exist (13 and
14); both were isolated cells in open space, and I render them as empty.

## Provenance and credits

Everything here — the engine, the pixel art, the synthesized sound, and the level
designs — is my own original work, under the BSD 3-Clause license in `LICENSE`. Note
that the third clause means my name may not be used to endorse derived works without
permission.

The mechanics reimplement the 1983 original by **Douglas E. Smith**, published by
**Brøderbund**. Game rules and algorithms are not copyrightable, so this is a
from-scratch implementation of behavior, not a port.

While building it I read **[LodeRunner_TotalRecall](https://github.com/SimonHung/LodeRunner_TotalRecall)**
by **Simon Hung** as a behavioral reference for timing constants and guard AI. That
project carries no license of any kind, so none of its code, sprites, or audio is
used here — only my own reimplementation of the behavior it documents.

*Lode Runner* is a trademark of **Tozai Games**. This project is unaffiliated with and
unendorsed by Tozai Games or any other rights holder, and contains none of the
commercial level data — only my 86 levels.
