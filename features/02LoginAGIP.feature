Feature: Inicio de Sesion con CUIT Valido


  Scenario Outline: Ingresar con AGIP
    Given  Iniciando Navegador en la Web https://gestioncolaborativa-hml.gcba.gob.ar/prestaciones
    When Realizar click en ingresar con MiBA
    When Realizar click en ingresar con AGIP
    When Escribiendo campo  User :"<CUIT>"
    When Escribiendo campo passw :"<Clave>"
    When Realizar click en el bonton ingresar AGIP
    Then Validar inicio de sesion y cerrar sesion


  Examples:
    | CUIT | Clave     |
    | 27289083524     | Troquel1 |