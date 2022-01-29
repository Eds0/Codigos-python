time = ('Flamengo','Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense','Grêmio','Palmeiras', \
    'Santos','Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO','Bahia','Sport', \
    'Fortaleza', 'Vasco',  'Goiás', 'Coritiba', 'Botafogo')
print('-'*130)
print(f'A tabeça final do brasileirão 2020 ficou: {time}')
print('-'*130)
print(f'Os cinco primeiros colocados do brasileirão 2020 foram {time[:5]}')
print('-'*130)
print(f'Os times rebaixados do brasileirão 2020 foram {time[-4:]}')
print('-'*130)
print(f'Os times em ordem alfabéticas do brasileirão 2020 foram {sorted(time)}')
print('-'*130)
print(f'O Sao Paulo está na {time.index("São Paulo")+1}° posição')