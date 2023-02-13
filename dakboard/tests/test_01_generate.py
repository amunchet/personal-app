import os
import datetime

import arrow

import generate

from datetime import datetime, timedelta
from pprint import pprint


def test_check_top_image():
    """
    Tests the top image generation
    """
    a = generate.create_image_combine_top(os.path.join("design", "test-top.png"))

    assert a
    assert a.size == (1080, 1920)

    assert a.getpixel((1000, 1000)) == (0, 0, 0)

    assert a.getpixel((10, 10)) == (50, 66, 82)


def test_overall_generate():
    """
    Tests the entire generate

    """


def test_current_week_array():
    now = arrow.get("2023-01-30T00:00:00").datetime
    result = generate.current_week_array(now=now)
    expected = [
        ("29", False),
        ("30", True),
        ("31", False),
        ("Feb", False),
        ("2", False),
        ("3", False),
        ("4", False),
    ]

    assert result == expected

    result = generate.current_week_array(now=now, offset=1)
    expected = [
        ("5", False),
        ("6", False),
        ("7", False),
        ("8", False),
        ("9", False),
        ("10", False),
        ("11", False),
    ]

    assert result == expected
