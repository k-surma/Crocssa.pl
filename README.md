# Crocssa.pl 

Crocssa.pl to aplikacja społecznościowa typu "Tinder", ale z naciskiem na wymianę doświadczeń z obuwiem, w szczególności na crocsy. Użytkownicy mogą przeglądać zdjęcia swoich crocsów, dodać opis, podać szczegóły (model, kolor, rozmiar, liczba dziurek, ozdoby itp.), a następnie nawiązywać interakcje poprzez system czatów.

Aplikacja pozwala na:
- Przeglądanie crocsów innych użytkowników.
- Swajpowanie (lajkowanie/odrzucanie) na wzór aplikacji Tinder.
- Rozpoczynanie rozmów po wzajemnym swajpowaniu.
- Czatowanie w czasie rzeczywistym z użyciem WebSocketów.
- Powiadomienia o nowych wiadomościach.
- Emotikony w wiadomościach.

## Technologie

- **Frontend:** Vue.js (SPA)
- **Backend:** Flask (Python)
- **Baza danych:** PostgreSQL
- **WebSockety:** Flask-SocketIO
- **Autentykacja:** JWT (JSON Web Tokens)
- **Powiadomienia:** Long-polling / WebSockety

## Struktura projektu

### Frontend (Vue.js)
``
```
frontend/
│
├── public/                # Statyczne pliki (index.html, favicon itp.)
@@ -37,11 +37,11 @@
│   ├── main.js            # Punkt wejścia aplikacji
│
└── package.json           # Plik konfiguracyjny npm (zależności, skrypty)
``
```


### Backend (Flask)
``
```
backend/
│
├── app/                   # Główny folder aplikacji
@@ -55,43 +55,43 @@
│
├── requirements.txt       # Lista zależności Pythona
└── run.py                 # Punkt wejścia do aplikacji (uruchomienie Flask)
``
```

### Baza danych (PostgreSQL)

### Tabela `users`

| Kolumna      | Typ danych   | Opis                      |
|--------------|--------------|---------------------------|
| `id`         | `INT`        | Unikalny identyfikator użytkownika, AUTO_INCREMENT |
| `name`       | `VARCHAR`    | Imię użytkownika          |
| `age`        | `INT`        | Wiek użytkownika          |
| `image`      | `TEXT`       | Link do zdjęcia użytkownika |
| `description`| `TEXT`       | Krótki opis użytkownika   |

### Tabela `messages`

| Kolumna      | Typ danych   | Opis                              |
|--------------|--------------|-----------------------------------|
| `id`         | `INT`        | Unikalny identyfikator wiadomości, AUTO_INCREMENT |
| `sender_id`  | `INT`        | Identyfikator nadawcy (FK do tabeli `users`) |
| `receiver_id`| `INT`        | Identyfikator odbiorcy (FK do tabeli `users`) |
| `message`    | `TEXT`       | Treść wiadomości                  |
| `timestamp`  | `TIMESTAMP`  | Czas wysłania wiadomości          |

### Tabela `matches`

| Kolumna      | Typ danych   | Opis                              |
|--------------|--------------|-----------------------------------|
| `id`         | `INT`        | Unikalny identyfikator dopasowania, AUTO_INCREMENT |
| `user1_id`   | `INT`        | Identyfikator pierwszego użytkownika (FK do tabeli `users`) |
| `user2_id`   | `INT`        | Identyfikator drugiego użytkownika (FK do tabeli `users`) |
| `matched_at` | `TIMESTAMP`  | Czas dopasowania                  |


## Autorzy
- Kinga Surma
- Radosław Brońka
- Kacper Pabian

