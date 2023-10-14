# Demostracion dagger

Este es un proyecto para experimentar con Dagger, sobre todo su area de CI, y comparar su performance al implementar lo mismo pero unicamente con Github Actions

2023-10-13 21:23 -> Implemente un workflow simple para correr pruebas unitarias con python. Me llevo 7 commits el tenerlo listo, la ejecucion en total suma + 168 segundos. Notese que busque el feedback temprano haciendo cambios pequeños, pero no optimos; si hubiese utilizado herramientas para cachear la preparacion del entorno probablemente se reduzca el tiempo de ejecucion. Lo cacheable en este caso es la preparacion del runner con las dependencias requeridas (en este caso python y pytest) y una posible solucion seria crear una imagen de docker con esto ya resuelto. Los errores que enfrente fueron: 
1. Formato yaml: Al no usarlo usualmente, tengo mas probabilidades de errores.
2. Problema de nombre de directorio: Al hacer "checkout" del commit entrante, se introdujo el nombre local de la carpeta raiz del proyecto, el cual diferia con la esperada por pytest dentro del runner.
Soluciones:
1. Minimizar el uso de yaml en el proceso de ci
2. Unificar los nombres, o hacer "checkout" unicamente del contenido del root entrante (./*)
