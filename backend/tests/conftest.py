import pytest
from sqlmodel import SQLModel, create_engine, Session
from sqlmodel.pool import StaticPool
from app.cursos.models import Categoria, Curso

@pytest.fixture(name="db_session")
def db_session_fixture():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    SQLModel.metadata.create_all(bind=engine)

    with Session(engine) as session:
        cat1 = Categoria(id=1, nombre="Categoria prueba 1")
        cat2 = Categoria(id=2, nombre="Categoria prueba 2")
        session.add(cat1)
        session.add(cat2)
        session.commit()

        yield session

    SQLModel.metadata.drop_all(bind=engine)