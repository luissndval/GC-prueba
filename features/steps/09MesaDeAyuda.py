from behave import *
from pages.MDA_page import Mesa_de_Ayuda


@when(u'Categoria Solicitud Mesa de ayuda')
def step_impl(context):
    try:
        Mesa_de_Ayuda.solicitud_Mesa_de_Ayuda(context)
        Mesa_de_Ayuda.Cargar_Nueva_Solicitud(context)
        Mesa_de_Ayuda.Confirmar_la_Solicitud(context)
        Mesa_de_Ayuda.Modal_Solicitud_Exitosa(context)
        Mesa_de_Ayuda.Confirmar_Mis_Solicitudes(context)
    except Exception:
        context.driver.close()
        assert False, ("La prueba fallo en: ****Flujo Mesa de ayuda****")