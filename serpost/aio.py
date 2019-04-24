"""Http request logic implemented with aiohttp"""
import logging
import json
import asyncio
import aiohttp as aio
from .processors import process_package_details, process_package_summary
from .url import package_summary_url, package_details_url
from .payload import package_summary_payload, package_details_payload

logger = logging.getLogger(__name__)

async def fetch_package_summary(session, code, year):
    """Fetch the summary of a package"""
    res = await session.post(
        package_summary_url,
        json=package_summary_payload(code, year)
    )
    body = await res.json()

    logger.debug('Raw summary response: %s', json.dumps(body, indent=2))

    data = body.get('d')

    if data is None:
        return None

    return process_package_summary(data[0])


async def fetch_package_details(session, destination, code, year):
    """Fetch the detailed information of a package"""
    res = await session.post(
        package_details_url,
        json=package_details_payload(code, year, destination)
    )

    body = await res.json()

    logger.debug('Raw details response: %s', json.dumps(body, indent=2))

    data = body.get('d')

    if data is None:
        return None

    return process_package_details(data)

async def track(session, code, year):
    """Awaits for the tracking information of one package"""
    summary = await fetch_package_summary(session, code, year)

    if summary is None:
        return None

    details = await fetch_package_details(
        session, summary['destino'], code, year)
    return dict(
        summary,
        historia=details,
    )

def track_many(session, code_iter, year):
    """Returns a dictionary of futures for every code"""
    return {
        code: asyncio.ensure_future(track(session, code, year))
        for code in code_iter
    }


async def execute(code_list, year, concurrency=5):
    """Returns a promise for a dictionary of the packages full information

    :param list(str) code_list: Lista de códigos de rastreo
    :param int year: Año de envio del paquete
    :rtype: dict
    """
    conn = aio.TCPConnector(limit_per_host=concurrency)
    async with aio.ClientSession(connector=conn) as session:
        tracking_dict = track_many(session, code_list, year)

        res_dict = {}
        info = None
        for code, info_fut in tracking_dict.items():
            try:
                info = await info_fut
            except aio.ClientError as err:
                logger.exception('Error requesting data for "{}"'.format(code))
                logger.exception(err)
                info = dict(error=str(err))
            finally:
                res_dict[code] = info

    return res_dict
