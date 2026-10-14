Módulo empacotado de `02-pagina-vendas-02-design-system-clinicas-saude.md`. Aplique a metodologia com a autonomia e o contrato de saída de `SKILL.md` e `execucao.md`.

# Design System Extrator — Landing de Clínicas de Saúde

Adaptação do arquivo original da coleção para páginas de clínicas de saúde.

Você extrai, organiza e traduz uma referência visual em especificação técnica. A estrutura vem da referência; a identidade e os fatos vêm dos insumos da clínica. Qualquer adaptação proposta deve ser identificada como recomendação, sem parecer uma característica observada na referência.

**Contexto do segmento:** a página precisa tornar reconhecíveis o atendimento, os profissionais, o local e o caminho de acesso. Fotos reais, apresentação da equipe, explicação da consulta e informações práticas podem sustentar confiança. Imagens de resultados clínicos não são requisito para uma página completa.

**Imagem tem função:** registre o que ela ajuda o visitante a entender ou verificar.

**Background organiza a leitura:** documente o ritmo existente, inclusive quando a referência usa um fundo contínuo. Não crie uma alternância claro/escuro apenas para preencher o mapa.

**Tratamento visual tem limites:** unidade de luz e cor deve respeitar a integridade de fotos reais e de eventuais provas clínicas.

## INSUMOS — LEIA O CONTEXTO ANTES DE PERGUNTAR

- **Referência visual:** URL, prints ou PDF da página modelo. É necessária para afirmar que houve extração. Se faltar, peça a referência; não apresente um sistema inventado como extraído.
- **Identidade da clínica:** logo, cores, fontes, manual de marca e escolhas já aprovadas. A identidade fornecida prevalece sobre sugestões padrão desta skill.
- **Copy e análise estratégica:** use os resultados das [etapas 00](00-analise.md) e [01](01-copy.md), quando disponíveis. Preserve serviço, público, CTA, provas e qualificações confirmados.
- **Materiais reais:** fotos de profissionais, clínica, acesso e estrutura; relatos utilizáveis; registros e informações de atendimento pertinentes à oferta.
- **Moodboard ou atmosfera desejada:** imagens ou palavras fornecidas pelo usuário. Calibra linguagem visual; não substitui a referência de layout.
- **Contexto de implementação:** plataforma, assets existentes, restrições técnicas e dispositivos prioritários, quando conhecidos.

Não pergunte novamente o que já está nos materiais. Sem copy final, entregue o mapa estrutural da referência e sinalize que sua associação às seções da clínica ainda é provisória.

Uma referência de outro segmento pode fornecer estrutura. Não transporte seus personagens, promessas, resultados ou provas para a clínica.

## ORIGEM E CONFIANÇA DAS ESPECIFICAÇÕES

Identifique cada decisão relevante como:

- **OBSERVADO:** visível na referência ou confirmado por seus arquivos e estilos.
- **ESTIMADO:** medida aproximada obtida de print ou de conteúdo sem acesso aos estilos; informe como estimou.
- **FORNECIDO:** identidade, asset ou escolha explicitamente enviada ou aprovada pelo usuário.
- **RECOMENDADO:** ajuste proposto para a copy, responsividade, acessibilidade ou contexto de saúde.
- **NÃO IDENTIFICADO:** informação que a evidência não permite determinar.

Um print pode mostrar uma fonte semelhante, mas não comprova seu nome. Não invente família, peso, HEX exato ou comportamento de hover invisível. Se houver apenas evidência desktop, trate o comportamento mobile como desconhecido ou proposta.

## FASE 1 — LEITURA E EXTRAÇÃO

### Estrutura macro

Registre grid, container, alinhamentos, largura das colunas, espaços verticais, número de seções, posição dos CTAs e ritmo de fundos. Use px para medidas observadas ou estimadas e identifique a origem. Na implementação, unidades fluidas podem ser usadas com correspondência documentada.

Se houver copy aprovada, associe sua função à estrutura disponível sem reescrever o texto nem inventar uma consulta, serviço ou condição comercial.

### Tipografia

Extraia ou registre: família quando identificável, estilo, pesos, tamanhos, altura de linha, tracking, escala H1 → corpo → legenda, uso de caixa alta, itálico e grifos. Separe desktop e mobile.

Quando houver necessidade autorizada de escolher uma fonte, mantenha as opções da metodologia original: Sora, DM Sans, Outfit; Newsreader, Playfair Display, Crimson Text; IBM Plex Mono para usos pontuais adequados. A escolha precisa corresponder aos insumos e ficar marcada como recomendação.

Evite adotar Inter, Poppins, Roboto, Arial, Open Sans ou system-ui como escolha principal automática. Se a marca ou o usuário tiver aprovado uma dessas fontes, preserve a escolha explícita. Fallback técnico não é identidade tipográfica.

Registre fonte, origem, pesos disponíveis, licença conhecida e método de carregamento; não fabrique uma URL de download. Para hero em duas colunas, especifique um ajuste próprio de H1 que funcione com a copy real. `clamp(24px, 2.8vw, 44px)` é um exemplo da metodologia, não uma medida obrigatória para toda headline.

### Paleta e legibilidade

Documente cores centrais em HEX: fundo, texto, primária, CTA e superfície. Registre separadamente bordas, texto secundário e estados semânticos necessários. Não imponha cores com base apenas no segmento.

Mostre os pares texto/fundo relevantes e o contraste calculado quando houver valores confiáveis. Para texto comum, considere pelo menos 4,5:1; para texto grande, 3:1, conforme os critérios e exceções do [W3C — contraste mínimo](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). Não declare contraste medido com base apenas em impressão visual.

Se a referência tiver baixa legibilidade, registre o problema e proponha o ajuste separadamente. Fonte, marca ou efeito visual não justificam esconder informações essenciais sobre serviço e acesso.

### Componentes

Especifique botões primário e secundário, cards, apresentação dos profissionais, FAQ, informações de acesso e formulários quando existirem: dimensões, padding, radius, borda, cor, sombra e estados conhecidos.

Descreva focus visível, labels, mensagens de erro e feedback de envio. Os elementos visuais necessários para reconhecer controles e estados devem considerar o [W3C — contraste não textual](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

Como recomendação de conforto, prefira área de toque de pelo menos 44px nos CTAs principais; identifique isso como escolha de projeto, não como requisito universal extraído. No formulário comercial, preserve a finalidade e os campos mínimos definidos na copy.

**Ícones:** mantenha uma família coerente. Na ausência de escolha fornecida, as opções da metodologia são Iconify Solar Outline, Feather ou Phosphor. Evite Lucide como substituição automática; uma família explicitamente aprovada pelo usuário prevalece. Ícone não comprova certificação, segurança ou qualificação profissional.

### Animações

Documente apenas comportamentos observados: entrada, hover, stagger e outros efeitos. Sem evidência interativa, marque a animação como desconhecida ou recomendação.

Para ajustes, priorize leitura e acesso ao CTA. Defina comportamento com movimento reduzido; evite revelar contato, identificação ou informações de consulta somente após uma animação. Não acrescente contadores, alertas ou urgência visual sem conteúdo confirmado.

### Decisão de luz

Registre a atmosfera fornecida e a luz observada. Como direções possíveis, não como fatos universais:

| Atmosfera fornecida | Direção a avaliar |
|---|---|
| Proximidade e acolhimento | Luz natural ou difusa, preservando aparência real |
| Clareza e precisão | Luz neutra, enquadramento informativo |
| Reserva e tranquilidade | Contraste moderado e ambiente sem distrações |

Uma foto existente não precisa receber nova iluminação para cumprir a direção. Registre exceções quando houver fontes reais diferentes. Não aplique filtros que modifiquem aparência clínica, pele ou evidência de resultado.

### Inventário de imagens — tipos 01–08

Conte todos os assets relevantes à composição, inclusive logos, ícones e fundos. Separe quantidade de arquivos únicos de quantidade de ocorrências. Um sprite pode ter um arquivo e vários ícones utilizados.

| Tipo | Uso em clínicas de saúde |
|---|---|
| 01 | Profissionais e equipe reais, com identidade e uso adequados |
| 02 | Clínica, estrutura e acesso reais |
| 03 | Experiência de atendimento ou recurso em uso, sem simular caso real |
| 04 | Relato ou avaliação de experiência real com uso adequado |
| 05 | Informação de cuidado ou resultado contextualizado, somente se pertinente e utilizável |
| 06 | Jornada de contato, consulta e acompanhamento conforme a rotina real |
| 07 | Atmosfera ou ilustração claramente identificada |
| 08 | Ícone, diagrama ou informação de acesso sem falso endosso |

Para cada asset, registre:

```text
ID / nome do arquivo / seção / tipo 01–08 / função
origem: real fornecido | a fotografar | ilustração | vetor | banco autorizado
status: disponível | pendente | uso público a verificar | dispensado
posição / proporção / enquadramento / resolução conhecida
tratamento permitido / contexto ou legenda necessários
mobile: mantém | reposiciona | reduz | substitui | decorativo removível
alt: texto útil | vazio quando puramente decorativo
```

Não remova no celular uma informação essencial apenas porque ela aparece dentro de uma imagem. Relatos e imagens disponíveis nos insumos não estão automaticamente liberados para publicação.

### Mapa de backgrounds

Para cada seção, registre cor, efeito observado, grafismo, imagem de fundo, overlay e movimento. Informe opacidade ou intensidade quando conhecida e marque estimativas.

Documento visual contínuo também tem ritmo por espaço, hierarquia e superfícies. Grain, gradientes e fotos de fundo entram somente se forem observados ou propostos com uma função clara.

## FASE 2 — SÍNTESE E VALIDAÇÃO DA DIREÇÃO

Apresente uma síntese concreta:

```text
DESIGN SYSTEM — CLÍNICA DE SAÚDE [NOME]
REFERÊNCIA / OFERTA / COPY UTILIZADA:
LAYOUT: grid / container / espaçamento / seções
TIPOGRAFIA: famílias / pesos / escala / origem e grau de confiança
PALETA: HEX e papéis / pares de contraste / origem
LUZ E IMAGENS: atmosfera / materiais reais / ilustrações / limites de tratamento
COMPONENTES: CTA / cards / FAQ / formulário / foco
ÍCONES E MOVIMENTO: família / comportamentos observados e propostos
INVENTÁRIO: arquivos únicos / ocorrências / distribuição 01–08
BACKGROUNDS: sequência / efeitos / ajustes de legibilidade
CONFLITOS: referência × identidade × copy / solução proposta
PENDÊNCIAS: somente o que afeta uma decisão relevante
```

Use um único checkpoint quando houver uma escolha de direção ainda dependente do usuário. Pergunte sobre o conflito concreto, sem pedir confirmação genérica de informações já aprovadas. Se a direção estiver autorizada ou o usuário tiver pedido execução completa com autonomia, siga para a entrega técnica; não acrescente uma parada automática.

Enquanto uma decisão necessária estiver pendente, avance nas especificações independentes. Não transforme uma autorização de uso de imagem desconhecida em fato confirmado.

## FASE 3 — ENTREGA COMPLETA

### A — DESIGN SYSTEM TÉCNICO

Entregue valores concretos e sua origem; mantenha desconhecidos identificados. O esquema abaixo orienta o conteúdo, não é CSS pronto para execução:

```text
# DESIGN SYSTEM — [CLÍNICA / SERVIÇO]

CORES: primária / CTA / BG / superfície / texto / muted / borda / estados
       HEX / origem / contraste dos pares utilizados
TIPOGRAFIA: família / arquivo ou URL verificada / licença conhecida / pesos
            mobile e desktop: H1 / H2 / H3 / corpo / legenda / CTA
            line-height / tracking / grifos / ajuste de H1 para hero split
ESPAÇOS: container / padding horizontal / section py / gaps / breakpoints
BORDAS: width / cor / radius de botão, card, input, imagem e badge
SOMBRAS: valores CSS / contexto de uso
BOTÕES: dimensões / padding / cores / hover / focus / ativo / desabilitado
CARDS: grid / padding / border / shadow / responsive
FORMULÁRIO: labels / campos confirmados / foco / erro / envio / sucesso
FAQ: estado aberto / foco / texto legível
ÍCONES: família / tamanho / peso / cor / labels necessários
IMAGENS: proporções / recortes / tratamento por categoria / alt / resolução
MOVIMENTO: gatilho / duração / easing / redução de movimento
```

Forneça um bloco real de CSS vars com nomes consistentes e valores válidos quando os insumos permitirem, incluindo cores, fontes, espaços, raios e sombras. Não entregue `#___` como se fosse uma cor implementável.

Mantenha um contrato de tokens para a etapa seguinte:

```text
--color-primary / --color-accent / --color-bg / --color-surface
--color-text / --color-muted / --color-border / --color-focus
--font-heading / --font-body
--container-max / --padding-x-m / --padding-x-d
--section-py-m / --section-py-d / --card-gap
--radius-btn / --radius-card / --radius-input
--shadow-sm / --shadow-md / --shadow-lg
```

Esse bloco lista nomes, não valores. Preencha o CSS final com a especificação verificada ou recomendada e identifique a origem das escolhas no documento.

Se usar overlay decorativo, especifique gradientes e cores válidas; para cores dinâmicas, defina os canais RGB ou RGBA necessários. Não use a expressão inválida `rgba(bg, ...)`. Não aplique opacidade global à imagem e ao texto juntos.

Em fotos reais, registre tratamentos permitidos. Filter e overlay não são obrigatórios para toda imagem; não devem alterar evidência clínica, comprometer identificação ou esconder conteúdo necessário.

### B — WIREFRAME DOBRA A DOBRA

“Dobra” identifica a seção narrativa, não uma promessa de caber em uma altura fixa de tela. Preserve a copy aprovada e o caminho de conversão.

```text
SEÇÃO [N] — [NOME]
ORIGEM: seção observada / adaptação para copy / proposta ainda pendente
FUNÇÃO: dúvida que responde / fato ou prática que demonstra
COMPOSIÇÃO: entrada visual / percurso de leitura / chegada ao CTA
DESKTOP: colunas e proporções / container / padding / alinhamentos
MOBILE: ordem / empilhamento / tamanhos / recorte / informações preservadas
BG: HEX / efeito / overlay / grafismo / origem
ASSETS: nome exato / tipo / função / proporção / tratamento / alt
PROVA: fato e material que sustentam / uso público verificado ou pendente
IDENTIFICAÇÃO: dados profissionais necessários e localização prevista
CTA: texto aprovado / primário ou secundário / destino e próximo passo
ÍCONES E MOVIMENTO: família / interação / comportamento reduzido
DEPENDÊNCIAS: asset ausente / dado desconhecido / peso ou script a avaliar
```

Se a referência trouxer uma barra fixa, documente como funciona. Só recomende uma para o projeto quando ajudar no acesso e não cobrir conteúdo ou foco. Não acrescente barra de escassez por padrão.

O wireframe desta etapa especifica a adaptação estrutural. A etapa 03 de direção de criação poderá detalhar a composição usando este sistema e a copy, sem reextrair a identidade.

### C — BRIEFINGS DE IMAGEM

Para cada asset a criar ou obter, escolha a produção adequada:

- **Foto real:** profissional, equipe, clínica, acesso ou atendimento documentado. Entregue briefing de fotografia e condições de uso a verificar.
- **Asset existente:** registre fonte, resolução, licença ou autorização conhecida e limites de tratamento.
- **Ilustração:** pode receber prompt de geração, com identificação e finalidade claras. Se explicar cuidado ou procedimento, o conteúdo precisa de base verificada; não improvise informação clínica.
- **Vetor, ícone ou diagrama:** especifique conteúdo e sistema gráfico. Não force geração raster quando a solução adequada for SVG ou código.

```text
BRIEFING — [nome-exato.ext]
Seção / tipo / função / origem / método de produção
Sujeito ou conteúdo confirmado / composição / proporção / enquadramento
Luz / cor / fundo / espaço para texto / recorte mobile
Tratamento permitido / elementos a evitar / alt e legenda
Dependências: fato, material ou autorização a verificar
Foto real: o que fotografar / como / identificação necessária
Ilustração: prompt, preferencialmente em inglês se a ferramenta exigir
Vetor: estrutura, labels e família gráfica
```

Prompt para ilustração nunca pede “foto de paciente atendido pela clínica” ou profissional fictício com aparência de integrante real. Não envie materiais identificáveis de pacientes a um gerador externo apenas porque estão nos insumos. Briefing não autoriza publicação nem uso público de um asset pendente.

### D — RESUMO DE PRODUÇÃO E HANDOFF

Entregue total de seções, assets únicos e ocorrências; seções com CTA; comportamento mobile; lista de arquivos exatos; fontes e origem; mapa de backgrounds; decisões observadas, fornecidas e propostas; pendências que afetam implementação.

Use nomes descritivos e estáveis, como `foto-profissional-nome.webp`, `foto-clinica-recepcao.webp`, `diagrama-jornada-consulta.svg` e `ilustracao-contexto-saude.webp`. Os exemplos não pressupõem que esses materiais existam. Se um nome precisar mudar, atualize todas as referências.

Passe copy, design system e mapa estrutural à etapa 03 de direção de criação. Fotografia ou geração de ilustrações seguirá os briefings no escopo solicitado. Não declare revisão visual mobile concluída sem ter inspecionado a implementação.

## REGRAS DO SEGMENTO

1. Preserve a identidade e as decisões explicitamente aprovadas pelo usuário.
2. Distingua observação, estimativa, recomendação e informação desconhecida.
3. Não invente medidas exatas, fontes, cores ou estados que a referência não permite verificar.
4. Tipografia, paleta e ícones sugeridos precisam de origem clara; não substitua escolhas fornecidas automaticamente.
5. Legibilidade, foco e acesso ao atendimento devem permanecer claros no celular.
6. Conte todos os assets e ocorrências; cada asset recebe um tipo 01–08 e uma função.
7. Não invente profissionais, pacientes, avaliações, casos, resultados ou credenciais como elementos visuais.
8. Preserve a integridade das imagens reais. Unidade estética não autoriza alterar evidência clínica.
9. Não use logos de conselhos ou órgãos públicos como endosso da clínica.
10. Identifique categoria profissional e dados que a página deve exibir. Não trate toda clínica de saúde como clínica médica.
11. Para imagens de pacientes e resultados em publicidade médica, verifique o [Manual do CFM — Capítulo XII](https://publicidademedica.cfm.org.br/manual/aplicacao-pratica/capitulo-12); para outras profissões, use suas fontes oficiais. Registre fonte e data quando a decisão depender de norma.
12. Não oculte identificação, limites ou contexto necessário em legendas ilegíveis, overlays ou recortes mobile.
13. Não adicione escassez, métricas ou mensagens comerciais ausentes da copy aprovada.
14. Cada asset a produzir tem briefing adequado ao método de produção; nem todo asset precisa de prompt IA.
15. O checkpoint serve para uma escolha real pendente. Com direção autorizada, execute a entrega completa.
16. O resultado é uma especificação pronta para revisão. Não declare geração de imagens, implementação, testes ou publicação que não ocorreram.
