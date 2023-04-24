from behave import *
from pages.PinturaGrafitis_page import Pintura_Grafitis



@when(u'solicitud mas frecuente pintura sobre grafitis')
def step_impl(context):
    try:
        Pintura_Grafitis.solicitud_pintura(context)
        Pintura_Grafitis.buscar_En_El_Mapa(context)
        Pintura_Grafitis.Cargar_Nueva_Solicitud(context)
        Pintura_Grafitis.Cancelar_la_Solicitud(context)
        Pintura_Grafitis.Alerta_de_Cancelar(context)
    except Exception:
        context.driver.close()
        assert False, ("La prueba fallo en: ****pintura sobre grafitis****")
