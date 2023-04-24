from behave import *
from pages.CFV_page import Calles_FV


@when(u'Categoria Solicitud Calle Feachada y veredas')
def step_impl(context):
    try:
        Calles_FV.Categoria_Calles_FV(context)
        Calles_FV.buscar_En_El_Mapa(context)
        Calles_FV.Cargar_Nueva_Solicitud(context)
        Calles_FV.Cancelar_la_Solicitud(context)
        Calles_FV.Alerta_de_Cancelar(context)
    except Exception:
        context.driver.close()
        assert False, ("La prueba fallo en: ****Flujo de reparacion de vereda****")
