DROP TABLE usopenstats19;

CREATE TABLE usopenstats19 AS       
SELECT stats19.player, us_open.finish, stats19.greens,us_open.greens_hit_rank AS usopen_greens , 
stats19.putt_rank, us_open.putts_rank AS usopen_putts, stats19.up_and_down, stats19.distance, us_open.driving_distance AS usopen_distance,
stats19.fairways, us_open.fairways_rank AS usopen_fairways
FROM stats19
JOIN us_open on us_open.player = stats19.player
WHERE us_open.year = 2019;

SELECT * FROM usopenstats19 order by finish asc;