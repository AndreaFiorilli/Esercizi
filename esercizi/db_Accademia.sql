create database DB_Accademia
Create type Strutturato as enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario')
Create type LavoroProgetto as enum ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro')
Create type LavoroNonProgettuale as enum ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro')
Create type CausaAssenza as enum ('Chiusura Universitaria', 'Maternita', 'Malattia')
Create domain PosInteger as integer check ( value >= 0 )
Create domain StringaM as varchar(100)
Create domain NumeroOre as integer Check ( value >= 0 and value <= 8 )
Create domain Denaro as float Check ( value >= 0 )

create table Persona (
    id PosInteger not null,
    nome StringaM not null,
    cognome StringaM not null,
    posizione Strutturato not null,         
    stipendio Denaro not null,
    primary key (id)
);

create table Progetto (
    id PosInteger not null,
    nome StringaM not null,
    inizio Date not null,
    fine Date not null check(inizio<fine),
    budget Denaro not null,
    primary key (id),
    unique (nome) 
);

create table WP (
    progetto PosInteger not null,
    id PosInteger not null,
    nome StringaM not null,
    inizio date not null,
    primary key (progetto, id),
    fine Date not null check(inizio<fine),
    unique(progetto, nome),
    foreign key (progetto) references Progetto ( id ) 
);

create table AttivitaProgetto (
    id PosInteger not null,
    persona PosInteger not null,
    progetto PosInteger not null,
    wp PosInteger not null,
    giorno date not null,
    tipo LavoroProgetto not null,
    oreDurata NumeroOre not null,
    primary key (id),
    foreign key (persona) references Persona ( id ),
    foreign key (progetto, wp) references WP ( progetto,id )
);

create table AttivitaNonProgettuale (
    id PosInteger not null,
    persona PosInteger not null,
    tipo LavoroNonProgettuale not null,
    giorno date not null,
    oreDurata NumeroOre not null,
    primary key (id),
    foreign key (persona) references Persona ( id )
);

create table Assenza (
    id PosInteger not null,
    persona PosInteger not null, 
    tipo CausaAssenza not null,
    giorno date not null,
    primary key (id),
    unique(persona, giorno),
    foreign key (persona) references Persona ( id )
);