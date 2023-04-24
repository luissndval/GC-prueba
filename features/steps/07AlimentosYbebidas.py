from behave import *
from pages.AlimentosYbebidas_page import Alimentos_y_Bebidas

@when(u'Cargar solicitud de alimentos y bebidas en malas condiciones')
def step_impl(context):
    try:
        Alimentos_y_Bebidas.input_buscador(context)
        Alimentos_y_Bebidas.buscar_En_El_Mapa(context)
        Alimentos_y_Bebidas.Cargar_Nueva_Solicitud(context)
        Alimentos_y_Bebidas.Cancelar_la_Solicitud(context)
        Alimentos_y_Bebidas.Alerta_de_Cancelar(context)
    except Exception:
        context.driver.close()
        assert False, ("La prueba fallo en: ****Alimentos y Bebidas en malas condiciones ****")
