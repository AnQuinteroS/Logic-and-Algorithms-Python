import ast
import os
import sys

def run_linter(directory):
    # Resolver ruta absoluta para que funcione desde cualquier lugar
    base_dir = os.path.abspath(directory)
    
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')
                    
                    # 1. Ignorar el propio linter si se está revisando a sí mismo
                    if os.path.basename(filepath) == 'linter.py':
                        continue
                        
                    # 2. Revisar longitud de línea
                    for i, line in enumerate(lines):
                        if len(line) > 79:
                            print(f"[{filepath}:{i+1}] Line exceeds 79 characters")

                # 3. Detectar funciones normales y asíncronas
                try:
                    tree = ast.parse(content)
                    for node in ast.walk(tree):
                        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            pass # Aquí va tu lógica de revisión de funciones
                except SyntaxError:
                    print(f"Syntax error in {filepath}")
