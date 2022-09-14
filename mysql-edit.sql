ALTER TABLE pit_stops ADD FOREIGN KEY(raceId) REFERENCES races(raceId);
ALTER TABLE results ADD FOREIGN KEY(raceId) REFERENCES races(raceId);
ALTER TABLE results ADD FOREIGN KEY(driverId REFERENCES divers(driverId);
ALTER TABLE results ADD FOREIGN KEY(constructorId) REFERENCES constructor(constructorId);

ALTER TABLE calificacion ADD FOREIGN KEY(raceId) REFERENCES races(raceId);
ALTER TABLE calificacion ADD FOREIGN KEY(constructorId) REFERENCES constructor(constructorId);
ALTER TABLE races ADD FOREIGN KEY(circuitId) REFERENCES circuits (circuitId);
ALTER TABLE results ADD FOREIGN KEY(driverId) REFERENCES drivers (driverId);



UPDATE drivers SET name =REPLACE(forename,';','');
update drivers set name= replace(name, 'forename', '');
update drivers set name= replace(name, 'surname', '');
UPDATE drivers SET name = REPLACE(name, "'", ''); 
UPDATE results SET time =replace(time, '+', '');
