import time
from selenium.webdriver.common.by import By
from Funciones.Funciones_GC import funciones_GC
from elements import solicitudesElements
from elements.solicitudesElements import *

##############################################################################################################
t = 1

##############################################################################################################
class Pintura_Grafitis(funciones_GC):
    def solicitud_pintura(self):
        funciones_GC.validates_visibility(self, By.XPATH, solicitudesElements.seccionPintura)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.seccionPintura)
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
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.tipodeFrente)
        funciones_GC.validates_visibility(self, By.XPATH, solicitudesElements.btnSiguienteTipodeFrente)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btnSiguienteTipodeFrente)
        time.sleep(t)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.lugar)
        funciones_GC.validates_visibility(self, By.XPATH, solicitudesElements.btnSigueinteLugar)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btnSigueinteLugar)
        time.sleep(t)
        funciones_GC.input_Texto(self, By.XPATH, solicitudesElements.textAreaPintura1, "1122334455")
        funciones_GC.click_Field_optional(self, By.XPATH, solicitudesElements.btnSiguiente2)
        time.sleep(t)
        funciones_GC.input_Texto(self,By.XPATH, solicitudesElements.textArea, "pintura en la pared")
        '''CARGA DE IMG Y PDF'''
        funciones_GC.subirArchivo(self, By.XPATH, solicitudesElements.cargarArchivo,
                                    '/home/paulrodriguez/Documentos/GC-Automation/IMG/photo.jpg')
        funciones_GC.click_Field_optional(self, By.XPATH, solicitudesElements.btnContedorSiguiente2)
        time.sleep(t)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btnSiguienteNS)

    ##############################################################################################################

    def Cancelar_la_Solicitud(self):
        funciones_GC.validates(self, By.XPATH, solicitudesElements.btnCancelarNS)
        funciones_GC.screenShot(self, "Datos de la solicitud")
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btnCancelarNS)
        time.sleep(t)

    ##############################################################################################################

    def Alerta_de_Cancelar(self):
        funciones_GC.validates_visibility(self, By.XPATH, solicitudesElements.ventanaModal)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.buttonSI)

