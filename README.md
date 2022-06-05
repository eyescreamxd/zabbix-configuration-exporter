## Zabbix API wrapper to save configuration to files 


This package allows to export desired Zabbix configuration (supported by Zabbix API) into files group by it's type

Zabbix API belongs to [Zabbix LLC](https://www.zabbix.com/)


### Based on
* [pyzabbix by adubkov](https://github.com/adubkov/py-zabbix)

Install
```bash
pip install git+https://github.com/eyescreamxd/zabbix-configuration-exporter.git
```

Use:
```python
from zabbix_exporter import ExporterRunner, FileTypes, ConfigurationType


# url, user and password can be defined by environment variables 
# ZABBIX_URL, ZABBIX_USER, ZABBIX_PASSWORD respectively
# default values are `https://localhost/zabbix`, Admin, zabbix
zapi = ExporterRunner(url='http://<IP:PORT>', user='Zabbix', password='zabbix')
zapi.configuration_export(ConfigurationType.HOSTS, FileTypes.YAML)

```
Or with context manager
```python
from zabbix_exporter import ExporterRunner, FileTypes, ConfigurationType

with ExporterRunner(url='http://<IP:PORT>', user='Zabbix', password='zabbix') as zapi:
    # export all templates and hosts in json format
    # creates exported_files folder in current working directory
    # and two sub-folders with names  
    zapi.configuration_export(ConfigurationType.TEMPLATES, FileTypes.JSON)
    zapi.configuration_export(ConfigurationType.HOSTS, FileTypes.JSON)
```

TODO:
- [ ] Custom user path to export files to
- [ ] Add tests