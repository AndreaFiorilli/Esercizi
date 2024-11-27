--1)
SELECT  Volo.codice, Volo.comp
FROM Volo
WHERE Volo.durataMinuti>180;
--2)
SELECT DISTINCT Volo.comp
FROM Volo
WHERE Volo.durataMinuti>180;
--3)
SELECT ArrPart.codice, ArrPart.comp
FROM ArrPart
WHERE partenza='CIA';
--4)
SELECT DISTINCT ArrPart.comp
FROM ArrPart
WHERE arrivo='FCO';
--5)
SELECT DISTINCT ArrPart.codice, ArrPart.comp
FROM ArrPart
WHERE partenza='FCO' and arrivo='JFK';
--6)
SELECT DISTINCT ArrPart.comp
FROM ArrPart
WHERE partenza='FCO' and arrivo='JFK';
--7)
SELECT DISTINCT ArrPart.comp
FROM ArrPart, LuogoAeroporto l1, LuogoAeroporto l2
WHERE l1.aeroporto=ArrPart.partenza and l2.aeroporto=ArrPart.arrivo 
and l1.citta='Roma' and l2.citta='New York';
--8)
SELECT Aeroporto.codice, Aeroporto.nome, LuogoAeroporto.citta
FROM ArrPart, Aeroporto, LuogoAeroporto
WHERE LuogoAeroporto.aeroporto=ArrPart.partenza and Aeroporto.codice=ArrPart.partenza
and ArrPart.comp='MagicFly';
--9)
SELECT DISTINCT ArrPart.codice, ArrPart.comp, ArrPart.partenza, ArrPart.arrivo
FROM ArrPart, Aeroporto, LuogoAeroporto l1, LuogoAeroporto l2
WHERE l1.aeroporto=ArrPart.partenza and l2.aeroporto=ArrPart.arrivo 
and l1.citta='Roma' and l2.citta='New York';