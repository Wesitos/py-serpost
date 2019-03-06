"""Json response handling logic"""
import logging
from datetime import datetime
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def process_fecha(raw_fecha):
    'Parses the date string from a package details row'
    if not raw_fecha:
        return None

    try:
        return datetime.strptime(raw_fecha, '%m/%d/%Y %I:%M:%S %p')
    except ValueError:
        logger.exception('Obtenida una cadena de fecha infalida {}'
                         .format(repr(raw_fecha)))
        return None


def process_package_details(details):
    """Cleans the response of the detailed information request"""
    soup = BeautifulSoup(details['ResulQuery'], 'html.parser')
    texts = [cell.text.strip()
             for row in soup.find_all('tr')
             for cell in row.find_all('td')]
    row_list = [texts[i:i+3] for i in range(0, len(texts), 3)]

    return [dict(
        destino=destino,
        fecha=process_fecha(fecha),
        descripcion=texto,
    ) for (destino, fecha, texto) in row_list]


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
        observacion=('RetornoCadena8', str)
    )

    return {k:t(summary[v]) for k,(v, t) in field_dict.items()}
