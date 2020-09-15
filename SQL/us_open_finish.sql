select year, player, finish, fairways_rank, driving_distance_rank, greens_hit_rank, putts_rank
from us_open
WHERE year in (   
    select YEAR
    from us_open
    group by year 
    having min(score_to_par) >= 0
) AND finish <= 5
