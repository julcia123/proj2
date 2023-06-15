# Projekt nr 2 - wtyczka do QGIS

WYMAGANIA SYSTEMOWE:
  - system Windows 10 lub 11
  - program QGIS (w wersji minimum 3.22)
  - python 3.9
  - biblioteka qgis.PyQt
  - biblioteka qgis.core
  - biblioteka qgis.utils
  - biblioteka numpy
  - biblioteka os
 


FUNKCJE WTYCZKI:

  1. Liczenie różnic wysokości pomiędzy dwoma punktami
  
     Aby policzyć różnicę wysokości między punktami należy z grupy punktów znajdujących się na tej samej warstwie wybrać dokładnie dwa.
     Program pobierze wtedy wartości z tabeli atrybutów w programie QGIS z kolumny o nazwie 'h_plevrf2007nh', w której znajdują się 
     wysokości tych punktów. Wtyczka odejmować będzie wysokość punktu początkowego od wysokości punktu końcowego, co da wynik o znaku 
     dodatnim bądź ujemnym - zależnie od tego w jakiej kolejności podamy nasze punkty. Na podstawie znaku uzyskanego przewyższenia 
     będzie można zatem stwierdzić, czy na wybranym odcinku nastąpił wzrost czy spadek terenu.
     
     Aby wtyczka poprawnie obliczyła różnicę wysokości pomiędzy punktami, ich wysokości powinny być wyrażone w systemie wysokości  
     'EVRF2007', a zaznaczone punkty muszą znajdować się na warstwie o nazwie 'Osnowa wysokościowa' lub takiej, która w tabeli artybutów
     posiada kolumnę z wysokościami w odpowiednim systemie o nazwie 'h_plevrf2007nh'. 
     
     Podany wynik wyrażony jest w metrach, z centymetrową dokładnością.
     
     
  2. Liczenie pola powierzchni pomiędzy zaznaczonymi punktami:
  
     Do obliczenia pola powierzchni między punktami należy z jednej warstwy wybrać przynajmniej trzy punkty. Następnie na podstawie współrzędych tych 
     punktów, program policzy pole powierzchni zawarte między nimi - przy użyciu metody Gaussa. 
     
     Aby wtyczka poprawnie obliczyła pole powierzchni między punktami, powinny się one znajdować na warstwie, która w swojej tabeli
     atrybutów posiada kolumny ze współrzędnymi w układzie PL2000 o nazwach 'x2000' oraz 'y2000'.
     
     Podany wynik wyrażany jest w hektarach, z dokładnością do trzeciego miejsca po przecinku.
     
     
     
SPOSÓB UŻYCIA WTYCZKI:
  1. Na samym początku należy pobrać wtyczkę i umieścić ją w folderze z wtyczkami (prawdopodobna ścieżka z wtyczkami Twojego urządzenia:                          "C:\Users\XXX\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins" ---- NALEŻY ZMIENIĆ "XXX" NA TWOJĄ NAZWĘ UŻYTKOWNIKA)                              a następnie załadować wtyczkę w programie QGIS.
  2. Następnie wczytać trzeba mapę zawierającą potrzebne, wymienione wyżej artybuty i uruchomić warstwę o nazwie 'Osnowa wysokościowa'
  3. Po wczytaniu mapy należy zaznaczyć na mapie odpowiednią liczbę punktów narzędziem o nazwie 'Zaznacz obiekty prostokątem lub 
     kliknięciem'
  5. Następnie w okienku wtyczki wybrać trzeba odpowiednią warstwę ('Osnowa wysokościowa')
  6. Po kliknięciu 'Policz' obok wybranej funkcji obok przycisku powinien pojawić się wynik. Jeśli użytkownik nie wybierze wymaganej
     do wykonania wybranej operacji liczby punktów program wyświetli komunikat o powstałym błędzie.
     
     
     
PRZYKŁADOWE PLIKI, NA KTÓRYCH MOŻNA UŻYĆ WTYCZKI (łącze WFS dostępne na stronie geoportal.gov.pl):
  - https://mtorun-wms.webewid.pl/iip/ows




