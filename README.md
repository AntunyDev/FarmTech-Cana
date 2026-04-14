# 🚜 FarmTech Cana - Inteligência na Gestão de Colheitas

## 📋 Contexto e Problema

O Brasil é o líder mundial na produção de cana-de-açúcar, alcançando recordes que ultrapassam **620 milhões de toneladas** por safra. No entanto, o setor enfrenta um desafio crítico: **as perdas na colheita**.

Estudos indicam que, enquanto na colheita manual as perdas raramente passam de **5%**, na colheita mecânica esse índice sobe drasticamente para **15%**. Esse gap de produtividade representa um prejuízo astronômico: apenas no estado de São Paulo, estima-se uma perda anual de **R$ 20 milhões**.

Para combater esse cenário, o produtor precisa de estratégias de monitoramento precisas, planejamento eficiente e análise de dados em tempo real para otimizar o uso de colhedoras e reduzir o desperdício.

## 💡 A Solução: FarmTech Cana

O **FarmTech Cana** surge como uma ferramenta de **Agrotech** focada em transformar dados de campo em decisões estratégicas. O sistema permite ao gestor rural:

1.  **Monitorar Precisamente**: Registrar cada colheita, comparando a produtividade esperada com a real.
2.  **Identificar Gargalos**: Calcular automaticamente o percentual de perda e o prejuízo financeiro causado por ineficiências.
3.  **Alertar Desvios**: O sistema emite avisos imediatos quando as perdas ultrapassam as referências técnicas (5% para manual e 15% para mecânico).
4.  **Análise Comparativa**: Gerar relatórios que permitem avaliar se a mecanização está operando dentro dos padrões de eficiência ou se necessita de ajustes.

---

## 🛠️ Funcionalidades Técnicas

Desenvolvido em conformidade com as exigências acadêmicas, o sistema integra:
- **Gestão de Talhões**: Cadastro completo com UUID, variedades de cana e área produtiva.
- **Registro de Colheitas**: Entrada de dados com validação rigorosa (evitando erros de digitação).
- **Relatórios Avançados**: Gráficos e tabelas térmicas no terminal para visualização de ineficiências.
- **Base de Dados Robusta**: Persistência dupla via **JSON** (local) e **Oracle Database** (nuvem/corporativo).
- **Logs de Auditoria**: Registro de todas as operações em arquivo de texto.

---

## 🎨 Interface e Usabilidade

O sistema utiliza a biblioteca **Rich** para oferecer uma experiência de **Agrotech moderna**:
- **Interface Verde e Amarelo**: Identificando-se com o agronegócio brasileiro.
- **Limpeza de Fluxo**: Terminal otimizado com limpeza de tela e menus dinâmicos.
- **Tabelas Organizadas**: Visualização clara de dados complexos diretamente no prompt de comando.

---

## ⚙️ Instalação e Configuração

### Requisitos
- **Python 3.10+** (utilize o comando `py` no Windows).
- **Oracledb library** e acesso a uma instância Oracle.

### Passo a Passo

1. **Instale as dependências:**
   ```bash
   py -m pip install -r requirements.txt
   ```

2. **Configure o Banco de Dados:**
   Crie um arquivo `.env` com:
   ```env
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_DSN=localhost:1521/xe
   ```

3. **Inicie o Sistema:**
   ```bash
   py main.py
   ```

---

## 🎓 Sobre o Projeto
Este software foi desenvolvido como parte das atividades acadêmicas da **FIAP**, aplicando conceitos avançados de subalgoritmos, estruturas de dados, persistência de arquivos e conectividade com bancos de dados relacionais para resolver problemas reais do agronegócio brasileiro.

**Desenvolvedor:**
*   **Antuny Marques** - [GitHub](https://github.com/AntunyDev)
