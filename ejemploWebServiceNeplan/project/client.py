import urllib3                                  # Para deshabilitar las advertencias de SSL al usar verify=False

from requests import Session                    # Para crear una sesión personalizada que permita deshabilitar la verificación SSL

from zeep import Client                         # Para crear un cliente SOAP a partir del WSDL
from zeep.wsse.username import UsernameToken    # Para manejar la autenticación WS-Security con nombre de usuario y contraseña
from zeep.transports import Transport           # Para personalizar el transporte del cliente SOAP, permitiendo deshabilitar la verificación SSL

from config import (                            # Importar las constantes de configuración desde el archivo config.py
    WSDL_URL,
    SERVICE_URL
)

from auth import get_credentials                # Importar la función para obtener las credenciales de autenticación desde el archivo auth.py

urllib3.disable_warnings()                      # Deshabilitar las advertencias de SSL al usar verify=False en la sesión personalizada

username, hashed_password = (                   # Obtener las credenciales de autenticación (nombre de usuario y contraseña hasheada) desde la función get_credentials() en auth.py
    get_credentials()
)

session = Session()                             # Crea una seasion persistente para el transporte del cliente SOAP (HTTP session)

session.verify = False                          # Deshabilitar la verificación SSL para esta sesión (no recomendado para producción, pero útil para entornos de desarrollo o pruebas)

client = Client(                                # Crear el cliente SOAP utilizando Zeep, con la URL del WSDL, el transporte personalizado y la autenticación WS-Security

    wsdl=WSDL_URL,                              # URL del WSDL que describe el servicio SOAP

    transport=Transport(                        # Conexión personalizada para el cliente SOAP, utilizando la sesión que tiene la verificación SSL deshabilitada
        session=session
    ),

    wsse=UsernameToken(                        # Configuración de autenticación WS-Security utilizando el nombre de usuario y la contraseña hasheada
        username,
        password=hashed_password
    )
)

neplan_service = client.create_service(        # Crea ejecutable el servicio SOAP a partir del cliente, utilizando el nombre del servicio y la URL del endpoint del servicio

    "{http://www.neplan.ch/Web/External}"
    "BasicHttpBinding_NeplanService",

    SERVICE_URL
)



settings_type = client.get_type(
    "ns2:AnalysisParameterSettings"
)

print(settings_type)
