import requests
import PySimpleGUI as sg

# funcao para buscar os dados do cep informado.
def solicitar_endereco_data(cep):    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()
    return data

sg.theme("DarkBrown")

layout = [
    [sg.Text("CEP:"), sg.Input(key="-CEP-")],
    [sg.Button("Buscar"), sg.Button("Sair")],
    [sg.Text(size=(50, 10), key="-OUTPUT-")]
]

# criacao da janela
window = sg.Window("Consulta de CEP", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    elif event == "Buscar":
        cep = values["-CEP-"]
        data = solicitar_endereco_data(cep)
        if "erro" not in data:
            output = f"CEP: {data['cep']}\n"
            output += f"Logradouro: {data['logradouro']}\n"
            output += f"Complemento: {data['complemento']}\n"
            output += f"Bairro: {data['bairro']}\n"
            output += f"Cidade: {data['localidade']}\n"
            output += f"Estado: {data['uf']}\n"
        else:
            output = "CEP não encontrado."
        window["-OUTPUT-"].update(output)

window.close()