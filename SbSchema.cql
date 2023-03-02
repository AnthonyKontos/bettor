CREATE KEYSPACE IF NOT EXISTS betData WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor':1};

CREATE TYPE IF NOT EXISTS betData.sourceType (
    abbrevation text, 
    location text, 
    name text, 
    nickname text, 
    short_name text
);

CREATE TYPE IF NOT EXISTS betData.eventgroupType (
    alias text,
    event_group_id int,
    name text
);

CREATE TYPE IF NOT EXISTS betData.scoresType (
    participant_id int, 
    period int,
    points_scored int
);

CREATE TYPE IF NOT EXISTS betData.participantsType (
    is_home boolean,
    participant_id int,
    source frozen<sourceType>
);

CREATE TYPE IF NOT EXISTS betData.lineType (
    market_id int,
    event_id int,
    sportsbook_id int,
    datetime date,
    participant_id int,
    spread_total decimal,
    decimal_odds decimal,
    american_odds int,
    team_id int
);

CREATE TABLE IF NOT EXISTS betData.teams (
    team_id int,
    league_id int, 
    name text,
    nickname text,
    short_name text,
    abbreviation text, 
    location text,
    stadium_type text,
    country text,
    conference_id int,
    division_id int,
    division_name text,
    conference_name text,
    PRIMARY KEY ((conference_id), division_name, nickname)
) WITH CLUSTERING ORDER BY (division_name DESC, nickname ASC);

CREATE TABLE IF NOT EXISTS betData.currentLines (
    entrid int,
    market_id int,
    event_id int,
    sportsbook_id int,
    datetime timestamp,
    participant_id int,
    spread_total double,
    decimal_odds double,
    american_odds int,
    event text,
    market text,
    result text,
    profit double,
    participant_score int,
    sportsbook text,
    participant text,
    participant_full_name text,
    inverse_odds double,
    PRIMARY KEY ((market), inverse_odds, result, event, datetime, participant, sportsbook)
) WITH CLUSTERING ORDER BY (inverse_odds ASC, result DESC, event DESC, datetime DESC, participant DESC, sportsbook DESC);

CREATE TABLE IF NOT EXISTS betData.lineHistory (
    icu boolean,
    market_id int,
    market text,
    event text,
    event_id int,
    sportsbook_id int,
    datetime timestamp,
    participant_id int,
    spread_total double,
    decimal_odds double,
    american_odds int,
    sportsbook text,
    participant text,
    participant_full_name text,
    participant_score int,
    result text,
    profit double,
    PRIMARY KEY ((market), event_id, sportsbook, participant, datetime)
) WITH CLUSTERING ORDER BY (event_id DESC, sportsbook DESC, participant DESC, datetime DESC);

CREATE TABLE IF NOT EXISTS betData.openingLines (
    market_id int,
    event_id int,
    sportsbook_id int,
    datetime timestamp,
    participant_id int,
    spread_total double,
    decimal_odds double,
    american_odds int,
    event text,
    sportsbook text,
    result text,
    participant_score float,
    participant_full_name text,
    participant text,
    profit double,
    market text,
    PRIMARY KEY ((market), event, sportsbook, participant, datetime)
) WITH CLUSTERING ORDER BY (event DESC, sportsbook DESC, participant DESC, datetime DESC);

CREATE TABLE IF NOT EXISTS betData.consensusHistory (
    event_id int,
    market_id int,
    participant_id int,
    system_sportsbook_id int,
    sportsbook_id int,
    wagers int,
    percentage double,
    volume int,
    total_volume int,
    datetime timestamp,
    line_id bigint,
    line frozen<map<text, double>>,
    PRIMARY KEY ((market_id), event_id, participant_id, datetime)
) WITH CLUSTERING ORDER BY (event_id DESC, participant_id DESC, datetime DESC);

CREATE TABLE IF NOT EXISTS betData.Events (
    sport_id int,
    league_id int,
    season_id int,
    event_id int,
    description text,
    location text,
    country text,
    event_status text,
    datetime timestamp,
    stadium_type text,
    scores list<frozen<map<text, int>>>,
    PRIMARY KEY ((event_status), datetime, event_id, location)
) WITH CLUSTERING ORDER BY (datetime DESC, event_id DESC, location ASC);

CREATE TABLE IF NOT EXISTS betData.bestLines (
    market_id int,
    event_id int,
    sportsbook_id int,
    datetime timestamp,
    participant_id int,
    spread_total double,
    decimal_odds double,
    american_odds int,
    event text,
    sportsbook text,
    result text,
    participant_score float,
    participant_full_name text,
    participant text,
    profit double,
    market text,
    PRIMARY KEY ((market), event, sportsbook, participant, datetime)
) WITH CLUSTERING ORDER BY (event DESC, sportsbook DESC, participant DESC, datetime DESC);

