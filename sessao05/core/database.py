from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import(
    create_async_engine,
    AsyncEngine,
    AsyncSession
)

# Embora o objetivo deste projeto seja explorar as capacidades do SQL Model, descobri que em sua versão atual ele inda depende do sqlAlchemy  para operaçõe sassíncronas

from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

# Aqui estou declarando o construtor de uma classe(Session)
Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)