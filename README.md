# g1-tech-scraper

Script em Python que extrai manchetes e links da editoria de tecnologia do G1 e exporta tudo num `.csv`.

Criei esse projeto a fim de praticar scraping e entendê-lo desde suas raízes, sem uso de frameworks pesados por enquanto, só o essencial: `requests` pra fazer a requisição e `BeautifulSoup` pra vasculhar o HTML das páginas.

---

## O que o script faz

1. Faz uma requisição GET no portal do G1 com um `User-Agent` no header (se não, o servidor barra com 403);
2. Verifica se a resposta voltou com status 200 antes de tentar parsear qualquer coisa;
3. Percorre o DOM procurando as tags `<a class="feed-post-link">`, que é onde ficam os títulos e hrefs das matérias;
4. Limpa os textos capturados com `.get_text(strip=True)`;
5. Grava tudo num arquivo `noticias_g1.csv` com título e link em colunas separadas.

---

## Tecnologias

| Lib | Pra quê serve |
|---|---|
| `requests` | Requisição HTTP com header customizado |
| `beautifulsoup4` | Parsing e navegação pela estrutura HTML |
| `csv` | Exportação dos dados coletados |

---

## Como rodar

```bash
# Instala as dependências
pip install requests beautifulsoup4

# Executa
python scraper.py
```

O arquivo `noticias_g1.csv` aparecerá na mesma pasta do script.

---

## Observação

Sites de notícias mudam a estrutura do HTML com frequência. Se o script retornar uma lista vazia, provavelmente a classe CSS do feed mudou, e é só inspecionar o elemento no navegador e atualizar o seletor no código.

---

## Por que fiz isso

Queria entender na prática como scraping funciona antes de partir pra ferramentas que abstraem tudo. Fazer na mão me ajudou a entender o que acontece por baixo, antes de partir pra ferramentas de alto nível (como Selenium ou Scrapy).

O que aprendi no processo:

1. **Protocolo HTTP**: entendi a importância dos headers e como o `User-Agent` evita um 403 desnecessário, além de lidar com status codes na prática;
2. **Manipulação do DOM**: navegar por estruturas de árvore HTML pra filtrar exatamente o dado que interessa;
3. **Tratamento de dados**: pegar o dado bruto em memória e estruturá-lo num formato limpo dentro de um `.csv`.

---

## Próximos passos

O script funciona, mas tem limitações, então planejo melhorar os seguintes tópicos:

- **Tratamento de erros de rede**: alertas caso a conexão caia ou o site fique fora do ar;
- **Editorias configuráveis**: deixar o usuário escolher a editoria (`/economia`, `/politica`, etc.) direto pelo terminal;
- **Agendamento**: configurar pra rodar automaticamente uma vez por dia e acumular histórico;
- **Scroll infinito**: o G1 carrega mais conteúdo via requisições XHR, então a próxima versão usaria Selenium ou Playwright pra lidar com isso.
