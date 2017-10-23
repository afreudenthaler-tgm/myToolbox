import threading



class SimpleCounter(threading.Thread):
    """
    Diese Klasse stellt einen Thread dar, welcher
    einen globalen Zaehler 1000-mal erhoeht.
    """

    # Globaler Zaehler
    counter = 0
    # Globale Lock erzeugen
    """
    Lock wird erstellt
    """
    lock = threading.Lock()
    def __init__(self):
        """
        Initialisiert die Basisklasse Thread.
        """ 
        threading.Thread.__init__(self)

    def run(self):
        """
        Erhoeht counter 1000-mal. run() wird
        aufgerufen, sobald der Thread über start()
        gestartet wird.
        :return: None
        """

        """
    Es wird ein sogenannter kritischer Bereich definiert
    Im kritischen Bereich kann sich nur 1 Thread gleichzeitig befinden
    Dort werden jene Operationen durchgefuehrt, die nicht unterbrochen werden duerfen
        """
        # https://docs.python.org/3/library/threading.html?highlight=threading#module-threading suchen nach: Lock
        for i in range(1000):
            # Lock sperren (falls frei), ansonsten warten, bis sie frei ist
            with SimpleCounter.lock:
                # --- Beginn kritischer Abschnitt ---
                # Dieser Bereich kann von nur 1 Thread
                # gleichzeitig betreten werden
                curValue = SimpleCounter.counter
                print("Current Value:" + str(curValue))
                SimpleCounter.counter = curValue + 1
                # --- Ende kritischer Abschnitt ---


# 10 Instanzen der Thread-Klasse erstellen
threads = []
for i in range(0, 10):
    thread = SimpleCounter()
    threads += [thread]
    thread.start()

# Auf die Kind-Threads warten
for x in threads:
    x.join()

# Counter ausgeben
print(SimpleCounter.counter)
if SimpleCounter.counter != 10000:
    print("Wrong result - we should probably synchronize those threads!")