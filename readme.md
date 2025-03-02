🚀 Guía de FastAPI y Uvicorn
📌 ¿Qué es FastAPI?
FastAPI es un framework moderno para construir APIs en Python de manera rápida y eficiente.
Se basa en Python type hints y utiliza Pydantic para la validación de datos.

✨ Características principales de FastAPI
✅ Rápido y eficiente → Optimizado para alto rendimiento, comparable a Node.js y Go.
✅ Documentación automática → Genera /docs (Swagger) y /redoc sin configuración extra.
✅ Validación de datos con Pydantic → Detecta y rechaza datos incorrectos.
✅ Compatible con Async/Await → Manejo eficiente de múltiples solicitudes.
✅ Basado en estándares → Compatible con OpenAPI y JSON Schema.

🛠️ ¿Qué es Uvicorn?
Uvicorn es un servidor ASGI ligero y rápido para ejecutar aplicaciones FastAPI.
Es compatible con WebSockets y HTTP/2, mejorando el rendimiento de la API.

📌 ¿Por qué usar Uvicorn?
Permite manejar múltiples peticiones concurrentes.
Compatible con frameworks modernos como FastAPI y Starlette.
Soporta despliegue en producción con configuraciones optimizadas.
🚀 Cómo ejecutar una API FastAPI con Uvicorn
1️⃣ Instalar FastAPI y Uvicorn
    #pip install fastapi uvicorn

2️⃣ Ejecutar el servidor
    #uvicorn main:app --reload

📌 Explicación:
main → Nombre del archivo (main.py).
app → Nombre de la instancia FastAPI en el código (app = FastAPI()).
--reload → Recarga automática al hacer cambios en el código (modo desarrollo).

📌 Buenas prácticas al definir endpoints en FastAPI
✅ Usar verbos HTTP correctamente

GET → Para obtener datos.
POST → Para enviar datos nuevos.
PUT → Para actualizar un recurso existente.
DELETE → Para eliminar un recurso.

✅ Definir rutas claras y organizadas
Usa nombres en plural: /users/, /products/.
Evita nombres genéricos como /data/ o /info/.

✅ Agregar documentación a los endpoints
Usa summary y description en cada endpoint para que la API sea más fácil de entender.

✅ Proteger endpoints con validaciones
Asegúrate de validar los datos correctamente usando BaseModel para evitar errores.

✅ Utilizar respuestas HTTP adecuadas
200 OK → Respuesta exitosa.
201 Created → Cuando se crea un recurso.
400 Bad Request → Datos incorrectos enviados por el cliente.
404 Not Found → Recurso no encontrado.
500 Internal Server Error → Error inesperado en el servidor.

#CLASES 
    🏗️ Uso de BaseModel en FastAPI
    📌 ¿Qué es BaseModel?
    BaseModel es una clase de Pydantic que permite definir modelos de datos en FastAPI.
    Sirve para validar, serializar y documentar datos automáticamente, evitando errores comunes al recibir información en una API.

    ✨ Características de BaseModel
    ✅ Validación automática de datos → Rechaza datos incorrectos antes de procesarlos.
    ✅ Conversión de tipos → Si envías un número como string ("25"), lo convierte a int.
    ✅ Generación automática de documentación → FastAPI usa estos modelos para mostrar esquemas en /docs.
    ✅ Protección de la API → Evita que se envíen datos no esperados o con tipos incorrectos.

    #EN FASTAPI ES RECOMENDABLE TIPAR CADA VARIABLE

#STATUS CODE
📌 Códigos de Estado HTTP (Status Codes) en FastAPI
Los códigos de estado HTTP indican el resultado de una solicitud a una API.
FastAPI permite personalizar estos códigos para responder de manera más precisa a cada escenario.

✅ Categorías de Status Codes
📌 1xx - Respuestas informativas
100 Continue → El servidor ha recibido la solicitud y el cliente puede continuar enviando datos.

📌 2xx - Éxito
200 OK → Respuesta exitosa (usada en GET, PUT, DELETE).
201 Created → Se ha creado un nuevo recurso (usado en POST).
204 No Content → Operación exitosa, pero sin contenido en la respuesta.

📌 3xx - Redirecciones
301 Moved Permanently → El recurso ha sido movido de forma permanente.
304 Not Modified → Indica que el recurso no ha cambiado desde la última solicitud.

📌 4xx - Errores del Cliente
400 Bad Request → Datos inválidos enviados por el cliente.
401 Unauthorized → Se requiere autenticación para acceder.
403 Forbidden → Acceso prohibido, incluso con autenticación.
404 Not Found → El recurso solicitado no existe.
422 Unprocessable Entity → Error de validación de datos en FastAPI (cuando fallan los modelos Pydantic).

📌 5xx - Errores del Servidor
500 Internal Server Error → Error inesperado en el servidor.
503 Service Unavailable → El servidor no puede procesar la solicitud en ese momento.

#ROUTERS

🚀 Routers en FastAPI
En FastAPI, los routers (APIRouter) permiten estructurar mejor nuestra API separando las rutas en módulos más organizados. Esto es útil cuando nuestra aplicación crece y tenemos múltiples endpoints.

🛠 Pasos para usar APIRouter
1️⃣ Importar APIRouter y definir un router
2️⃣ Definir los endpoints dentro del router
3️⃣ Registrar el router en main.py


📌 Características de los Routers
Permiten agrupar rutas relacionadas en módulos independientes.
Facilitan la organización del código en grandes aplicaciones.
Se pueden asignar prefijos (prefix) a las rutas para evitar redundancias.
Se pueden agrupar por etiquetas (tags) para mejorar la documentación interactiva de FastAPI.
Son reutilizables y se pueden importar en la aplicación principal (main.py).

✔ Usar prefix="/ruta" para evitar repetir rutas en cada endpoint.
✔ Asignar tags=["nombre"] para mejorar la documentación.
✔ Mantener el código modular e importar routers en main.py.


