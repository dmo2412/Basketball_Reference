-- SELECT Distinct us_open.player, us_open.driving_distance
-- from us_open
-- JOIN masters on masters.player = us_open.player
-- Join pga_championship on masters.player = pga_championship.player
-- join open_championship on masters.player = open_championship.player
-- Where us_open.finish = 1 or masters.finish = 1 or pga_championship.finish = 1 or open_championship.finish = 1
-- ORDER BY 

SELECT player, count(finish)
from masters
where finish < 3
GROUP BY player
order by count(finish) DESC;

