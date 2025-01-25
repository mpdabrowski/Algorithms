**Twierdzenie 1**: Dla każdego acyklicznego grafu skierowanego *G*=(*V*,*E*) w postaci listy sąsiedztwa:
>(a) Po zakończeniu działania algorytmu ```TopoSort```, każdy wierzchołek *v* ma przypisaną wartość *f*, a te wartości *f* stanowią uporządkowanie topologiczne grafu *G*.

>(b) Czas działania algorytmu TopoSort wynosi *O(m+n)*, gdzie *m=|E|*, a *n=|V|*.

**Dowód**: ```DFS-Topo``` zostanie wywołana dla każdego wierzchołka *v* ∈ *V* dokładnie raz, gdy v zostanie po raz pierwszy napotkany. Po zakończeniu wywołania ```DFS-Topo```, wierzchołkowi *v* zostanie przypisana etykieta. Zatem każdy wierzchołek otrzymuje etykietę, a poprzez dekrementację zmiennej ```curLabel``` przy każdym przypisaniu etykiety, algorytm zapewnia, że każdy wierzchołek otrzymuję unikatową etykietę *f(v)* z zakresu *{1, 2, …, |V|}*. Aby przekonać się, dlaczego te etykiety stanowią uporządkowanie topologiczne rozważmy dowolną krawędź *(v, w)*; należy wykazać, że *f(v)* < *f(w)*. Istnieją dwa przypadki, w zależności od tego, który z wierzchołków *v* czy w algorytm odkrywa jako pierwszy.\
**Przypadek 1** *v* jest odkrywany przed *w*:\
Wówczas ```DFS-Topo``` jest wywoływana dla wierzchołka *v* przed tym 
zanim w został oznaczony jako odwiedzony. Ponieważ *w* jest osiągalny z 
*v* (przez krawędź *(v,w)*), to wywołanie ```DFS-Topo``` w końcu odkryje *w* i 
rekurencyjnie wywoła ```DFS-Topo``` dla *w*. Ze względu na fakt, iż 
wywołania rekurencyjne tworzą stos wywołań (struktura last-in first
out), wywołanie ```DFS-Topo``` dla *w* zakończy się przed wywołaniem ```DFS-Topo``` dla *v*. Ponieważ etykiety są przypisywanie w porządku malejącym, 
*w* otrzyma większą wartość niż *v* co jest zgodne z wymogiem 
sortowania topologicznego.\
**Przypadek 2** w jest odkrywane przed *v*:\
 Ponieważ *G* jest grafem skierowanym acyklicznym nie istnieje ścieżka 
prowadząca z *w* do *v*; w przeciwnym razie połączenie takiej ścieżki z 
krawędzią *(v, w)* utworzyłoby graf skierowany. Oznacza to, że 
wywołanie ```DFS-Topo``` rozpoczynające się w w nie może odkryć *v* i kończy 
się gdy *v* jest nadal nieodwiedzone. Ponownie, wywołanie ```DFS-Topo``` dla 
w kończy się przed wywołanie dla *v*, a zatem *f(v)* < *f(w)* co kończy dowód części (a).

Algorytm ```TopoSort``` działa w czasie liniowym. Przegląda on każdą 
krawędź dokłanie raz (od je początku), a zatem wykonuje stałą liczbę 
operacji dla każdego wierzchołka lub krawiędzie. To implikuje czas 
działania równy *O(m + n)*, a zatem (b) jest również prawdziwe.





