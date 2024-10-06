# ayudaSegundaEv
para iniciar el proyecto hay que hacer git clone al repositorio, luego se inicia el proyecto con
# django-admin startproject proyecto
luego se debe agregar un .gitignore con: *.sqlite3 *.pyc

ahora, para crear apps se realiza con: 
# python manage.py startapp app1

luego de eso hay que agregar estas app a settings del proyecto principal

ahora para los templates y eso hay que seguir en settings, bajar hasta Templates, y arriba agregar
# import os
y luego dentro de templates y en DIRS: [], dentro de [] agregar
# [os.path.join(BASE_DIR,'templates')]

con eso realizado hay que continuar bajando, hasta static_url y agregar lo siguiente
#STATICFILES_DIR = [os.path.join(BASE_DIR, 'static')]

para el ejemplo de multiples apps se agrega otra app y un inicio, inicio suele ser donde comienza la web
# python manage.py startapp app2
# python manage.py startapp inicio

asi que luego hay que añadir a settings y se puede continuar con creacion de las views

ahora para la views, se puede comenzar de inicio la cual sera lo primero que se abrira al iniciar la app

y para crear una vista se crea una funcion con:
# def inicio(request):
#   return render(request, 'inicio/inicio.html')
esta funcion ira cambiando, primero al lado de def ira el nombre de la vista para luego usarlo en url,
y luego de request, ira 'nombre de app por la carpeta que tendra templates/nombre del archivo html que se quiere mostrar en la vista'

y esto mismo se puede hacer con las demas app, con la 1 y 2 haciendo 2 vista por cada una, cambiando solo nombre de vista y ruta de html
app 1
# def vista1_app1(request):
#   return render(request, 'app1/vista1_app1.html')
# def vista2_app1(request):
#   return render(request, 'app1/vista2_app1.html')
app 2
# def vista1_app2(request):
#   return render(request, 'app2/vista1_app2.html')
# def vista2_app2(request):
#   return render(request, 'app2/vista2_app2.html')


ahora hay que crear la carpeta templates, a altura de directorio, misma altura que readme

dentro de este añadir un base.html
se puede copiar el base.html de este proyecto, pero hay que recordar adaptar por las apps y carpetas que usa el proyecto nuevo diferente a este

luego de eso hay que crear cada template en cada carpeta de app que haya
el orden de creacion es en inicio por ejemplo:
inicio/templates/inicio
crear templates dentro de la app y dentro de templates crear una carpeta con el nombre de la app
dentro de esta carpeta crear un archivo html por cada view que se hizo, aqui es donde iran las views de antes
por ejemplo, inicio solo era inicio.html por lo que ese se crea

en el caso de ahora es solo de prueba, se puede copiar o usar algun otro, ahora con el resto de apps