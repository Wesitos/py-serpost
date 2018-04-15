"""Json response handling logic"""
from datetime import datetime
from bs4 import BeautifulSoup


def process_package_details(details):
    """Cleans the response of the detailed information request"""
    soup = BeautifulSoup(details['ResulQuery'], 'lxml')
    texts = [cell.text.strip()
             for row in soup.find_all('tr')
             for cell in row.find_all('td')]
    row_list = [texts[i:i+3] for i in range(0, len(texts), 3)]

    return [dict(
        destino=destino,
        fecha=datetime.strptime(fecha, '%d/%m/%Y'),
        descripcion=texto,
    ) for (destino, fecha, texto) in row_list]


def process_package_summary(summary):
    """Clenas the response of the summary request"""
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
