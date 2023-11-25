# Backend Docker Python

## 1. Instalación

Para descargar la aplicación del repo, se debe escribir el siguiente comando:

```
$ git clone https://github.com/FragmentosTemporales/backend-docker-python.git
```

### Variables de entorno

Al interior de la carpeta /Sripts debes crear un documento env.env el cual debe contener las siguiente variables, puedes guiarte con el documento example.env :

```
FIRST_NAME=
LAST_NAME=
API_KEY=
```
*_no te compliques y prueba con algo muy simple_*

### Instalación de Docker Compose

Para instalar la aplicación debes ejecutar el siguiente código:

```
$ docker compose build
```
*_recuerda mantener abierto docker en tu computador!!_*


## 2. Ejecución

Para ejecutar la aplicación debes ingresar el siguiente comando:

```
$ docker compose run --rm scripts sh -c "python manage.py"
```
*_esto ejecutará las funciones definidas en el documento manage.py_*

```
$ docker compose run --rm scripts sh -c "python app.py"
```
*_esto ejecutará las funciones definidas en el documento manage.py_*

## 3.- Bibliografía

```
null
```
