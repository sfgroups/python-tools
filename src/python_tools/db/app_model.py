import datetime
from typing import Optional

from sqlalchemy import String, TIMESTAMP, Integer
from sqlalchemy import func
from sqlalchemy.dialects import postgresql, sqlite
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import CreateTable
from typing_extensions import Annotated
from sqlalchemy.orm import registry

reg = registry()
timestamp = Annotated[datetime.datetime, mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),]


class Base(DeclarativeBase):
    type_annotation_map = {datetime.datetime: TIMESTAMP(timezone=True), }


@reg.mapped_as_dataclass
class LastRun(Base):
    __tablename__ = "lastrun"

   # id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), primary_key=True, nullable=False)
    fullname: Mapped[Optional[str]] = mapped_column(String(50), nullable=False)
    nickname: Mapped[Optional[str]] = mapped_column(String(30))
    start_date: Mapped[datetime.datetime] = mapped_column(nullable=True)
    last_date: Mapped[datetime.datetime] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[timestamp] = mapped_column(server_default=func.UTC_TIMESTAMP())
    updated_at: Mapped[timestamp] = mapped_column(server_default=func.UTC_TIMESTAMP())

    def __repr__(self):
        return (f"<LastRun(name='{self.name}', fullname='{self.fullname}', "
                f"nickname='{self.nickname}', start_date='{self.start_date}', "
                f"last_date='{self.last_date}', status='{self.status}', "
                f"created_at='{self.created_at}', updated_at='{self.updated_at}')>")

    def __str__(self):
        return (f"LastRun: {self.name} - {self.fullname} - "
                f"Nickname: {self.nickname}, Status: {self.status}")


if __name__ == '__main__':
    print(CreateTable(LastRun.__table__).compile(dialect=postgresql.dialect()))
    print(CreateTable(LastRun.__table__).compile(dialect=sqlite.dialect()))
