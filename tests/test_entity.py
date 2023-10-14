import pytest
from demostracion_dagger.src.entity.entity import Entity

def test_entity_should_be_created_with_a_name():
    assert Entity("John")!=None
