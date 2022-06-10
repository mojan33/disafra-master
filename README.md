# README.md

## Español

## CREAR UN FORK:

1. En la parte derecha superior de este repositorio aparece un botón llamado **fork**, por favor hacer clic para generar tu propia
 versión de este repositorio en tu cuenta.

## CONFIGURAR MI GIT:

1. Se debe instalar GIT según el sistema Windows, MacOs o Linux.
```
https://git-scm.com/downloads
```
2. Una vez instalado hay que ingresar a la consola que se prefiera.
3. Para configurar nombre y correo se escribe los siguientes comandos:
```
git config --global user.name "Mi Nombre"
git config --global user.email "Mi correo"
```

## CREAR MI REPOSITORIO LOCAL CON GIT:

1. Entrar a la consola y ubicarnos en la ruta donde clonaremos nuestro repositorio.
2. Escribir el siguiente comando para clonar el repositorio:

```
git clone https://github.com/miCuenta/miCopia
```
3. Comenzar a programar, o agregar documentos.

## CONFIGURAR MI FORK

1. Revisaremos el URL remoto de nuestro repositorio con:

```
git remote -v
```

2. Se cambiara el nombre de nuestro git remoto a fork con el siguiente comando:

```
git remote rename origin fork
git remote -v
```

3. Se agregará el URL remoto del repositorio original, para eso se colocará el siguiente comando:

```
git remote add origin https://github.com/amner-py/disafra.git
git remote -v
```

## CREAR MI PROPIA RAMA/BRANCH LOCAL:	\*Es necesario crear una rama para evitar errores en el repositorio principal\*

1. Con la consola dentro de la carpeta del repositorio existen diferentes maneras de crear nuestra rama/branch:

\*Es necesario reemplazar miRama por su nombre, ejemplo: git branch juan \*

```
git branch miRama
git checkout miRama
```

o

```
git checkout -b miRama
```

## UNIENDO MIS RAMAS A LA MASTER:

1. En consola escribimos los siguientes comandos:

```
git checkout master
git merge miRama
```

o

```
git merge master miRama
```

## SUBIR LOS CAMBIOS QUE REALICE A GITHUB

1. En la consola escribir el siguiente comando:

```
git push fork miRama
```

## HACER PULL REQUEST

1. Entrar a github
2. Entrar al repositorio copia que nos creo dentro de nuestra copia llamada disafra deberia salir así: miUsuario/disafra
3. Dar clic en branches
4. Dar clic en el botón: **New pull request**
5. Observar que en en base fork se muestre:

**base fork: amner-py/disafra	base: master	head fork: miUsuario/disafra	compare: miRama**

6. Se escribe un mensaje o comentario de lo que se realizó o una previa de qué se agregará.
7. Clic en **Create pull request**

## PRIMEROS PASOS CON EL SISTEMA

## INSTALANDO Y UTILIZANDO MYSQL

1. Instalar MySQL Workbench
2. Crear una conexión en workbench de no tener una.
3. Crear un usuario llamado: **admin**
4. Colocarle de contraseña: **admin123**
5. Abrir el documento **disafra.sql** en Workbench.
6. Correr el archivo.

## INSTALANDO REQUERIMIENTOS PARA EL PROYECTO

1. Entrar a la consola de preferencia
2. Ubicarse en el repositorio clonado
3. Desde consola ingresar los comandos para activar el entorno virtual python:

```
python -m venv env-win
```

Activar el entorno virual en windows

```
cd env-win/Scripts/
activate
```

de tener SO linux crear un entorno virtual de la siguiente manera en la ruta **DISAFRA/**:

```
python -m venv env-lin
```

activar el entorno de la siguiente manera:

```
source env-lin/bin/activate
```

Salir de la carpeta de entorno a la ruta principal

```
cd ..
cd ..
```

4. Una vez encendido el entorno virtual de python instalar los requerimientos con el comando:

```
pip install -r requirements.txt
```

5. Ingresar a la carpeta **app** con el siguiente comando

```
cd app
```

6. Crear migración necesaria para el admin de django:

```
python manage.py migrate
```

7. Crear un super usuario para ingresar al admin:

```
python manage.py createsuperuser
```

8. Corre el servidor local de Django:

```
python manage.py runserver
```