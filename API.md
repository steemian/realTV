*Here's the API for AI contest #2*

## The Real TV show problem

All you need to know about the problem is described on [the contest page](https://steemit.com/aicontest/@gbd/the-ai-contest-2-real-tv). You're on an island and cooperate for a common challenge, then vote for elimination of one player. Like on TV.

<center>
![AiContest](https://s19.postimg.org/mz2ksxjub/Ai_Contest-steem.jpg)
</center>



### The rules

Available `Player` AI scripts will be instantiated a total of 11 times, with different strength scores, ranging from 0 to 10. Then, for each phase, `Player` instances are randomly dispatched into islands of 12 instances, adding only the minimal amount of bots to fill the missing slots. A total of 100 phases are run, which means that each `Player` will visit one hundred different tropical islands. Lucky AIs!

On each island, every day:
* First, players vote for elimination
* Players who voted for themselves are considered traitors, and all traitors leave the island
* Non-traitor players have to solve a trial together. The sum of their strength must be equal or more than the `difficulty`, or they collectively fail and the island is disbanded
* Then the remaining player with the most votes leaves the island. If there's a tie, players are called again for tie break. In case of a second tie, the weakest player leaves. If they are same strength, the leaver is randomly chosen
* Next day starts unless there is only one player left (that player wins) or no player at all (no winner and no points awarded)

```
difficulty = 7*n - 3        
   # where n is the number of non-traitor players currently on the island
```

<center>
![Island](https://s10.postimg.org/zf0vo9z5l/maldives-500.jpg)
</center>

Points are awarded:
* 3 points to each player who participate in beating a challenge
* 100 points for the last man standing on an island (plus up to 36 points awarded for beating the challenges)
* No extra point awarded if all survivors betray at once
* 100 points distributed among all traitors if the team fails the challenge

Bots will spawn with strength randomly selected from allowed values (0 to 10). They vote for elimination of the weakest player 80% of the time, for the strongest 20% of the time (including itself). As usual, bots are recreated anew for each phase.

Here are the constants:

```
    PLAYERS_PER_ISLAND = 12

    PHASES_PER_GAME = 100
    SCORE_FOR_TRIAL = 3
    SCORE_FOR_LASTMAN = 100
    SCORE_FOR_EACH_TRAITOR = 0
    SCORE_FOR_ALL_TRAITORS = 100

    INSTANCES_STRENGTH = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    INSTANCES_PER_PLAYER = len(INSTANCES_STRENGTH)
    
    DIFFICULTY_A = 7           # round difficulty is A*n + B
    DIFFICULTY_B = -3

```




<center>
![Island](https://s10.postimg.org/7ro6a6teh/quay-500.jpg)
</center>

### Implement this

```
class Player:
    
    def getSteemUser(self):                              # return your steem name
        return "@gbd"

    def voteForElimination(self, context):               # override this
        # return either a Player or a PlayerContext
        # invalid entries and voting for self will be interpreted betraying

    def voteForTie(self, context):                       # override this
        # return either a Player or a PlayerContext
        # It is too late for betrayal, invalid entries will be ignored
```


And here's the `Context` object you'll get as argument

```
class PlayerContext:
    # self.id               a unique string identifier for this instance
    # self.name             classname this player is implementing
    # self.previousMoves    [(PlayerContext, PlayerContext)] 
    #                          votes cast by this instance: (firstVote, TieBreak)
    # self.strength         strength of that instance
    # self.score            score of that instance (updated at the beginning of day)

class GameContext:
    # self.totalBots        total number of bots in the whole arena
    # self.totalHumans      total number of non-bot instances in the whole arena
    # self.phaseIndex       index of the phase 
    #                          (ie. number of islands you've been in before this one)

class Context:
    # self.islandIndex          probably not useful for you
    # self.game                 GameContext object
    # self.activePlayers        {id: PlayerContext}, players still on the island 
    #                               at the beginning of the day
    # self.betrayers            {id: PlayerContext}, those who will share the 
    #                               bounty if you lose
    # self.eliminatedPlayers    {id: PlayerContext}, those who lost
    # self.currentTies          {id: PlayerContext}, only available in case of a tie
```


And here's your first opponent


```
from Game.Const import Const
from Game.Player import Player
        
class LikesThemStrong (Player):     # Always votes for the weakest (including itself)
    
    def getSteemUser(self):
        return ""

    def voteForElimination(self, context):
        return min(context.activePlayers.values(), key=lambda p: p.strength)

    def voteForTie(self, context):
        return min(context.currentTies.values(), key=lambda p: p.strength)
```


### And here you go!
You have until friday february 23 to submit AI scripts to the contest. Up to 5 AIs and one prize per account. You have two ways to submit an AI script, in order of preference:

* Directly file a pull request on the [project github](https://github.com/steemian/realTV)
* Post a comment with a link to the code hosted on a [gist](https://gist.github.com/) or somewhere else online

And don't forget to leave a reply with a link and a short explanation of how your AI works



### Read my previous posts


* The post [introducing the contest](https://steemit.com/aicontest/@gbd/the-ai-contest-2-real-tv) (or  ![french](https://steemitimages.com/0x0/https://s9.postimg.org/3mpd3j2sf/flag-fr-qc_14x21.png) *[french translation](https://steemit.com/aicontest/@gbd/fr-the-ai-contest-2-tele-realite)*)
* The [rules post](https://steemit.com/aicontest/@gbd/the-ai-contest-coming-soon) (or  ![french](https://steemitimages.com/0x0/https://s9.postimg.org/3mpd3j2sf/flag-fr-qc_14x21.png) *[french translation](https://steemit.com/aicontest/@gbd/the-ai-contest-bientot-sur-steem)*)
* The [payout for previous contest](https://steemit.com/aicontest/@gbd/the-ai-contest-1-results-are-out)


Vote the [Ai Contest](https://steemit.com/created/aicontest) posts to add money to the prize pool !

*(many thanks to the authors I link to, including anonymous Wikipedians)*
*Source of images: [Pixabay](https://www.pexels.com/u/pixabay/), Creative Commons CC0