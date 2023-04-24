import time
from selenium.webdriver.common.by import By
from configuration.config import Datatest
from Funciones.Funciones_GC import funciones_GC
from elements import loginElements
from elements import userElements
t = 1


class LoginPage(funciones_GC):

    def __init__(self, driver):
        super().__init__(driver)

    def OpenBrowser(self):
        #funciones_GC.driver_Firefox(self)
        funciones_GC.driver_Chrome(self)
        funciones_GC.browser(self, Datatest.URL)
        time.sleep(5)
###########################BUTTON MIBA##############################################
    def IngresaConMibaButton(self):
        funciones_GC.click_Field(self, By.XPATH, loginElements.IngresaConMibaButton)
        time.sleep(t)


###########################OPCIONES EN MIBA(BUTTON)#################################
    def IngresaConAGIPButton(self):
        funciones_GC.click_Field(self, By.XPATH, loginElements.IngresaConAGIPButton)
        time.sleep(t)

    def IngresarConEmailButton(self):
        funciones_GC.click_Field(self, By.XPATH , loginElements.IngresaConEmailButton)

########################INPUT USER PASSWORD MAIL - AGIP###############################
    def EmailInput(self, Correo):
        funciones_GC.input_Texto(self, By.XPATH, loginElements.MailInput, Correo)

    def PasswordInput(self, Password):
        funciones_GC.input_Texto(self, By.XPATH, loginElements.PasswordMailInput, Password)
        funciones_GC.screenShot(self,"User-Password")

    def CUITInput(self, CUIT ):
        funciones_GC.input_Texto(self, By.XPATH, loginElements.CuilInput, CUIT)

    def AGIPPasswInput(self, Clave):
        funciones_GC.input_Texto(self, By.XPATH, loginElements.AGIPPasswInput, Clave)
        funciones_GC.screenShot(self,"User-Password")

###############################BUTTON LOGIN (INGRESAR)#################################
    def LoginMailButton(self):
        funciones_GC.click_Field(self, By.XPATH, loginElements.LoginMailButton)
        funciones_GC.screenShot(self, "Sesion-Iniciada")
        time.sleep(t)

    def LoginAGIPButton(self):
        funciones_GC.click_Field(self, By.XPATH, loginElements.LoginAGIPButton)
        funciones_GC.screenShot(self, "Sesion-Iniciada")
        time.sleep(t)

    ###########################BUTTON CIUDADANO#####################################
    def ButtonListUser(self):
        funciones_GC.scrollToElement_visibility(self, By.XPATH, userElements.ButtonListUser)
        funciones_GC.click_Field(self, By.XPATH, userElements.ButtonListUser)
        time.sleep(t)

    def ButtonListMiCuenta(self):
        funciones_GC.scrollToElement_visibility(self, By.XPATH, userElements.ButtonListMiCuenta)
        funciones_GC.click_Field(self, By.XPATH, userElements.ButtonListMiCuenta)
        time.sleep(t)

    #######################FUNCIONES DE VALIDACION######################################
    def ValidarLogin(self):
        funciones_GC.validates(self,By.XPATH,loginElements.Validarlogin)
        time.sleep(t)
        funciones_GC.click_Field(self,By.XPATH,loginElements.DesplegableUser)
        time.sleep(t)
        funciones_GC.click_Field(self,By.XPATH,loginElements.LogoutOption)
        funciones_GC.screenShot(self, "Sesion-Cerrada")

    def ContNombreApellido(self):
        funciones_GC.validates(self, By.XPATH, userElements.ContNombreApellido)
        funciones_GC.screenShot(self, "Datos-del-Ciudadano")

    def ContCorreoElectronico(self):
        funciones_GC.scrollToElement(self, By.XPATH, userElements.ContCorreoElectronico)
        time.sleep(t)
        funciones_GC.screenShot(self, "Datos-del-Ciudadano")

    def LogOutMicuenta(self):
        funciones_GC.scrollToElement(self, By.XPATH, userElements.ButtonLogouMicuenta)
        time.sleep(t)
        funciones_GC.click_Field(self, By.XPATH, userElements.ButtonLogouMicuenta)
        time.sleep(t)
        funciones_GC.validates_visibility(self, By.XPATH, userElements.ModalAlertaMicuenta)
        time.sleep(t)
        funciones_GC.click_Field_visibility(self, By.XPATH, userElements.ButtonModalCerrarSesion)
        funciones_GC.click_Field_visibility(self, By.XPATH, userElements.buttonVolverAlInicio)



