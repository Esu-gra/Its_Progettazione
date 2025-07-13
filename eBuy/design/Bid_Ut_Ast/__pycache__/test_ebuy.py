from datetime import datetime, timedelta
from UtentePrivato import UtentePrivato
from Bid import Bid
from Asta import Asta 
from  custom_types import *


def test_ebuy():
    print("🔧 Avvio test...")

    # 1. Crea utenti
    venditore = UtentePrivato("mario", datetime(2024, 1, 1), URL("https://shop.mario.it"))
    acquirente1 = UtentePrivato("lucia", datetime(2024, 2, 1), URL("https://lucia.it"))
    acquirente2 = UtentePrivato("gianni", datetime(2024, 3, 1), URL("https://gianni.it"))
    print("✅ Utenti creati")

    # 2. Crea un'asta pubblicata da mario
    scadenza = datetime.now() + timedelta(days=2)
    asta = Asta(scadenza, FloatGEZ(10.0), pubblicato_da=venditore)
    print(f"✅ Asta creata con scadenza {asta._scadenza} e prezzo_rialzo {asta._prezzo_rialzo}")

    # 3. Due utenti fanno offerte valide
    t1 = datetime.now()
    bid1 = Bid(t1, asta, acquirente1)

    t2 = t1 + timedelta(minutes=5)
    bid2 = Bid(t2, asta, acquirente2)

    print("✅ Bid validi accettati")

    # 4. Tentativo illegale: venditore fa bid sulla propria asta
    try:
        Bid(t2 + timedelta(minutes=1), asta, venditore)
        print("❌ Errore: il vincolo selfBid non è stato rispettato!")
    except PermissionError as e:
        print(f"✅ Vincolo selfBid rispettato: {e}")

    # 5. Verifica vincitore e ultimo bid
    vincitore = asta.vincitore()
    print(f"🏆 Vincitore: {vincitore._username}")

    ultimo = asta.ultimo_bid(datetime.now())
    print(f"🕓 Ultimo bid fatto da: {ultimo.utente._username} alle {ultimo.istante}")

    # 6. Verifica prezzo e chiusura
    print(f"💰 Prezzo attuale: {asta.prezzo(datetime.now())} €")
    print(f"⌛ Asta conclusa? {asta.conclusa()}")

test_ebuy()
