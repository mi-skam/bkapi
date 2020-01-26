import sys
from interact import BKAPI


def compare(f, e, i=None):
    if i == None:
        o = f()
        i = "-"
    else:
        o = f(i)
    if not o == e:
        raise ValueError(f"{f.__name__}({i}) -> {o} != {e}")


# tests creation of BKAPI object
sys.argv.append("vserver_info")
sys.argv.append("1234")
bk = BKAPI(config_file="./EXAMPLE.interact.yaml")

# tests _remove_brackets
compare(bk._remove_brackets, 'p', i='<p>')

# tests _load_config
expected = {'username': 'BKAPI-12345-abcdefgh123', 'password': 'mypass123'}
compare(bk._load_config, expected)

# tests _select
expected = ('vserver_info', "vid: '1234'\n")
compare(bk._select, expected)
