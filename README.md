<h1 align="center">
  <br>
  <a href=# name="readme-top">Proyecto Planner</a>
</h1>

<p align="center">
  <a href="#descripción">Descripción</a> •
  <a href="#instalación-y-desarrollo">Instalación</a> •
  <a href="#mocks">Mocks</a> •
  <a href="#deployment">Deployment</a> •
  <a href="#equipo">Equipo</a> •
  <a href="contributors.md">Contribuidores</a> •
  <a href="#licencia">Licencia</a>
</p>

<h4 align="center">
  <a href=# name="readme-top"><img src="./docs/img/demo_gif.gif" width="700px" alt="banner"></a>
</Es>

[![All Contributors](https://img.shields.io/github/all-contributors/open-source-uc/planner?color=ee8449&style=flat-square)](#contributors)

---

## Descripción

Este es el hogar para el desarrollo del nuevo Planner de Ingeniería UC, hecho por estudiantes para estudiantes.

Tras varios años en ideación, este proyecto se lanzó como [una propuesta conjunta](https://drive.google.com/file/d/1IxAJ8cCzDkayPwnju5kgc2oKc7g9fvwf/view) entre la Consejería Académica de Ingeniería y Open Source UC, con el propósito de reemplazar el [actual planner de Ingeniería](https://planner.ing.puc.cl/). La propuesta, tras ser aprobada por la Escuela de Ingeniería, dió comienzo al proyecto en modalidad de marcha blanca. A principios del 2023, y con un MVP listo, la Dirección de Pregrado oficialmente aprobó la continuación del desarrollo del proyecto.

## ¿Cómo agregar funcionalidades o modificar Mallas ING?

1. **Hacer un fork** de este repositorio.
2. Realizar los cambios en tu repo forkeado, trabajando en la rama `dev`.
3. **Crear un Pull Request (PR)** desde la rama `dev` de tu repo hacia la rama `dev` de este repo.
4. Esperar a que el equipo del Nuevo Planner + OSUC acepte tu solicitud.
5. Una vez aceptado, el equipo del Nuevo Planner + OSUC abre un **PR** desde `dev` hacia `main` en este mismo repositorio.
6. Luego, el equipo del Nuevo Planner + OSUC podrá hacer un **PR** desde `main` hacia `main` del repositorio controlado por la universidad: [spavea/mallas.ing.uc.cl](https://github.com/spavea/mallas.ing.uc.cl).
7. Finalmente, solo queda esperar a que la universidad apruebe los cambios. El deploy se hará automáticamente al recibir la aprobación 🚀

## Instalación y desarrollo

El proyecto está configurado para ser desarrollado en [Visual Studio Code](https://code.visualstudio.com/) con [Dev Containers](https://code.visualstudio.com/docs/remote/containers). Puedes [instalar VSCode aquí](https://code.visualstudio.com/download). Existen 2 maneras de correr Dev Containers: GitHub Codespaces y localmente.

#### Desarrollo en GitHub Codespaces

Codespaces es un servicio de GitHub que permite correr VSCode en la nube.
Provee una cantidad limitada de horas de uso, que puede ser [expandida activando la cuenta Pro gratis a estudiantes](https://education.github.com/discount_requests/application).

- Instala la extensión de [GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces).
- Crea o abre un Codespace desde el botón en la esquina superior derecha de este repositorio (o desde el menú de VSCode). Si no lo has creado, ingresa `open-source-uc/planner` como el repositorio a abrir.

Sigue en la sección [Desarrollo general](#desarrollo-general).

- Una vez terminado de desarrollar, [detén el Codespace](https://docs.github.com/es/codespaces/developing-in-codespaces/stopping-and-starting-a-codespace) para no consumir horas de uso. También puedes usar un [timeout para que se detenga automáticamente](https://docs.github.com/es/codespaces/customizing-your-codespace/setting-your-timeout-period-for-github-codespaces).

### Desarrollo local

- Instala [Docker](https://www.docker.com/). Asegurate que esté corriendo.
- Instala la extensión [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
- Clona este repositorio y abre el proyecto en VSCode.
- Corre el comando `Dev Containers: Open Folder in Container` o has click en el popup que saldrá al abrir el proyecto.

Sigue en la sección [Desarrollo general](#desarrollo-general).

### Desarrollo general

- El Dev Container correrá automaticamente el setup necesario con `just init`. Espera que termine para continuar.
- Utiliza `Run and Debug` de VSCode con `Launch all 🚀` para correr todos los servicios al mismo tiempo. Espera que el backend (que puedes inspeccionar en `Python Debug Console`) termine de correr para continuar (cuando se muestre _"Application startup complete"_).

Una vez listo, podrás entrar a la app en [http://localhost:3000](http://localhost:3000) 🎉

Necesitaras un nombre de usuario para acceder a CAS. Puedes acceder con `testuser` o con otros usuarios definidos en `cas-mock-users.json`.

Para realizar acciones sobre el repositorio (migraciones, generación de código, etc) puedes usar:

- el task runner de VSCode (<kbd>Ctrl/Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> -> _"Tasks: Run Task"_).
- `just` en la linea de comandos. Para ver comandos disponibles, corre `just` desde cualquier carpeta.

Es importante que cuando:

- Cambias la estructura de la API, corras la tarea _"Generate client"_ (también disponible en modo watch).
- Cambies el esquema de la base de datos, corras la tarea _"Create/apply migrations"_ para que los cambios se reflejen en la base de datos.

Para realizar contribuciones, revisa [contributing.md](contributing.md).

### Bug Reports & Feature Requests

> **Nota:** Este proyecto usa [Linear](https://linear.app/) para rastrear el progreso del proyecto. Por ahora, el Linear no es público, pero de todas formas se revisan los issues y features creados en GitHub.

La app aún está en una etapa muy temprana del desarrollo por lo que podrían haber cosas que no funcionan correctamente o difieren de la documentación, por lo que cualquier lector siéntase libre a colaborar :rocket:. Toda ayuda es bienvenida :)

## Mocks

El proyecto se integra con dos servicios externos: SIDING (para acceder a mallas y datos de estudiantes) y CAS (para el login UC). Ambos son configurables por medio de variables de entorno, y se proveen mocks para ambos servicios en caso de no tener credenciales para acceder a ellos.

- Para SIDING se provee un mock que se activa automáticamente en ausencia de credenciales. El mock es limitado, y solo permite probar algunas combinaciones de malla.
- Para CAS, se provee el servicio `cas-server-mock` que corre automáticamente junto a la app. Las cuentas de usuario disponibles son configurables en el archivo `cas-mock/data/cas-mock-users.json`.

## Deployment

### Deployment automático

Para deployments a producción, se provee un playbook de [Ansible](https://docs.ansible.com/ansible/latest/index.html)
que permite levantar la app completa de principio a fin, pensado para su uso en un entorno de producción, en particular
en un servidor corriendo [Rocky Linux 9](https://rockylinux.org/).

Teniendo acceso SSH a un servidor, solo se necesita correr (desde un entorno de desarrollo ya configurado):

```shell
$ ansible-playbook infra/playbook.yml -i <IP>, -u <USUARIO>
```

Asumiendo que ya se tenga una llave SSH al servidor. El playbook es completamente idempotente, por lo que
también puede ser utilizado para corregir configuration drift en un servidor de producción.

El playbook opcionalmente provee prompts para entregar credenciales de Tailscale, Netdata y SIDING. Por defecto
el playbook no levanta un mock de CAS, que es necesario para instalaciones sin acceso al SSO UC.

También se provee un script más ligero en [just](./justfile), que principalmente está pensado para su uso en
junto al sistema de [Continuous Deployment](./.github/workflows/deploy.yml) del repositorio. Sin embargo,
dado un entorno ya configurado de Docker Compose, este puede ser utilizado para levantar un servidor independiente,
incluyendo uno que utilice un SSO mock.

Abajo se entregan instrucciones manuales de deploy.

### Deployment manual: Staging

El ambiente de staging está diseñado para testear las nuevas versiones del planner en un ambiente real antes de pasar a producción.

En primer lugar, es necesario generar manualmente los archivos `.env` y reemplazar los valores según corresponda para cada servicio utilizando los ejemplos ubicados en cada carpeta:

- _API_ → `backend/.env.staging.template`
- _servidor web_ → `frontend/.env.staging.template`
- _base de datos_ → `database/.env.staging.template`

Luego, se debe crear el volumen de Caddy con `docker volume create caddy_data`.

Ahora, para correr la aplicación utilizando un servidor mock de **CAS externo** se debe:

1. Definir las variables `CAS_SERVER_URL` y `CAS_LOGIN_REDIRECTION_URL` en `backend/.env` con la URL del servidor externo.
2. Levantar los contenedores con `docker compose up planner -d --build` desde la raíz del repositorio.

Alternativamente, para correr la aplicación utilizando un servidor mock de **CAS local**:

1. Dejar las variables `CAS_SERVER_URL` y `CAS_LOGIN_REDIRECTION_URL` en `backend/.env` con los valores predeterminados del archivo de ejemplo `.env.staging.template`.
2. Luego, es necesario generar el archivo `cas-mock-users.json` en `cas-mock/data` a partir del ejemplo `cas-mock-users.json.example`.
3. Levantar los contenedores con `docker compose up -d --build` desde la raíz del repositorio.

Finalmente, se puede detener la app con `docker compose down` desde la raíz del repositorio.

### Deployment manual: Producción

El ambiente de producción es manejado por la universidad de forma interna, por lo que aquí se detallan las **instrucciones para desplegar el planner** de forma manual:

1. Se debe crear el archivo `.env` para la API. En particular, crear `backend/.env` a partir del ejemplo `backend/.env.production.template`.

2. Reemplazar los valores de las variables de entorno según corresponda en todos los archivos `.env` creados. **IMPORTANTE:** no olvidar modificar la variable `JWT_SECRET` en `backend/.env` y otras variables que puedan contener secretos para evitar vulnerabilidades de seguridad.

- Para generar una clave `JWT_SECRET` segura y aleatoria se puede utilizar el comando `openssl rand -base64 32`.

3. Se debe crear el volumen donde Caddy guardará los certificados SSL con `docker volume create caddy_data`.
4. Levantar los contenedores con `docker compose up planner -d --build` desde la raíz del repositorio. Requiere _Docker_ y _Docker Compose_ instalados en la máquina.
5. Revisar el estado de los contenedores con `docker ps` o `docker container ls`.
6. Finalmente, se puede detener la app con `docker compose down` desde la misma ubicación.

Nota: los comandos podrían variar ligeramente dependiendo del sistema operativo y versión de _Docker Compose_. En particular, podría ser necesario utilizar `docker-compose` en vez de `docker compose` y `sudo docker compose` en vez de `docker compose`.

---

## Equipo

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="20%"><a href="https://github.com/shantifabri"><img src="https://avatars.githubusercontent.com/u/37163566?v=4" width="175px;" alt="Shantal Fabri"/><br /><sub><b>Shantal Fabri</b></sub></a><br /><a href="#" title="Coordinación">📋</a><a href="https://github.com/open-source-uc/planner/commits?author=shantifabri" title="Frontend">💻</a></td>
      <td align="center" valign="top" width="20%"><a href="https://github.com/Diegothx"><img src="https://avatars.githubusercontent.com/u/37160496?v=4" width="175px;" alt="Diego Prudencio"/><br /><sub><b>Diego Prudencio</b></sub></a><br /><a href="https://github.com/open-source-uc/planner/commits?author=Diegothx" title="Frontend">💻</a></td>
      <td align="center" valign="top" width="20%"><a href="https://github.com/kovaxis"><img src="https://avatars.githubusercontent.com/u/7827085?v=4" width="175px;" alt="Martín Andrighetti"/><br /><sub><b>Martín Andrighetti</b></sub></a><br /><a href="https://github.com/open-source-uc/planner/commits?author=kovaxis" title="Backend">⚙️</a></td>
      <td align="center" valign="top" width="20%"><a href="https://github.com/fagiannoni"><img src="https://avatars.githubusercontent.com/u/27508976?v=4" width="175px;" alt="Franco Giannoni Humud "/><br /><sub><b>Franco Giannoni Humud</b></sub></a><br /><a href="https://github.com/open-source-uc/planner/commits?author=fagiannoni" title="Backend">⚙️</a> </td>
      <td align="center" valign="top" width="20%"><a href="https://github.com/agucova"><img src="https://avatars.githubusercontent.com/u/4694408?v=4" width="175px;" alt="Agustín Covarrubias"/><br /><sub><b>Agustín Covarrubias</b></sub></a><br /><a href="https://github.com/open-source-uc/planner/commits?author=agucova" title="Apoyo Frontend">💻</a> <a href="https://github.com/open-source-uc/planner/commits?author=agucova" title="Apoyo Backend">⚙️</a></td>
    </tr>
  </tbody>
</table>

Además del equipo núcleo, nos apoyan los contribuidores al proyecto. Puedes ver [la lista completa de contribuidores aquí.](contributors.md)

## Licencia

[![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](./license.md)

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>
