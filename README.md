# cis-1051-final-project
Final project for CIS 1051

So, here we are. This was, ultimately, a lot of work and a lot of fun. There's still a bit I'd like to do with this project - this is definitely going to be a program I'll use myself on a regular basis - but I'm satisfied with all I managed to do before the deadline. I initially wanted to add double blank functionality, but, given my coding style (that is to say, my bespoke inefficiency), getting the result of an input with two blanks would probably take at least a good few minutes of real time, so I opted against it after seeing how long it took with just one. That's the only major compromise I'd say I had to make, though - the rest of the program works pretty much how I'd envisioned it to from the get-go. It's, of course, a bit drab, but functionally, I'm pretty proud of what I've managed to do in just over a week (yeah, we Hildebrands are pretty notorious procrastinators - but, as you can see, we always get it done in the end!).

Perhaps it's just because it's most fresh in my mind, seeing as I worked it out earlier today, but one of the trickiest things here was working out how, if the letter imitated by a blank tile falls on a double-letter score, to ensure it's not the blank that lands there. An example will probably better explain what I'm talking about - in the video, I use the example rack "fraz?le", with "?" representating the blank, to show blank functionality. To maximize score with the play of "frazzle", you have to get the second Z to land on the double-letter score (as the first one can't reach it) and, furthermore, you have to in turn label the blank as the first Z, not the second, because otherwise you find yourself doubling a tile score of zero. As with most things, it seems simple in hindsight (now that I know how it's done, of course), but I must admit I was stuck on that issue of how to get the program to turn the right copy of the tile into a blank for a good bit of today and yesterday.

Then, of course, there's the fact that I had to learn the basics of pygame (Pygame? PyGame? Not sure exactly how, if at all, to capitalize it) for the visual aspect, but that wasn't too bad - it's decently intuitive, once you work out "blitting", and the example programs were rather helpful. A notable stitch there was figuring out key repetition - you don't really notice it (actually, I'm sure you have, being a programmer, but I certainly didn't until this project), but games interpret keypresses slightly yet significantly different from how your keyboard behaves otherwise. If you hold down a key when, say, you're typing something, your computer generally registers one key press, and, if the key is held for longer than, say, half a second or so, then the chained inputs begin. Not so with games - if you're holding down the D button to move to the right, you don't want to move forward a pixel, wait for half a second, and then begin walking; you want to get going as soon as possible (yes, I'm sure you know all this by now, but this is for my own benefit - they say explaining something is the best way to learn it yourself, after all). Naturally, pygame defaults to the latter, being (believe it or not) primarily game-focused, so I had to work out how to put that delay back in to avoid adding three or four A's to the rack with a single key press. My solution was to implement a variable, on if no keys are pressed and off otherwise, and have key presses only function when this variable is turned on, forcing each key press to register once, and only once, until the key is lifted. It means you can't, say, hold down backspace to clear a rack - you've gotta press it seven separate times - but it allows you more control than the alternative without having to treat your keyboard as a stovetop.

It does feel a bit silly adding each of the tiles and numbers used in the program as separate files to this repository, but, if you want the experience as it was meant to be, I suppose you're going to need them.

In any case, that's about it from me. I hope this program amused you for a minute, because I don't imagine it achieved either of the other avenues toward getting an A, and I bid you good luck on the rest of your project-reviewing escapade - unless this is the final one, in which case, I bid you fair rest after what must undoubtedly have been quite the long day.

Video link: https://www.youtube.com/watch?v=7gg_oN4djKU
