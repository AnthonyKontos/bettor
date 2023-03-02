olextract = "INSERT INTO betData.openingLines (market_id, event_id,\
                                               sportsbook_id, datetime, participant_id, spread_total, \
                                               decimal_odds, american_odds, event, sportsbook, result, participant_score, \
                                               participant_full_name, participant, profit, market) \
                                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

evextract = "INSERT INTO betData.events (scores, sport_id, league_id, season_id, event_id, \
                                         description, location, country, event_status, datetime, stadium_type) \
                                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

lhextract = "INSERT INTO betData.lineHistory (icu, market_id, event_id, sportsbook_id, \
                                              datetime, participant_id, spread_total, decimal_odds, american_odds, sportsbook, \
                                              participant, participant_full_name, participant_score, profit, result, event, market) \
                                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                       
clextract = "INSERT INTO betData.currentLines (entrid, market_id, event_id, sportsbook_id, \
                                               datetime, participant_id, spread_total, decimal_odds, american_odds, \
                                               event, market, result, profit, participant_score, sportsbook, \
                                               participant, participant_full_name, inverse_odds) \
                                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                       
teamextract = "INSERT INTO betData.teams (team_id, league_id, name, nickname, short_name, abbreviation, \
                                          location, stadium_type, country, conference_id, division_id, \
                                          division_name, conference_name) \
                                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"                              
                                                               
chextract = "INSERT INTO betData.consensusHistory (event_id, market_id, participant_id, system_sportsbook_id, \
                                                   sportsbook_id, wagers, percentage, volume, total_volume, datetime, \
                                                   line_id, line) \
                                                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                                         
blextract = "INSERT INTO betData.bestLines (market_id, event_id,\
                                            sportsbook_id, datetime, participant_id, spread_total, \
                                            decimal_odds, american_odds, event, sportsbook, result, participant_score, \
                                            participant_full_name, participant, profit, market) \
                                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
