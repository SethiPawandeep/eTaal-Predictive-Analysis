import pandas as pd

def get_data(project_name, standard_service):
	mmp_data = pd.read_excel('../MMP_transactionDatewise.xlsx')
	mmp_data = mmp_data[:-19]
	data = 1
	data_dict = {'Date': [], 'Count': []}
	for i in range(0, len(mmp_data)):
		if mmp_data['Project Name'][i] == project_name and mmp_data['Standard Service'][i] == standard_service:
			if len(data_dict['Date']) == 0 or data_dict['Date'][-1] != mmp_data['STDDate'][i]:
				data_dict['Date'].append(mmp_data['STDDate'][i])
				data_dict['Count'].append(mmp_data['TotalCount'][i])
			else:
				data_dict['Count'][-1] += mmp_data['TotalCount'][i]
	data = pd.DataFrame(data=data_dict)
	data.index = data.Date
	data.drop('Date', axis=1, inplace=True)
	return data