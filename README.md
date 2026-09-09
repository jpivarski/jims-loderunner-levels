# Jim's Levels

[Click here to play the 86 Lode Runner levels I made when I was a kiddo.](https://jpivarski.github.io/jims-loderunner-levels/)

<a href="https://jpivarski.github.io/jims-loderunner-levels/"><img src="img/level-1.png" alt="Click here to play!" width="500" style="margin-left: auto; margin-right: auto;"></a>

<!-- BEGIN HERE -->

## I didn't invent this game!

Just to be clear: this is [Lode Runner](https://en.wikipedia.org/wiki/Lode_Runner), a hit in 1983 that featured a level editor, spawned a community sharing user-designed levels, [magazine contests](https://cgwmuseum.org/galleries/index.php?year=1985&pub=2&id=21), [books of levels to copy](https://ndlsearch.ndl.go.jp/books/R100000002-I000001903930), and [competitions](https://note.com/cyborgmsx/n/n9c87c5cbef81).

**What you see above are _my_ levels, which I made when I was 10.** I was lucky enough to find my original floppy disks and have access to an old-enough computer, so I got the data by converting the game files to hexidecimal, photographing the text, interpreting it with OCR, and then fixing the transcription errors. Fortunately, the files are very small.

<img src="img/example-hexidecimal.jpg" alt="Old Macintosh screen with hexidecimal of my game level files" width="500" style="margin-left: auto; margin-right: auto;">

## Lode Runner is awesome

It's like chess with reaction time. The architecture of a level forces you to plan how you're going to get all of the golds without getting eaten by the guards, and then implement it. You can't jump, and although you can shoot, you don't shoot the guards. You shoot the floor: to jump through it, to (temporarily) trap a guard, or to dig out some deeply buried gold. But think carefully, because you need a place to stand while digging.

The guards are idiots. They have an algorithm, but it only sometimes involves chasing you. Nevertheless, you need to learn their algorithm because they can carry gold, and you need to get it from them. In some levels, the gold is hidden in places that you can't get to, but you can kill the guards (by burying them and letting the ground swallow them up) to make them respawn, sometimes in the places where you need them.

Also, you fall faster than they do. That can be a part of the puzzle, too.

There's a lot to think about!

## Other levels

My levels are not especially challenging. If you want to solve something fiendishly clever, check out [Stephen Linhart](https://slinhart.com/)'s "Sneaky Levels":

[Click here to play the Stephen Linhart's 30 "sneaky levels".](https://jpivarski.github.io/jims-loderunner-levels/?levels=stephen-linhart-sneaky-levels.json&readme=stephen-linhart-sneaky-levels.md)

<a href="https://jpivarski.github.io/jims-loderunner-levels/?levels=stephen-linhart-sneaky-levels.json&readme=stephen-linhart-sneaky-levels.md"><img src="img/stephen-linhart-level-1.png" alt="Click here to play!" width="500" style="margin-left: auto; margin-right: auto;"></a>

I found them on [a newsgroup from 1997](https://info-mac.org/viewtopic.php?t=5066):

> 30 very tough and interesting levels for Lode Runner. Most of these levels are very intellectual. Some may seem to be impossible, but they have all been done by two or more people. These levels were created by Stephen Linhart and Doug Hewitt. Have fun!

Do you also have Lode Runner levels you'd want to share? [Let me know!](https://github.com/jpivarski/jims-loderunner-levels/issues/new)

## Original levels

Simon Hung's [LodeRunner_TotalRecall](https://github.com/SimonHung/LodeRunner_TotalRecall) is another reimplementation that includes all of the published levels:
* [Lode Runner](https://en.wikipedia.org/wiki/Lode_Runner) (150 levels)
* [Professional Lode Runner](http://www.gb64.com/game.php?id=5906&d=42) (150 levels)
* [Revenge of Lode Runner](http://www.vizzed.com/play/revenge-of-lode-runner-appleii-online-apple-ii-6223-game) (17 levels)
* [Lode Runner Fan Book](https://web.archive.org/web/20230824044358/http://www.spoonbillsoftware.com.au/loderunner.htm) (66 levels)
* [Championship Lode Runner](https://en.wikipedia.org/wiki/Championship_Lode_Runner) (51 levels)

## Who owns Lode Runner? Is this site legal?

The original game was created by Douglas Smith and published by Brøderbund in 1983 ([full story](https://www.filfre.net/2020/12/lode-runner/)). The version I played was ported to the Apple Macintosh in 1984 by Glenn Axworthy. The copyright is now owned by [Tozai Games](https://global.tozaigames.com/), and they created a new version, [Lode Runner Legacy](https://global.tozaigames.com/legacy/) ([Steam](https://store.steampowered.com/app/628660/Lode_Runner_Legacy/)), which includes the classic levels.

This website has none of the classic levels, only ones that I have permission to distribute, and the game engine is rewritten from scratch. It was inspired by Simon Hung's [LodeRunner_TotalRecall](https://github.com/SimonHung/LodeRunner_TotalRecall), which has no license, but I didn't copy any code from it. The pixel art and sounds on this site are also original.

Game rules and algorithms are not copyrightable.

"Lode Runner" is a trademark of Tozai Games. This project is unaffiliated with and unendorsed by Tozai Games or any other rights holder.

<!-- END HERE -->
