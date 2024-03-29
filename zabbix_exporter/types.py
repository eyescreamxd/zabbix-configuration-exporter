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
    hosts, templates, templateGroups, mediaTypes, maps, images, groups
    """
    HOSTS = MethodMapping('hosts', 'host.get', 'hostid')
    TEMPLATES = MethodMapping('templates', 'template.get', 'templateid')
    TEMPLATEGROUPS = MethodMapping('template_groups', 'templategroup.get', 'groupid')
    MEDIATYPES = MethodMapping('mediaTypes', 'mediatype.get', 'mediatypeid')
    MAPS = MethodMapping('maps', 'map.get', 'sysmapid')
    IMAGES = MethodMapping('images', 'image.get', 'imageid')
    GROUPS = MethodMapping('host_groups', 'hostgroup.get', 'groupid')
