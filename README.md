# Projekt nr 2 - wtyczka do QGIS


FUNKCJE WTYCZKI:

  1. Liczenie różnic wysokości pomiędzy dwoma punktami
     Aby policzyć różnicę wysokości między punktami należy z grupy punktów znajdujących się na tej samej warstwie wybrać dokładnie dwa.
     Program pobierze wtedy wartości z tabeli atrybutów w programie QGIS z kolumny o nazwie 'h_plevrf2007nh', w której znajdują się 
     wysokości tych punktów. Wtyczka odejmować będzie wysokość punktu początkowego od wysokości punktu końcowego, co da wynik o znaku 
     dodatnim bądź ujemnym - zależnie od tego w jakiej kolejności podamy nasze punkty. Na podstawie znaku uzyskanego przewyższenia 
     będzie można zatem stwierdzić, czy na wybranym odcinku nastąpił wzrost czy spadek terenu.

  2. Liczenie pola powierzchni pomiędzy trzema punktami:
     Do obliczenia pola powierzchni między punktami należy z jednej warstwy wybrać trzy punkty. Następnie na podstawie współrzędych tych 
     punktów, które w tabeli atrybutów w programie QGIS znajdują się w kolumnach o nazwach 'x2000' oraz 'y2000', program policzy pole 
     powierzchni zawarte między nimi - przy użyciu metody Gaussa. 
