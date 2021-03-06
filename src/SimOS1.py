
#Universidad del Valle de Guatemala
#Algoritmos y Estructuras de Datos
#
#
#Hoja de Trabajo 5
#
#SimOS.py
#
#Ana Fernanda Solares, 13125
#Jose Rolaes, 13576
#

import simpy
import random
import time

print ("Simulacion de corrida de programas en un Sistema Operativo de tiempo compartido.")

# se usa para que el random siempre genere la misma secuancia de numeros.
random.seed(9)
# Cantidad de procesos a generar
numeroProcesos = 25 
#intervalo de llegada de los procesos
intervalo = 10
# cantidad de ram
ram_cant = 100
# intrucciones que puede ejecutar el cpu por proceso
cpu_cap= 3
#tiempo de llegada de procesos
tllprocesos = random.expovariate(1.0 / intervalo)
# cantidad de intrucciones de cada proceso, entero de 1 a 10, (1, 11) ya q 11 no se toma en cuenta
#Esto crea un valor random solo una vez!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
instrucc = random.randint(1, 11)
# cantidad de ram requerida por el proceso , entero de 1 a 100
ramAsig = random.randrange(1, 101)
#tiempo de todos los procesos
global tiempoT

def proceso(env, nproceso, ram, intrucc):
    #tomar tiempo de entrada del proceso
    tEntrada = env.now
    #entrada de proceso %s en el tiempo %d
    print ('%s entrado en %d' % (nproceso, env.now))

    
    #tiempo de por proceso
    tiempoxproceso = env.now - tEntrada
    #se suman todos los tiempos a tiempoT
    tiempoT = tiempoT + tiempoxproceso
def source (env, procesos, intervalo, procesador, ram, ):
# se crea el ambiente de simulacion
env = simpy.Environment()

#se define el la cantidad de ram
ram = simpy.Container(env, ram_cant, init=0)
#se define la capacidad del cpu
cpu = simpy.Resource(env, capacity=1)
#tiempo de todos los procesos
tiempoT = 0.0

# crear los procesos
for i in range(numeroProcesos):
    tiempo = random.randint(1, 11)
    #crear proceso
    env.process(proceso(env, 'Proceso %d' % i, ramAsig, instrucc))
    # pausa para generar los procesos a diferentes intervalos (en segundos)
    time.sleep(tiempo)

# se corre la simulacion
env.run()

# se toma el promedio de ejecucion de los procesos
promedio = (tiempoT/numeroProcesos)

# se imprime el promedio
print ("Promedio con %d prcesos: %.2f" % (numeroProcesos, promedio))

