import math

def vitesse(distance, temps):
    return distance / temps

def distance(vitesse, temps):
    return vitesse * temps

def temps(distance, vitesse):
    return distance / vitesse

def masse_volumique(masse, volume):
    return masse / volume

def masse(masse_volumique, volume):
    return masse_volumique * volume

def volume(masse, masse_volumique):
    return masse / masse_volumique

def poids(masse, gravite=9.81):
    return masse * gravite

def masse_from_poids(poids, gravite=9.81):
    return poids / gravite

def gravite(poids, masse):
    return poids / masse

def energie_cinetique(masse, vitesse):
    return 0.5 * masse * vitesse ** 2

def masse_from_energie_cinetique(energie, vitesse):
    return 2 * energie / (vitesse ** 2)

def vitesse_from_energie_cinetique(energie, masse):
    return math.sqrt(2 * energie / masse)

# Formules d'electricite
def loi_ohm_u(i, r):
    return i * r

def loi_ohm_i(u, r):
    return u / r

def loi_ohm_r(u, i):
    return u / i

def puissance_p(u, i):
    return u * i

def puissance_u(p, i):
    return p / i

def puissance_i(p, u):
    return p / u

def energie_e(p, t):
    return p * t

def energie_p(e, t):
    return e / t

def energie_t(e, p):
    return e / p

# Loi de Snell-Descartes
def snell_descartes_n1(n2, angle2, angle1):
    return n2 * math.sin(math.radians(angle2)) / math.sin(math.radians(angle1))

def snell_descartes_n2(n1, angle1, angle2):
    return n1 * math.sin(math.radians(angle1)) / math.sin(math.radians(angle2))

def snell_descartes_angle1(n1, n2, angle2):
    return math.degrees(math.asin(n2 * math.sin(math.radians(angle2)) / n1))

def snell_descartes_angle2(n1, n2, angle1):
    return math.degrees(math.asin(n1 * math.sin(math.radians(angle1)) / n2))

# Formules de concentration en masse
def concentration_masse(masse_solute, volume_solution):
    return masse_solute / volume_solution

def masse_solute(concentration, volume_solution):
    return concentration * volume_solution

def volume_solution(masse_solute, concentration):
    return masse_solute / concentration

# Formules de dilution
def concentration_dilution(c_initiale, v_initiale, v_finale):
    return c_initiale * v_initiale / v_finale

def volume_initial(c_initiale, v_finale, c_finale):
    return c_finale * v_finale / c_initiale

def volume_final(c_initiale, v_initiale, c_finale):
    return c_initiale * v_initiale / c_finale

# Formules de conversion
def convertir_vitesse(valeur, unite_source, unite_cible):
    conversion = {
        "m/s": 1,
        "km/h": 3.6,
        "mi/h": 2.237
    }
    return valeur * conversion[unite_source] / conversion[unite_cible]

def convertir_temps(valeur, unite_source, unite_cible):
    conversion = {
        "s": 1,
        "min": 60,
        "h": 3600
    }
    return valeur * conversion[unite_source] / conversion[unite_cible]

def convertir_volume(valeur, unite_source, unite_cible):
    conversion = {
        "m^3": 1,
        "L": 1000,
        "cm^3": 1e6
    }
    return valeur * conversion[unite_source] / conversion[unite_cible]

def convertir_aire(valeur, unite_source, unite_cible):
    conversion = {
        "m^2": 1,
        "cm^2": 1e4,
        "mm^2": 1e6
    }
    return valeur * conversion[unite_source] / conversion[unite_cible]

def convertir_masse_volumique(valeur, unite_source, unite_cible):
    conversion = {
        "kg/m^3": 1,
        "g/cm^3": 1e3,
        "mg/mm^3": 1e6
    }
    return valeur * conversion[unite_source] / conversion[unite_cible]

def conv(valeur,unite_source,unite_cible):
    # Définition des exposants des puissances de 10 pour chaque unité
    exposants = {
        1: 9,   # Giga (10^9)
        2: 6,   # Méga (10^6)
        3: 3,   # Kilo (10^3)
        4: 2,   # Hecto (10^2)
        5: 1,   # Deca (10^1)
        6: 0,   # Base (10^0)
        7: -1,  # Déci (10^-1)
        8: -2,  # Centi (10^-2)
        9: -3   # Milli (10^-3)
    }
    
    if unite_source not in exposants or unite_cible not in exposants:
        print("Unité incorrecte")
        return
    
    # Correction du calcul du facteur de conversion
    facteur_conversion = 10 ** (exposants[unite_cible] - exposants[unite_source])
    
    # Conversion
    valeur_convertie = valeur * facteur_conversion
    return valeur_convertie
    

def main():
    while True:
        print("1. Calculer la vitesse")
        print("2. Calculer la distance")
        print("3. Calculer le temps")
        print("4. Calculer la masse volumique")
        print("5. Calculer la masse")
        print("6. Calculer le volume")
        print("7. Calculer le poids")
        print("8. Calculer la masse a partir du poids")
        print("9. Calculer la gravite")
        print("0. Suivant")
        choix = input("Entrez votre choix: ")
        try: 
            choix = int(choix)
        except ValueError:
            print("Choix invalide.")
            main()

        if choix < 0 or choix > 9 :
            print("Choix invalide.")
            main()

        elif choix == 0:
            print("10. Calculer l'energie cinetique")
            print("11. Calculer la masse a partir de l'energie cinetique")
            print("12. Calculer la vitesse a partir de l'energie cinetique")
            print("13. Calculer la tension")
            print("14. Calculer le courant")
            print("15. Calculer la resistance")
            print("16. Calculer la puissance")
            print("17. Calculer la tension")
            print("18. Calculer le courant")
            print("0. Suivant")
            choix = input("Entrez votre choix: ")
            try:
                choix = int(choix)
            except ValueError:
                print("Choix invalide")
                main()

            if choix < 10  and choix != 0 or choix > 18:
                print("Choix invalide.")
                main()
            elif choix == 0:
                print("19. Calculer l'energie")
                print("20. Calculer la puissance")
                print("21. Calculer le temps")
                print("22. Calculer l'indice de refraction n1")
                print("23. Calculer l'indice de refraction n2")
                print("24. Calculer l'angle d'incidence")
                print("25. Calculer l'angle de refraction")
                print("26. Calculer la concentration en masse")
                print("27. Calculer la masse du solute")
                print("0. Suivant")
                choix = input("Entrez votre choix: ")
                try:
                    choix = int(choix)
                except ValueError:
                    print("Choix invalide")
                    main()

                if choix < 19  and choix != 0 or choix > 27 :
                    print("Choix invalide.")
                    main()
                elif choix == 0:
                    print("28. Calculer le volume de la solution")
                    print("29. Calculer la concentration finale")
                    print("30. Calculer le volume initial")
                    print("31. Calculer le volume final")
                    print("32. Convertir la vitesse")
                    print("33. Convertir le temps")
                    print("34. Convertir le volume")
                    print("35. Convertir l'aire")
                    print("36. Convertir la masse volumique")
                    print("0. suivant")
                    choix = input("Entrez votre choix: ")
                    try:
                        choix = int(choix)
                    except ValueError:
                        print("Choix invalide")
                        main()
                    if choix < 28  and choix != 0 or choix > 36:
                        print("Choix invalide.")
                        main()

                    elif choix == 0:
                        print("37. conversion d'unité normales (ex : kilo vers mili)")
                        print("38. suggérer une amélioration au développeur")
                        print("0. retour au début")
                        choix = input("Entrez votre choix: ")
                        try:
                            choix = int(choix)
                        except ValueError:
                            print("choix invalide")
                            main()
                        if choix == 0:
                            main()
                        elif choix < 37 and choix != 0 or choix > 38:
                            print("Choix invalide.")
                            main()
                        
                    

        


        if choix == 1:
            d = float(input("Entrez la distance (d): "))
            T = float(input("Entrez le temps (T): "))
            v = vitesse(d, T)
            print("La vitesse est", v, "unites de distance par unite de temps.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 2:
            v = float(input("Entrez la vitesse (v): "))
            T = float(input("Entrez le temps (T): "))
            d = distance(v, T)
            print("La distance est", d, "unites de distance.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 3:
            d = float(input("Entrez la distance (d): "))
            v = float(input("Entrez la vitesse (v): "))
            T = temps(d, v)
            print("Le temps est", T, "unites de temps.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 4:
            m = float(input("Entrez la masse (m): "))
            V = float(input("Entrez le volume (V): "))
            ρ = masse_volumique(m, V)
            print("La masse volumique est", ρ, "unites de masse par unite de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 5:
            ρ = float(input("Entrez la masse volumique (ρ): "))
            V = float(input("Entrez le volume (V): "))
            m = masse(ρ, V)
            print("La masse est", m, "unites de masse.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 6:
            m = float(input("Entrez la masse (m): "))
            ρ = float(input("Entrez la masse volumique (ρ): "))
            V = volume(m, ρ)
            print("Le volume est", V, "unites de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 7:
            m = float(input("Entrez la masse (m): "))
            use_default_g = input("Voulez-vous utiliser la gravite par defaut (9.81) ? (oui/non): ").strip().lower()
            if use_default_g == 'non':
                g = float(input("Entrez la gravite (g): "))
            else:
                g = 9.81
            P = poids(m, g)
            print("Le poids est", P, "unites de force.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 8:
            P = float(input("Entrez le poids (P): "))
            use_default_g = input("Voulez-vous utiliser la gravite par defaut (9.81) ? (oui/non): ").strip().lower()
            if use_default_g == 'non':
                g = float(input("Entrez la gravite (g): "))
            else:
                g = 9.81
            m = masse_from_poids(P, g)
            print("La masse est", m, "unites de masse.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 9:
            P = float(input("Entrez le poids (P): "))
            m = float(input("Entrez la masse (m): "))
            g = gravite(P, m)
            print("La gravite est", g, "unites de gravite.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 10:
            m = float(input("Entrez la masse (m): "))
            v = float(input("Entrez la vitesse (v): "))
            E_c = energie_cinetique(m, v)
            print("L'energie cinetique est", E_c, "unites d'energie.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 11:
            E_c = float(input("Entrez l'energie cinetique (E_c): "))
            v = float(input("Entrez la vitesse (v): "))
            m = masse_from_energie_cinetique(E_c, v)
            print("La masse est", m, "unites de masse.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 12:
            E_c = float(input("Entrez l'energie cinetique (E_c): "))
            m = float(input("Entrez la masse (m): "))
            v = vitesse_from_energie_cinetique(E_c, m)
            print("La vitesse est", v, "unites de vitesse.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 13:
            i = float(input("Entrez le courant (I): "))
            r = float(input("Entrez la resistance (R): "))
            u = loi_ohm_u(i, r)
            print("La tension est", u, "volts.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 14:
            u = float(input("Entrez la tension (U): "))
            r = float(input("Entrez la resistance (R): "))
            i = loi_ohm_i(u, r)
            print("Le courant est", i, "amperes.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 15:
            u = float(input("Entrez la tension (U): "))
            i = float(input("Entrez le courant (I): "))
            r = loi_ohm_r(u, i)
            print("La resistance est", r, "ohms.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 16:
            u = float(input("Entrez la tension (U): "))
            i = float(input("Entrez le courant (I): "))
            p = puissance_p(u, i)
            print("La puissance est", p, "watts.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 17:
            p = float(input("Entrez la puissance (P): "))
            i = float(input("Entrez le courant (I): "))
            u = puissance_u(p, i)
            print("La tension est", u, "volts.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 18:
            p = float(input("Entrez la puissance (P): "))
            u = float(input("Entrez la tension (U): "))
            i = puissance_i(p, u)
            print("Le courant est", i, "amperes.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 19:
            p = float(input("Entrez la puissance (P): "))
            t = float(input("Entrez le temps (t): "))
            e = energie_e(p, t)
            print("L'energie est", e, "joules.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 20:
            e = float(input("Entrez l'energie (E): "))
            t = float(input("Entrez le temps (t): "))
            p = energie_p(e, t)
            print("La puissance est", p, "watts.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 21:
            e = float(input("Entrez l'energie (E): "))
            p = float(input("Entrez la puissance (P): "))
            t = energie_t(e, p)
            print("Le temps est", t, "secondes.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 22:
            n2 = float(input("Entrez l'indice de refraction n2: "))
            angle2 = float(input("Entrez l'angle de refraction (angle2) en degres: "))
            angle1 = float(input("Entrez l'angle d'incidence (angle1) en degres: "))
            n1 = snell_descartes_n1(n2, angle2, angle1)
            print("L'indice de refraction n1 est", n1)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 23:
            n1 = float(input("Entrez l'indice de refraction n1: "))
            angle1 = float(input("Entrez l'angle d'incidence (angle1) en degres: "))
            angle2 = float(input("Entrez l'angle de refraction (angle2) en degres: "))
            n2 = snell_descartes_n2(n1, angle1, angle2)
            print("L'indice de refraction n2 est", n2)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 24:
            n1 = float(input("Entrez l'indice de refraction n1: "))
            n2 = float(input("Entrez l'indice de refraction n2: "))
            angle2 = float(input("Entrez l'angle de refraction (angle2) en degres: "))
            angle1 = snell_descartes_angle1(n1, n2, angle2)
            print("L'angle d'incidence (angle1) est", angle1, "degres.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 25:
            n1 = float(input("Entrez l'indice de refraction n1: "))
            n2 = float(input("Entrez l'indice de refraction n2: "))
            angle1 = float(input("Entrez l'angle d'incidence (angle1) en degres: "))
            angle2 = snell_descartes_angle2(n1, n2, angle1)
            print("L'angle de refraction (angle2) est", angle2, "degres.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 26:
            masse_solute = float(input("Entrez la masse du solute (m): "))
            volume_solution = float(input("Entrez le volume de la solution (V): "))
            concentration = concentration_masse(masse_solute, volume_solution)
            print("La concentration en masse est", concentration, "unites de masse par unite de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 27:
            concentration = float(input("Entrez la concentration en masse (C): "))
            volume_solution = float(input("Entrez le volume de la solution (V): "))
            masse_solute = masse_solute(concentration, volume_solution)
            print("La masse du solute est", masse_solute, "unites de masse.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 28:
            masse_solute = float(input("Entrez la masse du solute (m): "))
            concentration = float(input("Entrez la concentration en masse (C): "))
            volume_solution = volume_solution(masse_solute, concentration)
            print("Le volume de la solution est", volume_solution, "unites de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 29:
            c_initiale = float(input("Entrez la concentration initiale (C_initiale): "))
            v_initiale = float(input("Entrez le volume initial (V_initiale): "))
            v_finale = float(input("Entrez le volume final (V_finale): "))
            c_finale = concentration_dilution(c_initiale, v_initiale, v_finale)
            print("La concentration finale est", c_finale, "unites de concentration.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 30:
            c_initiale = float(input("Entrez la concentration initiale (C_initiale): "))
            c_finale = float(input("Entrez la concentration finale (C_finale): "))
            v_finale = float(input("Entrez le volume final (V_finale): "))
            v_initiale = volume_initial(c_initiale, v_finale, c_finale)
            print("Le volume initial est", v_initiale, "unites de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 31:
            c_initiale = float(input("Entrez la concentration initiale (C_initiale): "))
            v_initiale = float(input("Entrez le volume initial (V_initiale): "))
            c_finale = float(input("Entrez la concentration finale (C_finale): "))
            v_finale = volume_final(c_initiale, v_initiale, c_finale)
            print("Le volume final est", v_finale, "unites de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 32:
            valeur = float(input("Entrez la valeur de la vitesse: "))
            unite_source = input("Entrez l'unite source (m/s, km/h, mi/h): ")
            unite_cible = input("Entrez l'unite cible (m/s, km/h, mi/h): ")
            resultat = convertir_vitesse(valeur, unite_source, unite_cible)
            print("La vitesse convertie est", resultat, unite_cible)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 33:
            valeur = float(input("Entrez la valeur du temps: "))
            unite_source = input("Entrez l'unite source (s, min, h): ")
            unite_cible = input("Entrez l'unite cible (s, min, h): ")
            resultat = convertir_temps(valeur, unite_source, unite_cible)
            print("Le temps converti est", resultat, unite_cible)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 34:
            valeur = float(input("Entrez la valeur du volume: "))
            unite_source = input("Entrez l'unite source (m^3, L, cm^3): ")
            unite_cible = input("Entrez l'unite cible (m^3, L, cm^3): ")
            resultat = convertir_volume(valeur, unite_source, unite_cible)
            print("Le volume converti est", resultat, unite_cible)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 35:
            valeur = float(input("Entrez la valeur de l'aire: "))
            unite_source = input("Entrez l'unite source (m^2, cm^2, mm^2): ")
            unite_cible = input("Entrez l'unite cible (m^2, cm^2, mm^2): ")
            resultat = convertir_aire(valeur, unite_source, unite_cible)
            print("L'aire convertie est", resultat, unite_cible)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 36:
            valeur = float(input("Entrez la valeur de la masse volumique: "))
            unite_source = input("Entrez l'unite source (kg/m^3, g/cm^3, mg/mm^3): ")
            unite_cible = input("Entrez l'unite cible (kg/m^3, g/cm^3, mg/mm^3): ")
            resultat = convertir_masse_volumique(valeur, unite_source, unite_cible)
            print("La masse volumique convertie est", resultat, unite_cible)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 37:
            valeur = float(input("Entrez la valeur a convertir:"))
            print("1. Giga")
            print("2. Méga")
            print("3. Kilo")
            print("4. Hecto")
            print("5. Deca")
            print("6. Base")
            print("7. Déci")
            print("8. centi")
            print("9. milli")
            unite_source = input("Entrez l'unitée source:")
            try:
                unite_source = int(unite_source)
            except:
                print("valeur incorecte")
            print("1. Giga")
            print("2. Méga")
            print("3. Kilo")
            print("4. Hecto")
            print("5. Deca")
            print("6. Base")
            print("7. Déci")
            print("8. centi")
            print("9. milli")
            unite_cible = input("Entrez l'unitée cible:")
            try:
                unite_cible = int(unite_cible)
            except:
                print("valeur incorecte")
            resultat = conv(valeur,unite_cible,unite_source)
            print("La valeur convertie est :", resultat)
            input("appuyer sur 1 pour continuer...")
        elif choix == 38: 
            print("Pour suggerer quelque chose au developeur, allez sur ce lien :")
            print(" https://github.com/llv-devpy\n/Formules-physique.py/issues")
            print(" et creez y un issue.")
            input("appuyer sur 1 pour continuer...")
                    
        else:
            print("Choix invalide.")
            main()

main()