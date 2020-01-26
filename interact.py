#!/usr/bin/env python

"""
Consumes BK Cloud API

Usage:
    interact accounts_list
    interact actions_available
    interact bootimages_list
    interact flavors_list
    interact images_list
    interact update_reverse_dns_name_of_ip4 <address> <rdns>
    interact update_reverse_dns_name_of_primary_ip4 <address> <rdns>
    interact update_reverse_dns_name_of_ip6 <address> <rdns>
    interact vserver_add <flavor_id> <zone_id> <image_name> <host_name> <rootpw> [sshkeys] [customscript] [motd]
    interact vserver_change_hostname <vid> <host_name>
    interact vserver_delete  <vid>
    interact vserver_delete  <client_id> <primary_ip>
    interact vserver_info <vid>
    interact vserver_reinstall <vid> <root_pw> <image_name> [sshkeys] [motd]
    interact vserver_reboot <vid> [force_mode]
    interact vserver_rescue <vid> [force_mode] [boot_image]
    interact vserver_rootpassword <vid> <root_pw>
    interact vserver_shutdown <vid> [force_mode]
    interact vserver_vncinfo <vid>
	interact vservers_list
    interact zones_list
	interact (-h | --help | --version)
"""
import requests
import yaml
from docopt import docopt


class BKAPI:
    CONFIG = {
        'url': 'https://cloud-api.virtualhosts.de/',
        'config': './interact.yaml'
    }

    def __init__(self, config_file=None):
        if config_file == None:
            self.config_file = self.CONFIG['config']

        self.arguments = docopt(__doc__)

    def load_config(self):
        """Loads user configuration from YAML file
        """
        with open(self.config_file) as f:
            return yaml.load(f, Loader=yaml.SafeLoader)

    def _remove_brackets(self, elem):
        """removes angular brackets from tags like <a> -> a
        """
        return elem.strip("<>")

    def select(self):
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


if __name__ == "__main__":
    bk = BKAPI()
    action = bk.load_config()
    action['action'], action['data'] = bk.select()

    r = requests.post(BKAPI.CONFIG['url'], data=action)
    print(r.text) if (r.status_code == 200) else print(
        f"API error ${r.status_code}")
