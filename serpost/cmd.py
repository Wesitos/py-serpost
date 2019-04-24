"""Command line interface"""
import logging
import asyncio
import argparse
from datetime import datetime
from .aio import execute
from .formatters import json_formatter, yaml_formatter, summarize

base_logger = logging.getLogger(__package__)
logger = logging.getLogger(__name__)

formatters = dict(
    json=json_formatter,
    yaml=yaml_formatter,
)

def main():
    parser = argparse.ArgumentParser(
        description='Consulta el estado del envio de paquetes '
        'por medio de la API de serpost')
    parser.add_argument('--year', '-y', type=int,
                        default=datetime.now().year)
    parser.add_argument('--format', '-f',
                        help='Formato de los resultados',
                        type=str,
                        choices=formatters.keys(),
                        default='yaml')
    parser.add_argument('--concurrency', '-c', type=int,
                        default=10, help='numero de peticiones paralelas')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'),
                        help='Archivo con los codigos de rastreo (uno por linea)')
    parser.add_argument('--detailed', '-d', type=bool, nargs='?',
                        const=True, default=False,
                        help='Mostrar informacion detallada')
    parser.add_argument('--tracking', '-t', metavar='T', nargs='+', type=str,
                        help='Codigos de rastreo a consultar')
    parser.add_argument('--debug', '-D', type=bool, nargs='?',
                        const=True, default=False,
                        help='Imprime informacion de depuración')

    args = parser.parse_args()

    concurrency = args.concurrency
    formatter = formatters.get(args.format)
    year = args.year
    tracking = args.tracking
    detailed = args.detailed

    if args.debug:
        logging.basicConfig()
        base_logger.setLevel(logging.DEBUG)
        logger.info('Logging level set to DEBUG')

    if tracking is None and args.file is None:
        parser.print_help()
        exit()

    if tracking is None:
        tracking = args.file.read().upper().split()

    async def task():
        data = await execute(tracking, year, concurrency)
        if not detailed:
            data = {k: summarize(d) for k,d in data.items()}
        print(formatter(data))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(task())


if __name__ == '__main__':
    main()
