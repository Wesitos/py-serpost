Py-Serpost
============
Herramienta para consultar el estado de los paquetes de Serpost Perú sin necesidad
de autenticarse.

Instalación
============

Usando pip::

    $ pip install --user py-serpost


Cómo utilizar
==============

Indicando los numeros de rastreo como parametros::

    $ serpost -y 2018 -t EA325602591CN RF495973328SG
    EA325602591CN:
      descripcion: FUE ENTREGADO
      destino: ADMINISTRACION POSTAL LIMA
      estado: ENTREGADO
      fecha: 2018-01-23 00:00:00
    RF495973328SG:
      descripcion: SALIO A DISTRIBUCION
      destino: OFICINA POSTAL CHEPEN
      estado: PENDIENTE DE ENTREGA
      fecha: 2018-02-02 00:00:00

Para devolver la informacion detallada::

    $ serpost --detailed -y 2018 -t EA325602591CN RF495973328SG
    EA325602591CN:
      año: 2018
      codigo: EA325602591CN
      destino: ADMINISTRACION POSTAL LIMA
      estado: ENTREGADO
      historia:
      - descripcion: ENVÍO EN PROCESAMIENTO EN LA SEDE PRINCIPAL DE SERPOST - NO DISPONIBLE
        PARA ENTREGA
        destino: ADMINISTRACION POSTAL LIMA
        fecha: 2018-01-19 00:00:00
      - descripcion: ENVÍO EN TRÁNSITO HACIA LA ADMINISTRACION - NO DISPONIBLE PARA ENTREGA
        destino: ADMINISTRACION POSTAL LIMA
        fecha: 2018-01-19 00:00:00
      - descripcion: SALIO A DISTRIBUCION
        destino: ADMINISTRACION POSTAL LIMA
        fecha: 2018-01-20 00:00:00
      - descripcion: SE INTENTO ENTREGAR PERO FUE IMPOSIBLE
        destino: ADMINISTRACION POSTAL LIMA
        fecha: 2018-01-22 00:00:00
      - descripcion: FUE ENTREGADO
        destino: ADMINISTRACION POSTAL LIMA
        fecha: 2018-01-23 00:00:00
        num_aviso: NA002832
        observacion: '-'
        origen: GUANGZHOU EMS
        tipo: EXPRESS MAIL SERVICE EMS
    RF495973328SG:
      año: 2018
      codigo: RF495973328SG
      destino: OFICINA POSTAL CHEPEN
      estado: PENDIENTE DE ENTREGA
      historia:
      - descripcion: ENVÍO EN TRÁNSITO HACIA LA ADMINISTRACION - NO DISPONIBLE PARA ENTREGA
        destino: OFICINA POSTAL CHEPEN
        fecha: 2018-01-10 00:00:00
      - descripcion: ENVÍO EN PROCESAMIENTO EN LA SEDE PRINCIPAL DE SERPOST - NO DISPONIBLE
        PARA ENTREGA
        destino: OFICINA POSTAL CHEPEN
        fecha: 2018-01-10 00:00:00
      - descripcion: ENVÍO EN PROCESAMIENTO EN LA SEDE PRINCIPAL DE SERPOST - NO DISPONIBLE
        PARA ENTREGA
        destino: OFICINA POSTAL CHEPEN
        fecha: 2018-01-11 00:00:00
      - descripcion: ENVÍO EN TRÁNSITO HACIA LA ADMINISTRACION - NO DISPONIBLE PARA ENTREGA
        destino: OFICINA POSTAL CHEPEN
        fecha: 2018-01-18 00:00:00
      - descripcion: SALIO A DISTRIBUCION
        destino: OFICINA POSTAL CHEPEN
        fecha: 2018-02-02 00:00:00
      num_aviso: PP001152
      observacion: ENVÍO SELECCIONADO POR SUNAT - ADUANAS
      origen: SINGAPORE 06
      tipo: PEQUEÑOS PAQUETES AFORABLES


Tambien se pueden leer desde un archivo (un código por linea)::

    $ serpost tracking.txt
