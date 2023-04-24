import time
from selenium.webdriver.common.by import By
from Funciones.Funciones_GC import funciones_GC
from elements import solicitudesElements
from elements.solicitudesElements import *

##############################################################################################################
t = 1
Luminaria = "luminaria apagada durante la noche"
##############################################################################################################
class Alumbrado(funciones_GC):
    def input_Liminaria(self):
        funciones_GC.input_Texto(self, By.XPATH, solicitudesElements.inputPrestaciones, Luminaria)
        funciones_GC.clickAction(self, By.XPATH, solicitudesElements.prestacionesSugerencia)
        time.sleep(t)
        funciones_GC.scrollToElement_visibility(self, By.XPATH, solicitudesElements.buttonConfirmar)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.buttonConfirmar)


##############################################################################################################

    def buscar_En_El_Mapa(self):
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.lugarDeSolicitud)
        funciones_GC.input_Texto(self, By.XPATH, solicitudesElements.lugarDeSolicitud, direccion)
        time.sleep(t)
        funciones_GC.clickAction(self, By.XPATH, solicitudesElements.sugerenciaDeBusqueda)
        time.sleep(t)
        funciones_GC.screenShot(self, "busqueda de direccion en el mapa")
        funciones_GC.scrollToElement_visibility(self, By.XPATH, solicitudesElements.pingUbicacion)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.pingUbicacion)
        time.sleep(t)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.nuevaSolicitudMap)


##############################################################################################################

    def Cargar_Nueva_Solicitud(self):
        funciones_GC.input_Texto(self, By.XPATH, solicitudesElements.textArea, "TEXTO DE RELLENO")
        funciones_GC.click_Field_optional(self, By.XPATH, solicitudesElements.btnContedorSiguiente)
        '''CARGA DE IMG Y PDF'''
        funciones_GC.subirArchivo(self, By.XPATH, solicitudesElements.cargarArchivo,
                                    '/home/paulrodriguez/Documentos/GC-Automation/IMG/photo.jpg')
        funciones_GC.click_Field_optional(self, By.XPATH, solicitudesElements.btnContedorSiguiente2)
        time.sleep(t)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btnSiguienteNS)



    def Cancelar_la_Solicitud(self):
        funciones_GC.validates(self, By.XPATH, solicitudesElements.btnCancelarNS)
        funciones_GC.screenShot(self, "Datos de la solicitud")
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btnCancelarNS)
        time.sleep(t)


    def Alerta_de_Cancelar(self):
        funciones_GC.validates_visibility(self, By.XPATH, solicitudesElements.ventanaModal)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.buttonSI)


