# FarmTech Cana - Sistema de Inteligência na Gestão de Colheitas

## 👥 Integrantes
*   [Antuny Marques](https://github.com/AntunyDev) - RMxxxxx
*   [Nome do integrante 2](link-do-linkedin) - RMxxxxx
*   [Nome do integrante 3](link-do-linkedin) - RMxxxxx
*   [Nome do integrante 4](link-do-linkedin) - RMxxxxx
*   [Nome do integrante 5](link-do-linkedin) - RMxxxxx

### 👩‍🏫 Tutor(a)
*   [Nome do Tutor]

### 👨‍💼 Coordenador(a)
*   [Nome do Coordenador]

---

## 📜 Descrição
O projeto **FarmTech Cana** é uma solução de **Agrotech** desenvolvida para enfrentar um dos maiores desafios do agronegócio brasileiro: as perdas na colheita de cana-de-açúcar. Enquanto o Brasil lidera a produção mundial com mais de **620 milhões de toneladas**, as ineficiências na colheita mecânica chegam a gerar perdas de **15%** (contra 5% na colheita manual), resultando em prejuízos anuais de milhões de reais.

Nossa solução automatiza o monitoramento de produtividade, permitindo o registro de cada safra, cálculo automático de perdas (em toneladas e reais) e comparação de eficiência entre métodos de colheita. Com uma interface de terminal premium e integração com **Oracle Database**, o sistema fornece os dados necessários para uma tomada de decisão rápida e estratégica no campo.

---

## 📁 Estrutura de pastas
Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- **.github**: Arquivos de configuração específicos do GitHub e automações.
- **assets**: Imagens e elementos visuais do projeto.
- **config**: Arquivos de configuração, como o `.env` (credenciais) e `requirements.txt`.
- **document**: Documentação do projeto e relatórios complementares.
- **scripts**: Scripts auxiliares e automações de banco de dados.
- **src**: Todo o código-fonte do sistema (módulos e ponto de entrada).
- **README.md**: Guia geral e explicação do projeto.

---

## 🔧 Como executar o código

### Pré-requisitos
- **Python 3.10+** instalado.
- **Oracle Instant Client** configurado na máquina.
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
   Certifique-se de que o arquivo `.env` esteja dentro da pasta `config/` com o seguinte formato:
   ```env
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_DSN=localhost:1521/xe
   ```

4. **Execute o projeto:**
   A partir da raiz do projeto, execute:
   ```bash
   py src/main.py
   ```

---

## 🗃 Histórico de lançamentos
- **0.1.0 - 14/04/2026**
    - Estruturação inicial do projeto.
    - Implementação de CRUD de talhões e colheitas.
    - Integração com Rich UI e Oracle Database.
    - Organização conforme template FIAP.

---

## 📋 Licença
[MODELO GIT FIAP](https://github.com/agodoi/template) por [Fiap](https://fiap.com.br) está licenciado sobre [Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1).
