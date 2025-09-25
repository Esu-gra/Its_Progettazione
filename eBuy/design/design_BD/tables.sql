
create table categoria(
    nome Stringa primary key,
    super Stringa,
    check(nome<>super)
);

-- alter table categoria 
-- add foreign key (super) references categoria(nome)


-- recursive

create table utente(
    username Stringa primary key,
    registrazione timestamp
);

create table privato(
    utente Stringa primary key,
    foreign key(utente)
       references utente(username)
);


create table venditoreprof(
    utente Stringa primary key,
    vetrina URL not null,
    unique(vetrina),
    foreign key(utente)
        references utente(username)
);

-- [V.Utente.compl] e [V.Utente.disj] non ancora implementati

create table postoggetto(
    id serial primary key,
    pubblica Stringa not null,
    descrizione Stringa not null,
    pubblicazione timestamp not null,
    ha_feedback boolean not null,
    voto Voto,
    commento Stringa,
    istante_feedback timestamp,
    categoria Stringa not  null,
    -- vincoli di ennupla per modellare [V.PostOggetto.feedback]
    CHECK ((ha_feedback = TRUE) = (voto IS NOT NULL AND istante_feedback IS NOT NULL)),
-- se c'è il commento allora ha_feedback è true
    check(voto is null OR ha_feedback=true),
       foreign key (categoria)
           references categoria(nome),
-- v.incl. (id) occorre in met_post(postoggetto)
foreign key(pubblica)
   references utente(username)
);
ALTER TABLE postoggetto 
ADD UNIQUE(id,pubblica);

create table postoggettonuovo(
    postoggetto integer primary key,
    pubblica_nuovo Stringa not null,
    anni_garanzia IntGE2 not null,
    foreign key (pubblica_nuovo)
       references venditoreprof(utente),
    -- implementa [V.PostOggettoNuovo.pubblica.isa]
    foreign key(postoggetto,pubblica_nuovo)
        references postoggetto(id,pubblica)
);

create table metodopagamento(
    nome Stringa primary key
);

create table met_pos(
    postoggetto serial not null,
    metodopagamento Stringa not null,
    primary key(postoggetto,metodopagamento),
    foreign key(postoggetto)
        references postoggetto(id),
    foreign key(metodopagamento)
       references metodopagamento(nome)
);

create table postoggettousato(
    postoggetto serial primary key,
    condizione Condizione not null,
    anni_garanzia IntGEZ not null,
    foreign key(postoggetto)
       references postoggetto(id)
);


create table asta(
   postoggetto serial primary key,
   prezzobid RealGZ not null,
   scadenza timestamp not null,
   prezzobase RealGZ not null,
   foreign key(postoggetto)
       references postoggetto(id)
);

create table bid(
    codice serial primary key,
    asta integer not null,
    privato Stringa not null,
    istante timestamp not null,
    unique(istante),
    foreign key(asta)
       references asta(postoggetto),
    foreign key(privato)
        references privato(utente)
);

create table comprasubito(
    postoggetto serial primary key,
    prezzo RealGZ not null,
    istante timestamp not null,
    priv Stringa not null,
    foreign key(postoggetto)
        references postoggetto(id),
    foreign key(priv)
      references privato(utente)
);

