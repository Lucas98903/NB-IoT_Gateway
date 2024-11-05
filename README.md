# NB_Server_Gateway

# Estrutura de pastas
```
.(root)
├── controller/                             # Contém arquivos para controle.
│   ├── __init__.py                         # Arquivo inicializador do módulo.
│   ├──controller_comand.py                 # Controla os as configurações do sensor.
│   └──handle_client.py                     # Controla a comunicação do equipamento.
│           
├── database                                # Controla a comunicação do sensor
│    ├── __init__.py                        # Arquivo inicializador do módulo.
│    ├── database.py                        # Faz o acesso ao banco de dados
│    └── DAO                                # Arquivos para comunicar com banco de dados.
│         ├── __init__.py                   # Arquivo inicializador do módulo.
│         └──sensor_DAO.py                  # Envia os dados para o banco de dados.
│               
├── documents/                              # Contém todos o documentos do sensor 
│   └──.pdf         
│           
├──log                                      # Contém tudo relacionado a logs e registro
│  └──all.log                               # Report do funcionamento
│           
├──model                                    # Tem o modelo para dados esperados
│   ├── __init__.py                         # Arquivo inicializador do módulo.
│   ├── commands.py                         # Modelo para enviar comando para o equipamento.
│   └── data.py                             # modelo da saída de dados do equipamento
│           
├──routers                                  # Arquivos da rotas da API
│   ├── __init__.py                         # Arquivo inicializador do módulo.
│   ├── command_router.py                   # Rota das entradas dos comando para o equipamento.
│   └── Status_router.py                    # rota de saída de dado do equipamento.
│           
├──server                                   # Arquivos da rotas da API
│   ├── __init__.py                         # Arquivo inicializador do módulo.
│   ├── conection.py                        # Faz a conexão com o equipamento.
│   └── scan.py                             # Scaneia a o ip: 0.0.0.0.
│           
├──services                                 # Arquivos de serviços para funcionamento do código
│   ├── decode                              # Arquivos para decodificar a informaçao do equipamento.
│   │     ├──__init__.py                    # Arquivo inicializador do módulo.
│   │     └── Status_router.py              # rota de sapida de dado do equipamento.
│   ├── firebase            
│   │           
│   ├── logger          
│   ├── memory          
│   ├── preference          
│   └── upload          
├── .gitignore                              # Arquivos ignorados no versionamento
├── main.py                                 # Arquivo que inicializa o Gateway e configura as rotas
└── README.md                               # Readme do projeto
```         