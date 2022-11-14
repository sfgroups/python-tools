from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime

from sqlalchemy import Column, String, Integer, create_engine, UniqueConstraint, TIMESTAMP, text
from sqlalchemy.orm import registry
from sqlalchemy.orm import sessionmaker
from pathlib import Path

import lib.utils.utils as utils


mapper_registry = registry()


@mapper_registry.mapped
@dataclass
class User:
    __tablename__ = "user"

    __sa_dataclass_metadata_key__ = "sa"
    id: int = field(
        init=False, metadata={"sa": Column(Integer, primary_key=True, autoincrement=True)}
    )
    name: str = field(default=None, metadata={"sa": Column(String(50), nullable=False)})
    email: str = field(default=None, metadata={"sa": Column(String(50), nullable=False, index=True)})
    age: int = field(default=None, metadata={"sa": Column(Integer)})

    created_time: datetime = field(default=None,
                                   metadata={"sa": Column(TIMESTAMP, nullable=True, default=datetime.utcnow())})
    # updated_at: datetime = field(default=None, metadata={"sa": Column(TIMESTAMP, default=datetime, nullable=False,
    #                                                                   server_default=text(
    #                                                                       'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))})
    UniqueConstraint('email')


if __name__ == "__main__":
    connection_string = "sqlite:///" + str(Path(utils.get_data_dir(), 'test.db'))
    engine = create_engine(connection_string, echo=True)
    Session = sessionmaker(engine)

    mapper_registry.metadata.drop_all(engine)
    mapper_registry.metadata.create_all(engine)

    u = User("Sammy", "sammy@yahoo.com",30)
    u1 = User("Muthu", "muthu@yahoo.com",50)

    print(u)
    with Session() as session:
        with session.begin():
            session.add(u)
            session.add(u1)
            session.commit()

    print("==== Display values")
    with Session() as session:
        us = session.query(User).all()
        print(us)
        print("==== Update values")
        session.query(User).filter(User.id == 2).update({'name': "Siva"})
        session.commit()
        for c in session.query(User).all():
            c.age = c.age + 1
        session.commit()
        print("==== Display values")
        us = session.query(User).all()
        print(us)



