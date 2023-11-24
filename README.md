# Redimensionando Dados

- O dado bruto nesse dataset é a matriz [9][57024]
- A primeira dimensão são os eletrodos e a segunda são as amostragens de tempo

A última linha da matriz bruta é uma linha majoritariamente composta por zeros, mas os pontos onde ela é diferente de zero são os pontos que queremos encontrar.

Depois de encontrarmos e filtrarmos esses pontos podemos redimensionar a matriz com o mne.Epochs, formando uma matrix tridimensional [32][8][512]. Sendo a primeira dimensão, o [32], os pontos diferentes de 0 na última linha da matriz bruta.

- A primeira dimensão são os pensamentos do participante e a segunda e terceira ([8][512]) são o tempo
- Ou seja, [32][8][512] significa 32 pensamentos que foram adquiridos, cada, através de 8 eletrodos num período de 2 segundos (a frequência é 256Hz, logo 512 amostras de tempo são 2 segundos)

