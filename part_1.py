# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:36:11 2023

@author: Lukas
"""

from math import pi, acos, sin, cos
class Hotel ():
    def __init__(self,nom,codi_hotel,carrer,numero,codi_barri,codi_postal,telefon, latitud, longitud, estrelles):
        #numero/codi_barri/estrelles de tipus int i positius
        if (type(numero) != int) or (numero < 0):
            raise TypeError("numero ha de ser un valor enter positiu")
        if (type(codi_barri) != int) or (codi_barri < 0):
            raise TypeError("codi_barri ha de ser un valor enter positiu")
        if (type(estrelles) != int) or (estrelles < 0):
            raise TypeError("estrelles ha de ser un valor enter positiu")
        #latitud/longitud de tipus float
        if (type(latitud) != float):
            raise TypeError("latitud ha de ser un valor real")
        if (type(longitud) != float):
            raise TypeError("longitud ha de ser un valor real")
        #mirar si estrelles està entre 1 i 5(inclosos)
        if (estrelles < 1) or (estrelles > 5):
            raise ValueError("estrelles ha de ser un valor entre 1 i 5")
        self.nom = nom
        self.codi_hotel = codi_hotel
        self.carrer = carrer
        self.numero = numero
        self.codi_barri = codi_barri
        self.codi_postal = codi_postal
        self.telefon =  telefon
        self.latitud =  latitud
        self.longitud =  longitud
        self.estrelles = estrelles
        
    def __str__(self):
        return (str(self.nom)+" ("+str(self.codi_hotel)+") "+str(self.carrer)+","+str(self.numero)+" "+str(self.codi_postal)+" (barri: "+str(self.codi_barri)+") "+str(self.telefon)+" ("+str(self.latitud)+","+str(self.longitud)+") "+str(self.estrelles)+" estrelles")
    def __gt__(self, altre_hotel):
        #True si self tiene mas estrellas que el otro
        return self.estrelles > altre_hotel.estrelles
    def distancia(self, latitud, longitud):
        #distancia entre un hotel y unas cordenadas
        if (type(latitud) != float):
            raise TypeError(latitud, "ha de ser un valor real")
        if (type(longitud) != float):
            raise TypeError(longitud, "ha de ser un valor real")
        lat1 = (self.latitud *pi)/180
        lat2 = (latitud *pi)/180
        lon1 = (self.longitud *pi)/180
        lon2 = (longitud *pi)/180
        dist = (acos((sin(lat1)*sin(lat2))+(cos(lat1)*cos(lat2)*cos(lon2-lon1))))* 6378.137
        return dist

#Exercici 1.2
def codi_in_llista_hotels(llista_hotels, codi_hotel):
    for i in llista_hotels:
        if codi_hotel == i.codi_hotel:
            return True
    return False

#Exercici 1.3

def importar_hotels (fitxer, separador):
    try:
        llista_hotels = []
        no_primera = 0
        with open(fitxer, "r") as fitxer1:
            for linia in fitxer1:
                if (no_primera > 0):
                    fila = linia[:-1]
                    elements = fila.split(separador)
                    codi = elements[0].split(" - ")
                    nom = codi[0]
                    codi_hotel = codi[1]
                    carrer = elements[1]
                    numero = int(elements[2])
                    codi_barri = int(elements[3])
                    codi_postal = elements[4]
                    telefon = elements[5]
                    latitud = int(elements[6])/1000000
                    longitud = int(elements[7])/1000000
                    estrelles = int(elements[8])
                    if not (codi_in_llista_hotels(llista_hotels, codi_hotel)):
                        hotel = Hotel(nom,codi_hotel,carrer,numero,codi_barri,codi_postal,telefon, latitud, longitud, estrelles)
                        llista_hotels.append(hotel)
                no_primera = 1
            print("S'han importat correctament",(len(llista_hotels)),"hotels")
            return llista_hotels
    except:
         raise FileNotFoundError("fitxer no trobat")
         
#Exercici 1.4
class Barri():
    def __init__(self, nom, codi_districte):
        if (type(codi_districte) != int) or (codi_districte < 0):
            raise TypeError("codi_districte ha de ser un valor enter positiu")
        self.nom = nom
        self.codi_districte = codi_districte
    def __str__(self):
        return (str(self.nom)+" (districte: "+str(self.codi_districte)+")")
   
#Exercici 1.5

def importar_barris(fitxer, separador):
    try:
        barris = {}
        no_primera = 0
        with open(fitxer, "r") as fitxer1:
            for linia in fitxer1:
                if (no_primera > 0):
                    fila = linia[:-1]
                    elements = fila.split(separador)
                    codi_barri = float(elements[0])
                    codi_districte = int(elements[1])
                    nom = elements[2]
                    barri = Barri(nom, codi_districte)
                    barris[codi_barri] = barri
                no_primera = 1
        print("S'han importat correctament",(len(barris)),"barris")
        return barris
    except:
         raise FileNotFoundError("fitxer no trobat")
         
#Exercici 1.6

class Districte():
    def __init__(self, nom, extensio, poblacio): 
        if (type(poblacio) != int) or (poblacio < 0):
            raise TypeError("poblacio ha de ser un valor enter positiu")
        if (type(extensio) != float or (extensio < 0)):
            raise TypeError("extensio ha de ser un valor real positiu")
        self.nom=nom
        self.extensio=extensio
        self.poblacio=poblacio
        self.llista_barris= []
        
    
    def __str__(self):
        
        if (len(self.llista_barris)) == 0:
            noms_barris = "N/D" 
        else:
            for barri in self.llista_barris:
                noms_barris = ", ".join(self.llista_barris)
            
        return f"{self.nom} ({self.extensio} kms2, {self.poblacio} habitants) barris: {noms_barris}"
    
    def densitat(self):
        return self.poblacio/self.extensio
    
    
#Ejercicio 1.7
def importar_districtes (nom_fitxer, separador):
    try:
        with open(nom_fitxer, "r") as fitxer2:
            districtes = {}
            no_primera = 0
            for linia in fitxer2:
                if (no_primera > 0):
                    fila = linia[:-1]
                    elements = fila.split(separador)
                    codi = float(elements[0])
                    nom = (elements[1])
                    extensio = float(elements[2])
                    poblacio = int(elements[3])
                    districte = Districte(nom, extensio, poblacio)
                    districtes[codi] = districte
                no_primera = 1
        print("S'han importat correctament", len(districtes), "districtes")
        return districtes
    except:
        raise FileNotFoundError("fitxer no trobat")
        
        
#Exercici 1.8
def omplir_llista_barris(diccionari_districtes, diccionari_barris):
    # Comprovar si ja hi ha info a la llista_barris
    buits = True
    for districte in diccionari_districtes.values():
        #print(districte.nom , str(len(districte.llista_barris)))
        if len(districte.llista_barris) > 0:
            buits = False
            print("El diccionari de districtes ja conté informació dels barris")
            break
    if buits:    
        # Omplir la llista_barris per cada districte amb la info dels barris
        for barri in diccionari_barris.values():
            districte1 = diccionari_districtes.get(barri.codi_districte)
            districte1.llista_barris.append(barri.nom)
            
#Exercici 1.9
def mostrar_hotels(llista_hotels):
    if not llista_hotels:
        print("No hi ha hotels")
    else:
        for hotel in llista_hotels:
            print(hotel)
            
            
#Exercici 1.10            
def mostrar_menu():
    print(" ")
    print("--- MENÚ PRINCIPAL ---")
    print("1 - Veure hotels")
    print("S - Sortir del programa")
    

#Exercici 1.11 (PROGRAMA PRINCIPAL)
try:
    llista_hotels =importar_hotels ("hotels.csv", ";")
    diccionari_barris = importar_barris("barris.csv", ";")
    diccionari_districtes = importar_districtes("districtes.csv",";")
except FileNotFoundError as FNFE:
    print("Error llegint fitxers: ", FNFE)
except Exception as missage:
    print("Error processant els fitxers: ", missage)
else:
    while True:
        omplir_llista_barris(diccionari_districtes, diccionari_barris)
        mostrar_menu()
        op = input("Introdueix la operació a realitzar: ")
        if (op == "1"):
            mostrar_hotels(llista_hotels)
        if (op == "S" or op == "s"):
            print("Sortint del programa")
            break
        if (op != "S" and op != "s" and op != "1"):
            print("Opció no permesa")
            
        
finally: 
    print("© Lucas Carbó , Hector Rodriguez i Hector Cervelló")
