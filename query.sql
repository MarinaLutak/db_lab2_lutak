select number_of_players, name_team from football_team --grafic
select name_team, count(footballer.name_team) as pie_taem from football_team left join footballer using(name_team) group by name_team
select name_footballer, age from footballer 