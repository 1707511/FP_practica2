# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 01:08:50 2023

@author: Lukas
"""


#Exercici 1
from math import pi, acos, sin, cos
class Hotel ():
    def __init__(self,nom,codi_hotel,carrer,numero,codi_barri,codi_postal,telefon, latitud, longitud, estrelles):
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
        #numero/codi_barri/estrelles de tipus int i positius
        if (type(self.numero) != int) or (self.numero < 0):
            raise TypeError(self.numero, "ha de ser un valor enter positiu")
        if (type(self.codi_barri) != int) or (self.numero < 0):
            raise TypeError(self.codi_barri, "ha de ser un valor enter positiu")
        if (type(self.estrelles) != int) or (self.numero < 0):
            raise TypeError(self.estrelles, "ha de ser un valor enter positiu")
        #latitud/longitud de tipus float
        if (type(self.latitud) != float):
            raise TypeError(self.latitud, "ha de ser un valor real")
        if (type(self.longitud) != float):
            raise TypeError(self.longitud, "ha de ser un valor real")
        #mirar si estrelles està entre 1 i 5(inclosos)
        if (self.estrelles < 1) or (self.estrelles > 5):
            raise ValueError("estrelles ha de ser un valor entre 1 i 5")
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

#Exercici 2
def codi_in_llista_hotels(llista_hotels, codi_hotel):
    for i in llista_hotels:
        if codi_hotel == i.codi_hotel:
            return True
    return False

#Exercici 3

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
    except FileNotFoundError:
         print("fitxer no trobat")
         
#Exercici 4
class Barri():
    def __init__(self, nom, codi_districte):
            self.nom = nom
            self.codi_districte = codi_districte
            if (type(self.codi_districte) != int) or (self.codi_districte < 0):
                raise TypeError(self.codi_districte, "ha de ser un valor enter positiu")
    def __str__(self):
        return (str(self.nom)+" (districte: "+str(self.codi_districte)+")")
    
#Exercici 5

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
    except FileNotFoundError:
         print("fitxer no trobat")
         
#Exercici 6

class Districte():
    def __init__(self, nom, extensio, poblacio):  
        self.nom=nom
        self.extensio=extensio
        self.poblacio=poblacio
        self.llista_barris= []
        if (type(self.poblacio) != int) or (self.poblacio < 0):
            raise TypeError(self.poblacio, "poblacio ha de ser un valor enter positiu")
        if (type(self.extensio) != float) or (self.extensio < 0):
            raise TypeError(self.extensio, "extensio ha de ser un valor real positiu")
    
    def __str__(self):   
        missatge = (str(self.nom)+" ("+str(self.extensio)+" kms2, "+str(self.poblacio)+ "   habitants) barris: ")
        if (self.llista_barris):
            for barri in self.llista_barris:
                missatge+= str(barri.nom)
            return missatge
        else:
            missatge += " N/D"
            return missatge
    
    def densitat(self):
        return self.poblacio/self.extensio
    
#Ejercicio 7
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
    except FileNotFoundError:
        return ("fitxer no trobat")
        
        
#Exercici 8
def omplir_llista_barris(diccionari_districtes, diccionari_barris):
    # Comprovar si ja hi ha info a la llista_barris
    buits = True
    for districte in diccionari_districtes.values():
        #print(districte.nom , str(len(districte.llista_barris)))
        if len(districte.llista_barris) > 0:
            buits = False
            print("El diccionari de districtes ja conté informació dels barris")
            return
    if buits:    
        # Omplir la llista_barris per cada districte amb la info dels barris
        for barri in diccionari_barris.values():
            codi = barri.codi_districte
            districte1 = diccionari_districtes[codi]
            districte1.llista_barris.append(barri.nom)
                    
#Exercici 9
def mostrar_hotels(llista_hotels):
    if not llista_hotels:
        print("No hi ha hotels")
    else:
        for hotel in llista_hotels:
            print(hotel)
    

#Exercici 2.1
def ordenar_per_estrelles(llista_hotels):
    hotels_return = llista_hotels
    return sorted(hotels_return, key= lambda hotel: hotel.estrelles)

#Exercici 2.2
def  mostrar_noms_hotels(llista_hotels):
    for hotel in llista_hotels:
        print(str(hotel.nom)+" ("+str(hotel.codi_hotel)+")")
        
#Exercici 2.3
def buscar_per_nom(llista_hotels, cadena):
    # hotels_return = []
    # cadena_buscar = str(cadena.lower())
    # for hotel in llista_hotels:
    #     nom = str((hotel.nom).lower())
    #     if cadena_buscar in nom:
    #         hotels_return.append(hotel.nom)
    hotels_return = list(filter(lambda hotel: cadena.lower() in (hotel.nom).lower(), llista_hotels))
    return hotels_return
    
#Exercici 2.4
def buscar_per_estrelles(llista_hotels, num_estrelles):
    hotels_filtrats = list(filter(lambda hotel: hotel.estrelles == num_estrelles, llista_hotels))
    return (hotels_filtrats)

#Exercici 2.5
def  buscar_hotels(llista_hotels):
    criteri = input("Introdueix criteri de cerca (1 - per nom, 2 - per estrelles): ")
    if (criteri == "1"):
        nom_buscar = input("Introdueix el nom del Hotel a buscar: ")
        hotels_buscats = buscar_per_nom(llista_hotels, nom_buscar)
        if (len(hotels_buscats) > 0):
            print("S'han trobat "+str(len(hotels_buscats))+" hotels amb aquest nom")
            mostrar_noms_hotels(hotels_buscats)
        elif (len(hotels_buscats) == 0):
            print("No s'han trobat hotels")
    elif (criteri == "2"):
        estrella_comp = True
        while (estrella_comp):
            try:
                estrelles_buscar = int(input("Introdueix el número de estrelles que té l'hotel que busques: "))
                estrella_comp = False
            except ValueError:
                print("Error: el número d'estrelles ha de ser un valor enter")
                estrella_comp = True
            finally:
                if (1 > estrelles_buscar) or (estrelles_buscar > 5):
                    print("Error: el número d'estrelles ha de ser un valor entre 1 i 5")
                    estrella_comp = True
        hotels_buscats = buscar_per_estrelles(llista_hotels, estrelles_buscar)
        if (len(hotels_buscats) > 0):
            print("S'han trobat "+str(len(hotels_buscats))+" hotels de "+str(estrelles_buscar)+" estrelles")
            mostrar_noms_hotels(hotels_buscats)
        elif (len(hotels_buscats) == 0):
            print("No s'han trobat hotels")
    else:
        print("Error: criteri de cerca no vàlid")

#Exercici 2.6
def  hotel_mes_proper(llista_hotels, latitud, longitud):
    if ((len(llista_hotels)) == 0):
        return None, None
    else:
        hotel_proper = 1
        distancia_propera = 9999999999999.0
        for hotel in llista_hotels:
            distancia_hotel = hotel.distancia(latitud, longitud)
            if (distancia_hotel < distancia_propera):
                distancia_propera = distancia_hotel
                hotel_proper = hotel
        return hotel_proper, distancia_propera
    
#Ejercicio 3.1
def ordernar_per_nom (llista_hotels_ciutat):
    llista_manipulable = llista_hotels_ciutat
    return list(sorted(llista_manipulable, key=lambda Hotel: (Hotel.nom).lower()))

#Ejercicio 3.2
def carrers_amb_hotels(llista_hotels_ciutat):
    carrers=set()
    for hotel in llista_hotels_ciutat:
        carrers.add(hotel.carrer)
    return list(carrers)

#Ejercicio 3.3
def estrelles_per_barri(llista_hotels, diccionari_barris):
    estrelles_barri = {}
    for barri in diccionari_barris:
        llista = [0,0,0,0,0]
        for hotel in llista_hotels:
            estrella = 0
            if (barri == hotel.codi_barri):
                estrella = hotel.estrelles
                if (estrella == 1):
                    llista[0] += 1
                if (estrella == 2):
                    llista[1] += 1
                if (estrella == 3):
                    llista[2] += 1
                if (estrella == 4):
                    llista[3] += 1
                if (estrella == 5):
                    llista[4] += 1
        estrelles_barri[(diccionari_barris[barri].nom)] = llista
    return estrelles_barri


#Ejercicio 3.4
def densitat_per_districte (llista_hotels, diccionari_barri, diccionari_districtes):
    diccionari_nou = {}
    for hotel in llista_hotels:
        codi_barri = hotel.codi_barri
        codi_districte = diccionari_barri[codi_barri].codi_districte
        if codi_districte in diccionari_nou:
            diccionari_nou[codi_districte] +=1
        else: 
            diccionari_nou[codi_districte] = 1
    for codi, districte in diccionari_districtes.items():
        superficie = districte.extensio
        hotels = diccionari_nou[codi]
        densitat = hotels/superficie
        diccionari_nou[codi] = densitat        
    return diccionari_nou

#Ejercicio 3.5
def afegir_prefixe_int(hotel):
    telefon = hotel.telefon
    if (telefon[0] != "+"):
       telefon = "+34"+str(telefon)
       hotel.telefon = telefon
    return hotel
    

#Ejercicio 3.6
def modificar_telefons(llista_hotels):
    comprovacio_telefons= list(map(afegir_prefixe_int, llista_hotels))
    return comprovacio_telefons

#Ejercicio 3.7
def mostrar_menu():
    print("--- MENÚ PRINCIPAL ---")
    print("1 - Veure hotels")
    print("2 - Veure hotels per estrelles")
    print("3 - Buscar hotels")
    print("4 - Buscar hotel proper")
    print("5 - Llistat alfabètic d'hotels")
    print("6 - Carrers amb hotels")
    print("7 - Estadística per barris")
    print("8 - Estadística per districtes")
    print("9 - Internacionalitzar telèfons")
    print("S - Sortir del programa")
    
#Exercici 3.8 (PROGRAMA PRINCIPAL) ---> (modificat del anterior ex,2.8)   
try:
    llista_hotels =importar_hotels ("hotels.csv", ";")
    diccionari_barris = importar_barris("barris.csv", ";")
    diccionari_districtes = importar_districtes("districtes.csv",";")
except FileNotFoundError as FNFE:
    print("Error llegint fitxers: ", FNFE)
except Exception as missage:
    print("Error processant els fitxers: ", missage)
else:
    op = 1
    omplir_llista_barris(diccionari_districtes, diccionari_barris)
    while (op != "s"):
        mostrar_menu()
        op = input("Introdueix la operació a realitzar: ")
        if (op == "1"):
            mostrar_hotels(llista_hotels)
        elif (op == "2"):
            llista_ordenada_estrelles = ordenar_per_estrelles(llista_hotels)
            mostrar_hotels(llista_ordenada_estrelles)
        elif (op == "3"):
            buscar_hotels(llista_hotels)
        elif (op == "4"):
            try:
                latitud = float(input("Introdueix el valor de latitud del punt des d'on vol buscar un hotel proper: "))
                longitud = float(input("Introdueix el valor de longitud del punt des d'on vol buscar un hotel proper: "))
                hotel_proper, distancia_hotel = hotel_mes_proper(llista_hotels, latitud, longitud)
                print("L'hotel més proper és el "+str(hotel_proper)+" a "+str(distancia_hotel)+" kms")
            except ValueError:
                print("Error: latitud i longitud han de ser valors reals")
        elif (op == "5"):
            llista_hotels_ordenats = ordernar_per_nom(llista_hotels)
            mostrar_hotels(llista_hotels_ordenats)
        elif (op == "6"):
            llista_carrers = carrers_amb_hotels(llista_hotels)
            print("Hi ha "+str(len(llista_carrers))+" carrers amb algun hotel: "+str(llista_carrers))
        elif (op == "7"):
            estrelles_barris = estrelles_per_barri(llista_hotels, diccionari_barris)
            for nom_barri, llista_estrelles_barri in estrelles_barris.items():
                print("El barri "+str(nom_barri)+" té "+str(llista_estrelles_barri[0])+" hotels de 1 estrella, "+str(llista_estrelles_barri[1])+" hotels de 2 estrelles, "+str(llista_estrelles_barri[2])+" hotels de 3 estrelles, "+str(llista_estrelles_barri[3])+" hotels de 4 estrelles, "+str(llista_estrelles_barri[4])+" hotels de 5 estrelles\n")
        elif (op == "8"):
            diccionari_densitats = densitat_per_districte(llista_hotels, diccionari_barris, diccionari_districtes)
            for codi_districte, densitat in diccionari_densitats.items():
                print("Districte "+str(codi_districte)+": "+str(densitat)+" hotels/km2\n")
        elif (op == "9"):
            modificar_telefons(llista_hotels)
        elif (op == "S" or op == "s"):
            op = op.lower()
            print("Sortint del programa")
        else:
            print("Opció no permesa")
            
        
finally: 
    print("© Lucas Carbó , Hector Rodriguez i Hector Cervelló")
        











