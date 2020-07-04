# BKAPI

Access the BK Cloud [API](http://kb.providerservice.com/bk-cloud/api/bkcloud-api.html) with Python

e.G. get the vnc link to a vserver of yours

```
python ./interactive.py vserver_vncinfo <your_id>
-->
https://vncproxy-dus2-de.virtualhosts.de/novnc/vnc_auto.html?mvid=1234567809003049304f&vncpw=123abcd
```

## Getting Started

Clone the git repository to your local folder.

### Prerequisites

```
Python 3
pip
PyYAML
docopt
requests
```

### Installing

I recommend using a local environment.

```
python -m venv ./env
# activate it
. ./env/bin/activate
```

Install the necessary dependencies.

```
(env) pip install docopt
(env) pip install pyyaml
(env) pip install requests
```

Install the package

```
(env) python setup.py install
```

Install with nix

```
nix-build -f ./default.nix -i
```

Running `bkapi (or: python ./interact.py)` shows all available **commands** and `--version` the current **version**.

Set up the _configuration_ file with the help of [EXAMPLE.interact.yaml](EXAMPLE.interact.yaml)

```
cp EXAMPLE.interact.yaml interact.yaml
```

Example call:

```
(env) bkapi vservers_list
```

## Built With

- [docopt](http://docopt.org/) - Command-line interface description langugae
- [PyYAML](https://pyyaml.org) - Full-featured YAML framework for the Python programming language
- [requests](https://2.python-requests.org/en/master/#) - HTTP for Humans

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **plumps** - _Initial work_ - https://codeberg.org/plumps

## License

This project is licensed under the ISC License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to the great support team of BK who found a nice bug in my code
