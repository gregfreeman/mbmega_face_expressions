import pytest
import asyncio as aio
from mbmega_face_expressions.controller import Controller


@pytest.fixture
async def robot():
    """robot fixture
    """
    ctrl = Controller(sim=True)
    yield ctrl
    await ctrl.stop()
