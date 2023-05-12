<h1 align="center"> Documentacion Repositorio</h1>
![logotec](https://github.com/Mariopzb/ejemplo/blob/a2b3a7f55da325d8b358384360116c2801d38b35/tecnologico-de-monterrey-blue.png)
Mario Alberto Pérez Barrera A01799928 

Sandra Paulina Herrera Rebolledo A01798452



Para utilizar el repositorio realizamos lo siguiente:
1. Creamos una cuenta en la plataforma Github.
2. Creamos un repositorio en Github.
3. Para realizar cambios al repositorio ocupamos la consola del sistema, está pudiendo ser como “Windows PowerShell”, “Ubuntu”, “Git Bash” o “Terminal de Mac”. Desde ahí realizamos los commits correspondientes a cada archivo (o cada juego) y para descargar los cambios que hizo la otra persona realizamos un pull. (Este paso es para realizar los cambios de forma forma remota, sin necesidad de entrar a Github, cabe aclarar que no es necesario y se puede realizar directamente de la página, aunque es menos organizado y más tardado).

En cada uno de los archivos está el historial con todos los commits hechos por cada miembro del equipo. 

En el repositorio “Videojuegos”  creamos 5 archivos .py para cada uno de los juegos con el Código de Referencia tomado del sitio Grant Jenk http://www.grantjenks.com/docs/freegames 

Los 5 juegos que fueron modificados fueron:
1. Paint.       http://www.grantjenks.com/docs/freegames/paint.html
2. Snake      http://www.grantjenks.com/docs/freegames/snake.html
3. Pacman   http://www.grantjenks.com/docs/freegames/pacman.html
4. Cannon    http://www.grantjenks.com/docs/freegames/cannon.html
5. Memory   http://www.grantjenks.com/docs/freegames/memory.html

Los requisitos para poder jugar estos juegos, así como realizar modificaciones son:
Tener Python en tu sistema.
Descargar el módulo o biblioteca de “freegames”,  esta biblioteca cuenta con todas las herramientas y clases necesarias para correr cada uno de los juegos.
Se debe de tener un IDE de python como “Visual Studio”, “Jupyter”, “Spyder”, “Thonny” o algún otro.(no es totalmente necesario).
Los juegos pueden ser ejecutados desde el IDE o directamente desde la consola utilizando la función python y el nombre del juego, ejemplo: “python snake.py”

Cada uno de los juegos tuvo distintas modificaciones que nos repartimos y fuimos agregando conforme íbamos terminando. Algunas de las modificaciones fueron:

-Paint: Se añadió un color nuevo que en nuestro caso fue el rosa, se definieron las funciones para dibujar un círculo, rectángulo y triángulo.

-Snake: Cambiamos que la comida se moviera solo un paso a la vez sin salirse del juego; cada partida los colores tanto de la serpiente como la comida cambiarán dentro de un rango de 5 colores distintos, (nosotros seleccionamos azul, naranja, verde, amarillo, rosa), seleccionados al azar pero sin repetirse y sin seleccionar el rojo.

–Pacman: Modificamos para que los fantasmas fueran más “listos”, se cambió el diseño del tablero modificando la matriz y la velocidad en la que se movían los fantasmas. 

-Cannon: Cambiamos la velocidad tanto del proyectil como de los balones para que se movieran más rápido, y que el juego no se terminará reposicionando a los balones pero evitando que no se salieran de los límites del espacio del juego. 

-Memory: Añadimos que el juego contará y mostrará el número de “Taps” (clicks en el mouse o pad), centrar los números en los recuadros, detectar cuándo todos los recuadros se hayan destapado y se revele la figura completa, y como elemento de innovación para mejorar la memoria del usuario decidimos que lo mejor sería colocar dibujos en lugar de números. Colocamos “emojis” del mismo tamaño y de distintas formas centrados en los cuadros del juego.  

