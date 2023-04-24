from behave import *
from pages.HospitalesCtrosSalud_page import Hospitales_Ctros_Salud

@when(u'Inconvenientes con turno en hospitales y centros de salud')
def step_impl(context):
    try:
        Hospitales_Ctros_Salud.input_buscador(context)
        Hospitales_Ctros_Salud.buscar_En_El_Mapa(context)
        Hospitales_Ctros_Salud.Cargar_Nueva_Solicitud(context)
        Hospitales_Ctros_Salud.Cancelar_la_Solicitud(context)
        Hospitales_Ctros_Salud.Alerta_de_Cancelar(context)
    except Exception:
        context.driver.close()
        assert False, ("La prueba fallo en: **** Turno en hospitales y centros de salud ****")
