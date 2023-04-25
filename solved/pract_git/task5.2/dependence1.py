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

   
    module_tree.node('main', 'main.py')
    for module_path in module_paths:
        with open(module_path) as f:
            for node in ast.walk(ast.parse(f.read())):
                if isinstance(node, ast.Import):
                    for import_alias in node.names:
                       

    return module_tree.source

# Пример вызова функции build_module_tree
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'project'))
module_tree_source = build_module_tree(path)
print(module_tree_source)
