-- DROP TABLE Playernames;
-- CREATE TABLE Playernames 
-- AS (Select Year, Player, Place from US_Open, Masters, Open_Championship, PGA_Championship);
-- CREATE TABLE Playernames AS (SELECT DISTINCT player from US_Open)
-- Insert Into Playernames(player)
DROP TABLE stats19;

CREATE TABLE stats19 AS
SELECT DISTINCT player, greens_hit19.greens, putting19.putt_rank, scrambling19.up_and_down, distance19.distance, fairways_hit19.fairways
From players
LEFT JOIN greens_hit19 ON players.player = greens_hit19.name
LEFT JOIN putting19 ON players.player = putting19.name 
LEFT JOIN scrambling19 ON players.player = scrambling19.name 
Left JOIN distance19 ON distance19.name = players.player
Left JOIN fairways_hit19 ON fairways_hit19.name = players.player;



DELETE FROM stats19 
WHERE greens is Null And putt_rank is Null And up_and_down is Null and distance is Null and fairways is Null;
SELECT * from stats19 
order by player DESC;