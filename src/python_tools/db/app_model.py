import datetime
from typing import Optional

from sqlalchemy import BIGINT, NVARCHAR, String, TIMESTAMP
from sqlalchemy import func
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import CreateTable
from typing_extensions import Annotated

timestamp = Annotated[datetime.datetime, mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),]


class Base(DeclarativeBase):
    type_annotation_map = {int: BIGINT, datetime.datetime: TIMESTAMP(timezone=True),
        str: String().with_variant(NVARCHAR, "postgresql"), }


class SomeClass(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    fullname: Mapped[Optional[str]] = mapped_column(String(50), nullable=False)
    nickname: Mapped[Optional[str]] = mapped_column(String(30))
    date: Mapped[datetime.datetime]
    status: Mapped[str]
    created_at: Mapped[timestamp] = mapped_column(server_default=func.UTC_TIMESTAMP())
    updated_at: Mapped[timestamp] = mapped_column(server_default=func.UTC_TIMESTAMP())


if __name__ == '__main__':
    print(CreateTable(SomeClass.__table__).compile(dialect=postgresql.dialect()))
