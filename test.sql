DROP TABLE pga_test2;

CREATE TABLE pga_test2
(
    year int,
    player Char(50),
    finish smallint,
    round_1_score smallint,
    round_2_score smallint,
    round_3_score smallint,
    round_4_score smallint,
    Total_score smallint,
    score_to_par smallint,
    money integer,
    place_after_first smallint,
    place_after_second smallint,
    place_after_third smallint,
    place_after_fourth smallint,
    fairways_hit smallint,
    fairways_rank smallint,
    driving_distance real,
    driving_distance_rank smallint,
    greens_hit smallint,
    greens_hit_rank smallint,
    avg_putts real,
    total_putts smallint,
    putts_rank smallint,
    par_3s smallint,
    par_4s smallint,
    par_5s smallint,
    eagles smallint,
    birdies smallint,
    pars smallint,
    bogeys smallint,
    other smallint
);

-- COPY pga_test2(year, player, finish, round_1_score, round_2_score, round_3_score, round_4_score, total_score, score_to_par, money, place_after_first, place_after_second, place_after_third, place_after_fourth, fairways_hit, fairways_rank, driving_distance, driving_distance_rank, greens_hit, greens_hit_rank, avg_putts, total_putts, putts_rank, par_3s, par_4s, par_5s, eagles, birdies, pars, bogeys, other)
-- FROM '/Users
-- /dannymorgan/Desktop/Masters_stats/pga.csv'
-- DELIMITER ','
-- CSV Header;
copy pga_test2 from '/Users/dannymorgan/Desktop/Masters_stats/usopentest.csv'
DELIMITER ',' CSV HEADER;