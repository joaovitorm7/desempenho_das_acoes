# Desempenho das ações
Atividade de Matriz do professor Pedro Luis Saraiva Barbosa, que ministra a matéria de PEED (PROGRAMAÇÃO ESTRUTURADA E ESTRUTURA DE DADOS).

Questão: Você é um engenheiro de dados trabalhando para uma empresa de análise financeira que monitora as flutuações diárias dos preços das ações de cinco empresas em um período de 7 dias. Os preços das ações são registrados em uma matriz onde cada linha representa um dia e cada coluna representa uma empresa. A empresa deseja analisar o desempenho das ações e gerar um relatório com base nos dados coletados.

Considere a seguinte matriz que representa os preços das ações das cinco empresas (A, B, C, D e E) ao longo de uma semana (7 dias):
# Criação da matriz de preços das ações 
precos_acoes = np.array([ 
      [150, 200, 180, 220, 170], 
      [155, 205, 185, 225, 175], 
      [160, 210, 190, 230, 180],
      [165, 215, 195, 235, 185], 
      [170, 220, 200, 240, 190], 
      [175, 225, 205, 245, 195], 
      [180, 230, 210, 250, 200] 
])

1º Calcule a média diária dos preços das ações para cada empresa ao longo da semana.
2º Determine a variação diária (diferença entre o preço máximo e o preço mínimo) das ações para cada empresa ao longo da semana.
3º Encontre o dia da semana em que a ação da empresa B teve o maior preço e o menor preço.
4º Se a empresa decide que o preço das ações deve aumentar 5% ao final da semana, atualize a matriz com os novos preços das ações e calcule a nova média diária.
