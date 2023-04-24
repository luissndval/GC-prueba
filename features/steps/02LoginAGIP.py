from behave import *
from pages.LoginPage import LoginPage

@when(u'Realizar click en ingresar con AGIP')
def step_impl(context):
    try:
        LoginPage.IngresaConAGIPButton(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en: ****Ingresar a Login con AGIP****"

@when(u'Escribiendo campo  User :"{CUIT}"')
def step_impl(context,CUIT):
    try:
        LoginPage.CUITInput(context, CUIT)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en: ****Escribiendo campo CUIT****"

@when(u'Escribiendo campo passw :"{Clave}"')
def step_impl(context,Clave):
    try:
        LoginPage.AGIPPasswInput(context, Clave)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en: ****Escribiendo campo Clave****"

@when(u'Realizar click en el bonton ingresar AGIP')
def step_impl(context):
    try:
        LoginPage.LoginAGIPButton(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en: ****Click en bonton ingresar****"