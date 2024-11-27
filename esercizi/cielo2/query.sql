--1)
select a.codice, a.nome, count(distinct comp)
from aeroporto a, arrpart ap 
where ap.partenza=a.codice or ap.arrivo=a.codice
group by a.codice, a.nome;

--2)
select count(*) as numeroVoli
from volo v, arrpart ap 
where v.codice=ap.codice and ap.partenza='HTR' and v.durataminuti>=100;

--3)
select la.nazione, count(distinct aeroporto)
from aeroporto a, arrpart ap, LuogoAeroporto la 
where (ap.partenza=la.aeroporto or ap.arrivo=la.aeroporto) and ap.comp='Apitalia'
group by la.nazione;

--4)
select avg(durataMinuti) as media, max(durataMinuti)as massimo, min(durataMinuti) as minimo
from volo v
where comp='MagicFly';

--5
select a.codice, a.nome, min(c.annoFondaz) as anno
from aeroporto a, arrpart ap, Compagnia c
where (a.codice=ap.arrivo or ap.arrivo=a.codice) and ap.comp=c.nome 
group by a.codice, a.nome;

--6)
select lp.nazione, count(distinct la.nazione)
from arrpart ap, LuogoAeroporto lp, LuogoAeroporto la
where ap.partenza=lp.aeroporto and ap.arrivo=la.aeroporto
group by lp.nazione;

--7)
select a.codice, a.nome, avg(v.durataMinuti)
from aeroporto a, arrpart ap, volo v
where (ap.partenza=a.codice or ap.arrivo=a.codice) and v.codice=ap.codice
group by a.codice, a.nome;

--8)
select c.nome, sum(v.durataMinuti) as durata_tot
from aeroporto a, arrpart ap, Compagnia c, volo v
where (a.codice=ap.arrivo or ap.arrivo=a.codice) and ap.comp=c.nome and c.annoFondaz>=1950 and v.codice=ap.codice
group by c.nome;

--9)
select a.codice, a.nome
from aeroporto a, arrpart ap, Compagnia c
where (a.codice=ap.arrivo or ap.arrivo=a.codice) and ap.comp=c.nome
group by a.codice, a.nome
having count(distinct ap.comp)=2;

--10)
select la.citta
from LuogoAeroporto la 
group by la.citta
having count(distinct aeroporto)>=2;

--11)
select c.nome as compagnia
from Compagnia c, volo v, arrpart ap
where ap.comp=c.nome and v.codice=ap.codice
group by c.nome
having avg(v.durataMinuti) >360;