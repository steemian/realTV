*Here's the API for AI contest #2*

## The Real TV show problem

All you need to know about the problem is described on [the contest page](https://steemit.com/aicontest/@gbd/the-ai-contest-2-real-tv). You're on an island and cooperate for a common challenge, then vote for elimination of one player. Like on TV.

<center>
![AiContest](https://s19.postimg.org/mz2ksxjub/Ai_Contest-steem.jpg)
![French](https://s9.postimg.org/3mpd3j2sf/flag-fr-qc_14x21.png) *(read the [french translation](https://steemit.com/aicontest/@gbd/))*
</center>



### The rules

Available `Player` AI scripts will be instantiated a total of 11 times, with different strength scores, ranging from 0 to 10. Strength is used for common challenge. Then, for each phase, instances are randomly dispatched into islands of 12 instances, adding only the minimal amount of bots. A total of 100 phases are run, which means that each player will visite one hundred different tropical islands. Lucky AIs!

On each island, every day:
* First, players vote for elimination
* Players who voted for themselves are considered traitors, and all traitors leave the island
* Non-traitor players have to solve a trial together. The sum of their strength must be equal or more than the `difficulty`, or they collectively fail and the island is disbanded
* Then the remaining player with the most votes leaves the island. If there's a tie, players are called again for tie break. In case of a second tie, the weakest player leaves. If they are same strength, the leaver is randomly chosen
* Next day starts unless there is only one player left (that player wins) or no player at all (no winner and no points awarded)

```
difficulty = 7*n - 3 		# where n is the number of players on the island
```

<center>
![Island](https://s10.postimg.org/zf0vo9z5l/maldives-500.jpg)
</center>

Points are awarded:
* 3 points to each player who participate in beating a challenge
* 100 points for the last man standing on an island
* no point awarded if an island ends on an unresolved tie (and all remaining players are eliminated)
* 100 points distributed among all traitors if the team fails the challenge

Bots will spawn with strength randomly selected from allowed values (0 to 10), and vote for elimination of the weakest player 80% of the time, for the strongest 20% of the time (including itself). As usual, bots are recreated anew for each phase

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
    
    DIFFICULTY_A = 7           # actual difficulty is A*n + B where n is the number of remaining players
    DIFFICULTY_B = -3

```




<center>
![Island](https://s10.postimg.org/7ro6a6teh/quay-500.jpg)
</center>





Well, your AIs will land on an artificial island, it's better than nothing. A certain amount of AIs (I'll tell you exactly how many in a while) will spawn on islands, together with stupid bots to fill the gaps.

Every day, all islanders will have to cooperate to solve a challenge together. Of course this challenge will get a little harder every day. Then islanders will vote to eliminate one of them. And days pass until either they fail the trial (and everybody lose) or the last man beats the last trial alone. (and this one wins).

You score points for every day you survive, a lot of points if you win, and some points if you decide to leave the island before the others fail the challenge.


### The trick ...

And there is a trick of course. Not all AIs are created equal for the challenge. Each participant (`Player`) in the contest will have several instances, with various strength scores, and instances will be randomly dispatched through islands. You'll have to chose between eliminating the weakest islander to get better chances, get rid of the strong ones that could beat you at the end, or just betraying the team to bet on their failure


See how vague the descriptions are for every number? I need to fine-tune the numbers to keep some balance, so I'm going to publish those in a few days. With precise rules and python interfaces. So right now you should just get prepared and think of your strategy. Just have a look at the [code on github](https://github.com/steemian/realTV)



## And the other contests?

*(read more on [AI Contest introductory post](https://steemit.com/aicontest/@gbd/the-ai-contest-coming-soon))*

The previous [Public Goods contest](https://steemit.com/aicontest/@gbd/the-ai-contest-1-public-goods-problem) is closed since yesterday. Results (and payouts) will be published soon. Thanks to all participants : @amosbastian, @grungealpha, @laxam, miripiri and @scorpil

### What if I'm not a programmer

Again, this is not a problem. Post your idea, I will implement it and watch it compete. Or learn Python, it's not that difficult! 

### The rewards

As usual, 90% of the prize pool will be redistributed, but there will be two slight changes for the payouts. Participants will be ranked based on the *total* score of their best-performing AI. Prize pool will be the sum of all payouts for posts and comments with the tag [AiConstest](https://steemit.com/created/aicontest) that have seen payout during the challenge (including fr the previous session). The rest of payouts will go to the next contest to be held.

* 1st participant: 30% of total rewards
* 2nd participant: 25%
* 3rd participant: 20%
* 4th participant: 15%
* 10% are kept for myself

Upvote to add money to the pool.



### Read my previous posts


* The post [introducing the contest](https://steemit.com/aicontest/@gbd/the-ai-contest-1-public-goods-problem) (or  ![french](https://steemitimages.com/0x0/https://s9.postimg.org/3mpd3j2sf/flag-fr-qc_14x21.png) *[french translation](https://steemit.com/aicontest/@gbd/fr-the-ai-contest-1-le-dilemme-du-bien-commun)*)
* The post [rules post](https://steemit.com/aicontest/@gbd/the-ai-contest-coming-soon) (or  ![french](https://steemitimages.com/0x0/https://s9.postimg.org/3mpd3j2sf/flag-fr-qc_14x21.png) *[french translation](https://steemit.com/aicontest/@gbd/the-ai-contest-bientot-sur-steem)*)
* [Welcome message for non-programmers](https://steemit.com/aicontest/@gbd/the-ai-contest-1-non-programmers-welcome)

*(many thanks to the authors I link to, including anonymous Wikipedians)*
*Source of images: [Pixabay](https://www.pexels.com/u/pixabay/), Creative Commons CC0