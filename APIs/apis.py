from flask import Flask, render_template
from graph import make_graph

app = Flask(__name__)

@app.route('/api/<project_name>/<standard_service>')
def graphs(project_name, standard_service):
	graph_url = make_graph(project_name, standard_service)

	return render_template('graph.html', 
		name=standard_service,
		graph=graph_url)

@app.route('/')
def index():
	return 'Test successful'