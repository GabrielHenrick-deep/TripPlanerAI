import google.generativeai as genai

genai.configure(api_key="your_key")

# Iniciar conversa com o modelo Gemini
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Função para coletar informações do usuário
def obter_informacoes():
    destino = input("Qual é o destino desejado? ")
    datas = input("Quais são as datas da viagem? ")
    pessoas = int(input("Quantas pessoas estarão viajando? "))
    interesses = input("Quais são seus interesses (praias, cultura, natureza, etc.)? ")
    orcamento = float(input("Qual é o seu orçamento para a viagem? "))

    return destino, datas, pessoas, interesses, orcamento

# Função para interagir com o modelo Gemini
def conversar(texto):
    return chat.send_message(texto).text

# Função para buscar informações sobre o destino
def buscar_informacoes(destino):
    return conversar(f"Informe-me sobre {destino}")

# Função para buscar opções de voos
def buscar_opcoes_de_voos(destino, datas, pessoas):
    return conversar(f"Busque opções de voos para {destino} em {datas} para {pessoas} pessoas")

# Função para buscar opções de hotéis
def buscar_opcoes_de_hoteis(destino, datas, pessoas, orcamento):
    return conversar(f"Encontre opções de hotéis em {destino} para {datas} para {pessoas} pessoas com um orçamento de {orcamento}")

# Função para sugerir roteiros personalizados
def sugerir_roteiros(destino, datas, interesses):
    return conversar(f"Sugira roteiros personalizados para {destino} em {datas} com base nos interesses em {interesses}")

# Função para organizar reservas
def organizar_reservas():
    return conversar("Organize as reservas para voos e hotéis")

# Função para oferecer recursos adicionais
def oferecer_recursos_adicionais():
    return conversar("Ofereça recursos adicionais, como conversão de moeda, tradução de frases, previsão do tempo e dicas de viagem")

# Função principal
def main():
    print("#" * 50)
    print("Bem-vindo ao Planejador de Viagens!")
    print("#" * 50)

    destino, datas, pessoas, interesses, orcamento = obter_informacoes()

    print("\nBuscando informações sobre o destino...")
    informacoes_destino = buscar_informacoes(destino)
    print("Informações sobre o destino:", informacoes_destino)

    print("\nBuscando opções de voos...")
    opcoes_voos = buscar_opcoes_de_voos(destino, datas, pessoas)
    print("Opções de voos encontradas:", opcoes_voos)

    print("\nBuscando opções de hotéis...")
    opcoes_hoteis = buscar_opcoes_de_hoteis(destino, datas, pessoas, orcamento)
    print("Opções de hotéis encontradas:", opcoes_hoteis)

    print("\nSugerindo roteiros personalizados...")
    roteiros = sugerir_roteiros(destino, datas, interesses)
    print("Roteiros sugeridos:", roteiros)

    print("\nOrganizando reservas...")
    organizar_reservas()

    print("\nOferecendo recursos adicionais...")
    recursos_adicionais = oferecer_recursos_adicionais()
    print("Recursos adicionais oferecidos:", recursos_adicionais)

    print("\nEncerrando Chat")

if __name__ == "__main__":
    main()
