

from . import log
from . import config

from .domains import pip
pip.install(config)


def updater():
    for domain_name in config.domains:
        domain = getattr(config, domain)
        domain.update()


if __name__ == '__main__':
    updater()
