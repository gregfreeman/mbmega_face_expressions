#!/usr/bin/env python

"""Tests for `mbmega_face_expressions` package."""

import pytest
import asyncio as aio


@pytest.mark.asyncio
async def test_run(robot):
    """
    """
    await aio.sleep(10)
    assert robot.state == 'Running'
    assert robot.step_count > 0 
