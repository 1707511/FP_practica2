# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:12:14 2023

@author: Lukas
"""
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
    for codi_districte, districte in diccionari_districtes.items():
        contador_hotels = 0
        densitat = 0
        for barri in districte.llista_barris:
            codi = barri.codi_barri
            for hotel in llista_hotels:
                if codi == hotel.codi_barri:
                    contador_hotels +=1
        superficie = districte.extensio
        densitat = contador_hotels/superficie
        diccionari_nou[codi_districte] = densitat
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
        











