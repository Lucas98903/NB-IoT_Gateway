# NB_Server_Gateway

# Estrutura de pastas
```
.(root)
├── decode/                       # Contém arquivos para interpretar o hexadecimal recebido
│ ├── __init__.py                 # Arquivo inicializador do módulo 
│ ├── dp201.py                    # Interpreta o hexadecimal
│ └── utility.py                  # Função para converter o valor do RSRP de ponto flutuante para float.
├── documents/                    # Contém todos o documentos do sensor 
│ └── ... 
├──log                            # Contém tudo que é relacionado a logs e registro
│  ├──hist                        # Apenas para manter alguns logs importantes
|  │  └──...
│  ├──logger.py                   # Gerencia o registros dos logs
│  └──all.log                     # Report do funcionamento
├── notes/                        # Contém anotações
│ └──ToDo.txt                     # Lista de coisas a fazer
├── .gitignore                    # Arquivos ignorados no versionamento
├── NB_Server_Gateway.py          # Arquivo que inicializa o Gateway e configura as rotas
└── README.md                     # Readme do projeto
```