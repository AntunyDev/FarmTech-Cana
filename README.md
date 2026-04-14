# 🚜 FarmTech Cana - Sistema de Gestão de Colheitas de Cana-de-açúcar

Bem-vindo ao **FarmTech Cana**, uma solução robusta e moderna desenvolvida para otimizar o monitoramento e a gestão de colheitas de cana-de-açúcar. O sistema foca no acompanhamento de produtividade e na análise detalhada de perdas, permitindo uma tomada de decisão baseada em dados reais.

---

## 🌟 Funcionalidades Principais

### 🏷️ Gestão de Talhões
- Cadastro detalhado de áreas de plantio (hectares, variedade da cana, município, ano de plantio).
- Identificação única via UUID simplificado.
- Listagem organizada em tabelas visuais.

### 🚜 Registro de Colheitas
- Acompanhamento de produtividade real vs. esperada.
- Registro de métodos de colheita (Manual ou Mecânico).
- Cálculo automático de perdas em toneladas, percentual e prejuízo financeiro (R$).
- Alertas visuais para perdas acima da referência técnica.

### 📊 Relatórios Inteligentes
- **Geral de Perdas**: Visão consolidada de toda a produção.
- **Comparativo de Métodos**: Análise de eficiência entre colheita manual e mecânica.
- **Top 5 Prejuízos**: Identificação rápida dos talhões com maior impacto financeiro.

### 🗄️ Integração Oracle Database
- Persistência robusta em banco de dados relacional.
- Sincronização automática de cadastros e registros de colheita.
- Consultas formatadas diretamente do banco.

---

## 🎨 Interface Premium (Terminal)

O sistema utiliza a biblioteca **Rich** para entregar uma experiência de usuário (UX) diferenciada no terminal, focando nos padrões:
- **Tema Verde e Amarelo**: Identidade visual limpa e conectada ao setor agrícola.
- **Tabelas e Painéis**: Organização visual superior para dados complexos.
- **Fluxo Limpo**: Limpeza automática de tela para manter o foco na tarefa atual.

---

## 🛠️ Requisitos e Instalação

### Requisitos
- **Python 3.10+**
- **Oracle Instant Client** (necessário para a biblioteca `oracledb`)

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/AntunyDev/FarmTech-Cana.git
   cd FarmTech-Cana
   ```

2. **Instale as dependências:**
   ```bash
   py -m pip install -r requirements.txt
   ```

3. **Configure as Variáveis de Ambiente:**
   Crie um arquivo `.env` na raiz do projeto com as suas credenciais Oracle:
   ```env
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_DSN=localhost:1521/xe
   ```

4. **Execute o sistema:**
   ```bash
   py main.py
   ```

---

## 📁 Estrutura do Projeto

- `main.py`: Ponto de entrada e gerenciamento de menus.
- `modulos/`:
  - `talhoes.py`: Lógica de gerenciamento de áreas de plantio.
  - `colheitas.py`: Registro e cálculos de produtividade.
  - `relatorios.py`: Processamento de dados e geração de estatísticas.
  - `banco.py`: Conectividade e comandos SQL para o Oracle.
  - `persistencia.py`: Salvamento local (JSON) e logs de operação.

---

## 👨‍💻 Autor

Desenvolvido como projeto para a **FIAP**.

*   **Antuny Marques** - [GitHub](https://github.com/AntunyDev)
