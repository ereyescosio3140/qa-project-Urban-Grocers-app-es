Automatización de Pruebas para Urban Grocers App

Descripción del Proyecto:
Este proyecto implementa pruebas automatizadas para la API de Urban Grocers. Su objetivo es validar la calidad de los endpoints críticos que soportan las principales funcionalidades de la aplicación, garantizando su correcto funcionamiento y robustez frente a errores.

Tecnologías Utilizadas:
Lenguaje: Python, 
Framework de Pruebas: Pytest, 
Biblioteca para Solicitudes HTTP: Requests, 
Formato de Datos: JSON

Instrucciones para Ejecutar el Proyecto:
1. Clona el repositorio:
git clone <URL-del-repositorio>
cd <nombre-del-directorio>
2. Instala las dependencias:
Asegúrate de tener pip instalado y ejecuta:
pip install -r requirements.txt
3. Configura las variables de entorno (si es necesario):
Si tu proyecto requiere variables específicas para URLs o tokens, configúralas en tu terminal.
export URL_SERVICE=[https://example.com/api/v1](https://cnt-d72c1bfc-4dc1-437e-b89a-8815ed402384.containerhub.tripleten-services.com/)
export AUTH_TOKEN=your_token
4. Ejecuta el proyecto:
Si tienes scripts principales, indícalos aquí. Ejemplo:
python sender_stand_request.py

Instrucciones para Ejecutar las Pruebas:
1. Ejecuta todas las pruebas:
pytest tests/
2. Ejecuta pruebas específicas:
Si deseas ejecutar un archivo o prueba en particular, usa:
pytest tests/test_create_kit.py

Estructura del Proyecto:

├── tests/                     # Directorio de pruebas  
│   ├── test_create_kit.py     # Pruebas para la creación de kits  
├── sender_stand_request.py    # Archivo para manejar solicitudes estándar  
├── configuration.py           # Configuración del proyecto  
├── data.py                    # Datos y headers utilizados en las pruebas  
├── requirements.txt           # Lista de dependencias del proyecto  
├── README.md                  # Documentación  
