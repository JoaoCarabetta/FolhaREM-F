# FolhaREM-F
Dados Brutos do Ranking de Eficiência dos Municípios desenvolvido pela Folha.

http://www1.folha.uol.com.br/remf/#/

O repositório tem o scrapper usado para puxar o banco de dados e os dados brutos. 
Se alguém desejar puxar outro dado, basta trocar o element id na função _get_info_:

### Número
>	values.append(element2float(element, 'some_id'))

### Texto
> values.append(element.find_element_by_id('some_id').text.encode('ascii','ignore'))



Os dados no arquivo database.csv são:

## Atendimento 

Abrangência do atendimento da prefeitura (2 x SAUDE + 2 x EDUCACAO + SANEAMENTO) / 5

## Grupo

Grupos dividios pela folha de acordo com a eficiência

1: ineficiente

2: pouco eficiente

3: alguma eficiencia

4: eficiente

# Indice

Valor atribuído pela folha por eficiencia, ele é 

Indice = Atendimento / (1 +  Renda)

## Saude

Alguma normalização das porcentagens de Crianças de 0 a 3 anos nas creches e Crianças de 4 a 5 anos na escola

## Educacao

Alguma normalização das porcentagens da Cobertura por equipes de atenção básica da saúde e Médicos por mil habitantes

## Saneamento

Alguma normalização das porcentagens dos Domicílios atendidos pelas redes de água e esgoto e Domicílios atendidos por sistemas de coleta de lixo

## Receita

Alguma normalização da Receita per capita do município
