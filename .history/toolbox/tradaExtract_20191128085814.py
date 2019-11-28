from bs4 import BeautifulSoup

arr = [['#', 'clienteEstado', 'warehouseId', 'Pendentes', 'de', 'integrao'], ['1', 'SP', '2404', '48'], ['2', 'SP', '2462', '10'], ['3', 'SP', '7100', '7'], ['4', 'MG', 'BR19_A002', '6'], ['5', 'SP', 'BR19_A002', '6'], ['6', 'PE', 'BR19_A002', '5'], ['7', 'SP', '2444', '3'], ['8', 'MG', '7100', '2'], ['9', 'RJ', 'BR19_A002', '2'], ['10', 'BA', 'BR19_A002', '2'], ['11', 'MG', '0', '1'], ['12', 'SP', '7134', '1'], ['13', 'SP', '7136', '1'], ['14', 'SP', 'BR1F_A002', '1']]

soup = BeautifulSoup(arr).encode("utf-8")
print(arr)