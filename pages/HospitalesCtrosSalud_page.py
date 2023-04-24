import time
from selenium.webdriver.common.by import By
from Funciones.Funciones_GC import funciones_GC
from elements import solicitudesElements
from elements.solicitudesElements import *

##############################################################################################################
t = 1
ITHCS = "Inconvenientes con turnos en centro de salud u Hospital Público"
##############################################################################################################
class Hospitales_Ctros_Salud(funciones_GC):
    def input_buscador(self):
        funciones_GC.input_Texto(self, By.XPATH, solicitudesElements.inputPrestaciones, ITHCS)
        funciones_GC.clickAction(self, By.XPATH, solicitudesElements.prestacionesSugerencia)
        time.sleep(t)
        funciones_GC.scrollToElement_visibility(self, By.XPATH, solicitudesElements.buttonConfirmar)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.buttonConfirmar)

    ################################### HASTA AQUI FUNCIONA EL MAPA NO REACCIONA #############################
##############################################################################################################

    def buscar_En_El_Mapa(self):
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.lugarDeSolicitud)
        funciones_GC.input_Texto(self, By.XPATH, solicitudesElements.lugarDeSolicitud, "Hospital Argerich (Infectología)")
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
        funciones_GC.validates_visibility(self, By.XPATH, solicitudesElements.radiobtn_Turno)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.radiobtn_Turno)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.siguiente_preguntaAbierta2)
        time.sleep(t)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.radiobtn_almacen)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btn_siguiente_almacen)
        time.sleep(t)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.radiobtn_loca_en_la_calle)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btn_siguiente_almacen)
        time.sleep(t)
        funciones_GC.input_Texto(self, By.XPATH, solicitudesElements.text_preguntaAbierta1, "TEXTO DE RELLENO 2")
        funciones_GC.validates_visibility(self, By.XPATH, solicitudesElements.siguiente_preguntaAbierta2)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.siguiente_preguntaAbierta2)
        time.sleep(t)
        funciones_GC.input_Texto(self, By.XPATH, solicitudesElements.text_preguntaAbierta1, "TEXTO DE RELLENO 3")
        funciones_GC.validates_visibility(self, By.XPATH, solicitudesElements.siguiente_preguntaAbierta2)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.siguiente_preguntaAbierta2)
        time.sleep(5)
        funciones_GC.input_Texto(self, By.XPATH, solicitudesElements.textArea, "TEXTO DE RELLENO 4")
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
