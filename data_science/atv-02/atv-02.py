from pandas import read_excel


file_name = 'jogar-tenis.xlsx' # change it to the name of your excel file
df = read_excel(file_name, engine='openpyxl')

def getValues(colum1, cond1, colum2, cond2):
    count = 0
    for i, cond_1 in enumerate(df[colum1]):
        for j, cond_2 in enumerate(df[colum2]):
            if cond_2 == cond2 and cond_1 == cond1 and i == j:
                count += 1
                break
    return count

def getProba(dias, cond):
    if dias != 0:
        return cond / dias
    else:
        return 0

# Jogar tênis
dias = len(df.index)
jogar_sim = df['Jogar'].map(lambda value: value == 'Sim').sum()
ensolarado = getValues('Jogar', 'Sim', 'Tempo', 'Ensolarado')
temperatura = getValues('Jogar', 'Sim', 'Temperatura', 'Intermediaria')
umidade = getValues('Jogar', 'Sim', 'Umidade', 'Alta')
vento_forte = getValues('Jogar', 'Sim', 'Vento', 'Forte')

pb_ensolarado = getProba(dias, ensolarado)
pb_temp_moderd = getProba(dias, temperatura)
pb_umid_alta = getProba(dias, umidade)
pb_vent_fort = getProba(dias, vento_forte)
pb_jogar_tenis = getProba(dias, jogar_sim)

jogar_tenis_final = pb_ensolarado * pb_jogar_tenis * pb_temp_moderd * pb_umid_alta * pb_vent_fort
print(f'Jogar Tênis: {jogar_tenis_final}')

#--------------------------------------------------------------
# Não jogar tênis
n_dias = dias - jogar_sim  #14 - 9
pb_ensolarado_n_jogar = getProba(n_dias, ensolarado)
pb_temp_moderd_n_jogar = getProba(n_dias, temperatura)
pb_umid_alta_n_jogar = getProba(n_dias, umidade)
pb_vent_fort_n_jogar = getProba(n_dias, vento_forte)
pb_n_jogar_tenis = getProba(n_dias, jogar_sim)

n_jogar_tenis_final = pb_ensolarado_n_jogar * pb_n_jogar_tenis * pb_temp_moderd_n_jogar * pb_umid_alta_n_jogar * pb_vent_fort_n_jogar
print(f'Não Jogar Tênis: {n_jogar_tenis_final}')
