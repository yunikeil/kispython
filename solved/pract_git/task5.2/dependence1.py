import os
import ast
import graphviz

def build_module_tree(root_path):
    # Рекурсивно обходим все каталоги, начиная с корневого каталога проекта,
    # и ищем файлы с расширением .py
    module_paths = []
    for dir_path, _, file_names in os.walk(root_path):
        for file_name in file_names:
            if file_name.endswith('.py'):
                module_path = os.path.join(dir_path, file_name)
                module_paths.append(module_path)

    # Строим иерархическое дерево модулей, где корневой узел - это main.py,
    # а потомками являются все модули, которые импортируются в main.py
    module_tree = graphviz.Digraph()
    module_tree.node('main', 'main.py')
    for module_path in module_paths:
        with open(module_path) as f:
            module_node_name = os.path.splitext(os.path.basename(module_path))[0]
            module_node_label = module_node_name + '.py'
            module_tree.node(module_node_name, module_node_label)
            module_tree.edge('main', module_node_name, constraint='false')
            for node in ast.walk(ast.parse(f.read())):
                if isinstance(node, ast.Import):
                    for import_alias in node.names:
                        import_name_parts = import_alias.name.split('.')
                        import_node_name = import_name_parts[0]
                        if import_node_name != '__future__':
                            if import_node_name in [os.path.splitext(os.path.basename(p))[0] for p in module_paths]:
                                import_node_label = import_node_name + '.py'
                            else:
                                import_node_label = '[' + import_node_name + ']'
                            module_tree.node(import_node_name, import_node_label)
                            module_tree.edge(module_node_name, import_node_name, constraint='false')
                elif isinstance(node, ast.ImportFrom):
                    import_name_parts = node.module.split('.')
                    import_node_name = import_name_parts[0]
                    if import_node_name != '__future__':
                        if import_node_name in [os.path.splitext(os.path.basename(p))[0] for p in module_paths]:
                            import_node_label = import_node_name + '.py'
                        else:
                            import_node_label = '[' + import_node_name + ']'
                        module_tree.node(import_node_name, import_node_label)
                        module_tree.edge(module_node_name, import_node_name, constraint='false')

    return module_tree.source

# Пример вызова функции build_module_tree
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'project'))
module_tree_source = build_module_tree(path)
print(module_tree_source)
