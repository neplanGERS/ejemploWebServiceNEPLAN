from client import neplan_service

from operations import (
    load_project,
    change_element,
    run_loadflow,
    get_active_power,
    get_result_element_by_id
)

print("Connected successfully")

print(neplan_service)

# Cargar el proyecto /Nombre del proyecto/Nombre del escenario

project_name = (
    "LoadFlow_WebServices_Example"
)

scenario = None

diagram = None

layer = None

ext = load_project(

    neplan_service,

    project_name,

    scenario,

    diagram,

    layer
)

# llamar a la función para cambiar el valor de un atributo de un elemento


if ext:

    change_element(

        neplan_service,

        ext,

        "LOAD SEVEN",

        "Load",

        "P",

        10
    )

"""
if ext:

    analysis_id, analysis = (
        run_loadflow(
            neplan_service,
            ext
        )
    )

"""

# Obtener el resultado de un elemento específico por su ID después de ejecutar el flujo de carga

if ext:

    analysis_id, analysis = (
        run_loadflow(
            neplan_service,
            ext
        )
    )

    element_id = (
        "94453c94-c916-54cc-2357-3a2176c59997"
    )

    xml_result = (
        get_result_element_by_id(

            neplan_service,

            ext,

            element_id
        )
    )

    active_power = (
        get_active_power(
            xml_result
        )
    )

    print(
        f"Potencia activa: "
        f"{active_power} MW"
    )


