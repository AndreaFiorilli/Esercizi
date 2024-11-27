CREATE TABLE Nazione (
    nome varchar not null,
    PRIMARY KEY(nome)
);

CREATE TABLE Regione (
    nome varchar not null,
    nazione varchar not null,
    PRIMARY KEY(nome, nazione),
    FOREIGN KEY nazione 
        references Nazione (nome)
);

CREATE TABLE Citta (
    nome varchar not null,
    regione varchar not null,
    nazione varchar not null
    PRIMARY KEY(nome, regione, nazione),
    FOREIGN KEY(regione, nazione)
        references Regione(nome, nazione)
);

CREATE TABLE Officina (
    nome varchar not null,
    indirizzo Indirizzo not null,
    id Integer not null,
    citta varchar not null,
    regione varchar not null,
    nazione varchar not null,
    PRIMARY KEY(id),
    FOREIGN KEY(citta, regione, nazione)
        references Citta(nome, regione, nazione)
);

CREATE TABLE Riparazione (
    riconsegna timestamp,
    codice Integer not null,
    inizio timestamp not null,
    officina Integer not null,
    veicolo Targa not null,
    PRIMARY KEY(codice),
    FOREIGN KEY(offcina) references Offina(id)
    FOREIGN KEY(veicolo) references Veicolo(targa)
);

CREATE TABLE Marca (
    nome varchar not null,
    PRIMARY KEY(nome)
);

CREATE TABLE TipoVeicolo (
    nome varchar not null,
    PRIMARY KEY(nome)
);

CREATE TABLE Modello (
    nome varchar not null,
    marca varchar not null,
    tipoveicolo varchar not null,
    PRIMARY KEY(nome, marca),
    FOREIGN KEY(marca) references Marca(nome),
    FOREIGN KEY(tipoveicolo) references TipoVeicolo(nome)
);

CREATE TABLE Veicolo (
    targa Targa not null,
    immatricolazione Integer not null,
    modello varchar not null,
    marca varchar not null,
    cliente CodFisc not null,
    PRIMARY KEY(targa),
    FOREIGN KEY(modello,marca) references Modello(nome, marca),
    FOREIGN KEY(cliente) references Cliente(persona)
);

CREATE TABLE Cliente (
    persona CodFisc not null,
    PRIMARY KEY(persona),
    FOREIGN KEY(persona) references Persona(cf),
    v.incl.persona occorre in Veicolo(cliente)
);

CREATE TABLE Persona (
    cf CodFisc not null,
    nome varchar not null,
    indirizzo Indirizzo not null,
    telefono varchar not null, 
    PRIMARY KEY(cf)
);

