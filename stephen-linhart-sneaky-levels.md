# Stephen Linhart's Sneaky Levels

[Click here to play Stephen Linhart's 30 Lode Runner levels.](https://jpivarski.github.io/jims-loderunner-levels/?levels=stephen-linhart-sneaky-levels.json&readme=stephen-linhart-sneaky-levels.md)

<!-- BEGIN HERE -->

## Placeholder

_(Jim: replace everything between the `BEGIN HERE` and `END HERE` comments with the real
writeup. The notes below came out of a code comment that had nowhere else to live once the
levels moved into their own file; keep whatever is useful and delete the rest.)_

These 30 levels were decoded from `original-files/stephen-linhart-levels.bin`, and all 30
re-encode byte-identically to the original file.

They lean much harder on the engine than my own levels do: 29 of the 30 use the engine's
maximum of five guards and only three chests, several put two or more guards on the same
row, and level 27 is half false brick. That is why the timing and chase rules in this
implementation had to be measured against the original rather than guessed.

<!-- END HERE -->
