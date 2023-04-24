#########BUTTON - SIGUIENTE  - VOLVER - CONFIRMAR - CANCELAR#####################
buttonSiguiente = "//button[contains(text(),'Siguiente')]"
buttonConfirmar = "//button[@type='button'][contains(.,'Confirmar')]"
btnContedorSiguiente = "(//button[@class='btn btn-sm btn-primary'][contains(.,'Siguiente')])[1]"
btnContedorSiguiente2 = "(//button[@class='btn btn-sm btn-primary'][contains(.,'Siguiente')])[2]"
btnCancelarNS = "/html/body/app-root/app-confirmacion-solicitud/main/section/div/div[5]/div[2]/div/div/div[2]/button[2]"
btnSiguienteNS = "//body/app-root[1]/app-datos-solicitud[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[2]/button[2]"
buttonVolver = "//body/app-root[1]/app-datos-solicitud[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[2]/button[2]"
#######################CONTENEDORES DE CUESTIONARIO INPUT TEXT###################
textArea = "//textarea[@id='text-area']"
text_preguntaAbierta1 = "//textarea[contains(@name,'preguntaAbierta')]"
text_preguntaAbierta2 = " //textarea[contains(@class,'form-control ng-pristine ng-valid ng-touched')]"
textAreaPintura1 = "(//textarea[@class='form-control ng-untouched ng-pristine ng-valid'])[1]"
siguiente_preguntaAbierta1 ='//*[@id="collapseCuestionario"]/div/button'
btntxtAreaSiguiente = "(//button[contains(@class,'btn btn-sm btn-primary')])[1]"
siguiente_preguntaAbierta2 = "//button[@class='btn btn-sm btn-default btn-primary'][contains(.,'Siguiente')]"
#######################CONTENEDORES DE CUESTIONARIO INPUT TEXT###################
radiobtn_Turno = "//label[@class='custom-control-label'][contains(.,'Me cancelaron el turno')]"
#########################################################
cargarArchivo = '//*[@id="file-upload"]'
seccionPintura = "//span[@class='access-title'][contains(.,'Pintura sobre grafitis')]"
btnConfirmarSolicitud = "//button[@type='submit'][contains(.,'Confirmar')]"
######################CONFIRMAR SOLICITUD MDA##################################
ventanaModalFinal ="(//div[contains(@class,'app-modal-body')])[5]"
experieciaCheck = "(//input[contains(@type,'radio')])[4]"
btnAceptarSolicitud ="(//button[@type='button'][contains(.,'Aceptar')])[4]"
#################MDA- VALIDAR######################
getNumeroSolicitud = "//span[contains(.,'Nro de solicitud:')]"
btnVolverMDA = "//button[contains(text(),'Volver')]"
ultimaSolicitud = "(//h4[@class='texto-responsive'][contains(.,'Nº de solicitud:')])[1]"
##############################ELEMENTOS DEL MAPA################################
lugarDeSolicitud = "//input[contains(@placeholder,'Lugar de tu solicitud. Ej: Uspallata 3160')]"
sugerenciaDeBusqueda = "(//a[contains(@class,'titulo-sugerencia')])[1]"
pingUbicacion = "//*[@id='map']/div[1]/div[4]/img"
nuevaSolicitudMap = "//*[@id='popupButton']"
direccion = "Santa Fe av 1750"
#########################################################
tipodeFrente = "//label[contains(text(),'Comercio')]"
btnSiguienteTipodeFrente = "//body/app-root[1]/app-datos-solicitud[1]/main[1]/section[1]/div[1]/div[1]/div[1]/mat-accordion[1]/div[1]/app-contenedor-cuestionario[1]/div[1]/div[1]/div[1]/div[1]/button[1]"
lugar = "//label[contains(text(),'Pared')]"
btnSigueinteLugar = "(//button[contains(.,'Siguiente')])[1]"
btnSiguiente2 = '//*[@id="collapseCuestionario"]/div/button[2]'
selectInconveniente = "//label[contains(text(),'Los datos básicos del titular del turno no coincid')]"
btnSiguenteMDA2 = '//*[@id="collapseDescribirSituacion"]/div/button[2]'
##############################ELEMENTOS DE NUEVA SOLICITUD#######################
ventanaModal = "/html/body/app-root/app-confirmacion-solicitud/app-modal-simple[3]/app-modal/div/div/div/div[3]"
buttonSI = "//button[@type='button'][contains(.,'Sí')]"

##############################INPUT PRESATACIONES################################
inputPrestaciones = "//input[@id='prestaciones']"
prestacionesSugerencia = "//button[@id='ngb-typeahead-0-0']"
##############################RADIO BUTTON ALIMENTOS Y BEBIDAS###################
radiobtn_establecimiento = "//label[contains(text(),'Locales comerciales de venta de alimentos y bebida')]"
btn_siguiente_establecimiento = "//*[@id='collapseCuestionario']/div/button[2]"
radiobtn_almacen = "//label[@class='custom-control-label'][contains(.,'Almacén y autoservicios')]"
btn_siguiente_almacen = "//body/app-root[1]/app-datos-solicitud[1]/main[1]/section[1]/div[1]/div[1]/div[1]/mat-accordion[1]/div[1]/app-contenedor-cuestionario[1]/div[1]/div[1]/div[1]/div[1]/button[2]"
radiobtn_loca_en_la_calle = "//label[contains(text(),'Local a la calle')]"
btn_siguiente_establecimiento_denunciado = "//button[@class='btn btn-sm btn-default btn-primary'][contains(.,'Siguiente')]"
#########ELEMENTOS DE TODAS LAS CATEGORIAS DE SOLICITUDES########################
Alumbrado = "//h4[@class='card-title'][contains(.,'Alumbrado')]"
txtAlumbrado = "//h3[contains(text(),'Alumbrado')]"
opcionAlumbrado = "//span[@class='access-title'][contains(.,'Reparación de luminaria')]"
boxAlumbrado = "//label[@class='custom-control-label'][contains(.,'Luminaria apagada durante la noche')]"
################################################################################
Animales = "//h4[@class='card-title'][contains(.,'Animales')]"
opcionAnimales = "//span[contains(text(),'Reclama a tu Perro/Gato')]"
txtAnimales = "//h3[contains(text(),'Animales')]"
tipoAnimales = "//label[contains(text(),'Perro')]"
IdReclamo = '//*[@id="collapseCuestionario"]/div/div[2]/input'
IdAnimal = "0002"
btnSiguienteAnimales = '//*[@id="collapseCuestionario"]/div/button'
################################################################################
Arbolado = "//h4[contains(text(),'Arbolado')]"
txtArbolado = "//h3[contains(text(),'Arbolado')]"
opcionArbolado = "//span[contains(text(),'Enfermedades en árbol')]"
boxArbolado = '//*[@id="pregunta0"]/div/div[1]/label'
################################################################################
Calles = "//h4[contains(text(),'Calles, Fachadas y Veredas')]"
txtCalles = "//h3[contains(text(),'Calles, Fachadas y Veredas')]"
opcionCalles = '//span[contains(.,"Reparación de vereda")]'
boxCalles = "//*[@id='pregunta0']/div/div[2]/label"
################################################################################
ControlEdifObras = "//h4[contains(text(),'Control Edilicio, Obras y Catastro')]"
txtControlEdifObras = "//h3[contains(text(),'Control Edilicio, Obras y Catastro')]"
opcionEdifObras = "/html/body/app-root/app-detalle-categoria/main/section/div/div[2]/div[3]/div/a/span"
boxEdifObras = "//label[contains(text(),'Obra sin protección a edificios linderos')]"
################################################################################
Educacion = "//h4[contains(text(),'Educación')]"
txtEducacion = "//h3[contains(text(),'Educación')]"
opcionEducacion = "/html/body/app-root/app-detalle-categoria/main/section/div/div[2]/div[5]/div/a"
boxEducacion = "//label[contains(text(),'Suministro eléctrico')]"
################################################################################
Fiscalizacion = "//h4[contains(text(),'Fiscalización Actividades Comerciales')]"
txtfiscalizacion = "//h3[contains(text(),'Fiscalización Actividades Comerciales')]"
opcionFiscalizacion = "//span[contains(text(),'Higiene y salud')]"
boxFiscalizacion = "//label[contains(text(),'Alimentos o bebidas en malas condiciones')]"
################################################################################
Limpieza = "//h4[contains(text(),'Limpieza y Recolección')]"
txtLimpieza = "//h3[contains(text(),'Limpieza y Recolección')]"
opcionLimpienza = "//a[@class='list-group-item'][contains(.,'Residuos voluminosos')]"
boxLimpieza = "//label[contains(text(),'Retiro de residuos verdes')]"
################################################################################
MesaDeAyuda = "//h4[contains(text(),'Mesa de ayuda de sistemas y trámites digitales')]"
txtMesaDeAyuda = "//h3[contains(text(),'Mesa de ayuda de sistemas y trámites digitales')]"
opcionMesaDeAyuda = "//a[@class='list-group-item'][contains(.,'Turnos')]"
boxMesaDeAyuda = "//label[contains(text(),'Trámites a Distancia-TAD')]"
siguienteMDA = "//*[@id='pregunta0']/div/button"
boxSiguenteMDA = "//label[contains(text(),'Con la devolución de pago (BUI/CENAT)')]"
################################################################################
Ordenamiento = "//h4[contains(text(),'Ordenamiento del Espacio Público')]"
txtOrdenamiento = "//h3[contains(text(),'Ordenamiento del Espacio Público')]"
opcionOrdenamiento = "(//a[contains(@class,'list-group-item')])[3]"
boxOrdenamiento = "//label[contains(.,'Manteros/venta ambulante')]"
################################################################################
Parques = "//h4[contains(text(),'Parques y Plazas')]"
txtParques = "//h3[contains(text(),'Parques y Plazas')]"
opcionParques = "//span[contains(text(),'Plazas y Parques de la Ciudad')]"
boxParques = "//label[contains(text(),'Mantenimiento de bancos, mesas y sillas en parque/')]"
################################################################################
Pluviales = "//h4[contains(text(),'Pluviales')]"
txtPluviales = "//h3[contains(text(),'Pluviales')]"
opcionPluviales = "//span[contains(text(),'Alcantarillas / sumideros')]"
boxPluviales = "//label[contains(text(),'Sumidero/alcantarilla rota')]"
################################################################################
Proteccion = "//h4[contains(text(),'Protección Ambiental')]"
txtProteccion = "//h3[contains(text(),'Protección Ambiental')]"
opcionProteccion = "//span[contains(.,'Ruidos molestos, emanaciones o derrames')]"
boxProteccion = "//label[contains(text(),'Ruidos molestos y vibraciones')]"
################################################################################
Reciclado = "//h4[contains(text(),'Reciclado')]"
txtReciclado = "//h3[contains(text(),'Reciclado')]"
opcioneReciclado = "//a[@class='list-group-item'][contains(.,'Puntos Verdes')]"
boxReciclado = "//label[contains(text(),'Punto Verde cerrado en horario de atención')]"
################################################################################
Salud = "//h4[contains(text(),'Salud')]"
txtSalud = "//h3[contains(text(),'Salud')]"
opcionSalud = "//span[@class='access-title'][contains(.,'Atención en Hospitales Públicos y Centros de Salud')]"
boxSalud = "//label[contains(text(),'Con un turno en un Centro de Salud u Hospital Públ')]"
################################################################################
Seguridad = "//h4[contains(text(),'Seguridad')]"
txtSeguridad = "//h3[contains(text(),'Seguridad')]"
################################################################################
Servicios = "//h4[contains(text(),'Servicios')]"
txtServicios = "//h3[contains(text(),'Servicios')]"
################################################################################
Sugerencias = "//h4[contains(text(),'Sugerencias y Libro de Quejas')]"
txtSugerencias = "//h3[contains(text(),'Sugerencias y Libro de Quejas')]"
opcionSugerencias = "//body/app-root[1]/app-detalle-categoria[1]/main[1]/section[1]/div[1]/div[2]/div[3]/div[1]/a[1]"
boxSugerencias = "//label[@class='custom-control-label'][contains(.,'Con un turno en un Centro de Salud u Hospital Público')]"
################################################################################
Transito = "//h4[contains(text(),'Tránsito y Transporte')]"
txtTransito = "//h3[contains(text(),'Tránsito y Transporte')]"
opcionTransito = "//span[@class='access-title'][contains(.,'Subtes')]"
boxTransito = "//label[contains(text(),'Interrupciones')]"

###############################LISTA DE ELEMENTOS###############################
Categorias = list([Alumbrado, Animales, Arbolado, Calles, ControlEdifObras, Educacion, Fiscalizacion, Limpieza,
                   MesaDeAyuda, Ordenamiento, Parques, Pluviales, Proteccion, Reciclado, Salud, Seguridad,
                   Servicios, Sugerencias, Transito])
Categorias2 = list([Alumbrado, Animales, Arbolado, Calles, ControlEdifObras, Educacion, Fiscalizacion, Limpieza,
                   MesaDeAyuda, Ordenamiento, Parques, Pluviales, Proteccion, Reciclado, Salud, Sugerencias, Transito])
################################################################################
txtCategorias = list([txtAlumbrado, txtAnimales, txtArbolado, txtCalles, txtControlEdifObras, txtEducacion,
                      txtfiscalizacion, txtLimpieza, txtMesaDeAyuda, txtOrdenamiento, txtParques, txtPluviales,
                      txtProteccion, txtReciclado, txtSalud, txtSeguridad, txtServicios, txtSugerencias,
                      txtTransito])
################################################################################
opcionCategorias = list([opcionAlumbrado, opcionArbolado, opcionCalles, opcionEdifObras, opcionEducacion,
                      opcionFiscalizacion, opcionLimpienza, opcionMesaDeAyuda, opcionOrdenamiento, opcionParques,
                      opcionPluviales, opcionProteccion, opcioneReciclado, opcionSalud, opcionSugerencias,
                      opcionTransito])

boxCategorias = list([boxAlumbrado, boxArbolado, boxCalles, boxEdifObras, boxEducacion,
                      boxFiscalizacion, boxLimpieza, boxMesaDeAyuda, boxOrdenamiento, boxParques,
                      boxPluviales, boxProteccion, boxReciclado, boxSalud, boxSugerencias,
                      boxTransito])


