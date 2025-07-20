import asyncio
import socket
import time
from app.core.init.app import init_data
from app.core.init.db import connect_db, close_db

DB_HOST = "db"
DB_PORT = 5432

def wait_for_postgres(host: str, port: int, timeout: int = 60):
    print("⏳ Waiting for PostgreSQL to be ready...")
    start = time.time()
    while True:
        try:
            with socket.create_connection((host, port), timeout=2):
                print("✅ PostgreSQL is ready.")
                return
        except OSError:
            if time.time() - start > timeout:
                raise TimeoutError("PostgreSQL did not become ready in time.")
            time.sleep(1)

async def main():
    wait_for_postgres(DB_HOST, DB_PORT)
    await connect_db()
    await init_data()
    await close_db()

if __name__ == "__main__":
    asyncio.run(main())