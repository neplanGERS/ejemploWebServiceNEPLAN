# Función para cargar un proyecto de Neplan.

def load_project(
    neplan_service,
    project_name,
    scenario,
    diagram,
    layer
):

    ext = neplan_service.GetProject(

        project_name,  # Nombre del proyecto

        scenario,      # Escenario dentro del proyecto

        diagram,       # Diagram Name

        layer          # Layer Name 
    )

    if ext is not None:

        print("Proyecto cargado correctamente")

        return ext

    else:

        print("No se pudo cargar el proyecto")

        return None
    
# Función para cambiar el valor de un atributo de un elemento. 

def change_element(

    neplan_service,           # Instancia del servicio de Neplan

    ext,                      # Extensión del proyecto cargado

    element_name,             # Nombre del elemento a modificar

    element_type,             # Tipo del elemento (e.g., "Load", "Generator", etc.)

    attribute_name,           # Nombre del atributo a modificar (e.g., "P", "Q", "I", etc.)

    new_value                 # Nuevo valor del atributo
):

    result = neplan_service.SetElementAttribute(

        ext,

        element_name,          # Nombre del elemento a modificar

        element_type,          # Tipo del elemento (e.g., "Load", "Generator", etc.)

        attribute_name,        # Nombre del atributo a modificar (e.g., "P", "Q", "I", etc.)

        str(new_value)         # Nuevo valor del atributo (convertido a string)    
    )

    if result:

        print(

            f"Atributo {attribute_name} "
            f"actualizado correctamente a {new_value}"
        )

    else:

        print("No se pudo actualizar")

    return result

# código para ejecutar un análisis de flujo de carga y obtener el resultado de un elemento específico por su ID.

import uuid  # Para generar un ID único para el análisis

def run_loadflow(

    neplan_service,

    project,

    variant="Default"    # Nombre de la variante a analizar (puede ser "Default" o el nombre de una variante específica en el proyecto)     
):

    analysis_id = str(   # Generar un ID único para el análisis utilizando uuid4, que genera un UUID aleatorio. Esto se utiliza para identificar de manera única el análisis que se va a ejecutar en Neplan.
        uuid.uuid4()     # Convertir el UUID a string para usarlo como ID del análisis
    )

    analysis = (
        neplan_service.AnalyseVariant(

            project,

            analysis_id,

            "LoadFlow",

            variant,

            "", "", ""
        )
    )

    print(
        "Load Flow ejecutado correctamente"
    )

    return analysis_id, analysis

# Función para obtener el resultado de un elemento específico por su ID después de ejecutar un análisis.

import xml.etree.ElementTree as ET   # Para parsear el resultado XML y extraer el valor de un atributo específico (en este caso, la potencia activa "P")

def get_active_power(xml_result):

    root = ET.fromstring(xml_result)  # Parsear el resultado XML para obtener la raíz del documento
   
    for elem in root.iter():           # Iterar sobre todos los elementos del XML para encontrar el atributo "P" (potencia activa)

        if elem.tag.endswith("P"):

            return elem.text

    return None

# Función para obtener el resultado de un elemento específico por su ID después de ejecutar un análisis, devolviendo el resultado completo en formato XML.

def get_result_element_by_id(

    neplan_service,

    ext,

    element_id,

    analysis_type="LoadFlow",

    port_number=0
):

    xml_result = (
        neplan_service.GetResultElementByID(

            ext,

            element_id,

            port_number,

            analysis_type,

            None
        )
    )

    return xml_result