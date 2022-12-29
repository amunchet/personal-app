import os
import generate


def test_check_top_image():
    """
    Tests the top image generation
    """
    a = generate.create_image_combine_top(os.path.join("design", "test-top.png"))

    assert a
    assert a.size == (1080, 1920)

    assert a.getpixel((1000, 1000)) == (0,0,0)

    assert a.getpixel((10,10)) == (50,66,82)