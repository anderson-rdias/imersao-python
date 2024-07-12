# Titulo: Hashizap
# Botão: Iniciar chat
    # popup/modal/alerta
        # Titulo: Bem vindo ao Hashzap
        # Campo de texto: Escreva seu nome no chat
        # Botão: Entrar no chat
        # Sumir com o título e botão inicial
        # Fechar o popup
        # Criar o chat com a mensagem "nome_user entrou no chat"
        # Embaixo do chat:
            # Campo de texto: Digite sua mensagem
            # Botão: Enviar
                # Vai aparecer a mensagem no chat com o nome do user
                # Anderson: salve

# pip install flet

# importar o flet
import flet as ft

# criar a função principal do seu sistema
def main(pagina):
    # criar o título
    titulo = ft.Text("Hashzap")


    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # cria o túnel de comunicação

    titulo_janela = ft.Text("Bem vindo ao Hashzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    def enviar_mensagem(evento):
        # enviar a mensagem no chat: 
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
            # Usuario: mensagem do usuario

        # enviar uma mensagem no tunel
        pagina.pubsub.send_all(texto)
        # limpar o campo de mensagem
        texto_mensagem.value = ""
        pagina.update()

    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    chat = ft.Column()

    # colunas e linhas
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    def entrar_chat(evento):
        # tirar o titulo da página
        pagina.remove(titulo)
        # tirar o botão iniciar
        pagina.remove(botao_iniciar)
        # fechar o popup
        janela.open = False
        # criar o chat
        pagina.add(chat)
        # adicionar a linha de mensagem
        pagina.add(linha_mensagem)

        # escrever a mensagem: usuario entrou no chat
        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou_chat)

        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click= entrar_chat)

    janela = ft.AlertDialog(
        title= titulo_janela, 
        content= campo_nome_usuario, 
        actions= [botao_entrar]
        )
    
    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click= abrir_popup)

    # adicionar o título na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)


# executar o seu sistema
ft.app(main, view= ft.WEB_BROWSER)