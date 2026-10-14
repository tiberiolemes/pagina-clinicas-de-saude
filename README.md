<div align="center">

```text
╔══════════════════════════════════════════════════════════════════╗
║  CLÍNICAS DE SAÚDE · PÁGINA COMPLETA                            ║
║  estratégia → copy → sistema visual → direção de criação        ║
║  Codex · Claude Code · MIT                                       ║
╚══════════════════════════════════════════════════════════════════╝
```

**Agente autônomo para planejar landing pages de clínicas de saúde.**

[![Version](https://img.shields.io/badge/version-1.0.0-2563eb?style=for-the-badge)](plugins/clinicas-saude-lp-suite/.claude-plugin/plugin.json)
[![License](https://img.shields.io/badge/license-MIT-16a34a?style=for-the-badge)](LICENSE)
![Codex](https://img.shields.io/badge/Codex-supported-111827?style=for-the-badge)
![Claude Code](https://img.shields.io/badge/Claude%20Code-supported-111827?style=for-the-badge)

[English version below](#english)

</div>

## O que faz

A skill conduz, em uma só solicitação, análise estratégica, copy, design system, direção de criação, inventário de assets, briefings e revisão final. Coordena agentes especialistas quando a plataforma oferece essa capacidade e informa quando precisa trabalhar sequencialmente.

O pacote termina no planejamento pronto para produção. Construção ou publicação do site é uma extensão que precisa ser solicitada. A skill não substitui a revisão dos profissionais responsáveis nem certifica conformidade regulatória ou eficácia clínica.

## Instalação — Codex

Clone este repositório e copie a pasta da skill para seu diretório pessoal:

```bash
git clone https://github.com/tiberiolemes/pagina-clinicas-de-saude.git
mkdir -p ~/.agents/skills
cp -R pagina-clinicas-de-saude/plugins/clinicas-saude-lp-suite/skills/clinicas-saude-lp-completa ~/.agents/skills/
```

Abra/recarregue o Codex e invoque:

```text
$clinicas-saude-lp-completa
```

Para instalação apenas no projeto, copie para `.agents/skills/` na raiz do repositório.

## Instalação — Claude Code

Adicione o marketplace público e instale o plugin em escopo de usuário:

```text
/plugin marketplace add tiberiolemes/pagina-clinicas-de-saude
/plugin install clinicas-saude-lp-suite@tiberio-clinicas-saude
```

A skill aparece como `/clinicas-saude-lp-suite:clinicas-saude-lp-completa`. Para uso apenas em uma sessão local de desenvolvimento, clone o repo e inicie Claude Code com `--plugin-dir ./plugins/clinicas-saude-lp-suite`.

## Uso

Forneça os materiais disponíveis, delimite o serviço e o canal de conversão, e execute as quatro etapas:

```text
Use $clinicas-saude-lp-completa com estes materiais da clínica. Conduza análise, copy, design system e direção de criação até entregar o pacote completo.
```

Inclua fatos confirmados, documentos comerciais, identidade, referência visual e condições de agendamento quando disponíveis. A skill aproveita materiais parciais, registra lacunas e pergunta somente quando uma informação essencial impede escolher o serviço, identificar a clínica ou definir o próximo passo. Não envie prontuários ou dados clínicos identificáveis.

## Estrutura

```text
plugins/clinicas-saude-lp-suite/
├── .claude-plugin/plugin.json
├── agents/clinicas-saude-lp-completa-agent.md
└── skills/clinicas-saude-lp-completa/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    └── scripts/validate_delivery.py
```

## Licença e contribuição

Este pacote é público sob MIT; consulte [LICENSE](LICENSE). Contribuições e correções de conteúdo são bem-vindas conforme [CONTRIBUTING.md](CONTRIBUTING.md). A publicidade em saúde varia por profissão, procedimento, jurisdição e contexto. Confirme regras vigentes com fontes oficiais e os responsáveis profissionais antes de publicar conteúdo.

---

<a id="english"></a>

## English

**An autonomous agent for planning landing pages for healthcare clinics.** It coordinates four stages in one request: strategy, copy, design system, and creative direction, then delivers an asset inventory, production briefs, and a final review. It uses specialist agents when the host supports delegation and reports when it must work sequentially.

The default deliverable is a production-ready plan. Website implementation or publication must be separately requested. This workflow does not replace review by responsible professionals or certify regulatory compliance or clinical efficacy.

### Install — Codex

```bash
git clone https://github.com/tiberiolemes/pagina-clinicas-de-saude.git
mkdir -p ~/.agents/skills
cp -R pagina-clinicas-de-saude/plugins/clinicas-saude-lp-suite/skills/clinicas-saude-lp-completa ~/.agents/skills/
```

Reload Codex if needed, then invoke `$clinicas-saude-lp-completa`. For project-only use, copy it to `.agents/skills/` at your repository root.

### Install — Claude Code

```text
/plugin marketplace add tiberiolemes/pagina-clinicas-de-saude
/plugin install clinicas-saude-lp-suite@tiberio-clinicas-saude
```

Invoke `/clinicas-saude-lp-suite:clinicas-saude-lp-completa`. For one local development session, clone the repository and start Claude Code with `--plugin-dir ./plugins/clinicas-saude-lp-suite`.

### Use

Provide the available clinic materials, the service in scope, and the conversion channel. Ask the skill to complete all four stages and deliver the package. It records missing facts instead of inventing them and asks only when an essential gap prevents defining the service, clinic, or next step. Do not provide identifiable medical records or clinical data.

### License and contribution

This public package is licensed under MIT; see [LICENSE](LICENSE). Contributions are welcome under [CONTRIBUTING.md](CONTRIBUTING.md). Healthcare advertising rules vary by profession, procedure, jurisdiction, and context. Verify current requirements with official sources and the responsible professionals before publication.
