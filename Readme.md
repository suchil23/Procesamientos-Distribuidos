* Procesamiento Distribuido

Función process_node:

Simula el procesamiento de datos en un nodo.

Utiliza await asyncio.sleep(1) para simular un tiempo de procesamiento.

Almacena el resultado en el diccionario results.

* Función send_data:

Simula el envío de datos a un nodo utilizando aiohttp para manejar solicitudes HTTP de manera asíncrona.

En este caso, simplemente llama a process_node para simular el procesamiento local.

* Función main:

Define los "trozos" de datos que se enviarán a los nodos.

Crea una lista de tareas asíncronas para enviar los datos a los nodos.

Utiliza await asyncio.gather(*tasks) para ejecutar todas las tareas concurrentemente y esperar a que terminen.

* Ejecución del programa:

Llama a asyncio.run(main()) para ejecutar la función principal de manera asíncrona.