Feature: categorias de solicitud Mesa de ayuda con Confirmacion


  Scenario Outline: Flujo de Mesa de ayuda
    Given  Iniciando Navegador en la Web https://gestioncolaborativa-hml.gcba.gob.ar/prestaciones
    When Realizar click en ingresar con MiBA
    When Realizar click en ingresar con email
    When Escribiendo campo  Username :"<Correo>"
    When Escribiendo campo password :"<Password>"
    When Realizar click en el bonton ingresar
    When Categoria Solicitud Mesa de ayuda
    Then Validar inicio de sesion y cerrar sesion


  Examples:
    | Correo                      | Password  |
    | pablorondon789789@gmail.com | 123456789 |
