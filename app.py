from flask import Flask, request,make_response, send_file
from flask_protobuf import flask_protobuf as FlaskProtobuf
from Encoding_pb2 import KlabData
from infomap import Infomap
import networkx as nx
import pandas as pd

app = Flask(__name__)
fb = FlaskProtobuf(app,parse_dict=True)

@app.post("/")
@fb(KlabData)
def get_communities():
    
    data = request.data
    print(data)
    network = data.get("objects")[0]
    params = data.get("objects")[1]
    print(params)

    G = nx.DiGraph()
    for edge in network.get("objects"):
        source = edge.get("properties").get("source")
        target = edge.get("properties").get("target")
        weight = float(edge.get("properties").get("time"))
        G.add_edge(source,target,weight=weight)

    print(G)    

    im = Infomap(
            silent=True,
            flow_model="directed",
            no_file_output=True
        )
    mapping = im.add_networkx_graph(G)  
    im.run() 
  
    communities = { mapping.get(node_id) : str(module) for node_id,module in im.get_modules().items()}

    print(communities)

    klab_data = KlabData()
    object = klab_data.objects.add(properties=communities, name="Communities-level1")
    
    print(klab_data)
    
    with open("/home/dibepa/infomap-response", "wb") as f:
        f.write(klab_data.SerializeToString())


    send_file("/home/dibepa/infomap-response")

    response = make_response('Response')
    response.status_code = 200

    return response