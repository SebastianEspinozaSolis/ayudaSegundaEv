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