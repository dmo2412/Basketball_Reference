-- SELECT Distinct us_open.player, us_open.driving_distance
-- from us_open
-- JOIN masters on masters.player = us_open.player
-- Join pga_championship on masters.player = pga_championship.player
-- join open_championship on masters.player = open_championship.player
-- Where us_open.finish = 1 or masters.finish = 1 or pga_championship.finish = 1 or open_championship.finish = 1
-- ORDER BY 

SELECT player, finish, fairways_rank, greens_hit_rank, putts_rank , driving_distance_rank
from open_championship
where finish = 1
-- GROUP BY player
-- -- having count(finish) > 1
order by year DESC;

-- Create masters table with each players stats
-- Create table for all finishes
-- Create table for averages on greens and shit