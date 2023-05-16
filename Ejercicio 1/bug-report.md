# Prueba exploratoria y reporte de bugs

## Prueba exploratoria

Se realizó una prueba exploratoria en el sitio [Wordpress Codex](https://codex.wordpress.org/) manual en línea y repositorio para la documentación de Wordpress, a saber:

> "Welcome to the WordPress Codex, the online manual for WordPress and a living repository for WordPress information and documentation."

Existen múltiples enlaces, por cada uno de sus apartados, que contienen referencia a documentación obsoleta. Algunos de estos casos pueden ser, entre otros:

- What You Most Need to Know About WordPress
    - [WordPress Features](https://codex.wordpress.org/WordPress_Features)
- Working With Themes
    - [Child Themes](https://codex.wordpress.org/Child_Themes)

Considerando el primer ejemplo, puede observarse la siguiente leyenda:

> "This page was moved to [https://wordpress.org/support/article/wordpress-features/](https://wordpress.org/support/article/wordpress-features/) except above language locator."

Lo cual repercute en disponibilizar al usuario, un contenido desactualizado, cuya referencia debe ser actualizada y corregida.

## Reporte de bug

Se detalla la siguiente información del bug detectado:

| Tipo | Descripción |
| --- | ----------- |
| ID | WP-001 |
| Tipo | Caja negra |
| Descripción | Enlaces desactualizados en la documentación de Wordpress Codex |
| Pasos | 1. Ingresar a [codex.wordpress.org](https://codex.wordpress.org/) |
|  		| 2. Visualizar la sección "What You Most Need to Know About WordPress" | 
|		| 3. Hacer click en [WordPress Features](https://codex.wordpress.org/WordPress_Features) |
| Resultado obtenido | Se visualiza el contenido de [codex.wordpress.org/WordPress_Features](https://codex.wordpress.org/WordPress_Features) |
| Resultado esperado | Se visualiza el contenido de [wordpress.org/about/features](https://wordpress.org/about/features/) |
| Prioridad | Baja |
| Impacto | Alto |
| Probabilidad de ocurrencia | Alta |

> **Nota:** Este bug sucede para múltiples artículos y se utiliza el detallado en el bug como referencia del caso.

## Anexo técnico

El ingreso a cada uno de los enlaces retorna un código de estado HTTP igual a 200 (OK).

```shell
$ curl -I https://codex.wordpress.org/WordPress_Features

HTTP/2 200 
server: nginx
date: Tue, 16 May 2023 15:52:11 GMT
content-type: text/html; charset=UTF-8
vary: Accept-Encoding
x-content-type-options: nosniff
vary: Accept-Encoding, Cookie
expires: Thu, 01 Jan 1970 00:00:00 GMT
cache-control: private, must-revalidate, max-age=0
last-modified: Sat, 25 Mar 2023 13:25:13 GMT
content-language: en
strict-transport-security: max-age=31536000
```

Sería el comportamiento deseado que retorne un código de estado HTTP igual a 301 (Moved Permanently) que incluya una redirección desde el [contenido obsoleto](https://codex.wordpress.org/WordPress_Features) hacia el [contenido nuevo](https://wordpress.org/about/features/).

Para más información respecto a los códigos de estados HTTP [200](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) o [301](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/301) se sugieren los enlaces detallados.

Según Google existen 1,140 resultados que no sólo no deben estar indexados sino que su redirección debe estar implementada a fin de solucionar el fallo reportado. Para reproducir tal comportamiento sólo basta con ingresar `site:codex.wordpress.org This page was moved` en [Google](https://www.google.com/) o bien hacer uso de este [enlace](https://google.com/search?q=site%3Acodex.wordpress.org+This+page+was+moved). A continuación se detallan de forma ilustrativa algunos resultados de la búsqueda:

```text
Moving WordPress - WordPress Codex

wordpress.org
https://codex.wordpress.org › Moving_WordPress
This page was moved to https://wordpress.org/support/article/moving-wordpress/ except above language locator.

Users Screen - WordPress Codex

wordpress.org
https://codex.wordpress.org › Users_Screen
This page was moved to https://wordpress.org/support/article/users-screen/ except above language locator.

Talk:Using Themes - WordPress Codex

wordpress.org
https://codex.wordpress.org › Talk:Using_Themes
Note: When moving pages, the talk pages have to be moved too. Talk:Themes still exists, so that history is lost, or at least not easily available to someone ...
```