import yaml
from easydict import EasyDict as edict


def read_config(name):
    with open('configs/{}.txt'.format(name.lower())) as f:
        config = edict(yaml.load(f))
        return config
