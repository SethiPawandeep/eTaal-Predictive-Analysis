from flask import Flask, render_template
from graph import make_graph_for_service, make_graph_for_state

app = Flask(__name__)

@app.route('/api/<project_name>/<standard_service>')
def graph_service(project_name, standard_service):
	graph_url = make_graph_for_service(project_name, standard_service)

	return render_template('graph.html', 
		name=standard_service,
		graph=graph_url)

@app.route('/api/<state>')
def graph_state(state):
	graph_url = make_graph_for_state(state)

	return render_template('graph.html',
		name=state,
		graph=graph_url)

@app.route('/')
def index():
	return 'Test successful'