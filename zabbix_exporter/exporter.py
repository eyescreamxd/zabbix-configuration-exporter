import json
import os
from pathlib import Path

from pyzabbix import ZabbixAPI

from .types import ConfigurationType, Entry, FileTypes


class ExporterRunner(ZabbixAPI):

    def _get_type_ids(self, method: ConfigurationType) -> [Entry]:
        """
        Prepare list of Entry objects with templates names and ids
        :return: Sorted alphabetic List of Entry objects
        """
        templates = self.do_request(method.value.method)
        return sorted([Entry(i.get('name'), i.get(method.value.id_field)) for i in templates.get('result')])

    def _get_configuration(self, configuration_type: ConfigurationType, configuration_id: Entry,
                           file_extension: FileTypes):
        """

        :param configuration_id:
        :param file_extension:
        :return:
        """
        return self.configuration.export(format=file_extension.value,
                                         prettyprint=True,
                                         options={configuration_type.value.name: [configuration_id.id]})

    @staticmethod
    def _save_file(configuration_type: ConfigurationType, filename: Entry,
                   file_extension: FileTypes, content: str):
        folder = Path(os.path.join(os.getcwd(), 'exported_files/' + configuration_type.value.name))
        folder.mkdir(exist_ok=True, parents=True)
        # print(Path(os.path.join(folder, filename.name + '.' + file_extension.value)))
        with open(Path(os.path.join(folder,
                                    filename.name.replace('/', '_') + '.' + file_extension.value)),
                  'w') as template_file:
            try:
                template_file.write(content)
            except TypeError:
                template_file.write(json.dumps(content))

    def configuration_export(self, configuration_type: ConfigurationType,
                             file_extension: FileTypes = FileTypes.YAML):
        entries = self._get_type_ids(configuration_type)
        for entry in entries:
            content = self._get_configuration(configuration_type, entry, file_extension)
            self._save_file(configuration_type, entry, file_extension, content)
