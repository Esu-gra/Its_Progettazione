

-- Categorie
INSERT INTO categoria(nome, super) VALUES
  ('Elettronica', NULL),
  ('Telefonia', 'Elettronica'),
  ('Computer', 'Elettronica'),
  ('Casa e Arredamento', NULL),
  ('Mobili', 'Casa e Arredamento'),
  ('Abbigliamento', NULL),
  ('Uomo', 'Abbigliamento'),
  ('Donna', 'Abbigliamento');

-- Utenti
INSERT INTO utente(username, registrazione) VALUES
  ('alice', '2025-01-10 09:15:00'),
  ('bob',   '2025-02-20 12:00:00'),
  ('carla', '2025-03-05 16:30:00'),
  ('dario', '2025-04-01 08:45:00'),
  ('emma',  '2025-05-10 14:20:00');

-- Privati (utenti “Privato”)
INSERT INTO privato(utente) VALUES
  ('alice'),
  ('carla'),
  ('emma');

-- Venditori professionali
INSERT INTO venditoreprof(utente, vetrina) VALUES
  ('bob', 'http://vetrina-bob.example.com'),
  ('dario', 'http://vetrina-dario.example.com');

-- Metodi di pagamento
INSERT INTO metodopagamento(nome) VALUES
  ('PayPal'),
  ('Carta di Credito'),
  ('Bonifico'),
  ('Contanti');

-- PostOggetto
INSERT INTO postoggetto(
  id, pubblica, descrizione, pubblicazione, ha_feedback, voto, commento, istante_feedback, categoria
) VALUES
  (1, 'bob',   'Smartphone nuovo, marca X', '2025-05-15 10:00:00', false, NULL, NULL, NULL, 'Telefonia'),
  (2, 'dario', 'Divano due posti usato',    '2025-05-20 18:30:00', true, 4, 'Buono ma con segni di usura', '2025-05-22 09:00:00', 'Mobili'),
  (3, 'bob',   'Giacca in pelle taglia M',   '2025-06-01 12:00:00', true, 5, 'Perfetta, spedizione veloce', '2025-06-03 14:45:00', 'Donna'),
  (4, 'alice', 'Laptop gaming 16GB RAM',      '2025-06-10 08:00:00', false, NULL, NULL, NULL, 'Computer');

-- Oggetti Nuovi
INSERT INTO postoggettonuovo(postoggetto, pubblica_nuovo, anni_garanzia) VALUES
  (1, 'bob', 2),
  (4, 'alice', 3);

-- Oggetti Usati
INSERT INTO postoggettousato(postoggetto, condizione, anni_garanzia) VALUES
  (2, 'Discreto', 0),
  (3, 'Ottimo', 1);

-- Associazione metodi di pagamento ai post
INSERT INTO met_pos(postoggetto, metodopagamento) VALUES
  (1, 'PayPal'),
  (1, 'Carta di Credito'),
  (2, 'Bonifico'),
  (3, 'Contanti'),
  (4, 'PayPal');

-- Aste
INSERT INTO asta(postoggetto, prezzobid, scadenza, prezzobase) VALUES
  (2, 50.00, '2025-06-30 20:00:00', 30.00);

-- Bid
INSERT INTO bid(codice, asta, privato, istante) VALUES
  (1, 2, 'alice', '2025-06-20 10:00:00'),
  (2, 2, 'carla', '2025-06-25 15:30:00'),
  (3, 2, 'emma',  '2025-06-29 19:45:00');

-- CompraSubito
INSERT INTO comprasubito(postoggetto, prezzo, istante, priv) VALUES
  (3, 120.00, '2025-06-05 11:00:00', 'emma');

