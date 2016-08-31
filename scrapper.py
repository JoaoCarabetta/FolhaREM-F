from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


def wait_load_page(driver):
	
	time.sleep(0.5)
	try:
		return WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((By.ID, "municipio-detalhes")))
	except:
		return None

element2float = lambda element, id: float(element.find_element_by_id(id).text.replace(',','.'))

def get_info(element, data, i):

	values = []
	
	# cidade
	values.append(element.find_element_by_id('citie-name-val').text.encode('ascii','ignore'))

	#indice
	values.append(element2float(element, 'ranking'))

	# saude
	values.append(element2float(element, 'saude-val'))
	
	# educacao
	values.append(element2float(element, 'educacao-val'))
	
	# saneamento
	values.append(element2float(element, 'saneamento-val'))

	# receita
	values.append(element2float(element, 'receita-val'))

	data.loc[i] = values

	return data
    
    
if __name__ == '__main__':
	data = pd.DataFrame(columns=["Cidade", "Indice", "Saude", "Educacao", "Saneamento", "Receita"])
	driver = webdriver.Firefox()

	for i in range(1, 5282):
		driver.get("http://www1.folha.uol.com.br/remf/#/municipio/{}".format(i))
		element = wait_load_page(driver)
		data = get_info(element, data, i)
		

		if i % 50 == 0:
			data.to_csv('database.csv')
			print data
