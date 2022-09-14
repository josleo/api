-- Año con más carreras
create view pregunta1 as  select  year , count(year) as cantidad   from  races  group by year order by  cantidad desc limit 1;

-- Piloto con mayor cantidad de primeros puestos
create view pregunta2 as  select name , count(name) as cantidad  from  races  group by name  order by  cantidad desc limit 1;

-- Nombre del circuito más corrido
create view pregunta3 as  SELECT count(r.circuitId) as cantidad , c.name FROM races r inner JOIN circuits c ON c.circuitId = r.circuitId  group  by r.circuitId order by  cantidad desc limit 1;


-- Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
create view pregunta4 as 
select  d.name, sum(r.points) as puntos  
from  results r
inner join  drivers d
on  r.driverId=d.driverId
group by r.driverId
order by puntos desc limit 1;


drop view if exists pregunta1,pregunta2,pregunta3,pregunta4
