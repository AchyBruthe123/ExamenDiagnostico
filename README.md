Nombre del proyecto: Alumnos

Descripción: Una aplicacion sensilla en donde se pueden registrar alumnos, verlos, editarlos y/o eliminarlos

Tecnologías utilizadas: Django junto con Bootstrap, HTML y mysql

Funcionalidades: Se puede agrgar a un alumno y guardar este en la base de datos por mediode un formularios, al momento de crearlo tambien se puede modificar la info de este en el mismo formulario anterior, a la vez que tambien se puede eliminar.

Instrucciones para ejecutar el proyecto:

1.- Tener python instalado junto con las siguientes dependencias
      pip install django
      pip install djangorestframework
      pip install mysqlclient
      pip install Pillow
      pip install django-cors-headers
2.- Crear una base de datos con el nombre de "escuela" (En caso de ser nesesario cambiar las credenciales en Settings.py en el apartado de "DATABASES")
3.- (RECOMENDABLE: Eliminar el archivo de migrations)
4.- realizar el siguiente comando en un CMD que apunte en la carpeta del proyecto "python manage.py migrate"
5.- correr el proyecto con "python manage.py runserver" estando en el CMD anterior
6.- meterte en esta url "http://127.0.0.1:5500/frontend/index.html"

Evidencias o capturas de pantalla.

<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/ae68d75c-9928-40d4-baf2-a828587b353e" />

<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/c1e98411-cd2f-4559-8be2-c0fa3235da1b" />

Indicación de si se usó IA y para qué.

  Creacion de los modelos
  Creacion total del Front
  Creacion de las rutas 
  Creacion de las vistas 
