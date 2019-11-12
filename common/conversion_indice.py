import pandas as pd

# Conversión de unidades de microgramo/metro_cúbico a ppb(partículas por billón)
def convertir_ppb(row, columna):
    ppb = row[columna] / 1.96
    return ppb


def convertir_ppm(row, columna):
    ppm = row[columna] / 1000
    return ppm


# Cálculo del índice de calidad del aire para el PM10 (usando datos en microgramo/metro_cúbico)
# noinspection PyChainedComparisons,PyChainedComparisons,PyChainedComparisons,PyChainedComparisons,PyChainedComparisons,PyChainedComparisons,PyChainedComparisons
def indice_PM10(row, columna):
    if row[columna] >= 0 and row[columna] <= 40:
        indice = 1.2500 * (row[columna])
        return round(indice)
    if row[columna] >= 41 and row[columna] <= 75:
        indice = (1.4412 * (row[columna] - 41)) + 51
        return round(indice)
    if row[columna] >= 76 and row[columna] <= 214:
        indice = (0.3551 * (row[columna] - 76)) + 101
        return round(indice)
    if row[columna] >= 215 and row[columna] <= 354:
        indice = (0.3525 * (row[columna] - 215)) + 151
        return round(indice)
    if row[columna] >= 355 and row[columna] <= 424:
        indice = (1.4348 * (row[columna] - 355)) + 201
        return round(indice)
    if row[columna] >= 425 and row[columna] <= 504:
        indice = (1.2532 * (row[columna] - 425) + 301)
        return round(indice)
    if row[columna] >= 505 and row[columna] <= 604:
        indice = (1.0000 * (row[columna] - 505) + 401)
        return round(indice)


# Cálculo del índice de calidad del aire para el O3 (usando datos convertidos a ppm)
# noinspection PyChainedComparisons,PyChainedComparisons,PyChainedComparisons,PyChainedComparisons,PyChainedComparisons,PyChainedComparisons,PyChainedComparisons
def indice_O3(row, columna):
    if row[columna] >= 0.000 and row[columna] <= 0.070:
        indice = 714.29 * (row[columna])
        return round(indice)
    if row[columna] >= 0.071 and row[columna] <= 0.095:
        indice = (2041.67 * (row[columna] - 0.071)) + 51
        return round(indice)
    if row[columna] >= 0.096 and row[columna] <= 0.154:
        indice = (844.83 * (row[columna] - 0.096)) + 101
        return round(indice)
    if row[columna] >= 0.155 and row[columna] <= 0.204:
        indice = (1000.00 * (row[columna] - 0.155)) + 151
        return round(indice)
    if row[columna] >= 0.205 and row[columna] <= 0.404:
        indice = (497.49 * (row[columna] - 0.205)) + 201
        return round(indice)
    if row[columna] >= 0.405 and row[columna] <= 0.504:
        indice = (1000.00 * (row[columna] - 0.405) + 301)
        return round(indice)
    if row[columna] >= 0.505 and row[columna] <= 0.604:
        indice = (1000.00 * (row[columna] - 0.505) + 401)
        return round(indice)

# Operar NaN
def no_operar_nan(valor_1, valor_2):
    result=0
    if pd.isnull(valor_1) or pd.isnull(valor_2):
        result=float('NaN')
        return result
    else:
        result= int(round(max(valor_1, valor_2)))
        return result