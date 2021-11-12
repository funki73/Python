friendsselect * from countries;
select * from cities;

-- Question 1 --
select countries.name, languages.language, languages.percentage
from languages
join countries on countries.id = languages.country_id
where languages.language = "slovene" 
Order by percentage desc;

-- Question 2 (Level 3) --
select countries.name, COUNT(country_id)
AS city_count
from cities
join  countries on countries.id = cities.country_id
group by countries.id
order by city_count DESC;

-- Question 3 --
select countries.name, cities.name, cities.population
from cities
join countries on countries.id = cities.country_id
where country_id = '136'
and cities.population > '500000'
order by population desc;

-- Question 4 --
select countries.name, languages.language, languages.percentage
from languages
join countries on countries.id = languages.country_id
where percentage > '89%'
order by percentage desc;

-- Question 5 (Level 2) --
select name, surface_area, population
from countries
where surface_area < '502'
and population > '100000';

-- Question 6 --
select name, life_expectancy, government_form, capital
from countries
where government_form like "Constitutional Monarchy" 
and life_expectancy > '75'
and capital > '200';

-- Question 7 (Level 2)
select countries.name, cities.name, cities.district, cities.population
from cities, countries
where countries.name = "Argentina"
and cities.district = "Buenos Aires"
and cities.population > '500000';

-- Question 8 (Level 2)
select region, Count(region)
as country_count
from countries
group by region
order by country_count DESC;