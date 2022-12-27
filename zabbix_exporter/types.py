from enum import Enum
from typing import NamedTuple


class Entry(NamedTuple):
    name: str
    id: int


class FileTypes(Enum):
    YAML = 'yaml'
    JSON = 'json'
    XML = 'xml'
    RAW = 'raw'


class MethodMapping(NamedTuple):
    name: str
    method: str
    id_field: str


class ConfigurationType(Enum):
    """
    hosts, templates, mediaTypes, maps, images, groups
    """
    HOSTS = MethodMapping('hosts', 'host.get', 'hostid')
    TEMPLATES = MethodMapping('templates', 'template.get', 'templateid')
    MEDIATYPES = MethodMapping('mediaTypes', 'mediatype.get', 'mediatypeid')
    MAPS = MethodMapping('maps', 'map.get', 'sysmapid')
    IMAGES = MethodMapping('images', 'image.get', 'imageid')
    HOSTGROUPS = MethodMapping('hostgroups', 'hostgroup.get', 'groupid')
