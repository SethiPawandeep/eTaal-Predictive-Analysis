import pandas as pd
from fastai.tabular import add_datepart
import os.path
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

def make_predictions(data):
	# if os.path.exists('models/{0}_{1}.sav'.format(project_name, standard_service)):
	# 	# TODO Load model and predict
	# 	return

	new_data = pd.DataFrame(index=range(0,len(data)),columns=['Date', 'Total Count'])
	for i in range(0, len(data)):
		new_data['Date'][i] = data.index[i]
		new_data['Total Count'][i] = data['Total Count'][i]
	add_datepart(new_data, 'Date')
	new_data.drop(['Dayofyear', 'Dayofweek', 'Elapsed', 'Is_quarter_end', 'Week', 'Is_month_end', 'Is_month_start', 'Is_quarter_start', 'Is_year_end', 'Is_year_start'], axis=1, inplace=True)

	train_size = len(new_data)
	train = new_data[:train_size]
	x_train = train.drop('Total Count', axis=1)
	y_train = train['Total Count']

	model = LinearRegression()
	model.fit(x_train, y_train)
	
	# TODO Save model

	test = pd.date_range(data.index[-1], data.index[-1] + timedelta(days=365), freq='D')
	test = pd.DataFrame(test, columns=['Date'])
	test_date = pd.date_range(data.index[-1], data.index[-1] + timedelta(days=365), freq='D')
	test_date = pd.DataFrame(test, columns=['Date'])
	add_datepart(test, 'Date')
	test.drop(['Dayofyear', 'Dayofweek', 'Elapsed', 'Is_quarter_end', 'Week', 'Is_month_end', 'Is_month_start', 'Is_quarter_start', 'Is_year_end', 'Is_year_start'], axis=1, inplace=True)

	predictions = model.predict(test)
	test['Predictions'] = predictions
	test.index = test_date.Date
	
	return test