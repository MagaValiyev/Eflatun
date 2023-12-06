import requests
from qrcodescanner import getcrcode

# POST /api/giris:
entry_data = {
    "kadi" : "takimkadi",
    "sifre" : "takimsifresi"
}

giris_response = requests.post('/api/giris', data = entry_data)
giris_response_json = giris_response.json()
takim_numarasi = giris_response_json['takim_numarasi']

# GET /api/sunucusaati:
sunucu_saati = requests.get('/api/sunucusaati')
sunucu_saati_json = sunucu_saati.json()

# POST /api/telemetri_gonder:
telemetri_data = {
    "takim_numarasi": takim_numarasi,
    "iha_enlem": 41.508775,
    "iha_boylam": 36.118335,
    "iha_irtifa": 38,
    "iha_dikilme": 7,
    "iha_yonelme": 210,
    "iha_yatis": -30,
    "iha_hiz": 28,
    "iha_batarya": 50,
    "iha_otonom": 1,
    "iha_kilitlenme": 1,
    "hedef_merkez_X": 300,
    "hedef_merkez_Y": 230,
    "hedef_genislik": 30,
    "hedef_yukseklik": 43,
    "gps_saati": {
        "saat": 11, 
        "dakika": 38, 
        "saniye": 37, 
        "milisaniye": 654 
    }
}

telemetri_response = requests.post('/api/telemetri_gonder', data=telemetri_data)

# POST /api/kilitlenme_bilgisi:
kilitlenme_data = {
    "kilitlenmeBaslangicZamani": {
        "saat": 11,
        "dakika": 40,
        "saniye": 51,
        "milisaniye": 478
    },
    "kilitlenmeBitisZamani": {
        "saat": 11,
        "dakika": 41,
        "saniye": 3,
        "milisaniye": 141
    },
    "otonom_kilitlenme": 1
}

kilitlenme_response = requests.post('/api/kilitlenme_bilgisi', data=kilitlenme_data)

# POST /api/kamikaze_bilgisi:
qr_text = getcrcode()

kamikaze_entry = {
    "kamikazeBaslangicZamani": {
        "saat": 11,
        "dakika": 44,
        "saniye": 13,
        "milisaniye": 361
    },
    "kamikazeBitisZamani": {
        "saat": 11,
        "dakika": 44,
        "saniye": 27,
        "milisaniye": 874
    },
    "qrMetni ": qr_text
}

kamikaze_response = requests.post('/api/kamikaze_bilgisi', data = kamikaze_entry)

# GET /api/qr_koordinati: 
qr_koordinati = requests.get('/api/qr_koordinati')
qr_koordinati_json = qr_koordinati.json()