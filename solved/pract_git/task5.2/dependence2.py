import os
import graphviz


def generate_module_graph(root_path):
    graph = graphviz.Digraph(comment='Module Hierarchy')

    for dirpath, dirnames, filenames in os.walk(root_path):
        dir_label = os.path.basename(dirpath)
        dir_name = f'cluster_{dirpath}'
        with graph.subgraph(name=dir_name) as subgraph:
            subgraph.attr(label=dir_label, shape='folder', style='filled', color='lightgrey')
            for filename in filenames:
                if filename.endswith('.py'):
                    module_path = os.path.join(dirpath, filename)
                    module_name = os.path.splitext(filename)[0]
                    subgraph.node(module_name, label=f'{module_name}.py', shape='box', style='filled', color='white')
                    with open(module_path, 'r') as f:
                        for line in f:
                            if line.startswith(('import', 'from')):
                                for import_name in line.split()[1:]:
                                    if not import_name.startswith('.'):
                                        import_name = import_name.rstrip(',;')
                                        if import_name not in ['*', 'import']:
                                            subgraph.edge(module_name, import_name, arrowhead='none')

    return graph.source



path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'project'))
print(generate_module_graph(path))


