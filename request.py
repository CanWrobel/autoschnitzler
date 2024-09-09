import requests


def alarm():
# URL für die Telegram Bot API
    url = "https://api.telegram.org/bot7443671380:AAGj_vR3jKwReGI3wWB-93jvZhBOtTaClok/sendMessage"
    # Parameter für die GET-Anfrage
    params = {
        'chat_id': '7066969213',
        'text': '⚠️ Bimst voll!'
    }

    # GET-Anfrage senden
    response = requests.get(url, params=params)

    # Überprüfen der Antwort
    if response.status_code == 200:
        print("Nachricht erfolgreich gesendet.")
    else:
        print(f"Fehler beim Senden der Nachricht: {response.status_code} - {response.text}")
