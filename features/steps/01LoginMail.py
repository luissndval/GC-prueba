from behave import *
from pages.LoginPage import LoginPage


#######################ABRIENDO NAVEGADOR#############################
@given(u'Iniciando Navegador en la Web https://gestioncolaborativa-hml.gcba.gob.ar/prestaciones')
def step_impl(context):
    try:
        LoginPage.OpenBrowser(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en: ****Iniciando Navegador en la Web****"



#######################INGRESAR A MIBA###############################
@when(u'Realizar click en ingresar con MiBA')
def step_impl(context):
    try:
        LoginPage.IngresaConMibaButton(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en: ****Realizar click en ingresar con MiBA****"



#######################SELECCIONANDO MAIL#############################
@when(u'Realizar click en ingresar con email')
def step_impl(context):
    try:
        LoginPage.IngresarConEmailButton(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en: ****Realizar click en ingresar con email****"



##########INGRESO DATOS PARA INICIO DE SESION CON MAIL#################
@when(u'Escribiendo campo  Username :"{Correo}"')
def step_impl(context,Correo):
    try:
        LoginPage.EmailInput(context, Correo)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en: ****Escribiendo campo  Username****"

@when(u'Escribiendo campo password :"{Password}"')
def step_impl(context, Password):
    try:
        LoginPage.PasswordInput(context, Password)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en: ****Escribiendo campo  Password****"

@when(u'Realizar click en el bonton ingresar')
def step_impl(context):
    try:
        LoginPage.LoginMailButton(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en: ****Realizando clik en Ingresar****"



#######################CERRANDO SESION###############################
@then(u'Validar inicio de sesion y cerrar sesion')
def step_impl(context):
    try:
        LoginPage.ValidarLogin(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en: ****Validar Inicio y cierre de sesion****"