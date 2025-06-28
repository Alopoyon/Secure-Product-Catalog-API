import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import metadata_obj

@pytest.fixture(scope="module")
def db_engine():
    """
    In memory database to discard after testing
    """
    engine = create_engine("sqlite:///:memory:")
    metadata_obj.create_all(engine)
    yield engine
    engine.dispose()


@pytest.fixture
def db_session(db_engine):
    Session = sessionmaker(bind=db_engine)
    session = Session()
    yield session
    session.rollback()
    session.close()