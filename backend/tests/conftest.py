import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session
from sqlmodel.pool import StaticPool
from app.main import app
from app.database import get_session
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

@pytest.fixture(name="client")
def client_fixture(db_session: Session):
    def get_session_override():
        return db_session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

@pytest.fixture
def token_usuario_comun():
    return "mock_token_usuario_comun"

@pytest.fixture
def token_admin():
    return "mock_token_admin"
