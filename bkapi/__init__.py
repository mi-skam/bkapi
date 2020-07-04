#!/usr/bin/env python

"""
Consumes BK Cloud API

Usage:
    bkapi accounts_list
    bkapi actions_available
    bkapi bootimages_list
    bkapi flavors_list
    bkapi images_list
    bkapi update_reverse_dns_name_of_ip4 <address> <rdns>
    bkapi update_reverse_dns_name_of_primary_ip4 <address> <rdns>
    bkapi update_reverse_dns_name_of_ip6 <address> <rdns>
    bkapi vserver_add <flavor_id> <zone_id> <image_name> <host_name> <rootpw> [sshkeys] [customscript] [motd]
    bkapi vserver_change_hostname <vid> <host_name>
    bkapi vserver_delete  <vid>
    bkapi vserver_delete  <client_id> <primary_ip>
    bkapi vserver_info <vid>
    bkapi vserver_reinstall <vid> <root_pw> <image_name> [sshkeys] [motd]
    bkapi vserver_reboot <vid> [force_mode]
    bkapi vserver_rescue <vid> [force_mode] [boot_image]
    bkapi vserver_rootpassword <vid> <root_pw>
    bkapi vserver_shutdown <vid> [force_mode]
    bkapi vserver_vncinfo <vid>
    bkapi vservers_list
    bkapi zones_list
    bkapi (-h | --help | --version)
"""
import os
import requests
import yaml
from docopt import docopt


class BKAPI:
    """Wraps BK Api and populates a dict ready for requests
    """

    CONFIG = {
        'url': 'https://cloud-api.virtualhosts.de/',
        'config': 'bkapi.yaml'
    }
    VERSION = '1.1.0'

    def load_config(self):
        """Loads user configuration from YAML file.
        """
        config_home = os.environ['APPDATA'] if 'APPDATA' in os.environ else os.path.join(
            os.environ['HOME'], '.config')

        config_file = os.path.join(config_home, self.config_file)
        with open(config_file) as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as ye:
                raise(ye)

    def __init__(self, config_file=None):
        if config_file == None:
            self.config_file = self.CONFIG['config']
        else:
            self.config_file = config_file

        self.arguments = docopt(__doc__, version=BKAPI.VERSION)
        self.action = self.load_config()
        self.action['action'], self.action['data'] = self._select()

    def _remove_brackets(self, elem):
        """Removes angular brackets from tags like <a> -> a.
        """
        return elem.strip("<>")

    def _select(self):
        """returns action command and data parameter
        """
        # returns only set arguments and options
        active_elements = {self._remove_brackets(
            k): v for k, v in self.arguments.items() if v}

        command = [k for k, v in active_elements.items()
                   if isinstance(v, bool)][0]
        active_elements.pop(command)
        parameter = yaml.dump(active_elements)

        return command, parameter


def get_vncinfo(response_text):
    """ clean up servers response of vncserver_vncinfo and return a clickable link 😀
    """
    # 1. split the string into a list of tuples
    temp = [i.split(": ") for i in result.split("\n")]
    # 2. unfortunately there are some tuples with just one element, we need to remove them
    def remove_singles(tuples): return filter(lambda x: len(x) > 1, tuples)

    return dict(remove_singles(temp))


def main():
    bk = BKAPI()
    r = requests.post(BKAPI.CONFIG['url'], data=bk.action)
    result = r.text

    # Adapt formatting for vserver_vncinfo
    if bk.action['action'] == 'vserver_vncinfo':
        u = get_vncinfo(result)
        # https://vncproxy-dus2-de.virtualhosts.de/novnc/vnc_auto.html?mvid=52c0d49cded81c9cb12f29c10e68d1ef&vncpw=QUU5y77w
        print(
            f"https://{u['vncproxy']}/novnc/vnc_auto.html?mvid={u['mvid']}&vncpw={u['vncpw']}")
        exit()

    print(result) if (r.status_code == 200) else print(
        f"API error ${r.status_code}")


if __name__ == "__main__":
    main()
