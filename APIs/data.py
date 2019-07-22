# import pandas as pd

# def get_data(project_name, standard_service):
# 	mmp_data = pd.read_excel('../MMP_transactionDatewise.xlsx')
# 	mmp_data = mmp_data[:-19]
# 	data = 1
# 	data_dict = {'Date': [], 'Count': []}
# 	for i in range(0, len(mmp_data)):
# 		if mmp_data['Project Name'][i] == project_name and mmp_data['Standard Service'][i] == standard_service:
# 			if len(data_dict['Date']) == 0 or data_dict['Date'][-1] != mmp_data['STDDate'][i]:
# 				data_dict['Date'].append(mmp_data['STDDate'][i])
# 				data_dict['Count'].append(mmp_data['TotalCount'][i])
# 			else:
# 				data_dict['Count'][-1] += mmp_data['TotalCount'][i]
# 	data = pd.DataFrame(data=data_dict)
# 	data.index = data.Date
# 	data.drop('Date', axis=1, inplace=True)
# 	return data

# from db_connect import db_connect

import mysql.connector
import pandas as pd
import yaml

def get_data(project_name, standard_service):
	with open("config.yaml", 'r') as ymlfile:
		cfg = yaml.load(ymlfile)
	connection = cfg['mysql']
	mydb = mysql.connector.connect(
		host=connection['host'],
		user=connection['user'],
		passwd=connection['passwd'],
		database=connection['database'])
	mycursor = mydb.cursor()
	query = 'SELECT std_date, sum(total_count) from MMP_transactionDatewise where project_name="' + project_name + '" and standard_service="' + standard_service + '" group by std_date'
	mycursor.execute(query)
	result = mycursor.fetchall()
	result = [(i[0], int(i[1])) for i in result]
	data = pd.DataFrame(result, columns=['Date', 'Total Count'])
	data.index = data.Date
	data.drop('Date', axis=1, inplace=True)
	return data