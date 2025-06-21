
# GPT to Notion Backend

Ten prosty backend zapisuje wiadomości z pliku `test_message.txt` do bazy danych w Notion co 30 sekund.

## Jak używać:

1. Stwórz plik `.env` na podstawie `.env.example` i wstaw swoje dane:
   - `NOTION_TOKEN`
   - `NOTION_DATABASE_ID`

2. Zainstaluj zależności:
    pip install -r requirements.txt

3. Uruchom backend:
    python main.py

✅ Nowe wiadomości w pliku `test_message.txt` będą zapisywane do Notion!
