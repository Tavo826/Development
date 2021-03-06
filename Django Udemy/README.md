## DJANGO

Promueve la filosofía del desarrollo ágil y extensible, aplicando el pricipio DRY (Don't Repeat Yourself)

### Características importantes:

* Cuenta con un sistema basado en componentes reutilizables (apps).
* Tiene un mapeador ORM para manejar registros de la BD como objetos.
* Panel de administrador para gestionar objetos a través de formularios.
* Sistema de plantillas extensibles con herencia basado en etiquetas.

### Iniciar un proyecto

django-admin startproject **NombreProyecto**

### Apps

Forma en que se organiza el código para ser reutilizado, sirven para gestionar el panel de administrador, la autenticación de los usuarios, entre otros.

Las apps activas se encuentran en settings.py - INSTALLED_APPS

python manage.py startapp **NombreApp** para crear una app

### Vistas

Hacen referencia a la lógica que se ejecuta cuando se hace una petición a la Web

### Urls

Administran la dirección en la que se va a mostrar cada una de las vistas

### Ficheros estáticos (configuración)

Django no puede trabajar con los ficheros estáticos predefinidos en el frontend, para ver cómo quedaría la página finalizada se deben realizar algunas configuraciones

Se crea una carpeta static dentro de la app y se copia allí los recursos estáticos necesarios para la app

### Modelos

Son las clases que están enlazadas a la base de datos de la app, cada clase representa una tabla en la base de datos

### Crear superusuario ADMIN

Es necesario para ingresar el administrador de Django en el que se pueden modificar los modelos del proyecto, los cuales deben estar registrados previamente en el fichero **admin.py** de la app

python manage.py createsuperuser

#### Personalizar el ADMIN (1)

Para modificar el nombre de la app se agrega en el script *apps.py* de la app, la variable **verbose_name** con el nombre que se desea que aparezca, para validar esta acción se debe modificar en la lista **INSTALED_APPS** del script *settings.py* del proyecto:

'portfolio.apps.NombreClase'

Para modificar el nombre del modelo se crea una subclase dentro de la misma clase llamada **Meta** para añadir metadatos extendidos en la que se puede agregar el nombre con que se desea ver el modelo tanto en singular (verbose_name) como en plural (verbose_name_plural), también se puede agregar un campo para ordenar los registros utilizando la variable 

ordering = [lista de atributos con los que se desea ordenar]

Para modificar la foma como se ven las publicaciones en el ADMIN se agrega dentro de la subclase una función *__str__(self)* y retornando de esta el parámetro qeu se desee

Para que se pueda visualizar la fecha de cración y de edición de cada publicación, en el script *admin.py* se crea una clase para extender las funcionalidades del ADMIN, en ella se redefinen el 'created' y el 'updated' como campos de lectura

Para mostrar las imágenes de las publicaciones, como primera medida se guardan en la raíz del proyecto en una carpeta llamada *media*, esta carpeta se registra en el fichero *settings.py*, añadiendo al final la dirección pública de la carpeta (MEDIA_URL), la dirección privada de la carpeta (MEDIA_ROOT). Luego de esto, siempre que se tenga el bug en True, se debe añadir una configuración extendida. En el fichero *urls.py* del proyecto.

### Patrón MVT: Modelo-Vista-Template

Cuando se trabaja con bases de datos y modelos, el proceso que sigue Django es el siguiente:

* Se recibe la petición
* Se pasa a la vista
* En la vista se recuperan los datos del modelo correspondiente
* Se renderiza el template, integrando los datos dinámicos del modelos que se pasa desde la vista, antes de que el navegador muestre el html resultante

### Relaciones entre modelos

#### Relaciones One to One (1:1):

Indican que solo puede haber un perfil por cada usuario

#### Relaciones con foreign keys (1:N):

Permiten enlazar una insancia de un modelo con otra instancia de otro modelo, o del mismo. Un ejemplo es el enlace de una entrada con un usuario que representa al autor

#### Relaciones many to many (N:M): 

Permiten enlazar varias instancias. Un ejemplo es la asignación de varias categorías a una sola entrada.

#### Personalizar el ADMIN (2)

En el script *admin.py* de la app se puede modificar las columnas que se desean mostrar en el admin

list_display = (*args,)

También se pueden ordenar las entradas por uno o varios campos

ordering = (*args,)

Se puede mostrar un formulario de búsqueda

search_fields = (args*,)

Para poder buscar por autor, al hacer parte de un modelo relacional foreign key

search_fields = ('author__username',)

Para poder buscar por categorías, al hacer parte de un modelo relacional many to many

search_fields = ('categories__name',)

Se puede usar una gerarquía de fechas para modelos con campos DateTime

date_hierarchy = *arg

Finalmente se puede crear una lista de campos con los que se desea filtrar, normalmente son relaciones

list_filter = (*args,)

Para mostrar los elementos relacionados en campos many to many se crea un método dentro de la clase

### Procesadores de contexto

Se utilizan para recuperar los enlaces de las páginas web, se entiende como contexto un diccionario común que contiene información que puede extenderse a todos los templates y así no enviar esta información desde la vista

Si se tiene creado un diccionario y se desea que este extienda el proceso global, en el script *settings.py* la variable **TEMPLATES** contiene una clave llamada *OPTIONS* y dentro de los procesadores de contexto se añade dicho diccionario

### Template tags propios

Muestra un contenido personalizado. Es una herramienta más flexible al procesador de contexto, pero consume más recursos porque se debe ejecutar el template tag en cada template, en comparación co el procesdor de contexto que ya está inyectado en todos los templates

#### Creación del template tag

Se crea dentro de la app un directorio llamado **templatetags**, dentro de este se indica que es un package creando el script *__init__.py*. Segidamente se crea un segundo fichero y se registra dentro de la librería de templates escribiendo **from django import template**, y también se importa el modelo que se va a utilizar. Se crea un función para recuperar el contenido y lo devuelva al template en forma de template tag, este template tag debe registrarse en la librería de templates, se crea una variable donde se hace referencia a la librería **template.Library()** y se añade un decorador a la función del template tag **@'variable'.simple_tag**. Finalmente se modifica el template donde se quiera usar

### Orden manual de los modelos

Orden manual de las páginas secundarias, en el modelo que se quiere ordenar, se agrega un nuevo campo de tipo **SmallIntegerField**, luego se cambia la variable **ordering** dándole prioridad al campo que se acaba de crear. Luego de esto se agrega una variable en el admin que permita visualizar los campos de ordenamiento

### Edición directa de un modelo

Destecta el tipo de usuario y habilita un botón en el front que lo lleva a la edición de la página. Para conocer el tipo de usuario, este se guarda en el contexto ubicado en el script *settings.py* **django.contrib.auth.context_processors.auth** lo que permite que se pueda visualizar desde cualquier template

### Personalizar el ADMIN (3)

Añadir un editor de texto wysiwyg (what you see is what you get), en este caso el *ckeditor*, para esto se debe tener instalada la librería **django-ckeditor**, luego se añade a las apps instaladas en *settings.py* y se modifica el modelo donde se quiera agregar

Para establecer una configuración personalizada básica se debe redefinir su diccionario de configuración en *settings.py*. Se crea un diccionario **CKEDITOR_CONFIGS** y dentro de la clade **defautlt** se pueden cambiar parámetros como

* 'toolbar': None -> muestra todas las opciones de la barra de herramientas
* 'toolbar': 'Basic' -> muestra un diseño simple con negritas y cursivas

Para que django interprete los cambios que se realizan en el texto, se cambia el template donde se use la variable de contenido del modelo

### Formularios

Se crean en un script *forms.py* dentro de la app, allí se importa la librería **forms** y se declara una clase con los campos necesarios para el modelo

#### Enviar formulario por correo

Para hacer pruebas se puede hacer con **Mailtrap.io** y copiar la configuración en *settings.py*

### Personalizar el ADMIN (4)

Modificando los permisos de los usuarios, se crea un grupo en el admin y se les da los permisos, cada modelo tiene 4 permisos añadir, cambiar, borrar y ver. También puede ser necesario que algunos campos sean de solo lectura, esto se hace en el script *admin.py* de la app

### Vistas basadas en clases

**FBV** (vistas basadas en funciones)

**CBV** (vistas basadas en clases)

Las CBV:

* Sirven como moldes

* Contienen atributos y métodos

* Permiten el uso de herencia

Los tipos de vistas blasadas en clases se dividen en grupos 

* **autenticación:** LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView

* **genéricas de detalles:** DetailView
 
* **genéricas de edición:** CreatedView, DeleteView, FormView, UpdateView

* **genéricas de base:** RedirectView, TemplateView, View

* **genéricas de listas:** ListView

* **genéricas de fechas:** ArchiveIndexView, DateDetailView, DayArchiveView, MonthArchiveView, TodayArchiveView, WeekArchiveView, YearArchiveView

Estas vistas se deben llamar de manera diferente en el script *urls.py*. Dentro de la clase creada en las vistas, se puede sobreescribir el diccionario de contexto por si se desea enviar información

#### Vistas CRUD (Create, Read, Update, Delete) con CBV

Se le da al ususario la opción de administrar las páginas a través de un menú que solamente les aparece a ellos.

Para la creación de páginas se utiliza una vista basada en clases llamada **CreateView**. Para editar una página, se utiliza la CBV **UpdateView** y para eliminar una página se usa la CBV **DeleteView**

#### Personalizar el formulario de las CBV

Se crea en la app un nuevo script *forms.py* y se crea la clase del formulario con las características necesarias. En este se pueden añadir widgets con configuraciones avanzadas

### Mixin de identificación

Se añade un acceso privado para que las vistas no sean públicas y solamente las personas con permisos puedan crear, modificar o borrar. Para realizar esto se crea una clase que sobreescribe un método llamado **dispatch**

### Decoradores de identificación

Existen con el fin de evitar crear un mixin cada que se requiera que el usuario deba identificarse agregándolo a las vistas basadas en clase que se requiera que el usuario se identifique

### Configurar un servidor SMTP para pruebas

En este caso se usa para la recuperación de la contraseña a través del correo electrónico del usuario

### Señales

Disparador que se llama automáticamente después de un evento que ocurre en el ORM (modelo). Esta se crea en el script *models.py*

### Pruebas unitarias

Se encargan de automatizar un procedimiento, gestionadas es una base de datos aparte y una vez finalizada, no queda rastro de los cambios.

Para crear una prueba, se hace en el script *test.py* cargando los modelos que se van a utilizar

Para ejecutarlo:

python manage.py test **nombre_app**

### Paginación

Permite dividir los registros en distintas páginas

### Principio de las 5 W

* **Who:** quién hará uso de la funcionalidad?

* **What:** qué hará la funcionalidadr

* **When:** cuándo?

* **Where:** dónde?

* **Why:** por qué?

#### Thread (hilo de conversación) - Modelo

Lugar donde ocurre la conversación, punto de encuentro deonde se almacenan los mensajes, por lo tanto no se necesita un receptor, este será el propio hilo que contendrá el mensaje

### TTD (Test Driven Development o Desarrollo Guiado por Pruebas)

Para llevarlo a cabo se usan 4 fases

1. Escribir el Test y hacer que falle

2. Escribir la mínim cantidad de código para que el test pase

3. Escribir un nuevo test y hacer que falle

4. Escribir el algoritmo necesario para hacer pasar el test

* Por facilidad lo que se hace en este proyecto es pasar del punto **1** al punto **4** directamente

Para llevar a cabo una prueba, se escribe en la terminal

python manage.py test **Nombre_app**

Para hacer un test de un entorno en particular

python manage.py test **Nombre_app**.test.**Nombre_clase**

Para hacer un test singular en particular

python manage.py test **Nombre_app**.test.**Nombre_clase**.**Nombre_test**

### Peticiones asíncronas

Cuando un proceso es síncrono, el usuario queda en un limbo (lo que tarde en responder el servidor) esperando una respuesta. Al hacer la petición de forma asíncrona, la página sigue funcionando, o sea que la peticióm se maneja en segundo plano. Estas peticiones asíncronas no requieren recargar toda la página, simplemente una sección determinada.

Se utiliza js para crear un objeto en la memoria donde se maneja la petición, se captura la respuesta y se modifica el DOM (Document Object Model) lo que permite cambiar la estructura de un HTML en tiempo real


## DESPLIEGUE (webempresa)

### Entornos

Lo **entornos de ejecución** son una configuración que envuelve la ejecución del software, los entornos más comunes son de *desarrollo*, *producción* y *pruebas*

* *Entorno de desarrollo:* donde los programadores crean las aplicaciones ayudándose de configuraciones específicas

* *Entorno de producción:* está dirigido al usuario final, el lugar donde corre el código una vez está funcionando públicamente

El proceso de cambiar el código de un entorno a otro se conoce como **fase de despliegue** y contiene la instalación, configuración y unas pruebas mínimas de funcionamiento

### Aplicaciones que permiten realizar despliegues en la nube

* Heroku
* Amazon Web Service
* VPS (Servidor Virtual Privado)
* *Pythonanywhere*

### Proceso en pythonanywhere

#### 1. Crear un entorno virtual para el despliegue

Consolas -> bash:

--> Crear entorno virtual *mkviertualenv --python=python3.7 **Nombre***

--> Clonar el repositorio *git clone **url***

--> Instalar dependencias *pip install -r requirements.txt*

--> Comprobar configuraciones a optimizar para realizar el despliegue *python3.7 manage.py check --deploy*

#### 2. Modificar las configuraciones

Se debe cambiar el DEBUG a False

Agregar los servidores o dominos que tienen permitido acceder en la variable ALLOWED_HOST (ejm. 'tavo826.pythonanywhere.com/', 'localhost', '127.0.0.1')

La base de datos subida al repositorio, por ser SQLite, se gestiona con un fichero individual, por lo que es una copia

#### 3. Crear una app para mantener el servicio de django en marcha

Web -> add a new web app -> configuración manual -> python3.7

#### 4. Configurar el source code de la web app

**pwd** en el bash: */home/Tavo826/webempresa*

#### 5. Configurar el entorno virtual

**which python** en el bash: */home/Tavo826/.virtualenvs/Des*

#### 6. Configurar el archivo WSGI

Se borra el contenido y el nuevo código se encuentra en el manual de pythonanywhere

mysite <=> *Tavo826/webempresa*

mysite.settings <=> *webempresa.settings*

#### 7. Configurar los archivos estáticos

Static files:

**URL 1:** */static/*   **Path1:** */home/Tavo826/webempresa/static/*
**URL 2:** */media/*    **Path2:** */home/Tavo826/webempresa/media/*

El directorio static se gestiona añadiendo bajo la variable **STATIC_URL**, *STATIC_ROOT = os.path.join(BASE_DIR, 'static')*

Luego en el bash se escribe el comando *python3.7 manage.py collectstatic*

#### 8. Configurar una cuenta de correo electrónico para que funcione el envío de contacto

### Personalizar el ADMIN (5)

Cambiando los títulos del panel y agregando un logo:

En el fichero *urls.py* de la app se modifican los títulos

Para agregar un logo, se deben modificar los templates del panel del administrador, estos estarán en la carpeta templates de la raíz y se agrega en *settings.py* en la variable **TEMPLATES** en la clave **DIRS** este directorio

Los templates del panel de aministrador se encuentran en el entorno virtual *Lib -> site-packages -> django -> contrib -> admin -> templates -> admin*

La imagen se guarda en la carpeta static de la raíz y se configura *settings.py* bajo la variable **STATIC_URL**