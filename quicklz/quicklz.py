from _pyquicklz.lib import *
from _pyquicklz import ffi

qlz_state_compress = ffi.new("qlz_state_compress *")


def compress(data):
    """
    qlz_compress(const void *source, char *destination, size_t size, qlz_state_compress *state)
    :param data:
    :return:
    """

    if isinstance(data, str):
        data = data.encode()

    source = ffi.new('char[]', data)
    destination = ffi.new('char[]', len(source) + 400)
    qlz_compress(source, destination, len(source), qlz_state_compress)
    return destination

def decompress(data):
    """
    TODO
    :param data:
    :return:
    """
    pass


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

