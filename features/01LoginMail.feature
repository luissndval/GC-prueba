Feature: Inicio de Sesion con MAil Valido


  Scenario Outline: Ingresar con MAIL
    Given  Iniciando Navegador en la Web https://gestioncolaborativa-hml.gcba.gob.ar/prestaciones
    When Realizar click en ingresar con MiBA
    When Realizar click en ingresar con email
    When Escribiendo campo  Username :"<Correo>"
    When Escribiendo campo password :"<Password>"
    When Realizar click en el bonton ingresar
    Then Validar inicio de sesion y cerrar sesion


  Examples:
    | Correo                      | Password  |
    | pablorondon789789@gmail.com | 123456789 |