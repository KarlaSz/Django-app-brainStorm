# pip install django
# django-admin startproject nazwaFolderu

#projekt django zawiera w srodku wiele aplikacji
#appki jak np. forum,crm ,sklep, takie duze zlozone segmenty
#django te appki moga byc wspoldzielone
#moze te appki kopiowac

#forum

# python manage.py startapp ideas


#asocjacje (powiazanie) - w schemacie jeden do jednego, 1 user = 1 konto/profil,
#  1 do wielu  1 = komentarz = wiele glosow
# wielu do wielu np. 1 glos w wielu pomyslach - tutaj nie
# pomysl posiada wiele glosow - Foreign key

#modele zamienic na bazy danych i zarejestrowac jako admin, w panelu admin. i dostowac czy dziala
#wygenerowac migracje i puscic migracje - to co zmienia stan bazy, i jesli inni programisci maja tez miec dostep do tego to trzeba udostepnic kawalek kodu na glowna galaz i przeniesc to tez zarazem na inne srodowiska testowe, deweloperskie czy produkcyjne
#zamiasz dyktowac kazdemu co robic za kazdym razem bo ma sie te zmiany czasowo u siebie lokalnie
#skrypty migracyje - lista polecen i zostana zaplikowane zmiany dostepne dla wszystkich i w bazie danych

#python manage.py makemigration ideas
#python manage.py migrate

#python manage.py runserver


# http://127.0.0.1:8000/admin

# karo
# karo1234

#admin to jest przywilej w pythonie, bo mozna przechowywac realne dane z panelem dla osob do tworzenia aplikacji i zarzadzac nimi pelnowymiarowo. nie trzeba dodatkowo go instalowac
#w kazdym projekcie potrzebne sa dane, do zarzadzania danymi apki jest admin model


# w ramach projektu mamy wiele aplikacji
#a kazda aplikacja powinna miec ten model zarejestrowany
# admin.site.register() # i podaje sie model jaki sie chce ziamportowac


#wpisanie w terminaly "python manage.py" - wywoluje liste dostepnych funkcji
