# Sistema de Gestão de Tarefas para Equipes Educacionais

Aplicação web desenvolvida em Django para gerenciamento de tarefas em contextos educacionais, permitindo a colaboração entre professores e alunos com funcionalidades de acompanhamento e análise de progresso.

## Funcionalidades Principais

- **Gestão de Usuários**: 
  - Dois perfis de acesso: Professor (criação de equipes/tarefas) e Aluno (execução de tarefas)
  - Sistema de autenticação com sessões

- **Gestão de Tarefas**:
  - Criação de tarefas com múltiplas alternativas e resposta correta
  - Atribuição a equipes específicas
  - Marcadores de conclusão e acompanhamento de respostas

- **Trabalho em Equipe**:
  - Criação de equipes com múltiplos membros
  - Dashboard de progresso por equipe
  - Sistema de mensagens para comunicação interna

- **Análise de Dados**:
  - Estatísticas visuais (gráficos) de desempenho individual e de equipe
  - Exportação de relatórios em Excel com dados de progresso

## Tecnologias Utilizadas

- **Backend**: Django 4.x
- **Visualização de Dados**: Matplotlib
- **Processamento de Planilhas**: Openpyxl
- **Frontend**: HTML5, CSS3 