import os
import sys

# current_dir = os.path.dirname(os.path.abspath(__file__))
# project_root = os.path.join(current_dir, os.pardir)
# sys.path.insert(0, project_root)
# # e = sys.path.insert(0, os.path.join(os.path.dirname(__file__),".."))
# print(f"{current_dir=} {project_root=}")

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models import metadata_obj


@pytest.fixture(scope="session")
def db_engine():
    """
    In memory database to discard after testing
    """
    test_engine = create_engine("sqlite://")
    # rgs, kwargs = test_engine.dialect.create_connect_args(test_engine.url)
    # print(f"{rgs=}\n{kwargs=}")
    metadata_obj.create_all(bind=test_engine)
    yield test_engine
    test_engine.dispose()
    metadata_obj.drop_all(bind=test_engine)


@pytest.fixture(scope="function")
def db_session(db_engine):
    """
    Session for each database access
    """
    Session = sessionmaker(bind=db_engine)
    session = Session()
    try:
        yield session
    except Exception as e:
        print(e)
    finally:
        session.rollback()
        session.close()