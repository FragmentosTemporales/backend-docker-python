# Backend Docker Python


## 1. Instalación

Para descargar la aplicación del repo, se debe escribir el siguiente comando:

```
$ git clone https://github.com/FragmentosTemporales/backend-docker-python.git
```


### Instalación de Docker Compose

Para instalar la aplicación debes ejecutar el siguiente código:

```
$ docker compose build
```
*_recuerda mantener abierto docker en tu computador!!_*


### Variables de entorno

Al interior de la carpeta /Sripts debes crear un documento env.env el cual debe contener las siguiente variables, puedes guiarte con el documento example.env :

```
FIRST_NAME=
LAST_NAME=
```
*_no te compliques y prueba con algo muy simple_*



## 2. Ejecución

Para ejecutar la aplicación debes ingresar el siguiente comando:

```
$ docker compose run --rm scripts sh -c "python manage.py"
```
*_esto ejecutará las funciones definidas en el documento manage.py_*


## 3.- ¿Qué estamos ejecutando?

En el documento Manage.py obtenemos las variables de entorno utilizando _os.environ.get()_, con esto generamos un saludo.
Posteriormente ejecutamos la función *create_app()*, la cual es la que, en primera instancia, genera una lista de 100 usuarios utilizando *Faker()*, para luego retornar un mensaje verificando si el usuario creado es mayor de edad o no.

## 4.- Bibliografía

A continuación te dejo la documentación de Faker() en Pypi.org:

```
$ https://pypi.org/project/Faker/
```
