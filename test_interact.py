import sys
from interact import BKAPI

# tests creation of BKAPI object
sys.argv.append("vserver_info")
sys.argv.append("1234")
bk = BKAPI(config_file="./EXAMPLE.interact.yaml")
