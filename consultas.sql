
# eliminamos las vistas si ya existen 
drop view if exists pregunta1,pregunta2,pregunta3,pregunta4;

-- Año con más carreras
create view pregunta1 as  select  year , count(year) as cantidad   from  races  group by year order by  cantidad desc limit 1;

-- Piloto con mayor cantidad de primeros puestos
SELECT MAX(gan.driver) as ' carreras ganadas', gan.driverId as piloto, d.name as Nombre 
       FROM (SELECT driverId, COUNT(driverId) as driver
             FROM results
             WHERE positionOrder='1'
             GROUP BY driverId) gan
	    JOIN drivers d 
        ON (gan.driverId=d.driverId);


-- Nombre del circuito más corrido
create view pregunta3 as  SELECT count(r.circuitId) as cantidad , c.name FROM races r inner JOIN circuits c ON c.circuitId = r.circuitId  group  by r.circuitId order by  cantidad desc limit 1;


-- Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British


select driverId,sum(points) as re from results  group by driverId order by driverId asc;
select driverId,sum(points) as re from results  where driverId=154 ;

create view pregunta4 as 
(select r.driverId,sum(r.points) as sumapuntos , d.name , c.nationality
from results r
inner join  drivers d
on  r.driverId=d.driverId
inner join constructor c 
on r.constructorId=c.constructorId
where c.nationality="American"
group by r.driverId limit 1 )
union all
(select r.driverId,sum(r.points) as sumapuntos , d.name , c.nationality
from results r
inner join  drivers d
on  r.driverId=d.driverId
inner join constructor c 
on r.constructorId=c.constructorId
where c.nationality="British"
group by r.driverId limit 1 );
select * from pregunta4 ;
select * from constructor where nationality="American" or nationality="British";




