import matplotlib.pyplot as plt
import io
import base64
from data import get_data_for_service, get_data_for_state

def build_graph(data, predictions):
	img = io.BytesIO()
	plt.plot(data)
	plt.plot(predictions['Predictions'])
	plt.savefig(img, format='png')
	img.seek(0)
	graph_url = base64.b64encode(img.getvalue()).decode()
	plt.close()
	return 'data:image/png;base64,{}'.format(graph_url)

def make_graph_for_service(project_name, standard_service):
	service_data, predictions = get_data_for_service(project_name, standard_service)
	graph_url = build_graph(service_data, predictions)
	return graph_url

def make_graph_for_state(state):
	state_data, predictions = get_data_for_state(state)
	graph_url = build_graph(state_data, predictions)
	return graph_url