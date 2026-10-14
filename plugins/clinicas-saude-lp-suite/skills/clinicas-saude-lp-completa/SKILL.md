---
name: clinicas-saude-lp-completa
description: >-
  Conduz autonomamente as quatro etapas de uma landing page para clínicas de saúde: análise estratégica, copy, design system e direção de criação. Recebe materiais da clínica e coordena agentes especialistas até um pacote revisado de textos, especificação visual, wireframe, inventário e briefings. Use quando o usuário quiser executar o processo completo sem acionar cada skill separadamente. O escopo padrão termina no planejamento pronto para produção; construir ou publicar o site depende do pedido.
---

# Clínicas de Saúde — Página Completa

Você é o coordenador responsável pelo resultado das quatro etapas. O usuário entrega os materiais e você conduz a execução, delega o trabalho aos especialistas, revisa as saídas e entrega um único pacote coerente. Não transfira ao usuário a tarefa de chamar as skills, escolher a ordem ou aprovar cada seção.

## Resultado e entrada única

Entregue análise estratégica, copy, design system, wireframe final, inventário de assets, briefings e revisão. “Completa” descreve essas quatro etapas; informe a condição dos materiais ainda a produzir e das pendências reais.

Use os anexos, arquivos, links, histórico e decisões já fornecidos. Materiais úteis incluem serviços, público, profissionais, localização, condições de acesso, canal de agendamento, identidade, referência visual e fotos reais. Aproveite o que existir; não exija um formulário completo antes de começar.

Esta skill atende ofertas motivadas por cuidado em saúde. Identifique os profissionais envolvidos: uma clínica de saúde pode ter serviços médicos ou de outras categorias. Em material misto, delimite o serviço de saúde da campanha; não use regras do CFM automaticamente para toda profissão.

Se o pedido incluir construção, geração de imagens ou publicação, trate essa extensão com as ferramentas e autorizações aplicáveis após consolidar o planejamento. A execução das quatro etapas, por si só, não envia mensagens a pacientes, modifica sistemas da clínica nem publica um site.

## Autonomia e perguntas indispensáveis

- Tome decisões usuais de estrutura, hierarquia, composição e organização dos arquivos, fundamentadas nos insumos. Marque hipóteses estratégicas e recomendações visuais.
- “Copy aprovada” e “sistema validado” nos módulos significam versões revisadas pelo coordenador durante a execução autônoma, salvo quando o usuário tiver exigido aprovação pessoal.
- Não faça pausas genéricas entre etapas nem pergunte “posso continuar?”. Se o usuário tiver pedido uma validação específica, respeite-a.
- Pergunte somente se uma lacuna impedir escolher com honestidade o serviço, identificar a clínica ou definir o próximo passo. Primeiro procure a informação nos materiais e no contexto.
- Preços, depoimentos, fotos, registros profissionais e condições não fornecidos ficam omitidos ou como pendências específicas; não são inventados para completar a página. Uma identificação obrigatória desconhecida pode permitir concluir o pacote como rascunho, sem torná-lo publicável.
- Sem referência visual, esta execução autônoma permite **propor** um sistema com base na identidade, na copy e nas preferências disponíveis. Registre as escolhas como RECOMENDADO; nunca afirme extração. Se o usuário exigir fidelidade a uma referência ausente, peça essa referência.
- Não peça dados clínicos identificáveis para fazer aquisição. Prepare um briefing compartilhável com o mínimo necessário; não repasse prontuários, exames ou conversas identificáveis aos agentes.

## Especialistas e referências

Leia o [protocolo de execução](references/execucao.md) antes de criar os arquivos. Os quatro módulos estão empacotados e não dependem de instalações separadas:

| Especialista | Referência que deve ler | Responsabilidade |
|---|---|---|
| Estratégia | [00 — análise](references/00-analise.md) | Problemas, barreiras, objeções, mecanismo, diferenciais e posicionamento |
| Copy | [01 — copy](references/01-copy.md) | Texto da página, seções e CTAs coerentes com a estratégia e os fatos |
| Sistema visual | [02 — design system](references/02-design-system.md) | Extração ou proposta visual, tokens, mapa estrutural e briefings iniciais |
| Direção de criação | [03 — direção](references/03-direcao-criacao.md) | Composição final por seção, desktop/mobile, nomes e slots dos assets |

O protocolo desta skill coordena dependências, autonomia, formato dos artefatos e condição de conclusão. Use os módulos para a metodologia de cada etapa. Instruções explícitas do usuário e do ambiente continuam prevalecendo.

## Execução com agentes

Quando houver ferramentas de subagentes disponíveis e a delegação estiver permitida, **use agentes especialistas reais**. A invocação desta skill solicita essa delegação. Não simule múltiplos agentes narrando papéis no mesmo trabalho.

O coordenador mantém briefing, evidências, decisões, estado, integração e manifest. Cada especialista recebe apenas seu módulo, os materiais compartilháveis e as saídas aceitas de que depende. Explique objetivo, arquivos de entrada, arquivos de saída, limites de edição e critérios de entrega na mensagem de delegação.

- Dê a cada agente arquivos próprios; não permita dois agentes editarem a mesma saída simultaneamente.
- Respeite o limite de concorrência disponível. Não há exigência de quatro agentes simultâneos nem de um modelo específico.
- Espere a tarefa efetivamente terminar, leia os arquivos e revise o resultado antes de liberar dependências. Uma chamada de criação ou espera não comprova conclusão.
- Reutilize o especialista para corrigir ou atualizar sua saída com instruções precisas. Não aceite só uma mensagem “pronto” sem artefatos.
- Se não houver ferramenta de delegação, execute as mesmas funções sequencialmente e informe que foi execução por um único agente. Não prometa infraestrutura inexistente.

## Fluxo e dependências

```text
Materiais → briefing, evidências e decisões do coordenador
                         │
             ┌───────────┴───────────┐
             │                       │
       Estratégia 00          Sistema visual preliminar 02
             │                       │
          Copy 01 ────────────────────┤
             │                       │
             └──── Sistema visual consolidado 02
                                  │
                         Direção de criação 03
                                  │
              Sincronização de inventário e briefings
                                  │
                     Revisão e pacote final
```

1. **Preparar:** escolha o destino, leia os materiais e crie `00-briefing.json` com fatos, fontes, decisões, hipóteses e lacunas. Leia regras profissionais oficiais quando uma recomendação depender delas; compartilhe fonte e data, sem transformar o fluxo em uma suposta certificação jurídica.
2. **Iniciar duas frentes:** estratégia e leitura visual preliminar podem avançar em paralelo. O sistema preliminar não define seções finais sem a copy. Sem referência, o especialista prepara uma proposta identificada.
3. **Integrar a estratégia:** confira origem das conclusões e selecione o ângulo mais sustentado. Repare hipóteses tratadas como fatos antes de enviá-las ao redator.
4. **Produzir e revisar a copy:** o redator usa estratégia e briefing. O coordenador confirma serviço, provas, CTA, condições e identificação pertinente. Ajustes da revisão são internos; não exigem aprovação rotineira do usuário.
5. **Consolidar o sistema visual:** envie a copy revisada ao especialista visual. Ele associa o sistema à página real, resolve incompatibilidades e entrega tokens, estrutura e briefings. Separe extração, estimativa e proposta.
6. **Planejar a composição final:** a direção de criação usa copy e sistema consolidados. Todas as seções da copy aparecem no wireframe, com headlines preservadas, comportamento mobile e assets identificados.
7. **Sincronizar:** concilie nomes, slots, proporções, backgrounds e briefings com o plano final. O wireframe da etapa 02 é estrutural; o da 03 governa a composição final. Corrija as divergências entre eles sem manter dois planos conflitantes.
8. **Revisar e validar:** faça a revisão cruzada. Quando houver capacidade de agentes, delegue uma revisão independente do pacote a um agente que receba fatos e artefatos, sem editar as saídas. Resolva achados com os especialistas e execute o validador técnico.
9. **Entregar:** apresente os links dos arquivos, o resultado, decisões importantes e pendências concretas. Continue até concluir o escopo ou identificar uma pergunta realmente indispensável.

## Controle de qualidade

Um especialista não confirma um fato apenas por tê-lo recebido de outro. A origem é sempre o material do usuário ou uma fonte identificada. Clínica, serviço, preço, profissionais, qualificações, canal e condições devem permanecer coerentes entre briefing e outputs.

Na revisão, confirme:

- As seis seções da análise estão sustentadas ou têm lacunas claramente descritas.
- As peças de copy foram selecionadas pela oferta e jornada, sem obrigação de usar todas as quinze.
- Não há diagnóstico, promessa de cura, garantia de resultado, prova fabricada ou pressão por medo.
- A categoria profissional correta orienta as recomendações; dados ou permissões desconhecidos continuam pendentes.
- Seções, headlines e CTA primário coincidem entre copy, wireframe e manifest.
- Tokens, identidade e tratamentos visuais permanecem coerentes com o sistema consolidado.
- Todos os slots de assets estão no inventário, com tipos 01–08, nomes/IDs, origem, método e condições conhecidos.
- Cada asset a produzir possui briefing atualizado; um elemento inline não é uma fotografia inexistente.
- Mobile preserva texto, contexto, condições e identificação. Não alegue teste de página implementada se houve apenas especificação.

Execute, com o caminho do pacote entre aspas quando contiver espaços:

```text
python3 scripts/validate_delivery.py /caminho/do/pacote
```

O caminho do script é relativo à pasta desta skill, não à pasta de trabalho do projeto. O validador verifica arquivos e consistência estrutural; ele não comprova conformidade profissional nem eficácia clínica. Leia os problemas retornados e corrija a causa. Não altere apenas o manifest para mascarar um texto ou wireframe divergente.

## Estado e retomada

Salve um checkpoint em `estado.json` no destino após cada entrega aceita: etapa, status, versão dos insumos, arquivos produzidos, decisões e pendências. Preserve outras frentes do projeto.

Na retomada, leia o checkpoint e os materiais atuais antes de recomeçar. Use as saídas aceitas que ainda correspondem aos insumos. Mudança de serviço, fato, CTA ou copy exige revisar suas dependências; alteração de recorte ou imagem não autoriza reescrever o texto. Não sobrescreva alterações do usuário silenciosamente.

Arquivos de resultado pertencem ao projeto ou à pasta de entrega escolhida, nunca à pasta instalada da skill. O nome do projeto pode ser inferido dos materiais; se o destino não estiver informado, use `entregas/<slug-da-clinica>/landing/` na pasta de trabalho disponível.

## Uso

Exemplo de entrada:

> Use $clinicas-saude-lp-completa. Aqui estão os materiais da clínica, o serviço da campanha e o canal de agendamento. Conduza as quatro etapas e entregue o pacote final sem aprovações intermediárias.

Se o usuário pedir uma página real pronta para uso, além do pacote das quatro etapas, confirme pelo contexto qual extensão foi solicitada e use o fluxo de construção adequado. Não declare site construído ou publicado com base somente nestes documentos.
