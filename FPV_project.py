import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pi = math.pi

def deg_to_rad(theta):
    return theta * (2 * pi) / 360

def rad_to_deg(theta):
    return theta * 360 / (2 * pi)

lake_poma_frame = pd.read_csv('lake_poma.csv')
lake_rubino_frame = pd.read_csv('lake_rubino.csv')
lake_trinita_frame = pd.read_csv('lake_trinita.csv')
lake_arancio_frame = pd.read_csv('lake_arancio.csv')
lake_giovanni_frame = pd.read_csv('lake_giovanni.csv')
lake_villarosa_frame = pd.read_csv('lake_villarosa.csv')
lake_nicoletti_frame = pd.read_csv('lake_nicoletti.csv')
lake_comunelli_frame = pd.read_csv('lake_comunelli.csv')
lake_disueri_frame = pd.read_csv('lake_disueri.csv')


lake_poma = []
lake_rubino = []
lake_trinita = []
lake_arancio = []
lake_giovanni = []
lake_villarosa = []
lake_nicoletti = []
lake_comunelli = []
lake_disueri = []

for i in range(len(lake_poma_frame)):
    lake_poma.append(np.array(lake_poma_frame['Days'])[i])
    lake_poma.append(np.array(lake_poma_frame['Longitude'])[i])
    lake_poma.append(np.array(lake_poma_frame['Latitude'])[i])
    lake_poma.append(np.array(lake_poma_frame['Tilt'])[i])
    lake_poma.append(np.array(lake_poma_frame['DNI'])[i])
    lake_poma.append(np.array(lake_poma_frame['GHI'])[i])
    lake_rubino.append(np.array(lake_rubino_frame['Days'])[i])
    lake_rubino.append(np.array(lake_rubino_frame['Longitude'])[i])
    lake_rubino.append(np.array(lake_rubino_frame['Latitude'])[i])
    lake_rubino.append(np.array(lake_rubino_frame['Tilt'])[i])
    lake_rubino.append(np.array(lake_rubino_frame['DNI'])[i])
    lake_rubino.append(np.array(lake_rubino_frame['GHI'])[i])
    lake_trinita.append(np.array(lake_trinita_frame['Days'])[i])
    lake_trinita.append(np.array(lake_trinita_frame['Longitude'])[i])
    lake_trinita.append(np.array(lake_trinita_frame['Latitude'])[i])
    lake_trinita.append(np.array(lake_trinita_frame['Tilt'])[i])
    lake_trinita.append(np.array(lake_trinita_frame['DNI'])[i])
    lake_trinita.append(np.array(lake_trinita_frame['GHI'])[i])
    lake_arancio.append(np.array(lake_arancio_frame['Days'])[i])
    lake_arancio.append(np.array(lake_arancio_frame['Longitude'])[i])
    lake_arancio.append(np.array(lake_arancio_frame['Latitude'])[i])
    lake_arancio.append(np.array(lake_arancio_frame['Tilt'])[i])
    lake_arancio.append(np.array(lake_arancio_frame['DNI'])[i])
    lake_arancio.append(np.array(lake_arancio_frame['GHI'])[i])
    lake_giovanni.append(np.array(lake_giovanni_frame['Days'])[i])
    lake_giovanni.append(np.array(lake_giovanni_frame['Longitude'])[i])
    lake_giovanni.append(np.array(lake_giovanni_frame['Latitude'])[i])
    lake_giovanni.append(np.array(lake_giovanni_frame['Tilt'])[i])
    lake_giovanni.append(np.array(lake_giovanni_frame['DNI'])[i])
    lake_giovanni.append(np.array(lake_giovanni_frame['GHI'])[i])
    lake_villarosa.append(np.array(lake_villarosa_frame['Days'])[i])
    lake_villarosa.append(np.array(lake_villarosa_frame['Longitude'])[i])
    lake_villarosa.append(np.array(lake_villarosa_frame['Latitude'])[i])
    lake_villarosa.append(np.array(lake_villarosa_frame['Tilt'])[i])
    lake_villarosa.append(np.array(lake_villarosa_frame['DNI'])[i])
    lake_villarosa.append(np.array(lake_villarosa_frame['GHI'])[i])
    lake_nicoletti.append(np.array(lake_nicoletti_frame['Days'])[i])
    lake_nicoletti.append(np.array(lake_nicoletti_frame['Longitude'])[i])
    lake_nicoletti.append(np.array(lake_nicoletti_frame['Latitude'])[i])
    lake_nicoletti.append(np.array(lake_nicoletti_frame['Tilt'])[i])
    lake_nicoletti.append(np.array(lake_nicoletti_frame['DNI'])[i])
    lake_nicoletti.append(np.array(lake_nicoletti_frame['GHI'])[i])
    lake_comunelli.append(np.array(lake_comunelli_frame['Days'])[i])
    lake_comunelli.append(np.array(lake_comunelli_frame['Longitude'])[i])
    lake_comunelli.append(np.array(lake_comunelli_frame['Latitude'])[i])
    lake_comunelli.append(np.array(lake_comunelli_frame['Tilt'])[i])
    lake_comunelli.append(np.array(lake_comunelli_frame['DNI'])[i])
    lake_comunelli.append(np.array(lake_comunelli_frame['GHI'])[i])
    lake_disueri.append(np.array(lake_disueri_frame['Days'])[i])
    lake_disueri.append(np.array(lake_disueri_frame['Longitude'])[i])
    lake_disueri.append(np.array(lake_disueri_frame['Latitude'])[i])
    lake_disueri.append(np.array(lake_disueri_frame['Tilt'])[i])
    lake_disueri.append(np.array(lake_disueri_frame['DNI'])[i])
    lake_disueri.append(np.array(lake_disueri_frame['GHI'])[i])




lakes_info = {
'lake_poma': lake_poma,
'lake_rubino': lake_rubino,
'lake_trinita': lake_trinita,
'lake_arancio': lake_arancio,
'lake_giovanni': lake_giovanni,
'lake_villarosa': lake_villarosa,
'lake_nicoletti': lake_nicoletti,
'lake_comunelli': lake_comunelli,
'lake_disueri': lake_disueri
}

lakes_results = {
'lake_poma': {},
'lake_rubino': {},
'lake_trinita': {},
'lake_arancio': {},
'lake_giovanni': {},
'lake_villarosa': {},
'diga_nicoletti': {},
'lake_comunelli': {},
'lake_disueri': {}
}

lakes_max_irradiances = {
'lake_poma': {},
'lake_rubino': {},
'lake_trinita': {},
'lake_arancio': {},
'lake_giovanni': {},
'lake_villarosa': {},
'diga_nicoletti': {},
'lake_comunelli': {},
'lake_disueri': {}
}

hsc = 1.353

def calcolo_irradianza(lst):
    risultati = []
    length = len(lst)
    for i in range(0, length, 6):
        n = lst[i]
        latitudine = lst[i + 2]
        longitudine = lst[i + 1]
        tilt = lst[i + 3]
        Irradianza = lst[i + 4]
        GHI = lst[i + 5]
        delta = 23.45 * math.sin(deg_to_rad(360 * (284 + n) / 365))
        rb = (math.sin(deg_to_rad(latitudine - tilt)) * math.sin(deg_to_rad(delta))) + math.cos(deg_to_rad(latitudine - tilt)) * math.cos(deg_to_rad(delta)) * math.cos(deg_to_rad(longitudine)) / (math.sin(deg_to_rad(latitudine)) * math.sin(deg_to_rad(delta)) + math.cos(deg_to_rad(latitudine)) * math.cos(deg_to_rad(longitudine)) * math.cos(deg_to_rad(delta)))
        rd = (1 + math.cos(deg_to_rad(tilt))) / 2
        rr = (1 - math.cos(deg_to_rad(tilt))) / 2
        hs = rad_to_deg(math.acos(-1 * math.tan(deg_to_rad(latitudine)) * math.tan(deg_to_rad(delta))))
        ho = ((hsc / pi) * 24) * (1 + 0.033 * math.cos(deg_to_rad(360 * n) / 365)) * ((math.cos(deg_to_rad(latitudine)) * math.cos(deg_to_rad(delta)) * math.sin(deg_to_rad(hs))) + ((((2 * pi) / 360) * hs) * math.sin(deg_to_rad(latitudine)) * math.sin(deg_to_rad(delta))))
        kt = Irradianza / ho
        hd = GHI * ((0.775 + (0.00653 * (hs - 90))) - (0.505 + (0.00455 * (hs - 90))) * (math.cos(deg_to_rad(115 * kt - 103))))
        hdif = GHI * (1 - (1.13 * kt))
        hb = (GHI - hd)
        roh = 0.5
        hr = GHI * roh
        ht = hr * rr + hb * rb + hd * rd
        risultati.append(ht)
        #print('Per il mese di ' + mese + ' l\'irradianza per il valore di angle_max di tilt pari a ' + str(tilt) + ' vale Ht (kWh / m2) ' + str(ht))
    return risultati


mesi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']



def resulting_irradiance(string):
    input = lakes_info[string]
    angoli_tilt = []
    risultati = {}
    angoli = {}
    for i in range(12):
        risultati[mesi[i]] = []
        angoli[mesi[i]] = []
        lakes_results[string][mesi[i]] = []
    for j in range(90):
        angoli_tilt.append(j)
        for k in range(0, len(input), 6):
            input[k + 3] = j
        report = calcolo_irradianza(input)
        for i in range(12):
            risultati[mesi[i]].append(report[i])
            lakes_results[string][mesi[i]].append(report[i])
            angoli[mesi[i]].append(j)

    for i in range(12):
        maximum = 0
        for j in range(len(risultati[mesi[i]])):
            #print('Per il mese di ' + mesi[i] + ' l\'irradianza vale ' + str(risultati[mesi[i]][j]) + ' ad un angle_max di tilt di ' + str(angoli[mesi[i]][j]))
            if maximum < risultati[mesi[i]][j]:
                angle_max = angoli[mesi[i]][j]
                maximum = risultati[mesi[i]][j]
        
        lakes_max_irradiances[mesi[i]] = (angle_max, maximum)
        
    
def print_results(string):

    for i in range(12):
        
        print('The maximum value of tilted solar irradiance on the ' + string + ' for the month ' + mesi[i] + ' happens at a tilt angle ' + str(lakes_max_irradiances[mesi[i]][0]) + ' degrees and the corresponding solar irradiance is ' + str(round(lakes_max_irradiances[mesi[i]][1], 2)))
        
        plt.subplot(4, 3, int(i + 1))
        plt.plot(list(range(90)), lakes_results[string][mesi[i]])
        plt.xlabel('Tilt angles on degrees')
        h = plt.ylabel('GHI tilted (kWh / m2)')
        h.set_rotation(90)
        plt.title(str(mesi[i]))
        plt.subplots_adjust(wspace = 2, hspace = 2)
    plt.show()

strings = ['lake_poma', 'lake_rubino', 'lake_trinita', 'lake_arancio', 'lake_giovanni', 'lake_villarosa', 'lake_nicoletti', 'lake_comunelli', 'lake_disueri']

string = 'lake_poma'
   
resulting_irradiance(string)
print_results(string)
