import configparser

_conf = configparser.ConfigParser()
_conf.read("setup.conf")


def get_intvalue(section, name):
    return int(_conf.get(section, name))


def get_fvalue(section, name):
    return float(_conf.get(section, name))


def get_str(section, name):
    return str(_conf.get(section, name))
