import networkx as nx
import matplotlib.pyplot as plt
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend

data = open('edgesList.csv', 'r')
graphType = nx.DiGraph()

g = nx.parse_edgelist(data, delimiter=',', create_using=graphType,
                      nodetype=str)


model = ep.SEIRModel(g)

cfg = mc.Configuration()
cfg.add_model_parameter('beta', 0.01)
cfg.add_model_parameter('gamma', 0.005)
cfg.add_model_parameter('alpha', 0.05)
cfg.add_model_parameter("fraction_infected", 0.05)
model.set_initial_status(cfg)

iterations = model.iteration_bunch(200)

trends = model.build_trends(iterations)

viz = DiffusionTrend(model, trends)
viz.plot("diffusion.pdf")