import os
import dotw

def test_dotw_item():
    """
    Tests the DOTW item
    """
    filename = os.path.join("tests", "results", "02-dotw-item.jpg")
    a = dotw.dotw_item("A")
    if not os.path.exists(filename):
        a.save(filename)
    else:
        b = dotw.Image.open(filename)
        assert b
        assert b.getpixel((66,75)) == (255,255,255)
        assert b.getpixel((97,53)) == (0,0,0)

def test_dotw_header():
    """
    Tests the DOTW Header
    """
    filename = os.path.join("tests", "results", "03-dotw-header.jpg")
    a = dotw.dotw_header()
    if not os.path.exists(filename):
        a.save(filename)
    else:
        b = dotw.Image.open(filename)
        assert b
        assert b.getpixel((250,66)) == (255,255,255)
        assert b.getpixel((908,60)) == (0,0,0)

