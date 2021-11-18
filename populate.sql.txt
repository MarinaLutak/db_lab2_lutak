
INSERT INTO football_league(id_league, name_league)
VALUES(10001, 'French Ligue 1');
INSERT INTO football_league(id_league, name_league)
VALUES(10002, 'Spain Primera Division');
INSERT INTO football_league(id_league, name_league)
VALUES(10003, 'Italian Serie A');
INSERT INTO football_league(id_league, name_league)
VALUES(10004, 'English League Championship');
INSERT INTO football_league(id_league, name_league)
VALUES(10005, 'Ukrainian Premier League');


INSERT INTO football_team(name_team, id_league, coach, number_of_players, stadium)
VALUES('Paris Saint-Germain', 10001, 'Mauricio Roberto Pochettino Trossero', 28, 'Parc des Princes');
INSERT INTO football_team(name_team, id_league, coach, number_of_players, stadium)
VALUES('Real Madrid', 10002, 'Carlo Ancelotti', 31, 'Estadio Santiago Bernabéu');
INSERT INTO football_team(name_team, id_league, coach, number_of_players, stadium)
VALUES('Juventus', 10003, 'Massimiliano Allegri', 36, 'Allianz Stadium');
INSERT INTO football_team(name_team, id_league, coach, number_of_players, stadium)
VALUES('Dynamo Kyiv', 10005, 'Mircea Lucescu', 29, 'NSC «Оlimpiyskiy»');
INSERT INTO football_team(name_team, id_league, coach, number_of_players, stadium)
VALUES('Blackpool', 10004, 'Neil Critchley', 30, 'Bloomfield Road');


INSERT INTO footballer(id_footballer, name_team, name_footballer, age)
VALUES(231747, 'Paris Saint-Germain', 'K. Mbappé', 22);
INSERT INTO footballer(id_footballer, name_team, name_footballer, age)
VALUES(158023, 'Paris Saint-Germain', 'L. Messi', 34);
INSERT INTO footballer(id_footballer, name_team, name_footballer, age)
VALUES(20801, 'Juventus', 'Cristiano Ronaldo', 36);
INSERT INTO footballer(id_footballer, name_team, name_footballer, age)
VALUES(190871, 'Paris Saint-Germain', 'Neymar Jr', 29);
INSERT INTO footballer(id_footballer, name_team, name_footballer, age)
VALUES(165153, 'Real Madrid', 'K. Benzema', 33);
INSERT INTO footballer(id_footballer, name_team, name_footballer, age)
VALUES(15983, 'Dynamo Kyiv', 'G. Bushchan', 27);