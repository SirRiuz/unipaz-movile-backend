<h1>unipaz-mobile</h1>
<p>unipaz-mobile es una aplicación móvil desarrollada con React Native para la Universidad de la Paz. La aplicación permite a los estudiantes de la universidad acceder a información importante sobre la institución y su progreso académico.</p>
<h2>Tecnologías utilizadas</h2>
<ul>
<li><a href="https://reactnative.dev/">React Native</a>: Framework utilizado para desarrollar la aplicación móvil.</li>
<li><a href="https://www.python.org/">Python</a>: Lenguaje de programación utilizado para desarrollar el back-end de la aplicación.</li>
<li><a href="https://fastapi.tiangolo.com/">FastAPI</a>: Framework web utilizado para construir la API RESTful de la aplicación.</li>
<li><a href="https://pandas.pydata.org/">Pandas</a>: Biblioteca de análisis de datos utilizada para procesar y analizar los datos de la universidad.</li>
<li><a href="https://aws.amazon.com/">AWS</a>: Plataforma de alojamiento en la nube utilizada para implementar y alojar el back-end de la aplicación.</li>
<li><a href="https://redis.io/">Redis</a>: Sistema de base de datos en memoria utilizado para almacenar en caché datos de la aplicación.</li>
<li><a href="https://www.crummy.com/software/BeautifulSoup/">Beautiful Soup</a>: Biblioteca de web scraping utilizada para extraer información de sitios web.</li>
<li><a href="https://requests.readthedocs.io/en/master/">Requests</a>: Biblioteca utilizada para realizar solicitudes HTTP.</li>
</ul>
<h2>Características</h2>
<ul>
<li>Información sobre los cursos y programas de la universidad obtenida a través de web scraping del portal académico de la universidad en <code>http://unipaz.uxxi.com/</code>.</li>
<li>Consulta del progreso académico de los estudiantes.</li>
<li>Estadísticas sobre el rendimiento académico de los estudiantes.</li>
<li>Acceso a información importante sobre la universidad y los servicios que ofrece.</li>
<li>Extracción de información de sitios web externos a través de web scraping.</li>
<li>Almacenamiento en caché de datos utilizando Redis.</li>
</ul>
<h2>Instalación</h2>
<p>Para instalar el proyecto, sigue estos pasos:</p>
<ol>
<li>Clona el repositorio de GitHub:</li>
<pre><code>git clone https://github.com/tu-usuario/unipaz-mobile.git</code></pre>
<li>Instala las dependencias utilizando pip:</li>
<pre><code>pip install -r requirements.txt</code></pre>
<li>Configura las variables de entorno en un archivo <code>.env</code>. Puedes utilizar el archivo <code>.env.example</code> como plantilla.</li>
<li>Ejecuta el servidor web:</li>
<pre><code>uvicorn main:app --reload</code></pre>
</ol>
<h2>Contribución</h2>
<p>Si deseas contribuir al desarrollo de unipaz-mobile, puedes hacer un fork del repositorio en GitHub y enviar tus pull requests con tus cambios propuestos. También puedes abrir un issue si encuentras algún problema o tienes alguna sugerencia para mejorar la aplicación.</p>
<h2
