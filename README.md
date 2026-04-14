# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="https://raw.githubusercontent.com/agodoi/templateFiapVfinal/main/assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Cana
## Inteligência na Gestão de Colheitas

## 👨‍🎓 Integrantes: 
- <a href="https://github.com/AntunyDev">Antuny Marques</a>
- <a href="#">Nome do integrante 2</a>
- <a href="#">Nome do integrante 3</a> 
- <a href="#">Nome do integrante 4</a> 
- <a href="#">Nome do integrante 5</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="#">Nome do Tutor</a>
### Coordenador(a)
- <a href="#">Nome do Coordenador</a>


## 📜 Descrição

O projeto **FarmTech Cana** é uma solução de **Agrotech** desenvolvida para enfrentar um dos maiores desafios do agronegócio brasileiro: as perdas na colheita de cana-de-açúcar. Enquanto o Brasil lidera a produção mundial com mais de **620 milhões de toneladas**, as ineficiências na colheita mecânica chegam a gerar perdas de **15%** (contra 5% na colheita manual).

Nossa solução automatiza o monitoramento de produtividade, permitindo o registro de cada safra, cálculo automático de perdas (em toneladas e reais) e comparação de eficiência entre métodos de colheita. Com uma interface de terminal premium e integração com **Oracle Database**, o sistema fornece os dados necessários para uma tomada de decisão rápida e estratégica no campo.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto (como o `.env` e `requirements.txt`).

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", estão os arquivos de dados e logs do sistema.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: scripts SQL de inicialização do banco.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto.

## 🔧 Como executar o código

### Pré-requisitos
- **Python 3.10+** instalado.
- **Oracle Instant Client** configurado.
- Bibliotecas: `rich`, `oracledb`, `python-dotenv`.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/AntunyDev/FarmTech-Cana.git
   cd FarmTech-Cana
   ```

2. **Instale as dependências:**
   ```bash
   py -m pip install -r config/requirements.txt
   ```

3. **Configure as Variáveis de Ambiente:**
   Certifique-se de que o arquivo `.env` esteja na pasta `config/`:
   ```env
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_DSN=localhost:1521/xe
   ```

4. **Execute o sistema:**
   ```bash
   py src/main.py
   ```


## 🗃 Histórico de lançamentos

* 0.1.0 - 14/04/2026
    * Estruturação inicial conforme template FIAP vFinal.
    * Implementação da lógica de gestão de colheitas e talhões.
    * Integração com Oracle Database e interface Rich.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
