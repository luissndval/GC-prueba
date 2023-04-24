from selenium.webdriver.common.by import By
from elements import solicitudesElements
from elements import userElements
'''from elements.solicitudesElements import *'''
from Funciones.Funciones_GC import *

##############################################################################################################
t = 2
##############################################################################################################

class Mesa_de_Ayuda(funciones_GC):
    def solicitud_Mesa_de_Ayuda(self):
        funciones_GC.scrollToElement_visibility(self, By.XPATH, solicitudesElements.MesaDeAyuda)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.MesaDeAyuda)
        time.sleep(t)
        ###############CONFIRMAR LEYENDA - Y VALIDAR####################
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.opcionMesaDeAyuda)
        funciones_GC.scrollToElement_visibility(self, By.XPATH, solicitudesElements.buttonConfirmar)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.buttonConfirmar)

    ##########################################################################################################

    def Cargar_Nueva_Solicitud(self,):
        ####CONTESTA EL CUESTIONARO-INPUT INCONVENIENTE DE TURNO########
        funciones_GC.input_Texto(self, By.XPATH, solicitudesElements.textAreaPintura1, "CUIT DNI CEDULA")
        funciones_GC.click_Field_optional(self, By.XPATH, solicitudesElements.siguiente_preguntaAbierta1)
        time.sleep(t)
        ##################SELECCIONA EL INCONVENIENTE###################
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.selectInconveniente)
        funciones_GC.validates_visibility(self, By.XPATH, solicitudesElements.btnSiguiente2)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btnSiguiente2)
        time.sleep(t)
        ###############DESCRIBI LA SITUACION -INPUT####################
        funciones_GC.input_Texto(self,By.XPATH, solicitudesElements.textArea, "Texto de Relleno")
        funciones_GC.click_Field_optional(self, By.XPATH, solicitudesElements.btnSiguenteMDA2)
        ###################CARGA DE IMG Y PDF#########################
        funciones_GC.subirArchivo(self, By.XPATH, solicitudesElements.cargarArchivo,
                                    '/home/paulrodriguez/Documentos/GC-Automation/IMG/photo.jpg')
        funciones_GC.click_Field_optional(self, By.XPATH, solicitudesElements.btnContedorSiguiente2)
        time.sleep(t)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btnSiguienteNS)

    ##########################################################################################################
    def Confirmar_la_Solicitud(self,):
        funciones_GC.validates(self, By.XPATH, solicitudesElements.btnConfirmarSolicitud)
        funciones_GC.screenShot(self, "Datos de la solicitud")
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btnConfirmarSolicitud)
        time.sleep(t)

    ##########################################################################################################
    def Modal_Solicitud_Exitosa(self):
        funciones_GC.validates_visibility(self, By.XPATH, solicitudesElements.ventanaModalFinal)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.experieciaCheck)
        time.sleep(t)
        funciones_GC.validates_visibility(self, By.XPATH, solicitudesElements.btnAceptarSolicitud)
        funciones_GC.click_Field(self, By.XPATH, solicitudesElements.btnAceptarSolicitud)
        time.sleep(t)

    ##########################################################################################################

    def Confirmar_Mis_Solicitudes(self):
        funciones_GC.scrollToElement_visibility(self, By.XPATH, userElements.ButtonListUser)
        funciones_GC.click_Field(self, By.XPATH, userElements.ButtonListUser)
        time.sleep(t)
        funciones_GC.validates_visibility(self, By.XPATH, userElements.buttonMisSolicitudes)
        funciones_GC.click_Field(self, By.XPATH, userElements.buttonMisSolicitudes)
        time.sleep(t)
        funciones_GC.screenShot(self, "mis solicitudes")
        funciones_GC.scrollToElement(self, By.XPATH, userElements.ButtonLogouMicuenta)
        time.sleep(t)
        funciones_GC.click_Field(self, By.XPATH, userElements.ButtonLogouMicuenta)










