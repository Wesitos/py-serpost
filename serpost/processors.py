"""API response processing logic"""
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def process_fecha(raw_fecha):
    'Parses the date string from a package details row'
    if not raw_fecha:
        return None

    try:
        return datetime.strptime(raw_fecha, '%d/%m/%Y')
    except ValueError:
        logger.exception('Obtenida una cadena de fecha invalida %s', raw_fecha)
        return None

def process_package_details_item(details):
    """Cleans the response of one row of the detailed information request"""
    field_dict = dict(
        fecha=('RetornoCadena3', process_fecha),
        destino=('RetornoCadena2', str),
        descripcion=('RetornoCadena4', str),
    )

    return {k:func(details[v]) for k, (v, func) in field_dict.items()}


def process_package_details(details_list):
    """Cleans the response of the detailed information request"""
    return [process_package_details_item(details) for details in details_list]


def process_package_summary(summary):
    """Cleans the response of the summary request"""
    field_dict = dict(
        año=('RetornoCadena1', int),
        codigo=('RetornoCadena2', str),
        estado=('RetornoCadena3', str),
        num_aviso=('RetornoCadena4', str),
        origen=('RetornoCadena5', str),
        destino=('RetornoCadena6', str),
        tipo=('RetornoCadena7', str),
        observacion=('RetornoCadena8', lambda x: None if x == '-' else x)
    )

    return {k:func(summary[v]) for k, (v, func) in field_dict.items()}
