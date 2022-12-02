from sqlalchemy import Column, SmallInteger, ForeignKey, VARCHAR, select, Integer, BigInteger, Sequence, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy


from loader import DATABASE_URL


Base = declarative_base()


class BaseMixin(object):
    id = Column(Integer, primary_key=True)
    engine = create_async_engine(f'postgresql+asyncpg://{DATABASE_URL}')

    def __init__(self, **kwargs) -> None:
        for kw in kwargs.items():
            self.__getattribute__(kw[0])
            self.__setattr__(*kw)

    @staticmethod
    def create_async_session(func) -> object:
        async def wrapper(*args, **kwargs) -> object:
            async with AsyncSession(bind=BaseMixin.engine) as session:
                return await func(*args, **kwargs, session=session)

        return wrapper

    @create_async_session
    async def save(self, session: AsyncSession = None) -> None:
        session.add(self)
        await session.commit()
        await session.refresh(self)

    @create_async_session
    async def delete(self, session: AsyncSession = None) -> None:
        await session.delete(self)
        await session.commit()

    @classmethod
    @create_async_session
    async def get(cls, pk: int, session: AsyncSession) -> Base:
        return await session.get(cls, pk)

    @classmethod
    @create_async_session
    async def all(cls, session: AsyncSession = None, **kwargs) -> list[Base]:
        models = await session.execute(
            select(cls)
            .filter_by(**kwargs)
            .order_by('id')
        )
        return [model[0] for model in models]

    async def dict(self):
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data


class User(BaseMixin, Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    first_name = Column(VARCHAR(100), nullable=False)
    last_name = Column(VARCHAR(100), nullable=True)


    def __str__(self):
        return self.first_name


class Categories(BaseMixin, Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(64), nullable=False)


class Item(BaseMixin, Base):
    __tablename__ = 'items'
    id = Column(BigInteger, Sequence("item_id_seq"), primary_key=True)
    name = Column(VARCHAR(100), nullable=False)
    price = Column(VARCHAR(100))
    category_id = Column(VARCHAR(24))

    def __repr__(self):
        return f"""
Товар №{self.id} - {self.name}
Цена:{self.price}
"""
