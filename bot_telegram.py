import telebot
from api.apibot import api_bot

bot = telebot.TeleBot(api_bot)


@bot.message_handler(commands=["Ladingpage"])
def opcao_one_site_ladingpage(mensagem):
    text = """
    Show!
    O valor é $$$$, prazo de 2 semanas.
    É necessário mais informações, um dos nossos técnicos irá entrar em contato.
  """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["Dinamico"])
def opcao_one_site_dinamico(mensagem):
    text = """
    Show!
    O valor é $$$$, prazo de 4 semanas.
    É necessário mais informações, um dos nossos técnicos irá entrar em contato.
  """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["Sim", "Nao"])
def opcao_one_site_tipo(mensagem):
    text = """
    Qual o tipo de site ideal para você?
    /Ladingpage Um site de uma página
    /Dinamico  Site com diversas páginas e com botões
  """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["Site"])
def opcao_two_outro(mensagem):
    text = """
    O site é E-commerce?
    /Sim
    /Nao
  """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["Gerenciamento", "Criar", "Chatbot"])
def opcao_one_sistema_type(mensagem):
    text = """
      Certo, 
      Um dos nossos administradores irá entrar em contato para pegar mais detalhes
    
  """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["Manutencao"])
def opcao_one_manutencao_type(mensagem):
    text = """
      A manutenção é de:
      /Computadores
      /Sites
  """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["Computadores", "Sites"])
def opcao_one_manutencao_type_pc_and_sites(mensagem):
    text = """
    Show!
    Um dos nossos técnicos irá enviar um e-mail pedindo mais detalhes
      
  """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["Sistema"])
def opcao_one_sistema(mensagem):
    text = """
    Existe diversos tipos de sistemas, clique na opção que se encaixe no que você está procurando?
    /Gerenciamento Gerenciamento de um projeto e/ou realizar uma lógica de gerenciamento
    /Criar Realizar uma criação de um sistema de acordo com o cliente deseja
    
  """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["Outro"])
def opcao_one_outro(mensagem):
    text = """
    Qual o produto que encaixa o que está procurando?
    /Sistema
    /Chatbot Criar ou gerenciar um chatbot
    /Manutencao Manutenção de computadores ou de sites 
  """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["opcao1"])
def opcao_one(mensagem):
    text = """
    Qual produto é ideal para você?
      /Site
      /Outro
    """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["Email"])
def opcao_two_email(mensagem):
    text = """
    Ótimo!
    Segue o email de um dos nossos
    administradores:
    Email: admin@admin.com
  """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["WhatsApp"])
def opcao_two_wttp(mensagem):
    text = """
    Ótimo!
    Segue o link para iniciar uma conversa no WhatsApp
    de um dos nossos administradores
    https:/api/whatsapp/99999999
  """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["opcao2"])
def opcao_two(mensagem):
    text = """
    Entrar em contato via:
    /Email
    /WhatsApp
    """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=["opcao3"])
def opcao_three(mensagem):
    text = """
    Caso ainda não conheça os nossos trabalhos
    clique nesses links:
    /link1
    /link2
  """
    bot.send_message(mensagem.chat.id, text)


def verification(mensagem):
    return True


@bot.message_handler(func=verification)
def response(mensagem):
    text = """
    Escolha uma opção para continuar (Clique no item): 
        /opcao1 Fazer um orçamento
        /opcao2 Entrar em contato
        /opcao3 Redes Sociais
        Responder qualquer outra coisa não irá funcionar, clique em uma das opções
    """
    bot.reply_to(mensagem, text)


bot.polling()
