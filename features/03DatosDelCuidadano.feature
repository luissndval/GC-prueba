Feature: Visualizar sección MI CUENTA


  Scenario Outline: Ver datos del ciudadano en sistema
    Given  Iniciando Navegador en la Web https://gestioncolaborativa-hml.gcba.gob.ar/prestaciones
    When Realizar click en ingresar con MiBA
    When Realizar click en ingresar con email
    When Escribiendo campo  Username :"<Correo>"
    When Escribiendo campo password :"<Password>"
    When Realizar click en el bonton ingresar
    When visualizar datos en MI CUENTA
    Then Validar inicio de sesion y cerrar sesion


  Examples:
    | Correo                      | Password  |
    | pablorondon789789@gmail.com | 123456789 |