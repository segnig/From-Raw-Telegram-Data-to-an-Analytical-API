from config import *

def main():
    print("✅ Environment setup complete.")
    print(f"🔑 Telegram API ID: {TELEGRAM_API_ID}")
    print(f"🗃️  PostgreSQL DB: {POSTGRES_DB} at {POSTGRES_HOST}")

if __name__ == "__main__":
    main()
