import sqlite3

import pandas as pd
import pandas.core.frame

Autor = ['sun izu', 'Fernando Pessoa', 'Thomas Mann', 'João Guimarães Rosa']

Livro = ['A Arte Da Guerra', 'Poesias Selecionadas', 'A Montanha Mágica', 'pRIMEIRAS Estorías']

Ano= {2000, 2004, 2015,2017}

Autor = list(Autor)  # Convert set to list if Autor is a set
Livro = list(Livro)  # Convert set to list if Livro is a set
Ano = list(Ano)      # Convert set to list if Ano is a set

df = pd.DataFrame({
    'Autor': Autor,
    'Livro': Livro,
    'Ano': Ano
})

print(df.index)
df.index






#series_objeto = pd.Series([1, 7, 9, 13, 17, 99])
#print(series_objeto)
#series_objeto2= pd.Series([4, 7, 8, -2], index = ['alfa', 'beta', 'teta', 'gama'])
#print(series_objeto2)

# Connect to the database
con = sqlite3.connect("juntandocompython.bd")

# Create a cursor object
cur = con.cursor()

# Create the table 'contato'
cur.execute("CREATE TABLE IF NOT EXISTS contato(nome TEXT, endereco TEXT, telefone TEXT)")

# Execute a query to get the table names
res = cur.execute("SELECT name FROM sqlite_master")

# Fetch the first result
#print(res.fetchone())  # Should print ('contato',) if the table was created successfully










#nome_cidade= pd.Series(['Maringa', 'Itabira', 'Uberlândia','Salvador','Fortaleza'])
#populacao = pd.Series ([403.604,120.903,699.807, 2.886698,2.686612])

#df=pd.DataFrame({"Cidade": nome_cidade, "População":populacao})

#populacao_cidades = dict(zip(nome_cidade,populacao))

#populacao_cidades['Vitoria'] = 365.855
#del populacao_cidades['Fortaleza']

#type(populacao_cidades)

#print(populacao_cidades)
