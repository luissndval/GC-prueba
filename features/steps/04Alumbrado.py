from behave import *
from pages.Alumbrado_page import Alumbrado

@when(u'cargando solicitud de reparacion luminaria')
def step_impl(context):
    try:
        Alumbrado.input_Liminaria(context)
        Alumbrado.buscar_En_El_Mapa(context)
        Alumbrado.Cargar_Nueva_Solicitud(context)
        Alumbrado.Cancelar_la_Solicitud(context)
        Alumbrado.Alerta_de_Cancelar(context)
    except Exception:
        context.driver.close()
        assert False, ("La prueba fallo en: **** solicitud de reparacion luminaria ****")
