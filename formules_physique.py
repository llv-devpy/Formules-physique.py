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

# Formules d'électricité
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

def main():
    while True:
        print("1. Calculer la vitesse")
        print("2. Calculer la distance")
        print("3. Calculer le temps")
        print("4. Calculer la masse volumique")
        print("5. Calculer la masse")
        print("6. Calculer le volume")
        print("7. Calculer le poids")
        print("8. Calculer la masse à partir du poids")
        print("9. Calculer la gravité")
        print("38. Suivant")
        choix = input("Entrez votre choix: ")
        try: 
            choix = int(choix)
        except ValueError:
            print("Choix invalide.")
            main()

        if choix < 1 or choix > 9 and choix != 38:
            print("Choix invalide.")
            main()

        elif choix == 38:
            print("10. Calculer l'énergie cinétique")
            print("11. Calculer la masse à partir de l'énergie cinétique")
            print("12. Calculer la vitesse à partir de l'énergie cinétique")
            print("13. Calculer la tension")
            print("14. Calculer le courant")
            print("15. Calculer la résistance")
            print("16. Calculer la puissance")
            print("17. Calculer la tension")
            print("18. Calculer le courant")
            print("38. Suivant")
            choix = input("Entrez votre choix: ")
            try:
                choix = int(choix)
            except ValueError:
                print("Choix invalide")
                main()

            if choix < 10 or choix > 18 and choix != 38:
                print("Choix invalide.")
                main()
            elif choix == 38:
                print("19. Calculer l'énergie")
                print("20. Calculer la puissance")
                print("21. Calculer le temps")
                print("22. Calculer l'indice de réfraction n1")
                print("23. Calculer l'indice de réfraction n2")
                print("24. Calculer l'angle d'incidence")
                print("25. Calculer l'angle de réfraction")
                print("26. Calculer la concentration en masse")
                print("27. Calculer la masse du soluté")
                print("38. Suivant")
                choix = input("Entrez votre choix: ")
                try:
                    choix = int(choix)
                except ValueError:
                    print("Choix invalide")
                    main()

                if choix < 19 or choix > 27 and choix != 38:
                    print("Choix invalide.")
                    main()
                elif choix == 38:
                    print("28. Calculer le volume de la solution")
                    print("29. Calculer la concentration finale")
                    print("30. Calculer le volume initial")
                    print("31. Calculer le volume final")
                    print("32. Convertir la vitesse")
                    print("33. Convertir le temps")
                    print("34. Convertir le volume")
                    print("35. Convertir l'aire")
                    print("36. Convertir la masse volumique")
                    print("37. retour au debut")
                    choix = input("Entrez votre choix: ")
                    try:
                        choix = int(choix)
                    except ValueError:
                        print("Choix invalide")
                        main()
                    if choix < 28 or choix > 36 and choix != 38:
                        print("Choix invalide.")
                        main()
                    elif choix == 37:
                        main()
        


        if choix == 1:
            d = float(input("Entrez la distance (d): "))
            T = float(input("Entrez le temps (T): "))
            v = vitesse(d, T)
            print("La vitesse est", v, "unités de distance par unité de temps.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 2:
            v = float(input("Entrez la vitesse (v): "))
            T = float(input("Entrez le temps (T): "))
            d = distance(v, T)
            print("La distance est", d, "unités de distance.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 3:
            d = float(input("Entrez la distance (d): "))
            v = float(input("Entrez la vitesse (v): "))
            T = temps(d, v)
            print("Le temps est", T, "unités de temps.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 4:
            m = float(input("Entrez la masse (m): "))
            V = float(input("Entrez le volume (V): "))
            ρ = masse_volumique(m, V)
            print("La masse volumique est", ρ, "unités de masse par unité de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 5:
            ρ = float(input("Entrez la masse volumique (ρ): "))
            V = float(input("Entrez le volume (V): "))
            m = masse(ρ, V)
            print("La masse est", m, "unités de masse.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 6:
            m = float(input("Entrez la masse (m): "))
            ρ = float(input("Entrez la masse volumique (ρ): "))
            V = volume(m, ρ)
            print("Le volume est", V, "unités de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 7:
            m = float(input("Entrez la masse (m): "))
            use_default_g = input("Voulez-vous utiliser la gravité par défaut (9.81) ? (oui/non): ").strip().lower()
            if use_default_g == 'non':
                g = float(input("Entrez la gravité (g): "))
            else:
                g = 9.81
            P = poids(m, g)
            print("Le poids est", P, "unités de force.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 8:
            P = float(input("Entrez le poids (P): "))
            use_default_g = input("Voulez-vous utiliser la gravité par défaut (9.81) ? (oui/non): ").strip().lower()
            if use_default_g == 'non':
                g = float(input("Entrez la gravité (g): "))
            else:
                g = 9.81
            m = masse_from_poids(P, g)
            print("La masse est", m, "unités de masse.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 9:
            P = float(input("Entrez le poids (P): "))
            m = float(input("Entrez la masse (m): "))
            g = gravite(P, m)
            print("La gravité est", g, "unités de gravité.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 10:
            m = float(input("Entrez la masse (m): "))
            v = float(input("Entrez la vitesse (v): "))
            E_c = energie_cinetique(m, v)
            print("L'énergie cinétique est", E_c, "unités d'énergie.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 11:
            E_c = float(input("Entrez l'énergie cinétique (E_c): "))
            v = float(input("Entrez la vitesse (v): "))
            m = masse_from_energie_cinetique(E_c, v)
            print("La masse est", m, "unités de masse.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 12:
            E_c = float(input("Entrez l'énergie cinétique (E_c): "))
            m = float(input("Entrez la masse (m): "))
            v = vitesse_from_energie_cinetique(E_c, m)
            print("La vitesse est", v, "unités de vitesse.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 13:
            i = float(input("Entrez le courant (I): "))
            r = float(input("Entrez la résistance (R): "))
            u = loi_ohm_u(i, r)
            print("La tension est", u, "volts.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 14:
            u = float(input("Entrez la tension (U): "))
            r = float(input("Entrez la résistance (R): "))
            i = loi_ohm_i(u, r)
            print("Le courant est", i, "ampères.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 15:
            u = float(input("Entrez la tension (U): "))
            i = float(input("Entrez le courant (I): "))
            r = loi_ohm_r(u, i)
            print("La résistance est", r, "ohms.")
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
            print("Le courant est", i, "ampères.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 19:
            p = float(input("Entrez la puissance (P): "))
            t = float(input("Entrez le temps (t): "))
            e = energie_e(p, t)
            print("L'énergie est", e, "joules.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 20:
            e = float(input("Entrez l'énergie (E): "))
            t = float(input("Entrez le temps (t): "))
            p = energie_p(e, t)
            print("La puissance est", p, "watts.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 21:
            e = float(input("Entrez l'énergie (E): "))
            p = float(input("Entrez la puissance (P): "))
            t = energie_t(e, p)
            print("Le temps est", t, "secondes.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 22:
            n2 = float(input("Entrez l'indice de réfraction n2: "))
            angle2 = float(input("Entrez l'angle de réfraction (angle2) en degrés: "))
            angle1 = float(input("Entrez l'angle d'incidence (angle1) en degrés: "))
            n1 = snell_descartes_n1(n2, angle2, angle1)
            print("L'indice de réfraction n1 est", n1)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 23:
            n1 = float(input("Entrez l'indice de réfraction n1: "))
            angle1 = float(input("Entrez l'angle d'incidence (angle1) en degrés: "))
            angle2 = float(input("Entrez l'angle de réfraction (angle2) en degrés: "))
            n2 = snell_descartes_n2(n1, angle1, angle2)
            print("L'indice de réfraction n2 est", n2)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 24:
            n1 = float(input("Entrez l'indice de réfraction n1: "))
            n2 = float(input("Entrez l'indice de réfraction n2: "))
            angle2 = float(input("Entrez l'angle de réfraction (angle2) en degrés: "))
            angle1 = snell_descartes_angle1(n1, n2, angle2)
            print("L'angle d'incidence (angle1) est", angle1, "degrés.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 25:
            n1 = float(input("Entrez l'indice de réfraction n1: "))
            n2 = float(input("Entrez l'indice de réfraction n2: "))
            angle1 = float(input("Entrez l'angle d'incidence (angle1) en degrés: "))
            angle2 = snell_descartes_angle2(n1, n2, angle1)
            print("L'angle de réfraction (angle2) est", angle2, "degrés.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 26:
            masse_solute = float(input("Entrez la masse du soluté (m): "))
            volume_solution = float(input("Entrez le volume de la solution (V): "))
            concentration = concentration_masse(masse_solute, volume_solution)
            print("La concentration en masse est", concentration, "unités de masse par unité de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 27:
            concentration = float(input("Entrez la concentration en masse (C): "))
            volume_solution = float(input("Entrez le volume de la solution (V): "))
            masse_solute = masse_solute(concentration, volume_solution)
            print("La masse du soluté est", masse_solute, "unités de masse.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 28:
            masse_solute = float(input("Entrez la masse du soluté (m): "))
            concentration = float(input("Entrez la concentration en masse (C): "))
            volume_solution = volume_solution(masse_solute, concentration)
            print("Le volume de la solution est", volume_solution, "unités de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 29:
            c_initiale = float(input("Entrez la concentration initiale (C_initiale): "))
            v_initiale = float(input("Entrez le volume initial (V_initiale): "))
            v_finale = float(input("Entrez le volume final (V_finale): "))
            c_finale = concentration_dilution(c_initiale, v_initiale, v_finale)
            print("La concentration finale est", c_finale, "unités de concentration.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 30:
            c_initiale = float(input("Entrez la concentration initiale (C_initiale): "))
            c_finale = float(input("Entrez la concentration finale (C_finale): "))
            v_finale = float(input("Entrez le volume final (V_finale): "))
            v_initiale = volume_initial(c_initiale, v_finale, c_finale)
            print("Le volume initial est", v_initiale, "unités de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 31:
            c_initiale = float(input("Entrez la concentration initiale (C_initiale): "))
            v_initiale = float(input("Entrez le volume initial (V_initiale): "))
            c_finale = float(input("Entrez la concentration finale (C_finale): "))
            v_finale = volume_final(c_initiale, v_initiale, c_finale)
            print("Le volume final est", v_finale, "unités de volume.")
            input("Appuyez sur 1 pour continuer...")
        elif choix == 32:
            valeur = float(input("Entrez la valeur de la vitesse: "))
            unite_source = input("Entrez l'unité source (m/s, km/h, mi/h): ")
            unite_cible = input("Entrez l'unité cible (m/s, km/h, mi/h): ")
            resultat = convertir_vitesse(valeur, unite_source, unite_cible)
            print("La vitesse convertie est", resultat, unite_cible)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 33:
            valeur = float(input("Entrez la valeur du temps: "))
            unite_source = input("Entrez l'unité source (s, min, h): ")
            unite_cible = input("Entrez l'unité cible (s, min, h): ")
            resultat = convertir_temps(valeur, unite_source, unite_cible)
            print("Le temps converti est", resultat, unite_cible)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 34:
            valeur = float(input("Entrez la valeur du volume: "))
            unite_source = input("Entrez l'unité source (m^3, L, cm^3): ")
            unite_cible = input("Entrez l'unité cible (m^3, L, cm^3): ")
            resultat = convertir_volume(valeur, unite_source, unite_cible)
            print("Le volume converti est", resultat, unite_cible)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 35:
            valeur = float(input("Entrez la valeur de l'aire: "))
            unite_source = input("Entrez l'unité source (m^2, cm^2, mm^2): ")
            unite_cible = input("Entrez l'unité cible (m^2, cm^2, mm^2): ")
            resultat = convertir_aire(valeur, unite_source, unite_cible)
            print("L'aire convertie est", resultat, unite_cible)
            input("Appuyez sur 1 pour continuer...")
        elif choix == 36:
            valeur = float(input("Entrez la valeur de la masse volumique: "))
            unite_source = input("Entrez l'unité source (kg/m^3, g/cm^3, mg/mm^3): ")
            unite_cible = input("Entrez l'unité cible (kg/m^3, g/cm^3, mg/mm^3): ")
            resultat = convertir_masse_volumique(valeur, unite_source, unite_cible)
            print("La masse volumique convertie est", resultat, unite_cible)
            input("Appuyez sur 1 pour continuer...")
        else:
            print("Choix invalide.")

main()

