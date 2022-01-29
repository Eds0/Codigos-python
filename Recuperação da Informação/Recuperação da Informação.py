import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt


entrada = open('C:/Users/Dell/Desktop/Jason/camera_wifiCall.json', 'r')
saida = open('C:/Users/Dell/Desktop/Jason/Planilha.xlsx','w')

leitor = pd.read_json