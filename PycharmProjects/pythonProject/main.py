import pandas as panda
import twilio as twi
import openpyxl as openx

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC961d6efceac948909a51ea894519ba6b"
# Your Auth Token from twilio.com/console
auth_token  = "150f05dbb04b9e14a0dd028271f76623 "

client = Client(account_sid, auth_token)
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:

    tabela_vendas = panda.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 50000).any():
        vendedor=tabela_vendas.loc[tabela_vendas['Vendas'] > 50000, 'Vendedor'].values[0]
        venda = tabela_vendas.loc[tabela_vendas['Vendas'] > 50000,'Vendas'].values[0]
        print(f"No mes de {mes} o vendendor {vendedor} vendeu {venda}")
        message = client.messages.create(
            to="+(CAIXAPOSTAL)(DDD)(NUMERO)",
            #TUDO SEM PARENTESES
            from_="+19285507135",
            body=f"No mes de {mes} o vendendor {vendedor} vendeu {venda}")

        print(message.sid)
        #print(f"no mes de {mes} encontrou alguem com mais de 55k de venda.")
