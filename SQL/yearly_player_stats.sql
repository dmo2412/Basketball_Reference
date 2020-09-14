DROP TABLE scrambling19;
DROP TABLE greens_hit19;
DROP TABLE distance19;
DROP TABLE fairways_hit19;

CREATE TABLE putting19 (
    rem int,
    name VARCHAR(50),
    putt_rank int
);

CREATE TABLE scrambling19 (
    rem int,
    name VARCHAR(50),
    up_and_down int
);

CREATE TABLE greens_hit19 (
    rem int,
    name VARCHAR(50),
    greens int
);

CREATE TABLE distance19 (
    rem int,
    name VARCHAR(50),
    distance int
);

CREATE TABLE fairways_hit19 (
    rem int,
    name VARCHAR(50),
    fairways int
);

-- \copy putting19 from '/Users/dannymorgan/Desktop/Masters_stats/Importing/Putting/putts_hit_2019.csv' Delimiter ',' CSV HEADER;
-- \copy scrambling19 from '/Users/dannymorgan/Desktop/Masters_stats/Importing/Scrambling/up_and_downs_2019.csv' Delimiter ',' CSV HEADER;
-- \copy greens_hit19 from '/Users/dannymorgan/Desktop/Masters_stats/Importing/Greens_hit/greens_hit_2019.csv' Delimiter ',' CSV HEADER;
-- \copy distance19 from '/Users/dannymorgan/Desktop/Masters_stats/Importing/Distance/distance_2019.csv' Delimiter ',' CSV HEADER;
-- \copy fairways_hit19 from '/Users/dannymorgan/Desktop/Masters_stats/Importing/Fairways_Hit/fairways_2019.csv' Delimiter ',' CSV HEADER;