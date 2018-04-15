"""Cli result formatters"""

def package_summary_payload(code, year):
    """Returns the summary endpoint payload json (as a dict)"""
    return dict(
        Anio=str(year),
        Tracking=code
    )

def package_details_payload(code, year, destination):
    """Returns the details endpoint payload json (as dict)"""
    return dict(
        Anio=str(year),
        Tracking=code,
        Destino=destination
    )
