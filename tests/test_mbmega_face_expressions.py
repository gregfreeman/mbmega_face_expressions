#!/usr/bin/env python

"""Tests for `mbmega_face_expressions` package."""

import pytest
import asyncio as aio
import logging


@pytest.mark.asyncio
async def test_run(robot, caplog):
    """
    """
    caplog.set_level(logging.DEBUG)
    await aio.sleep(60)
    assert robot.state == 'Running'
    assert robot.step_count > 0 
