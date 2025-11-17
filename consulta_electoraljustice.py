import pandas as pd
# import path
import subprocess


subprocess.run(['python', '/Users/guilherme/CNPJ-full/consulta.py', 'file', '/Users/guilherme/electoral-justice/build/query/network_judge.csv', '/Users/guilherme/electoral-justice/build/query/cnpj/', '--nivel 3', '--csv', '--graphml', '--viz', '--conexoes'], check=True)
