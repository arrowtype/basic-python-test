"""
    From https://github.com/coldtype/coldtype/blob/06537ff4e8dd3a9616aef7a113070cdf94533482/examples/animations/versioned.py
"""

from coldtype import *

VERSIONS = {
    "A": dict(text="COLD"),
    "B": dict(text="TYPE"),
}  # /VERSIONS


@animation((1080, 1080 / 4), bg=1, tl=45, release=lambda a: a.gifski())
def versioned_ƒVERSION(f):
    return StSt(
        __VERSION__["text"].upper(),
        Font.MuSan(),
        100,
        wght=f.e("eeio", 2),
        wdth=f.e("eeio", 1),
    ).align(f.a.r)
