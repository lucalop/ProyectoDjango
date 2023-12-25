# El presente proyecto corresponde a la entrega final del curso de Python|Coderhouse
## Requisitos del proyecto:

Crear web similar a un blog
✓ Contar con algún acceso visible a la vista de "Acerca de mí" donde se contará acerca de los dueños de la página manejado en el route about/. 
✓ Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/. 
✓ Acceder a una pantalla que contendrá las páginas. Al clickear en “Leer más” debe navegar al
detalle de la page mediante un route pages/<pageId>. 
✓Si no existe ninguna página mostrar un "No hay páginas aún"
✓Para crear, editar o borrar las fotos debes estar registrado como Administrador.
✓Cada blog, es decir cada model Blog debe tener como mínimo, un título, subtítulo, cuerpo, autor, fecha y una imagen
✓Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario.
✓Tener una app de login en el route accounts/login/ la cual permite loguearse con los datos de administrador o de usuario normal.
✓Tener una app de perfiles en el route accounts/profile/ la cual muestra la info de nuestro usuario y permite poder modificar y/o borrar: imagen - nombre - descripción - un link a una página web - email y contraseña
✓Contar con un admin en route admin/ donde se puedan manejar las apps y los datos en las apps.
✓Tener una app de mensajería en el route messages/ para que los perfiles se puedan contactar
entre sí.

# Video y Casos de prueba

Link a Video: https://www.youtube.com/watch?v=HqUfDiEu9C0
Link a casos e prueba: https://docs.google.com/spreadsheets/d/1xTkx235--tglDGJ07VEJC1pKYRtL6Bwx/edit#gid=268081881

# Prerequisitos
Instalar Python (Idealmente V3.11)
Instalar Django

# Pasos para clonar el proyecto:
- Dirigirse a la carpeta local en la cual se desea clonar el proyecto
- Abrir terminal y escribir el comando "git clone https://github.com/lucalop/ProyectoDjango.git"


# Pasos para correr el proyecto
Abrir terminal y escribir los siguientes comandos en orden: 
- python manage.py makemigrations
- python manage.py migrate
- Python3 manage.py createsuperuser 
- Escribir username y pass. El usuario quie se creará será administrador
- python manage.py runserver     

Para poder hacer uso de la app dirigirse a 

http://127.0.0.1:8000/accounts/login/

# Funcionalidades

## Login y Signup
- Al ingresar a la app solicitará que el usuario se loguee o se registre. 
- Registro: La app solicita nombre de usuario, email y password. Si alguno de los campos no es llenado correctamente devuelve un mensaje de error en rojo
- En el nav pueden apreciarse los siguiente botones
    - Trekkings:
        - El botón crear trekking solicitará: Title, City, Content, Author, Avatar trekking, date. 
        Luego de completar los campos presionar el botón "Create treking"
        - Al retornar al listado de Trekings, se puede observar el trekking creado. Existen dos filtros que permiten distinguir por título op or ciudad. El boton Clean filter, remueve los filtros.
        - El botón details permite visualizar el detalle del Treking
        - Dentro del detalle existe la opción de "Comentar". Al comentar se guarda el nombre de usuario y fecha además del mensaje escrito.
    - About me: Redirecciona a la parte baja de la landing. Contiene información sobre mi.
    - My account: Al ingresar a esta sección se puede apreciar el Mail, username y avatar. Para cargar un Avatar existe el botón "Edit Avatar" y en caso de querer cambiarlo, puede hacer click nuevamente para cambiarlo. Existe también la posibilidad de editar el usuario. Al hacer click permite editar el mail y last name del usuario
    - Logout: Opción para desloguearse





