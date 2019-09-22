# best-nba-matchups
This project parses a complete CSV of games to identify the best matchups of the NBA season.


## How to customize

Customize this repo by changing the team names and "scores" in `goodteams.csv`. A team with a higher score is considered to have more interesting games; use any positive number for a team's score. From this file, each matchup is a given a score, and the matchups are sorted into tiers by how interesting you decided each should be.

After customizing `goodteams.csv`, run the project as follows

```
python3 process.py
```

You can then find your custom schedule written to `result.html`.

To view this compiled, you can use [HTML Preview](http://htmlpreview.github.io/?https://github.com/dnoursi/best-nba-matchups/blob/master/results.html).

## Thanks

The CSV file `allgames.csv` was downloaded from Fixture Download [at this URL](https://fixturedownload.com/results/nba-2019), thanks to Fixture Download!
