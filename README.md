# marvelchamppy
Script I wrote to parse my Marvel Champions BGG play data and perform analysis on it. I wrote it
quick and dirty, because the next phase of my project was to begin translating it to Typescript
and into a static web app.

This script requires a specific format to the data stored in your boardgamegeek.com (BGG) plays.

The villain and the difficulty must appear in the play comments and no abbreviations.  For example, 
if you played against "Expert Ultron", make sure those two words appear in the comments close together
with no other conflicting villain names or villain levels in the comment. In other words, don't
say I something like "I beat expert Ultron with this play and now moving onto expert Klaw". That will
confuse the script!

Also, make sure you enter your username as one of the players even if you're playing solo and multiple
heroes.  The script is looking for the username.  

Put the hero you played in the "Start Position" field for the player with your username. For "Team Color",
enter the name of the aspect you played (not the color).  If you were playing Spider Woman, make sure both
aspects are listed in the "Team Color" box spelled out completely and not abbreviated.  For instance, if you 
played "Justice and Leadership", you could say the following: "Justice/Leadership", "Justice&Leadership",
"Leadership Justice", etc.  

Last but no least, mark the win box so the script can count your wins :)

This script is somewhat forgiving with the hero names, but do your best to spell them correctly.


To run the script, make sure you have Python 3.7+ and requests installed on your system.

Edit the "USER" in marvel_champions_data.py to your BGG username.

Run from a bash shell with the following "./marvel_champions_data.py"
