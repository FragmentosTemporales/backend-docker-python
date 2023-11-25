# Docker Python

## 1. Instalación

Para descargar la aplicación del repo, se debe escribir el siguiente comando:

```
https://github.com/FragmentosTemporales/testing-docker-windows.git
```

### Variables de entorno

Al interior de la carpeta /Sripts debes crear un documento env.env el cual debe contener las siguiente variables:

```
null
```

### Instalación de Docker Compose

Para instalar la aplicación debes ejecutar el siguiente código:

```
$ docker compose build
```

## 2. Ejecución

Para ejecutar la aplicación debes ingresar el siguiente comando:

```
$ docker compose run --rm scripts sh -c "python manage.py"
```

### Bibliografía

```
null
```
