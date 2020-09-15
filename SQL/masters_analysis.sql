select masters.year, masters.player, masters.finish, masters.place_after_first, masters.place_after_second, masters.place_after_third, masters_odds.round1 AS opening_odds, 
    CASE
        When round2 > round3 and round2 > round4 then round2
        When round3 > round2 and round3 > round4 then round3
        ELSE round4
    End as max_live_odds
from masters
JOIN masters_odds on masters_odds.name = masters.player and masters_odds.year = masters.year
WHERE masters.finish = 1;


SELECT avg(place_after_first) as first_round_position, avg(place_after_second) as second_round_position, avg(place_after_third) as third_round_position
from masters
where finish = 1;

SELECT player, avg(finish) as average_finish, count(finish) as masters_played
from masters
group by player
having count(player) >= 5
order by average_finish ASC
limit 10;


SELECT round(avg(fairways_rank),1) as fairways_hit_rank, round(avg(driving_distance_rank),1) as driving_distance_rank, round(avg(greens_hit_rank),1) as greens_hit_rank, round(avg(putts_rank),1) as putts_rank
from masters
where finish = 1;

select year, player as winner, fairways_rank, driving_distance_rank, greens_hit_rank, putts_rank
from masters
where finish = 1;

