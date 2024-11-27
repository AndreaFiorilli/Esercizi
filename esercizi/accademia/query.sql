select distinct Persona.cognome 
from Persona

select Persona.*
from Persona
where Persona.posizione='Ricercatore'

select Persona.*
from Persona
where Persona.posizione='Professore Associato' and Persona.cognome like 'V%'

select Persona.*
from Persona
where (Persona.posizione='Professore Associato' or Persona.posizione='Professore Ordinario') and Persona.cognome like 'V%'

select Progetto.*
from Progetto
where Progetto.fine < current_date

select Progetto.nome
from Progetto
order by Progetto.inizio

select WP.nome
from WP
order by WP.nome

select distinct Assenza.tipo
from Assenza

select distinct AttivitaProgetto.tipo
from AttivitaProgetto

select distinct AttivitaNonProgettuale.giorno
from AttivitaNonProgettuale
where AttivitaNonProgettuale.tipo='Didattica'

