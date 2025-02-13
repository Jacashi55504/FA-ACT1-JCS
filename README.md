# Intercambio de Claves y Ataque MITM en Diffie-Hellman

Este repositorio contiene una implementación del protocolo Diffie-Hellman y una simulación del ataque Man-in-the-Middle (MITM) para demostrar sus vulnerabilidades cuando no se utiliza autenticación.

## Descripción
El código realiza los siguientes pasos:
1. Define un número primo estándar de Diffie-Hellman.
2. Genera claves privadas para Alice, Bob y Eve.
3. Calcula las claves compartidas entre Alice y Bob con la intervención de Eve.
4. Verifica si Eve logra obtener la clave secreta compartida.
5. Aplica la función hash a las claves obtenidas.

## Resultados
El programa mostrará las claves generadas, los mensajes intercambiados y la clave secreta obtenida por Eve.

## JCS
