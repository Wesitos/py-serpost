"""Command line interface"""
import asyncio
import argparse
from datetime import datetime
from .aio import execute
from .formatters import json_formatter, yaml_formatter

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
    parser.add_argument('--tracking', '-t', metavar='T', nargs='+', type=str,
                        help='Codigos de rastreo a consultar')

    args = parser.parse_args()

    concurrency = args.concurrency
    formatter = formatters.get(args.format)
    year = args.year
    tracking = args.tracking

    if tracking is None and args.file is None:
        parser.print_help()
        exit()

    if tracking is None:
        tracking = args.file.read().upper().split()

    async def task():
        print(formatter(await execute(tracking, year, concurrency)))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(task())


if __name__ == '__main__':
    main()
