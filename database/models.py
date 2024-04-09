from sqlalchemy import (
    DateTime,
    ForeignKey,
    Numeric,
    String,
    Text,
    BigInteger,
    func
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Banner(Base):
    __tablename__ = 'banner'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(15), unique=True)
    image: Mapped[str] = mapped_column(String(150), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False)
    image: Mapped[str] = mapped_column(String(150))
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id', ondelete='CASCADE'), nullable=False)

    category: Mapped['Category'] = relationship(backref='product')


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    first_name: Mapped[str] = mapped_column(String(150), nullable=True)
    last_name: Mapped[str] = mapped_column(String(150), nullable=True)
    phone: Mapped[str] = mapped_column(String(13), nullable=True)


class Cart(Base):
    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id', ondelete='CASCADE'), nullable=False)
    quantity: Mapped[int]

    user: Mapped['User'] = relationship(backref='cart')
    product: Mapped['Product'] = relationship(backref='cart')


"""
Данный код представляет собой пример использования SQLAlchemy для создания модели базы данных.
 Каждый класс в этом примере представляет таблицу в базе данных, а атрибуты классов представляют столбцы этих таблиц.

 *  * Базовый класс Base *  * 

Класс Base наследуется от DeclarativeBase и определяет общие атрибуты для всех таблиц.
 Атрибуты created и updated являются столбцами, которые автоматически заполняются 
 текущим временем при создании записи и обновлении соответственно.

 *  * Классы Banner, Category, Product, User, Cart *  * 

Каждый из этих классов определяет структуру конкретной таблицы в базе данных.
 Например, класс Banner имеет атрибуты id, name, image, и description,
  которые соответствуют столбцам таблицы banner.

Атрибуты, начинающиеся с двойного подчеркивания (__tablename__), определяют имя таблицы в базе данных.

Атрибуты, начинающиеся с символа двоеточия (:), являются столбцами таблицы. 
Типы данных столбцов определяются с помощью таких классов, как DateTime, String, Text, Numeric, и BigInteger.

Атрибуты, такие как mapped_column и Mapped, используются для определения столбцов и их свойств.

Атрибуты, такие как relationship, используются для определения связей между таблицами.
 Например, в классе Cart определены связи с таблицами User и Product.

Этот код не включает в себя создание самой базы данных или выполнение каких-либо операций с ней,
 он лишь определяет структуру таблиц, которые будут использоваться в дальнейшем для работы с базой данных.
"""