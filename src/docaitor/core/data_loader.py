import tomllib
from typing import IO
import yaml


class DataLoaderException(Exception):
    pass


def toml_loader(input_stream):
    try:
        return tomllib.load(input_stream)
    except tomllib.TOMLDecodeError as ex:
        raise DataLoaderException(ex)


def yaml_loader(input_stream):
    try:
        return yaml.load(input_stream, yaml.loader.SafeLoader)
    except yaml.YAMLError as ex:
        raise DataLoaderException(ex)


LOADERS = {
    "TOML": toml_loader,
    "YAML": yaml_loader,
}

DEFAULT_LOADER = "TOML"


class DataLoader:
    def __init__(self, input_data_source: str | IO, loader_override=None):
        self._input = input_data_source
        self._file_name = ""
        if isinstance(self._input, str):
            self._file_name = self._input
        self._loader = (
            LOADERS[loader_override.upper()]
            if loader_override
            else LOADERS[DEFAULT_LOADER]
        )

    def _load(self):
        if self._file_name:
            with open(self._file_name, "rb") as fp:
                return self._loader(fp)
        return self._loader(self._input)

    def load(self):
        return self._load()
