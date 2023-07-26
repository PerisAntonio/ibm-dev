import fireopal, networkx as nx, qiskit
from qiskit_ibm_provider import IBMProvider

def run(input_data, solver_params, extra_arguments):
    print("Starting MaxCut Qtrl")
    token = "d44b51582d42552a549f8b72860c3281acfd385c515f80e6824135c3f102ac4b773d87717c0e4523bc488e6d80d1ec49322019c196c7ceb06934359f7a29e823"
    hub = "summer-school-5"
    group="group-8"
    project="6917883049"
    i=0
    print('MaxCut Qtrl step ',str(i))
    i+=1
    credentials = fireopal.credentials.make_credentials_for_ibmq(token=token, hub=hub, group=group, project=project)
    print('MaxCut Qtrl step ',str(i))
    i+=1
    IBMProvider.save_account(token, overwrite=True, instance=hub + "/" + group + "/" + project)
    print('MaxCut Qtrl step ',str(i))
    i+=1
    provider = IBMProvider()
    print('MaxCut Qtrl step ',str(i))
    i+=1
    backend_name = "ibmq_manila"
    backend = provider.get_backend(backend_name)
    print('MaxCut Qtrl step ',str(i))
    i+=1
    graph=input_data['edges']
    G=nx.Graph()
    nodes=[]
    for edge in graph:
        x=int(edge[0])
        y=int(edge[1])
        if x not in nodes:
            nodes.append(x)
        if y not in nodes:
            nodes.append(y)
    for node in nodes:
        G.add_node(node,weight=0)
    for edge in graph:
        G.add_edge(int(edge[0]),int(edge[1]),weight=1)
    print('MaxCut Qtrl step ',str(i))
    i+=1
    fire_result = fireopal.solve_qaoa(G, "maxcut", credentials, backend_name)
    print('MaxCut Qtrl step ',str(i))
    i+=1
    return fire_result['solution_bitstring']