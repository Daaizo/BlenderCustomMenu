# Blender Custom Menu using Python 

To run menu : 
1) download script (file with .py)
2) open blender
3) go to scripting workspace (top right)
4) open script by pressing "Open" (file with .py)
5) click run or ALT+P
6) done, now you can close scripting workspace

Custom menu with BPY for basic operations such as:
- Add basic shapes
- select/unselect all objects
- delete selected obejct/s
- Move object 
- Reset object postition
- Resize object
- Reset object size
- Enlarge or reduce the object by 2 times
- Rotate object
- Reset rotation of object

<br>Author Daniel Charlak CS student<br>
<br>Menu made with official documentation :https://docs.blender.org/api/current/index.html#blender-3-2-python-api-documentation <hr>
<h3> Final menu design </h3>

<img align="center" src=https://user-images.githubusercontent.com/84875747/173661607-75235c40-cfbe-43e1-be1e-ec4184827c00.png>
<h3> Where to find the menu - just click </h3>



<img align="center" src=https://user-images.githubusercontent.com/84875747/173660943-cfee51f9-a2e4-4c6c-a3e9-5ac147b5ae70.png>


<h3>FULL EXPLANATION [PL] </h3><br>
<h4>Jak to działa ?<h4>
Blender posiada wbudowany interpreter Pythona, który jest ładowany po jego uruchomieniu i pozostaje aktywny podczas jego pracy. Blender udostępnia swoje moduły Pythona, takie jak bpy i  mathutils, wbudowanemu interpreterowi, dzięki temu możemy zaimportować je do skryptu i  uzyskać dostęp do danych, klas i funkcji Blendera. Zapewnia on środowisko w którym możemy pisać i  uruchamiać skrypty. 
W celu otworzenia menu skryptowego należy wybrać zakładkę "Scripting" z górnego menu Blendera. Będzie to miejsce w którym zostanie wykonana cała praca.
 
<h4>Tworzenie obietków za pomocą skrypu</h4>
W momencie gdy mamy otworzone środowisko do skryptów widzimy w jaki sposób Blender tworzy nowe obiekty. W celu stworzenia wbudowanego obiektu użyłem skrótu klawiszowego Shift+A . Następnie przesunąłem obiekty zaznaczając go i naciskając klawisz G. Po tym czynnościach możemy zaobserwować jakich poleceń Blender użył do wykonania konkretnych akcji.
Do stworzenia kuli została użyta funkcja bpy.ops.mesh.primitive_uv_sphere_add(), a do stworzenia kostki bpy.ops.mesh.primitive_cube_add(). Funkcje te posiadają różne argumenty ale gdy chcemy stworzyć standardową bryłę, taką samą jak przy użyciu skrótu Shift+A możemy użyć tych funkcji bez argumentów. Do przesunięcia obiektów została użyta funkcja bpy.ops.tranfsorm.translate() , która po słowie value przyjmuje 3 argumenty X,Y,Z. Odpowiadają one przesunięciu w danej osi. 
W celu zautomatyzowania tego procesu możemy napisać skrypt. Pierwszą rzeczą jaką musimy zrobić jest zaimportowanie biblioteki bpy. Następnie możemy użyć poznanych funkcji do tworzenia obiektów. Dodatkowo zmieniłem motyw Blendera(górne menu -> edit -> preferences->themes) na "print friendly" tak, aby pisany kod był bardziej widoczny.


  <h4>Klasa panel – tworzenie menu</h4>
W celu stworzenia bardziej skomplikowanego skryptu użyłem klasy bpy.types.Panel . Udostępnia ona metody do tworzenia menu i rysowania obiektów. Najważniejsze jej zmienne to :
•	bl_description – etykieta panelu
•	bl_label – etykieta wyświetlana w nagłówku panelu
•	bl_space_type – przestrzeń, w której panel będzie używany
•	bl_category - kategoria (karta), w której będzie wyświetlany panel.
Dodatkowo tworząc tą klasę musimy zaimplementować metodę draw(self,content). Gdzie self jest to referencja do klasy. Metoda ta pozwala na dodawanie elementów do obiektu. Zgodnie z definicją w dokumentacji w celu dodania tekstu do naszego panelu należy użyć  self.layout.label(text=" ") . W celu utworzenia klasy i dodania jej do Blendera musimy użyć rejestracji klasy – polecenia bpy.utils.register_class(nazwaKlasy). Ponieważ nie dodaliśmy żadnej kategorii do panelu został on dodany w nowej zakładce o nazwie "Misc".






  <h4>Tworzenie przycisków z ikonami</h4>
W celu stworzenia przycisków najpierw musimy stworzyć miejsce w naszym panelu. Użyjemy do tego funkcji row(),column() i box() w metodzie draw() wewnątrz naszej klasy. Metody te tworzą odpowiednio : wiersz, obramowane miejsce i kolumny. Dodatkowo możemy te elementy używać wielokrotnie i dzielić metodą split() w celu uzyskania ciekawego wyglądu. Przykładowe użycie tych metod :
W celu stworzenia przycisku użyjemy funkcji operator(), jako argumenty może ona przyjąć funkcję jaką chcemy nadać przyciskowi, ikonę i tekst. Funkcje dodawania wyglądają tak samo jak na zrzucie ekranu nr 3, tylko bez przedrostka "by.ops".Lista dostępnych ikon możemy włączyć w górnym menu (edit -> preferences -> Add-ons). Listę możemy włączyć kiedy jesteśmy  w zakładce scripting i naciśniemy Ctrl+T. Każdą z ikon możemy dodać do naszego przycisku.
 Bardzo przydatne okazało się włączenie "python tooltips" w górnym menu (edit->preferences->interface). Pozwala to zobaczyć jaki kod jest użyty to wykonania jakiej akcji.
 

<h4> Klasa Operator – tworzenie właśnych funkcji</h4>
W celu dodania ciekawszych funkcji potrzebne jest zdefiniowane własnych operatorów. Operatorem jest każda instrukcja zaczynająca się od przedrostka "by.ops". Klasa ta podobnie jak klasa Panel jest rozszerzeniem klasy types. Do najważniejszych atrybutów klasy należą :
•	bl_idname – nazwa z jaką będziemy wywoływać naszą funkcję. Każdy operator musi posiadać co najmniej jedną kropkę w nazwie.
•	bl_label – tytuł z jakim będzie wyświetlone okno operatora
•	bl_options – kluczowe jest dodanie opcji REGISTER, która pozwoli na wyświetlenie okna operatora i opcji UNDO, która pozwoli na cofanie operacji
•	dodatkowo po definicji klasy możemy  w potrójnym apostrofach zdefiniować podpowiedź jaka będzie wyświetlana do naszego operatora

Bardzo ważną funkcją w tym wypadku jest execute(self,context), jest to funkcja w której określamy co robi nasz operator. Funkcja ta musi zwracać określny typ, ja będę używał głównie tych trzech :
•	CANCELLED - operator zakończył akcję ale nic się nie stało
•	FINISHED – operator pomyślnie zakończył akcję 
•	PASS_THROUGH – zakończenie akcji bez żadnej akcji, może być użyte do sprawdzenia warunku np. czy obiekt istnieje 
Typ zwracany musi zostać umieszczony w {} i w apostrofach. Podobnie jak klasa Panel, klasa Operator musi zostać zarejestrowana przed użyciem. Dodatkowo potrzebujemy zdefiniować zmienne, które będą przekazywane do funkcji execute() za pośrednictwem referencji self. W Blenderze zamiast użycia tradycyjnych wartości float i int będziemy używać properties z klasy by.props. Pozwalają one na wstawienie elementów graficznych np. sliederów przez klasę bpy.props.FloatProperty(), czy checkboxa przez klasę  bpy.props.BoolProperty(). Dodatkowo możemy nadać tym wartościom nazwę i opis. Pozwoli nam to w dalszym dodaniu operatora do naszego menu. Po manualnym teście okazuje się, że gdy obiekt jest skalowany w danej osi zostaje wywołany operator bpy.context.object.scale[0] = wartość. Podanie 0 jako argumentu zmienia wielkość w płaszczyźnie X, 1- Y i 2 – Z. Kiedy nasz operator jeszcze nie został dodany do menu możemy wywołać go tylko przez konsolę. 
Stworzenie klasy zaczyna się od nadania nazwy operatora. Ponieważ każdy operator musi posiadać kropkę w przedrostku dodałem "object" ponieważ odnosi się on do obiektów. Przedrostek może być dowolny. Cały operator został nazwany object.resize_selected więc przez konsolę mamy do niego dostęp używając by.ops.object.resize_selected(). W klasie zostały zadeklarowane 3 wartości bpy.props.FloatProperty(), które odpowiadają graficznemu stworzeniu slidera  z liczbami zmiennoprzecinkowymi. W funkcji wykonującej pobierane są wartości ze slidera i wstawiane bezpośrednio do funkcji skalującej w danej osi. Wywołując operator jako argumenty musimy podać 3 wartości : size_x, size_y i size_z. Po wykonaniu powyższych kroków i zarejestrowaniu operatora został on dodany do Blendera. Stał się on pełnoprawną funkcją do wykonania i po zaznaczeniu opcji "developer extras" (Preferences -> Interface) jest on dostępny do wyszukania pod klawiszem F3 i także w konsoli. Testowe wywołanie nowego operatora na kuli 
Możemy zauważyć, że każda zmiana na sliderze wywołuje naszą funkcję z odpowiednimi parametrami. Gdy operator już działa możemy go dodać do naszego menu przez wywołanie .operator(nazwa operatora) na naszym elemencie do którego dodajemy przyciski. Tak samo jak w przypadku predefiniowanych operatorów.
 

<h4>Funkcja Invoke</h4>
Po kilku próbach testowych okazało się, że nowy operator nie działa zgodnie z  oczekiwaniami. Zaznaczając kolejny obiekt nasz operator był wywoływany bez parametrów, a  wartościom sliderów przypisywane było 0. Dodatkowo gdy zmieniliśmy wielkość jednego obiektu i  uruchomiliśmy operator na drugim obiekcie przypisywane zostawały mu poprzednie wartości sliderów .Do rozwiązania tego problemu zastosowałem funkcję invoke. Funkcja operator.invoke służy do inicjalizacji operatora z kontekstu w momencie jego wywołania. invoke() jest zwykle używana do przypisywania właściwości, które są następnie wykorzystywane przez execute(). Definiuje się ją podobnie jak funkcję execute tylko z dodatkowym parametrem event : def invoke(self, context, event): . W funkcji pobrałem wartości x,y i z jakie obiekt ma w momencie wywołania i dodałem je do sliderów. W skutek czego problem został rozwiązany.
 
<h4>Funkcja poll</h4>
Funkcja poll jest używana do sprawdzenia czy operator może się wykonać. W naszym przypadku jednym kryterium jest istnienie jakiegoś obiektu. W celu sprawdzenia, czy jakiś obiekt istnieje lub czy jest zaznaczony możemy w dokumentacji znaleźć gotową funkcję :
Po dodaniu funkcji do klasy operatora w momencie, gdy nie ma żadnego obiektu przycisk odpowiadający operatorowi jest szary i nie jest możliwe wywołanie operatora.

