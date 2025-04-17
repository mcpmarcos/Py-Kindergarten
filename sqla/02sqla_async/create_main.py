from conf.db_session import create_tables
import asyncio

if __name__ == "__main__":
    # create_tables()
    asyncio.run(create_tables())