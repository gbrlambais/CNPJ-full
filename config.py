PATH_BD = 'data/CNPJ_full.db'
NIVEL_MAX_DEFAULT = 3

PATH_NAVEGADOR = ''
#PATH_NAVEGADOR = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'

SEP_CSV = ';'
COLUNAS_CSV =  ['tipo_pessoa',
                'nivel',
                'cnpj',
                'cpf',
                'nome',
                'matriz_filial', 
                'razao_social', 
                'nome_fantasia', 
                'situacao', 
                'data_situacao',
                'motivo_situacao',
                'nm_cidade_exterior',
                'cod_pais',
                'nome_pais',
                'cod_nat_juridica',
                'data_inicio_ativ', 
                'cnae_fiscal',
                'tipo_logradouro',
                'logradouro',
                'numero',
                'complemento',
                'bairro',
                'cep',
                'uf',
                'cod_municipio',
                'municipio',
                'email',
                'qualif_resp',
                'capital_social',
                'porte',
                'opc_simples',
                'data_opc_simples',
                'data_exc_simples',
                'opc_mei',
                'sit_especial',
                'data_sit_especial']

QUALIFICACOES = 'TODAS'
#QUALIFICACOES = ['05','08','10','16','17','20','21','22','23','24','25','26','28','29',
#				 '30','31','37','38','47','48','49','52','53','54','55','56','57','58',
#				 '59','63','65','66','67','68','70','71','72','73','74','75']

# Qualificacoes para referencia
#05 Administrador 
#08 Conselheiro de Administração 
#10 Diretor 
#16 Presidente 
#17 Procurador 
#20 Sociedade Consorciada 
#21 Sociedade Filiada 
#22 Sócio 
#23 Sócio Capitalista 
#24 Sócio Comanditado 
#25 Sócio Comanditário 
#26 Sócio de Indústria 
#28 Sócio-Gerente 
#29 Sócio Incapaz ou Relat.Incapaz (exceto menor) 
#30 Sócio Menor (Assistido/Representado) 
#31 Sócio Ostensivo 
#37 Sócio Pessoa Jurídica Domiciliado no Exterior 
#38 Sócio Pessoa Física Residente no Exterior 
#47 Sócio Pessoa Física Residente no Brasil 
#48 Sócio Pessoa Jurídica Domiciliado no Brasil 
#49 Sócio-Administrador 
#52 Sócio com Capital 
#53 Sócio sem Capital 
#54 Fundador 
#55 Sócio Comanditado Residente no Exterior 
#56 Sócio Comanditário Pessoa Física Residente no Exterior 
#57 Sócio Comanditário Pessoa Jurídica Domiciliado no Exterior 
#58 Sócio Comanditário Incapaz 
#59 Produtor Rural 
#63 Cotas em Tesouraria 
#65 Titular Pessoa Física Residente ou Domiciliado no Brasil 
#66 Titular Pessoa Física Residente ou Domiciliado no Exterior 
#67 Titular Pessoa Física Incapaz ou Relativamente Incapaz (exceto menor) 
#68 Titular Pessoa Física Menor (Assistido/Representado) 
#70 Administrador Residente ou Domiciliado no Exterior 
#71 Conselheiro de Administração Residente ou Domiciliado no Exterior 
#72 Diretor Residente ou Domiciliado no Exterior 
#73 Presidente Residente ou Domiciliado no Exterior 
#74 Sócio-Administrador Residente ou Domiciliado no Exterior 
#75 Fundador Residente ou Domiciliado no Exterior