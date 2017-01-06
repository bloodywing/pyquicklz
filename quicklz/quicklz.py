from _pyquicklz.lib import *


def compression_level():
    return qlz_get_setting(0)


def qlz_memory_safe():
    return bool(qlz_get_setting(6))


def qlz_version():
    return (
        qlz_get_setting(7),
        qlz_get_setting(8),
        qlz_get_setting(9)
    )

