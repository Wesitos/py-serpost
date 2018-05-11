"""Response formatters"""
import json
import yaml
from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.strftime('%d/%m/%Y')
    raise TypeError ("Type {} not serializable".format(type(obj)))

def summarize(obj):
    if not hasattr(obj, 'items'):
        return obj
    return dict(obj.get('historia', [{}])[-1], estado=obj.get('estado', ''))

def json_formatter(packages_dict):
    return json.dumps(packages_dict, default=json_serial, indent=2, ensure_ascii=False)


def yaml_formatter(packages_dict):
    return yaml.dump(packages_dict, default_flow_style=False, allow_unicode=True)
