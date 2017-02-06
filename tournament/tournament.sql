-- ##########################################
-- # Project 3: Tournament Results
-- # Date Started: 02/03/2017
-- # Date Completed: 02/05/2017
-- # Submitted by: Fang Wang
-- ##########################################


-------------------------------------------
-- CREATE new DATABASE instance          --
-------------------------------------------

-- Check for and drop database if exists:
DROP DATABASE IF EXISTS tournament;

-- CREATE and CONNECT to tournament:
CREATE DATABASE tournament;

-------------------------------------------
-- CONNECT TO DATABASE and CREATE TABLES --
-------------------------------------------
\c tournament;

CREATE TABLE players(id SERIAL PRIMARY KEY,
                     name TEXT);


CREATE TABLE matches(match_id SERIAL PRIMARY KEY,
                     winner_id INTEGER REFERENCES players(id),
                     loser_id INTEGER REFERENCES players(id));


-------------------------------------------
-- CREATE VIEWS                          --
-------------------------------------------

-- standings view
-- Contains the players and their win records, sorted by wins.
-- This view is used in player_Standings function.
CREATE VIEW standings AS
	SELECT players.id,
		players.name,
		(SELECT COUNT(*) FROM matches WHERE players.id = matches.winner_id) AS wins,
		(SELECT COUNT(*) FROM matches WHERE players.id = matches.winner_id OR
    players.id = matches.loser_id) AS matches
	FROM players
	ORDER BY wins DESC;
