from behave import *
from pages.LoginPage import LoginPage


@when(u'visualizar datos en MI CUENTA')
def step_impl(context):
    try:
        LoginPage.ButtonListUser(context)
        LoginPage.ButtonListMiCuenta(context)
        LoginPage.ContNombreApellido(context)
        LoginPage.LogOutMicuenta(context)
    except Exception:
        context.driver.close()
        assert False, ("La prueba fallo en: ****Validando los datos en Mi cuenta****")

