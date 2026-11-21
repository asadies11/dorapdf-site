POSTS = [
dict(slug='juntar-pdf-unir-varios-arquivos-em-um-so', lang='pt', title='Juntar PDF: como unir vários arquivos em um só (grátis, sem cadastro e até pelo celular)', date='2026-11-20',
 desc='Juntar PDF grátis e sem cadastro: una vários arquivos em um só no navegador, acerte a ordem das páginas e deixe o arquivo pronto para enviar.',
 tools=['pdf-merger', 'pdf-compressor', 'rotate-pdf'], md="""
Matrícula na faculdade, inscrição em concurso, documentos de admissão no emprego novo, prestação de contas no fim do mês: o formulário tem um único campo de anexo e você tem seis PDFs soltos. Em vez de imprimir tudo e escanear de novo, dá para **juntar os PDFs em um só arquivo** em menos de um minuto.

O [PDF Merger](/pdf-merger/) do DoraPDF une arquivos PDF grátis, sem cadastro e sem marca d'água. Os arquivos são combinados dentro do seu navegador, sem upload para servidor. A tela da ferramenta está em inglês, mas são só três cliques, explicados aqui em português.

## Antes de começar: organize os arquivos

Dois minutos de preparo evitam refazer tudo depois.

- **Reúna tudo numa pasta só**, inclusive o que estiver no e-mail ou no WhatsApp.
- **Renomeie com números na frente**, na ordem que o destinatário espera: `01-requerimento.pdf`, `02-rg.pdf`, `03-comprovante-residencia.pdf`, `04-historico.pdf`.
- **Confira se tudo é PDF.** Foto de documento (JPG, PNG, HEIC) precisa virar PDF antes, com o [Images to PDF](/images-to-pdf/). Arquivo do Word, salve como PDF no próprio Word ou use o Word to PDF.

## Como juntar PDF online, passo a passo

1. Abra o [PDF Merger](/pdf-merger/).
2. Arraste os arquivos para a área de upload ou clique nela para escolher. É preciso adicionar **pelo menos dois PDFs**.
3. Confira a lista que aparece: os arquivos serão unidos **na ordem da lista**, de cima para baixo. A própria tela avisa: *"they merge in this order"*.
4. Adicionou algo errado? Remova pelo ✕ ao lado do nome.
5. Clique em **Merge PDFs** e baixe o arquivo `merged.pdf`.

Todas as páginas de cada arquivo entram no resultado, do jeito que estão. Uma página A4 em pé e uma planilha deitada convivem no mesmo PDF sem distorção.

## Como acertar a ordem das páginas

A lista não muda de ordem arrastando os nomes: cada arquivo novo entra no final. Por isso a ordem se resolve na hora de adicionar.

**Poucos arquivos:** adicione um de cada vez, já na sequência final. Primeiro o requerimento, depois o documento de identidade, depois os comprovantes.

**Muitos arquivos:** use a numeração no nome (`01-`, `02-`...) e selecione todos de uma vez numa pasta ordenada por nome. Normalmente eles chegam na ordem certa, mas olhe a lista antes de clicar no botão.

Errou mesmo assim? Tire os arquivos com o ✕ e adicione de novo na ordem correta. Como nada é enviado para servidor, refazer leva segundos.

## Juntar PDF pelo celular (Android e iPhone)

Não precisa instalar aplicativo. A ferramenta funciona no navegador do telefone.

- **Android:** abra a página no Chrome, toque na área de upload e escolha os PDFs no gerenciador de arquivos ou no Google Drive. O resultado vai para a pasta Downloads.
- **iPhone:** abra no Safari, toque na área de upload e escolha os arquivos no app Arquivos (o iCloud Drive aparece ali). O PDF unido fica em Arquivos, na pasta Downloads.

Recebeu os documentos pelo WhatsApp? Salve cada PDF no telefone primeiro (no Android, normalmente vão para a pasta do WhatsApp em Documentos; no iPhone, use *Compartilhar → Salvar em Arquivos*) e depois selecione na ferramenta.

## Checklist antes de enviar

Juntou? Antes de anexar, abra o `merged.pdf` e passe por esta lista rápida:

- **A ordem está certa?** Role até o fim e confira a sequência dos documentos.
- **Alguma página de lado?** Digitalizações feitas na horizontal costumam aparecer giradas. Corrija com o [Rotate PDF](/rotate-pdf/), escolhendo o ângulo e só as páginas que precisam (por exemplo `3, 7`).
- **Tem página sobrando?** Verso em branco, página repetida? Tire com o Delete PDF Pages, informando os números.
- **O tamanho cabe no limite?** Juntar várias digitalizações gera arquivos pesados. Se o portal ou o e-mail recusar, passe o resultado no [PDF Compressor](/pdf-compressor/): o modo *Smart* mantém o texto selecionável; o modo *Strong* reduz muito mais documentos escaneados.
- **O nome diz o que é?** Troque `merged.pdf` por algo como `documentos-admissao-maria-souza.pdf`.

## Problemas comuns e como resolver

**Aparece "Add at least 2 PDF files".** Você adicionou só um arquivo. Coloque pelo menos mais um.

**Um arquivo não entra na lista.** A ferramenta aceita apenas PDF. Converta fotos com o Images to PDF e documentos do Word com o Word to PDF.

**Um PDF com senha deu erro ou saiu estranho.** Arquivos que pedem senha para abrir podem não ser lidos corretamente. Se o documento é seu e você sabe a senha, abra no seu leitor de PDF, salve uma cópia sem proteção (por exemplo com *Imprimir → Salvar como PDF*) e use a cópia.

**No celular antigo está demorando.** Todo o trabalho é feito pelo próprio aparelho. Com muitos arquivos grandes, feche outras abas e tenha um pouco de paciência, ou faça a união no computador.

## Privacidade: seus documentos não saem do aparelho

O que a gente junta em PDF costuma ser sensível: RG, CPF, comprovante de residência, holerite, histórico escolar. O PDF Merger lê os arquivos e monta o documento final dentro do navegador. Nada é enviado aos servidores do DoraPDF e não é preciso criar conta.

## Perguntas frequentes

**Quantos PDFs posso juntar de uma vez?**
A ferramenta não define um número máximo. O limite prático é a memória do aparelho: dezenas de documentos comuns funcionam bem num computador.

**Juntar PDF diminui a qualidade?**
Não. As páginas são copiadas como estão, sem nova compressão. Texto, imagens e links continuam iguais.

**Dá para juntar só algumas páginas de cada arquivo?**
O PDF Merger une arquivos inteiros. Para usar só parte de um documento, extraia as páginas antes com o PDF Splitter e depois junte os arquivos extraídos.

**Tem marca d'água ou limite diário?**
Não. É grátis, sem marca d'água, sem limite de uso e sem cadastro.
"""),
dict(slug='converter-jpg-em-pdf-no-celular', lang='pt', title='Converter JPG em PDF no celular: transformar foto em PDF no Android e no iPhone', date='2026-11-20',
 desc='Como converter JPG em PDF no celular sem instalar app: várias fotos num só PDF, tamanho A4, fotos HEIC do iPhone e dicas para o documento ficar legível.',
 tools=['images-to-pdf', 'scan-to-pdf', 'pdf-compressor'], md="""
O site do concurso pede o RG em PDF. A empresa quer o comprovante de residência "digitalizado". A faculdade aceita o atestado só em PDF. Na prática, o que você tem é uma foto no celular. A boa notícia: **converter JPG em PDF no celular** leva menos de um minuto e não exige baixar nenhum aplicativo.

O [Images to PDF](/images-to-pdf/) do DoraPDF transforma uma ou várias fotos em um único PDF, direto no navegador do telefone, grátis e sem cadastro. As fotos são processadas no próprio aparelho, sem upload. A interface está em inglês; abaixo cada opção está explicada.

## O que você precisa saber antes

- **Formatos aceitos:** JPG, PNG, WebP e também **HEIC**, o formato padrão das fotos do iPhone. A conversão do HEIC é automática.
- **Cada foto vira uma página.** Cinco fotos geram um PDF de cinco páginas.
- **A ordem das páginas é a ordem da lista.** Isso importa para frente e verso de documentos.

## Passo a passo no Android

1. Abra o [Images to PDF](/images-to-pdf/) no Chrome (ou no navegador que você usa).
2. Toque na área de upload. O Android mostra opções como *Câmera*, *Fotos* ou *Arquivos*: escolha onde está a imagem.
3. Selecione uma ou várias fotos de uma vez.
4. Em **Page size**, escolha **A4 page** para documentos (explicação mais abaixo).
5. Toque em **Create PDF** e baixe. O arquivo vai para a pasta **Downloads**, de onde você pode anexar no e-mail, no portal ou no WhatsApp.

## Passo a passo no iPhone

1. Abra o [Images to PDF](/images-to-pdf/) no Safari.
2. Toque na área de upload e escolha **Fototeca** (ou *Escolher Arquivo*, se a imagem estiver no app Arquivos).
3. Marque as fotos e toque em *Adicionar*.
4. Ajuste **Page size** e **Margin**.
5. Toque em **Create PDF**. Depois do download, o PDF fica no app **Arquivos → Downloads**.

As fotos do iPhone costumam estar em HEIC. Você não precisa fazer nada: a ferramenta converte sozinha. Se o navegador for muito antigo e a foto não carregar, atualize o iOS ou, para as próximas fotos, ative *Ajustes → Câmera → Formatos → Mais Compatível*, que salva em JPG.

## As opções da tela, em português

### Page size (tamanho da página)

- **Fit page to image:** a página fica exatamente do tamanho e formato da foto. Bom para prints de tela, artes e fotos que serão vistas só na tela.
- **A4 page:** a foto é centralizada e ajustada numa folha A4. É a escolha certa para **documentos que vão para empresas, faculdades e órgãos públicos**, porque é o tamanho que eles imprimem.
- **US Letter:** tamanho americano, quase nunca usado no Brasil.

A orientação é automática: foto deitada vira página deitada; foto em pé, página em pé.

### Margin (margem)

*No margin*, *Small margin* (padrão) ou *Big margin*. Para documento em A4, a margem pequena fica com cara de digitalização. Para fotos que serão vistas no celular, sem margem aproveita melhor a tela.

PNG com fundo transparente ganha fundo branco no PDF.

## RG, CNH e outros documentos com frente e verso

Muita gente erra aqui: manda frente e verso em dois PDFs separados, ou em ordem trocada.

1. Fotografe a **frente** e depois o **verso**, em fotos separadas.
2. Adicione primeiro a frente e depois o verso. Cada foto nova entra no fim da lista, e a lista não se reordena arrastando, então a ordem de adição é a ordem final.
3. Escolha **A4 page** com margem pequena.
4. Gere o PDF e confira as duas páginas antes de enviar.

Precisa juntar documentos diferentes (RG, comprovante, certidão) num arquivo só? Gere um PDF por documento e una tudo com o PDF Merger, ou adicione todas as fotos de uma vez na ordem certa.

## Como tirar a foto para o PDF ficar legível

O PDF só fica tão bom quanto a foto. Alguns cuidados simples:

- **Luz natural, sem flash.** O flash cria reflexo em documento plastificado.
- **Celular paralelo ao papel**, bem de cima, para as linhas não ficarem tortas.
- **Fundo escuro e liso** embaixo de papel claro: as bordas ficam nítidas.
- **Só o documento no quadro**, sem a mesa em volta.
- **Toque na tela para focar** no texto antes de fotografar.

Quer resultado de scanner, com bordas recortadas e contraste melhor? Use o [Scan to PDF](/scan-to-pdf/): no celular ele abre a câmera, você arrasta os cantos para recortar e endireitar a página, escolhe um filtro de digitalização e exporta um PDF de várias páginas.

## Problemas comuns

**O PDF ficou grande demais para o site.** Fotos de celular são pesadas. Passe o arquivo no [PDF Compressor](/pdf-compressor/), modo *Strong* com qualidade *Balanced*, e confira se números pequenos continuam legíveis.

**A foto apareceu de lado.** Gire a foto na galeria, salve e adicione de novo. Se o PDF já estiver pronto, gire a página com o Rotate PDF.

**Preciso de um PDF para cada foto.** Converta uma foto por vez: cada conversão gera um PDF com o nome da imagem.

## Privacidade

Foto de RG, CNH, comprovante e holerite é exatamente o tipo de arquivo que você não quer espalhado por aí. O Images to PDF monta o PDF dentro do navegador: as fotos não são enviadas aos servidores do DoraPDF e não há cadastro.

## Perguntas frequentes

**Converter foto em PDF no celular é grátis?**
Sim, sem limite de uso, sem marca d'água e sem criar conta.

**Quantas fotos cabem num PDF?**
Não há número fixo. Depende da memória do aparelho. Em celulares mais simples, para muitas fotos, faça em grupos e depois junte os PDFs.

**A qualidade da foto cai?**
Imagens muito grandes são reduzidas para uma resolução ainda alta, suficiente para ler e imprimir em A4.

**Qual o nome do arquivo gerado?**
Com uma foto, o PDF leva o nome da imagem. Com várias, chama-se `images.pdf`. Renomeie antes de enviar.
"""),
dict(slug='remover-fundo-de-imagem-gratis-com-ia', lang='pt', title='Remover fundo de imagem grátis com IA: PNG transparente ou fundo branco em segundos', date='2026-11-20',
 desc='Remover fundo de imagem grátis com IA no navegador: PNG transparente ou fundo branco para fotos de produto, perfil e logos, sem enviar a foto a servidor.',
 tools=['image-background-remover', 'image-resizer', 'image-compressor'], md="""
Quem vende pela internet sabe: a mesma peça fotografada sobre a colcha da cama ou sobre um fundo branco limpo parece outro produto. E não é só loja. Foto de perfil profissional, logo para colocar num slide colorido, figurinha, convite: em todos esses casos dá vontade de **tirar o fundo da foto**.

O [Background Remover](/image-background-remover/) do DoraPDF remove o fundo de imagens com inteligência artificial, grátis e sem cadastro. O detalhe que faz diferença: a IA roda **dentro do seu navegador**, então a foto não é enviada para servidor nenhum. A tela da ferramenta está em inglês, mas tudo está explicado aqui.

## Para que serve, na prática

- **Foto de produto** com fundo branco para lojas virtuais, marketplaces e catálogo no WhatsApp Business.
- **Imagem com fundo transparente (PNG)** para colocar sobre outra cor ou foto: slides, banners, posts, convites.
- **Foto de perfil** mais limpa para currículo ou rede profissional.
- **Logo** que veio com fundo branco e precisa ficar sobre um fundo escuro.

## Como remover o fundo de uma foto

1. Abra o [Background Remover](/image-background-remover/).
2. Envie a imagem: JPG, PNG, WebP ou HEIC do iPhone.
3. Em **Mode**, escolha *Quick* ou *HD* (diferença logo abaixo).
4. Em **Background**, escolha o que vai no lugar do fundo antigo.
5. Clique em **Remove background**.
6. Arraste o controle deslizante para comparar o antes e o depois e baixe o PNG, que se chama `nome-da-foto-no-bg.png`.

Na primeira vez, o navegador baixa o modelo de IA, então demora um pouco mais. Nas próximas, começa bem mais rápido.

## Quick ou HD?

**⚡ Quick — pessoas e retratos.** Usa um modelo leve, de cerca de 13 MB, baixado uma única vez. É rápido e roda em quase qualquer aparelho, inclusive celular. Ideal para selfies, fotos de perfil e meio corpo.

**✨ HD — qualquer objeto.** Usa um modelo bem maior, de cerca de 115 MB, também baixado uma vez só. Reconhece melhor produtos, animais e contornos complicados. Precisa de um navegador moderno com aceleração por GPU (WebGPU). Se o seu não tiver, a ferramenta avisa e usa o modo Quick automaticamente.

**Regra simples:** pessoa → comece pelo Quick. Tênis, bolsa, caneca, planta, cachorro → HD.

## Qual fundo escolher

- **Transparent:** o famoso **PNG com fundo transparente**. Use quando a imagem vai ser colocada sobre outra coisa.
- **White:** fundo branco sólido, o padrão para foto de produto em muitas lojas online.
- **Black**, **Pink** e **Light grey:** opções prontas para artes e redes sociais.

Atenção com foto 3x4 ou foto para documento oficial: esses órgãos têm regras de iluminação, enquadramento e fundo. Um fundo branco colocado no computador nem sempre é aceito, então confira as exigências antes.

## Dicas para um recorte caprichado

A IA trabalha melhor quando a foto ajuda:

- **Contraste entre objeto e fundo.** Camiseta escura na frente de parede clara recorta melhor que camiseta branca na frente de parede branca.
- **Boa luz e foco.** Partes tremidas ou na sombra geram bordas indefinidas.
- **Objeto inteiro no quadro.** O que foi cortado pela borda da foto continua cortado.
- **Cabelo e pelo** são o desafio de qualquer ferramenta. Fundo liso atrás da cabeça ajuda muito; teste também o modo HD.
- **Vidro, garrafa transparente e objetos espelhados** continuam difíceis: espere alguma imperfeição.

Para foto de produto em série, monte um "estúdio" simples: uma cartolina clara apoiada na parede, formando uma curva até a mesa, e luz de janela de lado. As fotos ficam parecidas entre si e a IA recorta todas com mais facilidade.

## Depois do recorte: tamanho e peso do arquivo

O resultado é sempre PNG, formato que preserva a transparência. Imagens muito largas são reduzidas para 2000 pixels de largura, o que atende bem lojas virtuais, sites e apresentações.

- Plataforma pede **medida exata**, como imagem quadrada de 1000 x 1000? Ajuste com o [Image Resizer](/image-resizer/), por pixels ou porcentagem.
- Arquivo **pesado demais** para o site ou para o e-mail? O [Image Compressor](/image-compressor/) salva PNGs como WebP, bem mais leve e ainda com transparência. Só confira antes se o lugar onde você vai publicar aceita WebP.

## Quando algo dá errado

**"AI model could not load".** O modelo não foi baixado, quase sempre por conexão instável. Verifique a internet e tente de novo.

**Mensagem dizendo que não há GPU.** Seu navegador não tem WebGPU e a ferramenta usou o modo Quick. Uma versão recente do Chrome ou do Edge pode liberar o HD.

**A IA apagou parte do objeto.** Acontece quando objeto e fundo têm cores parecidas. Teste o outro modo ou fotografe de novo com um fundo mais contrastante.

**No celular ficou lento.** O processamento é feito no próprio aparelho. Prefira o modo Quick no telefone.

## Privacidade: a foto fica com você

Muitos removedores de fundo online enviam a imagem para um servidor. Aqui, o modelo de IA é baixado para o navegador e o processamento acontece no seu computador ou celular. Seu retrato, ou a foto de um produto que ainda nem foi lançado, não é enviado ao DoraPDF.

## Perguntas frequentes

**O modo HD também é grátis?**
Sim. Os dois modos são gratuitos, sem marca d'água e sem cadastro.

**Dá para remover o fundo de várias fotos de uma vez?**
A ferramenta trabalha com uma foto por vez. Depois que o modelo é carregado na primeira imagem, as seguintes levam poucos segundos.

**O PNG sai com marca d'água?**
Não, o arquivo baixado é limpo.

**Funciona sem internet?**
Na primeira vez é preciso conexão para baixar o modelo. O processamento em si acontece no aparelho.
"""),
dict(slug='extrair-texto-de-imagem-ocr-gratis', lang='pt', title='Extrair texto de imagem (OCR) grátis: como copiar o texto de uma foto ou print', date='2026-11-20',
 desc='Extrair texto de imagem grátis com OCR em português: copie o texto de fotos, prints e páginas de livro, com dicas para menos erros com acentos e ç.',
 tools=['image-to-text', 'pdf-ocr', 'scan-to-pdf'], md="""
Você tem o texto na sua frente, mas não consegue selecionar: é a foto de uma página de livro, o print de um slide da aula, a imagem de um comunicado que chegou no grupo, um documento antigo que só existe impresso. Digitar tudo de novo cansa e gera erro. A solução é **extrair o texto da imagem** com OCR, o reconhecimento óptico de caracteres, que "lê" as letras da foto e devolve texto editável.

O [Image to Text](/image-to-text/) do DoraPDF faz isso de graça e sem cadastro. O reconhecimento acontece no seu navegador: a imagem não é enviada para servidor. A tela está em inglês, mas o idioma do texto reconhecido você escolhe, e **português está na lista**.

## Copiar texto de imagem em 5 passos

1. Abra o [Image to Text](/image-to-text/).
2. Envie uma ou mais imagens: JPG, PNG, WebP, foto HEIC do iPhone ou print de tela.
3. No menu **Language**, escolha **Portuguese**.
4. Clique em **Extract text**.
5. O texto aparece numa caixa. Corrija ali mesmo se quiser e depois clique em **Copy text** ou baixe o arquivo `.txt`.

Na primeira vez que você usa um idioma, o navegador baixa o modelo de reconhecimento dele (de 2 a 10 MB, aproximadamente). Depois disso, o processo começa mais rápido.

Enviou várias imagens? O texto de cada uma vem separado por uma linha com o nome do arquivo, assim você sabe de qual foto saiu cada trecho.

## Por que escolher "Portuguese" faz tanta diferença

O OCR não olha só o desenho das letras: ele também usa o conhecimento do idioma para decidir entre opções parecidas. Com o idioma em inglês, palavras como *atenção*, *não*, *pôr* e *você* costumam sair sem acento ou com caracteres trocados. Com **Portuguese**, o ç, o til e os acentos são reconhecidos muito melhor.

Outros idiomas disponíveis: inglês, espanhol, francês, alemão, italiano, turco, russo, árabe, urdu, hindi, indonésio e chinês simplificado. Texto misturado, como um artigo em português com citações em inglês? Escolha o idioma que predomina e revise o restante.

## Usos do dia a dia

- **Estudo:** transformar páginas de livro fotografadas na biblioteca em fichamento; passar slides fotografados para as suas anotações.
- **Trabalho:** reaproveitar o texto de um documento impresso sem redigitar; copiar dados de um panfleto ou cartaz.
- **Burocracia:** copiar endereço, número de protocolo ou código que está só numa foto.
- **Acessibilidade:** ter o texto em formato que pode ser ampliado, traduzido ou lido em voz alta por leitor de tela.

## Como tirar a foto para o OCR acertar mais

A qualidade da imagem pesa mais que qualquer configuração. Antes de fotografar:

1. **Luz uniforme.** Cuidado com a sombra da sua mão ou do celular sobre a página.
2. **Foto reta, de frente.** Linhas inclinadas ou curvas, como as perto da lombada do livro, são as mais difíceis.
3. **Chegue perto.** O texto deve ocupar quase toda a foto. Duas fotos nítidas de meia página rendem mais que uma foto borrada da página inteira.
4. **Nada de zoom digital.** Aproxime o celular em vez de ampliar na tela.
5. **Na tela, use print.** Se o texto está num monitor ou no celular, um print sempre dá resultado melhor que fotografar a tela.

Para documentos de várias páginas, vale passar antes pelo [Scan to PDF](/scan-to-pdf/), que recorta, endireita e melhora o contraste das páginas.

## O que o OCR ainda faz mal

Melhor saber antes para não perder tempo:

- **Letra de mão.** O reconhecimento é feito para texto impresso; com caligrafia o resultado costuma ser fraco.
- **Tabelas.** O texto sai linha por linha. Os números estão lá, mas as colunas precisam ser arrumadas numa planilha.
- **Fontes decorativas**, texto sobre foto, letras muito pequenas ou desbotadas.
- **Páginas com várias colunas** (jornal, revista): as colunas podem se misturar. Recorte a foto e faça uma coluna por vez.

Sempre revise números, datas e nomes próprios. Trocas como *1* por *l* e *0* por *O* são os erros mais comuns.

## E se o arquivo for um PDF escaneado?

O Image to Text trabalha com imagens. Para PDF escaneado, use o [PDF OCR](/pdf-ocr/): ele processa até 60 páginas e devolve um PDF com a mesma aparência, mas com texto selecionável e pesquisável, além de um arquivo de texto. Lá você também escolhe **Portuguese**.

## Privacidade

As imagens das quais se extrai texto muitas vezes são pessoais: anotações, contratos, documentos. O Image to Text baixa o modelo de reconhecimento para o navegador e processa a foto no seu aparelho. Nem a imagem nem o texto reconhecido são enviados aos servidores do DoraPDF.

## Perguntas frequentes

**Extrair texto de imagem é grátis?**
Sim, sem limite de uso, sem marca d'água e sem conta.

**Funciona no celular?**
Sim, em qualquer navegador atual. No telefone pode levar alguns segundos a mais, porque o cálculo é feito no aparelho.

**O texto mantém negrito e formatação?**
Não. O resultado é texto simples. Cole no Word ou no Google Docs e formate por lá.

**Reconhece português com acento e cedilha?**
Sim, desde que você selecione **Portuguese** no menu de idioma antes de clicar em Extract text.

**Posso processar várias fotos juntas?**
Pode. Envie várias imagens e você recebe um único texto, separado por arquivo.
"""),
dict(slug='pdf-naar-word-omzetten-zonder-opmaak-te-verliezen', lang='nl', title='PDF naar Word omzetten zonder dat de opmaak verdwijnt (gratis, in je browser)', date='2026-11-20',
 desc='PDF naar Word omzetten met behoud van opmaak: welke modus je kiest, hoe je het .docx-bestand netjes bewerkt en wat je doet met een gescande PDF.',
 tools=['pdf-to-word', 'pdf-ocr', 'word-to-pdf'], md="""
Een huurcontract waarin één datum moet veranderen. Een aanmeldformulier van de sportclub dat je liever typt dan met de hand invult. Een oud cv dat je alleen nog als PDF hebt. In al die gevallen wil je de PDF **omzetten naar Word**, aanpassen en daarna weer opslaan. Het probleem dat iedereen kent: na het omzetten staan tabellen scheef, zijn kopjes verdwenen of springt de tekst alle kanten op.

Met de [PDF to Word](/pdf-to-word/)-converter van DoraPDF zet je een PDF gratis om naar een bewerkbaar .docx-bestand, zonder account en zonder je bestand te uploaden. De conversie gebeurt in je browser. Het scherm van de tool is in het Engels, maar je hebt maar één keuze te maken, en die leggen we hieronder uit.

## In vijf stappen van PDF naar Word

1. Open [PDF to Word](/pdf-to-word/) op je pc, Mac, tablet of telefoon.
2. Sleep de PDF naar het uploadvak of klik erop om een bestand te kiezen.
3. Kies bij **Layout** een van de twee modi (zie hieronder).
4. Start de conversie. Bij lange documenten duurt het iets langer, omdat je eigen apparaat het werk doet.
5. Download het **.docx**-bestand. Het krijgt dezelfde naam als je PDF.

Het bestand opent in Microsoft Word, LibreOffice Writer, Google Documenten en Pages.

## De belangrijkste keuze: welke modus?

### Keep original layout (aanbevolen)

Dit is de standaardinstelling en de modus die je wilt als **het document er hetzelfde uit moet blijven zien**. Elke Word-pagina toont de oorspronkelijke PDF-pagina: achtergrond, afbeeldingen, lijnen en kaders blijven op hun plek. Daarbovenop wordt de tekst opnieuw opgebouwd als echte, bewerkbare tekst, met lettertype, vet, cursief, kleur en grootte zo dicht mogelijk bij het origineel.

Ideaal voor:

- een formulier dat je digitaal wilt invullen;
- een brief op briefpapier waarin een adres of datum verandert;
- een folder of uitnodiging met een kleine correctie.

Goed om te weten: elke tekstregel staat in deze modus op een vaste plek op de pagina. Perfect voor kleine aanpassingen, minder handig als je hele alinea's herschrijft, want de tekst loopt niet vanzelf door naar de volgende regel. Schuine tekst, zoals een stempel, blijft onderdeel van de achtergrond.

### Text only

Hier haalt de converter alleen de tekst uit de PDF en zet die in gewone, doorlopende alinea's. Regels die duidelijk groter zijn dan de rest worden vetgedrukte kopjes, en elke PDF-pagina begint op een nieuwe pagina. Afbeeldingen en vormgeving gaan niet mee.

Kies deze modus als het je om de **inhoud** gaat: stukken uit een rapport hergebruiken, een reglement aanpassen voor je eigen vereniging, aantekeningen verder uitwerken.

**Kort gezegd:** kleine wijziging, zelfde uiterlijk → *Keep original layout*. Tekst herschrijven → *Text only*.

## "No text found"? Dan is je PDF gescand

Veel PDF's bevatten geen echte tekst maar foto's van pagina's: alles wat door een scanner is gegaan, documenten die je met je telefoon hebt gefotografeerd en veel oude archiefstukken. De converter stopt dan met de melding *"No text found — this PDF looks scanned"*.

Zo los je dat op:

1. Open [PDF OCR](/pdf-ocr/) en laad dezelfde PDF.
2. Kies bij de taal **English**. Nederlands staat (nog) niet in de lijst, maar Nederlandse tekst gebruikt grotendeels dezelfde letters, dus dit werkt meestal goed.
3. Start de OCR. De tool verwerkt tot 60 pagina's en geeft je een PDF met selecteerbare tekst, plus een tekstbestand.
4. Zet die nieuwe PDF om met PDF to Word en controleer woorden met ë, ï of é, zoals *ideeën* of *café*.

Snelle test of een PDF gescand is: probeer met je muis één woord te selecteren. Wordt de hele pagina blauw als één plaatje, dan heb je OCR nodig.

## Bewerken zonder dat alles verschuift

Een paar gewoontes die veel ergernis schelen:

- **Schrijf in de layoutmodus niet langer dan het origineel.** Een langere zin loopt over de volgende regel heen. Kort in, maak de letter een punt kleiner, of kies bij veel wijzigingen alsnog voor *Text only*.
- **Ander lettertype?** De PDF gebruikte een font dat niet op je computer staat, dus Word kiest een vervanger. Is het uiterlijk belangrijk, selecteer dan alles en kies een standaardfont als Arial of Calibri.
- **Tabellen** zijn in de layoutmodus tekst bovenop een getekende tabel. Je kunt de inhoud aanpassen, maar geen rijen toevoegen. Wil je met de cijfers rekenen, kopieer ze dan uit de *Text only*-versie naar Excel.
- **Bewaar het origineel.** Werk altijd in een kopie, zodat je kunt vergelijken.

## Klaar? Terug naar PDF

Om te versturen of af te drukken zet je het document weer om naar PDF. In Word via *Bestand → Opslaan als → PDF*, in Google Documenten via *Bestand → Downloaden → PDF-document*. Geen programma bij de hand? Met [Word to PDF](/word-to-pdf/) zet je een .docx direct in je browser om.

## Privacy: je document blijft op je apparaat

Contracten, loonstroken en formulieren met je BSN wil je niet zomaar ergens uploaden. Bij PDF to Word wordt de PDF in je browser gelezen en verwerkt, op je eigen computer of telefoon. Er gaat niets naar de servers van DoraPDF en je hoeft geen account aan te maken.

## Veelgestelde vragen

**Is PDF naar Word omzetten bij DoraPDF echt gratis?**
Ja. Geen abonnement, geen watermerk en geen registratie.

**Kan ik meerdere PDF's tegelijk omzetten?**
Nee, de tool zet één bestand per keer om. Een conversie duurt meestal maar een paar seconden.

**Werkt het op mijn iPhone of Android-telefoon?**
Ja, in de browser. Op oudere telefoons duurt een lang document wat langer.

**Waarom kan ik de afbeeldingen in Word niet verplaatsen?**
In de layoutmodus vormen afbeeldingen en vormgeving de achtergrond van de pagina, zodat alles op zijn plek blijft. De tekst erboven is wel bewerkbaar.

**Werkt het met een beveiligde PDF?**
Vraagt de PDF om een wachtwoord om te openen, dan kan de converter hem niet lezen. Is het jouw document en ken je het wachtwoord, open het dan in je PDF-lezer, sla een onbeveiligde kopie op (bijvoorbeeld via *Afdrukken → Opslaan als PDF*) en zet die om.
"""),
dict(slug='pdf-verkleinen-voor-email-en-uploads', lang='nl', title='PDF verkleinen voor e-mail en uploads: zo maak je een te grote PDF kleiner', date='2026-11-20',
 desc='PDF verkleinen gratis en zonder upload: het verschil tussen Smart en Strong, hoe de tekst leesbaar blijft en wat je doet als de PDF nog steeds te groot is.',
 tools=['pdf-compressor', 'pdf-splitter', 'delete-pdf-pages'], md="""
"Bestand is te groot." Die melding krijg je precies op het moment dat het niet uitkomt: bij een sollicitatie die vandaag de deur uit moet, bij het uploaden van bewijsstukken voor je zorgverzekeraar of bij een mail naar je boekhouder met een stapel gescande bonnen. Bijna altijd zit het probleem in gescande of gefotografeerde pagina's die als enorme afbeeldingen in de PDF zitten. De oplossing: de **PDF verkleinen**.

Met de [PDF Compressor](/pdf-compressor/) van DoraPDF maak je een PDF gratis kleiner, zonder account en zonder je bestand te uploaden: het comprimeren gebeurt in je browser. De tool is in het Engels; alle opties staan hieronder in het Nederlands uitgelegd.

## Eerst even: hoe groot mag het zijn?

Dat verschilt per dienst. Gmail accepteert bijvoorbeeld bijlagen tot 25 MB per bericht en biedt daarboven een Google Drive-link aan. Andere mailproviders hanteren vergelijkbare of lagere grenzen, en de mailserver van de ontvanger kan strenger zijn. Uploadformulieren van werkgevers, gemeenten en verzekeraars vermelden de maximale bestandsgrootte meestal bij het uploadveld.

Mik ruim onder de grens. Bijlagen worden bij verzending gecodeerd en worden daardoor groter dan het bestand op je schijf.

## PDF kleiner maken in vijf stappen

1. Open de [PDF Compressor](/pdf-compressor/).
2. Sleep je PDF naar het uploadvak of klik om een bestand te kiezen.
3. Kies bij **Mode** voor *Smart* of *Strong*.
4. Bij *Strong* kies je ook de beeldkwaliteit: *High quality*, *Balanced* (standaard) of *Smallest*.
5. Klik op **Compress** en download `bestandsnaam-compressed.pdf`. Naast de naam zie je hoeveel procent kleiner het bestand is geworden.

## Smart of Strong: wat is het verschil?

**Smart houdt de tekst selecteerbaar.** Deze modus herschikt de interne structuur van de PDF zonder iets aan de inhoud te veranderen. Tekst, links en kwaliteit blijven precies hetzelfde. De winst is meestal bescheiden, en is de PDF al geoptimaliseerd, dan meldt de tool *"already optimised"*. De beste keuze voor PDF's die uit Word of een ander programma komen.

**Strong geeft maximale compressie.** Elke pagina wordt opnieuw getekend en als JPG-afbeelding opgeslagen in de kwaliteit die je kiest. Bij gescande documenten scheelt dat vaak flink. De keerzijde: tekst is daarna niet meer selecteerbaar of doorzoekbaar, links werken niet meer en invulvelden worden onderdeel van het plaatje.

| Soort PDF | Begin met |
|---|---|
| Rapport, offerte of factuur uit een programma | Smart |
| Gescande of gefotografeerde documenten | Strong + Balanced |
| Strong + Balanced nog te groot | Strong + Smallest |

## Leesbaar blijven: de controle die mensen overslaan

De grootste fout is de sterkste stand kiezen en het resultaat ongezien versturen. Doe na het comprimeren altijd dit:

1. Open het nieuwe bestand.
2. **Zoom in op de kritieke plekken:** kleine cijfers, bedragen, IBAN-nummers, handtekeningen, stempels.
3. Alles scherp en onder de grens? Klaar.
4. Te wazig? Ga een stap terug in kwaliteit en maak de PDF op een andere manier kleiner (zie hieronder).

Comprimeer altijd vanaf het **originele bestand**. Twee keer Strong achter elkaar comprimeert al gecomprimeerde afbeeldingen opnieuw, en dat gaat ten koste van de leesbaarheid.

## Nog steeds te groot? Drie uitwegen

**Haal overbodige pagina's weg.** Lege achterkanten van een scan, dubbele pagina's, algemene voorwaarden die de ontvanger al heeft. Met [Delete PDF Pages](/delete-pdf-pages/) vul je de paginanummers in (bijvoorbeeld `2, 4-6`) en je krijgt een PDF zonder die pagina's. Doe dit vóór het comprimeren.

**Splits het bestand.** Accepteert het formulier meerdere bijlagen, of kun je twee mails sturen? Met de [PDF Splitter](/pdf-splitter/) haal je paginabereiken uit een PDF (bijvoorbeeld `1-10` en `11-20`) of maak je van elke pagina een apart bestand.

**Comprimeer per onderdeel.** Moet je meerdere documenten samen opsturen, comprimeer ze dan eerst los en voeg ze daarna samen met de PDF Merger. Zo bepaal je per document hoeveel kwaliteit je inlevert.

## Scannen met het eindformaat in gedachten

- Voor tekstdocumenten is **200 tot 300 dpi** ruim voldoende.
- Scan in **grijstinten** als kleur er niet toe doet.
- Fotografeer je met je telefoon, zet dan alleen het document in beeld, zonder tafel eromheen.

## Privacy: je bestand verlaat je apparaat niet

Wat je per mail of upload verstuurt, bevat vaak persoonsgegevens: loonstroken, een kopie van je ID-bewijs (maak daar bij voorkeur een veilige kopie van met afgeschermd BSN), bankafschriften, medische declaraties. De PDF Compressor verwerkt je bestand in de browser. Er gaat niets naar de servers van DoraPDF en een account is niet nodig.

## Veelgestelde vragen

**Gaat de kwaliteit achteruit als ik een PDF verklein?**
In Smart-modus niet: de inhoud blijft identiek. In Strong-modus worden pagina's gecomprimeerde afbeeldingen; met *High quality* of *Balanced* is het verschil op een scherm meestal klein.

**Kan ik een PDF verkleinen op mijn telefoon?**
Ja, in de browser van je Android-telefoon of iPhone. Lange PDF's in Strong-modus duren wat langer, omdat je telefoon elke pagina zelf verwerkt.

**Mijn PDF is nauwelijks kleiner geworden. Hoe kan dat?**
Waarschijnlijk heb je Smart gebruikt op een gescand of al geoptimaliseerd bestand. Probeer Strong.

**Kan ik meerdere PDF's tegelijk verkleinen?**
De tool werkt met één bestand per keer. Horen ze bij elkaar, voeg ze dan eerst samen en comprimeer het resultaat.
"""),
dict(slug='pdf-samenvoegen-tot-een-bestand', lang='nl', title='PDF samenvoegen tot één bestand: gratis, zonder account en ook op je telefoon', date='2026-11-20',
 desc='PDF samenvoegen tot één bestand, gratis en zonder upload: in de juiste volgorde, op pc of telefoon, met een checklist voor hypotheek, huur en sollicitatie.',
 tools=['pdf-merger', 'rotate-pdf', 'pdf-compressor'], md="""
Een hypotheekadviseur die "alles in één PDF graag" wil. Een woningcorporatie of verhuurder met één uploadveld voor loonstroken, werkgeversverklaring en ID. Een vacature waar cv en motivatiebrief samen in één bijlage moeten. Je kunt alles printen en opnieuw scannen, maar sneller is het om de **PDF's samen te voegen** tot één bestand.

De [PDF Merger](/pdf-merger/) van DoraPDF voegt PDF-bestanden gratis samen, zonder account en zonder watermerk. Je bestanden worden in je eigen browser gecombineerd en niet geüpload. Het scherm is in het Engels, maar de stappen zijn simpel.

## Zo voeg je PDF-bestanden samen

1. Open de [PDF Merger](/pdf-merger/).
2. Sleep je bestanden naar het uploadvak of klik om ze te kiezen. Je hebt er **minstens twee** nodig.
3. Bekijk de lijst. De bestanden worden samengevoegd **in de volgorde van de lijst**, van boven naar beneden.
4. Per ongeluk het verkeerde bestand toegevoegd? Klik op het ✕ naast de naam.
5. Klik op **Merge PDFs** en download `merged.pdf`.

Alle pagina's van elk bestand komen erin, zoals ze zijn. Een staande A4-brief en een liggend overzicht kunnen gewoon in hetzelfde document zitten.

## De volgorde goed krijgen

Je kunt de lijst niet herschikken door namen te verslepen: elk nieuw bestand komt onderaan. De volgorde regel je dus bij het toevoegen.

**Weinig bestanden?** Voeg ze één voor één toe, meteen in de juiste volgorde.

**Veel bestanden?** Zet een nummer voor de bestandsnaam: `01-aanvraagformulier.pdf`, `02-id-bewijs.pdf`, `03-loonstrook-sept.pdf`. Selecteer ze daarna in één keer vanuit een map die op naam is gesorteerd. Meestal komen ze dan in de goede volgorde binnen; kijk de lijst toch even na.

Fout gegaan? Haal de bestanden weg met het ✕ en voeg ze opnieuw toe. Omdat er niets geüpload wordt, ben je zo klaar.

## Checklists voor veelvoorkomende situaties

Vraag altijd na welke volgorde de ontvanger wil. Staat er niets, dan werkt een logische opbouw het best.

**Hypotheek of huurwoning**
1. Ingevuld aanvraagformulier
2. Kopie ID-bewijs (voor- en achterkant)
3. Werkgeversverklaring
4. Recente loonstroken, nieuwste eerst of oudste eerst, maar consequent
5. Bankafschriften of overige bewijsstukken

**Sollicitatie**
1. Motivatiebrief
2. Cv
3. Diploma's of certificaten, als daarom gevraagd wordt

**Administratie voor de btw-aangifte of je boekhouder**
Facturen en bonnen per maand of kwartaal, gesorteerd op datum. Geef het bestand een duidelijke naam, zoals `inkoopfacturen-2026-Q4.pdf`.

## Samenvoegen op je telefoon

Geen app nodig: het werkt in de browser.

- **Android:** open de pagina in Chrome en kies de PDF's via Bestanden of Google Drive. Het resultaat staat in Downloads.
- **iPhone:** open de pagina in Safari en kies de bestanden in de Bestanden-app (ook iCloud Drive). Na het downloaden vind je de PDF in *Bestanden → Downloads*.

Heb je sommige documenten alleen als foto? Zet ze eerst om met [Images to PDF](/images-to-pdf/) en voeg ze daarna samen.

## Na het samenvoegen: even nalopen

**Pagina's op hun kant?** Een liggend gescande pagina staat in het samengevoegde bestand vaak scheef. Met [Rotate PDF](/rotate-pdf/) draai je alle pagina's of alleen bepaalde, bijvoorbeeld `3, 7`.

**Bestand te groot voor het uploadveld?** Meerdere scans bij elkaar worden al snel zwaar. Haal het resultaat door de [PDF Compressor](/pdf-compressor/): *Smart* houdt de tekst selecteerbaar, *Strong* maakt gescande documenten veel kleiner.

**Lege pagina's of dubbele scans?** Verwijder ze met Delete PDF Pages door de paginanummers in te vullen.

**Bestandsnaam.** `merged.pdf` zegt de ontvanger niets. Maak er `hypotheekaanvraag-de-vries.pdf` van.

## Als het niet lukt

**"Add at least 2 PDF files".** Je hebt maar één bestand toegevoegd. Voeg er minstens één bij.

**Een bestand wordt niet geaccepteerd.** De tool werkt alleen met PDF's. Een Word-bestand sla je eerst op als PDF (of gebruik Word to PDF), een foto zet je om met Images to PDF.

**Een beveiligde PDF geeft problemen.** Vraagt een bestand om een wachtwoord bij het openen, open het dan in je PDF-lezer en sla een onbeveiligde kopie op voordat je gaat samenvoegen.

**Traag op een oudere telefoon.** Je apparaat doet al het werk. Sluit andere tabbladen of voeg grote bestanden samen op een computer.

## Privacy: je documenten blijven bij jou

Juist bij samenvoegen gaat het vaak om gevoelige papieren: ID-bewijs, loonstroken, bankafschriften. De PDF Merger leest je bestanden en bouwt het nieuwe document in je browser. Er wordt niets opgeslagen op de servers van DoraPDF en je hebt geen account nodig.

## Veelgestelde vragen

**Hoeveel PDF's kan ik samenvoegen?**
De tool heeft geen vast maximum. De praktische grens is het geheugen van je apparaat; tientallen gewone documenten zijn op een computer geen probleem.

**Gaat er kwaliteit verloren bij het samenvoegen?**
Nee. Pagina's worden ongewijzigd gekopieerd, zonder extra compressie. Tekst, afbeeldingen en links blijven hetzelfde.

**Kan ik maar een paar pagina's uit een PDF meenemen?**
De PDF Merger voegt hele bestanden samen. Haal de pagina's die je nodig hebt eerst uit het document met de PDF Splitter en voeg die daarna samen.

**Zit er een watermerk of daglimiet op?**
Nee. Gratis, zonder watermerk, zonder limiet en zonder registratie.
"""),
dict(slug='jpg-naar-pdf-omzetten-telefoon-pc', lang='nl', title="JPG naar PDF omzetten op je telefoon en pc: foto's in één PDF, op A4", date='2026-11-20',
 desc="JPG naar PDF omzetten zonder app: meerdere foto's in één PDF, A4-formaat, iPhone-foto's (HEIC) en tips voor een leesbare foto van je document.",
 tools=['images-to-pdf', 'scan-to-pdf', 'heic-to-jpg'], md="""
Een foto van je rijbewijs, een kassabon voor de garantie, de handgeschreven aantekeningen van een vergadering: je hebt ze als foto, maar het formulier accepteert alleen PDF. Gelukkig is **JPG naar PDF omzetten** in een paar tikken gedaan, op je telefoon én op je computer, zonder iets te installeren.

Met [Images to PDF](/images-to-pdf/) van DoraPDF zet je één of meer foto's om in één PDF, gratis en zonder account. De foto's worden op je eigen apparaat verwerkt en niet geüpload. Het scherm is in het Engels; hieronder staat elke optie in het Nederlands uitgelegd.

## Welke bestanden kun je gebruiken?

Naast **JPG** werkt de tool met PNG, WebP en **HEIC**, het standaardformaat van iPhone-foto's. HEIC wordt automatisch omgezet. Elke foto wordt één pagina in de PDF, in de volgorde van de lijst.

## Op de computer: slepen en klaar

Op een pc of Mac is dit de snelste manier:

1. Open [Images to PDF](/images-to-pdf/).
2. Open de map met je foto's, selecteer ze en sleep ze in één keer naar het uploadvak.
3. Kijk de lijst na. De pagina's komen in **deze volgorde** in de PDF. Een foto verwijderen doe je met het ✕ naast de naam.
4. Kies **Page size** en **Margin**.
5. Klik op **Create PDF** en download het bestand.

Tip: heb je de foto's een nummer gegeven (`01.jpg`, `02.jpg` ...), dan komen ze meestal al in de juiste volgorde binnen.

## Op je telefoon

**iPhone:** open de pagina in Safari, tik op het uploadvak en kies *Fotobibliotheek*. Selecteer de foto's en tik op *Voeg toe*. Na het downloaden staat de PDF in de Bestanden-app, map Downloads.

**Android:** open de pagina in Chrome, tik op het uploadvak en kies je foto's uit de galerij of uit Bestanden. De PDF komt in de map Downloads terecht.

De lijst laat zich niet herschikken door te slepen: elke nieuwe foto komt onderaan. Is de volgorde belangrijk, voeg de foto's dan één voor één toe in de goede volgorde.

## De opties uitgelegd

### Page size

- **Fit page to image:** de pagina krijgt precies de verhoudingen van de foto. Handig voor schermafbeeldingen en foto's die je alleen op een scherm bekijkt.
- **A4 page:** de foto wordt gecentreerd en geschaald op een A4-pagina. Kies dit voor **documenten die je afdrukt of naar een instantie, werkgever of verzekeraar stuurt**: A4 is hier de standaard.
- **US Letter:** het Amerikaanse formaat, in Nederland en België zelden nodig.

De oriëntatie gaat vanzelf: een liggende foto komt op een liggende pagina.

### Margin

*No margin*, *Small margin* (standaard) of *Big margin*. Voor een document op A4 ziet een smalle marge er netjes uit, als een echte scan. Doorzichtige delen van een PNG worden wit in de PDF.

## Voorbeeld: ID-bewijs of rijbewijs, voor- en achterkant

1. Maak twee aparte foto's: eerst de voorkant, dan de achterkant.
2. Voeg ze in die volgorde toe.
3. Kies **A4 page** met **Small margin**.
4. Maak de PDF en controleer beide pagina's.

Moet je een kopie van je ID-bewijs delen, scherm dan je BSN en pasfoto af als de ontvanger daar niet om vraagt. De Rijksoverheid biedt hiervoor de KopieID-app aan; vraag bij twijfel na wat de ontvanger precies nodig heeft.

## Zo maak je een foto die goed leesbaar blijft

- **Daglicht, geen flitser.** Flitslicht geeft schittering op glanzend papier en plastic pasjes.
- **Telefoon recht boven het papier**, niet schuin. Dan blijven regels recht.
- **Donkere, egale ondergrond** onder licht papier: de randen vallen dan goed op.
- **Alleen het document in beeld**, geen tafel of toetsenbord eromheen.

Wil je een resultaat dat op een echte scan lijkt? Gebruik dan [Scan to PDF](/scan-to-pdf/): op je telefoon opent het de camera, je sleept de hoeken om de pagina bij te snijden en recht te zetten, kiest een scanfilter en exporteert een PDF met meerdere pagina's.

## Veelvoorkomende problemen

**De PDF is te groot om te uploaden.** Foto's van moderne telefoons zijn groot. Maak de PDF kleiner met de PDF Compressor (modus *Strong*, kwaliteit *Balanced*) en controleer daarna of kleine cijfers nog leesbaar zijn.

**De foto staat op zijn kant.** Draai de foto in je galerij, sla hem op en voeg hem opnieuw toe. Of draai de pagina achteraf met Rotate PDF.

**HEIC-foto's laden niet.** Werk je browser bij. Wil je de foto's zelf ook als JPG hebben, bijvoorbeeld voor een website die geen HEIC accepteert, zet ze dan om met [HEIC to JPG](/heic-to-jpg/).

**Ik wil per foto een aparte PDF.** Zet de foto's één voor één om. Elke conversie levert een PDF op met de naam van de foto.

## Privacy

De foto's die je naar PDF omzet zijn vaak de gevoeligste: ID-bewijs, loonstroken, medische papieren. Images to PDF maakt het bestand in je browser. Je foto's gaan niet naar de servers van DoraPDF en je hebt geen account nodig.

## Veelgestelde vragen

**Is JPG naar PDF omzetten gratis?**
Ja, zonder watermerk, zonder limiet en zonder registratie.

**Hoeveel foto's passen in één PDF?**
Er is geen vast aantal; dat hangt af van het geheugen van je apparaat. Werk op een oudere telefoon met kleinere groepjes.

**Gaat de kwaliteit achteruit?**
Zeer grote foto's worden verkleind tot een nog steeds hoge resolutie, ruim genoeg om een document op A4 te lezen en af te drukken.

**Hoe heet het bestand?**
Met één foto krijgt de PDF de naam van de foto, met meerdere heet hij `images.pdf`. Geef hem een duidelijke naam voordat je hem verstuurt.
"""),
dict(slug='achtergrond-verwijderen-foto-gratis', lang='nl', title='Achtergrond verwijderen uit een foto, gratis: transparant of wit met AI in je browser', date='2026-11-20',
 desc="Achtergrond verwijderen uit een foto, gratis en zonder upload: transparante PNG of witte achtergrond voor productfoto's, profielfoto's en logo's.",
 tools=['image-background-remover', 'image-resizer', 'image-compressor'], md="""
Je wilt je oude racefiets verkopen, maar op de foto staan ook de vuilnisbakken en de schuur. Je hebt een mooi portret voor je LinkedIn-profiel, alleen de achtergrond is een rommelige kantoortuin. Of je logo heeft een witte rand die lelijk afsteekt op een gekleurde slide. Allemaal momenten om de **achtergrond van een foto te verwijderen**.

Met de [Background Remover](/image-background-remover/) van DoraPDF haal je de achtergrond gratis weg met AI, zonder account. Het bijzondere: het AI-model draait **in je eigen browser**, dus je foto wordt nergens naartoe gestuurd. Het scherm is in het Engels; hieronder vind je alles in het Nederlands.

## Achtergrond weghalen: de stappen

1. Open de [Background Remover](/image-background-remover/).
2. Kies een foto: JPG, PNG, WebP of HEIC van je iPhone.
3. Kies bij **Mode** voor *Quick* of *HD*.
4. Kies bij **Background** wat er in plaats van de oude achtergrond moet komen.
5. Klik op **Remove background**.
6. Sleep de schuifregelaar om voor en na te vergelijken en download de PNG. Die heet `fotonaam-no-bg.png`.

De eerste keer downloadt je browser het AI-model, dus dan duurt het wat langer. Daarna gaat het een stuk sneller.

## Quick of HD?

**⚡ Quick, voor mensen en portretten.** Een licht model van ongeveer 13 MB dat één keer wordt gedownload. Snel en geschikt voor bijna elk apparaat, ook je telefoon. Prima voor profielfoto's en selfies.

**✨ HD, voor elk object.** Een veel groter model van ongeveer 115 MB, ook maar één keer te downloaden. Herkent producten, dieren en ingewikkelde randen beter. Heeft een moderne browser met GPU-versnelling (WebGPU) nodig. Ondersteunt je browser dat niet, dan meldt de tool dat en schakelt hij automatisch over naar Quick.

**Vuistregel:** persoon → Quick. Fiets, tas, schoen, plant of hond → HD.

## Transparant, wit of een kleur?

- **Transparent:** een **PNG met transparante achtergrond**. Gebruik dit als je de afbeelding op iets anders wilt plaatsen: een presentatie, flyer, website of collage.
- **White:** een effen witte achtergrond. Netjes en rustig voor **productfoto's** in een webshop of op een tweedehandsplatform.
- **Black**, **Pink** en **Light grey:** kant-en-klare alternatieven voor social posts en ontwerpen.

Let op bij pasfoto's: voor een paspoort, ID-kaart of rijbewijs gelden strenge eisen voor achtergrond, belichting en houding. Een achtergrond die je achteraf op de computer verandert, voldoet daar meestal niet aan. Laat een officiële pasfoto maken volgens de regels van je gemeente.

## Drie voorbeelden uit de praktijk

**Tweedehands verkopen.** Fotografeer het product bij daglicht tegen een rustige muur, kies HD en een witte achtergrond. Alle foto's van je advertenties krijgen zo dezelfde, verzorgde uitstraling.

**Profielfoto.** Kies Quick en *Light grey* of wit. Een neutrale achtergrond leidt niet af van je gezicht. Wil je liever een eigen kleur of een kantoorsfeer, download dan de transparante versie en zet die in je ontwerpprogramma op de achtergrond van je keuze.

**Logo op een gekleurde slide.** Kies HD en *Transparent*. Controleer de randen ingezoomd: dunne letters en lijntjes zijn het lastigst.

## Tips voor strakke randen

- **Contrast helpt.** Een donkere jas voor een lichte muur gaat beter dan een witte jas voor een witte muur.
- **Scherp en goed belicht.** Bewogen of beschaduwde delen geven rafelige randen.
- **Alles in beeld.** Wat door de rand van de foto is afgesneden, blijft afgesneden.
- **Haar en vacht** zijn voor elke tool het moeilijkst. Een effen achtergrond achter het hoofd scheelt veel; probeer bij krullen ook HD.
- **Glas en spiegelende objecten** blijven lastig. Reken op kleine onvolkomenheden.

## Formaat en bestandsgrootte

Het resultaat is altijd een PNG, het formaat dat transparantie bewaart. Heel brede foto's worden teruggebracht tot 2000 pixels breed, genoeg voor webshops, websites en presentaties.

- Vraagt een platform om **exacte afmetingen**, bijvoorbeeld een vierkante afbeelding? Pas ze aan met de [Image Resizer](/image-resizer/), in pixels of procenten.
- Is het bestand **te zwaar** voor je website of mail? De [Image Compressor](/image-compressor/) slaat PNG's op als WebP: veel kleiner en nog steeds transparant. Controleer wel of de plek waar je hem uploadt WebP accepteert.

## Problemen oplossen

**"AI model could not load".** Het model kon niet worden gedownload, meestal door een haperende verbinding. Controleer je internet en probeer het opnieuw.

**Melding dat er geen GPU is.** Je browser ondersteunt geen WebGPU, dus de tool gebruikte Quick. Een recente versie van Chrome of Edge kan HD mogelijk maken.

**Een deel van het onderwerp is weggevallen.** Dat gebeurt als onderwerp en achtergrond bijna dezelfde kleur hebben. Probeer de andere modus of maak een nieuwe foto met meer contrast.

**Traag op mijn telefoon.** De berekening gebeurt op je apparaat. Quick is daar het meest geschikt voor.

## Privacy: je foto blijft bij jou

Bij veel online tools om de achtergrond te verwijderen wordt je foto naar een server gestuurd. Hier niet: het AI-model wordt in je browser geladen en de bewerking gebeurt op je eigen computer of telefoon. Je portret of de foto van een product dat nog niet gelanceerd is, gaat niet naar DoraPDF.

## Veelgestelde vragen

**Is HD ook gratis?**
Ja, beide modi zijn gratis, zonder watermerk en zonder registratie.

**Kan ik meerdere foto's tegelijk bewerken?**
De tool werkt met één foto per keer. Als het model eenmaal geladen is, duurt elke volgende foto maar een paar seconden.

**Zit er een watermerk op het resultaat?**
Nee, de gedownloade PNG is schoon.

**Werkt het offline?**
De eerste keer heb je internet nodig om het model te downloaden. De bewerking zelf gebeurt op je apparaat.
"""),
dict(slug='tekst-uit-afbeelding-halen-ocr', lang='nl', title='Tekst uit een afbeelding halen (OCR): tekst kopiëren uit een foto of screenshot', date='2026-11-20',
 desc="Tekst uit een afbeelding halen met gratis OCR in je browser: tekst kopiëren uit foto's en screenshots, tips voor Nederlandse tekst en minder fouten.",
 tools=['image-to-text', 'pdf-ocr', 'scan-to-pdf'], md="""
Een recept uit een kookboek dat je wilt bewaren. De tekst op een dia die de docent te snel wegklikte en die je hebt gefotografeerd. Een screenshot van een rooster, een oude brief van de gemeente die je alleen op papier hebt. De tekst staat er, maar je kunt hem niet selecteren. Overtypen kost tijd en levert typefouten op. Met OCR (optische tekenherkenning) kun je **tekst uit een afbeelding halen** en als gewone, bewerkbare tekst gebruiken.

[Image to Text](/image-to-text/) van DoraPDF doet precies dat, gratis en zonder account. De herkenning gebeurt in je browser: je afbeelding wordt niet geüpload. Het scherm is in het Engels, maar je hoeft maar twee dingen te kiezen.

## Tekst kopiëren uit een foto: zo werkt het

1. Open [Image to Text](/image-to-text/).
2. Voeg één of meer afbeeldingen toe: JPG, PNG, WebP, iPhone-foto's (HEIC) of screenshots.
3. Kies bij **Language** de taal van de tekst.
4. Klik op **Extract text**.
5. De tekst verschijnt in een tekstvak. Verbeter hem daar meteen, klik op **Copy text** of download hem als `.txt`-bestand.

De eerste keer dat je een taal gebruikt, downloadt je browser het herkenningsmodel voor die taal (ongeveer 2 tot 10 MB). Daarna start het sneller.

Meerdere afbeeldingen tegelijk? Dan krijg je één tekst, met boven elk deel een regel met de bestandsnaam. Zo weet je altijd uit welke foto een stuk komt.

## Welke taal kies je voor Nederlandse tekst?

Eerlijk is eerlijk: **Nederlands staat (nog) niet in de lijst.** De beschikbare talen zijn Engels, Duits, Frans, Spaans, Italiaans, Portugees, Turks, Russisch, Arabisch, Urdu, Hindi, Indonesisch en vereenvoudigd Chinees.

Voor Nederlandse tekst kies je het best **English**. Nederlands gebruikt grotendeels dezelfde letters als het Engels, dus gewone woorden komen meestal goed door. Let bij het nalezen vooral op:

- woorden met trema of accent: *ideeën*, *coëfficiënt*, *café*, *één*;
- de combinatie *ij*, die soms als *y* of *ii* wordt gelezen;
- lange samenstellingen die over twee regels zijn afgebroken met een koppelteken.

Is de tekst in het Duits, Frans of Turks? Kies dan die taal: de herkenning van speciale tekens als ß, é, ç of ğ wordt daar duidelijk beter van.

## Waar gebruik je het voor?

- **Studie:** citaten uit gefotografeerde boekpagina's, dia's omzetten in aantekeningen die je kunt doorzoeken.
- **Werk:** gegevens uit een geprinte offerte of brief overnemen zonder alles over te typen.
- **Thuis:** een recept, handleiding of garantiebewijs als tekst bewaren.
- **Toegankelijkheid:** tekst die je kunt vergroten, vertalen of laten voorlezen door een schermlezer.

## Betere resultaten in vier stappen

Hoe goed OCR werkt, hangt vooral af van de foto:

1. **Gelijkmatig licht.** Pas op voor de schaduw van je hand of telefoon op de pagina.
2. **Recht van voren.** Scheve of gebogen regels, zoals vlak bij de rug van een boek, zijn het moeilijkst.
3. **Dichtbij.** De tekst moet het grootste deel van de foto vullen. Twee scherpe foto's van een halve pagina werken beter dan één wazige van de hele pagina.
4. **Screenshot in plaats van foto van een scherm.** Staat de tekst op je monitor of telefoon, maak dan een schermafbeelding.

Voor documenten van meerdere pagina's kun je eerst [Scan to PDF](/scan-to-pdf/) gebruiken: dat snijdt pagina's bij, zet ze recht en verbetert het contrast.

## Wat OCR (nog) slecht leest

- **Handschrift.** De herkenning is gemaakt voor gedrukte tekst; met handgeschreven notities zijn de resultaten meestal matig.
- **Tabellen.** Tekst komt regel voor regel naar buiten. De cijfers zijn er, maar de kolommen moet je zelf in Excel rechtzetten.
- **Sierlijke lettertypes**, tekst op een drukke foto, heel kleine of vervaagde letters.
- **Meerdere kolommen** (krant, tijdschrift): kolommen kunnen door elkaar raken. Snijd de foto bij en doe één kolom per keer.

Lees getallen, data en namen altijd na. Een *1* die een *l* wordt of een *0* die een *O* wordt, zijn de klassiekers.

## Een gescande PDF in plaats van een foto?

Image to Text werkt met afbeeldingen. Voor een gescande PDF gebruik je [PDF OCR](/pdf-ocr/): dat verwerkt tot 60 pagina's en geeft een PDF die er hetzelfde uitziet, maar waarin je tekst kunt selecteren en doorzoeken, plus een los tekstbestand. Ook daar kies je voor Nederlandse tekst **English**.

## Privacy

Afbeeldingen waar je tekst uit haalt, zijn vaak persoonlijk: brieven, contracten, aantekeningen. Image to Text laadt het herkenningsmodel in je browser en verwerkt de foto op je eigen apparaat. De afbeelding en de herkende tekst gaan niet naar de servers van DoraPDF.

## Veelgestelde vragen

**Is tekst uit een afbeelding halen gratis?**
Ja, zonder limiet, zonder watermerk en zonder account.

**Werkt het op mijn telefoon?**
Ja, in elke moderne browser. Op een telefoon duurt het soms wat langer, omdat je toestel het rekenwerk doet.

**Blijft de opmaak behouden?**
Nee, je krijgt platte tekst. Plak hem in Word of Google Documenten en maak hem daar op.

**Herkent het Nederlandse woorden met een trema?**
Er is geen aparte Nederlandse taaloptie, dus woorden met ë, ï of é kunnen fout gaan. Kies English en controleer die woorden bij het nalezen.
"""),
dict(slug='convertire-pdf-in-word-gratis-mantenendo-layout', lang='it', title='Convertire PDF in Word gratis mantenendo il layout (e cosa fare se il PDF è scansionato)', date='2026-11-18',
 desc='Come convertire PDF in Word gratis senza perdere la formattazione: due modalità, consigli per modificare il file e la soluzione per i PDF scansionati.',
 tools=['pdf-to-word', 'pdf-ocr', 'word-to-pdf'], md="""
Ti hanno mandato un modulo, un contratto o una dispensa in PDF e devi cambiare qualche riga. Ricopiare tutto a mano non ha senso: la strada più rapida è **convertire il PDF in Word**, correggere e poi, se serve, salvare di nuovo in PDF. Con il convertitore [PDF to Word](/pdf-to-word/) di DoraPDF lo fai gratis, senza registrazione e senza caricare il documento su un server (la schermata dello strumento è in inglese, ma i passaggi sono pochi e li trovi qui sotto).

In questa guida vediamo come convertire un PDF in Word **senza perdere la formattazione**, quale delle due modalità scegliere e come comportarsi con i PDF scansionati, che sono la causa più comune dei "non funziona".

## Convertire PDF in Word online: i passaggi

1. Apri [PDF to Word](/pdf-to-word/) dal browser, su PC, Mac o telefono.
2. Trascina il PDF nell'area di caricamento oppure toccala per sceglierlo.
3. Nel menu **Layout** scegli la modalità (le spieghiamo nel prossimo paragrafo).
4. Premi il pulsante di conversione e attendi qualche secondo: i documenti lunghi richiedono un po' di più.
5. Scarica il file **.docx**, che avrà lo stesso nome del PDF originale.

Il file si apre in Microsoft Word, LibreOffice Writer, Google Documenti e Pages.

## Le due modalità: quale scegliere

### "Keep original layout" – per mantenere l'aspetto della pagina

È l'opzione consigliata e quella attiva di default. Ogni pagina del documento Word riproduce la pagina del PDF: lo sfondo, le immagini, le linee e i riquadri restano dove erano, mentre il testo viene ricostruito sopra come testo modificabile, con carattere, grassetto, corsivo, colore e dimensione il più possibile vicini all'originale.

È la scelta giusta quando ti serve che il documento **resti uguale**: un modulo da compilare, un volantino, una lettera intestata in cui cambiare una data o un indirizzo.

Una cosa da sapere: in questa modalità ogni riga di testo è posizionata nel punto esatto della pagina. È perfetto per piccole correzioni, meno comodo se devi riscrivere interi paragrafi, perché il testo non "scorre" da una riga all'altra come in un documento normale. Anche le scritte ruotate (per esempio un timbro in diagonale) restano parte dell'immagine di sfondo e non diventano modificabili.

### "Text only" – per riscrivere e riutilizzare il testo

Qui il convertitore estrae solo il testo e lo dispone in paragrafi che scorrono liberamente. Le righe più grandi del resto vengono trasformate in titoli in grassetto e ogni pagina del PDF inizia su una nuova pagina. Immagini e grafica non vengono riportate.

Usala quando ti interessa il **contenuto**: citare parti di un articolo nella tesina, rielaborare appunti, copiare il testo di un regolamento per adattarlo.

**In breve:** devi ritoccare il documento → *Keep original layout*. Devi lavorare sul testo → *Text only*.

## Se compare "No text found": il PDF è scansionato

Molti PDF non contengono testo vero, ma solo fotografie delle pagine: succede con i documenti passati allo scanner, con le foto trasformate in PDF dal telefono e con molti fax. In questi casi lo strumento si ferma con il messaggio *"No text found — this PDF looks scanned"*.

Come risolvere:

1. Apri [PDF OCR](/pdf-ocr/) e carica lo stesso file.
2. Nel menu della lingua scegli **Italian**: il riconoscimento delle lettere accentate (à, è, ì, ò, ù) migliora molto.
3. Avvia l'OCR. Lo strumento elabora fino a 60 pagine e restituisce un PDF in cui il testo è selezionabile, più un file di testo.
4. Converti il nuovo PDF con PDF to Word.

Un trucco per capire subito se un PDF è scansionato: aprilo e prova a selezionare una parola con il mouse. Se si evidenzia la pagina intera come un'immagine, serve l'OCR.

## Problemi frequenti e come risolverli

**Il carattere è diverso dall'originale.** Il PDF usava un font che sul tuo computer non c'è, quindi Word lo sostituisce con uno simile. Se l'aspetto è importante, seleziona tutto il testo e imposta un font comune come Arial o Times New Roman.

**Una frase corretta finisce sopra quella successiva.** Succede in modalità layout quando scrivi una riga più lunga dell'originale. Accorcia il testo, riduci di un punto la dimensione del carattere oppure, se le modifiche sono tante, rifai la conversione in modalità *Text only*.

**Le tabelle non si modificano come tabelle.** Nella modalità layout le celle sono testo posizionato sopra il disegno della tabella: puoi cambiare il contenuto, ma non aggiungere righe. Per tabelle da rielaborare conviene copiare i dati dalla versione *Text only*.

**Il telefono non apre il .docx.** Installa l'app gratuita di Word o apri il file con Google Documenti.

## Dopo le modifiche: di nuovo in PDF

Quando hai finito, per inviare o stampare il documento conviene tornare al PDF. Da Word usa *File → Salva con nome → PDF*; da Google Documenti *File → Scarica → Documento PDF*. Se non hai un programma a portata di mano puoi usare [Word to PDF](/word-to-pdf/), che converte un file .docx direttamente nel browser.

## Privacy: il file non lascia il tuo dispositivo

La conversione avviene interamente nel browser: il PDF viene letto ed elaborato sul tuo computer o telefono, non viene inviato ai nostri server e non serve creare un account. È un dettaglio che conta quando il documento contiene dati personali, buste paga, contratti o certificati medici.

## Domande frequenti

**Convertire PDF in Word con DoraPDF è davvero gratis?**
Sì. Nessun abbonamento, nessuna filigrana sul documento e nessuna registrazione.

**Posso convertire più PDF insieme?**
No, lo strumento converte un file alla volta. Se hai più PDF, convertili uno dopo l'altro: ogni conversione richiede pochi secondi.

**Funziona da iPhone o Android?**
Sì, basta il browser. Su telefoni meno recenti i documenti con molte pagine possono richiedere più tempo, perché tutto il lavoro viene fatto dal dispositivo.

**Perché nel Word vedo il testo, ma non riesco a spostare le immagini?**
In modalità layout grafica e immagini formano lo sfondo della pagina, così l'impaginazione resta identica. Il testo sopra è modificabile; lo sfondo no.

**Posso convertire un PDF protetto da password?**
Se il PDF chiede una password per essere aperto, il convertitore non riesce a leggerlo. Se il documento è tuo e conosci la password, aprilo nel tuo lettore PDF, salvane una copia senza protezione (per esempio con *Stampa → Salva come PDF*) e converti quella.
"""),
dict(slug='comprimere-pdf-email-pec-portali', lang='it', title='Comprimere un PDF per email, PEC e portali: come ridurre le dimensioni senza rovinarlo', date='2026-11-18',
 desc='Comprimere PDF gratis online per email, PEC o portali: quale modalità scegliere, come restare leggibili e cosa fare se il file resta pesante.',
 tools=['pdf-compressor', 'pdf-splitter', 'delete-pdf-pages'], md="""
"Il file supera la dimensione massima consentita." Lo vedi quando provi a caricare la domanda su un portale, a mandare la documentazione per PEC o ad allegare una scansione a un'email. Di solito il colpevole è un PDF creato dallo scanner o dal telefono, con pagine salvate come immagini ad alta risoluzione. La soluzione è **comprimere il PDF**, cioè ridurne il peso mantenendolo leggibile.

Con [PDF Compressor](/pdf-compressor/) di DoraPDF puoi ridurre le dimensioni di un PDF gratis, senza registrarti e senza che il file venga caricato online: tutto avviene nel browser (l'interfaccia dello strumento è in inglese).

## Prima di iniziare: quanto deve pesare il file?

Ogni destinazione ha il suo limite, e cambia da un servizio all'altro:

- **Email normale:** molti provider accettano allegati intorno ai 20–25 MB in totale, ma conviene restare ben sotto, perché il messaggio codificato pesa più degli allegati.
- **PEC:** il limite dipende dal gestore e dal tuo piano, e vale per l'intero messaggio, destinatario compreso. Controlla le condizioni del tuo gestore.
- **Portali di enti, università e concorsi:** spesso indicano un limite per singolo file, a volte di pochi MB. Lo trovi nel bando o nelle istruzioni del modulo.

Conoscere il numero esatto ti evita di comprimere troppo: inutile trasformare un contratto in un documento sgranato se il portale accettava già il file con una piccola riduzione.

## Come comprimere un PDF online, passo per passo

1. Apri [PDF Compressor](/pdf-compressor/).
2. Carica il PDF trascinandolo nell'area apposita o toccandola per sceglierlo.
3. Nel menu **Mode** scegli tra *Smart* e *Strong* (vedi sotto).
4. Se usi *Strong*, scegli anche la qualità delle immagini: *High quality*, *Balanced* (predefinita) o *Smallest*.
5. Premi **Compress** e scarica il file, che si chiamerà `nomefile-compressed.pdf`. Accanto al nome vedrai di quanto si è ridotto, in percentuale.

## Smart o Strong: la scelta che conta davvero

| | Smart | Strong |
|---|---|---|
| Cosa fa | Riorganizza la struttura interna del PDF | Trasforma ogni pagina in un'immagine compressa |
| Testo selezionabile e ricercabile | Sì | No |
| Riduzione | Moderata, a volte nulla | Di solito molto più forte |
| Ideale per | PDF creati da Word o da programmi | Scansioni, foto, PDF pieni di immagini |

**Smart** è la scelta prudente: il documento resta identico, il testo si può ancora copiare e cercare. Su un PDF già ottimizzato può darsi che non ci sia nulla da recuperare: in quel caso lo strumento lo indica con *"already optimised"*.

**Strong** è quella che fa la differenza con le scansioni. Ogni pagina viene ridisegnata e salvata come immagine JPG con la qualità che hai scelto. Il prezzo da pagare: il testo non è più selezionabile, i link non sono più cliccabili e gli eventuali campi compilabili diventano parte dell'immagine. Per un documento d'identità scansionato o una ricevuta va benissimo; per un modulo da compilare ancora, no.

## Il metodo che funziona quasi sempre

1. Prova prima con **Smart**. Se il file rientra nel limite, hai finito.
2. Se non basta, passa a **Strong** con qualità **Balanced**.
3. Apri il risultato e **ingrandisci i punti critici**: numeri piccoli, codice fiscale, IBAN, firme, timbri. Se si leggono bene, il file è pronto.
4. Solo se è ancora troppo pesante, prova con **Smallest** e ricontrolla la leggibilità.

Consiglio pratico: se *Smallest* rende illeggibili le cifre più piccole, torna a *Balanced* e riduci il numero di pagine con uno dei metodi del paragrafo successivo.

## Se il PDF resta troppo grande

- **Togli le pagine inutili.** Pagine bianche, retro vuoti di una scansione, informative che il destinatario ha già: eliminale con [Delete PDF Pages](/delete-pdf-pages/), poi comprimi.
- **Dividi il documento.** Molti portali accettano più allegati. Con [PDF Splitter](/pdf-splitter/) estrai gli intervalli di pagine che ti servono (per esempio 1-5 e 6-10) e carica due file più leggeri.
- **Riscansiona con impostazioni più leggere.** Se hai accesso allo scanner, per i documenti di testo bastano 200–300 dpi in scala di grigi; il colore ad alta risoluzione serve raramente.

## Errori da evitare

- **Comprimere due volte in modalità Strong.** Ogni passaggio ricomprime immagini già compresse e peggiora la qualità senza grandi vantaggi. Riparti sempre dal file originale.
- **Inviare senza controllare.** Un file illeggibile può farti perdere tempo con un'integrazione documentale o, peggio, una scadenza.
- **Sovrascrivere l'originale.** Il file compresso ha un nome diverso apposta: conserva la versione di partenza in caso ti serva di nuovo.

## Privacy: perché è meglio comprimere nel browser

I documenti che finiscono in una PEC o su un portale contengono spesso dati personali: documenti d'identità, buste paga, certificati, dichiarazioni dei redditi. Con PDF Compressor il file viene elaborato sul tuo dispositivo e non viene caricato sui nostri server. Non serve un account e non resta traccia del documento online.

## Domande frequenti

**Comprimere un PDF fa perdere qualità?**
In modalità Smart no: il contenuto resta identico. In modalità Strong le pagine diventano immagini compresse, quindi un po' di qualità si perde; con *High quality* o *Balanced* nella maggior parte dei documenti la differenza a schermo è minima.

**Funziona anche da telefono?**
Sì, da qualsiasi browser moderno su Android e iPhone. Con PDF molto lunghi la modalità Strong può richiedere più tempo, perché ogni pagina viene ridisegnata dal dispositivo.

**Perché il file compresso pesa quasi come prima?**
Probabilmente hai usato Smart su un PDF già ottimizzato, o su una scansione: in questo caso prova Strong.

**Posso comprimere più PDF insieme?**
Lo strumento lavora su un file alla volta. Se devi inviarne diversi, comprimili uno per uno; se servono in un unico allegato, uniscili prima e comprimi il risultato.
"""),
dict(slug='unire-pdf-in-un-unico-file', lang='it', title='Unire PDF in un unico file: guida gratuita, senza registrazione, anche da iPhone e Android', date='2026-11-18',
 desc='Come unire PDF in un unico file gratis e senza registrazione: ordine giusto delle pagine, uso da telefono, e cosa fare se il file finale è troppo pesante.',
 tools=['pdf-merger', 'pdf-compressor', 'rotate-pdf'], md="""
Una domanda di iscrizione, un fascicolo per il commercialista, la documentazione per un'agenzia immobiliare: quasi sempre ti chiedono **un solo PDF**, non sei allegati separati. Invece di stampare tutto e riscansionare, puoi **unire i PDF in un unico file** in meno di un minuto.

Lo strumento [PDF Merger](/pdf-merger/) di DoraPDF unisce PDF gratis, senza registrazione e senza inviarli a un server: i file vengono combinati direttamente nel browser, sia su computer sia su telefono. La schermata è in inglese, ma i passaggi sono tre.

## I casi in cui unire i PDF ti semplifica la vita

- **Pratiche e domande online** che accettano un solo allegato: documento d'identità, codice fiscale, ISEE, certificati.
- **Tesi e tesine**: frontespizio, testo e allegati prodotti con programmi diversi diventano un unico documento.
- **Contabilità**: fatture e ricevute del mese in un solo file per il commercialista.
- **Lavoro**: offerta, condizioni e listino in un PDF da allegare a una sola email.

## Come unire PDF online in un unico file

1. Apri [PDF Merger](/pdf-merger/).
2. Aggiungi i file trascinandoli nell'area di caricamento o toccandola per sceglierli. Servono **almeno due PDF**.
3. Controlla l'elenco: i file verranno uniti **nell'ordine in cui compaiono**, dall'alto verso il basso.
4. Hai aggiunto un file per errore? Toglilo con la ✕ accanto al nome.
5. Premi **Merge PDFs** e scarica il risultato, `merged.pdf`.

Tutte le pagine di ogni file vengono incluse così come sono: un documento A4 verticale e una tabella orizzontale possono convivere nello stesso PDF senza essere deformati.

## Come ottenere l'ordine giusto al primo colpo

L'elenco non si riordina trascinando i nomi: i file si mettono in fila nell'ordine in cui li aggiungi, e ogni nuovo caricamento finisce in fondo. Due modi semplici per non sbagliare:

**Aggiungi i file uno alla volta**, nell'ordine finale. Prima la domanda, poi il documento d'identità, poi gli allegati. È il metodo più sicuro quando i file sono pochi.

**Numera i file prima di caricarli.** Rinominali `01-domanda.pdf`, `02-documento.pdf`, `03-isee.pdf` e selezionali tutti insieme da una cartella ordinata per nome. Di solito arrivano nell'ordine giusto, ma dai sempre un'occhiata all'elenco prima di premere il pulsante.

Se ti accorgi di un errore dopo il download, nessun problema: elimina i file dall'elenco con la ✕ e ricaricali nell'ordine corretto.

## Unire PDF da iPhone e Android

Lo strumento funziona dal browser del telefono, senza installare app.

- **iPhone:** apri la pagina in Safari, tocca l'area di caricamento e scegli i PDF dall'app File (anche da iCloud Drive). Dopo il download, il file finisce nella cartella Download dell'app File.
- **Android:** apri la pagina in Chrome e seleziona i PDF dal gestore file o da Google Drive. Il risultato lo trovi nei Download.

Se i documenti li hai solo come foto, prima trasformali in PDF con [Images to PDF](/images-to-pdf/), poi uniscili.

## Dopo l'unione: tre ritocchi utili

**Pagine girate.** Una scansione fatta in orizzontale si ritrova di lato nel PDF finale. Raddrizzala con [Rotate PDF](/rotate-pdf/), che permette di ruotare tutte le pagine o solo alcune.

**File troppo pesante.** Unendo diverse scansioni si superano facilmente i limiti di email e portali. Passa il risultato in [PDF Compressor](/pdf-compressor/): la modalità *Smart* mantiene il testo selezionabile, la modalità *Strong* riduce molto di più le scansioni.

**Pagine di troppo.** Pagine bianche o retro vuoti si eliminano con Delete PDF Pages, indicando i numeri delle pagine da togliere.

**Nome del file.** Prima di inviarlo, rinomina `merged.pdf` con qualcosa di chiaro, per esempio `domanda-borsa-di-studio-rossi.pdf`. Chi lo riceve ti ringrazierà.

## Problemi comuni

**"Add at least 2 PDF files".** Hai caricato un solo file. Aggiungine almeno un altro.

**Un file non viene accettato.** Lo strumento accetta solo PDF. Un documento Word va prima convertito in PDF; un'immagine si trasforma con Images to PDF.

**Un PDF protetto dà problemi.** Se un file richiede una password per essere aperto, aprilo con il tuo lettore PDF e salvane una copia senza protezione prima di unirlo.

**Su un telefono vecchio l'operazione è lenta.** Il lavoro lo fa il dispositivo stesso: con molti file pesanti serve qualche secondo in più. Chiudi le altre schede del browser e riprova.

## I tuoi documenti restano sul tuo dispositivo

Per unire i PDF non serve caricarli da nessuna parte: PDF Merger legge i file e crea il documento finale all'interno del browser. Nessun account, nessuna copia sui nostri server. Per documenti con dati personali, come carte d'identità o certificati, è il modo più tranquillo di lavorare.

## Domande frequenti

**Quanti PDF posso unire?**
Non c'è un numero massimo fissato dallo strumento: il limite pratico dipende dalla memoria del dispositivo. Decine di documenti normali non sono un problema su un computer recente.

**Si perde qualità unendo i PDF?**
No. Le pagine vengono copiate così come sono, senza ricompressione: testo, immagini e link restano invariati.

**Posso unire solo alcune pagine di un PDF?**
Lo strumento unisce i file interi. Per prendere solo alcune pagine, estraile prima con PDF Splitter e poi unisci i file estratti.

**È davvero gratis?**
Sì, senza filigrana, senza limiti di utilizzo giornalieri e senza registrazione.
"""),
dict(slug='jpg-in-pdf-telefono-computer', lang='it', title='Da JPG a PDF su telefono e computer: trasformare foto in PDF gratis, anche più immagini insieme', date='2026-11-18',
 desc='Convertire JPG in PDF gratis da cellulare o PC: più foto in un unico PDF, formato A4 o adattato, margini, ordine e consigli per foto leggibili.',
 tools=['images-to-pdf', 'scan-to-pdf', 'pdf-compressor'], md="""
Hai fotografato il documento d'identità, la ricevuta di un bonifico o le pagine di un quaderno, e il modulo online accetta solo PDF. Succede di continuo. La buona notizia è che **convertire JPG in PDF** non richiede app né programmi: basta il browser, sia sul cellulare sia sul computer.

Con [Images to PDF](/images-to-pdf/) di DoraPDF puoi trasformare una o più foto in un unico PDF, gratis e senza registrazione. Le immagini vengono elaborate sul tuo dispositivo, non su un server. Lo strumento è in inglese, quindi qui sotto trovi ogni opzione spiegata in italiano.

## Quali immagini puoi usare

Oltre ai classici **JPG**, lo strumento accetta PNG, WebP e le foto **HEIC** scattate con l'iPhone, che vengono convertite automaticamente. Ogni immagine diventa una pagina del PDF.

## Dal telefono: trasformare foto in PDF in pochi tocchi

1. Apri [Images to PDF](/images-to-pdf/) nel browser del telefono (Chrome, Safari, Samsung Internet...).
2. Tocca l'area di caricamento e scegli le foto dalla galleria o dall'app File. Puoi selezionarne diverse in una volta.
3. Controlla l'elenco: le pagine seguiranno **quest'ordine**. Per eliminare una foto, tocca la ✕ accanto al nome.
4. Scegli **Page size** e **Margin** (spiegati più sotto).
5. Tocca **Create PDF** e scarica il file.

Su iPhone il PDF finisce nell'app File, nella cartella Download; su Android nella cartella Download del telefono. Da lì puoi allegarlo a un'email o caricarlo sul portale.

**Ordine delle foto:** l'elenco non si riordina trascinando. Se l'ordine è importante (le pagine di un contratto, per esempio), aggiungi le foto una alla volta nella sequenza giusta: ogni nuova immagine si mette in fondo.

## Dal computer: JPG in PDF con trascinamento

Su PC e Mac il procedimento è lo stesso, ma ancora più veloce: apri la cartella con le immagini, selezionale e trascinale tutte insieme nell'area di caricamento. Se hai rinominato i file con un numero davanti (`01.jpg`, `02.jpg`...), di solito arrivano già in ordine; controlla comunque l'elenco prima di creare il PDF.

## Le opzioni spiegate

### Page size: che formato dare alle pagine

- **Fit page to image** – ogni pagina ha esattamente le proporzioni della foto. Ideale per immagini da guardare a schermo, grafiche, screenshot.
- **A4 page** – le foto vengono centrate e ridimensionate su pagine A4. È la scelta giusta per **documenti da stampare o inviare a enti e uffici**, dove l'A4 è lo standard.
- **US Letter** – il formato americano; in Italia serve raramente.

L'orientamento si sceglie da solo: una foto orizzontale finisce su una pagina orizzontale, una verticale su una verticale.

### Margin: il bordo bianco

*No margin* (nessun bordo), *Small margin* (predefinito) o *Big margin*. Per una carta d'identità su A4 un margine piccolo va benissimo; per foto da sfogliare a schermo puoi toglierlo del tutto.

**Nota sulle immagini PNG trasparenti:** le parti trasparenti diventano bianche nel PDF.

## Come fotografare un documento perché sia leggibile

La qualità del PDF dipende quasi tutta dalla foto. Qualche accorgimento:

- **Luce naturale e niente flash**, che crea riflessi sulla carta lucida.
- **Telefono parallelo al foglio**, non inclinato: le righe resteranno dritte.
- **Sfondo scuro e uniforme** sotto un foglio chiaro, così i bordi si distinguono.
- **Inquadra solo il documento**, senza il tavolo intorno.
- **Fronte e retro** di un documento d'identità: due foto separate, nell'ordine fronte → retro.

Se invece vuoi un risultato da scanner vero, con bordi ritagliati e contrasto migliorato, usa [Scan to PDF](/scan-to-pdf/): fotografi il documento, trascini gli angoli per ritagliarlo e raddrizzarlo, scegli un filtro di scansione ed esporti un PDF di più pagine.

## Problemi frequenti

**Il PDF è troppo pesante per il portale.** Le foto dei telefoni moderni sono molto grandi. Comprimi il PDF con [PDF Compressor](/pdf-compressor/): la modalità *Strong* con qualità *Balanced* di solito riduce molto il peso delle pagine fotografate.

**La foto risulta storta nel PDF.** A volte il telefono salva la rotazione in modo strano. Ruota la foto nella galleria, salvala e ricaricala; oppure ruota la pagina nel PDF con Rotate PDF.

**Le foto HEIC non si caricano.** Aggiorna il browser: la conversione HEIC richiede un browser recente. In alternativa, su iPhone puoi impostare *Impostazioni → Fotocamera → Formati → Più compatibile* per scattare direttamente in JPG.

**Ho bisogno di un file per ogni foto.** Carica e converti una foto alla volta: ogni conversione produce un PDF separato con il nome dell'immagine.

## Privacy: le foto restano sul tuo dispositivo

Le immagini che si trasformano in PDF sono spesso le più delicate: documenti d'identità, tessera sanitaria, buste paga. Images to PDF crea il file nel browser: le foto non vengono caricate sui nostri server e non serve alcun account.

## Domande frequenti

**Quante foto posso mettere in un PDF?**
Non c'è un numero fisso: dipende dalla memoria del dispositivo. Decine di foto non sono un problema su un computer; su un telefono datato conviene procedere a gruppi.

**La qualità delle foto peggiora?**
Le immagini molto grandi vengono ridimensionate a una risoluzione comunque alta, più che sufficiente per leggere e stampare un documento in A4.

**Posso convertire JPG in PDF senza installare app?**
Sì, funziona tutto dal browser, sia su Android sia su iPhone, e anche su tablet.

**Come si chiama il file creato?**
Con una sola foto prende il nome dell'immagine; con più foto si chiama `images.pdf`. Rinominalo prima di inviarlo.
"""),
dict(slug='rimuovere-sfondo-foto-gratis', lang='it', title='Rimuovere lo sfondo da una foto gratis: PNG trasparente o sfondo bianco in pochi secondi', date='2026-11-18',
 desc='Rimuovere lo sfondo da una foto gratis: PNG trasparente o sfondo bianco, modalità Quick e HD, consigli per bordi puliti. L\'IA gira nel browser.',
 tools=['image-background-remover', 'image-compressor', 'image-resizer'], md="""
Una foto del prodotto da mettere in un annuncio, il tuo ritratto per il profilo professionale, un logo da appoggiare su una slide colorata: in tutti questi casi lo sfondo originale dà fastidio. **Rimuovere lo sfondo da una foto** un tempo voleva dire passare mezz'ora con lo strumento di selezione di un programma di grafica. Oggi lo fa un modello di intelligenza artificiale in pochi secondi.

Il [Background Remover](/image-background-remover/) di DoraPDF scontorna persone, oggetti e prodotti gratis e senza registrazione. La particolarità: l'IA gira **dentro il tuo browser**, quindi la foto non viene mai caricata su un server. (La schermata dello strumento è in inglese; qui trovi tutto spiegato.)

## Togliere lo sfondo da una foto: come si fa

1. Apri il [Background Remover](/image-background-remover/).
2. Carica una foto: JPG, PNG, WebP o HEIC dell'iPhone.
3. Scegli la **Mode** (Quick o HD, vedi sotto).
4. Scegli il **Background** che vuoi al posto di quello originale.
5. Premi **Remove background** e attendi.
6. Usa il cursore di confronto per vedere il prima e il dopo, poi scarica il PNG, che si chiamerà `nomefoto-no-bg.png`.

La prima volta il browser scarica il modello di IA, quindi serve qualche secondo in più. Le volte successive parte molto più in fretta.

## Quick o HD: quale modalità scegliere

**Quick – persone e ritratti.** Usa un modello leggero (circa 13 MB, scaricato una sola volta) pensato soprattutto per le persone. È veloce e funziona su quasi tutti i dispositivi, telefoni compresi. Ottima per foto profilo, mezzibusti, selfie.

**HD – qualsiasi oggetto.** Usa un modello molto più grande (circa 115 MB, anche questo scaricato una volta sola) che riconosce meglio oggetti, prodotti, animali e contorni complicati. Richiede un browser moderno con accelerazione grafica (WebGPU). Se il tuo browser non la supporta, lo strumento te lo segnala e passa automaticamente alla modalità Quick.

**Regola pratica:** per una persona inizia con Quick; per una scarpa, una borsa, un vaso o un animale usa HD.

## Che sfondo scegliere al posto di quello vecchio

- **Transparent** – il classico **PNG con sfondo trasparente**. È quello che serve per appoggiare l'immagine su una presentazione, un volantino, un sito o un fotomontaggio.
- **White** – sfondo bianco pieno. È lo standard per le **foto prodotto** di molti negozi online e piattaforme di annunci.
- **Black**, **Pink**, **Light grey** – alternative pronte per grafiche e post social.

Un appunto sulle foto per documenti: per passaporto, carta d'identità o permessi ci sono regole precise su sfondo, luce e dimensioni del viso. Uno sfondo bianco aggiunto al computer non sempre è accettato; verifica i requisiti dell'ufficio prima di usarla.

## Consigli per un contorno pulito

L'IA lavora meglio se la foto la aiuta:

- **Contrasto tra soggetto e sfondo.** Una maglia scura davanti a un muro chiaro si scontorna meglio di una maglia bianca davanti a un muro bianco.
- **Soggetto a fuoco e ben illuminato.** Le zone mosse o in ombra creano bordi incerti.
- **Soggetto intero nell'inquadratura.** Un braccio tagliato dal bordo della foto resta tagliato anche dopo.
- **Capelli e pelo.** Sono la parte più difficile per qualunque strumento. Uno sfondo semplice e uniforme dietro la testa migliora molto il risultato; per i ritratti con capelli mossi prova anche la modalità HD.
- **Oggetti trasparenti** (bicchieri, bottiglie) e riflettenti restano complicati: aspettati qualche imperfezione.

## Dopo lo scontorno: dimensioni e peso

Il risultato è sempre un PNG, il formato che conserva la trasparenza. Le immagini molto larghe vengono ridotte a 2000 pixel di larghezza, che bastano per annunci, siti e presentazioni.

- Se una piattaforma chiede **misure precise** (per esempio un'immagine quadrata), usa [Image Resizer](/image-resizer/) per impostare i pixel esatti.
- Se il file è **troppo pesante** per un sito o un'email, passalo in [Image Compressor](/image-compressor/): i PNG vengono salvati in formato WebP, molto più leggero e capace di conservare la trasparenza. Se la piattaforma accetta solo PNG o JPG, controlla prima che il WebP sia supportato.

## Problemi comuni

**"AI model could not load".** Il modello non è stato scaricato: di solito è un problema di connessione. Controlla la rete e riprova; una volta scaricato, il modello resta disponibile.

**Il messaggio dice che manca la GPU.** Il tuo browser non supporta WebGPU e lo strumento ha usato la modalità Quick. Aggiornare il browser o provare con un'altra versione recente di Chrome o Edge può abilitare la modalità HD.

**Parte del soggetto è stata cancellata.** Succede quando soggetto e sfondo hanno colori molto simili. Prova l'altra modalità, oppure scatta una nuova foto con uno sfondo più contrastato.

**Su telefono è lento.** Il calcolo avviene sul dispositivo. La modalità Quick è la più adatta ai telefoni.

## Privacy: la foto non lascia il tuo dispositivo

Molti servizi online per togliere lo sfondo caricano la foto sui propri server. Qui no: il modello di IA viene scaricato nel browser e l'elaborazione avviene sul tuo computer o telefono. Il tuo ritratto, o la foto di un prodotto non ancora presentato, non viene inviato a DoraPDF.

## Domande frequenti

**Rimuovere lo sfondo è gratis anche in HD?**
Sì, entrambe le modalità sono gratuite, senza filigrana e senza registrazione.

**Posso scontornare più foto insieme?**
Lo strumento lavora su una foto alla volta. Per una serie di prodotti, ripeti l'operazione: dopo il primo caricamento del modello ogni foto richiede pochi secondi.

**Il risultato ha la filigrana?**
No, il PNG scaricato è pulito.

**Funziona offline?**
Il modello va scaricato la prima volta, quindi serve la connessione. Dopo, l'elaborazione vera e propria avviene sul dispositivo.
"""),
dict(slug='estrarre-testo-da-immagine-ocr', lang='it', title='Estrarre testo da un\'immagine con l\'OCR: copiare il testo da foto e screenshot gratis', date='2026-11-18',
 desc='Estrarre testo da immagine gratis con l\'OCR: copia il testo da foto, screenshot e scansioni in italiano, con consigli per risultati precisi.',
 tools=['image-to-text', 'pdf-ocr', 'scan-to-pdf'], md="""
Una pagina di libro fotografata in biblioteca, lo screenshot di una slide, la foto di un avviso in bacheca, un vecchio documento stampato di cui non hai il file: il testo è lì, ma non puoi selezionarlo. Ricopiarlo a mano richiede tempo e porta errori. Per **estrarre il testo da un'immagine** si usa l'OCR (riconoscimento ottico dei caratteri), che "legge" le lettere nella foto e le trasforma in testo modificabile.

Lo strumento [Image to Text](/image-to-text/) di DoraPDF fa proprio questo, gratis e senza registrazione. Il riconoscimento avviene nel tuo browser: le foto non vengono caricate su un server. L'interfaccia è in inglese, ma la lingua del testo da riconoscere la scegli tu, italiano compreso.

## Copiare il testo da una foto: i passaggi

1. Apri [Image to Text](/image-to-text/).
2. Carica una o più immagini: JPG, PNG, WebP o foto HEIC dell'iPhone. Vanno bene anche gli screenshot.
3. Nel menu **Language** scegli la lingua del testo, per esempio **Italian**.
4. Premi **Extract text**.
5. Il testo compare in un riquadro: puoi correggerlo lì, copiarlo con **Copy text** oppure scaricarlo come file `.txt`.

La prima volta che usi una lingua, il browser scarica il relativo modello di riconoscimento (qualche MB). Dalla volta successiva il processo parte più rapidamente.

Se carichi più immagini, il testo di ognuna viene separato da una riga con il nome del file, così sai sempre da quale foto arriva ogni pezzo.

## Perché la lingua giusta fa la differenza

L'OCR non riconosce solo le forme delle lettere: usa anche la conoscenza della lingua per decidere tra possibilità simili. Con la lingua impostata su **Italian**, le lettere accentate come *à, è, é, ì, ò, ù* e gli apostrofi di *l'anno* o *un'idea* vengono riconosciuti molto meglio che con l'inglese.

Le lingue disponibili sono inglese, italiano, spagnolo, francese, tedesco, portoghese, turco, russo, arabo, urdu, hindi, indonesiano e cinese semplificato. Se un'immagine contiene due lingue, scegli quella prevalente e correggi a mano le parole dell'altra.

## A cosa serve, in pratica

- **Studio:** recuperare citazioni da pagine di libri fotografate, trasformare le slide proiettate in appunti modificabili.
- **Lavoro:** copiare dati da un documento stampato senza ridigitarli, estrarre il testo di un volantino o di un cartello.
- **Burocrazia:** riprendere il testo di una vecchia lettera per rispondere, copiare un indirizzo o un codice da una foto.
- **Accessibilità:** ottenere testo che può essere ingrandito, tradotto o letto ad alta voce da un lettore di schermo.

## Come ottenere un testo più preciso

La qualità dell'OCR dipende dalla qualità dell'immagine molto più che dallo strumento. Prima di scattare:

- **Luce uniforme.** Evita ombre della mano o del telefono sulla pagina.
- **Foto dritta e frontale.** Le righe inclinate o curve (tipiche delle pagine vicine alla rilegatura di un libro) sono le più difficili.
- **Avvicinati.** Il testo deve occupare la maggior parte della foto. Meglio due foto nitide di mezza pagina che una foto sfocata dell'intera pagina.
- **Niente zoom digitale**: avvicina il telefono, non ingrandire lo schermo.
- **Screenshot invece di foto dello schermo.** Se il testo è su un monitor, uno screenshot dà sempre un risultato migliore di una foto.

Per documenti di più pagine conviene passare prima da [Scan to PDF](/scan-to-pdf/), che ritaglia e raddrizza le pagine e ne migliora il contrasto.

## Cosa l'OCR fa fatica a leggere

Meglio saperlo prima, per non perdere tempo:

- **Scrittura a mano.** Il riconoscimento è pensato per il testo stampato: con la calligrafia i risultati sono di solito poco affidabili.
- **Tabelle.** Il testo viene estratto riga per riga: i numeri ci sono, ma le colonne vanno sistemate a mano in un foglio di calcolo.
- **Caratteri decorativi**, scritte su sfondi fotografici, testo molto piccolo o sbiadito.
- **Impaginazioni a più colonne** (giornali, riviste): a volte le colonne si mescolano. Ritaglia la foto per lavorare una colonna alla volta.

Rileggi sempre il risultato, soprattutto numeri, date e nomi propri: un *1* che diventa *l* o uno *0* che diventa *O* sono errori tipici.

## Hai un PDF scansionato invece di una foto?

Image to Text lavora con le immagini. Se il documento è un PDF scansionato, usa [PDF OCR](/pdf-ocr/): ottieni un PDF dall'aspetto identico in cui il testo diventa selezionabile e ricercabile, più un file di testo. Anche qui puoi scegliere la lingua italiana.

## Privacy: il testo resta tuo

Le immagini da cui si estrae il testo sono spesso documenti personali, appunti, contratti. Image to Text scarica nel browser il modello di riconoscimento ed elabora la foto sul tuo dispositivo: l'immagine e il testo riconosciuto non vengono inviati ai server di DoraPDF.

## Domande frequenti

**Estrarre testo da un'immagine è gratis?**
Sì, senza limiti di utilizzo, senza filigrane e senza account.

**Funziona dal telefono?**
Sì, da qualsiasi browser moderno. Su telefono il riconoscimento può richiedere qualche secondo in più, perché il calcolo avviene sul dispositivo.

**Posso estrarre il testo da più foto insieme?**
Sì: carica più immagini e otterrai un unico testo, diviso per file.

**Il testo estratto mantiene la formattazione?**
No, si ottiene testo semplice: grassetti, colori e impaginazione non vengono conservati. Puoi incollarlo in Word o Google Documenti e formattarlo lì.

**Riconosce l'italiano con gli accenti?**
Sì, a patto di selezionare **Italian** nel menu della lingua prima di avviare l'estrazione.
"""),
dict(slug='firmare-pdf-online-senza-stampare', lang='it', title='Firmare un PDF online senza stamparlo: disegna o scrivi la firma e inseriscila gratis', date='2026-11-18',
 desc='Firmare un PDF online gratis senza stampare né scansionare: firma disegnata o scritta, posizione, dimensione e differenza con la firma digitale.',
 tools=['sign-pdf', 'pdf-editor', 'pdf-merger'], md="""
Il copione è sempre lo stesso: ricevi un PDF da firmare, lo stampi, firmi con la penna, lo scansioni (storto) e lo rispedisci. Per molti documenti di tutti i giorni (un modulo di adesione, una delega, una liberatoria, l'accettazione di un preventivo) esiste un modo più rapido: **firmare il PDF online**, direttamente dal computer o dal telefono.

Con [Sign PDF](/sign-pdf/) di DoraPDF disegni la firma con il mouse o con il dito, oppure la scrivi con la tastiera, e la inserisci nel documento. È gratis, non serve registrarsi e il PDF non viene caricato su un server. La schermata dello strumento è in inglese; qui sotto trovi ogni passaggio in italiano.

## Firma elettronica semplice o firma digitale? Chiariamolo subito

Una firma disegnata e inserita in un PDF è una **firma elettronica semplice**: un'immagine della tua firma sul documento. Per moltissimi usi quotidiani è sufficiente e accettata.

Non è però una **firma digitale**, cioè la firma con certificato qualificato rilasciata da un ente certificatore (tramite smart card, token o firma remota), che alcuni atti richiedono espressamente: contratti con la pubblica amministrazione, determinate pratiche professionali, atti con valore legale particolare. Se il destinatario chiede un file firmato digitalmente (spesso con estensione `.p7m`), una firma disegnata non basta.

**In pratica:** se nel modulo leggi "firma" e il destinatario accetta un PDF via email, la firma disegnata va bene. Se leggi "firma digitale" o "firmato digitalmente", serve il kit di firma. Nel dubbio, chiedi a chi deve ricevere il documento.

## Come firmare un PDF online, passo per passo

**1. Crea la firma.** Nel riquadro bianco in alto, disegna la tua firma con il mouse, il touchpad o il dito sullo schermo del telefono. Non ti piace? Premi **Clear** e riprova. In alternativa, scrivi il tuo nome nel campo **Or type it**: verrà mostrato in uno stile corsivo.

**2. Carica il PDF.** Trascinalo nell'area di caricamento o toccala per sceglierlo.

**3. Scegli dove metterla:**

- **Page** – la pagina da firmare. Il valore predefinito è `last`, cioè l'ultima pagina, dove di solito si trova lo spazio per la firma. Per un'altra pagina scrivi il numero, per esempio `2`.
- **Position** – in basso a destra (*Bottom right*), in basso a sinistra (*Bottom left*) o in basso al centro (*Bottom center*).
- **Size** – un cursore per regolare la larghezza della firma rispetto alla pagina.

**4. Firma e scarica.** Premi **Sign PDF** e scarica il file, che si chiamerà `nomefile-signed.pdf`.

## Consigli per una firma credibile

- **Disegna in grande.** Usa tutta la larghezza del riquadro: la firma verrà poi rimpicciolita e risulterà più pulita.
- **Dal telefono viene meglio.** Firmare con il dito sullo schermo è più naturale che con il mouse. Puoi anche usare un pennino su tablet.
- **Regola la dimensione.** Una firma enorme sembra finta, una minuscola non si legge. Per un documento A4 un valore intorno a quello predefinito è di solito equilibrato.
- **Controlla il risultato.** Apri il PDF firmato e verifica che la firma non copra testo o timbri. Se è nel posto sbagliato, riparti dal file originale cambiando posizione o dimensione.

La firma viene inserita nella parte bassa della pagina, a un margine fisso dal bordo. Funziona bene con i documenti che hanno lo spazio firma in fondo; se il riquadro della firma è a metà pagina, valuta se il destinatario accetta la firma in basso.

## "Luogo e data", più pagine e altri casi

**Compilare luogo, data e nome.** Molti moduli chiedono anche *Luogo e data* accanto alla firma. Puoi aggiungerli con [PDF Editor](/pdf-editor/): clicchi nel punto della pagina in cui vuoi scrivere, inserisci il testo e salvi. Conviene farlo prima di firmare.

**Firmare più pagine.** Sign PDF aggiunge una firma per volta. Per siglare anche altre pagine, carica di nuovo il file già firmato e ripeti l'operazione cambiando il numero di pagina.

**Rimandare il documento con gli allegati.** Se insieme al modulo firmato devi inviare un documento d'identità, uniscili in un solo file con [PDF Merger](/pdf-merger/).

## Problemi comuni

**La firma risulta spezzata o tremolante.** Con il mouse capita. Prova con il touchpad, con il dito su un telefono o scrivi il nome con la tastiera.

**Ho scritto un numero di pagina che non esiste.** Lo strumento usa la pagina più vicina valida (per esempio l'ultima). Controlla il file prima di inviarlo.

**Il PDF non si apre nello strumento.** Se è protetto da password per l'apertura, aprilo con il tuo lettore PDF e salvane una copia senza protezione.

## Privacy: la tua firma non viene inviata a nessuno

La firma è un dato personale delicato. Con Sign PDF sia l'immagine della firma sia il documento restano nel browser: l'unione avviene sul tuo dispositivo e niente viene caricato sui server di DoraPDF. Non viene creato un archivio delle firme e non serve un account.

## Domande frequenti

**Firmare un PDF online è gratis?**
Sì, senza registrazione, senza filigrane e senza limiti di documenti.

**Posso firmare un PDF dal telefono?**
Sì, anzi è il modo più comodo: disegni la firma con il dito direttamente nel browser, su Android o iPhone.

**La firma disegnata ha valore legale?**
È una firma elettronica semplice: è accettata in molti contesti quotidiani, ma non sostituisce la firma digitale quando questa è richiesta. Per documenti importanti verifica cosa chiede il destinatario.

**Posso salvare la firma per la prossima volta?**
No, lo strumento non conserva la firma: la disegni o la scrivi ogni volta. È anche una garanzia di privacy.
"""),
dict(slug='convertire-word-in-pdf-gratis', lang='it', title='Convertire Word in PDF gratis: da PC, da cellulare o online, e come scegliere il metodo giusto', date='2026-11-18',
 desc='Convertire Word in PDF gratis da PC, Mac o cellulare: salvare in PDF da Word e Google Documenti, convertitore online nel browser e controlli prima di inviare.',
 tools=['word-to-pdf', 'pdf-merger', 'pdf-compressor'], md="""
Il CV da allegare a una candidatura, la tesina da caricare sulla piattaforma dell'università, una lettera formale da mandare via PEC: quasi sempre ti chiederanno un PDF, non un file Word. Il motivo è semplice: un .docx può cambiare aspetto a seconda del programma e dei caratteri installati, mentre un PDF appare uguale su ogni schermo.

**Convertire Word in PDF** è facile, ma non tutti i metodi danno lo stesso risultato. In questa guida trovi le strade gratuite più comuni, da PC e da cellulare, e quando conviene usare il convertitore online [Word to PDF](/word-to-pdf/) di DoraPDF (la schermata dello strumento è in inglese).

## La risposta veloce

- Hai **Word o LibreOffice** sul computer? Salva direttamente in PDF dal programma: è il metodo più fedele.
- Scrivi su **Google Documenti**? Scarica il documento come PDF.
- Sei su un **computer non tuo**, sul telefono o senza programmi installati? Usa un convertitore nel browser.

Vediamoli uno per uno.

## Da Word e LibreOffice: il metodo più fedele

**Microsoft Word (Windows):** *File → Salva con nome* e, nel menu del tipo di file, scegli **PDF**. In alternativa *File → Esporta → Crea documento PDF/XPS*.

**Word per Mac:** *File → Salva con nome → Formato file: PDF*, oppure *File → Esporta*.

**LibreOffice Writer:** *File → Esporta come → Esporta direttamente come PDF*.

Con questi metodi il PDF conserva tutto: caratteri, intestazioni e piè di pagina, numeri di pagina, margini, colonne, sommario con link. Il testo resta selezionabile e ricercabile. Per il CV, la tesi o qualsiasi documento importante, è la scelta da preferire.

## Da Google Documenti

*File → Scarica → Documento PDF (.pdf)*. Se hai ricevuto un file Word, caricalo su Google Drive, aprilo con Google Documenti e scaricalo in PDF. Anche questo metodo mantiene l'impaginazione e il testo selezionabile.

## Dal cellulare

Sul telefono hai due possibilità:

- **App di Word o Google Documenti:** apri il file e usa la funzione di esportazione o condivisione in PDF.
- **Dal browser, senza app:** apri [Word to PDF](/word-to-pdf/), carica il file e scarica il PDF. Comodo quando il documento ti arriva come allegato e non vuoi installare nulla.

## Convertire Word in PDF online con DoraPDF

1. Apri [Word to PDF](/word-to-pdf/).
2. Carica un file **.docx**. Il vecchio formato .doc non è supportato: aprilo e salvalo come .docx prima di convertirlo.
3. Premi il pulsante di conversione.
4. Scarica il PDF, che avrà lo stesso nome del documento.

### Cosa viene conservato e cosa cambia

Il convertitore legge il contenuto del documento e lo impagina in un PDF in formato **A4**. Vengono riportati:

- testo, titoli, grassetto e corsivo;
- elenchi puntati e numerati;
- tabelle (con bordi semplici);
- immagini inserite nel documento.

Ci sono però dei limiti da conoscere:

- il testo usa un **carattere standard** e non i font originali;
- **intestazioni, piè di pagina e numeri di pagina** non vengono riportati, e nemmeno colonne e margini personalizzati;
- le **interruzioni di pagina** non seguono quelle di Word: il contenuto scorre da una pagina all'altra;
- le pagine del PDF vengono create come immagini, quindi **il testo non è selezionabile** né ricercabile.

Per questo il convertitore online è ideale per documenti semplici da leggere o stampare: una lettera, un elenco, una relazione senza impaginazione complessa. Quando l'aspetto deve essere identico all'originale, o il PDF passerà per un sistema automatico che legge il testo (come quelli di selezione del personale), usa uno dei metodi precedenti.

## Controlla prima di inviare

Un minuto di verifica evita brutte figure:

- **Apri il PDF** e scorri tutte le pagine: niente righe tagliate, tabelle fuori posto o immagini mancanti.
- **Nome del file:** `cv-mario-rossi.pdf` è meglio di `Documento1.pdf`.
- **Peso:** se il PDF contiene molte foto e supera il limite del portale o della PEC, riducilo con [PDF Compressor](/pdf-compressor/).
- **Un solo file:** se devi consegnare lettera, CV e allegati in un unico PDF, uniscili con [PDF Merger](/pdf-merger/).

## Problemi frequenti

**Il file non viene accettato.** Probabilmente è un .doc, un .odt o un .rtf. Lo strumento accetta solo .docx: salva il documento in quel formato e riprova.

**Le pagine sono diverse da quelle di Word.** È normale con la conversione online, perché intestazioni, interruzioni di pagina e font personalizzati non vengono riprodotti. Se ti serve l'impaginazione esatta, salva in PDF da Word, LibreOffice o Google Documenti.

**Mancano dei caratteri speciali o dei simboli.** Font particolari e simboli rari possono essere sostituiti. Controlla soprattutto formule e caratteri non latini.

## Privacy

La conversione online avviene nel browser: il file Word viene letto ed elaborato sul tuo dispositivo e non viene caricato sui server di DoraPDF. Non serve registrarsi. Per un CV con indirizzo e numero di telefono, o una lettera con dati personali, è un vantaggio non da poco.

## Domande frequenti

**Convertire Word in PDF online è gratis?**
Sì, senza registrazione, senza filigrana e senza limiti di documenti.

**Qual è il metodo migliore per una tesi o un CV?**
Salvare in PDF da Word, LibreOffice o Google Documenti: mantiene font, numeri di pagina e testo selezionabile.

**Posso convertire più file Word insieme?**
Lo strumento converte un documento alla volta. Se poi ti serve un unico PDF, unisci i file convertiti con PDF Merger.

**E se devo fare il contrario, da PDF a Word?**
Usa PDF to Word, che trasforma un PDF in un documento .docx modificabile.
"""),
dict(slug='converter-pdf-em-word-gratis-sem-perder-formatacao', lang='pt', title='Converter PDF em Word grátis sem perder a formatação: guia prático (com solução para PDF escaneado)', date='2026-11-18',
 desc='Como converter PDF em Word grátis e editável sem desconfigurar: qual modo escolher, como editar o arquivo, PDF escaneado e privacidade no navegador.',
 tools=['pdf-to-word', 'pdf-ocr', 'pdf-editor'], md="""
Você precisa corrigir uma cláusula de um contrato, atualizar um currículo que só existe em PDF ou reaproveitar trechos de uma apostila. Digitar tudo de novo não faz sentido. O caminho mais curto é **converter o PDF em Word**, editar e, se for preciso, salvar em PDF outra vez.

O conversor [PDF to Word](/pdf-to-word/) do DoraPDF transforma um PDF em um arquivo .docx editável, grátis, sem cadastro e sem enviar o documento para um servidor: tudo acontece no seu navegador. A tela da ferramenta está em inglês, mas o processo é simples e está explicado em português logo abaixo.

## O que significa "não perder a formatação"?

Quando alguém procura como converter PDF em Word sem desconfigurar, normalmente quer uma de duas coisas:

1. **Que o documento continue com a mesma cara**: logotipo no lugar, colunas, cores, tabelas desenhadas, só que com o texto editável.
2. **Que o texto venha limpo e organizado**, pronto para ser reescrito, sem caixas de texto espalhadas pela página.

São objetivos diferentes, e por isso a ferramenta tem dois modos. Escolher o certo resolve a maior parte das frustrações.

## Passo a passo para converter PDF em Word online

1. Abra o [PDF to Word](/pdf-to-word/) no navegador do computador ou do celular.
2. Arraste o PDF para a área de upload ou toque nela para escolher o arquivo.
3. No menu **Layout**, escolha o modo:
    - **Keep original layout (recommended)** – mantém a aparência da página;
    - **Text only (simple, flowing)** – só o texto, em parágrafos corridos.
4. Clique no botão de conversão e aguarde alguns segundos.
5. Baixe o arquivo **.docx**, que terá o mesmo nome do PDF.

O arquivo abre no Microsoft Word, no LibreOffice Writer, no Google Docs e no Pages.

## Modo layout: a página continua igual

Neste modo, cada página do Word reproduz a página do PDF. Imagens, linhas, fundos coloridos e molduras ficam como fundo da página, e o texto é recriado por cima, editável, com fonte, negrito, itálico, cor e tamanho o mais próximos possível do original.

**Use para:** formulários, currículos com design, cartas com papel timbrado, folhetos — qualquer documento em que você vai trocar uma data, um nome ou um valor e quer que o resto continue intacto.

**Saiba que:** cada linha de texto fica posicionada exatamente no seu lugar na página. Isso é ótimo para pequenas correções, mas pouco prático para reescrever parágrafos inteiros, porque o texto não "corre" de uma linha para a outra. Textos inclinados (como um carimbo na diagonal) continuam fazendo parte da imagem de fundo.

## Modo só texto: para reescrever e reaproveitar

Aqui a ferramenta extrai apenas o texto e monta parágrafos normais. Linhas maiores que o restante viram títulos em negrito, e cada página do PDF começa em uma nova página do Word. Imagens e elementos gráficos ficam de fora.

**Use para:** reaproveitar trechos de um artigo no seu TCC (sempre com a devida citação), adaptar um modelo de contrato, transformar uma apostila em resumo, revisar um texto longo.

## Deu erro "No text found"? O PDF é escaneado

Se o PDF nasceu de um scanner, de uma foto ou de um aplicativo de digitalização do celular, ele não tem texto de verdade, só imagens das páginas. Nesse caso a ferramenta avisa: *"No text found — this PDF looks scanned"*.

Para resolver, faça o OCR primeiro:

1. Abra o [PDF OCR](/pdf-ocr/) e envie o mesmo arquivo.
2. No menu de idioma, selecione **Portuguese** — os acentos e o "ç" são reconhecidos muito melhor.
3. Rode o OCR (a ferramenta processa até 60 páginas). Você recebe um PDF com texto selecionável e um arquivo de texto.
4. Converta esse novo PDF com o PDF to Word.

Dica para saber se um PDF é escaneado: tente selecionar uma palavra com o mouse. Se nada é selecionado, ou a página inteira fica marcada como uma imagem, ele precisa de OCR.

## Problemas comuns ao editar o Word convertido

**A fonte ficou diferente.** O PDF usava uma fonte que não está instalada no seu computador, e o Word colocou uma parecida. Se a aparência importa, selecione o texto e aplique uma fonte comum, como Arial ou Calibri.

**O texto que eu digitei invadiu a linha de baixo.** Acontece no modo layout quando a frase nova é maior que a original. Encurte o texto, reduza um ponto da fonte ou, se as mudanças forem grandes, converta de novo no modo *Text only*.

**Não consigo acrescentar linhas na tabela.** No modo layout, a tabela é o desenho do fundo e o conteúdo das células é texto posicionado por cima. Dá para trocar valores, mas não mudar a estrutura. Para trabalhar com os dados, use o modo só texto.

**Só preciso mudar uma palavrinha.** Às vezes nem é preciso converter: com o [PDF Editor](/pdf-editor/) você clica em qualquer ponto da página e acrescenta texto direto no PDF, por exemplo para preencher um campo em branco.

## Seus documentos ficam no seu aparelho

Contratos, holerites, documentos pessoais: muita coisa que vira Word começa como um PDF sensível. O PDF to Word lê e converte o arquivo dentro do navegador. Nada é enviado para os servidores do DoraPDF, e você não precisa criar conta.

## Perguntas frequentes

**Converter PDF em Word no DoraPDF é grátis mesmo?**
Sim. Sem assinatura, sem marca d'água e sem cadastro.

**Funciona no celular?**
Sim, em qualquer navegador moderno, no Android ou no iPhone. Em aparelhos mais antigos, PDFs com muitas páginas podem levar um pouco mais, porque o processamento é feito no próprio celular.

**Dá para converter vários PDFs de uma vez?**
Não, a conversão é de um arquivo por vez. Cada um leva poucos segundos.

**Depois de editar, como volto para PDF?**
No Word, use *Arquivo → Salvar como → PDF*. No Google Docs, *Arquivo → Fazer download → Documento PDF*.

**E se o PDF tiver senha?**
Se ele pede senha para abrir, a ferramenta não consegue lê-lo. Se o arquivo é seu e você sabe a senha, abra no seu leitor de PDF, salve uma cópia sem proteção (por exemplo com *Imprimir → Salvar como PDF*) e converta essa cópia.
"""),
dict(slug='comprimir-pdf-enviar-email', lang='pt', title='Como comprimir PDF para enviar por e-mail (e diminuir o tamanho sem deixar ilegível)', date='2026-11-18',
 desc='Comprimir PDF grátis para enviar por e-mail ou anexar em sites: modo Smart ou Strong, como manter a leitura e o que fazer se o arquivo continuar grande.',
 tools=['pdf-compressor', 'pdf-splitter', 'pdf-merger'], md="""
Você anexa o PDF, clica em enviar e o e-mail volta: arquivo grande demais. Ou o site de inscrição recusa o documento porque passou do limite. O motivo quase sempre é o mesmo: páginas escaneadas ou fotografadas com o celular, salvas como imagens enormes. A saída é **comprimir o PDF**, diminuindo o tamanho do arquivo sem estragar a leitura.

Com o [PDF Compressor](/pdf-compressor/) do DoraPDF você reduz o tamanho de um PDF grátis, sem cadastro e sem fazer upload: a compressão acontece no seu navegador (a ferramenta está em inglês, mas cada opção está explicada aqui).

## Qual é o tamanho máximo para enviar por e-mail?

Depende do serviço. O Gmail, por exemplo, aceita anexos de até 25 MB por mensagem; acima disso oferece enviar um link do Google Drive. Outros provedores têm limites parecidos ou menores, e o servidor de quem recebe também pode ter o seu. Sites de inscrição, concursos e órgãos públicos costumam indicar o limite por arquivo no edital ou no próprio formulário.

Uma regra útil: mire **bem abaixo do limite**. Um anexo de 24 MB num limite de 25 MB pode falhar, porque o e-mail codifica os anexos e eles ficam maiores no envio.

## Comprimir PDF em 5 passos

1. Abra o [PDF Compressor](/pdf-compressor/).
2. Arraste o PDF para a área de upload ou toque para escolher.
3. Em **Mode**, escolha *Smart* ou *Strong*.
4. Se escolher *Strong*, defina a qualidade das imagens: *High quality*, *Balanced* (padrão) ou *Smallest*.
5. Clique em **Compress** e baixe o arquivo `nome-compressed.pdf`. Ao lado do nome aparece quanto ele ficou menor, em porcentagem.

## Smart x Strong: entenda a diferença

**Smart — mantém o texto selecionável.** Reorganiza a estrutura interna do PDF sem mexer no conteúdo. Texto, links e qualidade ficam idênticos. A redução costuma ser modesta e, se o PDF já estiver otimizado, pode não haver ganho — nesse caso a ferramenta mostra *"already optimised"*. É a melhor opção para PDFs gerados pelo Word ou por outros programas.

**Strong — compressão máxima.** Cada página é redesenhada e salva como imagem JPG na qualidade escolhida. Em documentos escaneados, a diferença de tamanho costuma ser grande. Em troca, o texto deixa de ser selecionável e pesquisável, os links param de funcionar e campos de formulário viram parte da imagem.

Resumo prático:

- **PDF criado no computador** (relatório, contrato digitado, apresentação exportada): comece pelo **Smart**.
- **Documento escaneado ou fotografado** (RG, comprovante de residência, nota fiscal impressa): vá direto ao **Strong**.

## Como não deixar o documento ilegível

O erro mais comum é escolher a compressão máxima e enviar sem conferir. Faça assim:

1. Comece com **Strong + Balanced**.
2. Abra o arquivo comprimido e **dê zoom nas partes críticas**: números pequenos, CPF, código de barras, assinaturas, carimbos.
3. Se tudo estiver nítido e o tamanho couber no limite, pronto.
4. Se ainda estiver grande, tente **Smallest** e confira de novo.
5. Se o *Smallest* borrar os números, volte para *Balanced* e reduza o número de páginas (veja abaixo).

E sempre comprima a partir do **arquivo original**: comprimir duas vezes no modo Strong recomprime imagens já comprimidas e piora a qualidade.

## O PDF continua grande demais? Três saídas

**Divida o arquivo.** Muitos formulários aceitam mais de um anexo, e você pode mandar dois e-mails. Com o [PDF Splitter](/pdf-splitter/) você extrai intervalos de páginas (por exemplo 1-10 e 11-20) ou separa cada página em um PDF próprio.

**Tire páginas desnecessárias.** Versos em branco de uma digitalização, páginas repetidas, termos que o destinatário já tem. Remova antes de comprimir, com o Delete PDF Pages.

**Junte só o que importa.** Se você precisa enviar vários documentos, comprima cada um e depois una em um único arquivo com o [PDF Merger](/pdf-merger/). Assim você controla a qualidade de cada parte.

## Dicas para escanear já pensando no tamanho

- Para documentos de texto, **200 a 300 dpi** costumam ser suficientes.
- Use **tons de cinza** em vez de colorido quando a cor não importa.
- No celular, enquadre só o documento, sem a mesa em volta: menos área inútil, arquivo menor.

## Privacidade: o arquivo não sai do seu aparelho

Documentos que vão por e-mail muitas vezes trazem dados pessoais: RG, CPF, comprovantes, holerites, declarações. O PDF Compressor processa o arquivo no seu navegador. Nada é enviado aos servidores do DoraPDF e não é preciso criar conta.

## Perguntas frequentes

**Comprimir PDF diminui a qualidade?**
No modo Smart, não: o conteúdo fica idêntico. No modo Strong, as páginas viram imagens comprimidas; com *High quality* ou *Balanced* a diferença na tela costuma ser pequena.

**Posso comprimir PDF pelo celular?**
Sim, no navegador do Android ou do iPhone, sem instalar aplicativo. PDFs longos no modo Strong podem demorar um pouco mais, porque cada página é processada no aparelho.

**Por que meu PDF quase não diminuiu?**
Provavelmente você usou o modo Smart num arquivo escaneado ou já otimizado. Teste o modo Strong.

**Dá para comprimir vários PDFs de uma vez?**
A ferramenta trabalha com um arquivo por vez. Comprima um por um ou, se eles vão juntos, una primeiro e comprima o resultado.
"""),
dict(slug='fusionner-pdf-gratuit-en-ligne', lang='fr', title='Fusionner des PDF en un seul fichier : gratuit, sans inscription et sans envoi sur un serveur', date='2026-11-17',
 desc='Fusionner des PDF gratuitement, sans inscription : réunissez plusieurs fichiers en un seul PDF dans le bon ordre, sur PC, Mac ou téléphone.',
 tools=['pdf-merger', 'pdf-compressor', 'delete-pdf-pages'], md="""
Une attestation employeur, trois bulletins de salaire, un avis d'imposition, une pièce d'identité : beaucoup de dossiers demandent **un seul PDF**, et non cinq pièces jointes séparées. Plutôt que d'imprimer puis de tout rescanner, il suffit de **fusionner les PDF**. Avec l'outil [Fusionner des PDF](/pdf-merger/) de DoraPDF (l'interface de l'outil est en anglais), c'est gratuit, sans inscription, et les fichiers ne quittent pas votre appareil.

Ce guide montre comment combiner plusieurs PDF en un seul, comment obtenir le bon ordre du premier coup, et quoi faire quand le fichier final est trop lourd ou contient des pages en trop.

## Fusionner des PDF en ligne, étape par étape

1. Ouvrez [Fusionner des PDF](/pdf-merger/).
2. Glissez vos fichiers dans la zone de dépôt, ou cliquez dessus pour les choisir. Il en faut **au moins deux**.
3. Vérifiez la liste qui s'affiche : les fichiers seront assemblés **dans cet ordre**, de haut en bas.
4. Un fichier en trop ? Retirez-le avec la croix (✕) à droite de son nom.
5. Cliquez sur **Merge PDFs**.
6. Téléchargez le résultat, nommé `merged.pdf`. Pensez à le renommer avant de l'envoyer (par exemple `dossier-location-dupont.pdf`) : c'est plus clair pour la personne qui le reçoit.

Toutes les pages de chaque fichier sont reprises, dans leur format d'origine. Un document en A4 portrait et un autre en paysage peuvent cohabiter dans le même PDF.

## Obtenir le bon ordre sans s'énerver

L'outil assemble les fichiers dans l'ordre où vous les ajoutez. Il n'y a pas de glisser-déposer pour réorganiser la liste ensuite, alors quelques réflexes font gagner du temps :

- **Ajoutez les fichiers un par un**, dans l'ordre voulu : d'abord la lettre de motivation, puis le CV, puis les justificatifs. Chaque nouveau fichier s'ajoute à la fin de la liste.
- **Ou numérotez-les avant** : renommez-les `01-lettre.pdf`, `02-cv.pdf`, `03-diplome.pdf`. En les sélectionnant tous d'un coup dans l'explorateur de fichiers triés par nom, ils arrivent généralement dans cet ordre (vérifiez quand même la liste).
- **Erreur d'ordre ?** Retirez le fichier mal placé avec la croix, puis ajoutez-le de nouveau : il se placera en dernier.

Si le dossier que vous devez envoyer précise un ordre (c'est souvent le cas pour les dossiers de location, de bourse ou de candidature), respectez-le : la personne qui instruit le dossier le lira plus vite.

## Sur téléphone, Mac ou PC

L'outil fonctionne dans le navigateur, donc de la même façon partout :

- **Sur PC Windows ou Mac** : Chrome, Edge, Firefox ou Safari font l'affaire. Le fichier fusionné arrive dans votre dossier Téléchargements.
- **Sur iPhone** : ouvrez la page dans Safari, touchez la zone de dépôt et choisissez « Choisir des fichiers » pour aller chercher vos PDF dans l'app Fichiers ou iCloud Drive. Le résultat s'enregistre dans Fichiers.
- **Sur Android** : depuis Chrome, la zone de dépôt ouvre le sélecteur de fichiers ; le PDF fusionné apparaît dans Téléchargements.

Sur mobile, ajoutez les fichiers un par un pour maîtriser l'ordre : le sélecteur ne trie pas toujours comme on l'imagine.

## Vos documents sont des photos, pas des PDF ?

Si certaines pièces sont des photos (une carte d'identité prise au téléphone, un justificatif en JPG), transformez-les d'abord en PDF avec [Images en PDF](/images-to-pdf/) (interface en anglais), puis ajoutez ce PDF à la fusion. Pour des pages de papier photographiées, [Scanner en PDF](/scan-to-pdf/) permet de recadrer et redresser chaque page avant.

## Problèmes fréquents et solutions

**« Add at least 2 PDF files »**
Le message apparaît si vous n'avez déposé qu'un seul fichier. Ajoutez-en un deuxième avant de cliquer sur le bouton.

**Le fichier final est trop lourd pour l'e-mail ou le portail**
Fusionner additionne les poids : trois scans de 6 Mo donnent un PDF d'environ 18 Mo. Passez le résultat dans le [compresseur de PDF](/pdf-compressor/) (interface en anglais). Pour des scans, le mode « Strong » réduit nettement la taille.

**Il y a des pages blanches ou inutiles**
Un recto-verso scanné laisse souvent des versos vides. Supprimez-les après la fusion avec [Supprimer des pages PDF](/delete-pdf-pages/) (interface en anglais).

**Une page est à l'envers**
Corrigez-la avec [Pivoter un PDF](/rotate-pdf/) avant ou après la fusion.

**Un fichier est protégé par mot de passe**
Les PDF chiffrés peuvent poser problème lors de l'assemblage. Si c'est votre document et que vous connaissez le mot de passe, retirez d'abord la protection avec [Déverrouiller un PDF](/unlock-pdf/), puis relancez la fusion.

**Le navigateur rame avec de très gros fichiers**
Tout se passe sur votre appareil, donc la mémoire de votre ordinateur ou téléphone compte. Avec des dizaines de fichiers très lourds, fusionnez par petits lots, puis fusionnez les lots entre eux.

## Pourquoi c'est plus sûr pour des documents sensibles

Les pièces d'un dossier administratif sont parmi les plus sensibles qui soient : revenus, adresse, numéro fiscal, copie de pièce d'identité. Avec DoraPDF, la fusion est réalisée **dans votre navigateur** : les fichiers ne sont pas envoyés sur nos serveurs et ne sont stockés nulle part. Une fois l'onglet fermé, il ne reste que le fichier téléchargé sur votre appareil.

Un conseil au passage : quand un organisme demande une copie de pièce d'identité, vous pouvez ajouter une mention du type « Copie pour dossier de location – novembre 2026 » avec le [filigrane texte](/pdf-text-watermark/). Cela limite la réutilisation du document à d'autres fins.

## Questions fréquentes

**Fusionner des PDF est-il vraiment gratuit ?**
Oui : pas de compte, pas d'abonnement, pas de filigrane ajouté au résultat.

**Combien de fichiers peut-on fusionner ?**
L'outil ne fixe pas de nombre maximum. La limite pratique dépend de la mémoire de votre appareil ; pour de très gros volumes, procédez par lots.

**La qualité des pages change-t-elle ?**
Non. Les pages sont copiées telles quelles : le texte reste sélectionnable et les images ne sont pas recompressées.

**Peut-on fusionner des PDF sur iPhone sans application ?**
Oui, depuis Safari. Vous choisissez les fichiers dans l'app Fichiers et le PDF fusionné y est enregistré.

**Et pour faire l'inverse, séparer un PDF ?**
Utilisez [Diviser un PDF](/pdf-splitter/) pour extraire une plage de pages ou découper le document page par page.
"""),
dict(slug='convertir-jpg-en-pdf-telephone-pc', lang='fr', title='Convertir JPG en PDF sur téléphone et PC : une ou plusieurs photos dans un seul fichier', date='2026-11-17',
 desc='Convertir JPG en PDF gratuitement sur iPhone, Android ou PC : regroupez vos photos en un PDF au format A4, avec ou sans marges, sans application.',
 tools=['images-to-pdf', 'heic-to-pdf', 'scan-to-pdf'], md="""
Le formulaire en ligne n'accepte que des PDF, et vous n'avez que des photos : un justificatif de domicile pris au téléphone, un relevé de notes, des captures d'écran. La solution la plus simple est de **convertir les JPG en PDF**, directement depuis le navigateur, sans installer d'application. Avec [Images en PDF](/images-to-pdf/) de DoraPDF (l'interface de l'outil est en anglais), vous pouvez transformer une photo en PDF ou en réunir plusieurs dans un seul fichier, sur téléphone comme sur ordinateur.

## Ce que fait l'outil

Chaque image devient **une page** du PDF, dans l'ordre où vous l'ajoutez. L'outil accepte les formats courants (JPG, PNG, WebP) et aussi les photos **HEIC** de l'iPhone. Deux réglages suffisent :

- **Page size** (format de page) :
  - *Fit page to image* : la page prend exactement les proportions de la photo. Idéal pour un album ou des captures d'écran.
  - *A4 page* : chaque image est centrée sur une feuille A4, le format standard en France pour tout ce qui sera imprimé ou déposé sur un portail administratif.
  - *US Letter* : le format américain, à éviter sauf demande particulière.
- **Margin** (marge) : aucune, petite (par défaut) ou grande.

L'orientation (portrait ou paysage) est choisie automatiquement pour chaque image : une photo prise à l'horizontale donne une page en paysage.

## Convertir JPG en PDF sur iPhone ou Android

1. Ouvrez [Images en PDF](/images-to-pdf/) dans Safari ou Chrome.
2. Touchez la zone de dépôt. Sur iPhone, choisissez « Photothèque » pour prendre vos photos directement dans l'app Photos, ou « Choisir des fichiers ». Sur Android, le sélecteur propose la galerie et les fichiers.
3. Sélectionnez vos images. Pour garder un ordre précis, ajoutez-les une par une : chaque nouvel ajout se place à la fin de la liste.
4. Choisissez **A4 page** si le document doit être imprimé ou déposé en ligne.
5. Touchez **Create PDF**, puis **Download**.

Le fichier s'appelle `images.pdf` (ou porte le nom de la photo s'il n'y en a qu'une). Sur iPhone, il se range dans l'app Fichiers ; sur Android, dans Téléchargements.

## Convertir JPG en PDF sur PC ou Mac

Même principe, en plus confortable : glissez les images depuis l'explorateur de fichiers ou le Finder sur la zone de dépôt. Vous pouvez en déposer plusieurs à la fois, puis compléter la liste avec d'autres. Une image ajoutée par erreur se retire avec la croix (✕).

Astuce pour l'ordre : renommez les fichiers `1-recto.jpg`, `2-verso.jpg` avant de les déposer, puis vérifiez la liste affichée avant de lancer la conversion.

## Photos iPhone en HEIC

Les iPhone enregistrent souvent les photos au format HEIC. Pas besoin de les convertir en JPG d'abord : [Images en PDF](/images-to-pdf/) les accepte directement. Si vous n'avez que des HEIC, la page dédiée [HEIC en PDF](/heic-to-pdf/) (interface en anglais) fonctionne exactement de la même manière, avec un sélecteur limité à ce format.

## Photo de document ou vrai scan ?

Une photo de feuille prise à main levée a souvent des bords de table, une perspective penchée et une ombre. Pour un justificatif officiel, le résultat fait parfois négligé. Dans ce cas, utilisez plutôt [Scanner en PDF](/scan-to-pdf/) (interface en anglais) : vous déplacez les coins pour recadrer et redresser la page, vous choisissez un filtre de numérisation, puis vous exportez un PDF propre de plusieurs pages.

En résumé :

- **Images en PDF** pour des photos, captures d'écran, visuels déjà propres ;
- **Scanner en PDF** pour des feuilles de papier photographiées.

## Conseils pour un PDF net et léger

**Photographiez à la lumière du jour**, sans flash, la feuille bien à plat. Le flash crée un reflet blanc qui peut masquer une ligne entière.

**Préférez A4 avec petite marge pour l'administratif.** Le document s'imprime correctement sans être coupé, et il ressemble à un vrai document plutôt qu'à une photo collée.

**Un PDF trop lourd ?** Les photos de téléphone font souvent 3 à 5 Mo chacune. L'outil ramène déjà les très grandes images à 2 400 pixels sur le plus grand côté, ce qui reste net sur une page A4. Si le fichier dépasse encore la limite d'un portail, passez-le dans le [compresseur de PDF](/pdf-compressor/).

**Une seule photo par page.** L'outil place une image par page. Pour mettre le recto et le verso d'une carte sur la même page, assemblez d'abord les deux images en une seule avec une application de retouche, ou acceptez deux pages : la plupart des organismes l'acceptent sans souci.

## Problèmes fréquents

**Les pages ne sont pas dans le bon ordre.** Retirez l'image mal placée avec la croix et ajoutez-la de nouveau : elle passera en dernière position. Recommencez jusqu'à obtenir l'ordre voulu, puis relancez la conversion.

**Une photo apparaît couchée.** Certaines photos de téléphone sont enregistrées avec une information d'orientation que tous les logiciels ne lisent pas de la même façon. Ouvrez le PDF pour vérifier ; si une page est tournée, corrigez-la avec [Pivoter un PDF](/rotate-pdf/).

**Rien ne se passe sur un vieux téléphone.** La conversion utilise la mémoire de l'appareil. Avec beaucoup de photos lourdes, convertissez-les par petits groupes, puis réunissez les PDF obtenus avec [Fusionner des PDF](/pdf-merger/).

## Confidentialité

Les photos de documents contiennent souvent des informations personnelles : adresse, numéro de sécurité sociale, revenus. Avec DoraPDF, la conversion se fait **entièrement dans votre navigateur** : les images ne sont pas envoyées sur un serveur et rien n'est conservé après la fermeture de la page.

## Questions fréquentes

**Peut-on convertir JPG en PDF gratuitement et sans inscription ?**
Oui, sans compte, sans limite d'utilisation et sans filigrane.

**Combien de photos peut-on mettre dans un PDF ?**
Il n'y a pas de nombre fixe. Sur téléphone, au-delà d'une vingtaine de grosses photos, procédez par lots pour éviter de saturer la mémoire.

**Le PDF obtenu contient-il du texte sélectionnable ?**
Non, chaque page est une image. Pour rendre le texte copiable et recherchable, passez ensuite le PDF dans l'outil [PDF OCR](/pdf-ocr/).

**Quelle différence entre « Fit page to image » et « A4 » ?**
« Fit » garde la forme exacte de la photo, sans bandes blanches. « A4 » place chaque image sur une feuille standard, ce qui est préférable pour imprimer ou déposer un dossier.
"""),
dict(slug='supprimer-arriere-plan-image-gratuit', lang='fr', title="Supprimer l'arrière-plan d'une image gratuitement : fond transparent ou blanc, sans envoyer la photo", date='2026-11-17',
 desc="Supprimez l'arrière-plan d'une image gratuitement avec l'IA, dans votre navigateur : fond transparent PNG ou fond blanc pour vos photos produit et portraits.",
 tools=['image-background-remover', 'image-compressor', 'image-resizer'], md="""
Une photo de produit pour une annonce Vinted ou Leboncoin, un portrait pour un CV, un logo à poser sur une couleur de fond : dans tous ces cas, il faut **supprimer l'arrière-plan de l'image**. Autrefois, cela voulait dire détourer à la main dans un logiciel de retouche. Aujourd'hui, une IA le fait en quelques secondes. Le [détoureur d'images](/image-background-remover/) de DoraPDF (interface en anglais) a une particularité : l'IA tourne **dans votre navigateur**, la photo n'est donc envoyée nulle part.

## Comment ça marche

Un modèle d'intelligence artificielle analyse l'image et calcule, pixel par pixel, ce qui appartient au sujet et ce qui appartient au fond. Le fond devient transparent, ou est remplacé par une couleur unie. Le résultat est enregistré en **PNG**, le format qui conserve la transparence.

Ce modèle est téléchargé une seule fois par votre navigateur, puis réutilisé. D'où les deux modes proposés :

| Mode | Idéal pour | Téléchargement unique | Ce qu'il faut |
|---|---|---|---|
| **Quick** | personnes, portraits, selfies | environ 13 Mo | n'importe quel navigateur récent |
| **HD** | tout objet : produits, animaux, plantes | environ 115 Mo | un navigateur avec accélération graphique (WebGPU) |

Si votre navigateur ne gère pas WebGPU, l'outil le signale et bascule automatiquement sur le mode Quick.

## Enlever le fond d'une image, étape par étape

1. Ouvrez le [détoureur d'images](/image-background-remover/).
2. Dans **Mode**, choisissez *Quick* pour une personne, *HD* pour un objet.
3. Dans **Background**, choisissez le résultat voulu : *Transparent*, *White* (blanc), *Black*, *Light grey* ou *Pink*.
4. Déposez votre image (JPG, PNG, WebP ou HEIC d'iPhone).
5. Cliquez sur **Remove background**. La première fois, patientez pendant le téléchargement du modèle ; les fois suivantes, c'est bien plus rapide.
6. Faites glisser le curseur de comparaison pour voir l'avant et l'après, puis téléchargez le fichier `-no-bg.png`.

Les très grandes photos sont ramenées à 2 000 pixels sur le plus grand côté, ce qui suffit largement pour le web, les annonces et les documents.

## Fond transparent ou fond blanc : lequel choisir ?

**Transparent** si l'image va être posée sur autre chose : un logo sur un site, un sujet à intégrer dans un montage, une signature à insérer dans un document. Attention : la transparence n'existe qu'en PNG (ou WebP). Si vous convertissez ensuite en JPG, le fond deviendra blanc ou noir selon le logiciel.

**Blanc** pour la plupart des annonces de vente et des boutiques en ligne : un fond blanc uni fait ressortir le produit et donne une galerie homogène. C'est aussi pratique pour une photo de type portrait sur un CV.

**Gris clair** pour un objet blanc (une tasse, une paire de baskets blanches) qui se perdrait sur un fond blanc pur.

## Des exemples concrets

**Photo de produit pour une annonce.** Posez l'objet sur une surface dégagée, près d'une fenêtre, et photographiez-le bien de face. Mode *HD*, fond *White*. Vous obtenez un visuel net qui se démarque dans les résultats de recherche des sites de petites annonces.

**Portrait pour un CV ou un profil professionnel.** Mode *Quick*, fond *White* ou *Light grey*. Recadrez ensuite l'image au carré avec le [redimensionneur d'images](/image-resizer/) si la plateforme le demande.

**Logo récupéré sur un vieux document.** Mode *HD*, fond *Transparent*. Pour un logo très simple (texte et aplats de couleur), le résultat peut ensuite être vectorisé avec [PNG en SVG](/png-to-svg/).

## Obtenir un détourage propre

- **Un contraste net aide beaucoup.** Un pull noir devant un mur blanc se détoure mieux qu'un pull beige devant un canapé beige.
- **Évitez le flou.** L'IA a du mal avec les contours flous ou bougés : ils deviennent semi-transparents.
- **Les cheveux et la fourrure** sont les zones les plus délicates. Le mode *HD* les gère généralement mieux ; zoomez sur le résultat pour vérifier.
- **Les objets transparents** (verre, bouteille, voilage) restent difficiles pour n'importe quel outil automatique : une partie du fond peut rester visible à travers.
- **Plusieurs sujets** sur une même photo ? Le mode *Quick* est entraîné pour les personnes ; pour un groupe d'objets, utilisez *HD*.

## Problèmes fréquents

**« No GPU acceleration in this browser — using Quick mode »** : votre navigateur ou votre appareil ne prend pas en charge WebGPU. Essayez une version récente de Chrome ou Edge sur ordinateur, ou contentez-vous du mode Quick.

**« AI model could not load »** : le téléchargement du modèle a échoué. Vérifiez votre connexion et réessayez ; une fois le modèle chargé, l'outil n'a plus besoin de le retélécharger à chaque image.

**Un bord du sujet a disparu** : la zone était sans doute trop proche de la couleur du fond. Reprenez la photo avec un fond plus contrasté, ou essayez l'autre mode.

**Le fichier PNG est lourd** : un PNG transparent pèse plus qu'un JPG. Pour un site web, passez-le dans le [compresseur d'images](/image-compressor/) : les PNG y sont convertis en WebP, qui conserve la transparence pour un poids bien moindre.

## Confidentialité

C'est la vraie différence avec la plupart des services en ligne : ici, **la photo reste sur votre appareil**. Seul le modèle d'IA est téléchargé ; le traitement se fait dans votre navigateur. Pour des photos de personnes, d'enfants ou de documents, c'est une garantie appréciable.

## Questions fréquentes

**Peut-on supprimer l'arrière-plan d'une image gratuitement sans inscription ?**
Oui, sans compte et sans filigrane sur le résultat.

**L'outil marche-t-il sur téléphone ?**
Oui, en mode Quick dans un navigateur récent. Le mode HD demande plus de mémoire et l'accélération graphique, il est plus fiable sur ordinateur.

**Peut-on traiter plusieurs images à la fois ?**
L'outil traite une image à la fois. Une fois le modèle chargé, les images suivantes vont vite.

**Pourquoi le premier essai est-il lent ?**
Le navigateur télécharge le modèle d'IA (environ 13 Mo ou 115 Mo selon le mode). Ce téléchargement n'a lieu qu'une fois.
"""),
dict(slug='extraire-texte-image-ocr-gratuit', lang='fr', title="Extraire le texte d'une image (OCR) : copier le texte d'une photo, d'une capture ou d'un scan", date='2026-11-17',
 desc="Extraire le texte d'une image gratuitement grâce à l'OCR : photo, capture d'écran ou PDF scanné. Réglez la langue sur le français pour garder les accents.",
 tools=['image-to-text', 'pdf-ocr', 'scan-to-pdf'], md="""
Vous avez une photo d'un tableau blanc, une capture d'écran d'un message, la page d'un livre ou un vieux courrier scanné, et vous voulez **récupérer le texte** pour le modifier, le citer ou le traduire, sans tout retaper. C'est exactement le rôle de l'**OCR** (reconnaissance optique de caractères). DoraPDF propose deux outils gratuits pour **extraire le texte d'une image** ou d'un PDF scanné, sans inscription, avec un traitement qui reste dans votre navigateur.

## Deux outils selon votre fichier

- **[Image en texte](/image-to-text/)** (interface en anglais) : pour les photos et captures d'écran (JPG, PNG, WebP, HEIC). Vous obtenez le texte brut, à copier ou à télécharger en `.txt`.
- **[PDF OCR](/pdf-ocr/)** (interface en anglais) : pour un PDF scanné. Vous obtenez un **PDF « interrogeable »** qui a exactement le même aspect que l'original, mais dans lequel on peut sélectionner, copier et rechercher le texte, plus un fichier `.txt`.

## Extraire le texte d'une image, pas à pas

1. Ouvrez [Image en texte](/image-to-text/).
2. Dans **Language**, choisissez **French**. C'est l'étape la plus importante : la langue par défaut est l'anglais, et un texte français reconnu « en anglais » perd souvent ses accents (é, è, à, ç) ou les transforme en caractères bizarres.
3. Déposez votre image. Vous pouvez en ajouter plusieurs d'un coup : leurs textes seront mis bout à bout, chacun précédé du nom du fichier.
4. Cliquez sur **Extract text**.
5. Le texte apparaît dans une zone modifiable. Corrigez si besoin, puis cliquez sur **Copy text** ou téléchargez le fichier `.txt`.

La première fois, le navigateur télécharge le modèle de reconnaissance pour la langue choisie (quelques mégaoctets). Ensuite, c'est plus rapide.

Autres langues disponibles : anglais, allemand, espagnol, italien, portugais, arabe, turc, russe, chinois simplifié, entre autres. Pour un document bilingue, choisissez la langue majoritaire.

## Rendre un PDF scanné copiable

Un PDF issu d'un scanner ou d'une application de numérisation n'est souvent qu'une suite d'images : impossible d'y faire une recherche avec Ctrl+F ou de copier une phrase.

1. Ouvrez [PDF OCR](/pdf-ocr/).
2. Choisissez **French** dans **Language**.
3. Déposez le PDF et cliquez sur **Run OCR**.
4. Téléchargez le fichier `-searchable.pdf` et, si besoin, le `.txt`.

Comptez environ 5 à 15 secondes par page, selon votre appareil. L'outil traite jusqu'à 60 pages par fichier ; pour un document plus long, découpez-le d'abord avec [Diviser un PDF](/pdf-splitter/) et traitez les parties l'une après l'autre.

## Ce que l'OCR fait bien, et moins bien

L'OCR fonctionne très bien sur :

- les **captures d'écran** (texte net, fond uni) ;
- les **documents imprimés** scannés ou photographiés bien à plat ;
- les pages de **livres et magazines** avec une mise en page simple.

Il a plus de mal avec :

- l'**écriture manuscrite**, surtout cursive : attendez-vous à beaucoup d'erreurs, voire à un résultat inutilisable ;
- les **photos penchées, floues ou mal éclairées** ;
- les **mises en page complexes** (colonnes multiples, encadrés, tableaux) : le texte est récupéré, mais l'ordre de lecture peut être mélangé ;
- les **polices décoratives** et les textes sur fond chargé (affiche, photo).

## Conseils pour une reconnaissance fiable

**Cadrez serré.** Plus le texte occupe l'image, mieux il est lu. Recadrez avant de lancer l'extraction si la photo contient beaucoup de décor.

**Photographiez bien en face.** Une page prise de biais déforme les lignes. Pour des feuilles de papier, [Scanner en PDF](/scan-to-pdf/) permet de redresser la page en déplaçant ses coins, puis vous passez le PDF obtenu dans l'outil OCR.

**Lumière uniforme, pas de flash.** Une ombre de main ou un reflet sur papier glacé suffit à effacer quelques mots.

**Relisez les chiffres.** Un « 0 » lu comme un « O », un « 1 » comme un « l » : pour des montants, des références ou des numéros de téléphone, vérifiez systématiquement.

## Idées d'usages

- **Étudiants** : récupérer une citation dans un livre photographié, ou les notes d'un tableau en fin de cours (si elles sont écrites lisiblement en majuscules, le résultat est souvent correct).
- **Vie administrative** : retrouver un numéro de contrat dans un vieux courrier scanné grâce à la recherche dans le PDF interrogeable.
- **Travail** : récupérer le texte d'une capture d'écran envoyée par un collègue au lieu de le recopier.
- **Traduction** : extraire le texte d'un document en langue étrangère, puis le coller dans un traducteur.

## Problèmes fréquents

**« No readable text found in this image »** : aucun texte n'a été reconnu. L'image est peut-être trop petite, floue, ou le texte est manuscrit. Essayez une photo plus nette et plus proche.

**Les accents sont remplacés par des symboles** : vérifiez que la langue sélectionnée est bien *French*, puis relancez.

**Le texte est dans le désordre** : c'est fréquent avec les mises en page en colonnes. Recadrez chaque colonne séparément et traitez-les comme des images distinctes.

## Confidentialité

La reconnaissance est faite **dans votre navigateur** : vos images et vos PDF ne sont pas envoyés sur nos serveurs. Seul le modèle de langue est téléchargé. C'est un avantage réel pour des courriers, des relevés ou des documents de travail confidentiels.

## Questions fréquentes

**L'OCR est-il gratuit et sans inscription ?**
Oui, les deux outils sont gratuits, sans compte et sans limite d'utilisation.

**Peut-on extraire le texte d'une image sur iPhone ?**
Oui, depuis Safari. Les photos HEIC de l'iPhone sont acceptées directement.

**L'outil reconnaît-il l'écriture manuscrite ?**
Très partiellement. Il est conçu pour du texte imprimé ; l'écriture à la main donne des résultats peu fiables.

**Le PDF interrogeable a-t-il le même aspect que l'original ?**
Oui. Chaque page est conservée comme image, et une couche de texte invisible est placée par-dessus, au bon endroit, pour permettre la sélection et la recherche.
"""),
dict(slug='signer-pdf-sans-imprimer', lang='fr', title="Signer un PDF sans l'imprimer : dessiner ou taper sa signature et la placer sur le document", date='2026-11-17',
 desc="Signer un PDF gratuitement sans l'imprimer ni le scanner : dessinez votre signature au doigt ou à la souris, choisissez la page et téléchargez le PDF signé.",
 tools=['sign-pdf', 'pdf-editor', 'pdf-merger'], md="""
Imprimer un document, le signer au stylo, le scanner, puis le renvoyer : pour une attestation, un devis ou une autorisation de sortie scolaire, c'est beaucoup d'efforts pour une seule signature. Vous pouvez **signer un PDF sans l'imprimer**, directement dans le navigateur, avec l'outil [Signer un PDF](/sign-pdf/) de DoraPDF (interface en anglais). C'est gratuit, sans inscription, et le document reste sur votre appareil.

Avant de commencer, un point important sur la valeur juridique, pour savoir quand cet outil suffit et quand il ne suffit pas.

## Signature « image » ou signature électronique certifiée ?

L'outil ajoute sur le PDF **une image de votre signature**, comme si vous aviez signé au stylo puis scanné la page. En droit européen (règlement eIDAS), c'est une **signature électronique simple** : elle est valable dans de nombreuses situations du quotidien, mais elle ne prouve pas à elle seule qui a signé.

Elle convient généralement pour :

- un devis ou un bon de commande à retourner ;
- une attestation sur l'honneur, une autorisation parentale ;
- un formulaire interne, une note de frais ;
- un courrier que vous envoyez vous-même par e-mail.

Pour un acte où l'enjeu est élevé (contrat de travail, compromis de vente, engagement de caution, documents bancaires), l'autre partie impose souvent une **signature électronique avancée ou qualifiée**, réalisée via un prestataire qui vérifie votre identité. Dans le doute, demandez au destinataire ce qu'il accepte.

## Signer un PDF en ligne, étape par étape

1. Ouvrez [Signer un PDF](/sign-pdf/).
2. **Dessinez votre signature** dans le cadre blanc, à la souris, au pavé tactile ou au doigt sur un téléphone. Raté ? Cliquez sur **Clear** et recommencez.
3. Vous préférez ne pas dessiner ? Tapez votre nom dans le champ **Or type it** : il s'affiche dans une écriture manuscrite.
4. Déposez le PDF à signer.
5. Réglez les options :
   - **Page** : `last` (dernière page, par défaut) ou un numéro de page, par exemple `2` ;
   - **Position** : en bas à droite, en bas à gauche ou en bas au centre ;
   - **Size** : la largeur de la signature, de 10 à 50 % de la largeur de la page.
6. Cliquez sur **Sign PDF**, puis téléchargez le fichier `-signed.pdf`.

Ouvrez toujours le résultat pour vérifier que la signature ne recouvre pas un texte. Si c'est le cas, changez la position ou réduisez la taille, puis relancez à partir du fichier d'origine.

## Ajouter « Lu et approuvé », la date et le lieu

Beaucoup de documents français demandent une mention manuscrite : « Lu et approuvé », « Bon pour accord », ou « Fait à Lyon, le 17 novembre 2026 ». Voici comment procéder :

1. Ouvrez le PDF dans l'[éditeur de PDF](/pdf-editor/) (interface en anglais).
2. Tapez la mention dans le champ **Text**, puis cliquez sur la page à l'endroit voulu. Répétez pour la date et le lieu.
3. Enregistrez avec **Save PDF**.
4. Signez ensuite ce nouveau fichier avec [Signer un PDF](/sign-pdf/).

L'éditeur permet aussi de remplir les champs vides d'un formulaire non interactif : nom, adresse, numéro de dossier.

## Conseils pour une signature qui ressemble à la vôtre

**Sur ordinateur, préférez un pavé tactile ou une tablette** à la souris : le tracé est plus naturel.

**Sur téléphone, signez en tenant l'appareil à l'horizontale** : le cadre est plus large, la signature moins tassée.

**Ne la faites pas trop grande.** Une taille de 20 à 25 % de la largeur de page correspond à peu près à une signature au stylo. Au-delà de 35 %, elle paraît disproportionnée.

**Plusieurs pages à parapher ?** L'outil place une signature sur une page à la fois. Pour parapher chaque page, relancez l'opération sur le fichier déjà signé en changeant le numéro de page, en position *Bottom right*, avec une taille réduite (10 à 15 %).

## Limites à connaître

- La signature se place **en bas de page** (droite, gauche ou centre). Si le document prévoit un cadre « Signature » au milieu de la page, la position ne tombera pas forcément dedans. Dans ce cas, signez en bas de la page concernée, à côté de la mention manuscrite.
- La signature est toujours **bleu foncé**, sur fond transparent.
- Pour un PDF protégé par mot de passe dont vous êtes le propriétaire, retirez d'abord la protection avec [Déverrouiller un PDF](/unlock-pdf/).

## Signer plusieurs documents d'un dossier

Si vous devez retourner plusieurs pièces signées dans un seul envoi, signez chaque document séparément, puis réunissez-les avec [Fusionner des PDF](/pdf-merger/) (interface en anglais). Le destinataire reçoit un seul fichier, dans l'ordre que vous avez choisi.

## Confidentialité

Votre signature est une donnée sensible : mal utilisée, elle peut servir à imiter votre accord. Avec DoraPDF, la signature et le document sont traités **dans votre navigateur** : rien n'est envoyé sur nos serveurs, rien n'est conservé. Votre signature n'est pas enregistrée d'une visite à l'autre ; vous la redessinez à chaque fois.

## Questions fréquentes

**Peut-on signer un PDF gratuitement sur iPhone ou Android ?**
Oui, depuis le navigateur du téléphone. Vous signez au doigt dans le cadre, puis vous choisissez le PDF dans vos fichiers.

**La signature est-elle légalement valable ?**
C'est une signature électronique simple, acceptée pour de nombreux documents courants. Pour un contrat important, l'autre partie peut exiger une signature avancée ou qualifiée via un prestataire spécialisé.

**Peut-on retirer une signature ajoutée par erreur ?**
Le fichier d'origine n'est pas modifié : repartez simplement de celui-ci et signez de nouveau.

**Faut-il installer Adobe Acrobat ?**
Non. Tout se fait dans le navigateur, sans logiciel ni extension.
"""),
dict(slug='convertir-word-en-pdf-gratuit', lang='fr', title='Convertir Word en PDF gratuitement, sans logiciel : la méthode rapide et ses limites', date='2026-11-17',
 desc='Convertir un document Word (.docx) en PDF gratuitement, sans installer de logiciel, sur PC ou téléphone. Ce qui est conservé, et quand préférer Word.',
 tools=['word-to-pdf', 'pdf-compressor', 'pdf-merger'], md="""
On vous demande votre CV « en PDF », le secrétariat n'accepte que des PDF, ou vous voulez simplement éviter que la mise en page bouge chez le destinataire. Si vous avez Microsoft Word sous la main, la commande *Enregistrer sous > PDF* fait très bien le travail. Mais sur un téléphone, sur l'ordinateur d'une médiathèque ou quand on vous a envoyé un `.docx` que vous ne pouvez pas ouvrir, il faut une autre solution. L'outil [Word en PDF](/word-to-pdf/) de DoraPDF (interface en anglais) permet de **convertir Word en PDF gratuitement, sans logiciel** et sans inscription.

Ce guide explique la marche à suivre, mais aussi, honnêtement, ce que cette conversion conserve et ce qu'elle ne conserve pas, pour choisir la bonne méthode selon votre document.

## Convertir un fichier Word en PDF en trois étapes

1. Ouvrez [Word en PDF](/word-to-pdf/).
2. Déposez votre fichier **.docx**.
3. Cliquez sur **Convert now**, puis téléchargez le PDF, qui porte le même nom que votre document.

Le PDF est créé au **format A4**, le format standard en France et en Europe.

Seul le format `.docx` (Word 2007 et versions suivantes) est accepté. Si vous avez un ancien `.doc`, ouvrez-le dans Word, LibreOffice ou Google Docs et réenregistrez-le en `.docx` avant la conversion. Pour un fichier LibreOffice `.odt`, il existe l'outil [ODT en PDF](/odf-to-pdf/), qui reprend le texte seul, sans la mise en forme.

## Ce que la conversion conserve

L'outil lit le contenu de votre document puis le recompose en pages A4. Il reprend :

- les **titres** et les paragraphes ;
- le **gras**, l'*italique* et les listes à puces ou numérotées ;
- les **tableaux** (avec des bordures fines) ;
- les **images** insérées dans le texte.

Pour un courrier, un compte rendu, un exposé ou un CV à la mise en page simple, le résultat est propre et lisible.

## Ce qu'elle ne conserve pas

Il vaut mieux le savoir avant d'envoyer un document important :

- **Les polices** : le texte est affiché dans une police à empattements standard, pas forcément celle que vous avez choisie.
- **La mise en page exacte** : marges personnalisées, colonnes, zones de texte, formes, en-têtes et pieds de page, numéros de page et sauts de page ne sont pas reproduits à l'identique.
- **Le texte sélectionnable** : chaque page du PDF est enregistrée comme une image. On peut lire et imprimer le document, mais pas copier une phrase ni faire une recherche dedans.

Conséquence pratique : pour un **CV très graphique**, un mémoire avec sommaire et numérotation, ou un document qui sera lu par un logiciel de recrutement (qui doit pouvoir lire le texte), préférez l'export PDF intégré de Word, de LibreOffice (gratuit) ou de Google Docs (*Fichier > Télécharger > Document PDF*). Ces logiciels reproduisent la mise en page à l'identique et gardent le texte sélectionnable.

## Quand l'outil en ligne est le bon choix

- Vous êtes **sur téléphone** et vous devez renvoyer un document Word en PDF, vite.
- Vous êtes sur un **ordinateur partagé** sans Word et vous ne voulez pas vous connecter à un compte en ligne.
- Vous voulez **figer un document simple** (lettre, attestation, liste) pour qu'il ne soit pas modifié facilement.
- Vous avez reçu un `.docx` et voulez simplement **le lire ou l'imprimer** depuis n'importe quel appareil.

## Conseils pour un meilleur résultat

**Gardez une mise en page simple.** Titres définis avec les styles de Word (Titre 1, Titre 2), paragraphes normaux, tableaux simples : c'est ce qui passe le mieux.

**Évitez les zones de texte pour le contenu important.** Si une information clé (vos coordonnées sur un CV, par exemple) est dans une zone de texte flottante, mettez-la plutôt dans un paragraphe ou un tableau.

**Vérifiez chaque page.** Ouvrez le PDF et faites défiler jusqu'au bout avant de l'envoyer, en particulier les tableaux longs.

**Pour un document à signer**, convertissez d'abord, puis ajoutez la signature avec [Signer un PDF](/sign-pdf/).

## Problèmes fréquents

**Le fichier n'est pas accepté.** C'est probablement un `.doc` ou un `.odt`. Réenregistrez-le en `.docx`.

**Une image manque.** Les images collées comme objets flottants ou intégrées à des formes peuvent ne pas être reprises. Insérez-les « aligné sur le texte » dans Word, puis reconvertissez.

**Le PDF est lourd.** Comme les pages sont des images, un long document peut peser plusieurs mégaoctets. Réduisez-le avec le [compresseur de PDF](/pdf-compressor/) (interface en anglais) si un portail impose une limite.

**Plusieurs fichiers Word à envoyer ensemble.** Convertissez-les un par un, puis réunissez les PDF avec [Fusionner des PDF](/pdf-merger/).

## Confidentialité

Le document est converti **dans votre navigateur** : il n'est pas envoyé sur nos serveurs et n'est conservé nulle part. Pour un contrat, un dossier RH ou un courrier personnel, c'est plus rassurant que de déposer le fichier sur un service inconnu.

## Questions fréquentes

**Peut-on convertir Word en PDF gratuitement sans inscription ?**
Oui, l'outil est gratuit, sans compte et sans filigrane.

**La mise en page est-elle conservée à l'identique ?**
Pas entièrement : la structure (titres, listes, tableaux, images) est reprise, mais pas les polices, les en-têtes et pieds de page ni la position exacte des éléments. Pour une copie fidèle, utilisez l'export PDF de Word, LibreOffice ou Google Docs.

**Peut-on copier le texte du PDF obtenu ?**
Non, les pages sont des images. Si vous avez besoin d'un texte copiable, passez le PDF dans [PDF OCR](/pdf-ocr/) ou utilisez l'export natif de votre traitement de texte.

**Comment convertir un document Word en PDF sur iPhone ?**
Ouvrez l'outil dans Safari, choisissez le fichier `.docx` dans l'app Fichiers, puis enregistrez le PDF obtenu au même endroit.
"""),
dict(slug='convertir-heic-en-jpg-windows', lang='fr', title="Convertir HEIC en JPG : ouvrir les photos de l'iPhone sur Windows (et partout ailleurs)", date='2026-11-17',
 desc="Convertir HEIC en JPG gratuitement, en lot et sans logiciel : ouvrez vos photos d'iPhone sur Windows, envoyez-les partout et évitez le problème à l'avenir.",
 tools=['heic-to-jpg', 'heic-to-pdf', 'image-compressor'], md="""
Vous transférez les photos de votre iPhone sur un PC Windows, et une partie refuse de s'ouvrir. Ou un site d'annonces, un portail administratif ou une imprimante photo affiche « format non pris en charge ». Le coupable s'appelle **HEIC**, le format par défaut des iPhone. La solution la plus simple : **convertir les HEIC en JPG**, le format que tout le monde sait lire. Avec le [convertisseur HEIC en JPG](/heic-to-jpg/) de DoraPDF (interface en anglais), c'est gratuit, sans inscription, et vous pouvez convertir des dizaines de photos d'un coup.

## HEIC, c'est quoi exactement ?

HEIC (ou HEIF) est un format d'image moderne adopté par Apple depuis iOS 11. À qualité visuelle comparable, une photo HEIC pèse sensiblement moins qu'un JPG, ce qui économise de la place sur le téléphone et dans iCloud.

Le revers : tout le monde ne le lit pas. Selon la version et la configuration de Windows, les fichiers HEIC peuvent ne pas s'ouvrir sans extension supplémentaire, et de nombreux sites web, logiciels anciens et bornes d'impression ne les acceptent pas.

## Convertir HEIC en JPG, étape par étape

1. Ouvrez le [convertisseur HEIC en JPG](/heic-to-jpg/).
2. Glissez vos fichiers `.heic` dans la zone de dépôt. Vous pouvez en sélectionner plusieurs à la fois, et en ajouter d'autres ensuite.
3. Réglez la **Quality** si besoin : le curseur va de 40 à 100, avec 92 par défaut.
4. Cliquez sur **Convert now**.
5. Chaque photo apparaît dans la liste avec son nouveau poids : cliquez sur **Download** à côté de chacune.

Les photos gardent leur **résolution d'origine** : seul le format change.

## Quelle qualité choisir ?

- **92 (par défaut)** : visuellement identique à l'original pour l'immense majorité des usages. Bon choix pour l'impression et l'archivage.
- **80 à 85** : fichiers nettement plus légers, différence presque invisible à l'écran. Idéal pour envoyer par e-mail ou publier sur un site.
- **En dessous de 70** : réservé aux cas où la taille compte plus que tout ; des défauts peuvent apparaître dans les dégradés (ciel, peau).

Le JPG obtenu est souvent un peu plus lourd que le HEIC d'origine : c'est normal, le JPG est un format plus ancien et moins efficace.

## Sur Windows : convertir ou installer une extension ?

Il existe deux approches :

- **Installer une extension de lecture HEIF** depuis le Microsoft Store. Vous pourrez alors ouvrir les HEIC dans l'application Photos de Windows. Mais cela ne règle que votre PC : la personne à qui vous envoyez la photo, ou le site sur lequel vous la déposez, aura peut-être le même problème.
- **Convertir en JPG** : le fichier devient lisible partout, sur tous les appareils et tous les sites. C'est la solution la plus sûre dès que la photo doit être partagée.

## Éviter le problème dès le départ (réglages iPhone)

Deux réglages de l'iPhone permettent de limiter les HEIC :

- **Réglages > Appareil photo > Formats > « Le plus compatible »** : les nouvelles photos sont prises en JPG au lieu de HEIC. Inconvénient : elles occupent plus d'espace.
- **Réglages > Photos > « Transférer sur Mac ou PC » > « Automatique »** : quand vous branchez l'iPhone sur un ordinateur, les photos sont converties dans un format compatible pendant le transfert.

Ces réglages ne changent rien aux photos déjà prises : pour celles-là, la conversion reste nécessaire.

## Autres besoins fréquents

**Mettre plusieurs photos d'iPhone dans un PDF** (un justificatif photographié, un relevé de notes) : utilisez directement [HEIC en PDF](/heic-to-pdf/) (interface en anglais), sans passer par le JPG.

**Garder la transparence ou une qualité sans perte** : convertissez plutôt en PNG avec [HEIC en PNG](/heic-to-png/). Les fichiers seront bien plus lourds, mais sans aucune compression destructrice.

**Respecter une limite de poids** (par exemple 500 Ko sur un formulaire) : après la conversion, passez les JPG dans le [compresseur d'images](/image-compressor/), qui peut aussi réduire les dimensions.

## Problèmes fréquents

**Le bouton ne réagit pas avec beaucoup de photos.** La conversion se fait sur votre appareil. Avec plus d'une cinquantaine de photos en haute résolution, procédez par lots de 10 à 20.

**Une photo est tournée.** Ouvrez le JPG obtenu dans une autre visionneuse pour vérifier ; si elle reste mal orientée, faites-la pivoter avec n'importe quel éditeur d'images.

**Les informations de la photo ont disparu.** La conversion crée un nouveau fichier image : les métadonnées comme la date de prise de vue, le modèle d'appareil ou la position GPS ne sont pas recopiées. C'est plutôt un avantage pour la vie privée quand vous publiez une photo en ligne, mais pensez à garder les originaux si vous classez vos photos par date.

**Un fichier « .heic » n'est pas reconnu.** Certaines photos en mode Live ou certaines rafales sont enregistrées différemment. Exportez-les depuis l'app Photos de l'iPhone en tant que photo fixe, puis réessayez.

## Confidentialité

Vos photos personnelles ne quittent pas votre appareil : la conversion se fait **entièrement dans votre navigateur**, sans envoi sur un serveur, sans stockage. Vous pouvez convertir des photos de famille ou de documents en toute tranquillité.

## Questions fréquentes

**Convertir HEIC en JPG est-il gratuit ?**
Oui, sans inscription, sans limite et sans filigrane.

**Peut-on convertir plusieurs photos HEIC à la fois ?**
Oui. Déposez-les toutes ensemble ; chaque photo est convertie et peut être téléchargée individuellement.

**La qualité baisse-t-elle ?**
Avec la qualité par défaut (92), la différence est invisible dans la pratique. La résolution reste identique à l'original.

**Ça marche sur Mac et sur Android ?**
Oui, l'outil fonctionne dans n'importe quel navigateur récent, sur ordinateur comme sur téléphone.
"""),
dict(slug='convertir-pdf-en-excel-gratuit', lang='fr', title='Convertir un PDF en Excel gratuitement : récupérer un tableau sans tout retaper', date='2026-11-17',
 desc='Convertir un PDF en Excel (.xlsx) gratuitement, sans inscription : extraire un tableau, vérifier les montants à virgule et que faire avec un PDF scanné.',
 tools=['pdf-to-excel', 'pdf-ocr', 'pdf-splitter'], md="""
Un relevé bancaire, une liste de prix fournisseur, un export de logiciel de comptabilité, un tableau de résultats : les données sont là, mais enfermées dans un PDF. Les recopier à la main dans un tableur prend du temps et produit des erreurs. Avec l'outil [PDF en Excel](/pdf-to-excel/) de DoraPDF (interface en anglais), vous pouvez **convertir un PDF en Excel** gratuitement, sans inscription, et obtenir un fichier `.xlsx` à retravailler dans Excel, LibreOffice Calc ou Google Sheets.

Le principe est simple, mais quelques précautions évitent les mauvaises surprises, surtout avec les montants à la française.

## Comment fonctionne la conversion

L'outil lit le texte du PDF ligne par ligne. Quand il détecte un espace suffisamment large entre deux blocs de texte, il considère qu'il s'agit de deux colonnes différentes et les place dans deux cellules. Chaque page du PDF devient **une feuille** du classeur, nommée « Page 1 », « Page 2 », etc. La largeur des colonnes est ajustée automatiquement à leur contenu.

Cela fonctionne bien pour les PDF **créés par un logiciel** (export d'un ERP, relevé téléchargé depuis l'espace client de votre banque, facture générée en ligne). Pour un PDF **scanné**, il n'y a pas de texte à lire : voir plus bas.

## Convertir un PDF en Excel, pas à pas

1. Ouvrez [PDF en Excel](/pdf-to-excel/).
2. Déposez votre fichier PDF.
3. Cliquez sur **Convert now**.
4. Téléchargez le fichier `.xlsx`, qui porte le même nom que le PDF.
5. Ouvrez-le dans votre tableur et parcourez chaque feuille.

Astuce : si seules deux pages vous intéressent dans un document de quarante, extrayez-les d'abord avec [Diviser un PDF](/pdf-splitter/) (interface en anglais). Le classeur sera plus simple à nettoyer.

## Attention aux montants avec une virgule décimale

C'est le point à vérifier en priorité. L'outil reconnaît automatiquement les nombres pour les transformer en vraies valeurs numériques, mais il suit la **notation anglo-saxonne**, où la virgule sépare les milliers (1,234.56). Or en France on écrit 1 234,56.

Concrètement, un montant comme **12,50** peut être interprété comme **1250**. Les montants écrits avec une espace pour les milliers (1 234,56) restent en général du texte, et ne sont donc pas faussés, mais il faudra les convertir en nombres pour faire des calculs.

Comment s'en sortir :

- **Comparez quelques lignes avec le PDF** dès l'ouverture du fichier, en particulier les colonnes de montants.
- Si tous les montants d'une colonne ont deux décimales et ont été lus sans la virgule, une colonne voisine avec la formule `=A2/100` les remet à la bonne échelle.
- Pour les montants restés en texte, sélectionnez la colonne et utilisez *Données > Convertir* dans Excel (ou *Rechercher et remplacer* pour supprimer les espaces), puis vérifiez le séparateur décimal.

Les PDF issus de logiciels anglophones ou internationaux (montants comme 1,234.56) ne posent pas ce problème.

## Et un PDF scanné ?

Si le PDF provient d'un scanner ou d'une photo, l'outil affiche « No text found — this PDF looks scanned ». Deux options :

1. Passez d'abord le fichier dans [PDF OCR](/pdf-ocr/) en choisissant la langue *French*. Vous obtenez un PDF dont le texte est lisible par les logiciels, que vous pouvez ensuite essayer de convertir en Excel. Le résultat dépend de la qualité du scan ; relisez attentivement les chiffres.
2. Pour un petit tableau, il est parfois plus rapide d'extraire le texte avec l'OCR, puis de le coller dans le tableur et de le répartir en colonnes.

## Nettoyer le tableau dans Excel

Même avec un bon PDF, le classeur demande souvent quelques retouches :

- **Cellules sur plusieurs lignes** : un libellé long qui tient sur deux lignes dans le PDF peut donner deux lignes dans Excel. Fusionnez-les à la main ou avec une formule de concaténation.
- **Colonnes décalées** : quand une cellule est vide dans le PDF, les valeurs suivantes peuvent glisser d'une colonne vers la gauche. Triez ou filtrez pour repérer ces lignes.
- **En-têtes et pieds de page répétés** : le nom de la banque, la mention « Page 3/12 » ou le total reporté apparaissent sur chaque feuille. Supprimez-les avant de regrouper les données.
- **Regrouper toutes les pages** : copiez les lignes utiles de chaque feuille l'une sous l'autre dans une nouvelle feuille, ou utilisez Power Query (*Données > Obtenir des données*) si vous le faites souvent.

## Exemples d'usage

**Suivre ses dépenses.** Convertissez le relevé mensuel de votre compte, supprimez les lignes d'en-tête, et vous avez une base pour un budget avec des totaux par catégorie.

**Comparer des tarifs.** Deux grilles de prix fournisseurs en PDF deviennent deux feuilles que vous pouvez comparer ligne à ligne avec une formule RECHERCHEV.

**Reprendre des données pour un devoir ou un rapport.** Un tableau statistique publié en PDF devient un graphique dans Excel en quelques minutes. Citez toujours la source.

## Confidentialité

Un relevé bancaire ou un fichier client n'a rien à faire sur un serveur inconnu. Avec DoraPDF, la conversion se fait **dans votre navigateur** : le PDF n'est pas envoyé sur nos serveurs et n'est pas conservé.

## Questions fréquentes

**Peut-on convertir un PDF en Excel gratuitement et sans inscription ?**
Oui, sans compte, sans limite et sans filigrane.

**La mise en forme (couleurs, bordures) est-elle conservée ?**
Non. L'outil récupère le contenu des cellules, pas la présentation. C'est souvent préférable pour retravailler les données.

**Pourquoi tout est-il dans une seule colonne ?**
Les colonnes du PDF sont trop serrées pour être distinguées. Utilisez *Données > Convertir* dans Excel pour découper la colonne selon un séparateur.

**Le fichier fonctionne-t-il avec Google Sheets et LibreOffice ?**
Oui, le format `.xlsx` s'ouvre dans tous les tableurs courants.
"""),
dict(slug='creer-facture-gratuit-tva', lang='fr', title='Créer une facture gratuitement avec TVA : méthode, mentions obligatoires et pièges à éviter', date='2026-11-17',
 desc="Créer une facture gratuite en PDF avec TVA, en euros, sans inscription : mentions obligatoires en France, cas de l'auto-entrepreneur et astuce pour les remises.",
 tools=['invoice-generator', 'receipt-generator', 'sign-pdf'], md="""
Premier client en freelance, prestation ponctuelle, vente entre professionnels : il faut une facture, et vite. Un logiciel de facturation complet n'est pas toujours nécessaire pour quelques factures par an. Le [générateur de factures](/invoice-generator/) de DoraPDF (interface en anglais) permet de **créer une facture gratuitement**, avec TVA, en euros, et de la télécharger en PDF A4, sans inscription. Ce guide explique comment le remplir et surtout quelles mentions ajouter pour une facture correcte en France.

Petit rappel : ce guide donne des repères pratiques, pas un conseil juridique ou comptable. En cas de doute sur votre situation, interrogez votre expert-comptable ou le service des impôts des entreprises.

## Les champs du générateur

Le formulaire tient sur une seule page :

- **From** : le nom de votre entreprise ;
- **Your details** : adresse, téléphone, e-mail et, en France, vos numéros d'identification (voir plus bas) ;
- **Invoice #** : le numéro de facture ;
- **Date** et **Due date** : date d'émission et date d'échéance ;
- **Bill to** : nom et adresse du client ;
- les **lignes de prestation** : description (*Item*), quantité (*Qty*) et prix unitaire (*Price*), avec un bouton **+ Add item** pour en ajouter ;
- **Currency** : choisissez **EUR** (la devise proposée par défaut n'est pas l'euro) ;
- **Tax %** : le taux de TVA, par exemple 20 ;
- **Discount (amount)** : une remise en montant ;
- **Brand color** : la couleur d'accent du document ;
- **Notes** : un champ libre en bas de facture, très utile pour les mentions légales.

Le PDF calcule automatiquement le sous-total, la TVA et le total.

## Créer une facture, étape par étape

1. Ouvrez le [générateur de factures](/invoice-generator/).
2. Remplissez **From** et **Your details**. Mettez une information par ligne : chaque retour à la ligne est repris sur le PDF.
3. Remplacez le numéro proposé par **votre propre numérotation** (voir ci-dessous).
4. Indiquez la date d'émission et la date d'échéance.
5. Remplissez **Bill to** avec la raison sociale et l'adresse du client.
6. Supprimez les deux lignes d'exemple avec la croix, puis ajoutez vos prestations, avec des **prix unitaires hors taxes**.
7. Choisissez **EUR**, saisissez le **taux de TVA**.
8. Ajoutez vos mentions légales dans **Notes**.
9. Cliquez sur **Download invoice PDF**.

## Les mentions obligatoires en France

Une facture entre professionnels doit notamment comporter :

- un **numéro unique**, basé sur une séquence chronologique et continue, sans trou ;
- la **date d'émission** ;
- l'**identité du vendeur** : nom ou raison sociale, adresse, numéro **SIREN ou SIRET**, et numéro de TVA intracommunautaire si vous êtes assujetti ;
- l'**identité du client** et son adresse de facturation ;
- la **désignation précise** des produits ou services, la quantité et le **prix unitaire hors taxes** ;
- le **taux de TVA**, le montant total HT, le montant de la TVA et le total TTC ;
- la **date d'échéance** du paiement ;
- le **taux des pénalités de retard** ;
- la mention de l'**indemnité forfaitaire pour frais de recouvrement de 40 €**, due en cas de retard de paiement entre professionnels.

Avec le générateur, placez le SIRET et le numéro de TVA dans *Your details*, et les conditions de paiement dans *Notes*. Exemple de texte pour le champ Notes :

- Paiement à 30 jours par virement. IBAN : FR76 …
- Pénalités de retard : trois fois le taux d'intérêt légal.
- Indemnité forfaitaire pour frais de recouvrement : 40 €.
- Pas d'escompte pour paiement anticipé.

## Le cas de l'auto-entrepreneur (micro-entrepreneur)

Si vous bénéficiez de la **franchise en base de TVA**, vous ne facturez pas de TVA :

- laissez **Tax %** à 0 ;
- ajoutez dans *Notes* la mention **« TVA non applicable, art. 293 B du CGI »** ;
- indiquez après votre nom la mention **« EI »** ou « Entrepreneur individuel », obligatoire depuis 2022 ;
- n'oubliez pas votre numéro SIRET dans *Your details*.

## Trois pièges à éviter

**La numérotation.** Le générateur propose un numéro aléatoire du type `INV-12345`. Remplacez-le par une séquence continue, par exemple `2026-001`, `2026-002`… Une facture annulée ne se supprime pas : on émet un avoir.

**La remise calculée après la TVA.** Le champ *Discount* est soustrait du total **après** l'application de la TVA. En France, une remise commerciale se déduit normalement du prix HT, avant TVA. Pour que la TVA soit calculée sur le bon montant, n'utilisez pas ce champ : ajoutez plutôt une ligne « Remise commerciale » avec un **prix négatif** (par exemple -50).

**Un seul taux de TVA.** Le générateur applique un taux unique à toute la facture. Si vous vendez des produits à des taux différents (20 % et 10 %, par exemple), il vaut mieux utiliser un logiciel de facturation.

## Ce qu'il faut savoir sur le document produit

Les intitulés du PDF sont en **anglais** (« INVOICE », « Bill to », « Subtotal », « Tax ») et les montants suivent la notation anglo-saxonne (€1,250.00). Pour un client à l'étranger, c'est parfait. Pour un client français, la facture reste compréhensible, mais si une présentation entièrement en français est importante pour vous ou votre client, ajoutez une phrase en français dans *Notes* ou utilisez un outil de facturation francophone.

**Facturation électronique.** La France généralise la facture électronique entre entreprises : toutes les entreprises doivent pouvoir recevoir des factures électroniques depuis septembre 2026, et l'obligation d'en émettre s'étend progressivement aux PME et micro-entreprises d'ici septembre 2027. Une facture électronique au sens de la réforme passe par une plateforme agréée : un simple PDF ne suffira plus pour les factures entre entreprises françaises concernées. Le générateur reste utile pour les clients particuliers, les clients à l'étranger, les devis et les besoins ponctuels ; vérifiez votre calendrier avec votre comptable.

## Compléments utiles

- Pour une petite vente au comptant, le [générateur de reçus](/receipt-generator/) produit un ticket au format étroit.
- Pour faire valider un devis par votre client, il peut le signer avec [Signer un PDF](/sign-pdf/) sans l'imprimer.

## Confidentialité

Les informations saisies (votre IBAN, les coordonnées de vos clients, vos tarifs) restent **dans votre navigateur** : le PDF est généré sur votre appareil, rien n'est envoyé ni stocké sur nos serveurs. Pensez en revanche à conserver vous-même une copie de chaque facture : l'outil ne garde pas d'historique.

## Questions fréquentes

**Peut-on créer une facture gratuitement sans inscription ?**
Oui, sans compte, sans limite et sans filigrane sur le PDF.

**Peut-on ajouter son logo ?**
Non, le générateur n'intègre pas de logo ; vous pouvez en revanche choisir la couleur d'accent du document.

**Le générateur enregistre-t-il mes factures ?**
Non. Téléchargez chaque PDF et archivez-le : les factures doivent être conservées pendant dix ans.

**Quel taux de TVA indiquer ?**
Le taux normal est de 20 % en France, avec des taux réduits pour certains produits et services. Vérifiez le taux applicable à votre activité.
"""),
dict(slug='reduire-taille-image-sans-perte-qualite', lang='fr', title="Réduire la taille d'une image sans perte de qualité visible : passer de plusieurs Mo à quelques centaines de Ko", date='2026-11-17',
 desc="Réduire la taille d'une image gratuitement : compressez vos photos JPG ou PNG en Ko pour un formulaire, un e-mail ou un site, sans perte de qualité visible.",
 tools=['image-compressor', 'image-resizer', 'heic-to-jpg'], md="""
« Le fichier ne doit pas dépasser 500 Ko. » Le message tombe au moment de déposer une photo d'identité sur un formulaire en ligne, un justificatif sur un portail, ou une image sur votre site. Une photo de smartphone pèse souvent entre 2 et 6 Mo : il faut donc **réduire la taille de l'image**, sans qu'elle devienne floue ou pixelisée. Le [compresseur d'images](/image-compressor/) de DoraPDF (interface en anglais) le fait gratuitement, sans inscription, sur plusieurs photos à la fois, et sans les envoyer sur un serveur.

## « Sans perte de qualité » : ce qui est possible

Soyons précis. Pour diviser le poids d'une photo par cinq ou dix, l'outil utilise une compression **avec perte** : il supprime des détails que l'œil ne remarque pratiquement pas. Le résultat n'est pas identique au pixel près, mais à l'écran ou à l'impression courante, la différence est **invisible** avec les réglages modérés.

Deux leviers réduisent le poids d'une image :

1. **La compression** : le niveau de détail conservé dans chaque zone de l'image.
2. **Les dimensions** : le nombre de pixels. Une photo de 4 000 pixels de large affichée dans un cadre de 800 pixels transporte des millions de pixels inutiles.

Combiner les deux donne les meilleurs résultats, et c'est ce que fait l'outil.

## Réduire la taille d'une image en ligne, étape par étape

1. Ouvrez le [compresseur d'images](/image-compressor/).
2. Choisissez la **Strength** (force de compression) :
   - *Light* : compression douce, qualité maximale ;
   - *Balanced* (par défaut) : le meilleur compromis pour la plupart des usages ;
   - *Strong* : poids minimal, pour les limites très strictes.
3. Choisissez le **Resize** (dimensions maximales) : taille d'origine, 2 560, 1 920 (par défaut), 1 280 ou 800 pixels sur le plus grand côté.
4. Déposez une ou plusieurs images.
5. Cliquez sur **Compress**.
6. Chaque image s'affiche avec le pourcentage gagné (par exemple « 84% smaller »). Téléchargez les fichiers, dont le nom se termine par `-small`.

## Quels réglages pour quel usage ?

| Usage | Strength | Resize |
|---|---|---|
| Formulaire administratif limité à 200–500 Ko | Balanced ou Strong | 1 280 |
| Envoi de photos par e-mail | Balanced | 1 920 |
| Images d'un site web ou d'un blog | Balanced | 1 920 ou 1 280 |
| Photos de produits pour une annonce | Light ou Balanced | 1 920 |
| Archivage ou impression | Light | 2 560 ou taille d'origine |

Si le fichier dépasse encore la limite, baissez d'abord les dimensions (de 1 920 à 1 280, puis 800), avant de passer en *Strong*. Une image plus petite mais bien compressée paraît souvent plus nette qu'une grande image écrasée par une compression forte.

## JPG, PNG, WebP : ce qui sort de l'outil

- Les **photos JPG** (et autres images sans transparence) ressortent en **JPG**.
- Les **images PNG** ressortent en **WebP**, un format moderne qui conserve la transparence tout en étant beaucoup plus léger. Tous les navigateurs actuels l'affichent. Si un formulaire refuse le WebP, convertissez le résultat en JPG avec [WebP en JPG](/webp-to-jpg/), ou en PNG si vous avez besoin de garder la transparence.
- Les **photos HEIC** de l'iPhone : convertissez-les d'abord avec [HEIC en JPG](/heic-to-jpg/), puis compressez-les.

## Obtenir des dimensions exactes

Certains formulaires demandent des dimensions précises (par exemple une photo de 600 × 800 pixels) plutôt qu'un poids maximal. Dans ce cas, utilisez le [redimensionneur d'images](/image-resizer/) (interface en anglais) pour fixer la largeur et la hauteur exactes, puis passez le résultat dans le compresseur si le poids est encore trop élevé.

## Pourquoi alléger les images d'un site web

Si vous gérez un site, une boutique en ligne ou un blog, des images trop lourdes ralentissent l'affichage des pages, surtout sur mobile. Les visiteurs attendent, certains repartent, et la vitesse de chargement compte parmi les signaux de qualité pris en compte par les moteurs de recherche. Pour la plupart des sites, une largeur de 1 920 pixels suffit pour une image pleine largeur, et 1 280 ou 800 pixels pour une image dans le texte.

## Problèmes fréquents

**Le fichier compressé est à peine plus léger.** L'image était sans doute déjà compressée (une image téléchargée sur un réseau social, par exemple). Réduisez les dimensions plutôt que la qualité.

**Des petits carrés ou des halos apparaissent.** La compression est trop forte pour cette image. Repartez de l'original avec *Balanced* ou *Light*. Ne recompressez jamais une image déjà compressée : les défauts s'accumulent.

**Le fond transparent est devenu blanc.** Cela arrive si vous convertissez le WebP obtenu en JPG, format qui ne gère pas la transparence. Gardez le WebP ou passez par le PNG.

**Le texte d'une capture d'écran est baveux.** Les captures d'écran avec du texte supportent mal une compression forte. Choisissez *Light* et gardez des dimensions suffisantes pour que le texte reste lisible.

## Confidentialité

Photos de famille, pièces justificatives, photos d'identité : les images sont compressées **dans votre navigateur**. Elles ne sont envoyées sur aucun serveur et ne sont pas conservées. Vous pouvez donc traiter des documents personnels sans inquiétude.

## Questions fréquentes

**Peut-on réduire la taille d'une image gratuitement et sans inscription ?**
Oui, sans compte, sans limite et sans filigrane.

**Peut-on compresser plusieurs photos d'un coup ?**
Oui, déposez-en autant que nécessaire. Chaque image est compressée avec les mêmes réglages et peut être téléchargée séparément.

**Comment passer une photo de Mo en Ko ?**
Avec *Balanced* et une taille maximale de 1 280 pixels, une photo de smartphone de plusieurs Mo descend généralement à quelques centaines de Ko. Le gain exact dépend de l'image : il s'affiche après la compression.

**L'outil fonctionne-t-il sur téléphone ?**
Oui, dans le navigateur. Les images compressées sont enregistrées dans vos téléchargements ou dans l'app Fichiers.
"""),
dict(slug='convert-png-to-svg-free-online-vectorize-logo', title='How to Convert PNG to SVG Free Online: Vectorize a Logo or Icon in Your Browser', date='2026-11-17',
 desc="Convert PNG to SVG for free, without sign-up. Learn which detail setting to pick, what tracing can and can't do, and how to get clean vector logos.",
 tools=['png-to-svg', 'svg-to-png', 'image-background-remover'], md="""
You have a logo as a small PNG, and now someone wants it "in vector": a printer, a sign maker, a web developer who needs it to stay sharp on a 4K screen. The usual answer is to **convert PNG to SVG**, a process called vector tracing. DoraPDF's free [PNG to SVG Converter](/png-to-svg/) does that in your browser, with no account and no upload to a server.

This guide explains what tracing actually does, how to get the cleanest result, and when it is better to ask the designer for the original file instead.

## PNG vs SVG in one minute

A **PNG** is a grid of pixels. Zoom in far enough and you see little squares, and enlarging it just makes the squares bigger.

An **SVG** describes shapes with maths: "draw a curve from here to here, fill it pink." Because the shapes are recalculated at every size, an SVG looks crisp on a business card and on a billboard. SVGs are also tiny for simple graphics and can be edited in Figma, Inkscape or Illustrator, or styled with CSS on a website.

Converting PNG to SVG means a program looks at the pixels, groups areas of similar colour and draws vector outlines around them. It is a smart guess, not a magic recovery of the original artwork.

## How to convert PNG to SVG on DoraPDF

1. Open the [PNG to SVG Converter](/png-to-svg/).
2. Drop your PNG file onto the page (one image at a time).
3. Choose a **Detail** level:
   - **High detail**: uses up to 32 colours and keeps small shapes. Good for illustrations with shading.
   - **Balanced** (default): 16 colours, a sensible middle ground for most icons and graphics.
   - **Simple / logo**: 8 colours with a light blur first, so stray pixels and soft edges are smoothed away. Best for flat logos, stamps and line icons.
4. Click **Vectorize**. A preview of the SVG appears under the button.
5. Download the `.svg` file.

The tracing library runs inside your browser tab, so the image never leaves your device.

## Getting a clean vector: practical tips

**Start with the cleanest PNG you have.** Tracing amplifies problems. A blurry, JPEG-compressed screenshot of a logo will turn into wobbly shapes with extra colour blobs. If there is a larger or sharper version anywhere (an old email signature, a website header, a PDF brochure), use that.

**Remove the background first if it is busy.** A logo on a photo or a textured background will be traced together with the background. Run it through the [background remover](/image-background-remover/) first, then vectorize the result.

**Pick "Simple / logo" for flat designs.** Most company logos use two to five solid colours. The 8-colour setting with its light blur produces fewer, smoother paths, and the file is easier to edit afterwards.

**Use "High detail" only when you need shading.** More colours mean many more paths. The SVG becomes heavier and harder to edit, and gradients still turn into visible colour bands rather than true smooth gradients.

**Expect to tidy up.** For anything that matters, such as a logo going on signage or merchandise, open the SVG in a vector editor, delete stray shapes, merge similar colours and straighten lines. Tracing gets you 80% of the way in seconds; the last 20% is a human job.

## What PNG to SVG conversion can't do

- **It doesn't add detail that isn't there.** The tool works from a copy of your image scaled to about 800 pixels on its longest side. That is plenty for logos and icons, but fine textures and tiny text will be simplified.
- **Text becomes shapes, not editable text.** The letters in your logo will be outlines. If you need to change a word, you will have to retype it with the right font.
- **Photos don't convert well.** A traced photo looks like a posterised illustration. That can be a nice artistic effect, but it won't replace a JPG.
- **Gradients turn into bands.** Smooth gradients are approximated with a few flat colour steps.

If you need a pixel-perfect vector of a professional logo, the best route is still to ask the original designer or agency for the source file (AI, EPS, PDF or SVG).

## Common problems and fixes

**"The SVG has lots of tiny specks."** Switch to *Simple / logo*. The pre-blur and lower colour count remove most noise.

**"The edges look jagged."** The source PNG is probably small or compressed. Find a bigger original, or upscale it first, then trace.

**"White areas became a white box."** The background was traced as a shape. Remove the background before vectorizing, or delete that shape in a vector editor.

**"The file is very large."** You likely used *High detail* on a complex image. Try *Balanced* or *Simple*.

## Going the other way: SVG to PNG

Many platforms (social media, some email tools, document editors) don't accept SVG uploads. When you need a regular image again, the [SVG to PNG Converter](/svg-to-png/) renders your vector at 1x, 2x, 4x or 8x size, so you can create a high-resolution PNG for any use.

## Privacy

Your PNG is processed locally in your browser. Nothing is uploaded to DoraPDF's servers, which matters if the logo belongs to a client or an unreleased project.

## FAQ

**Is this PNG to SVG converter really free?**
Yes. There is no sign-up, no watermark and no daily limit on how many images you can trace.

**Can I convert PNG to SVG on iPhone or Android?**
Yes. The tool runs in mobile browsers such as Safari and Chrome. Pick the image from your photos or files, vectorize, and save the SVG to your Files app.

**Will the SVG work with Cricut or a laser cutter?**
Usually, yes: the output is a standard SVG made of filled paths. For cutting machines, use the *Simple / logo* setting and remove the background first, so you get fewer, cleaner shapes.

**Can I convert JPG or WebP to SVG?**
This page accepts PNG. For WebP there is a separate [WebP to SVG converter](/webp-to-svg/); for JPG, run it through the [JPG to PNG converter](/jpg-to-png/) first.

**Why does my traced logo look slightly different from the original?**
Tracing simplifies colours and curves. For a perfect match, edit the SVG in a vector program or request the original vector file.
"""),
dict(slug='convert-svg-to-png-high-resolution-transparent', title='Convert SVG to PNG in High Resolution (With Transparent Background), Free', date='2026-11-17',
 desc='Turn SVG files into sharp PNG images at 1x, 2x, 4x or 8x size. Free, no sign-up, transparent background kept, and several files at once.',
 tools=['svg-to-png', 'png-to-svg', 'image-resizer'], md="""
SVG is the perfect format for logos and icons, right up until you try to upload one. Instagram, many email builders, Word, Google Slides and plenty of online forms simply refuse SVG files. The fix is to **convert SVG to PNG**: a normal image that every app accepts, while keeping a transparent background.

DoraPDF's [SVG to PNG Converter](/svg-to-png/) does this in your browser, lets you choose a high-resolution scale, and handles several files in one go.

## Why size matters when you export

An SVG has no fixed resolution, but a PNG does. When you convert, you decide how many pixels the PNG gets. Export too small and your logo looks soft on a retina screen or in print; export at a sensible multiple and it stays crisp.

The converter reads the width and height written inside your SVG and multiplies them by the scale you choose:

| Scale | SVG size 200 × 80 becomes | Good for |
|---|---|---|
| 1x | 200 × 80 px | Exact size on a standard screen |
| 2x (default) | 400 × 160 px | Websites and apps on high-density screens |
| 4x | 800 × 320 px | Presentations, documents, social posts |
| 8x | 1600 × 640 px | Print, large banners, merchandise mock-ups |

If an SVG has no size information at all, the tool assumes 512 pixels as the base before applying the scale.

## Step by step: SVG to PNG on DoraPDF

1. Open the [SVG to PNG Converter](/svg-to-png/).
2. Drag in one SVG file, or several at once.
3. Pick the **Scale**: 1x, 2x, 4x or 8x.
4. Run the conversion and download your PNG files. Each one keeps the original file name, with `.png` at the end.

Transparent areas in the SVG stay transparent in the PNG, so a logo will sit cleanly on any coloured slide or photo.

## Which scale should you choose?

- **Website header or app icon:** 2x is usually right. It looks sharp on phones and modern laptops without making the file heavy.
- **PowerPoint, Google Slides or Word:** 4x. Slides get projected on big screens, and documents get zoomed.
- **Printing:** think in DPI. A logo printed 5 cm wide at 300 DPI needs roughly 590 pixels across. Check your SVG's base width and pick the scale that gets you there; 8x is the safe choice for small source sizes.
- **Social media profile pictures:** most platforms crop to a square, so you may want to place the PNG on a square canvas afterwards, or resize it with the [image resizer](/image-resizer/).

## Common problems (and how to fix them)

**The fonts look wrong.**
If your SVG uses text with a web font that isn't embedded in the file, the browser substitutes a default font while rendering. In your design tool, convert text to outlines (sometimes called "create outlines" or "flatten text") before exporting the SVG, then convert again.

**Part of the image is missing.**
Browsers don't load external images or files linked from inside an SVG when it is rendered as a picture, for security reasons. Embed images in the SVG, or flatten the design before exporting.

**The PNG is tiny.**
Your SVG may declare a very small width and height (for example 24 × 24 for an icon). Use 8x, or open the SVG in a text editor and raise the `width` and `height` values while keeping the `viewBox` unchanged.

**The PNG has a white box instead of transparency.**
The white is part of the SVG itself, usually a background rectangle. Delete that shape in your vector editor and convert again.

**The file won't open.**
Make sure it is a real `.svg` file, not an HTML page saved with an SVG extension or an SVGZ (compressed) file.

## Tips for designers and developers

- Keep a master SVG and generate PNGs on demand. It's quicker than maintaining a folder of fixed-size exports that go out of date.
- For favicons and app icons, export at 8x from a simple square SVG, then resize down to exact sizes. Downscaling a big render looks better than upscaling a small one.
- Need the reverse? If you only have a PNG logo and want a vector, try the [PNG to SVG converter](/png-to-svg/), which traces the image into editable shapes.

## Privacy

Your SVG files are rendered by your own browser. They are not uploaded to DoraPDF's servers, so client logos and unreleased designs stay on your device.

## FAQ

**How do I convert SVG to PNG without losing quality?**
Choose a scale high enough for where the image will be used: 2x for screens, 4x for slides, 8x for print. Because the vector is redrawn at the new size, there's no blur from enlarging.

**Does the converter keep the transparent background?**
Yes. Any area without fill in your SVG stays transparent in the PNG.

**Can I convert several SVG files at once?**
Yes. Select or drop multiple files and they're all converted with the same scale.

**Can I convert SVG to PNG on my phone?**
Yes. It works in mobile browsers; choose the SVG from your Files app and save the PNG back to your device.

**Is there a file limit or watermark?**
No sign-up, no watermark. Very large or complex SVGs may take a little longer because your device does the work.
"""),
dict(slug='add-gps-location-date-time-stamp-to-photo-online', title='Add GPS Location, Date and Time Stamp to a Photo Online (No App Needed)', date='2026-11-17',
 desc='Stamp address, latitude/longitude and date-time onto photos you already took. Free, in your browser, reads GPS from the photo when available.',
 tools=['gps-photo-stamper', 'image-compressor', 'images-to-pdf'], md="""
GPS camera apps are great if you remembered to use them when you took the picture. Most of us didn't. The photo is already in the gallery, and now a report, a client or a site log asks for the location and time printed on it.

DoraPDF's [GPS Photo Stamper](/gps-photo-stamper/) lets you **add a location and timestamp to a photo you already have**, straight from the browser, without installing an app. It even tries to read the GPS coordinates and the original capture time stored inside the photo.

## Who uses a location stamp?

- **Site engineers and contractors** documenting progress at a construction site.
- **Field staff and surveyors** sending visit photos with their daily report.
- **Delivery and installation teams** recording where and when a job was completed.
- **Property agents and landlords** dating move-in and move-out photos.
- **Travellers** who want a neat caption with place and date on holiday shots.

## How to stamp location and time on a photo

1. Open the [GPS Photo Stamper](/gps-photo-stamper/).
2. Drop in your photo (JPG, PNG, HEIC support depends on your browser).
3. Check the fields the tool fills in for you:
   - **Latitude** and **Longitude**: read from the photo's EXIF data if your phone saved location with it.
   - **Date & time**: taken from the photo's original capture time if available, otherwise from the file's date.
4. Type a **Place**, for example "Plot 14, DHA Phase 6, Lahore" or "Hotel entrance, Rome". It's optional, but it makes the stamp readable for people who don't think in coordinates.
5. Watch the preview update as you type. The stamp appears as a dark, semi-transparent bar along the bottom of the photo, with white text on three lines: place, coordinates and the full date and time.
6. Click **Download stamped photo**. You get a JPG named after your original, ending in `-stamped.jpg`.

## Where do the coordinates come from?

Most phones can save GPS information inside each photo, but only when location access is enabled for the camera. If your photo has it, the tool fills it in automatically.

If the fields stay empty, the photo has no location data. Common reasons:

- Location was turned off for the camera app.
- The image was sent through a messaging app or social network that strips metadata.
- It's a screenshot or an edited export.

In that case you can enter the coordinates yourself. Open your maps app, long-press the exact spot, and copy the latitude and longitude (they look like `31.520370, 74.358749`). The stamper displays them with six decimal places.

## Tips for a clear, useful stamp

- **Keep the place name short.** One line reads best: building or plot, area, city.
- **Use the original photo, not a WhatsApp copy.** Originals keep the date and GPS data and have more resolution. The stamper keeps up to 2400 pixels on the longest side, which is sharp enough for reports.
- **Check the time zone.** The tool shows the time as stored in the photo or as you enter it. If you've travelled, make sure it reflects local time where the photo was taken.
- **Put important subjects away from the bottom edge.** The stamp bar covers roughly the lowest sixth of the image.
- **Building a report?** Stamp each photo, then combine them into one document with the [Images to PDF](/images-to-pdf/) tool. If an email limit is tight, shrink the photos first with the [image compressor](/image-compressor/).

## Be honest with your stamps

A stamp is a caption you control: you can type any place and time. That makes it useful for labelling real photos, but it also means a typed stamp isn't tamper-proof evidence. Only stamp the actual location and time where the photo was taken. If an employer, insurer or court needs verifiable proof, ask what they require; some insist on photos taken directly with a dedicated camera app or on the original files with their metadata intact.

## Common questions about problems

**The date shown is today, not the day I took the photo.**
The original capture date was missing (often because the file was forwarded through a chat app), so the tool used the file's own date. Simply correct it in the Date & time field.

**The text looks small on a vertical photo.**
The stamp scales with the image height. On very tall, narrow photos, try cropping a little before stamping.

**Does the stamped photo still contain the GPS metadata?**
No. The download is a fresh JPG with the information drawn on the picture. The hidden EXIF data, including GPS, isn't copied over, which is useful if you want to share the visible stamp without the embedded metadata.

## Privacy

Your photo and its location data are read and stamped entirely in your browser. Nothing is uploaded to DoraPDF. That matters, because GPS coordinates can reveal a home address.

## FAQ

**Can I add a GPS stamp to an old photo?**
Yes. That's exactly what the tool is for. If the photo has location data, it's filled in automatically; if not, type the coordinates and place yourself.

**Does it work on iPhone and Android?**
Yes. Open the page in Safari or Chrome, choose the photo from your gallery, and save the stamped JPG back to your phone.

**Can I stamp only the date and time without location?**
Yes. Leave Place, Latitude and Longitude empty and only the date line is printed.

**Is it free?**
Yes, with no sign-up and no watermark.
"""),
dict(slug='css-gradient-box-shadow-glassmorphism-generators', title='Free CSS Generators: Gradients, Box Shadows, Mesh Gradients and Glassmorphism', date='2026-11-17',
 desc='Design CSS gradients, box-shadows, mesh gradient backgrounds and frosted-glass cards visually, then copy clean code. Free, no sign-up.',
 tools=['css-gradient-generator', 'box-shadow-generator', 'mesh-gradient-generator', 'glassmorphism-generator'], md="""
Typing `box-shadow: 0 20px 60px rgba(...)` and refreshing the page twenty times is a slow way to design. Visual CSS generators let you drag a slider, see the result immediately, and copy code that's ready to paste. DoraPDF has four of them, all free and running in your browser:

- [CSS Gradient Generator](/css-gradient-generator/): linear, radial and conic gradients
- [Box Shadow Generator](/box-shadow-generator/): soft, hard, inset and coloured shadows
- [Mesh Gradient Generator](/mesh-gradient-generator/): blurry, multi-colour backgrounds
- [Glassmorphism CSS Generator](/glassmorphism-generator/): frosted-glass cards

Here's what each one does, which settings matter, and a few design habits that keep the results from looking dated.

## 1. CSS Gradient Generator

### What you can control

- **Two or three colours.** Tick "3 colors" to add a third stop.
- **Type:** *Linear* (a straight blend), *Radial* (a circle spreading from the centre) or *Conic* (colours sweeping around a point like a colour wheel).
- **Angle** from 0 to 360 degrees, used by linear and conic gradients.

The output is a single line such as:

```css
background: linear-gradient(135deg, #ff2e88, #9b3cff);
```

Click copy and paste it into your stylesheet, a Tailwind arbitrary value, or a Webflow or WordPress custom CSS field.

### Tips for nicer gradients

- **Stay close on the colour wheel.** Pink to purple or blue to teal blends smoothly. Opposite colours (red to green) tend to pass through a muddy grey in the middle.
- **Use the angle to lead the eye.** 135° (top-left to bottom-right) feels natural for hero sections because we read in that direction.
- **Check text contrast.** White text on the lightest part of the gradient must still be readable.
- **Conic for charts and badges.** Conic gradients are handy for pie-like progress rings and spinning loaders.

## 2. Box Shadow Generator

### The sliders

- **Horizontal** and **Vertical** offset (−100 to 100 px): where the shadow falls.
- **Blur** (0 to 150 px): how soft the edge is.
- **Spread** (−50 to 50 px): grows or shrinks the shadow before blurring.
- **Color** and **Opacity**, combined into an `rgba()` value.
- **Inset**: puts the shadow inside the element, for pressed buttons or input fields.

### Shadow recipes that work

- **Soft card shadow:** small vertical offset, large blur, low opacity (around 10 to 20%). Feels modern and light.
- **Floating element:** larger vertical offset (20 to 30 px), big blur, slightly negative spread so the shadow is narrower than the card.
- **Coloured glow:** zero offsets, large blur, the same colour as the button at 40 to 50% opacity. Great for call-to-action buttons on dark themes.
- **Pressed state:** turn on Inset with a small blur.

A common mistake is pure black shadows at high opacity. Real shadows are soft and slightly tinted, so try a dark version of your background colour instead of `#000`.

## 3. Mesh Gradient Generator

Mesh gradients are the soft, colourful "blob" backgrounds you see on landing pages and app splash screens. This generator builds them from several overlapping radial gradients, so they're pure CSS, with no image file needed.

### How it works

1. Click **Generate**. The tool picks one of its colour palettes and places four colour spots at random positions and sizes.
2. Keep clicking until you like the composition. Each click is a new arrangement.
3. **Copy the CSS** (a `background-color` plus a stacked `background-image` of radial gradients), or click **Download PNG** for a 1600 × 1000 image to use in slides, social posts or as a wallpaper.

### Where mesh gradients shine

- Hero sections behind a headline
- Blog and YouTube thumbnails
- Backgrounds for glassmorphism cards (see below)

Keep text on top short and bold; busy colour behind long paragraphs is tiring to read.

## 4. Glassmorphism CSS Generator

Glassmorphism is the frosted-glass look: a semi-transparent card that blurs whatever is behind it. The generator shows your card over a colourful background so you can judge the effect properly.

### Controls

- **Blur** (0 to 40 px): the strength of the frosted effect, via `backdrop-filter`.
- **Transparency** (0 to 60%): how much of the tint colour fills the card.
- **Border** (0 to 60%): opacity of a thin 1 px border that catches the light.
- **Tint**: usually white, but a coloured tint can match your brand.

The code includes both `backdrop-filter` and `-webkit-backdrop-filter`, so the effect also works in Safari, plus a 24 px border radius.

### Making glass look good

- **It needs something behind it.** On a flat, single-colour background, glass looks like a grey box. Pair it with a mesh gradient, a photo or shapes.
- **Keep transparency low** (10 to 20%) and blur moderate (10 to 20 px) for readability.
- **Add the border.** That faint edge is what sells the "glass" illusion.
- **Test performance on phones.** Many large blurred layers can make scrolling sluggish on older devices. Use glass for a few key elements, not every card.

## A quick workflow that combines all four

1. Generate a **mesh gradient** for the page background.
2. Place a **glass card** on top for your signup form or pricing box.
3. Give the main button a **linear gradient** in your brand colours.
4. Add a soft coloured **box-shadow** under the button so it lifts off the glass.

## Privacy

All four generators run entirely in your browser. Nothing is sent to a server, and there's no sign-up.

## FAQ

**Can I use the generated CSS in commercial projects?**
Yes. The code is standard CSS that you create with the tool; use it anywhere.

**Does glassmorphism work in all browsers?**
`backdrop-filter` is supported in current versions of Chrome, Edge, Safari and Firefox. Older browsers will show the semi-transparent tint without the blur, so keep text readable either way.

**How do I use these gradients in Tailwind CSS?**
Paste the value into an arbitrary property, for example `bg-[linear-gradient(135deg,#ff2e88,#9b3cff)]`, or add it to your theme as a custom background image.

**Can I get a mesh gradient as an image instead of CSS?**
Yes. Use the Download PNG button in the Mesh Gradient Generator.
"""),
dict(slug='get-hex-color-code-from-image-online', title='How to Get a HEX Color Code From an Image (Free Online Color Picker)', date='2026-11-17',
 desc="Click any pixel in a photo, logo or screenshot to get its HEX, RGB and HSL code. Plus an instant palette of the image's main colours. Free, private.",
 tools=['image-color-picker', 'css-gradient-generator', 'png-to-svg'], md="""
A client sends a screenshot of their website and says "use our brand pink." A friend wants party invitations that match the flowers in a photo. You love the exact blue in a sunset picture. In each case you need one thing: the **colour code from an image**.

DoraPDF's [Image Color Picker](/image-color-picker/) works like an eyedropper in your browser. Upload a picture, click any pixel, and get its HEX, RGB and HSL values, with the HEX code copied to your clipboard automatically.

## HEX, RGB and HSL: which one do you need?

All three describe the same colour in different notations:

- **HEX** (`#FF2E88`): the most common format. Used in CSS, Canva, Figma, WordPress themes, Shopify and most design apps.
- **RGB** (`rgb(255, 46, 136)`): red, green and blue values from 0 to 255. Used in CSS, Photoshop, Office apps and code.
- **HSL** (`hsl(334, 100%, 59%)`): hue, saturation and lightness. Handy when you want a lighter or darker version of a colour: keep the hue and change only the lightness.

If an app asks for a "color code" without saying which, HEX is almost always what it wants.

## How to pick a colour from an image

1. Open the [Image Color Picker](/image-color-picker/).
2. Drop in a photo, logo, screenshot or scanned design.
3. Your cursor turns into a crosshair over the image. Click the exact spot you want.
4. The result panel shows the **HEX**, **RGB** and **HSL** values, tinted with the colour you picked. The HEX code is already copied, so you can paste it straight into your design tool.
5. Click another spot to compare. Each click updates the values and copies the new code.

## The automatic palette

Below the image, the tool also shows up to **eight swatches** of the colours that cover the most area in the picture. Click any swatch to copy its HEX code.

The palette is great for quick inspiration: drop in a landscape photo and you instantly get a set of colours that already look good together. Keep in mind that the swatches are grouped, representative shades, so they can differ slightly from any single pixel. When you need an exact brand colour, click directly on the image.

## Getting accurate colour codes

**Click the middle of a flat area.** Edges are blended with neighbouring colours (anti-aliasing), so a pixel on the border of a logo can be a mix of logo and background.

**Avoid compressed screenshots.** JPEG compression adds faint noise, especially around text. A PNG screenshot gives cleaner, more consistent values. If you get slightly different codes from nearby pixels, that's compression at work; pick the value that appears most often.

**Shadows and lighting change colour.** In a photo of a painted wall or a product, the "same" colour will be lighter in highlights and darker in shadow. Sample a few spots in even light and choose the one that looks right.

**Brand colours deserve a source check.** If the colour is for official use, ask for the brand guidelines too. A colour picked from a screenshot depends on the screen and export it went through.

## Practical ways to use picked colours

- **Match a brand on a budget.** Pick the main colour from a company logo, then use it in slides, invoices or social posts.
- **Build a website palette from a photo.** Use the palette swatches for backgrounds and accents, then design a matching gradient in the [CSS Gradient Generator](/css-gradient-generator/).
- **Recreate a logo as a vector.** Note the exact HEX codes before tracing an old logo with the [PNG to SVG converter](/png-to-svg/), then correct the colours in the SVG so they match the original exactly.
- **Craft and print projects.** Find the thread, paint or paper colour closest to a reference photo by comparing RGB values.
- **Accessibility checks.** Grab the text and background colours from a design, then run them through a contrast checker to see whether they meet readability guidelines.

## Making a lighter or darker shade

Once you have the HSL value, adjust the last number (lightness):

- `hsl(334, 100%, 59%)` is the original pink.
- `hsl(334, 100%, 75%)` is a soft pastel version for backgrounds.
- `hsl(334, 100%, 40%)` is a deeper shade for hover states or text.

The hue stays the same, so the shades feel like one family.

## Troubleshooting

**Nothing happens when I click.** Make sure the image has finished loading and you're clicking on the picture itself, not the margin.

**The copied code doesn't paste.** Some browsers ask for clipboard permission the first time. You can always select the HEX value from the result panel and copy it manually.

**The colour looks different in my design app.** Check that both apps use the same colour profile (usually sRGB). Print colours (CMYK) can also differ from screen colours.

## Privacy

Your image is opened and read only inside your browser. It's never uploaded to DoraPDF, so unpublished designs and client screenshots stay private.

## FAQ

**How do I find the HEX code of a colour in a picture?**
Upload the picture to the Image Color Picker and click the colour. The HEX code is shown and copied instantly.

**Can I use it on my phone?**
Yes. Open the tool in your mobile browser, choose an image from your gallery and tap the spot you want.

**Does it work with screenshots of websites?**
Yes. Take a screenshot, upload it and click any element. PNG screenshots give the most accurate values.

**Is it free?**
Yes, completely free, with no sign-up and no limit on how many images you check.
"""),
dict(slug='add-open-to-work-frame-linkedin-profile-picture', title='Add an #OpenToWork Style Frame to Your Profile Picture (Custom Text and Colour)', date='2026-11-17',
 desc='Make a circular profile photo frame with your own text, like #OPENTOWORK, #HIRING or #FREELANCE, in any colour. Free, private, download as PNG.',
 tools=['linkedin-photo-frame', 'image-background-remover', 'resume-builder'], md="""
The coloured ring around a profile picture is one of the quickest signals on LinkedIn: at a glance, people know you're looking for a job, hiring, or available for freelance work. LinkedIn has its own built-in "Open to work" option, but it only offers fixed wording and colours, and it only exists on LinkedIn.

With DoraPDF's [LinkedIn Photo Frame Editor](/linkedin-photo-frame/) you can **add an Open to Work style frame to your profile picture** with your own words and brand colour, then use the image on LinkedIn, WhatsApp, Slack, X, Teams or anywhere else that shows round avatars.

## What the frame editor makes

- Your photo cropped into a **circle** (800 × 800 pixels).
- A thick **coloured arc** along the lower-left edge, in any colour you choose.
- Your **banner text** written in white capital letters, curving along the arc.
- A **PNG download** with transparent corners, ready to upload.

The tool is independent and isn't affiliated with LinkedIn; it simply creates an image you can use as your profile picture.

## Step by step

1. Open the [LinkedIn Photo Frame Editor](/linkedin-photo-frame/).
2. Upload your profile photo.
3. Edit the **Banner text**. It starts as `#OPENTOWORK`; change it to anything you like. Letters are converted to capitals automatically.
4. Pick a **Color** for the ring.
5. Check the live preview, then click **Download PNG**. The file is saved as `profile-frame.png`.
6. Upload it as your new profile photo on LinkedIn or any other platform.

## Text ideas that work

Short text reads best because it has to fit along a quarter of the circle. Roughly 12 to 16 characters looks clean; longer text gets crowded.

- **Job seekers:** `#OPENTOWORK`, `#OPENTOINTERNSHIP`, `AVAILABLE NOW`
- **Recruiters and founders:** `#HIRING`, `WE'RE HIRING`, `JOIN OUR TEAM`
- **Freelancers:** `#FREELANCE`, `OPEN FOR PROJECTS`, `BOOK A CALL`
- **Students and graduates:** `#CLASSOF2026`, `#GRADUATE`
- **Events and causes:** a conference hashtag, `SPEAKER`, `VOLUNTEER`

## Choosing a colour

- **Green** is the colour most people already associate with "open to work."
- **Purple** is widely associated with "hiring" frames.
- **Your brand colour** makes sense for company campaigns or event hashtags. If you don't know the exact code, use the [Image Color Picker](/image-color-picker/) on your company logo to get it.

Make sure white text stands out on the colour you choose. Very light colours like pale yellow or light grey make the letters hard to read.

## Getting the photo right

The editor fills the circle with your photo and centres it automatically, so the framing of the original matters:

- **Use a roughly square photo with your face in the centre.** If your face is off to one side in a wide photo, crop it to a square first.
- **Leave space around your head.** The ring covers the lower-left part of the circle, so keep your face slightly up and to the right, and avoid having your chin right at the bottom edge.
- **Use a clean background.** A busy background competes with the ring. You can replace it with a solid colour using the [background remover](/image-background-remover/).
- **Start with a sharp image.** The output is 800 × 800 pixels, which looks crisp on profile pages; a blurry source stays blurry.

## Should you use an "Open to Work" frame?

That's a personal choice, and opinions differ. Some recruiters like the clear signal; others feel a public frame can look less selective. Many people use the frame while actively searching and remove it once they're in interview rounds. If you'd rather be discreet, LinkedIn also lets you signal openness to recruiters only, without a visible frame.

Whatever you decide, the frame works best together with a profile that backs it up: a clear headline, a recent summary and an up-to-date CV. If yours needs a refresh, the free [resume builder](/resume-builder/) creates a clean PDF CV in minutes.

## Troubleshooting

**The text overlaps or looks squeezed.** It's too long for the arc. Shorten it or drop the hashtag.

**My head is cut off.** The photo was too tall or too wide. Crop it to a square around your face and upload again.

**The download has transparent corners.** That's intended: the outside of the circle is empty, so the picture looks clean wherever it's displayed. Platforms that show square avatars will fill the corners with their own background.

## Privacy

Your photo is processed in your browser and never uploaded to DoraPDF. Only the PNG you download leaves the page.

## FAQ

**Can I write my own text instead of #OPENTOWORK?**
Yes. Type any text in the Banner text field; it's shown in capitals along the ring.

**Does it work on a phone?**
Yes. Choose a photo from your gallery, adjust the text and colour, and save the PNG to your phone before uploading it to the LinkedIn app.

**Can I use the framed photo on WhatsApp or Slack?**
Yes. It's a normal PNG image, so any platform that accepts profile pictures will take it.

**Is it free?**
Yes, with no account and no watermark.
"""),
dict(slug='free-barcode-generator-ean-13-upc-code-128', title='Free Barcode Generator: Make EAN-13, UPC-A, Code 128 and ITF-14 Barcodes', date='2026-11-17',
 desc='Create CODE128, EAN-13, UPC-A, CODE39 and ITF-14 barcodes online and download them as PNG. Learn which barcode type to use and how to print it well.',
 tools=['barcode-generator', 'qr-code-generator', 'receipt-generator'], md="""
Whether you're labelling stock on a shelf, numbering assets in an office, or preparing packaging for a small product, you'll eventually need a barcode. DoraPDF's [Barcode Generator](/barcode-generator/) creates the most common types online, for free, and lets you download each one as a PNG image.

The tricky part isn't generating a barcode. It's choosing the right type and using the right number. This guide covers both.

## The barcode types you can create

| Format | What it encodes | Typical use |
|---|---|---|
| **CODE128** | Any text: letters, numbers, symbols | Internal stock labels, shipping and asset tags |
| **EAN-13** | 12 or 13 digits | Retail products in most of the world |
| **UPC-A** | 11 or 12 digits | Retail products in the US and Canada |
| **CODE39** | Capital letters, digits and a few symbols | Older warehouse, industry and ID systems |
| **ITF-14** | 14 digits | Outer cartons and cases of products |

If you enter 12 digits for EAN-13 or 11 for UPC-A, the generator calculates and adds the final check digit for you. If you enter the full number, the check digit must be correct or the tool shows an "Invalid value" warning.

## How to make a barcode

1. Open the [Barcode Generator](/barcode-generator/).
2. Type your **Value**: a product number, SKU, asset tag or any code.
3. Choose the **Format** from the list.
4. The barcode is drawn instantly on a white background, with the human-readable number printed underneath.
5. Click **Download PNG** to save it as `barcode.png`.

Repeat for each code. Because nothing has to upload, generating dozens of labels one after another is quick.

## Which barcode type should you use?

### For your own inventory: CODE128

If the barcode will only be scanned inside your own business, CODE128 is usually the best pick. It accepts any text (for example `SHOP-A-0042` or `LAPTOP-HR-07`), it's compact, and virtually every modern scanner reads it. Most point-of-sale and inventory apps let you assign your own codes to products.

### For products sold in shops: EAN-13 or UPC-A, with a real number

Here's the important part: **generating an EAN or UPC barcode image is easy; getting a valid number is not something a generator can do.** Retailers and marketplaces expect product numbers that are registered to your company, usually through GS1, the organisation that manages these codes worldwide. A made-up 13-digit number will scan, but it may clash with another company's product and can be rejected by stores and online marketplaces.

So the right order is: obtain your official numbers first, then use the generator to turn them into barcode images for your packaging.

### For cartons: ITF-14

Outer boxes that hold several units often carry an ITF-14 code. It's designed to print well even on corrugated cardboard.

### For legacy systems: CODE39

Choose CODE39 only if an existing system or customer specifically asks for it. It's wider than CODE128 for the same content.

## Printing tips so barcodes actually scan

- **Keep the white space.** The blank margin on each side (the "quiet zone") is part of the barcode. Don't crop it off or place the code against a border.
- **Don't squash it.** You can scale the image up or down, but keep the proportions. Stretching only the width or height can make it unreadable.
- **Dark bars on a light background.** Black on white is safest. Red bars, or barcodes on dark or shiny backgrounds, often fail with laser scanners.
- **Print at a decent resolution.** Use a laser printer or a label printer if possible; smudged inkjet prints on plain paper can blur thin bars.
- **Test before printing hundreds.** Scan your first label with a phone barcode app or your shop's scanner.

## Barcode or QR code?

Barcodes hold a short code that points to a record in your system, and they're what most checkout scanners expect. A QR code holds much more (a full web address, Wi-Fi details or contact card) and is read by phone cameras. If you want customers to scan with their phones to open a menu or a website, make a QR code with the [QR Code Generator](/qr-code-generator/) instead.

## Putting barcodes to work in a small business

- Label shelves and bins with CODE128 SKUs so stock counts are faster.
- Tag laptops, chairs and equipment with asset numbers.
- Add an order or receipt number as a barcode on paperwork. When you issue sales slips, the [Receipt Generator](/receipt-generator/) creates simple PDF receipts with your own numbering.

## Privacy

Barcodes are generated in your browser. Your product numbers and codes are not sent to a server.

## FAQ

**Is this barcode generator free for commercial use?**
Yes. The barcode images you create are yours to use on labels and packaging. Remember that retail EAN/UPC numbers themselves should be officially registered.

**Why do I see "Invalid value"?**
The value doesn't fit the format: for example letters in an EAN-13, the wrong number of digits, or a wrong check digit. Check the length or switch to CODE128.

**Can I make an EAN-13 barcode for Amazon or a supermarket?**
You can make the image here, but use a number registered to your brand. Marketplaces and retailers check product codes.

**What size should I print a barcode?**
Keep the proportions of the downloaded PNG and avoid shrinking it too much. Test-scan a printed sample at your intended size before printing a batch.
"""),
dict(slug='free-receipt-generator-pdf-small-business', title='Free Receipt Generator: Create a Simple PDF Receipt for Your Sales', date='2026-11-17',
 desc='Make clean PDF receipts for your shop, freelance work or home business: items, tax, discount, PKR/USD/EUR/GBP/AED. Free, no sign-up, private.',
 tools=['receipt-generator', 'invoice-generator', 'barcode-generator'], md="""
A customer has paid, and now they ask for a receipt. If you run a small shop, sell from home, tutor students or take freelance jobs, you may not have a point-of-sale system that prints one. Handwritten cash memos work, but they look informal and are easy to lose.

DoraPDF's [Receipt Generator](/receipt-generator/) lets you **create a receipt online and download it as a PDF** in about a minute. You can send it on WhatsApp or by email, or print it. There's no account, and your sales data stays on your device.

## Receipt or invoice: which do you need?

They look similar, but they do different jobs:

- An **invoice** asks for payment. It's sent before the customer pays and usually has a due date.
- A **receipt** confirms payment has already been received.

If you're billing a client who will pay later, use the [Invoice Generator](/invoice-generator/) instead. Once they've paid, issue a receipt.

## What goes on the receipt

The generator includes everything a simple sales receipt needs:

- **Your business name** at the top, with "RECEIPT" printed in your brand colour
- **Your details**: address, phone, email (one per line)
- **Receipt number**, pre-filled as `R-` plus a number, which you can change to your own series
- **Date**, defaulting to today
- **Customer** name (optional)
- **Line items** with description, quantity, price and line total
- **Subtotal**, optional **tax %**, optional **discount**, and the **total**
- A short **note**, such as a thank-you message or return policy

The PDF uses a narrow, receipt-like page shape rather than a full A4 sheet, so it looks like a till slip on screen and on paper.

## How to make a receipt, step by step

1. Open the [Receipt Generator](/receipt-generator/).
2. Enter your **business name** in the From field and your contact details below it.
3. Check the **Receipt #** and **Date**.
4. Add the **customer's name** if you want it on the slip.
5. Replace the sample items with what you actually sold. For each line enter the item, quantity and unit price. Use **+ Add item** for more lines and the ✕ button to remove one.
6. Choose the **Currency**: PKR, USD, EUR, GBP or AED.
7. Enter **Tax %** if you charge sales tax or VAT, and a **Discount** as a fixed amount if you gave one.
8. Pick a **Brand color** and write a short **note**.
9. Click **Download receipt PDF**. The file is named after the receipt number, for example `R-48213.pdf`.

## How the total is calculated

The generator adds up all line totals (quantity × price) to get the subtotal. Tax is calculated as a percentage of that subtotal, then the discount amount is subtracted:

**Total = Subtotal + Tax − Discount**

Example: 3 notebooks at Rs 250 and 1 pen set at Rs 600 give a subtotal of Rs 1,350. With no tax and a Rs 100 discount, the total is Rs 1,250.

If your tax rules require tax to be calculated after a discount, reduce the item prices instead of using the discount field, so the tax is applied to the reduced amount.

## Tips for professional-looking receipts

- **Use a consistent numbering system.** For example `R-2026-001`, `R-2026-002`. It makes records and returns much easier to track.
- **Write clear item names.** "Math tuition, November (8 sessions)" is better than "Tuition".
- **Add your policy in the notes.** "Exchange within 7 days with receipt" prevents arguments later.
- **Keep a copy.** Save every PDF in a folder by month. It's a simple sales record for your own accounts.
- **Match your brand.** Use the same colour as your logo or shop sign. You can find the exact code with the [Image Color Picker](/image-color-picker/).
- **Barcode-numbered receipts.** If you scan paperwork, you can make a barcode of the receipt number with the [Barcode Generator](/barcode-generator/).

## Use receipts honestly

This tool is meant for recording **your own real sales**. A receipt is a financial record: only issue one for a payment you actually received, with the true amount and date. Never create receipts for purchases that didn't happen or change amounts on someone else's receipt; that's fraud, for example in expense claims. If you need an official tax invoice under your country's rules (with a registration number or a specific format), check with your accountant or tax authority, as a simple receipt may not be enough.

## Common questions about problems

**Sample items still appear on my receipt.** Delete them with the ✕ button or overwrite them before downloading.

**My currency isn't listed.** The tool currently offers PKR, USD, EUR, GBP and AED. For other currencies, choose the closest option and mention the currency in the notes.

**Long item names wrap onto several lines.** That's normal on the narrow receipt layout. Shorten descriptions if you want a compact slip.

## Privacy

Everything is generated inside your browser. Your customers' names, prices and your business details are not uploaded to DoraPDF.

## FAQ

**Is the receipt generator free?**
Yes. No sign-up, no watermark, and no limit on the number of receipts.

**Can I make a receipt on my phone?**
Yes. Fill in the form in your mobile browser and download the PDF, then share it on WhatsApp or email.

**Can I add my logo?**
Not currently. The receipt shows your business name and brand colour at the top.

**Can I print the receipt?**
Yes. Open the PDF and print it on any printer. The page is narrower than A4, so check your print settings (actual size or fit to page) before printing.
"""),
dict(slug='free-email-signature-generator-gmail-outlook', title='Free Email Signature Generator: Make One and Add It to Gmail or Outlook', date='2026-11-17',
 desc='Create a clean, professional email signature in a minute, copy it with formatting, and add it to Gmail, Outlook or Apple Mail. Free, no sign-up.',
 tools=['email-signature', 'image-color-picker', 'qr-code-generator'], md="""
Your email signature is the business card you hand out dozens of times a day. Plenty of people still sign off with just their first name, or with a pasted block of grey text that loses its formatting on the way.

DoraPDF's [Email Signature Generator](/email-signature/) creates a tidy, two-column signature with your name, role, company and contact details in your brand colour. You copy it with one click and paste it into Gmail, Outlook or Apple Mail. Below you'll find the exact steps for each, plus tips for a signature that looks right on phones too.

## What your signature will look like

The generator builds a compact layout that works in nearly every email app:

- **Left side:** your name in bold, with your job title and company underneath in your chosen colour, finished by a vertical accent line.
- **Right side:** phone, email and website, each on its own line with a small icon.

It's built as a simple HTML table with inline styles, the most reliable way to keep formatting intact across email apps.

## Create your signature

1. Open the [Email Signature Generator](/email-signature/).
2. Fill in **Name**, **Title** and **Company**.
3. Add **Phone**, **Email** and **Website**.
4. Pick a **Color**. If you want your exact brand colour, grab its code from your logo with the [Image Color Picker](/image-color-picker/).
5. Check the live preview.
6. Click **Copy signature**. This copies the formatted version, ready to paste.

Important: fill in **every field**. Empty fields show the grey sample text from the form (for example a placeholder phone number) in the signature. If you don't want a line, for instance a website, it's better to enter something useful there, such as your LinkedIn URL.

There's also a **Copy HTML** button, which copies the raw code. Use it for email apps or marketing tools that have an HTML signature field.

## How to add the signature in Gmail

1. Open Gmail on a computer and click the **gear icon**, then **See all settings**.
2. On the **General** tab, scroll to **Signature** and click **Create new**.
3. Give it a name, then click into the empty box and **paste** (Ctrl+V, or Cmd+V on a Mac).
4. Under **Signature defaults**, choose it for new emails and, if you like, for replies and forwards.
5. Scroll to the bottom and click **Save Changes**.

Gmail's mobile apps use their own, plain-text mobile signature setting, so the formatted version appears when you send from a computer.

## How to add the signature in Outlook

In Outlook on the web and the new Outlook for Windows:

1. Open **Settings**, then **Account**, then **Signatures**.
2. Click **New signature**, type a name, and paste into the editor.
3. Choose your default signatures for new messages and replies.
4. Click **Save**.

In the classic Outlook desktop app, the same option is under **File > Options > Mail > Signatures**. Menu names change between versions, so if you can't find it, search "signatures" in Outlook's settings.

## How to add it in Apple Mail

Open **Mail > Settings** (or Preferences), go to **Signatures**, select your account, click **+**, and paste. If the formatting looks plain, untick "Always match my default message font."

## Tips for a signature people actually read

- **Keep it short.** Name, role, company, one phone number, email and website are enough. Long legal disclaimers and quotes push the useful parts out of sight.
- **Use one accent colour.** The generator uses a single colour for the title and divider line. That looks more professional than a rainbow.
- **Write your phone number in international format**, like `+92 300 1234567` or `+44 20 7946 0000`, so contacts abroad can tap and dial it from their phone.
- **Skip the giant logo image.** Images are often blocked or shown as attachments. A text-based signature, like this one, always loads.
- **Test it.** Send an email to yourself and open it on your phone and computer before you send it to clients.
- **Give people a quick way to save your details.** At events or on printed material, a QR code that links to your website or contact page helps. Make one with the [QR Code Generator](/qr-code-generator/).

## Troubleshooting

**The formatting disappears when I paste.** Your browser may not allow rich copying. Try a different browser, or use **Copy HTML** and paste into an HTML signature field if your email app has one.

**There's sample text in my signature.** One of the fields was left empty. Fill it in, copy again and replace the old signature.

**The icons look different on some devices.** The phone, mail and globe icons are emoji, so their style depends on the device's emoji set. They're still recognisable everywhere.

**The colours look off in dark mode.** Some apps invert colours in dark mode. Medium-dark accent colours (deep pink, blue, green) hold up better than very light ones.

## Privacy

Your name and contact details are used only to build the preview in your browser. Nothing is sent to DoraPDF or stored anywhere.

## FAQ

**Is the email signature generator free?**
Yes. No sign-up, no watermark, and no "made with" branding in your signature.

**Can I add a photo, logo or social media icons?**
Not in this generator. It creates a clean text-based signature, which displays reliably in all email apps. You can add your LinkedIn link in the website field.

**Will it work with Yahoo Mail or other email providers?**
Most webmail services have a signature setting that accepts pasted formatted text. Paste it there the same way as in Gmail.

**How do I update my signature later?**
Open the generator, change the details, copy again, and replace the old signature in your email settings.
"""),
dict(slug='word-counter-online-essay-speech-reading-time', title='Word Counter Online: Check Essay Length, Characters and Speaking Time', date='2026-11-17',
 desc='Count words, characters, sentences and paragraphs as you type, and see reading and speaking time. Free word counter for essays, speeches and posts.',
 tools=['word-counter', 'pdf-to-txt', 'text-formatter'], md="""
"Essay: 1,500 words, plus or minus 10%." "Abstract: maximum 250 words." "Speech: five minutes." Limits like these are everywhere in school, university and work, and going far over or under can cost marks or get a submission rejected.

DoraPDF's free [Word Counter](/word-counter/) counts as you type or paste. Alongside the word count, it shows characters (with and without spaces), sentences, paragraphs, and estimated reading and speaking time, all at once and without sign-up.

## What the word counter shows

| Result | What it means |
|---|---|
| **Words** | Every group of characters separated by spaces or line breaks |
| **Characters** | All characters, including spaces |
| **Characters (no spaces)** | Letters, numbers and punctuation only |
| **Sentences** | Pieces of text ending with `.`, `!` or `?` |
| **Paragraphs** | Blocks of text separated by an empty line |
| **Reading time** | Based on about 230 words per minute |
| **Speaking time** | Based on about 150 words per minute |

Results update live, so you can watch the count change while you edit.

## How to count words in your text

1. Open the [Word Counter](/word-counter/).
2. Paste your text into the box, or type directly.
3. Read the results below the box. That's it: no button to press.

It works the same on a phone, which is handy when you're checking a caption or application answer on the go.

## Counting words in a PDF, scan or image

The counter needs plain text. If your text is locked in a file:

- **PDF:** extract the text with the [PDF to TXT converter](/pdf-to-txt/), then paste it into the counter.
- **Photo or scanned page:** pull the text out with the [image to text (OCR) tool](/image-to-text/) first.
- **Word or Google Docs:** select all, copy and paste. (Both editors also have their own counters, but pasting here gives you reading and speaking time too.)

If the pasted text arrives with messy line breaks or double spaces, clean it with the [Text Formatter](/text-formatter/): "Remove extra spaces" and "Remove line breaks" fix most copy-paste problems, and they also make the paragraph count accurate.

## How many words for a 5-minute speech?

The speaking estimate uses about 150 words per minute, a comfortable pace for presentations. That gives a quick rule of thumb:

- **1 minute** ≈ 150 words
- **3 minutes** ≈ 450 words
- **5 minutes** ≈ 750 words
- **10 minutes** ≈ 1,500 words

Real speaking speed varies. Nervous speakers often go faster; pauses, slides and audience questions slow you down. Use the estimate to draft, then rehearse out loud with a timer and trim if needed. Leaving a little slack is better than rushing your conclusion.

## Practical tips for hitting a word limit

**Know what's counted.** Many universities exclude the reference list, title page and sometimes in-text citations or tables from the word count. Check your assignment brief, and paste only the parts that count.

**Cutting words without losing meaning:**

- Remove filler phrases: "in order to" becomes "to", "due to the fact that" becomes "because".
- Delete sentences that repeat the previous point.
- Replace long lists of examples with the strongest one or two.
- Use active voice: "The team analysed the data" is shorter than "The data was analysed by the team."

**Adding words without padding:**

- Add a concrete example or a short case study.
- Explain *why* a source matters, not just what it says.
- Address a counter-argument and respond to it.
- Strengthen your conclusion with implications or next steps.

If you're still at the planning stage, DoraPDF's AI [Assignment Helper](/blog/assignment-helper-for-students/) can help you build an outline and find sources to study from. The writing, the thinking and the final word count are still yours.

## Why counts sometimes differ between tools

You may notice small differences between this counter, Microsoft Word and Google Docs. That's normal:

- Hyphenated words (`well-known`), numbers, URLs and email addresses count as **one word** here, because words are split at spaces.
- Dashes surrounded by spaces (` – `) count as a word in some tools and not in others.
- Sentences are counted by end punctuation, so abbreviations like "Dr." or "e.g." can add an extra sentence, and a last line without a full stop isn't counted.
- Some emoji take up two characters in the character count.

For an assignment, use the counter your institution recommends if it specifies one, and treat small differences as rounding.

## Character counts for posts and forms

Character limits matter more than word counts for meta descriptions, ad headlines, social media bios and many online application forms. Use **Characters** when the limit includes spaces, and **Characters (no spaces)** when the form says so. When in doubt, assume spaces count.

## Privacy

Your text is counted in your browser and never sent to a server. You can safely paste unpublished essays, cover letters or confidential reports.

## FAQ

**Is this word counter free?**
Yes. Free, with no sign-up and no limit on text length for normal documents.

**Does it count words in other languages?**
It counts words separated by spaces, so it works for English, Urdu written with spaces, Spanish, German and most other languages. Languages written without spaces between words, such as Chinese or Japanese, won't give a meaningful word count; use the character count instead.

**How long does it take to read 1,000 words?**
At about 230 words per minute, roughly 4 to 5 minutes. Speaking 1,000 words aloud takes around 7 minutes.

**Does the word count include spaces or punctuation?**
No. Words are counted between spaces; punctuation attached to a word doesn't add an extra word.
"""),
dict(slug='compresser-pdf-envoyer-par-email', lang='fr', title="Compresser un PDF pour l'envoyer par e-mail : réduire la taille sans le rendre illisible", date='2026-11-17',
 desc="Votre PDF est trop lourd pour un e-mail ou un dépôt en ligne ? Compressez-le gratuitement, sans inscription, et choisissez entre qualité et poids minimal.",
 tools=['pdf-compressor', 'pdf-splitter', 'pdf-merger'], md="""
Le dossier de location est prêt, la candidature aussi, vous cliquez sur « Envoyer »… et la messagerie refuse la pièce jointe. Ou bien c'est le portail de l'administration, de l'école ou de l'employeur qui affiche « fichier trop volumineux ». Un PDF qui contient des scans ou des photos peut vite peser 15, 30 ou 50 Mo. Il faut alors **compresser le PDF** pour le faire passer, sans pour autant le rendre illisible.

Voici comment faire gratuitement avec le [compresseur de PDF](/pdf-compressor/) de DoraPDF (l'interface de l'outil est en anglais), et surtout comment choisir le bon réglage.

## Quelle taille viser ?

Les limites varient selon les services, mais quelques repères aident :

- **Gmail** accepte jusqu'à 25 Mo de pièces jointes par message ; au-delà, il propose un lien Google Drive à la place.
- **Outlook.com** limite les pièces jointes classiques à 20 Mo.
- **Les portails en ligne** (candidatures, dossiers administratifs, plateformes scolaires) imposent souvent des limites bien plus basses, parfois 2 ou 5 Mo par fichier. La limite est en général indiquée à côté du bouton de dépôt.

Gardez aussi en tête que votre destinataire a sa propre limite de réception, et qu'un fichier de 3 Mo s'ouvre bien plus vite sur un téléphone qu'un fichier de 30 Mo.

## Les deux modes de compression

### « Smart » : garder le texte sélectionnable

Ce mode réorganise la structure interne du PDF pour l'alléger, **sans toucher au contenu** : le texte reste net et sélectionnable, les images ne sont pas dégradées. C'est le premier à essayer, en particulier pour les documents créés sur ordinateur (exports Word, factures, rapports).

Le gain dépend beaucoup du fichier : parfois appréciable, parfois quasi nul. Si l'outil indique que le fichier est déjà optimisé (« already optimised »), c'est qu'il n'y a plus rien à gagner sans toucher aux images.

### « Strong » : compression maximale

Ici, chaque page est transformée en image puis recompressée. C'est très efficace sur les **scans et les PDF remplis de photos**, qui sont justement ceux qui pèsent le plus. Vous choisissez le niveau de qualité des images :

- **High quality** : le meilleur rendu, pour un document que l'on imprimera ;
- **Balanced** (par défaut) : un bon compromis pour l'écran et l'impression courante ;
- **Smallest** : le poids minimal, quand la limite est très stricte.

À savoir : en mode « Strong », **le texte n'est plus sélectionnable** ni recherchable, puisque les pages deviennent des images. Pour un dossier de pièces justificatives, ce n'est pas gênant ; pour un CV qui sera lu par un logiciel de recrutement, mieux vaut rester en mode « Smart ».

## Compresser un PDF étape par étape

1. Ouvrez le [compresseur de PDF](/pdf-compressor/).
2. Déposez votre fichier.
3. Dans **Mode**, choisissez « Smart » ou « Strong ».
4. En mode « Strong », réglez la **qualité des images** (Image quality).
5. Cliquez sur **Compress**.
6. Téléchargez le fichier : son nom se termine par « -compressed » et l'outil affiche le pourcentage gagné.

Ouvrez toujours le résultat avant de l'envoyer et zoomez sur les petits caractères (numéros, montants, signatures) pour vérifier qu'ils restent lisibles.

## La bonne méthode, du plus doux au plus fort

1. Essayez d'abord **Smart**. Si le fichier passe sous la limite, c'est terminé.
2. Sinon, passez en **Strong** avec **Balanced**.
3. Toujours trop lourd ? Essayez **Smallest**, puis vérifiez la lisibilité.
4. En dernier recours, **découpez le document** : avec [Diviser un PDF](/pdf-splitter/) (interface en anglais), séparez-le en deux ou trois parties et envoyez-les dans des e-mails distincts, ou retirez les pages inutiles.

Repartez toujours du fichier d'origine à chaque essai : compresser plusieurs fois un fichier déjà compressé dégrade la qualité sans gain réel.

## Cas pratiques

**Un dossier de location.** Pièces d'identité, avis d'imposition, bulletins de salaire, attestation d'employeur… souvent scannés un par un. Rassemblez-les dans l'ordre demandé avec [Fusionner des PDF](/pdf-merger/) (interface en anglais), puis compressez le fichier final en mode « Strong », qualité « Balanced ». Ces documents contiennent des données sensibles : c'est justement le genre de fichier qu'on préfère ne pas confier à un serveur inconnu.

**Une candidature en ligne.** CV et lettre de motivation exportés depuis Word pèsent rarement lourd. Si c'est le cas, cherchez le coupable : une photo très haute résolution, un logo géant. Le mode « Smart » suffit souvent ; sinon, réduisez l'image dans votre document d'origine et réexportez.

**Un mémoire ou un rapport plein de graphiques.** Si le texte doit rester sélectionnable pour le correcteur, restez en « Smart ». Si le fichier reste trop lourd, déposez-le plutôt via un lien de partage que votre établissement accepte.

## Confidentialité : le fichier ne quitte pas votre appareil

Avec DoraPDF, la compression se fait **dans votre navigateur**. Le PDF n'est pas envoyé sur nos serveurs et n'est stocké nulle part. Pour des documents comme un avis d'imposition ou une pièce d'identité, c'est un vrai plus en matière de protection des données.

## Questions fréquentes

**Peut-on compresser un PDF gratuitement et sans inscription ?**
Oui. L'outil est gratuit, sans compte et sans filigrane.

**La compression fait-elle perdre de la qualité ?**
En mode « Smart », non : le contenu n'est pas modifié. En mode « Strong », les pages sont recompressées en images ; avec « Balanced », la différence est rarement visible à l'écran.

**Pourquoi mon PDF ne diminue presque pas en mode Smart ?**
Parce que l'essentiel du poids vient des images, que ce mode ne touche pas. Passez en mode « Strong » si vous n'avez pas besoin de texte sélectionnable.

**Puis-je compresser un PDF sur mon téléphone ?**
Oui, depuis le navigateur. Le fichier compressé se retrouve dans vos téléchargements, prêt à être joint à un e-mail.

**Peut-on compresser plusieurs PDF d'un coup ?**
L'outil traite un fichier à la fois. Si vous avez plusieurs documents à envoyer ensemble, fusionnez-les d'abord, puis compressez le résultat.
"""),
dict(slug='convertir-pdf-en-word-gratuit-mise-en-page', lang='fr', title='Convertir un PDF en Word gratuitement sans perdre la mise en page : le bon mode pour chaque document', date='2026-11-17',
 desc='Convertir un PDF en Word gratuitement, sans inscription : garder la mise en page ou obtenir un texte facile à modifier, et que faire avec un PDF scanné.',
 tools=['pdf-to-word', 'pdf-ocr', 'word-to-pdf'], md="""
Vous devez corriger une coquille dans une attestation, mettre à jour un ancien CV dont vous n'avez plus le fichier d'origine, ou reprendre un modèle de courrier reçu en PDF. Dans tous ces cas, il faut **convertir le PDF en Word** pour retrouver un document modifiable. Et la question qui revient toujours : est-ce que la mise en page va survivre ?

La réponse honnête : cela dépend de ce que vous voulez faire du document. Le convertisseur gratuit [PDF en Word](/pdf-to-word/) de DoraPDF propose justement deux modes, pensés pour deux besoins différents. L'interface de l'outil est en anglais, mais elle tient en trois clics.

## Deux modes, deux usages

### « Keep original layout » : garder la mise en page

C'est le mode recommandé, sélectionné par défaut. Pour chaque page, l'outil reconstruit un document Word où :

- le texte est placé **exactement là où il était** sur la page PDF, ligne par ligne ;
- la **taille**, la **couleur**, le **gras** et l'**italique** sont conservés, avec une police aussi proche que possible de l'originale ;
- les éléments graphiques (logos, images, cadres, lignes, fonds colorés) restent en arrière-plan, comme une image de la page.

Résultat : le fichier .docx ressemble trait pour trait au PDF. C'est idéal pour **corriger quelques mots**, changer une date, un nom ou un montant, puis réenregistrer.

La contrepartie : chaque ligne est un bloc indépendant. Réécrire un paragraphe entier ou ajouter plusieurs lignes est moins pratique, car le texte ne « coule » pas d'une ligne à l'autre comme dans un document Word classique.

### « Text only » : un texte simple et fluide

Ce mode récupère le texte de chaque page sous forme de paragraphes normaux. Les lignes plus grandes que le texte courant (les titres) sont mises en gras et en plus grand, et chaque page du PDF commence sur une nouvelle page Word.

Vous perdez les images et la disposition exacte, mais vous obtenez un document **très facile à retravailler** : réécrire, couper, déplacer des paragraphes, changer de police d'un coup.

## Quel mode choisir ?

| Ce que vous voulez faire | Mode conseillé |
|---|---|
| Corriger une date, un nom, un chiffre | Keep original layout |
| Modifier un formulaire ou un document très mis en forme | Keep original layout |
| Réécrire de larges passages, reprendre un rapport | Text only |
| Récupérer le texte d'un cours ou d'un article pour le citer | Text only |

## Convertir un PDF en Word étape par étape

1. Ouvrez le convertisseur [PDF en Word](/pdf-to-word/).
2. Choisissez le mode dans le menu **Layout**.
3. Déposez votre PDF dans la zone d'envoi.
4. Cliquez sur le bouton de conversion et patientez quelques secondes.
5. Téléchargez le fichier **.docx**, qui porte le même nom que votre PDF.

Le fichier s'ouvre dans Microsoft Word, LibreOffice Writer, Pages ou Google Docs. Pour un résultat fidèle en mode « mise en page », Word et LibreOffice donnent généralement le meilleur rendu.

## Et si le PDF est scanné ?

Si l'outil affiche un message indiquant qu'aucun texte n'a été trouvé (« No text found »), votre PDF est une image : une numérisation ou une photo de document. Il n'y a pas de texte à extraire, seulement des pixels.

La solution se fait en deux temps :

1. Passez d'abord le fichier dans l'outil [OCR PDF](/pdf-ocr/) (interface en anglais) en choisissant **French** comme langue. La reconnaissance de caractères crée un PDF dans lequel le texte devient sélectionnable, ainsi qu'un fichier .txt.
2. Convertissez ensuite ce nouveau PDF en Word.

L'OCR travaille page par page et prend quelques secondes par page, jusqu'à 60 pages par fichier. Plus le scan est net et droit, meilleur sera le résultat. Relisez toujours les chiffres et les noms propres : ce sont eux qui posent le plus souvent problème.

## Astuces pour un meilleur résultat

- **Ne convertissez que les pages utiles.** Pour modifier une seule page d'un dossier de 30 pages, extrayez-la d'abord : le fichier Word sera plus léger et plus simple à manipuler.
- **Vérifiez les polices.** Si une police du PDF n'est pas installée sur votre ordinateur, Word la remplace par une police proche. Les espacements peuvent alors légèrement varier.
- **Pour les tableaux à retravailler**, le mode « Text only » donne du texte brut ; si vous voulez des cellules à calculer, une conversion vers Excel est souvent plus adaptée.
- **Repassez en PDF à la fin.** Une fois vos corrections faites, enregistrez le document en PDF depuis Word (Fichier → Enregistrer sous → PDF). Si vous n'avez pas Word sous la main, l'outil [Word en PDF](/word-to-pdf/) (interface en anglais) accepte aussi les fichiers .docx.

## Problèmes fréquents

**Le texte est découpé en petites zones dans Word.** C'est le fonctionnement normal du mode « mise en page ». Pour éditer librement, reconvertissez en mode « Text only ».

**Des caractères manquent ou sont remplacés.** Certains PDF utilisent des polices incorporées avec un encodage inhabituel. Essayez l'autre mode, ou passez le document par l'OCR.

**Le PDF est protégé par un mot de passe.** S'il s'agit de votre document et que vous connaissez le mot de passe, retirez-le d'abord, puis convertissez.

## Confidentialité : vos fichiers restent dans le navigateur

Contrats, bulletins de salaire, CV, attestations : les PDF que l'on convertit contiennent souvent des données personnelles. Avec DoraPDF, la conversion se fait **directement dans votre navigateur**. Le fichier n'est pas envoyé sur un serveur pour être converti et n'est stocké nulle part, ce qui simplifie aussi les choses du point de vue du RGPD.

## Questions fréquentes

**Peut-on convertir un PDF en Word gratuitement et sans inscription ?**
Oui. L'outil est gratuit, sans compte et sans filigrane.

**La mise en page est-elle vraiment conservée ?**
En mode « Keep original layout », le texte reste à sa place avec sa taille, sa couleur et son style, et les éléments graphiques restent en arrière-plan. C'est très fidèle visuellement, mais moins pratique pour réécrire de longs passages.

**Fonctionne-t-il sur Mac, sur iPhone ou sur Android ?**
Oui, il suffit d'un navigateur récent. Sur mobile, le fichier .docx s'ouvre ensuite avec l'application Word ou Google Docs.

**Pourquoi l'outil dit-il qu'il ne trouve pas de texte ?**
Parce que le PDF est une image scannée. Passez-le d'abord par l'OCR, puis relancez la conversion.
"""),
dict(slug='crear-curriculum-pdf-gratis', lang='es', title='Crear un currículum en PDF gratis: dos caminos según dónde vayas a enviarlo', date='2026-11-17',
 desc='Crea tu currículum en PDF gratis y sin registro: con un generador de CV en el navegador o desde Word, con consejos de contenido y errores que evitar.',
 tools=['resume-builder', 'word-to-pdf', 'pdf-compressor'], md="""
Un buen currículum no necesita un diseño espectacular ni una suscripción de pago. Necesita ser claro, caber en una o dos páginas y llegar en un formato que se abra igual en cualquier ordenador. Ese formato es el PDF. Si quieres **crear un currículum en PDF gratis**, tienes dos caminos, y elegir bien depende sobre todo de a dónde vas a enviarlo.

## Camino 1: el generador de CV de DoraPDF

El [Creador de currículum](/resume-builder/) es un formulario en el navegador que genera un CV limpio en PDF tamaño A4, sin registro y sin marca de agua. La pantalla está en inglés, igual que los títulos de las secciones que aparecen en el PDF: **SUMMARY, EXPERIENCE, EDUCATION y SKILLS**. Todo lo que tú escribas aparece tal cual, con tildes y eñes.

Por eso encaja especialmente bien cuando tu candidatura es **en inglés**: empresas multinacionales, prácticas en el extranjero, becas internacionales o un puesto donde te piden el CV en ese idioma.

Una ventaja importante: el texto del PDF queda **seleccionable**, así que los portales de empleo que leen el currículum de forma automática pueden extraer tus datos y palabras clave.

### Cómo rellenarlo

1. Abre el [Creador de currículum](/resume-builder/).
2. **Full name** y **Job title**: tu nombre y el puesto al que aspiras (por ejemplo, «Junior Data Analyst»).
3. **Email, Phone, City, Website / LinkedIn**: tus datos de contacto. Aparecen en una sola línea bajo tu nombre.
4. **Summary**: dos o tres frases sobre quién eres y qué aportas.
5. **Experience**: cada empleo en un bloque, **separados por una línea en blanco**. Las líneas sin viñeta (puesto, empresa y fechas) salen en negrita, y las que empiezan por «•» o «-» salen en texto normal. Por eso conviene escribir las tareas y logros siempre como viñetas.
6. **Education**: estudios, centro y años, con el mismo sistema.
7. **Skills**: tus habilidades separadas por comas.
8. Elige un **color de acento** para el nombre, los títulos y la línea separadora.
9. Pulsa **Download resume PDF**. Si el contenido no cabe en una página, se añade otra automáticamente.

El generador no incluye foto. En muchos países, sobre todo en candidaturas en inglés, es habitual no ponerla.

## Camino 2: escribirlo en Word o Google Docs y pasarlo a PDF

Si buscas trabajo en España o Latinoamérica y quieres el CV completamente en español, con títulos como «Experiencia profesional» o «Formación», o necesitas incluir foto, lo más práctico es usar un procesador de texto:

1. Escribe el CV en Word, LibreOffice o Google Docs (todos tienen plantillas).
2. Expórtalo directamente a PDF: en Word, Archivo → Guardar como → PDF; en Google Docs, Archivo → Descargar → Documento PDF.

Exportar desde el propio programa conserva tu diseño y deja el texto seleccionable. Si estás en un ordenador sin programas o en el móvil, puedes usar [Convertir Word a PDF](/es/convertir-word-a-pdf/) con tu archivo .docx. Ten en cuenta que ese conversor usa una fuente estándar y guarda cada página como imagen, así que para el CV definitivo que envíes a un portal de empleo es mejor exportar desde el editor en cuanto puedas.

## Qué poner en el currículum (y qué no)

**Sí:**

- Datos de contacto actualizados y un correo con aspecto profesional.
- Experiencia en orden cronológico inverso: lo más reciente, primero.
- Logros concretos con verbos de acción: «Reduje el tiempo de respuesta a clientes», «Coordiné un equipo de cuatro personas». Si tienes cifras reales, úsalas; no las inventes.
- Las palabras clave que aparecen en la oferta, si de verdad describen lo que sabes hacer.
- Idiomas con su nivel (por ejemplo, según el Marco Común Europeo: B2, C1).

**No hace falta:**

- DNI, estado civil o fecha de nacimiento completa.
- La palabra «Currículum vítae» como título.
- Una lista interminable de cursos de pocas horas sin relación con el puesto.

## Extensión y nombre del archivo

Con poca experiencia, **una página** es suficiente. Con muchos años de trayectoria, dos páginas están bien. Más allá de eso, resume.

El nombre del archivo también comunica: «Lucia_Martin_CV.pdf» es mucho mejor que «curriculum_final_v3.pdf». En el generador de DoraPDF, el archivo se nombra automáticamente con tu nombre seguido de «-resume».

## Antes de enviarlo: lista de comprobación

- Ábrelo en el móvil y en el ordenador: ¿se lee bien en los dos?
- Selecciona un trozo de texto con el ratón. Si se selecciona, los sistemas automáticos también podrán leerlo.
- Revisa la ortografía, sobre todo nombres de empresas y fechas.
- Comprueba el tamaño. Un CV de texto pesa muy poco; si el tuyo lleva foto o gráficos y supera el límite de un portal, redúcelo con [Comprimir PDF](/es/comprimir-pdf/).
- Adapta el resumen y las habilidades a cada oferta. Cinco minutos de ajuste por candidatura marcan diferencia.

## Privacidad

Un currículum reúne tu nombre, teléfono, correo y trayectoria. Con DoraPDF, tanto el generador de CV como el conversor de Word a PDF funcionan **en tu navegador**: tus datos no se envían a ningún servidor ni se guardan.

Un último consejo práctico: como la herramienta no almacena nada, guarda tus textos (resumen, experiencia) en un documento aparte. Así, cuando quieras actualizar el CV, solo tendrás que copiarlos y pegarlos.

## Preguntas frecuentes

**¿Puedo crear un currículum en PDF gratis sin registrarme?**
Sí. El generador es gratuito, no pide cuenta y no añade marca de agua.

**¿El CV sale en español?**
Lo que escribes sale en el idioma que uses, pero los títulos de las secciones salen en inglés. Para un CV con títulos en español, usa Word o Google Docs y expórtalo a PDF.

**¿Los portales de empleo pueden leer el PDF del generador?**
Sí, el texto queda seleccionable, que es lo que necesitan esos sistemas para leerlo.

**¿Puedo añadir foto?**
El generador no tiene campo de foto. Si la necesitas, crea el CV en un procesador de texto.

**¿Se guarda mi currículum en la web?**
No. Guarda el PDF y una copia de tus textos para futuras actualizaciones.
"""),
dict(slug='comprimir-imagen-sin-perder-calidad', lang='es', title='Comprimir imagen sin perder calidad: qué ajustes elegir para web, correo y formularios', date='2026-11-17',
 desc='Comprime imágenes JPG y PNG gratis y sin perder calidad visible: qué nivel y tamaño elegir para tu web, el correo o un formulario con límite de KB.',
 tools=['image-compressor', 'image-resizer', 'png-to-jpg'], md="""
«El archivo supera el tamaño máximo permitido». Si alguna vez has intentado subir una foto a un formulario, a una tienda online o a tu web, conoces el mensaje. Las fotos de un móvil actual pesan varios megas y casi ningún sitio las necesita tan grandes. La solución es **comprimir la imagen**, y bien hecho no se nota a simple vista.

Vamos a ver qué significa realmente «sin perder calidad», cómo comprimir imágenes gratis con el [compresor de imágenes](/es/comprimir-imagen/) de DoraPDF y qué ajustes elegir según para qué la quieras.

## «Sin perder calidad»: lo que es posible y lo que no

Seamos precisos. Casi toda la compresión que reduce mucho el peso de una foto es **con pérdida**: elimina información que el ojo humano apenas percibe. El objetivo no es que la imagen sea idéntica bit a bit, sino que **no notes la diferencia** al verla en pantalla o impresa a un tamaño normal.

Hay dos palancas que se combinan:

1. **La calidad de compresión**: cuánto detalle fino se descarta.
2. **La resolución**: cuántos píxeles tiene la imagen. Una foto de 4000 píxeles de ancho que se va a ver en un hueco de 800 lleva muchísimos píxeles que nadie verá.

Reducir la resolución suele ahorrar más peso y con menos efecto visible que bajar mucho la calidad.

## Cómo comprimir imágenes paso a paso

1. Abre el [compresor de imágenes](/es/comprimir-imagen/).
2. Añade una o **varias imágenes a la vez**.
3. En **Strength** (intensidad) elige:
   - **Light**: compresión suave, máxima fidelidad.
   - **Balanced** (por defecto): el mejor equilibrio para la mayoría de usos.
   - **Strong**: el menor peso posible, con más riesgo de que se note.
4. En **Resize** elige el ancho máximo: tamaño original, 2560, 1920 (por defecto), 1280 u 800 píxeles. Las imágenes más estrechas que ese valor no se agrandan.
5. Pulsa **Compress** y descarga los archivos. Junto a cada uno verás cuánto se ha reducido en porcentaje.

Los archivos comprimidos llevan «-small» al final del nombre, para que no se confundan con los originales.

## Qué ajustes elegir según el uso

| Para qué es la imagen | Intensidad | Ancho máximo |
|---|---|---|
| Imprimir o archivar con buena calidad | Light | Original o 2560 px |
| Web, blog o tienda online | Balanced | 1920 o 1280 px |
| Enviar por correo o WhatsApp como archivo | Balanced | 1280 px |
| Formulario con límite estricto (por ejemplo, 200 KB) | Balanced o Strong | 800 px |
| Foto de perfil o miniatura | Balanced | 800 px |

Si después de comprimir todavía te pasas del límite, baja primero el ancho máximo y solo después sube la intensidad.

## Lo que pasa con cada formato

**Fotos JPG (y la mayoría de formatos).** Se guardan como **JPG** comprimido. Si la imagen tenía zonas transparentes, se rellenan de blanco.

**Imágenes PNG.** Se guardan en formato **WebP**, que es mucho más ligero que PNG y **conserva la transparencia**. Es ideal para logotipos y gráficos en una web. Ojo: algunos formularios antiguos no aceptan WebP. Si ese es tu caso y la imagen no necesita transparencia, conviértela primero con [PNG a JPG](/es/png-a-jpg/) y comprime después el JPG.

**Fotos del iPhone (HEIC).** Si tienes problemas para seleccionarlas, conviértelas antes con [HEIC a JPG](/es/heic-a-jpg/).

## Si necesitas una medida exacta

El compresor limita el ancho, pero no fuerza unas dimensiones concretas (y en fotos verticales el alto queda mayor que el ancho). Si un portal exige, por ejemplo, una foto de 600 × 800 píxeles, usa primero el [Redimensionador de imágenes](/image-resizer/) (pantalla en inglés) para fijar las medidas exactas y luego comprime el resultado.

## Errores habituales

**Comprimir varias veces la misma imagen.** Cada pasada con pérdida degrada un poco más. Si no te convence el resultado, vuelve a partir del original con otros ajustes.

**Usar «Strong» para todo.** En fotos con cielos, piel o degradados suaves pueden aparecer bandas o manchas. Reserva la intensidad fuerte para cuando el límite de peso no deja otra opción.

**Reducir demasiado capturas de pantalla con texto.** El texto pequeño se vuelve borroso enseguida. Para capturas, mantén un ancho máximo generoso (1920 px) y la intensidad en Light o Balanced.

**Olvidarse del original.** Guarda siempre las fotos originales. La versión comprimida es para compartir, no para archivar.

## Por qué importa en una web

Las imágenes suelen ser lo que más pesa en una página. Unas fotos de 5 MB hacen que la web cargue lenta, sobre todo con datos móviles, y eso afecta a quien la visita. Comprimir antes de subir (en lugar de confiar en que la plataforma lo haga) te da control sobre el resultado final.

## Privacidad: tus imágenes no se suben

Fotos personales, documentos fotografiados, imágenes de clientes… En DoraPDF, la compresión se hace **en tu navegador**. Las imágenes no salen de tu dispositivo ni se guardan en ningún servidor.

## Preguntas frecuentes

**¿Cómo comprimo una imagen sin perder calidad visible?**
Usa la intensidad Balanced o Light y reduce el ancho al que realmente necesitas (por ejemplo, 1920 px para web). Así baja mucho el peso sin diferencias apreciables.

**¿Puedo comprimir varias fotos a la vez?**
Sí, puedes añadir varias imágenes en la misma tanda y descargarlas todas.

**¿Por qué mi PNG se ha convertido en WebP?**
Porque WebP pesa mucho menos y mantiene la transparencia. Si necesitas JPG, convierte el PNG antes de comprimir.

**¿Es gratis y sin registro?**
Sí, sin cuenta y sin marca de agua.

**¿Funciona en el móvil?**
Sí, desde el navegador del teléfono puedes elegir fotos de tu galería y descargar las versiones comprimidas.
"""),
dict(slug='hacer-factura-gratis-online', lang='es', title='Hacer una factura gratis online en PDF: cómo rellenarla bien y cuándo te sirve', date='2026-11-17',
 desc='Cómo hacer una factura gratis online y descargarla en PDF: datos obligatorios, IVA, descuentos y casos en los que necesitas un programa de facturación.',
 tools=['invoice-generator', 'receipt-generator', 'sign-pdf'], md="""
Acabas de terminar un encargo como freelance, has vendido algo a una empresa o un cliente extranjero te pide «an invoice» para poder pagarte. No tienes programa de facturación y tampoco quieres pelearte con una plantilla de Word que se descuadra cada vez que añades una línea. Para estos casos, **hacer una factura gratis online** y descargarla en PDF es lo más rápido.

En esta guía verás cómo usar el [Generador de facturas](/invoice-generator/) de DoraPDF, qué datos no pueden faltar en una factura en España y, con la misma claridad, en qué casos esta herramienta no es la adecuada.

## Lo que hace el generador de facturas

Es un formulario sencillo que produce una factura en PDF tamaño A4, con tu nombre comercial arriba, una tabla de conceptos y los totales calculados automáticamente. La pantalla de la herramienta está en inglés, y **los títulos del PDF también salen en inglés** («INVOICE», «Bill to», «Item», «Qty», «Price», «Subtotal», «Total»). Los importes se muestran con el formato inglés (por ejemplo, €1,250.00).

Esto lo hace especialmente práctico para **facturar a clientes internacionales**, que esperan precisamente ese formato.

## Cómo hacer una factura paso a paso

1. Abre el [Generador de facturas](/invoice-generator/).
2. **From**: escribe tu nombre o el de tu negocio.
3. **Invoice #**: la herramienta propone un número automático; cámbialo por tu numeración correlativa (por ejemplo, 2026-014). La numeración debe ser seguida y sin saltos.
4. **Date** y **Due date**: fecha de emisión y fecha de vencimiento del pago.
5. **Your details**: tu dirección, teléfono, correo y, muy importante, tu **NIF**.
6. **Bill to**: nombre o razón social del cliente, su dirección y su NIF (o el número de IVA intracomunitario si es una empresa de otro país de la UE).
7. Añade los **conceptos**: descripción, cantidad y precio unitario. Con «+ Add item» sumas líneas y con la ✕ borras las de ejemplo.
8. Elige la **moneda** (EUR, USD, GBP, AED o PKR) y escribe el **Tax %**, por ejemplo 21 para el IVA general.
9. En **Notes** pon tu IBAN, el plazo de pago y cualquier mención legal que corresponda.
10. Elige un **color** de marca si quieres y pulsa **Download invoice PDF**.

## Datos que debe llevar una factura en España

Una factura completa debe incluir, entre otros:

- Número (y serie, si usas) y fecha de expedición.
- Nombre y apellidos o razón social, NIF y domicilio de quien emite y de quien recibe.
- Descripción de los bienes o servicios.
- Base imponible, tipo de IVA aplicado y cuota.
- Importe total.

En el generador, todo esto encaja en los campos «Your details», «Bill to», los conceptos y el porcentaje de impuesto. Si una operación está exenta de IVA o sujeta a inversión del sujeto pasivo, la mención correspondiente va en «Notes».

## Dos detalles importantes al calcular

**Los descuentos, mejor como línea negativa.** El campo «Discount» resta el importe al final, **después** de calcular el impuesto. En España el IVA se calcula sobre la base ya descontada. Para que salga bien, añade el descuento como un concepto más con precio negativo (por ejemplo, «Descuento 10 %» con precio −50). Así el impuesto se aplica sobre la base correcta.

**La retención de IRPF no está incluida.** Si eres autónomo y facturas a empresas o profesionales en España, normalmente tienes que aplicar una retención de IRPF. El generador solo tiene un campo de impuesto que se suma, así que no puede restar la retención correctamente. Para esas facturas, lo adecuado es un programa de facturación o tu gestoría.

## Cuándo te sirve y cuándo no

**Te sirve bien para:**

- Facturas a **clientes de fuera de España**, sobre todo en inglés.
- Ventas puntuales sin retención, con un cálculo sencillo.
- **Facturas proforma** y propuestas de precio antes de cerrar un trabajo (indícalo en las notas).
- Tener un PDF limpio y con tu color de marca en un par de minutos.

**No es la herramienta adecuada si:**

- Necesitas aplicar **retención de IRPF**.
- Necesitas una factura con los títulos en español.
- Tienes que emitir factura electrónica a través de un sistema oficial. En muchos países de Latinoamérica la factura válida es la que se emite por el sistema de la autoridad fiscal, y un PDF generado aparte no la sustituye. En España, el calendario aprobado a finales de 2025 hace obligatorio Verifactu para los programas de facturación a lo largo de 2027 (salvo nuevos cambios). Si facturas de forma habitual, consulta con tu gestoría qué herramienta debes usar.

## Consejos prácticos

- **Guarda una copia de cada factura** en una carpeta por año. La herramienta no guarda nada por ti.
- **Ponle nombre al archivo** con el número y el cliente, por ejemplo «2026-014_Cliente.pdf».
- **¿Te piden la factura firmada?** Fírmala después con [Firmar PDF](/es/firmar-pdf/).
- **¿Cobraste en mano en tu tienda?** Para eso es más práctico un recibo. El [Generador de recibos](/receipt-generator/) (pantalla en inglés) crea un ticket estrecho tipo caja.

## Privacidad

Una factura contiene tu NIF, tu dirección, tu IBAN y los datos de tu cliente. En DoraPDF, la factura se genera **en tu navegador**: los datos no se envían a ningún servidor y no se almacenan.

## Preguntas frecuentes

**¿Puedo hacer una factura gratis sin registrarme?**
Sí. Rellenas el formulario, descargas el PDF y listo, sin cuenta y sin marca de agua.

**¿Puedo poner el IVA al 21 %, 10 % o 4 %?**
Sí, en el campo de impuesto escribes el porcentaje. Si una factura mezcla tipos distintos, haz facturas separadas o usa un programa de facturación.

**¿Se guardan mis facturas en la web?**
No. Descarga cada factura y guárdala tú mismo.

**¿La factura sale en español?**
No: los títulos del PDF salen en inglés. Lo que tú escribas (conceptos, notas, datos) aparece tal cual en el idioma que uses.
"""),
dict(slug='dividir-pdf-extraer-paginas', lang='es', title='Dividir PDF: cómo extraer solo las páginas que necesitas (o separar todas)', date='2026-11-17',
 desc='Dividir un PDF gratis: extrae páginas sueltas o rangos a un PDF nuevo, o separa cada página en su propio archivo. Sin registro y sin subir tus documentos.',
 tools=['pdf-splitter', 'delete-pdf-pages', 'pdf-merger'], md="""
Te piden «solo la página del DNI», «el certificado de notas del último curso» o «la factura de marzo», y lo tienes todo dentro de un PDF de treinta páginas. Enviar el documento entero no es buena idea: pesa más, obliga a la otra persona a buscar y, sobre todo, compartes datos que nadie te ha pedido.

La solución es **dividir el PDF** y quedarte únicamente con las páginas que necesitas. Con la herramienta gratuita [Dividir PDF](/es/dividir-pdf/) de DoraPDF puedes hacerlo de dos maneras, en el navegador y sin instalar nada.

## Los dos modos de la herramienta

**Extraer páginas en un solo PDF** («Extract pages into one PDF»). Escribes qué páginas quieres y obtienes un PDF nuevo que contiene solo esas. Es el modo para el 90 % de los casos: sacar un anexo, un certificado, unas cuantas páginas de un temario.

**Separar cada página en su propio PDF** («Split every page into its own PDF»). Cada página del documento se convierte en un archivo independiente. Recibes un .zip con todas ellas y, además, enlaces directos a las diez primeras para descargarlas sueltas.

## Cómo extraer páginas de un PDF paso a paso

1. Abre [Dividir PDF](/es/dividir-pdf/).
2. Sube tu documento.
3. En **Mode**, deja «Extract pages into one PDF».
4. En **Pages**, escribe las páginas que quieres. Ejemplos:
   - `5` → solo la página 5.
   - `1-3` → de la página 1 a la 3.
   - `1-3, 7, 10-12` → páginas 1, 2, 3, 7, 10, 11 y 12.
5. Pulsa **Split** y descarga el archivo. Se llamará como el original, con «-pages» al final.

## Reglas útiles del campo de páginas

- Separa los grupos con **comas**.
- Escribe los rangos **de menor a mayor** (`3-8`, no `8-3`).
- Las páginas se guardan **en el orden del documento original**, aunque las escribas desordenadas: `9, 2` produce un PDF con la página 2 y después la 9.
- Si escribes un número mayor que el total de páginas, simplemente se ignora. Si ninguna página es válida, la herramienta te avisa del rango permitido.

Si necesitas las páginas en otro orden, extráelas por separado y luego júntalas en el orden que quieras con [Unir PDF](/es/unir-pdf/).

## Tres situaciones típicas

### 1. Enviar solo una parte de un documento escaneado

Escaneaste todos tus papeles en un único PDF y ahora el banco te pide únicamente la nómina. Abre el PDF en tu visor, apunta el número de página (el del visor, no el que esté impreso en el papel) y extrae solo esa.

### 2. Separar un PDF con muchas facturas o recibos

Si tu gestor o tu programa de contabilidad quiere cada factura en un archivo distinto y las tienes todas en un PDF de una página por factura, usa el modo de separar todas las páginas. Descarga el .zip, descomprímelo y renombra cada archivo con la fecha o el número de factura.

### 3. Quedarte con un capítulo de un temario o un libro

Para estudiar en el móvil o imprimir solo lo que toca esta semana, extrae el rango del tema (por ejemplo, `45-68`). Pesa menos, carga antes en la tableta y no tienes que buscar la página cada vez.

## ¿Dividir o eliminar páginas?

Depende de cuánto quieras conservar:

- Si quieres **pocas páginas** de un documento largo, es más rápido indicar cuáles quieres con Dividir PDF.
- Si quieres **casi todo** menos un par de páginas (una en blanco, una portada que sobra), es más cómodo indicar cuáles quitar con [Eliminar páginas de PDF](/delete-pdf-pages/) (pantalla en inglés).

## Problemas frecuentes

**«Los números de página no coinciden».** Muchos documentos empiezan a numerar después de la portada o del índice. La herramienta cuenta las páginas físicas del archivo desde la primera. Fíate del número que muestra tu visor de PDF, no del impreso en la página.

**«El archivo extraído pesa casi lo mismo que el original».** Puede pasar cuando todas las páginas comparten recursos pesados, como fuentes o imágenes incrustadas. Si necesitas reducirlo, pásalo después por [Comprimir PDF](/es/comprimir-pdf/).

**«El PDF tiene contraseña».** Si es tuyo y conoces la contraseña, quítala primero con [Desbloquear PDF](/es/desbloquear-pdf/).

**«Separé todas las páginas y solo veo diez enlaces».** Los enlaces sueltos se muestran para las diez primeras páginas; el resto está dentro del archivo .zip, que siempre incluye todas.

## Privacidad: tus documentos se quedan contigo

Dividir un PDF suele ser justo el paso que das para **no** compartir más de la cuenta. Por eso es coherente que el archivo tampoco viaje a un servidor: en DoraPDF el PDF se procesa en tu navegador y no se sube ni se guarda en ningún sitio.

## Preguntas frecuentes

**¿Cómo separo páginas de un PDF gratis?**
Sube el PDF a Dividir PDF, escribe las páginas (por ejemplo, `2-4`) y descarga el nuevo archivo. Es gratis y sin registro.

**¿Puedo dividir un PDF desde el móvil?**
Sí, funciona en el navegador del móvil. En el modo de separar todas las páginas recibirás un .zip, que puedes abrir con la app de archivos de tu teléfono.

**¿Se pierde calidad al dividir?**
No. Las páginas se copian tal cual, sin volver a comprimir texto ni imágenes.

**¿Puedo extraer páginas no consecutivas?**
Sí, separándolas con comas: `1, 4, 9-11`.
"""),
dict(slug='convertir-pdf-a-excel-editar-tablas', lang='es', title='Convertir PDF a Excel gratis y editar las tablas: guía práctica con trucos de limpieza', date='2026-11-17',
 desc='Convierte un PDF a Excel gratis y edita sus tablas: una hoja por página, números listos para sumar y cómo limpiar el resultado. También para PDF escaneados.',
 tools=['pdf-to-excel', 'pdf-splitter', 'pdf-ocr'], md="""
Un extracto bancario, una lista de precios de un proveedor, las notas de una evaluación o un informe con decenas de filas. Todo en PDF, y tú necesitas sumar, filtrar u ordenar esos datos. Copiar y pegar desde el PDF suele terminar con todo el texto amontonado en una sola columna. Lo que necesitas es **convertir el PDF a Excel** para trabajar con las tablas como lo que son: filas y columnas.

Esta guía explica cómo hacerlo gratis con el conversor [PDF a Excel](/es/convertir-pdf-a-excel/) de DoraPDF y, sobre todo, cómo dejar el resultado limpio en pocos minutos.

## Antes de empezar: ¿qué tipo de PDF tienes?

Haz esta prueba rápida: abre el PDF e intenta seleccionar una palabra con el ratón.

- **Si se selecciona**, es un PDF «digital», generado desde un programa (un banco, un ERP, Excel, Word). Se convierte directamente.
- **Si no se selecciona nada** o se selecciona la página entera como un bloque, es un PDF **escaneado**: en realidad es una foto del papel. Para estos hay un paso previo, que verás más abajo.

## Cómo convertir PDF a Excel paso a paso

1. Abre [Convertir PDF a Excel](/es/convertir-pdf-a-excel/).
2. Sube el PDF.
3. Pulsa el botón de convertir. Verás una barra de progreso mientras se leen las páginas.
4. Descarga el archivo **.xlsx** y ábrelo con Excel, LibreOffice Calc, Numbers o Google Sheets.

## Qué vas a encontrar en el archivo

- **Una hoja por cada página del PDF**, con nombres como «Page 1», «Page 2», etc. Así puedes localizar cualquier dato comparándolo con el original.
- **Columnas separadas según los espacios** que hay entre los textos en el PDF. Si en el documento hay un hueco claro entre «Fecha», «Concepto» e «Importe», cada uno irá a su columna.
- **Números como números**, no como texto, de forma que puedes usar SUMA, filtros y gráficos sin convertir nada.
- **Anchos de columna ajustados** al contenido para que se lea bien al abrirlo.

## Truco: convierte solo las páginas que te interesan

Si el PDF tiene 40 páginas pero la tabla está en las páginas 12 a 15, sepáralas antes con [Dividir PDF](/es/dividir-pdf/) escribiendo «12-15». El Excel resultante tendrá solo cuatro hojas en lugar de cuarenta, sin portadas, textos legales ni gráficos que luego tendrías que borrar.

## Limpia el resultado en cinco minutos

La conversión de PDF a Excel reconstruye la tabla a partir de la posición del texto, y un PDF no «sabe» qué es una tabla. Estas son las correcciones más habituales:

**Encabezados repetidos.** Si la tabla ocupa varias páginas, el encabezado aparece al principio de cada hoja. Al unir todo en una sola hoja, borra los duplicados (un filtro por el texto del encabezado lo hace en segundos).

**Juntar todas las hojas en una.** Copia los datos de «Page 2», «Page 3»… y pégalos debajo de los de «Page 1». En Excel también puedes hacerlo con Power Query si lo haces a menudo.

**Celdas de varias líneas.** Un concepto largo que en el PDF ocupaba dos líneas aparecerá en dos filas. Únelas a mano o con una fórmula como `=A5&" "&A6` y borra la fila sobrante.

**Columnas desplazadas.** Si una fila tiene un hueco vacío (por ejemplo, un movimiento sin referencia), sus valores pueden correrse una columna a la izquierda. Ordena o filtra por la columna de importes y verás enseguida las filas que no encajan.

**Importes con coma decimal.** Revisa con atención las cifras escritas con formato europeo, como «1.234,56» o «12,50». El conversor puede interpretarlas con la convención inglesa (la coma como separador de miles), y entonces el valor no coincide con el del PDF. Compara siempre el total de la columna con el total que aparece en el documento antes de usar los datos.

## ¿Y si el PDF está escaneado?

Si el conversor te avisa de que no encuentra texto («No text found»), el PDF es una imagen. Haz esto:

1. Pásalo primero por [PDF OCR](/pdf-ocr/) (pantalla en inglés), eligiendo «Spanish» como idioma. Esta herramienta reconoce el texto y crea un PDF con texto seleccionable, además de un archivo .txt.
2. Sube ese PDF nuevo al conversor de PDF a Excel.

El reconocimiento de texto trabaja página a página y puede tardar unos segundos por página. Con un escaneo nítido y recto los resultados son mucho mejores; si el papel salió torcido o con sombras, revisa más a fondo las cifras.

## Ejemplos donde merece la pena

- **Extractos bancarios** para clasificar gastos por categorías o preparar la declaración.
- **Tarifas de proveedores** para comparar precios con otra lista.
- **Listados de alumnos o calificaciones** que llegan en PDF y necesitas ordenar o promediar.
- **Facturas con muchas líneas** para cotejar cantidades con un pedido.

## Privacidad

Extractos, nóminas o listas de clientes contienen datos delicados. El conversor de DoraPDF trabaja **en tu navegador**: el PDF se lee en tu dispositivo y no se sube a ningún servidor para convertirlo.

## Preguntas frecuentes

**¿Puedo convertir PDF a Excel gratis y sin registrarme?**
Sí. No necesitas cuenta y no hay marca de agua en el archivo.

**¿Se mantiene el formato de la tabla (colores, bordes)?**
No. Se extraen los datos, organizados en filas y columnas; colores, bordes y fuentes del PDF no se trasladan. Para un informe bonito, da formato en Excel una vez limpios los datos.

**¿Funciona con PDF escaneados?**
No directamente. Primero pásalos por la herramienta de OCR para que el texto sea reconocible y después conviértelos.

**¿Por qué cada página va en una hoja distinta?**
Para que puedas comprobar cada dato con su página original. Si quieres una sola tabla, copia y pega las hojas una debajo de otra.

**¿Puedo abrir el archivo en Google Sheets?**
Sí. Sube el .xlsx a Google Drive y ábrelo con Hojas de cálculo de Google.
"""),
dict(slug='heic-a-jpg-abrir-fotos-iphone-windows', lang='es', title='HEIC a JPG: cómo abrir las fotos del iPhone en Windows (y convertirlas gratis)', date='2026-11-17',
 desc='¿No se abren las fotos del iPhone en Windows? Convierte HEIC a JPG gratis en el navegador, varias a la vez, y evita el problema desde los ajustes del iPhone.',
 tools=['heic-to-jpg', 'heic-to-pdf', 'image-compressor'], md="""
Pasas las fotos del iPhone al ordenador, haces doble clic y Windows responde con un mensaje de error, una miniatura en blanco o una invitación a instalar algo desde la Microsoft Store. El archivo termina en **.HEIC** y ni el visor de fotos, ni el formulario de la web donde quieres subirlo, ni tu programa de edición parecen entenderlo.

La solución más directa es **convertir HEIC a JPG**. En esta guía te explicamos qué es ese formato, cómo pasar tus fotos a JPG gratis con el [conversor HEIC a JPG](/es/heic-a-jpg/) de DoraPDF y qué ajuste del iPhone evita el problema en el futuro.

## ¿Qué es un archivo HEIC y por qué el iPhone lo usa?

HEIC es el formato que el iPhone utiliza por defecto para guardar fotos. Su gran ventaja es que ocupa bastante menos espacio que un JPG con una calidad parecida, así que caben más fotos en el teléfono y en iCloud.

El inconveniente es la compatibilidad. Mientras que el JPG lo abre cualquier dispositivo desde hace décadas, el HEIC necesita soporte específico. En Windows suele hacer falta instalar extensiones adicionales, muchas páginas web no lo aceptan en sus formularios de subida y bastantes programas de edición más antiguos tampoco.

## Convertir HEIC a JPG gratis, paso a paso

1. Abre el [conversor HEIC a JPG](/es/heic-a-jpg/) en tu navegador.
2. Arrastra tus archivos .heic o .heif a la zona de carga, o selecciónalos. **Puedes añadir varios a la vez**.
3. Ajusta la **calidad** con el control deslizante si lo necesitas. Viene en 92, un valor alto que mantiene la foto prácticamente igual que el original.
4. Pulsa el botón de convertir.
5. Descarga los JPG. Cada uno conserva el nombre de su archivo original.

La conversión se hace en tu propio dispositivo, así que la primera vez puede tardar un poco más mientras el navegador carga el decodificador. Con muchas fotos de alta resolución, ten paciencia y no cierres la pestaña.

## ¿Qué calidad elegir?

- **92 (por defecto):** para guardar, imprimir o editar después. Apenas notarás diferencia con el original.
- **75-85:** buen equilibrio si vas a enviar las fotos por correo o subirlas a una web. Pesan bastante menos.
- **Por debajo de 70:** solo si el tamaño es lo que más importa; en fotos con cielos o degradados pueden aparecer bandas.

Un detalle útil: el JPG resultante a menudo pesa **más** que el HEIC original, porque HEIC comprime mejor. Si necesitas archivos ligeros, convierte primero y después pasa los JPG por el [compresor de imágenes](/es/comprimir-imagen/), que además puede reducir la resolución a un máximo de 1920 píxeles.

## Otras formas de abrir HEIC en Windows

Convertir no es la única opción, y según tu caso puede que prefieras otra:

**Instalar las extensiones de Microsoft.** En la Microsoft Store existen las «Extensiones de imagen HEIF» y, para algunos archivos, también hacen falta las «Extensiones de vídeo HEVC», que son de pago. Con ellas, la app Fotos abre los HEIC directamente. Es cómodo si ves fotos del iPhone a menudo, pero no resuelve el problema cuando tienes que subir la imagen a una web que solo acepta JPG.

**Pedir al iPhone que convierta al transferir.** En el iPhone, ve a **Ajustes → Fotos** y, al final, en «Transferir a Mac o PC», elige **Automático**. Así, cuando copias fotos por cable al ordenador, el iPhone las entrega en un formato compatible.

**Hacer que el iPhone dispare en JPG.** En **Ajustes → Cámara → Formatos**, elige **Más compatible**. A partir de ese momento las fotos nuevas se guardan en JPG. Ocuparán más espacio en el teléfono, así que piénsalo si vas justo de almacenamiento. Las fotos ya hechas seguirán siendo HEIC.

## Casos prácticos

**Subir una foto a un formulario oficial o a un portal de empleo.** Muchos formularios solo aceptan JPG o PNG. Convierte la foto, comprueba el tamaño máximo que piden y, si te pasas, comprímela.

**Mandar fotos a alguien con Windows o Android.** Si las envías por correo como archivo, conviértelas antes para que las pueda abrir sin instalar nada.

**Juntar fotos de documentos en un PDF.** Si fotografiaste un contrato o unos recibos con el iPhone, no hace falta pasar por JPG: [HEIC a PDF](/heic-to-pdf/) (pantalla en inglés) convierte las fotos directamente en un PDF.

**Necesitas transparencia o máxima calidad para diseño.** En ese caso, el formato adecuado es PNG; DoraPDF también tiene un conversor [HEIC a PNG](/heic-to-png/) (pantalla en inglés).

## Problemas frecuentes

**«El archivo no se convierte».** Comprueba que la extensión sea realmente .heic o .heif. Algunos archivos que vienen de apps de mensajería ya están en JPG aunque el nombre confunda.

**«La conversión va muy lenta».** Las fotos HEIC de los iPhone recientes tienen muchos megapíxeles. Convierte por tandas de diez o veinte en lugar de cien de golpe, sobre todo en móviles u ordenadores modestos.

**«Mi foto era una Live Photo».** Se convierte la imagen fija; la parte de vídeo corto no se incluye en el JPG.

## Tus fotos no se suben a ningún servidor

Las fotos personales son de lo más privado que tenemos en el móvil. En DoraPDF, la conversión de HEIC a JPG se hace **en el navegador de tu dispositivo**: las imágenes no se envían a ningún servidor ni se guardan en ningún sitio.

## Preguntas frecuentes

**¿Cómo convierto HEIC a JPG en Windows 10 u 11 sin instalar nada?**
Abre el conversor en el navegador, sube los archivos y descarga los JPG. No hace falta instalar extensiones ni programas.

**¿Se pierde calidad al pasar de HEIC a JPG?**
Con la calidad por defecto (92) la diferencia es prácticamente imperceptible. Si bajas mucho la calidad, sí se notará.

**¿Puedo convertir varias fotos HEIC a la vez?**
Sí, puedes añadir varios archivos en la misma tanda y descargarlos todos.

**¿Funciona desde el propio iPhone?**
Sí, puedes abrir la herramienta en Safari, elegir las fotos desde la app Archivos y descargar los JPG.
"""),
dict(slug='convertir-word-a-pdf-trabajos-solicitudes', lang='es', title='Convertir Word a PDF para trabajos y solicitudes: qué método usar en cada caso', date='2026-11-17',
 desc='Convertir Word a PDF gratis para entregar un trabajo o enviar una solicitud: desde Word, Google Docs o el móvil sin programas, y qué revisar antes de enviar.',
 tools=['word-to-pdf', 'pdf-merger', 'pdf-compressor'], md="""
Son las once de la noche, el trabajo de clase está terminado y el campus virtual solo acepta PDF. O estás rellenando una solicitud de beca, de empleo o de plaza y el formulario rechaza tu archivo .docx. En los dos casos necesitas **convertir Word a PDF**, y lo necesitas bien hecho: que se vea igual que en tu pantalla y que la persona (o el sistema) que lo reciba pueda leerlo sin problemas.

No hay un único método que sirva para todo. Aquí tienes los tres caminos principales, cuándo conviene cada uno y cómo usar el conversor gratuito [Convertir Word a PDF](/es/convertir-word-a-pdf/) de DoraPDF cuando no tienes Word a mano.

## Primero: ¿por qué PDF y no Word?

Un archivo de Word se ve distinto según el programa, la versión y las fuentes instaladas en cada ordenador. Un PDF, en cambio, «congela» el aspecto del documento. Por eso universidades, empresas y administraciones lo prefieren: el profesor ve exactamente lo que entregaste, sin márgenes movidos ni tablas descolocadas. Además, nadie puede modificar tu texto por accidente al abrirlo.

## Elige el método según tu situación

| Situación | Mejor método |
|---|---|
| Tienes Word o LibreOffice en tu ordenador | Exportar desde el propio programa |
| Escribes en Google Docs | Descargar como PDF desde Docs |
| Estás en el móvil, en un ordenador ajeno o sin programas | Conversor online en el navegador |

### Método 1: desde Word o LibreOffice (el más fiel)

- **Microsoft Word:** Archivo → Guardar como → en «Tipo», elige PDF. En Mac también funciona Archivo → Exportar.
- **LibreOffice Writer:** Archivo → Exportar como → Exportar directamente como PDF.

Este método conserva tus fuentes, encabezados, pies de página, números de página y márgenes, y el texto queda seleccionable. Es el que deberías usar para el currículum o para cualquier documento que vaya a pasar por un sistema automático.

### Método 2: desde Google Docs

Archivo → Descargar → Documento PDF (.pdf). Igual de fiel que el anterior y no necesitas instalar nada. Si te han pasado un .docx, puedes abrirlo en Google Drive con Docs y descargarlo como PDF.

### Método 3: convertir Word a PDF online, sin programas

Cuando estás con el móvil, en el ordenador de la biblioteca o simplemente no tienes ningún editor instalado, el camino más corto es el navegador:

1. Abre [Convertir Word a PDF](/es/convertir-word-a-pdf/).
2. Sube tu archivo **.docx** (el formato moderno de Word; los antiguos .doc no se aceptan).
3. Pulsa el botón de convertir y espera unos segundos.
4. Descarga el PDF, que tendrá el mismo nombre que tu documento.

## Qué conserva el conversor online y qué cambia

Conviene saberlo antes de entregar nada importante. El conversor de DoraPDF lee el contenido del documento y lo vuelve a componer en páginas A4:

- **Se mantiene:** el texto, los títulos y subtítulos, las negritas y cursivas, las listas, las tablas y las imágenes.
- **Cambia:** el texto se compone con una fuente estándar con serifa en lugar de la tuya, y no se trasladan encabezados, pies de página ni números de página. Los márgenes y saltos de página también son los de la herramienta, no los de tu documento.
- **Importante:** cada página del PDF se guarda como imagen. Se ve nítida en pantalla e impresa, pero el texto no se puede seleccionar ni buscar.

Para una entrega rápida o para compartir algo que se va a leer en pantalla, es perfecto. Para documentos donde el formato exacto o el texto seleccionable importan, usa el método 1 o 2 en cuanto puedas.

## Antes de entregar un trabajo de clase

- **Comprueba si tu universidad usa detección de plagio.** Herramientas de este tipo necesitan leer el texto del PDF. Un PDF donde las páginas son imágenes puede dar error o aparecer «vacío». Para estas entregas, exporta desde Word o Google Docs.
- **Revisa los saltos de página.** Abre el PDF y desplázate por todas las páginas: que ninguna tabla o imagen quede cortada y que la portada esté sola en su página.
- **Pon un nombre claro al archivo.** Algo como «Apellido_Nombre_Asignatura_Trabajo2.pdf» ayuda al profesor y evita confusiones.

## Antes de enviar una solicitud (empleo, beca, oposición)

- **Currículum y carta de presentación, siempre con texto seleccionable.** Muchos portales de empleo analizan el texto del CV para buscar palabras clave. Expórtalo desde tu editor.
- **Un solo archivo si lo piden así.** Si la convocatoria pide «toda la documentación en un PDF», convierte cada parte y júntalas después con [Unir PDF](/es/unir-pdf/), en el orden que indiquen las bases.
- **Vigila el límite de tamaño.** Si el portal admite, por ejemplo, 2 MB y tu archivo pesa más, redúcelo con [Comprimir PDF](/es/comprimir-pdf/). Empieza por el modo que mantiene el texto seleccionable.

## Problemas frecuentes

**«Mi archivo es .doc y no lo acepta».** Ábrelo en Word, LibreOffice o Google Docs y guárdalo como .docx, o expórtalo directamente a PDF desde ahí.

**«Las fuentes no se parecen a las mías».** Es normal con el conversor online, que usa una fuente estándar. Si la tipografía forma parte del diseño (un CV con estilo propio, por ejemplo), exporta desde tu programa.

**«Falta el número de página o el encabezado».** El conversor online no los incluye. Si son obligatorios en tu entrega, usa Word o Google Docs.

**«El PDF pesa demasiado».** Suele deberse a fotos grandes dentro del documento. Reduce las imágenes antes de insertarlas o comprime el PDF al final.

## Privacidad

Trabajos, solicitudes y currículums contienen datos personales. Con DoraPDF, la conversión se hace **en tu navegador**: el documento no se sube a un servidor para convertirlo y no se guarda en ningún sitio.

## Preguntas frecuentes

**¿Convertir Word a PDF es gratis?**
Sí, la herramienta es gratuita, sin registro y sin marca de agua.

**¿Puedo convertir Word a PDF desde el móvil?**
Sí. Abre la herramienta en el navegador del móvil, sube el .docx desde tus archivos y descarga el PDF.

**¿El PDF tendrá exactamente el mismo formato que mi Word?**
Con el conversor online se mantienen el texto, los títulos, las tablas y las imágenes, pero cambian la fuente y desaparecen encabezados y pies. Para un resultado idéntico, exporta desde Word o Google Docs.

**¿Qué método recomiendas para el currículum?**
Exportar desde tu editor de texto, porque el texto queda seleccionable y los portales de empleo pueden leerlo.
"""),
dict(slug='firmar-pdf-sin-imprimir-gratis', lang='es', title='Firmar un PDF sin imprimirlo: dibuja o escribe tu firma y colócala en segundos (gratis)', date='2026-11-17',
 desc='Cómo firmar un PDF sin imprimir ni escanear: dibuja tu firma con el dedo o el ratón, elige página y posición y descarga el PDF firmado. Gratis y sin registro.',
 tools=['sign-pdf', 'pdf-editor', 'pdf-merger'], md="""
Te mandan un contrato de alquiler, una autorización del colegio o una hoja de conformidad y te piden que la devuelvas «firmada». La reacción de siempre: imprimir, firmar con bolígrafo, escanear (o hacer una foto torcida) y volver a enviar. Hay una forma más rápida. Puedes **firmar un PDF sin imprimirlo** directamente en el navegador, desde el ordenador o el móvil, y tener el archivo firmado en menos de un minuto.

En esta guía verás cómo hacerlo gratis con la herramienta [Firmar PDF](/es/firmar-pdf/) de DoraPDF, qué tipo de firma obtienes realmente y cuándo necesitas otra cosa (por ejemplo, un certificado digital para trámites con la Administración).

## Qué hace exactamente la herramienta

La herramienta coloca una imagen de tu firma sobre una página del PDF. Esa firma la puedes crear de dos maneras:

- **Dibujándola** en un recuadro blanco con el ratón, el panel táctil o el dedo si estás en el móvil o la tableta.
- **Escribiendo tu nombre**, que se muestra con una tipografía manuscrita en cursiva.

Después eliges en qué página va (la última por defecto, o el número que indiques), si la quieres abajo a la derecha, abajo a la izquierda o abajo en el centro, y qué tamaño debe tener. El resultado se descarga como un nuevo archivo con «-signed» al final del nombre; el original no se modifica.

## Cómo firmar un PDF online paso a paso

1. Abre [Firmar PDF](/es/firmar-pdf/).
2. **Dibuja tu firma** en el recuadro. Si no te convence, pulsa «Clear» y repite. Si prefieres no dibujar, escribe tu nombre en el campo de texto.
3. **Sube el PDF** arrastrándolo a la zona de carga o seleccionándolo desde tu dispositivo.
4. En **Page** deja «last» para firmar la última página o escribe el número de la página que quieras (por ejemplo, 3).
5. En **Position** elige la esquina o el centro de la parte inferior.
6. Ajusta el **tamaño** con el control deslizante. Va del 10 % al 50 % del ancho de la página; alrededor del 20-25 % suele quedar natural en un A4.
7. Pulsa **Sign PDF** y descarga el archivo.

Antes de enviarlo, ábrelo y comprueba que la firma no tapa ningún texto. Si queda encima de algo, vuelve a empezar con otra posición o un tamaño menor.

## Firmar un PDF desde el móvil

En el móvil la experiencia es incluso mejor, porque firmas con el dedo y el trazo sale más parecido a tu firma de papel. Algunos consejos:

- Gira el teléfono en horizontal para tener más espacio en el recuadro de firma.
- Firma despacio y de una sola vez; los trazos rápidos en pantallas pequeñas salen temblorosos.
- Si el PDF te llegó por WhatsApp o por correo, guárdalo primero en «Archivos» (iPhone) o en «Descargas» (Android) para poder seleccionarlo desde el navegador.

El PDF firmado se guarda en la carpeta de descargas del navegador y desde ahí lo puedes adjuntar o reenviar.

## Trucos para que la firma quede profesional

**Usa un trazo limpio.** La tinta es de color azul oscuro y el fondo de la firma es transparente, así que no aparece un rectángulo blanco sobre el documento. Aun así, una firma pequeña y nítida queda mejor que una enorme.

**Añade fecha y nombre si te los piden.** Muchos documentos piden «Nombre, fecha y firma». Con el [Editor de PDF](/pdf-editor/) (pantalla en inglés) puedes hacer clic en cualquier punto de la página y escribir el texto que falte, justo donde va la línea.

**Varios firmantes.** Si dos personas deben firmar, la primera firma y envía el archivo resultante; la segunda lo vuelve a subir y coloca su firma en otra posición (por ejemplo, abajo a la izquierda).

**Documentos de varias partes.** Si te han mandado el contrato y los anexos por separado, únelos primero con [Unir PDF](/es/unir-pdf/) y firma después la página final.

## Problemas frecuentes y cómo resolverlos

**«La línea de firma está en mitad de la página, no abajo».** La herramienta solo coloca la firma en la parte inferior de la página (izquierda, centro o derecha). Si el documento exige firmar en un punto concreto más arriba, lo más práctico es firmar abajo y, si hace falta, indicar con el editor de PDF «Firmado al pie». Si el formato es estricto, consulta con quien te lo envía.

**«Necesito firmar varias páginas».** Cada pasada firma una página. Para rubricar varias, repite el proceso con el archivo ya firmado, cambiando el número de página cada vez.

**«El PDF está protegido con contraseña».** Si el archivo es tuyo y conoces la contraseña, primero quítasela con [Desbloquear PDF](/es/desbloquear-pdf/) y después fírmalo.

**«La firma escrita no parece manuscrita».** La tipografía cursiva depende de las fuentes instaladas en tu dispositivo, así que puede verse distinta en cada ordenador. Si te importa el aspecto, dibújala.

## ¿Es válida legalmente una firma así?

Conviene ser claros. Lo que obtienes es una **firma electrónica simple**: una imagen de tu firma insertada en el documento. En la Unión Europea, el reglamento eIDAS reconoce este tipo de firma y no se le puede negar valor solo por ser electrónica, y para muchísimas situaciones del día a día (una autorización escolar, un parte interno, la aceptación de un presupuesto, un contrato privado entre particulares) es suficiente y se usa constantemente.

Lo que **no** es: una firma electrónica avanzada o cualificada basada en certificado. Para trámites con la Agencia Tributaria, la Seguridad Social o cualquier sede electrónica de la Administración, te pedirán firmar con tu certificado digital, el DNI electrónico o Cl@ve, normalmente con aplicaciones oficiales como AutoFirma. En contratos de mucho valor o si tienes dudas, pregunta a la otra parte qué tipo de firma aceptan.

## Privacidad: el documento no sale de tu dispositivo

Un contrato o una autorización suelen llevar tu nombre, tu dirección y a veces tu DNI. Por eso importa saber dónde se procesa. En DoraPDF, la firma y el PDF se procesan **en tu navegador**: el archivo no se sube a ningún servidor para firmarlo. Cuando cierras la pestaña, no queda copia en ningún sitio más que en tu propia carpeta de descargas.

## Preguntas frecuentes

**¿Puedo firmar un PDF gratis sin registrarme?**
Sí. La herramienta es gratuita y no necesitas crear una cuenta ni instalar ningún programa.

**¿Funciona en iPhone y Android?**
Sí, funciona en el navegador del móvil. Puedes dibujar la firma con el dedo directamente en la pantalla.

**¿Se guarda mi firma para la próxima vez?**
No. La firma se crea en el momento y no se almacena. Si firmas a menudo, tardas unos segundos en volver a dibujarla.

**¿Puedo elegir exactamente dónde va la firma?**
Puedes elegir la página, el tamaño y si va abajo a la izquierda, en el centro o a la derecha. No se puede arrastrar a un punto libre de la página.

**¿Sirve para presentar documentos en una sede electrónica?**
Normalmente no: la Administración pide firma con certificado digital o Cl@ve. Para documentos privados y del día a día, sí te sirve.
"""),
dict(slug='bewerbungsunterlagen-pdf-erstellen-anleitung', lang='de', title='Bewerbungsunterlagen als PDF erstellen: Schritt für Schritt zur Bewerbung in einer Datei', date='2026-11-15',
 desc='Bewerbungsunterlagen als PDF erstellen: Anschreiben, Lebenslauf und Zeugnisse in eine PDF, richtig sortiert und unter dem Größenlimit. Kostenlos im Browser.',
 tools=['pdf-merger', 'pdf-compressor', 'word-to-pdf', 'scan-to-pdf'], md="""
Die Stellenanzeige ist perfekt, das Anschreiben steht – und dann verlangt das Online-Portal „alle Unterlagen in einer PDF-Datei, maximal 5 MB". Spätestens jetzt merken viele, dass zwischen einem guten Lebenslauf und einer guten Bewerbung noch ein technischer Schritt liegt.

In dieser Anleitung erfahren Sie, wie Sie **Bewerbungsunterlagen als PDF erstellen**: welche Datei woher kommt, in welcher Reihenfolge alles zusammengehört und wie Sie die fertige Bewerbung als eine PDF unter das Limit bekommen. Alle DoraPDF-Werkzeuge, die dabei vorkommen, sind kostenlos, funktionieren ohne Anmeldung und verarbeiten Ihre Dateien direkt im Browser.

## Schritt 1: Erst sammeln, dann umwandeln

Eine typische Bewerbungsmappe besteht aus drei Arten von Dokumenten, und jede braucht einen etwas anderen Weg zur PDF:

| Dokument | Liegt meist vor als | Weg zur PDF |
|---|---|---|
| Anschreiben, Lebenslauf | Word- oder Google-Docs-Datei | Export aus dem Schreibprogramm |
| Arbeitszeugnisse, Abschlusszeugnis | Papier | Scannen oder abfotografieren |
| Zertifikate, Bescheinigungen | PDF oder Foto | übernehmen oder umwandeln |

Legen Sie sich einen Ordner an und speichern Sie dort jede Datei einzeln als PDF ab. Zusammengefügt wird erst ganz am Ende.

## Schritt 2: Anschreiben und Lebenslauf als PDF speichern

Für Anschreiben und Lebenslauf ist der direkte Export aus dem Schreibprogramm der beste Weg, denn dabei bleibt der Text als echter, auswählbarer Text erhalten. Viele Unternehmen lesen Bewerbungen mit einem Bewerbermanagementsystem ein, das Ihren Lebenslauf nach Stichworten durchsucht – das klappt nur, wenn der Text nicht als Bild in der PDF steckt.

- **Microsoft Word:** Datei → Speichern unter → Dateityp „PDF".
- **LibreOffice:** Datei → Exportieren als → Als PDF exportieren.
- **Google Docs:** Datei → Herunterladen → PDF-Dokument.

Haben Sie gerade kein Schreibprogramm zur Hand, etwa am Handy oder an einem fremden Rechner, hilft [Word in PDF umwandeln](/de/word-in-pdf-umwandeln/). Das Tool nimmt eine .docx-Datei an und erstellt daraus eine PDF im A4-Format. Gut zu wissen: Es übernimmt Text, Überschriften, Tabellen und Bilder, setzt die Seiten aber mit einer Standardschrift neu und speichert sie als Bild. Für eine schnelle Notlösung ist das ideal; für den Lebenslauf in einer wichtigen Bewerbung lohnt sich der Export aus Word, sobald Sie wieder am eigenen Rechner sitzen.

Wer noch gar keinen Lebenslauf hat, kann mit dem [Lebenslauf-Generator](/resume-builder/) (Tool-Seite auf Englisch) einen schlichten Lebenslauf ausfüllen und direkt als PDF herunterladen.

## Schritt 3: Zeugnisse scannen – ohne Scanner

Kein Scanner im Haus? Das Smartphone reicht. Mit [Scan to PDF](/scan-to-pdf/) (Tool-Seite auf Englisch) fotografieren Sie jedes Zeugnis, ziehen die Ecken auf die Blattkanten, damit das Bild gerade und ohne Tischplatte erscheint, wählen einen Scan-Filter und speichern alle Seiten als eine mehrseitige PDF.

Ein paar Tipps für saubere Scans:

- Bei Tageslicht fotografieren, ohne Blitz – der erzeugt helle Flecken.
- Das Blatt auf eine dunkle, ruhige Fläche legen, dann erkennt man die Kanten leichter.
- Das Handy parallel zum Blatt halten, nicht schräg.
- Mehrseitige Zeugnisse komplett scannen, auch die Seite mit Unterschrift.

## Schritt 4: Die richtige Reihenfolge

Personalabteilungen erwarten eine vertraute Struktur. Bewährt hat sich:

1. Anschreiben
2. Lebenslauf
3. Arbeitszeugnisse, das aktuellste zuerst
4. Studien- oder Ausbildungsabschluss, dann Schulabschluss
5. Weitere Nachweise wie Sprachzertifikate oder Weiterbildungen

Ein Deckblatt ist optional. Wenn Sie eines nutzen, gehört es ganz nach vorne – manche lassen es bei Online-Bewerbungen inzwischen weg, weil das Anschreiben ohnehin die erste Seite ist.

Benennen Sie die Dateien im Ordner so, dass die Reihenfolge schon im Dateinamen steht: `01-anschreiben.pdf`, `02-lebenslauf.pdf`, `03-zeugnis-firma-a.pdf` usw. Das erspart Ihnen im nächsten Schritt Sortierarbeit.

## Schritt 5: Bewerbung als eine PDF zusammenfügen

1. Öffnen Sie [PDF zusammenfügen](/de/pdf-zusammenfuegen/).
2. Fügen Sie die Dateien in der gewünschten Reihenfolge hinzu. Das Tool verbindet sie genau in der Reihenfolge, in der sie in der Liste stehen.
3. Prüfen Sie die Liste. Eine falsche Datei entfernen Sie mit dem ✕ und fügen sie an der richtigen Stelle neu hinzu.
4. Klicken Sie auf **Merge PDFs ✦** (die Schaltflächen sind auf Englisch) und laden Sie die Datei herunter.
5. Benennen Sie `merged.pdf` um, zum Beispiel in `Bewerbung_Lena_Schmidt_Projektmanagerin.pdf`.

Alle Seiten werden unverändert übernommen. Auswählbarer Text bleibt auswählbar.

## Schritt 6: Bewerbung PDF zu groß? So kommen Sie unter das Limit

Wie groß eine Bewerbung sein darf, steht meist in der Stellenanzeige oder im Portal. Häufig liegt die Grenze bei wenigen Megabyte. Die Übeltäter sind fast immer die Scans, nicht Anschreiben und Lebenslauf.

Deshalb der wichtigste Tipp: **Verkleinern Sie zuerst die Scans und fügen Sie erst danach zusammen.** In [PDF verkleinern](/de/pdf-verkleinern/) gibt es zwei Modi:

- **Smart** speichert die PDF optimiert neu. Der Text bleibt auswählbar, die Ersparnis ist bei Scans aber oft gering.
- **Strong** wandelt jede Seite in ein komprimiertes Bild um. Bei Scans spart das am meisten, und weil ein Scan ohnehin ein Bild ist, verlieren Sie dabei nichts. Wählen Sie die Bildqualität „Balanced"; „Smallest" nur, wenn es wirklich eng wird.

Würden Sie dagegen die fertige Mappe mit „Strong" verkleinern, würde auch Ihr Lebenslauf zum Bild. Genau das möchten Sie vermeiden. Mit der Reihenfolge „Scans verkleinern → zusammenfügen" bekommen Sie beides: eine kleine Datei und durchsuchbaren Text in Anschreiben und Lebenslauf.

## Typische Fehler vor dem Absenden

- **Leere oder doppelte Seiten.** Blättern Sie die fertige PDF einmal komplett durch.
- **Quer liegende Seiten.** Ein schief eingescanntes Zertifikat drehen Sie vorher mit [PDF drehen](/rotate-pdf/) (Tool-Seite auf Englisch).
- **Passwortgeschützte Zertifikate.** Manche Anbieter verschicken Nachweise mit Passwort. Viele Bewerbungsportale können solche Dateien nicht verarbeiten, entfernen Sie den Schutz vorher mit [PDF-Passwort entfernen](/de/pdf-passwort-entfernen/).
- **Unklarer Dateiname.** „Scan_0045.pdf" landet schnell im falschen Ordner. Name und Position im Dateinamen helfen der Personalabteilung.

## Datenschutz

Zeugnisse und Lebenslauf enthalten Geburtsdatum, Adresse und Ihre berufliche Geschichte. Bei DoraPDF bleiben diese Daten auf Ihrem Gerät: Umwandeln, Zusammenfügen und Verkleinern laufen im Browser, die Dateien werden nicht auf einen Server hochgeladen.

## Häufige Fragen

### Sollte ich die Bewerbung als eine PDF oder als mehrere Dateien schicken?

Wenn das Unternehmen nichts anderes vorgibt, ist eine einzige PDF die praktischste Lösung: Die Personalabteilung muss nur eine Datei öffnen und sieht alles in der richtigen Reihenfolge. Verlangt ein Portal getrennte Uploads, halten Sie sich daran.

### Wie groß darf eine Bewerbung per E-Mail sein?

Eine feste Regel gibt es nicht. Viele Bewerbungsratgeber empfehlen, unter etwa 5 MB zu bleiben. Gibt die Stellenanzeige einen Wert vor, gilt dieser.

### Kann ich Bewerbungsunterlagen am Handy als PDF erstellen?

Ja. Zeugnisse scannen Sie mit Scan to PDF, Word-Dateien wandeln Sie mit Word in PDF um, und das Zusammenfügen funktioniert im Handy-Browser genauso wie am PC.

### Bleibt der Text im Lebenslauf durchsuchbar?

Ja, solange Sie den Lebenslauf direkt aus Word, LibreOffice oder Google Docs als PDF speichern und die fertige Mappe nicht im Modus „Strong" verkleinern.
"""),
dict(slug='rechnung-erstellen-kostenlos-mwst-pdf', lang='de', title='Rechnung erstellen kostenlos: Mit MwSt. als PDF, ohne Anmeldung und ohne Software', date='2026-11-15',
 desc='Rechnung erstellen kostenlos und ohne Anmeldung: Pflichtangaben, MwSt. richtig ausweisen, Kleinunternehmer-Hinweis und PDF in A4 – direkt im Browser.',
 tools=['invoice-generator', 'sales-tax-calculator', 'receipt-generator'], md="""
Der erste Auftrag als Freelancer, ein gelegentlicher Nebenjob oder einfach eine Rechnung für den Verkauf einer gebrauchten Kamera an eine Firma: Eine Buchhaltungssoftware mit Monatsabo lohnt sich dafür oft nicht. Sie möchten nur schnell eine saubere **Rechnung erstellen, kostenlos** und als PDF zum Verschicken.

Genau dafür gibt es den [Rechnungsgenerator von DoraPDF](/invoice-generator/). Sie füllen ein Formular aus, das Tool rechnet Zwischensumme, Mehrwertsteuer und Gesamtbetrag, und Sie laden eine fertige Rechnung im A4-Format herunter. Ohne Anmeldung, ohne Installation. Die Bedienoberfläche und die Beschriftungen auf der Rechnung sind auf Englisch – wie Sie damit eine Rechnung erstellen, die deutschen Anforderungen genügt, erklärt dieser Artikel.

## Was muss auf eine Rechnung? Die Pflichtangaben

Nach dem Umsatzsteuergesetz (§ 14 UStG) gehören auf eine vollständige Rechnung:

- vollständiger Name und Anschrift von Ihnen und vom Kunden
- Ihre Steuernummer oder Umsatzsteuer-Identifikationsnummer
- Rechnungsdatum
- eine fortlaufende, einmalige Rechnungsnummer
- Menge und Art der Leistung oder Ware
- Zeitpunkt bzw. Zeitraum der Leistung
- Nettobetrag, Steuersatz und Steuerbetrag – oder ein Hinweis, warum keine Umsatzsteuer berechnet wird

Für **Kleinbetragsrechnungen bis 250 € brutto** gelten vereinfachte Regeln; dort reichen unter anderem Name und Anschrift des Leistenden, Datum, Leistung sowie Bruttobetrag und Steuersatz.

Dieser Überblick ersetzt keine Steuerberatung. Wenn Sie unsicher sind, ob Ihre Rechnung alle Angaben enthält, fragen Sie im Zweifel Ihr Steuerbüro.

## So füllen Sie den Rechnungsgenerator aus

Das Formular hat englische Feldnamen. Hier die Übersetzung und was Sie wo eintragen:

1. **From** – Ihr Name oder Firmenname.
2. **Invoice #** – die Rechnungsnummer. Das Tool schlägt eine zufällige Nummer wie `INV-48213` vor. Ersetzen Sie sie durch Ihre eigene fortlaufende Nummer, zum Beispiel `2026-014`.
3. **Date** – Rechnungsdatum, ist mit dem heutigen Tag vorbelegt.
4. **Due date** – Zahlungsziel, optional.
5. **Your details** – Ihre Anschrift, E-Mail, Telefon **und Ihre Steuernummer bzw. USt-IdNr.** Ein eigenes Feld für die Steuernummer gibt es nicht, deshalb gehört sie hierher.
6. **Bill to** – Name und Anschrift des Kunden.
7. **Positionen (Item, Qty, Price)** – Beschreibung, Menge und Einzelpreis netto. Löschen Sie die beiden Beispielpositionen mit dem ✕ und fügen Sie mit **+ Add item** eigene hinzu.
8. **Currency** – wählen Sie **EUR**.
9. **Tax %** – den Mehrwertsteuersatz, also meist 19 oder 7.
10. **Notes** – Platz für Bankverbindung (IBAN), Zahlungsbedingungen und den Leistungszeitraum.
11. **Brand color** – die Akzentfarbe Ihrer Rechnung.

Zum Schluss klicken Sie auf **Download invoice PDF ✦**. Die Datei wird nach der Rechnungsnummer benannt, also etwa `2026-014.pdf`.

## Beispiel: Rechnung einer Freelancerin mit 19 % MwSt.

Eine Grafikdesignerin stellt einem Café im Oktober zwei Leistungen in Rechnung:

- Logo-Entwicklung, Menge 1, Preis 900
- Speisekarte gestalten, Menge 2 Seiten, Preis 150

Das Tool rechnet: Zwischensumme (**Subtotal**) 1,200.00 €, darauf **Tax (19%)** 228.00 €, Gesamtbetrag **Total** 1,428.00 €. Beachten Sie, dass die Beträge im englischen Zahlenformat erscheinen, also mit Punkt vor den Cent.

In **Notes** schreibt sie: „Leistungszeitraum: Oktober 2026. Zahlbar innerhalb von 14 Tagen ohne Abzug auf IBAN DE… Vielen Dank für den Auftrag!" Damit ist auch der Leistungszeitpunkt erfasst, für den es kein eigenes Feld gibt.

Möchten Sie einen Bruttopreis vorher in netto und Steuer zerlegen, hilft der [Mehrwertsteuer-Rechner](/sales-tax-calculator/) (Tool-Seite auf Englisch): Er rechnet Steuer auf einen Preis auf oder aus einem Bruttopreis heraus.

## Kleinunternehmer: Rechnung ohne Mehrwertsteuer

Als Kleinunternehmer nach § 19 UStG weisen Sie keine Umsatzsteuer aus. Im Rechnungsgenerator setzen Sie dafür **Tax %** auf 0. Die Steuerzeile erscheint dann gar nicht auf der Rechnung. Wichtig ist der Hinweis, warum keine Steuer berechnet wird. Schreiben Sie in **Notes** zum Beispiel:

> Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.

Ob Sie die Kleinunternehmerregelung nutzen dürfen, hängt von Ihrem Umsatz ab. Seit 2025 liegen die Grenzen bei 25.000 € im Vorjahr und 100.000 € im laufenden Jahr.

## Drei Stolperfallen und wie Sie sie umgehen

**Rabatt richtig abziehen.** Das Feld **Discount** zieht einen festen Betrag erst *nach* der Steuer vom Gesamtbetrag ab. Die Mehrwertsteuer wird dann vom vollen Betrag berechnet, und das passt nicht zu einem deutschen Rabatt. Besser: Tragen Sie den Rabatt als eigene Position mit negativem Preis ein, etwa „Stammkundenrabatt", Menge 1, Preis -100. So sinkt die Zwischensumme, und die Steuer wird korrekt vom reduzierten Betrag berechnet.

**Zwei Steuersätze.** Es gibt nur ein Feld für den Steuersatz. Verkaufen Sie Leistungen mit 19 % und Waren mit 7 % an denselben Kunden, schreiben Sie zwei getrennte Rechnungen oder nutzen Sie dafür ein Programm, das mehrere Steuersätze aufschlüsselt.

**Fortlaufende Nummern.** Das Tool speichert keine Rechnungen und zählt nicht mit. Führen Sie eine einfache Liste, zum Beispiel in einer Tabelle, damit keine Nummer doppelt vergeben wird. Bewahren Sie jede heruntergeladene PDF auf – für Rechnungen gelten mehrjährige Aufbewahrungsfristen.

## PDF-Rechnung oder E-Rechnung?

An Privatkunden können Sie eine Rechnung weiterhin als PDF per E-Mail schicken. Zwischen Unternehmen wird in Deutschland schrittweise die strukturierte E-Rechnung (etwa XRechnung oder ZUGFeRD) Pflicht. Für eine Übergangszeit sind PDF-Rechnungen an Firmen noch erlaubt; Kleinunternehmer sind vom Ausstellen von E-Rechnungen ausgenommen. Eine PDF aus dem DoraPDF-Generator ist eine klassische Rechnung, keine E-Rechnung. Wer regelmäßig an Unternehmen fakturiert, sollte die Fristen im Blick behalten.

## Datenschutz

Kundendaten, Preise, Ihre IBAN: Das alles bleibt auf Ihrem Gerät. Die Rechnung wird direkt in Ihrem Browser als PDF erzeugt, an DoraPDF wird nichts übertragen. Das heißt aber auch: Nach dem Schließen des Tabs sind die Eingaben weg. Speichern Sie die PDF also sofort.

Für einfache Barverkäufe, etwa auf dem Flohmarkt oder im Kleingewerbe, gibt es außerdem den [Quittungsgenerator](/receipt-generator/) (Tool-Seite auf Englisch) im schmalen Kassenbon-Format.

## Häufige Fragen

### Kann ich eine Rechnung ohne Anmeldung erstellen?

Ja. Sie öffnen den Rechnungsgenerator, füllen ihn aus und laden die PDF herunter. Ein Konto ist nicht nötig.

### Darf eine Rechnung auf Englisch sein?

Eine Rechnung muss nicht zwingend auf Deutsch sein, solange alle Pflichtangaben enthalten sind. Das Finanzamt kann bei Bedarf eine Übersetzung verlangen. Bei Unsicherheit klären Sie das mit Ihrem Steuerbüro oder mit dem Kunden.

### Wo trage ich die Steuernummer ein?

Im Feld **Your details**, zusammen mit Ihrer Anschrift. Sie erscheint dann oben links unter Ihrem Namen.

### Welches Papierformat hat die Rechnung?

A4. Sie können die PDF also direkt drucken oder per E-Mail versenden.
"""),
dict(slug='bild-komprimieren-ohne-qualitaetsverlust', lang='de', title='Bild komprimieren ohne sichtbaren Qualitätsverlust: Fotos für E-Mail, Website und Upload verkleinern', date='2026-11-15',
 desc='Bild komprimieren kostenlos und online: JPG und PNG verkleinern, ohne dass man es sieht. Mehrere Fotos auf einmal, Dateien bleiben im Browser.',
 tools=['image-compressor', 'image-resizer', 'png-to-jpg'], md="""
Ein Handyfoto hat heute schnell 4 bis 8 MB. Für das Fotoalbum ist das wunderbar, für fast alles andere zu viel: Das E-Mail-Postfach streikt bei zwanzig Urlaubsbildern, das Formular beim Amt nimmt nur Dateien bis 1 MB an, und auf der eigenen Website lädt die Galerie gefühlt ewig.

Die Lösung: das **Bild komprimieren**. Mit dem kostenlosen [Bildkompressor von DoraPDF](/de/bild-komprimieren/) verkleinern Sie JPG- und PNG-Dateien direkt im Browser, auch mehrere auf einmal und ohne Anmeldung. Wie Sie dabei die Dateigröße stark senken, ohne dass man auf dem Bildschirm einen Unterschied sieht, zeigt dieser Artikel.

## Geht das wirklich „ohne Qualitätsverlust"?

Ehrlich gesagt: Bei JPG-Kompression gehen immer Bildinformationen verloren. Das Entscheidende ist, ob man es *sieht*. Und hier gibt es gute Nachrichten, denn ein typisches Handyfoto enthält weit mehr Informationen, als ein Bildschirm darstellen kann.

Zwei Stellschrauben bestimmen die Dateigröße:

1. **Die Pixelmaße.** Ein Foto mit 4000 × 3000 Pixeln hat zwölf Millionen Bildpunkte. Ein Laptop-Bildschirm zeigt in voller Breite rund 1900 Pixel. Wird das Bild auf 1920 Pixel Breite verkleinert, sieht es am Bildschirm genauso scharf aus, hat aber nur noch etwa ein Viertel der Pixel.
2. **Die Kompressionsstärke.** Sie legt fest, wie stark feine Details zusammengefasst werden. Bei mittlerer Stärke ist der Unterschied auf normalen Bildschirmen kaum zu erkennen.

Die Kombination aus beidem bringt die größte Ersparnis. Allein die Stärke hochzudrehen, bringt weniger und erzeugt eher sichtbare Artefakte.

## Anleitung: Bild komprimieren in drei Schritten

1. Öffnen Sie [Bild komprimieren](/de/bild-komprimieren/) und ziehen Sie ein oder mehrere Bilder in das Feld.
2. Wählen Sie zwei Einstellungen (die Bedienung ist auf Englisch):
   - **Strength:** *Light* (leicht), *Balanced* (ausgewogen, voreingestellt) oder *Strong* (stark).
   - **Resize:** *Original size* oder eine maximale Kantenlänge von 2560, 1920, 1280 oder 800 Pixeln. Voreingestellt sind 1920 Pixel.
3. Klicken Sie auf **Compress ✦** und laden Sie die Ergebnisse herunter.

Neben jeder Datei steht, um wie viel Prozent sie kleiner geworden ist. Die neuen Dateien heißen wie das Original mit dem Zusatz `-small`, Ihre Originale bleiben also unangetastet.

## Welche Einstellung für welchen Zweck?

| Zweck | Strength | Resize |
|---|---|---|
| Fotos per E-Mail an Familie | Balanced | 1920 px |
| Bilder für Website oder Blog | Balanced | 1920 oder 1280 px |
| Upload-Formular mit striktem Limit (z. B. 500 KB) | Balanced oder Strong | 1280 px |
| Profilbild, Vorschaubild | Balanced | 800 px |
| Foto, das noch gedruckt werden soll | Light | Original size |

Für den Druck sollten Sie die Pixelmaße nicht reduzieren. Ein Foto im Format 10 × 15 cm braucht deutlich mehr Pixel als ein Bild für den Bildschirm.

## Bild auf eine bestimmte Größe in KB verkleinern

Viele Portale schreiben eine Obergrenze vor, etwa „maximal 200 KB". Der Kompressor arbeitet mit festen Stufen, nicht mit einem Ziel in Kilobyte. So kommen Sie trotzdem schnell ans Ziel:

1. Starten Sie mit *Balanced* und 1280 px.
2. Ist die Datei noch zu groß, wählen Sie 800 px.
3. Reicht das immer noch nicht, wechseln Sie auf *Strong*.

Wenn Sie exakte Pixelmaße brauchen, etwa 600 × 800 Pixel für ein Bewerbungsfoto, bringen Sie das Bild zuerst mit [Bildgröße ändern](/image-resizer/) (Tool-Seite auf Englisch) auf das gewünschte Maß und komprimieren es danach.

## Was passiert mit PNG-Dateien?

JPG-Fotos werden wieder als JPG gespeichert. **PNG-Bilder werden als WebP gespeichert**, weil WebP deutlich kleiner ist und Transparenz behält. Ein Logo mit durchsichtigem Hintergrund bleibt also durchsichtig.

WebP wird von allen aktuellen Browsern und den meisten Content-Management-Systemen unterstützt. Verlangt ein Formular ausdrücklich JPG, wandeln Sie das PNG vorher mit [PNG in JPG umwandeln](/de/png-in-jpg-umwandeln/) um und komprimieren dann das JPG.

iPhone-Fotos im HEIC-Format wandeln Sie am besten vorher mit [HEIC in JPG umwandeln](/de/heic-in-jpg-umwandeln/) um.

## Wenn das Ergebnis nicht passt

**„0% smaller".** Das Bild war schon stark komprimiert, etwa ein Foto aus WhatsApp. Hier hilft nur eine kleinere Pixelgröße.

**Das Bild wirkt unscharf.** Die maximale Kantenlänge war zu klein für den Zweck. Wählen Sie die nächstgrößere Stufe.

**Kanten in Grafiken sehen ausgefranst aus.** Bei Screenshots mit Text oder Grafiken mit harten Linien macht sich JPG-Kompression eher bemerkbar als bei Fotos. Nehmen Sie *Light* oder speichern Sie solche Grafiken als PNG.

**Ein transparenter Bereich ist weiß geworden.** Das passiert, wenn das Bild kein PNG war, zum Beispiel ein GIF mit Transparenz. Bei der Umwandlung in JPG wird Transparenz durch Weiß ersetzt.

## Datenschutz

Ihre Fotos werden nicht hochgeladen. Der Bildkompressor arbeitet vollständig in Ihrem Browser auf Ihrem Gerät. Das gilt auch für private Familienfotos oder eingescannte Ausweisdokumente, die Sie für ein Formular verkleinern müssen.

## Häufige Fragen

### Kann ich mehrere Bilder gleichzeitig komprimieren?

Ja. Wählen Sie beliebig viele Bilder aus oder ziehen Sie einen ganzen Stapel in das Feld. Alle werden mit denselben Einstellungen verarbeitet.

### Funktioniert das am Handy?

Ja, der Bildkompressor läuft in jedem aktuellen Browser, auch auf Android und iPhone.

### Wird das Originalbild überschrieben?

Nein. Sie bekommen eine neue Datei mit dem Zusatz `-small` im Namen. Das Original bleibt unverändert.

### Was ist besser: Größe ändern oder komprimieren?

Für die größte Ersparnis beides. Die Pixelmaße zu verkleinern, bringt meist am meisten, die Kompressionsstärke holt den Rest heraus.
"""),
dict(slug='pdf-passwort-entfernen-eigene-pdf-entsperren', lang='de', title='PDF-Passwort entfernen: Eigene PDF entsperren – kostenlos und ohne Programm', date='2026-11-15',
 desc='PDF-Passwort entfernen ohne Programm: Lohnabrechnung oder Kontoauszug einmal entsperren und ohne Passwort speichern. Kostenlos, die Datei bleibt im Browser.',
 tools=['unlock-pdf', 'pdf-ocr', 'protect-pdf'], md="""
Die Gehaltsabrechnung kommt jeden Monat als PDF mit Passwort, die Kontoauszüge der Bank ebenfalls, und die Handyrechnung lässt sich nur mit Kundennummer öffnen. Das ist sinnvoll, solange die Datei per E-Mail unterwegs ist. Auf dem eigenen Rechner wird es lästig: Jedes Öffnen verlangt das Passwort, und manche Programme oder Upload-Portale – etwa beim Vermieter oder bei der Steuersoftware – lehnen geschützte Dateien ganz ab.

Mit dem Tool [PDF-Passwort entfernen](/de/pdf-passwort-entfernen/) geben Sie das Passwort einmal ein und speichern eine Kopie ohne Schutz. Kostenlos, ohne Programm und ohne Anmeldung. Wichtig vorab: Das Tool entsperrt **PDFs, deren Passwort Sie kennen**. Vergessene Passwörter knackt es nicht – und das ist auch richtig so.

## Zwei Arten von PDF-Schutz

PDFs können auf zwei verschiedene Arten geschützt sein, und das erklärt, warum sich manche Dateien unterschiedlich verhalten:

- **Öffnungspasswort.** Ohne Passwort lässt sich die Datei gar nicht anzeigen. Das ist der typische Fall bei Lohnabrechnungen und Kontoauszügen.
- **Rechtebeschränkung.** Die Datei öffnet sich normal, aber Drucken, Kopieren oder Bearbeiten ist gesperrt. Oft merkt man das erst, wenn man einen Absatz markieren möchte.

Das DoraPDF-Tool hilft in beiden Fällen. Beim Öffnungspasswort tragen Sie das Passwort ein. Bei einer reinen Rechtebeschränkung lässt sich die PDF oft auch mit leerem Passwortfeld verarbeiten.

## Anleitung: PDF entsperren in vier Schritten

1. Öffnen Sie [PDF-Passwort entfernen](/de/pdf-passwort-entfernen/).
2. Wählen Sie die geschützte PDF aus oder ziehen Sie sie in das Feld.
3. Tragen Sie das Passwort in das Feld **Password** ein.
4. Klicken Sie auf **Unlock ✦** (die Bedienung ist auf Englisch) und laden Sie die Datei herunter. Sie heißt wie das Original mit dem Zusatz `-unlocked`.

Erscheint die Meldung **„Wrong password"**, stimmt das Passwort nicht. Achten Sie auf Groß- und Kleinschreibung und auf das Format: Viele Arbeitgeber und Banken verwenden das Geburtsdatum, aber mal als `01011990`, mal als `01.01.1990`. Oft steht der Aufbau des Passworts in der Begleit-E-Mail.

## Gut zu wissen: Die Seiten werden neu aufgebaut

Damit die neue Datei wirklich keinen Schutz mehr hat, rendert das Tool jede Seite in hoher Auflösung und setzt daraus eine neue PDF zusammen. Das Ergebnis sieht aus wie das Original, unterscheidet sich aber in drei Punkten:

- **Der Text ist nicht mehr markierbar.** Jede Seite ist jetzt ein Bild.
- **Links und Formularfelder funktionieren nicht mehr.**
- **Die Datei kann größer werden** als das Original.

Für das Archivieren von Gehaltsabrechnungen oder das Hochladen eines Kontoauszugs ist das meist kein Problem. Wenn Sie den Text später durchsuchen oder kopieren möchten, gibt es einen zweiten Schritt.

## Text wieder durchsuchbar machen

Laden Sie die entsperrte PDF in den [PDF-OCR-Konverter](/pdf-ocr/) (Tool-Seite auf Englisch) und wählen Sie als Sprache **German**. Die Texterkennung legt eine unsichtbare Textebene über jede Seite. Danach können Sie wieder nach Wörtern suchen und Textstellen kopieren, und Sie erhalten zusätzlich eine Textdatei. Rechnen Sie mit einigen Sekunden pro Seite, denn die Erkennung läuft auf Ihrem Gerät.

Ist die Datei nach dem Entsperren zu groß für ein Upload-Portal, verkleinern Sie sie anschließend mit [PDF verkleinern](/de/pdf-verkleinern/).

## Praxisbeispiele

**Lohnabrechnungen für den Steuerberater sammeln.** Entsperren Sie die zwölf Abrechnungen des Jahres einzeln und fügen Sie sie anschließend mit [PDF zusammenfügen](/de/pdf-zusammenfuegen/) zu einer Datei zusammen. Geschützte Dateien direkt zusammenzufügen, klappt nicht zuverlässig.

**Gehaltsnachweis für den Mietantrag.** Viele Vermieter möchten die letzten Gehaltsabrechnungen sehen. Entsperren Sie die Abrechnungen, damit der Empfänger nicht Ihr persönliches Passwort braucht. Schwärzen Sie vorher alles, was nicht für den Antrag nötig ist.

**Datei weitergeben, aber nicht ungeschützt.** Möchten Sie eine PDF mit einem *eigenen* Passwort weitergeben, das Sie dem Empfänger separat mitteilen, versehen Sie die entsperrte Datei mit [PDF schützen](/protect-pdf/) (Tool-Seite auf Englisch) mit einem neuen Passwort.

## Wenn es nicht klappt

**„Could not open this PDF".** Die Datei ist beschädigt oder gar keine echte PDF. Öffnen Sie sie zur Probe im Browser oder in Ihrem PDF-Reader.

**Sie kennen das Passwort nicht.** Dann wenden Sie sich an den Absender: Arbeitgeber, Bank oder Behörde können Ihnen das Passwort nennen oder die Datei erneut schicken.

**Die Verarbeitung dauert lange.** Bei Dokumenten mit sehr vielen Seiten braucht das Neuaufbauen etwas Zeit. Lassen Sie den Tab geöffnet, bis der Download erscheint.

## Rechtlicher Hinweis und Datenschutz

Entsperren Sie nur PDFs, die Ihnen gehören oder für die Sie die Erlaubnis haben. Das Tool ist dafür gedacht, sich das wiederholte Eintippen eines bekannten Passworts zu sparen, nicht dafür, fremden Schutz zu umgehen.

Gerade passwortgeschützte Dokumente sind meist sensibel. Bei DoraPDF bleibt die Datei auf Ihrem Gerät: Das Passwort und die PDF werden im Browser verarbeitet und nicht an einen Server geschickt.

## Häufige Fragen

### Kann ich ein PDF-Passwort ohne Programm entfernen?

Ja. Sie brauchen nur einen Browser. Das Entsperren läuft direkt auf der Webseite, eine Installation ist nicht nötig.

### Kann ich eine PDF ohne Passwort entsperren?

Nur wenn die Datei lediglich gegen Drucken oder Kopieren gesperrt ist. Hat die PDF ein Öffnungspasswort, brauchen Sie dieses Passwort.

### Warum kann ich den Text danach nicht mehr markieren?

Weil die Seiten beim Entsperren als Bilder neu aufgebaut werden. Mit dem PDF-OCR-Konverter machen Sie den Text wieder durchsuchbar.

### Funktioniert das auch am Handy?

Ja, das Tool läuft im Handy-Browser. Bei langen Dokumenten ist ein Computer etwas schneller.
"""),
dict(slug='convertir-pdf-a-word-gratis-sin-perder-formato', lang='es', title='Cómo convertir PDF a Word gratis sin perder el formato (y qué hacer si el PDF está escaneado)', date='2026-11-15',
 desc='Convertir PDF a Word gratis y sin registrarse: elige entre conservar el diseño o texto editable, y aprende a tratar PDF escaneados. Todo en tu navegador.',
 tools=['pdf-to-word', 'pdf-ocr', 'word-to-pdf'], md="""
Te mandan un contrato en PDF y tienes que cambiar una fecha. Encuentras tu antiguo currículum, pero solo en PDF. O el ayuntamiento publica un formulario que quieres rellenar en el ordenador. La pregunta es siempre la misma: ¿cómo **convertir PDF a Word** sin que el documento quede descolocado?

Con el [convertidor de PDF a Word de DoraPDF](/es/convertir-pdf-a-word/) lo haces gratis, sin registrarte y sin instalar nada. El archivo se procesa en tu propio navegador. En esta guía te explico los dos modos de conversión, cuándo conviene cada uno y qué hacer cuando el PDF es en realidad un escaneo.

## Primero, una aclaración: por qué un PDF «se descoloca»

Un archivo de Word es texto que fluye: si añades una frase, todo lo que viene después se desplaza. Un PDF funciona al revés. Cada palabra tiene una posición fija en la página, como si estuviera pegada sobre papel. Al convertir de PDF a Word, el programa tiene que decidir qué priorizar: que se vea igual o que sea cómodo de editar. No siempre se pueden tener las dos cosas al cien por cien.

Por eso DoraPDF ofrece dos modos y te deja elegir.

## Los dos modos de conversión

En el desplegable **Layout** encontrarás estas opciones (la interfaz de la herramienta está en inglés):

**1. Keep original layout (recomendado).** Conserva el aspecto de cada página. El texto se coloca en la misma posición que en el PDF, con su fuente, tamaño, negrita, cursiva y color. Lo que no es texto (logotipos, líneas, tablas dibujadas, fondos de color) se mantiene como imagen detrás del texto. Resultado: el documento de Word se ve prácticamente igual que el PDF y puedes corregir palabras, números y fechas directamente.

**2. Text only (simple, flowing).** Extrae el texto en párrafos normales, que fluyen como en cualquier documento de Word. Los títulos se reconocen por su tamaño y se marcan en negrita, y cada página del PDF empieza en una página nueva. Las imágenes y el diseño se pierden.

| Lo que necesitas | Modo |
|---|---|
| Cambiar una fecha, un nombre o una cifra | Keep original layout |
| Rellenar o actualizar un formulario | Keep original layout |
| Reescribir párrafos enteros o reutilizar el texto | Text only |
| Copiar el contenido a otra plantilla | Text only |

Un detalle práctico del modo de diseño: cada línea va en su propio cuadro de texto. Puedes cambiar palabras sin problema, pero si añades varias frases a una línea, el texto no empuja a las líneas de abajo. Para reescribir mucho, usa el modo de solo texto.

## Paso a paso: de PDF a Word editable

1. Abre [Convertir PDF a Word](/es/convertir-pdf-a-word/).
2. Arrastra tu PDF o selecciónalo desde el ordenador o el móvil.
3. Elige el modo en **Layout**.
4. Pulsa el botón de convertir y espera a que se procese cada página.
5. Descarga el archivo .docx. Tiene el mismo nombre que tu PDF.

Puedes abrir el resultado en Microsoft Word, LibreOffice Writer, Google Docs o Pages.

## Si el PDF está escaneado

Si al convertir aparece el mensaje **«No text found — this PDF looks scanned (image only)»**, el PDF no contiene texto real, solo fotos de páginas. Pasa con documentos escaneados en una impresora o fotografiados con el móvil.

La solución es aplicar primero reconocimiento de texto (OCR):

1. Abre el [convertidor OCR de PDF](/pdf-ocr/) (la pantalla de la herramienta está en inglés).
2. Selecciona tu PDF y en **Language** elige **Spanish**.
3. Pulsa **Run OCR ✦**. Obtendrás un PDF con texto buscable y, además, un archivo .txt con todo el texto.
4. Si solo necesitas el contenido, copia el texto del .txt. Si quieres un Word, convierte el nuevo PDF con el modo **Text only**.

El OCR se ejecuta en tu dispositivo y tarda unos segundos por página; en documentos largos, ten paciencia. Funciona mejor con escaneos nítidos, rectos y con buen contraste.

## Consejos para obtener el mejor resultado

- **Fuentes que no tienes instaladas.** Si el PDF usa una tipografía especial, Word la sustituye por otra parecida. Puede que algunas líneas queden un poco más anchas o estrechas.
- **Texto girado.** El texto en diagonal o vertical (sellos, marcas de agua, rótulos laterales) se queda como parte de la imagen de fondo y no es editable.
- **Revisa números y símbolos.** Después de convertir, repasa importes, fechas y caracteres especiales antes de enviar el documento.
- **Vuelve a PDF al terminar.** Cuando hayas hecho los cambios, guarda el documento desde Word como PDF (Archivo → Guardar como → PDF). Si no tienes Word a mano, la herramienta [Convertir Word a PDF](/es/convertir-word-a-pdf/) también acepta archivos .docx.

## Privacidad: tus documentos no salen de tu equipo

Contratos, nóminas, currículums: lo que se convierte de PDF a Word suele ser personal. En DoraPDF la conversión se hace con JavaScript dentro de tu navegador. El archivo no se sube a ningún servidor, y cuando cierras la pestaña no queda rastro en ningún sitio.

## Preguntas frecuentes

### ¿Es gratis convertir PDF a Word en DoraPDF?

Sí. No hay registro, no hay marca de agua y no hace falta instalar ningún programa.

### ¿Puedo convertir PDF a Word en el móvil?

Sí. La herramienta funciona en el navegador de Android y iPhone. Después puedes abrir el .docx con la app de Word o con Google Docs.

### ¿Se conservan las tablas?

En el modo **Keep original layout**, las tablas se ven como en el original: los bordes y fondos quedan en la imagen y el texto de cada celda es editable. No se crean tablas de Word reales. Si necesitas trabajar con los datos, prueba [Convertir PDF a Excel](/es/convertir-pdf-a-excel/).

### ¿Por qué mi PDF no tiene texto?

Porque es un escaneo o una foto. Pásalo primero por el OCR y después conviértelo.
"""),
dict(slug='comprimir-pdf-enviar-correo-subir', lang='es', title='Comprimir PDF para enviarlo por correo o subirlo a una sede electrónica', date='2026-11-15',
 desc='Comprimir PDF gratis y online: reduce el tamaño para enviarlo por email o subirlo a un portal con límite de MB. Dos modos, sin registro, en tu navegador.',
 tools=['pdf-compressor', 'pdf-splitter', 'image-compressor'], md="""
Has escaneado el contrato de alquiler, las nóminas y el DNI, y el PDF pesa 18 MB. El correo tarda una eternidad en enviarse o directamente lo rechaza, y el portal de la administración te avisa: «el archivo no puede superar los 5 MB». Toca **comprimir el PDF**.

El [compresor de PDF de DoraPDF](/es/comprimir-pdf/) reduce el tamaño de tus archivos gratis, sin registrarte y sin subirlos a ningún servidor. En esta guía te explico cómo funciona, qué modo elegir según el documento y qué hacer si aun así no llegas al límite.

## ¿Por qué pesa tanto un PDF?

Casi siempre por las imágenes. Un PDF creado desde Word con solo texto ocupa unos pocos cientos de KB aunque tenga muchas páginas. En cambio, cada página escaneada o fotografiada es una imagen de alta resolución, y diez páginas así pueden sumar fácilmente decenas de megas.

Saber esto te ahorra frustraciones: un PDF de texto apenas se puede comprimir porque ya es pequeño; un PDF escaneado, en cambio, se puede reducir muchísimo.

## Los dos modos del compresor

La herramienta tiene dos modos en el desplegable **Mode** (la interfaz está en inglés):

**Smart — keep text selectable.** Vuelve a guardar el PDF de forma optimizada y reorganiza su estructura interna. El texto sigue siendo seleccionable y la calidad no cambia. Funciona bien con PDF generados por programas que guardan de forma poco eficiente. Si el archivo ya estaba bien optimizado, verás el aviso «already optimised» y casi no habrá diferencia.

**Strong — maximum compression.** Convierte cada página en una imagen comprimida. Es el modo que más reduce, sobre todo en escaneos. Aquí eliges además la calidad de imagen:

- **High quality:** buena nitidez, ahorro moderado.
- **Balanced:** el punto medio, adecuado para la mayoría de documentos.
- **Smallest:** el archivo más ligero; la letra pequeña puede verse menos nítida.

La contrapartida del modo Strong: el texto deja de ser seleccionable, y los enlaces y campos de formulario se pierden, porque cada página pasa a ser una foto.

## Qué modo elegir

| Tipo de PDF | Modo recomendado |
|---|---|
| Documento escaneado o fotos de papeles | Strong + Balanced |
| PDF exportado desde Word o Excel | Smart |
| Presentación con muchas fotos | Prueba Smart; si no basta, Strong + High quality |
| Contrato que el destinatario tiene que firmar o rellenar | Smart (Strong elimina los campos) |

## Paso a paso: comprimir un PDF

1. Abre [Comprimir PDF](/es/comprimir-pdf/).
2. Arrastra el archivo o selecciónalo.
3. Elige el **Mode** y, si usas Strong, la calidad en **Image quality**.
4. Pulsa **Compress ✦**.
5. Descarga el resultado. Junto al nombre verás cuánto se ha reducido, por ejemplo «62% smaller». El archivo se llama igual que el original con el añadido `-compressed`.

Tu archivo original no se modifica, así que puedes probar varias opciones y quedarte con la que mejor equilibre tamaño y calidad.

## Si sigue siendo demasiado grande

**Divide el documento.** Si el portal permite varios archivos, separa el PDF en partes con [Dividir PDF](/es/dividir-pdf/). Por ejemplo, las nóminas por un lado y el contrato por otro.

**Comprime solo las partes escaneadas.** Si tu PDF mezcla páginas de texto con páginas escaneadas, sepáralas, comprime los escaneos con el modo Strong y vuelve a juntarlo todo con [Unir PDF](/es/unir-pdf/). Así el texto de las páginas originales sigue siendo seleccionable.

**Reduce las fotos antes de crear el PDF.** Si vas a convertir fotos del móvil en PDF, comprímelas antes con [Comprimir imagen](/es/comprimir-imagen/). Partir de imágenes más ligeras da un PDF más ligero desde el principio.

**Comprueba la calidad.** Antes de enviar, abre el PDF comprimido y haz zoom en la letra más pequeña. Si un número de cuenta o una fecha no se lee bien, repite con una calidad más alta.

## Límites habituales que conviene conocer

Los servicios de correo más usados suelen limitar los adjuntos a unos 20 o 25 MB, y los archivos más grandes se envían como enlace a la nube. Las sedes electrónicas, plataformas de empleo y portales de universidades suelen tener límites bastante más bajos por archivo; el límite exacto aparece normalmente junto al botón de subida. Si no lo encuentras, un PDF de pocos megas suele ser seguro.

## Privacidad

Los documentos que más se comprimen son justo los más sensibles: DNI, nóminas, contratos, informes. Con DoraPDF el archivo se procesa dentro de tu navegador y no se envía a ningún servidor. Nadie más tiene acceso a él.

## Preguntas frecuentes

### ¿Comprimir un PDF reduce la calidad?

En el modo Smart, no. En el modo Strong, las páginas se convierten en imágenes comprimidas: con «High quality» o «Balanced» la diferencia apenas se nota al leer, con «Smallest» la letra muy pequeña puede perder nitidez.

### ¿Puedo comprimir un PDF en el móvil?

Sí. La herramienta funciona en el navegador de Android y iPhone, sin instalar ninguna app.

### ¿Por qué mi PDF casi no se reduce?

Probablemente es un PDF de texto que ya estaba optimizado. Si contiene imágenes o escaneos, prueba el modo Strong.

### ¿Hay límite de tamaño o de páginas?

La herramienta no fija un límite. Con archivos muy grandes, el tiempo de proceso depende de la potencia de tu dispositivo.
"""),
dict(slug='unir-pdf-combinar-varios-archivos-en-uno', lang='es', title='Unir PDF: cómo combinar varios archivos en uno, en el ordenador o en el móvil', date='2026-11-15',
 desc='Unir PDF gratis y sin instalar nada: combina varios archivos en uno en el orden que quieras, desde el ordenador o el móvil. Tus PDF no salen del navegador.',
 tools=['pdf-merger', 'pdf-splitter', 'images-to-pdf'], md="""
La solicitud de la beca pide «un único PDF con toda la documentación». Tú tienes el impreso firmado en un archivo, el certificado de notas en otro, la declaración de la renta en un tercero y el DNI en dos fotos. Antes de pelearte con el formulario, necesitas **unir los PDF** en uno solo y en un orden que tenga sentido.

Con la herramienta [Unir PDF de DoraPDF](/es/unir-pdf/) combinas varios archivos en uno gratis, sin registrarte y sin instalar ningún programa. Funciona igual en el ordenador que en el móvil, y los archivos se juntan dentro de tu navegador.

## Antes de empezar: tres comprobaciones rápidas

1. **¿Están todos en PDF?** La herramienta solo acepta archivos PDF. Si tienes fotos (por ejemplo, del DNI o de un recibo), conviértelas primero, como explico más abajo.
2. **¿Alguno tiene contraseña?** Los PDF protegidos pueden dar error al unirlos. Si conoces la contraseña, quítala antes con [Desbloquear PDF](/es/desbloquear-pdf/).
3. **¿Qué orden necesitas?** Las bases de una convocatoria suelen indicar el orden de los documentos. Apúntalo antes de empezar.

## Cómo unir PDF en el ordenador

1. Abre [Unir PDF](/es/unir-pdf/).
2. Arrastra los archivos a la zona de carga o haz clic para seleccionarlos. Puedes añadirlos todos de golpe o de uno en uno.
3. Revisa la lista: los archivos se unen **en el orden en que aparecen**, de arriba abajo.
4. Pulsa **Merge PDFs ✦** (la interfaz está en inglés).
5. Descarga `merged.pdf` y cámbiale el nombre por algo claro, como `Solicitud_beca_Garcia_Lopez.pdf`.

Necesitas al menos dos archivos. Todas las páginas se copian tal cual, con su calidad y tamaño originales. Si un documento es A4 y otro tamaño carta, cada página conserva su tamaño.

## Cómo unir PDF en el móvil

En el móvil el proceso es el mismo, solo cambia la forma de elegir los archivos:

- **Android:** al tocar la zona de carga se abre el selector de archivos. Busca en «Descargas» o en la carpeta donde guardas los documentos y marca varios a la vez si tu móvil lo permite.
- **iPhone:** al tocar la zona de carga, elige «Seleccionar archivo» para abrir la app Archivos. Los PDF que te llegan por correo o WhatsApp tienes que guardarlos antes en Archivos con la opción «Guardar en Archivos».

Cuando descargues el resultado, en Android aparecerá en «Descargas»; en iPhone, normalmente en la carpeta de descargas de la app Archivos.

## Cómo cambiar el orden

La herramienta no permite arrastrar archivos dentro de la lista para reordenarlos. Hay dos maneras sencillas de conseguir el orden correcto:

- **Numera los archivos antes.** Renómbralos como `1-solicitud.pdf`, `2-notas.pdf`, `3-renta.pdf`. Así aparecen ordenados al seleccionarlos.
- **Corrige sobre la marcha.** Si un archivo ha quedado en mal sitio, quítalo con la ✕ y vuelve a añadirlo: se colocará al final de la lista. Repite hasta que todo esté en su lugar.

## Unir solo algunas páginas

A veces no necesitas el documento entero, sino solo la primera página de la declaración y la última del contrato. Hazlo en dos pasos:

1. Extrae las páginas que te interesan con [Dividir PDF](/es/dividir-pdf/).
2. Une esos fragmentos con el resto de documentos.

## Mezclar fotos y PDF en un solo archivo

Las fotos del DNI, de un recibo o de un justificante no se pueden añadir directamente. Primero conviértelas con [JPG a PDF](/es/jpg-a-pdf/): puedes poner varias fotos en un mismo PDF, por ejemplo el anverso y el reverso del DNI, cada una en su página. Después añade ese PDF a la lista de Unir PDF junto con los demás documentos.

## Problemas frecuentes

**Aparece «Add at least 2 PDF files».** Solo has añadido un archivo. Añade al menos otro.

**Un archivo da error.** Puede estar dañado o protegido con contraseña. Ábrelo en tu lector de PDF para comprobarlo y, si está protegido, desbloquéalo primero.

**El PDF final es demasiado grande para el portal.** Unir no comprime nada: el resultado pesa aproximadamente lo mismo que la suma de los archivos. Redúcelo con [Comprimir PDF](/es/comprimir-pdf/) antes de subirlo.

**Una página sale girada.** Gírala antes con la herramienta [Rotar PDF](/rotate-pdf/) (pantalla en inglés) y vuelve a unir.

## Privacidad

Los documentos que se suelen unir para un trámite contienen datos personales: DNI, ingresos, notas, direcciones. En DoraPDF los PDF se leen y se combinan con JavaScript dentro de tu navegador. No se suben a ningún servidor ni se guardan en ningún sitio.

## Preguntas frecuentes

### ¿Puedo unir PDF sin instalar ningún programa?

Sí. Solo necesitas un navegador como Chrome, Firefox, Edge o Safari.

### ¿Cuántos PDF puedo unir a la vez?

Como mínimo dos. No hay un máximo fijo; con muchos archivos grandes, la velocidad depende de tu dispositivo.

### ¿Se pierde calidad al unir PDF?

No. Las páginas se copian sin volver a comprimirlas, y el texto seleccionable sigue siéndolo.

### ¿Tiene marca de agua el resultado?

No. El PDF final contiene solo tus páginas.
"""),
dict(slug='jpg-a-pdf-desde-movil-u-ordenador', lang='es', title='JPG a PDF desde el móvil o el ordenador: varias fotos en un solo PDF, gratis', date='2026-11-15',
 desc='Pasar JPG a PDF gratis desde el móvil o el ordenador: varias fotos en un PDF, tamaño A4 o ajustado, y fotos HEIC del iPhone. Sin subir tus imágenes.',
 tools=['images-to-pdf', 'heic-to-pdf', 'scan-to-pdf'], md="""
Las fotos del justificante de pago, los tickets de un viaje de trabajo o las páginas de unos apuntes: tienes las imágenes en el móvil, pero te las piden en PDF. Pasar de **JPG a PDF** es una de esas tareas que parecen complicadas hasta que se hacen una vez.

Con la herramienta [JPG a PDF de DoraPDF](/es/jpg-a-pdf/) conviertes una o varias fotos en un único PDF, gratis y sin registrarte. Acepta JPG, PNG y WebP, y también las fotos HEIC del iPhone. Las imágenes se procesan en tu navegador; no se suben a ningún servidor.

## Lo esencial en 30 segundos

1. Abre [JPG a PDF](/es/jpg-a-pdf/).
2. Añade tus fotos en el orden en que quieres las páginas.
3. Elige el tamaño de página y el margen.
4. Pulsa **Create PDF ✦** y descarga el archivo.

Cada foto se convierte en una página. Si añades varias, obtienes un solo PDF con todas.

## Las opciones, explicadas

La interfaz de la herramienta está en inglés, pero solo tiene dos ajustes:

**Page size (tamaño de página)**

- **Fit page to image:** la página tiene exactamente el tamaño de la foto. Ideal para compartir fotos o capturas de pantalla sin bordes blancos.
- **A4 page:** cada foto se centra en una hoja A4, el tamaño estándar en España y Latinoamérica. Es la opción correcta si el PDF se va a imprimir o si lo pide un organismo oficial.
- **US Letter:** el tamaño carta usado en Estados Unidos y algunos países de América.

**Margin (margen)**: *No margin*, *Small margin* (por defecto) o *Big margin*. Para imprimir, deja al menos el margen pequeño; muchas impresoras no llegan al borde del papel.

La orientación se ajusta sola: una foto apaisada se coloca en una página horizontal y una vertical en una página vertical.

## JPG a PDF desde el móvil

**En Android**, abre la herramienta en Chrome, toca la zona de carga y elige «Fotos» o «Galería». Puedes seleccionar varias imágenes a la vez. El PDF se guarda en la carpeta «Descargas».

**En iPhone**, abre la herramienta en Safari, toca la zona de carga y elige «Fototeca». Las fotos del iPhone suelen estar en formato HEIC; la herramienta las acepta sin que tengas que convertirlas antes. El PDF descargado aparece en la app Archivos, normalmente en «Descargas».

Si todas tus fotos son HEIC, también puedes usar la herramienta específica [HEIC a PDF](/heic-to-pdf/) (pantalla en inglés), que funciona exactamente igual y solo muestra archivos HEIC en el selector.

## JPG a PDF desde el ordenador

En Windows, Mac o Linux, arrastra las imágenes desde una carpeta directamente a la zona de carga. Un truco para controlar el orden: renombra los archivos antes como `01.jpg`, `02.jpg`, `03.jpg`. Al seleccionarlos todos a la vez quedarán ordenados.

Si te equivocas, elimina una imagen de la lista con la ✕. Las nuevas imágenes que añadas se colocan siempre al final.

## ¿Fotos de documentos? Mejor escanéalas

Si lo que fotografías son papeles (un contrato, un formulario, unos apuntes), una foto normal incluye la mesa, sombras y el papel torcido. Para esos casos es mejor [Scan to PDF](/scan-to-pdf/) (pantalla en inglés): haces la foto con la cámara del móvil, arrastras las esquinas hasta los bordes del papel para recortarlo y enderezarlo, eliges un filtro de escaneo y guardas todas las páginas en un PDF. El resultado parece salido de un escáner.

## Ejemplos prácticos

- **Gastos de un viaje de trabajo:** fotos de tickets → *A4 page* + *Small margin*. Quedan listos para imprimir o adjuntar a la hoja de gastos.
- **Capturas de pantalla para un informe:** *Fit page to image* + *No margin*. Cada captura ocupa su página sin espacio desperdiciado.
- **DNI por las dos caras:** dos fotos → *A4 page*. Obtienes un PDF de dos páginas, anverso y reverso.
- **Portafolio de dibujos o fotografías:** *Fit page to image* + *Big margin* para darles un marco blanco.

## Si algo no sale bien

**El PDF pesa demasiado.** Las fotos del móvil son grandes. La herramienta ya limita las imágenes muy grandes, pero si el PDF sigue siendo pesado, redúcelo con [Comprimir PDF](/es/comprimir-pdf/), o comprime las fotos antes con [Comprimir imagen](/es/comprimir-imagen/).

**Las páginas salen en otro orden.** Algunos móviles entregan las fotos en el orden en que las tocas y otros por fecha. Revisa la lista antes de crear el PDF y corrige con la ✕ si hace falta.

**Una foto sale girada.** Gírala antes en la galería del móvil y guárdala de nuevo.

**Quiero añadir las fotos a un PDF que ya tengo.** Convierte las fotos en PDF y después junta ambos archivos con [Unir PDF](/es/unir-pdf/).

## Privacidad

Tus fotos no se suben a ningún sitio. La conversión de JPG a PDF se hace dentro del navegador, en tu propio dispositivo. Es importante cuando se trata de documentos de identidad, recibos o fotos personales.

## Preguntas frecuentes

### ¿Cómo junto varias fotos en un solo PDF?

Selecciona todas las fotos a la vez (o añádelas una a una) y pulsa **Create PDF ✦**. Cada foto será una página del mismo PDF.

### ¿Puedo convertir JPG a PDF sin instalar una app?

Sí. La herramienta funciona en el navegador del móvil, sin descargar nada.

### ¿Funciona con fotos PNG o capturas de pantalla?

Sí. Acepta JPG, PNG, WebP y HEIC.

### ¿Se reduce la calidad de las fotos?

Las fotos se guardan en alta calidad. Solo las imágenes muy grandes se reducen ligeramente para que el PDF no sea enorme.
"""),
dict(slug='quitar-fondo-de-imagen-gratis-ia', lang='es', title='Quitar fondo de imagen gratis con IA: fondo transparente o blanco en segundos', date='2026-11-15',
 desc='Quitar el fondo de una imagen gratis con IA: PNG con fondo transparente o blanco para productos, perfiles y logos. Sin marca de agua y sin subir tu foto.',
 tools=['image-background-remover', 'image-compressor', 'image-resizer'], md="""
Vas a vender unas zapatillas en una app de segunda mano y la foto tiene de fondo el suelo del pasillo. Necesitas una foto de perfil profesional y solo tienes una de las vacaciones. O quieres poner el logo de tu negocio sobre un fondo de color y viene con un recuadro blanco. En los tres casos, la solución es **quitar el fondo de la imagen**.

El [eliminador de fondos de DoraPDF](/es/quitar-fondo-de-imagen/) lo hace automáticamente con inteligencia artificial. Es gratis, no pone marca de agua y no necesitas cuenta. Y hay un detalle que lo diferencia: la IA se ejecuta dentro de tu navegador, así que tu foto no sale de tu dispositivo.

## Cómo quitar el fondo paso a paso

1. Abre [Quitar fondo de imagen](/es/quitar-fondo-de-imagen/).
2. Sube la foto: JPG, PNG, WebP o HEIC del iPhone.
3. Elige el modo en **Mode** y el fondo que quieres en **Background** (la interfaz está en inglés).
4. Pulsa **Remove background ✦**.
5. Compara el antes y el después arrastrando el control deslizante y descarga el resultado en PNG.

La primera vez tardará un poco más, porque el navegador descarga el modelo de IA. Las siguientes veces ya lo tiene guardado y va mucho más rápido.

## Quick o HD: qué modo elegir

**⚡ Quick — people & portraits.** Está pensado para personas: retratos, fotos de perfil, selfies. El modelo ocupa unos 13 MB y se descarga una sola vez. Funciona en casi cualquier navegador y dispositivo.

**✨ HD — any object (GPU).** Sirve para cualquier objeto: productos, mascotas, coches, plantas, comida. Es más preciso con los bordes, pero el modelo pesa unos 115 MB (también se descarga una sola vez) y necesita un navegador moderno con aceleración gráfica (WebGPU). Si tu navegador no la tiene, la herramienta te avisa y usa automáticamente el modo Quick.

Regla sencilla: si en la foto sale una persona, empieza con Quick. Si es un objeto, usa HD.

## Fondo transparente, blanco o de color

En **Background** eliges qué poner detrás del recorte:

- **Transparent:** PNG con fondo transparente. Para logos, montajes, stickers o para colocar la imagen sobre cualquier diseño.
- **White:** fondo blanco. Es el estándar para fotos de producto en tiendas online y apps de compraventa.
- **Black:** para un aspecto elegante y de alto contraste.
- **Pink** y **Light grey:** dos colores suaves para perfiles o miniaturas.

El resultado siempre se descarga en PNG, con el nombre de tu foto y el añadido `-no-bg`. Las imágenes muy grandes se reducen para que el lado más largo tenga como máximo 2000 píxeles, suficiente para web, redes sociales y tiendas online.

## Trucos para que el recorte quede limpio

- **Contraste.** Una persona con jersey negro delante de una pared oscura es un reto para cualquier IA. Si puedes elegir, haz la foto con un fondo que contraste con el sujeto.
- **Buena luz.** Las sombras fuertes alrededor del objeto pueden confundirse con el propio objeto.
- **El sujeto completo y nítido.** Una foto desenfocada da bordes difusos.
- **Pelo y bordes finos.** El cabello suelto, el pelo de un animal o los objetos transparentes (vasos, botellas) son lo más difícil. Revisa estos bordes con el control deslizante antes de usar la imagen.

## Ejemplos de uso

**Fotos para vender online.** Fotografía el producto sobre una superficie lisa, usa el modo HD y el fondo White. Todas tus fotos tendrán un aspecto uniforme y más profesional.

**Foto para el currículum o LinkedIn.** Modo Quick y fondo White o Light grey. Después puedes recortarla a medida con [Cambiar tamaño de imagen](/image-resizer/) (pantalla en inglés).

**Logo con fondo transparente.** Modo HD y fondo Transparent. Si el logo es solo texto o formas planas muy simples, revisa bien el resultado: la IA está entrenada sobre todo con fotos.

**Material para clase o presentaciones.** Recorta personajes u objetos con fondo transparente y colócalos directamente en tus diapositivas.

## Problemas frecuentes

**«No GPU acceleration in this browser — using Quick mode».** Tu navegador no admite WebGPU. Prueba con una versión actual de Chrome o Edge en el ordenador para usar el modo HD.

**El modelo no carga.** La descarga del modelo necesita conexión a internet la primera vez. Comprueba la conexión y vuelve a intentarlo.

**Se ha borrado parte del objeto.** Cambia de modo: para objetos, HD suele dar mejores resultados que Quick.

**El PNG pesa mucho.** Los PNG con transparencia son más pesados que un JPG. Si necesitas un archivo más ligero, pásalo por [Comprimir imagen](/es/comprimir-imagen/): los PNG se guardan como WebP, que conserva la transparencia y ocupa mucho menos.

## Privacidad

Muchas herramientas de este tipo suben tu foto a un servidor para procesarla. Aquí no: el modelo de IA se descarga en tu navegador y el recorte se calcula en tu propio dispositivo. La foto de tus hijos, tu cara o el producto que aún no has lanzado no salen de tu equipo.

## Preguntas frecuentes

### ¿Es gratis quitar el fondo de una imagen?

Sí, sin límite de uso, sin registro y sin marca de agua.

### ¿Funciona en el móvil?

Sí, el modo Quick funciona bien en el navegador del móvil. El modo HD necesita un navegador con WebGPU y descarga un modelo grande, así que es más cómodo en el ordenador.

### ¿En qué formato se descarga?

Siempre en PNG, con fondo transparente o con el color que hayas elegido.

### ¿Puedo quitar el fondo de varias fotos a la vez?

La herramienta procesa una foto cada vez. Como el modelo queda guardado tras la primera descarga, las siguientes fotos se procesan rápido.
"""),
dict(slug='extraer-texto-de-imagen-ocr-paso-a-paso', lang='es', title='Extraer texto de una imagen (OCR) paso a paso: copia el texto de fotos, capturas y PDF escaneados', date='2026-11-15',
 desc='Extraer texto de una imagen gratis con OCR: copia el texto de fotos, capturas de pantalla y PDF escaneados, en español y otros idiomas. Sin subir archivos.',
 tools=['image-to-text', 'pdf-ocr', 'scan-to-pdf'], md="""
¿Te ha pasado? Tienes una foto de la pizarra con los apuntes de clase, una captura de pantalla de un mensaje largo o la foto de una receta del libro de tu abuela, y necesitas ese texto en el ordenador. Volver a teclearlo todo es lento y te equivocas. La alternativa es **extraer el texto de la imagen** con OCR (reconocimiento óptico de caracteres).

DoraPDF tiene dos herramientas gratuitas para esto: [Extraer texto de imagen](/es/extraer-texto-de-imagen/) para fotos y capturas, y el [convertidor OCR de PDF](/pdf-ocr/) para documentos escaneados. Las dos funcionan sin registro y reconocen el texto dentro de tu navegador, sin subir tus archivos.

## ¿Qué herramienta necesito?

| Tienes… | Usa… | Obtienes… |
|---|---|---|
| Una o varias fotos o capturas (JPG, PNG, WebP, HEIC) | Extraer texto de imagen | El texto para copiar y un archivo .txt |
| Un PDF escaneado o fotografiado | Convertidor OCR de PDF (pantalla en inglés) | Un PDF buscable y un archivo .txt |

## Extraer texto de una imagen: paso a paso

1. Abre [Extraer texto de imagen](/es/extraer-texto-de-imagen/).
2. Sube una imagen o varias a la vez.
3. En **Language** elige el idioma del texto, por ejemplo **Spanish** (la interfaz está en inglés).
4. Pulsa **Extract text ✦**.
5. El texto aparece en un cuadro debajo. Cópialo o descarga el archivo .txt.

Si subes varias imágenes, el texto de todas se junta en un único resultado, con el nombre de cada archivo como separador. Es muy práctico para pasar a limpio varias páginas fotografiadas de una vez.

La primera vez que uses un idioma, el navegador descarga el modelo de reconocimiento correspondiente (entre 2 y 10 MB, aproximadamente). Después queda guardado y no hace falta volver a descargarlo.

## Por qué es importante elegir bien el idioma

El OCR no solo «ve» letras: usa el conocimiento del idioma para decidir entre letras parecidas. Si el texto está en español y eliges inglés, es fácil que fallen la ñ, las tildes y los signos ¿ y ¡. Elige siempre el idioma real del texto.

Idiomas disponibles: inglés, español, francés, alemán, portugués, italiano, turco, indonesio, ruso, árabe, hindi, urdu y chino simplificado.

## Copiar texto de un PDF escaneado

Si intentas seleccionar texto en un PDF y no puedes, es que el PDF es en realidad una colección de imágenes. Pasa con contratos escaneados, apuntes fotocopiados o documentos antiguos.

1. Abre el [convertidor OCR de PDF](/pdf-ocr/).
2. Sube el PDF y elige el idioma en **Language**.
3. Pulsa **Run OCR ✦**.
4. Descarga los dos resultados: un PDF que se ve igual que el original pero en el que ya puedes buscar (Ctrl+F) y seleccionar texto, y un archivo .txt con todo el contenido, página por página.

El reconocimiento tarda unos segundos por página porque se hace en tu dispositivo. La herramienta procesa hasta 60 páginas por documento; si el tuyo es más largo, divídelo antes con [Dividir PDF](/es/dividir-pdf/).

## Cómo conseguir un texto más preciso

La calidad del resultado depende sobre todo de la calidad de la imagen:

- **Foto recta y de frente.** Las páginas inclinadas o curvadas (un libro abierto) dan más errores.
- **Buena luz, sin sombras.** Evita que tu mano o el móvil hagan sombra sobre el papel.
- **Enfoque.** Toca la pantalla sobre el texto antes de hacer la foto para enfocar.
- **Recorta lo que sobra.** Si en la foto aparecen otros elementos (la mesa, otra página), el OCR puede leer basura. Para documentos en papel, [Scan to PDF](/scan-to-pdf/) (pantalla en inglés) te permite recortar y enderezar la página antes.
- **Capturas de pantalla:** suelen dar resultados excelentes porque el texto es nítido y sin distorsión.

Un aviso honesto: el OCR funciona muy bien con texto impreso, pero la letra manuscrita se reconoce mal. Con apuntes escritos a mano, cuenta con tener que corregir bastante.

## Ejemplos prácticos

**Estudiantes:** fotografía las páginas de un libro de la biblioteca y extrae las citas que necesitas para tu trabajo, en lugar de copiarlas a mano. No olvides anotar la referencia bibliográfica.

**Oficina:** pasa una factura escaneada por el OCR de PDF para poder buscar el número de factura o copiar el NIF del proveedor.

**Día a día:** captura de pantalla de una dirección, un horario o un código, y cópialo directamente sin teclearlo.

**Idiomas:** extrae el texto de un cartel o un menú en francés y pégalo en tu traductor favorito.

## Problemas frecuentes

**«No readable text found in this image».** La herramienta no ha encontrado texto legible. Prueba con una foto más nítida o más cercana, o comprueba que has elegido el idioma correcto.

**Aparecen caracteres raros.** Suele deberse al idioma equivocado o a una imagen con poco contraste. Repite con el idioma correcto o con una foto mejor iluminada.

**Las columnas se mezclan.** En textos a dos columnas (periódicos, revistas), el orden de las líneas puede alterarse. Recorta cada columna por separado antes de extraer el texto.

## Privacidad

Las fotos de documentos suelen contener datos personales: nombres, direcciones, números de cuenta. Con DoraPDF el reconocimiento se hace dentro de tu navegador. Tus imágenes y PDF no se suben a ningún servidor; solo se descarga el modelo del idioma.

## Preguntas frecuentes

### ¿Es gratis extraer texto de una imagen?

Sí, sin registro y sin límite de imágenes.

### ¿Funciona en el móvil?

Sí. Puedes hacer la foto con el móvil y extraer el texto directamente en el navegador.

### ¿Reconoce letra escrita a mano?

Solo de forma limitada. Está pensado para texto impreso o de pantalla.

### ¿Puedo extraer texto de un PDF que no es escaneado?

Si el texto del PDF ya se puede seleccionar, no necesitas OCR. Basta con copiarlo, o convertirlo con [Convertir PDF a Word](/es/convertir-pdf-a-word/).
"""),
dict(slug='pdf-in-word-umwandeln-kostenlos-layout', lang='de', title='PDF in Word umwandeln – kostenlos und ohne dass das Layout kaputtgeht', date='2026-11-15',
 desc='PDF in Word umwandeln, kostenlos und ohne Anmeldung: zwei Modi für Layout oder Fließtext, Tipps für gescannte PDFs. Die Datei bleibt in Ihrem Browser.',
 tools=['pdf-to-word', 'pdf-ocr', 'pdf-to-excel'], md="""
Ein Vertrag, den Sie nur in einem Absatz ändern müssen. Ein Lebenslauf, dessen Word-Datei längst verschwunden ist. Ein Formular der Hausverwaltung, das als PDF kam. Fast jeder steht irgendwann vor derselben Frage: Wie kann ich eine **PDF in Word umwandeln**, ohne dass danach alles verrutscht ist?

Mit dem [PDF-in-Word-Konverter von DoraPDF](/de/pdf-in-word-umwandeln/) geht das kostenlos, ohne Anmeldung und ohne Programm. Die Umwandlung läuft direkt in Ihrem Browser – die PDF wird dafür nicht auf einen Server hochgeladen. Wie Sie das beste Ergebnis bekommen, hängt vor allem davon ab, welchen der zwei Modi Sie wählen.

## Zwei Modi, zwei Ziele

Bevor Sie auf den Button klicken, lohnt sich eine kurze Überlegung: Wollen Sie, dass die Word-Datei aussieht wie das Original, oder wollen Sie den Text frei weiterbearbeiten?

**„Keep original layout" (empfohlen):** Jede Seite wird nachgebaut. Grafiken, Linien, farbige Flächen und Logos landen als Seitenhintergrund im Dokument, der Text darüber wird als bearbeitbarer Text an genau die Stelle gesetzt, an der er im PDF stand – mit passender Schriftgröße, Fett- und Kursivschrift und Textfarbe. Das Ergebnis sieht dem Original sehr ähnlich. Ideal, wenn Sie nur Kleinigkeiten ändern: einen Namen, ein Datum, eine Telefonnummer.

**„Text only" (einfach, fließend):** Hier wird nur der Text übernommen, Zeile für Zeile, als normaler Fließtext. Größere Schrift wird als Überschrift erkannt und fett gesetzt, jede PDF-Seite beginnt mit einem Seitenumbruch. Bilder und Design fallen weg. Dieser Modus ist die bessere Wahl, wenn Sie den Inhalt umschreiben, kürzen oder in ein eigenes Dokument einbauen möchten.

Faustregel: Kleine Korrekturen → Layout-Modus. Große Umbauten → Text-Modus.

## Schritt für Schritt: PDF zu Word konvertieren

1. Öffnen Sie [PDF in Word umwandeln](/de/pdf-in-word-umwandeln/).
2. Ziehen Sie Ihre PDF in das Upload-Feld oder klicken Sie darauf, um sie auszuwählen. Das Tool verarbeitet eine Datei pro Durchgang.
3. Wählen Sie unter **Layout** den gewünschten Modus. Die Bedienelemente des Tools sind auf Englisch, die Bezeichnungen oben helfen bei der Zuordnung.
4. Klicken Sie auf **Convert now ✦**. Ein Fortschrittsbalken zeigt, wie weit die Seiten verarbeitet sind.
5. Laden Sie die fertige `.docx`-Datei über **Download** herunter. Sie trägt denselben Namen wie Ihre PDF, also wird aus `mietvertrag.pdf` die Datei `mietvertrag.docx`.

Die Datei öffnet sich in Microsoft Word, LibreOffice Writer und auch in Google Docs, wenn Sie sie dort hochladen.

## Was im Layout-Modus wichtig zu wissen ist

Damit das Original so genau wie möglich erhalten bleibt, steht jede Textzeile im Layout-Modus in einem eigenen, fest positionierten Textrahmen. Das hat Vor- und Nachteile:

- **Kurze Änderungen klappen hervorragend.** Klicken Sie in die Zeile, tippen Sie den neuen Text, fertig.
- **Längere Ergänzungen fließen nicht automatisch weiter.** Wenn Sie einen Satz deutlich verlängern, rutscht die nächste Zeile nicht nach unten. Hier hilft es, den Text auf zwei Zeilen zu verteilen – oder gleich den Text-Modus zu nutzen.
- **Schräg gestellter Text** (zum Beispiel ein diagonaler Stempel) bleibt Teil des Hintergrundbilds und ist nicht editierbar.
- **Schriftarten** werden anhand des Namens in der PDF zugeordnet. Ist eine Schrift auf Ihrem Rechner nicht installiert, ersetzt Word sie durch eine ähnliche. Kleine Abweichungen in der Laufweite sind dann normal.

## Gescannte PDFs: erst Texterkennung, dann Word

Ein häufiges Problem: Die Umwandlung bricht mit der Meldung „No text found – this PDF looks scanned" ab. Das heißt, Ihre PDF enthält keinen echten Text, sondern nur Fotos der Seiten – typisch für eingescannte Briefe oder Dokumente, die mit dem Handy abfotografiert wurden.

Die Lösung ist eine Texterkennung (OCR) als Zwischenschritt:

1. Öffnen Sie den [PDF-OCR-Konverter](/pdf-ocr/) (die Tool-Seite ist auf Englisch).
2. Stellen Sie die Sprache auf **German**, damit Umlaute und ß korrekt erkannt werden.
3. Klicken Sie auf **Run OCR ✦**. Sie erhalten eine durchsuchbare PDF und zusätzlich eine Textdatei.
4. Wandeln Sie die durchsuchbare PDF anschließend im Modus **Text only** in Word um.

Rechnen Sie bei OCR mit etwa 5 bis 15 Sekunden pro Seite; verarbeitet werden bis zu 60 Seiten pro Durchgang. Prüfen Sie das Ergebnis danach kurz auf Lesefehler, besonders bei kleiner Schrift oder schlechten Scans.

## Typische Probleme und schnelle Lösungen

**Die Zeilen sitzen leicht versetzt.** Meist liegt das an einer fehlenden Schriftart. Installieren Sie die Schrift oder markieren Sie den Text und weisen Sie eine vorhandene Schrift zu.

**Die PDF ist passwortgeschützt.** Wenn Sie das Passwort kennen, entfernen Sie den Schutz zuerst mit [PDF-Passwort entfernen](/de/pdf-passwort-entfernen/) und wandeln Sie danach um.

**Sie brauchen eigentlich nur eine Tabelle.** Für Zahlenkolonnen ist Word oft der falsche Zielort. Mit [PDF in Excel umwandeln](/de/pdf-in-excel-umwandeln/) landen Tabellen direkt in Zellen, eine Seite pro Tabellenblatt.

**Die Umwandlung dauert lange.** Bei vielen Seiten arbeitet Ihr Gerät ordentlich, weil alles lokal passiert. Schließen Sie andere Tabs mit großen Dateien, dann geht es schneller. Am Handy funktioniert es ebenfalls, bei sehr langen Dokumenten ist ein Laptop aber angenehmer.

## Datenschutz: Warum „ohne Hochladen" einen Unterschied macht

Viele Online-Konverter laden Ihre Datei auf einen fremden Server, wandeln sie dort um und schicken sie zurück. Bei Verträgen, Gehaltsabrechnungen oder Arztbriefen ist das unangenehm. DoraPDF geht einen anderen Weg: Die PDF wird mit JavaScript in Ihrem eigenen Browser gelesen und als Word-Datei zusammengebaut. Ihr Dokument verlässt Ihr Gerät nicht, und Sie brauchen kein Konto.

## Häufige Fragen

### Kann ich eine PDF kostenlos und ohne Anmeldung in Word umwandeln?

Ja. Der Konverter ist kostenlos, es gibt keine Registrierung und kein Wasserzeichen im Ergebnis.

### Welcher Modus erhält das Layout am besten?

„Keep original layout". Er übernimmt Seitengestaltung, Bilder und Textpositionen. Wenn Sie viel umschreiben wollen, ist „Text only" praktischer.

### Funktioniert das auch mit gescannten PDFs?

Nicht direkt. Machen Sie die PDF zuerst mit dem OCR-Tool durchsuchbar und wandeln Sie sie dann im Text-Modus um.

### Wird meine Datei auf einen Server hochgeladen?

Nein. Die Umwandlung passiert vollständig in Ihrem Browser.

### Kann ich die Word-Datei in Google Docs oder LibreOffice öffnen?

Ja, das Ergebnis ist eine normale `.docx`-Datei.
"""),
dict(slug='pdf-verkleinern-fuer-e-mail-upload', lang='de', title='PDF verkleinern für E-Mail und Upload-Portale: So klappt es kostenlos', date='2026-11-15',
 desc='Anhang zu groß? So können Sie eine PDF verkleinern und komprimieren – kostenlos, ohne Anmeldung und ohne Upload. Mit Tipps für E-Mail und Upload-Portale.',
 tools=['pdf-compressor', 'pdf-splitter', 'image-compressor'], md="""
„Die Datei überschreitet die maximale Größe." Diese Meldung kommt meistens dann, wenn es eilt: beim Hochladen einer Bewerbung, beim Einreichen von Belegen bei der Krankenkasse oder beim Versenden eines eingescannten Vertrags per Mail. Die gute Nachricht: Eine **PDF verkleinern** dauert meist weniger als eine Minute.

Mit dem [PDF-Kompressor von DoraPDF](/de/pdf-verkleinern/) können Sie eine PDF kostenlos komprimieren, ohne Anmeldung und ohne die Datei irgendwohin hochzuladen – die Verarbeitung findet in Ihrem Browser statt. Hier erfahren Sie, welche Einstellung für welchen Zweck passt und was Sie tun können, wenn die Datei trotzdem zu groß bleibt.

## Warum manche PDFs so riesig sind

Text braucht in einer PDF kaum Platz. Ein zehnseitiges Word-Dokument als PDF ist oft nur wenige hundert Kilobyte groß. Groß werden PDFs fast immer durch **Bilder**: eingescannte Seiten, Handyfotos von Dokumenten, hochaufgelöste Grafiken in Präsentationen. Ein einziger Scan in Fotoqualität kann mehrere Megabyte wiegen – zwanzig davon, und das Limit vieler Mail-Anbieter (häufig irgendwo zwischen 10 und 25 MB) ist überschritten.

Das erklärt auch, warum die zwei Modi des Kompressors so unterschiedlich wirken.

## Die zwei Modi im Überblick

**Smart – Text bleibt markierbar.** Die PDF wird neu und effizienter gespeichert. Inhalt, Text und Qualität bleiben unverändert, Sie können weiterhin Text markieren, kopieren und durchsuchen. Bei PDFs, die ungünstig erzeugt wurden, spart das spürbar Platz. Bei bereits gut optimierten Dateien ist der Effekt klein – dann zeigt das Tool „already optimised" an.

**Strong – maximale Komprimierung.** Jede Seite wird als Bild neu aufgebaut und als JPEG gespeichert. Das verkleinert vor allem gescannte Dokumente und bildlastige PDFs deutlich. Der Preis: Der Text ist danach nicht mehr markierbar oder durchsuchbar, weil jede Seite nur noch ein Bild ist. Für Strong können Sie die Bildqualität wählen: **High quality**, **Balanced** (Standard) oder **Smallest**.

## So verkleinern Sie Ihre PDF

1. Öffnen Sie [PDF verkleinern](/de/pdf-verkleinern/).
2. Ziehen Sie die PDF in das Feld oder wählen Sie sie per Klick aus.
3. Wählen Sie unter **Mode** zuerst **Smart**. (Die Bedienelemente sind auf Englisch.)
4. Klicken Sie auf **Compress ✦**.
5. Neben dem Ergebnis sehen Sie, um wie viel Prozent die Datei kleiner geworden ist. Laden Sie `dateiname-compressed.pdf` herunter.

Ist die Datei noch zu groß, wiederholen Sie den Vorgang mit der Originaldatei im Modus **Strong** und starten Sie mit **Balanced**. Reicht auch das nicht, probieren Sie **Smallest**. Öffnen Sie das Ergebnis jedes Mal kurz und prüfen Sie, ob Kleingedrucktes noch lesbar ist.

## Welche Einstellung für welchen Zweck?

| Situation | Empfehlung |
|---|---|
| Word-Export, Rechnung, digital erzeugtes Dokument | Smart |
| Eingescannter Brief für Behörde oder Versicherung | Strong, Balanced |
| Viele Handyfotos in einer PDF | Strong, Balanced oder Smallest |
| Bewerbungsmappe mit Zeugnissen | Strong, High quality |
| Dokument, in dem Text durchsuchbar bleiben muss | Smart |

Bei Bewerbungen lohnt sich ein genauer Blick: Wenn ein Portal Ihren Lebenslauf automatisch ausliest, sollte der Text erhalten bleiben. Komprimieren Sie in diesem Fall nur die eingescannten Zeugnisse mit Strong und lassen Sie das Anschreiben und den Lebenslauf im Smart-Modus.

## Wenn die PDF trotzdem zu groß ist

**Unnötige Seiten entfernen.** Leere Rückseiten aus dem Scanner, doppelte Seiten oder Anhänge, die niemand angefordert hat, kosten Platz. Mit [PDF teilen](/de/pdf-teilen/) extrahieren Sie nur die Seiten, die Sie wirklich brauchen, zum Beispiel „1-3, 5".

**Auf mehrere Mails aufteilen.** Wenn das Portal mehrere Dateien erlaubt, teilen Sie ein großes Dokument in zwei Teile und komprimieren Sie beide.

**Bilder vor dem Erstellen verkleinern.** Wenn Sie die PDF selbst aus Fotos zusammenstellen, komprimieren Sie die Fotos vorher mit [Bild komprimieren](/de/bild-komprimieren/). Kleinere Bilder ergeben automatisch eine kleinere PDF.

**Nicht mehrmals hintereinander komprimieren.** Nutzen Sie für einen neuen Versuch immer die Originaldatei. Wer eine bereits stark komprimierte PDF erneut mit Strong bearbeitet, verliert Qualität, ohne viel Platz zu gewinnen.

## PDF verkleinern am Handy

Oft entsteht das Problem unterwegs: Sie haben ein Dokument mit der Handykamera gescannt und wollen es direkt aus dem Mailprogramm verschicken. Öffnen Sie den Kompressor dafür einfach in Safari oder Chrome, wählen Sie die PDF aus der Dateien-App oder dem Download-Ordner und nutzen Sie gleich den Modus **Strong** mit **Balanced** – Handyscans bestehen ohnehin nur aus Bildern, sodass der Smart-Modus hier kaum etwas bringt. Die verkleinerte Datei landet wieder in Ihren Downloads und kann von dort an die Mail angehängt werden.

## Datenschutz bei sensiblen Dokumenten

Gerade die Dateien, die man verkleinern muss, sind oft persönlich: Gehaltsnachweise, Mietverträge, Ausweiskopien für die Wohnungssuche. Bei DoraPDF wird die PDF lokal in Ihrem Browser verarbeitet. Sie wird nicht auf unseren Server übertragen, und Sie brauchen kein Benutzerkonto.

## Häufige Fragen

### Wie kann ich eine PDF kostenlos verkleinern?

Öffnen Sie den PDF-Kompressor, laden Sie die Datei, wählen Sie Smart oder Strong und klicken Sie auf „Compress". Das ist kostenlos und ohne Anmeldung.

### Verliert die PDF beim Komprimieren an Qualität?

Im Smart-Modus nicht. Im Strong-Modus werden die Seiten als Bilder neu gespeichert; mit „High quality" bleibt das gut lesbar, mit „Smallest" wird es sichtbar weicher.

### Warum wird meine PDF kaum kleiner?

Wenn sie hauptsächlich Text enthält und schon effizient gespeichert ist, gibt es wenig zu sparen. Dann zeigt das Tool „already optimised". Hier hilft nur, Seiten zu entfernen.

### Funktioniert das am Handy?

Ja, im Browser auf iPhone und Android. Bei sehr großen Dateien ist ein Computer schneller.

### Kann ich danach noch Text kopieren?

Nach Smart ja, nach Strong nein.
"""),
dict(slug='mehrere-pdf-zusammenfuegen-kostenlos', lang='de', title='PDF zusammenfügen: Mehrere PDFs kostenlos zu einer Datei verbinden', date='2026-11-15',
 desc='Mehrere PDFs zu einer Datei zusammenfügen – kostenlos, ohne Programm und ohne Upload. Mit Tipps zur richtigen Reihenfolge und für Bewerbungsmappen.',
 tools=['pdf-merger', 'pdf-splitter', 'pdf-compressor'], md="""
Anschreiben, Lebenslauf, drei Zeugnisse und ein Zertifikat – und das Bewerbungsportal erlaubt genau einen Anhang. Oder: Die Nebenkostenabrechnung, die Belege und das Mietvertragsdeckblatt sollen gemeinsam an den Steuerberater. In beiden Fällen müssen Sie **PDF zusammenfügen**, und zwar in einer sinnvollen Reihenfolge.

Mit dem [PDF-Zusammenfüger von DoraPDF](/de/pdf-zusammenfuegen/) verbinden Sie mehrere PDFs kostenlos zu einer Datei. Sie brauchen kein Programm, kein Acrobat und kein Konto. Die Dateien werden in Ihrem Browser zusammengesetzt und nicht auf einen Server hochgeladen.

## Bevor Sie anfangen: Reihenfolge planen

Das Tool fügt die Dateien **in der Reihenfolge zusammen, in der Sie sie hinzufügen**. Eine nachträgliche Sortierung per Ziehen gibt es nicht. Das klingt nach einer Einschränkung, lässt sich aber leicht lösen:

- **Dateien vorher nummerieren.** Benennen Sie die Dateien im Ordner um: `01-anschreiben.pdf`, `02-lebenslauf.pdf`, `03-zeugnis-schule.pdf` und so weiter. Im Auswahlfenster stehen sie dann sauber sortiert untereinander. Wählen Sie mehrere auf einmal aus, kontrollieren Sie danach trotzdem die Liste im Tool – nicht jedes System übergibt die Dateien in derselben Reihenfolge.
- **Nacheinander hinzufügen.** Sie können das Upload-Feld mehrmals benutzen. Jede neue Datei wird hinten an die Liste angehängt.
- **Fehler korrigieren.** Mit dem ✕ neben einer Datei entfernen Sie sie aus der Liste. Falls die Reihenfolge durcheinandergeraten ist, entfernen Sie die betroffenen Dateien und fügen Sie sie in der richtigen Abfolge erneut hinzu.

## Anleitung: mehrere PDFs zu einer Datei

1. Öffnen Sie [PDF zusammenfügen](/de/pdf-zusammenfuegen/).
2. Ziehen Sie die erste PDF in das Feld, danach die weiteren – oder wählen Sie mehrere Dateien gleichzeitig aus.
3. Kontrollieren Sie die Liste. Oben steht, was im fertigen Dokument vorne steht.
4. Klicken Sie auf **Merge PDFs ✦** (die Bedienung ist auf Englisch).
5. Laden Sie die Datei `merged.pdf` herunter und benennen Sie sie sinnvoll um, etwa `Bewerbung_Mustermann_Vertrieb.pdf`.

Sie brauchen mindestens zwei Dateien. Alle Seiten jeder PDF werden vollständig übernommen, in ihrer Originalqualität und mit ihren ursprünglichen Seitengrößen.

## Praxisbeispiel: die Bewerbungsmappe als eine PDF

Viele Personalabteilungen wünschen sich alles in einem Dokument. Eine bewährte Reihenfolge ist:

1. Anschreiben
2. Lebenslauf
3. Arbeitszeugnisse, das neueste zuerst
4. Ausbildungs- oder Studienabschluss
5. Weitere Zertifikate

Ein paar Details machen den Unterschied:

- **Seitenformat einheitlich halten.** Wenn ein Zeugnis als quer fotografiertes Bild vorliegt, wirkt die Mappe unruhig. Drehen Sie solche Seiten vorher mit dem Tool [PDF drehen](/rotate-pdf/) (Tool-Seite auf Englisch).
- **Größe prüfen.** Mehrere Scans ergeben schnell eine große Datei. Liegt die fertige PDF über dem Limit des Portals, verkleinern Sie sie mit [PDF verkleinern](/de/pdf-verkleinern/).
- **Dateinamen professionell wählen.** „merged.pdf" oder „Scan_0034.pdf" wirkt unaufmerksam. Nachname, Position und vielleicht das Datum genügen.

## Teile verschiedener PDFs kombinieren

Manchmal brauchen Sie nicht die ganze Datei, sondern nur einzelne Seiten daraus – etwa Seite 1 und 4 eines Vertrags und dazu eine Anlage. Gehen Sie in zwei Schritten vor:

1. Extrahieren Sie die gewünschten Seiten mit [PDF teilen](/de/pdf-teilen/). Dort geben Sie zum Beispiel „1, 4" ein und erhalten eine neue PDF nur mit diesen Seiten.
2. Fügen Sie diese neue Datei dann mit den anderen Dokumenten zusammen.

So stellen Sie aus mehreren Quellen genau das Dokument zusammen, das Sie brauchen.

## Wenn etwas nicht klappt

**„Add at least 2 PDF files".** Sie haben nur eine Datei ausgewählt. Fügen Sie mindestens eine weitere hinzu.

**Eine Datei lässt sich nicht verarbeiten.** Das passiert gelegentlich bei beschädigten PDFs oder bei Dateien mit Passwortschutz. Öffnen Sie die Datei zur Probe in Ihrem PDF-Reader. Ist sie geschützt und kennen Sie das Passwort, entfernen Sie den Schutz vorher mit [PDF-Passwort entfernen](/de/pdf-passwort-entfernen/).

**Die Seiten sind in der falschen Reihenfolge.** Sortieren Sie die Dateinamen um, laden Sie die Seite neu und fügen Sie die Dateien noch einmal hinzu. Das geht schneller, als in einer fertigen PDF Seiten zu verschieben.

**Ein Foto statt einer PDF.** Bilder akzeptiert der Zusammenfüger nicht. Wandeln Sie JPGs vorher mit [JPG in PDF umwandeln](/de/jpg-in-pdf-umwandeln/) um.

## Datenschutz

Bewerbungsunterlagen, Kontoauszüge, Arztbefunde: Was man zusammenfügt, ist oft vertraulich. Beim DoraPDF-Zusammenfüger werden die PDFs mit einer JavaScript-Bibliothek direkt in Ihrem Browser gelesen und zu einer neuen Datei verbunden. Nichts davon wird auf einen Server übertragen.

## Häufige Fragen

### Kann ich PDFs ohne Programm zusammenfügen?

Ja. Sie brauchen nur einen Browser wie Chrome, Firefox, Edge oder Safari. Eine Installation ist nicht nötig.

### Wie viele PDFs kann ich zusammenfügen?

Mindestens zwei. Eine feste Obergrenze gibt das Tool nicht vor; bei sehr vielen oder sehr großen Dateien hängt die Geschwindigkeit von Ihrem Gerät ab.

### Wie ändere ich die Reihenfolge?

Die Dateien werden in der Reihenfolge verbunden, in der Sie sie hinzufügen. Nummerieren Sie die Dateinamen vorher oder entfernen und ergänzen Sie Dateien über die Liste.

### Bleibt die Qualität erhalten?

Ja. Die Seiten werden unverändert übernommen, es wird nichts neu komprimiert.

### Funktioniert das auf dem iPhone?

Ja. Wählen Sie die PDFs in Safari aus der Dateien-App aus. Die fertige Datei landet in Ihren Downloads.
"""),
dict(slug='jpg-in-pdf-umwandeln-handy-pc', lang='de', title='JPG in PDF umwandeln am Handy und PC – mehrere Fotos in eine PDF', date='2026-11-15',
 desc='JPG in PDF umwandeln auf iPhone, Android und PC: mehrere Fotos zu einer PDF, mit A4-Seiten und Rand. Kostenlos, ohne App und ohne Upload.',
 tools=['images-to-pdf', 'heic-to-pdf', 'pdf-compressor'], md="""
Die Kita will den Impfpass als PDF, der Vermieter die letzten drei Gehaltsnachweise, die Uni ein unterschriebenes Formular. Sie haben alles fotografiert – aber eben als Fotos. Jetzt müssen Sie **JPG in PDF umwandeln**, am besten so, dass alle Bilder in einer einzigen, ordentlichen Datei landen.

Mit dem [Bilder-zu-PDF-Konverter von DoraPDF](/de/jpg-in-pdf-umwandeln/) klappt das am Handy genauso wie am PC: kostenlos, ohne App und ohne Anmeldung. Die Fotos werden in Ihrem Browser zur PDF zusammengesetzt und nicht hochgeladen.

## Was der Konverter kann

- **JPG, PNG und WebP** werden verarbeitet, außerdem **HEIC/HEIF**, das Standardformat von iPhone-Fotos.
- **Mehrere Bilder auf einmal:** Jedes Bild wird eine Seite, in der Reihenfolge, in der Sie es hinzufügen.
- **Seitengröße:** „Fit page to image" (jede Seite so groß wie das Foto), **A4** oder **US Letter**. Für Deutschland, Österreich und die Schweiz ist A4 meistens die richtige Wahl.
- **Rand:** ohne Rand, kleiner oder großer Rand.
- **Hoch- und Querformat** werden automatisch erkannt. Ein Querformat-Foto bekommt eine Querformat-Seite.

Bei A4 und US Letter wird jedes Bild proportional eingepasst und zentriert. Nichts wird verzerrt oder abgeschnitten.

## Am PC: Schritt für Schritt

1. Öffnen Sie [JPG in PDF umwandeln](/de/jpg-in-pdf-umwandeln/).
2. Ziehen Sie die Fotos aus dem Explorer oder Finder in das Upload-Feld. Sie können auch mehrmals nacheinander Bilder hinzufügen; neue Bilder werden hinten angehängt.
3. Wählen Sie unter **Page size** „A4 page" und unter **Margin** zum Beispiel „Small margin". (Die Bedienelemente sind auf Englisch.)
4. Prüfen Sie die Liste. Ein falsch gewähltes Bild entfernen Sie mit dem ✕.
5. Klicken Sie auf **Create PDF ✦** und laden Sie die Datei herunter. Bei mehreren Bildern heißt sie `images.pdf`, bei einem einzelnen Bild trägt sie den Namen des Fotos.

## Am Handy: iPhone und Android

Eine extra App brauchen Sie nicht – der Browser reicht.

**iPhone (Safari):** Öffnen Sie die Tool-Seite und tippen Sie auf das Upload-Feld. iOS bietet Ihnen an, Fotos aus der Mediathek zu wählen, direkt ein Foto aufzunehmen oder eine Datei aus der Dateien-App zu nehmen. Markieren Sie mehrere Fotos in der gewünschten Reihenfolge, bestätigen Sie, wählen Sie A4 und tippen Sie auf „Create PDF". Die PDF finden Sie anschließend in der Dateien-App unter „Downloads".

**Android (Chrome):** Tippen Sie auf das Upload-Feld und wählen Sie die Fotos aus der Galerie oder dem Dateimanager. Nach dem Erstellen liegt die PDF im Download-Ordner.

Tipp: Fotografieren Sie Dokumente von oben, bei Tageslicht und auf einem dunklen, ruhigen Untergrund. Das wirkt im PDF deutlich sauberer als ein Foto mit Tischkante und Kaffeetasse.

## iPhone-Fotos im HEIC-Format

Viele iPhones speichern Fotos als HEIC. Das ist kein Problem: Der Konverter liest HEIC direkt. Wenn Sie ausschließlich iPhone-Fotos haben, können Sie auch den spezialisierten [HEIC-zu-PDF-Konverter](/heic-to-pdf/) nutzen (Tool-Seite auf Englisch) – er funktioniert genauso, akzeptiert aber nur HEIC-Dateien. Je nach iPhone-Einstellung wandelt iOS die Fotos beim Auswählen ohnehin schon in JPG um.

## Welche Einstellung für welchen Zweck?

**Formulare, Belege, Ausweise:** A4 mit kleinem Rand. So lässt sich die PDF später problemlos ausdrucken, und der Empfänger bekommt einheitliche Seiten.

**Fotoalbum oder Präsentation von Bildern:** „Fit page to image" ohne Rand. Jedes Bild füllt seine Seite komplett.

**Screenshots:** „Fit page to image" erhält das schmale Hochformat eines Handy-Screenshots, A4 würde viel Weißraum erzeugen.

## Die PDF ist zu groß?

Moderne Handykameras erzeugen große Fotos. Der Konverter rechnet sehr große Bilder bereits auf eine praktikable Auflösung herunter (auf maximal 2400 Pixel Breite) und speichert sie in hoher JPEG-Qualität. Bei vielen Seiten kann die PDF trotzdem mehrere Megabyte groß werden. Für E-Mail oder Upload-Portale verkleinern Sie die fertige Datei mit [PDF verkleinern](/de/pdf-verkleinern/) im Modus „Strong".

## Häufige Probleme

**Die Reihenfolge stimmt nicht.** Die Seiten folgen der Liste im Tool. Entfernen Sie falsch einsortierte Bilder mit ✕ und fügen Sie sie in der richtigen Reihenfolge wieder hinzu. Bei vielen Fotos hilft es, die Dateien vorher durchzunummerieren.

**Ein Foto liegt auf der Seite.** Manche Kameras speichern die Drehung nur als Zusatzinformation. Drehen Sie das Bild vorher in der Fotos-App und speichern Sie es erneut, oder drehen Sie die Seite nachträglich mit [PDF drehen](/rotate-pdf/) (Tool-Seite auf Englisch).

**Ich brauche die Bilder später wieder einzeln.** Dafür gibt es den umgekehrten Weg: [PDF in JPG umwandeln](/de/pdf-in-jpg-umwandeln/).

## Datenschutz

Ausweise, Gehaltszettel, Arztbriefe – Fotos von Dokumenten sind oft sehr persönlich. Bei DoraPDF werden die Bilder lokal in Ihrem Browser gelesen und zur PDF zusammengesetzt. Sie werden nicht auf einen Server hochgeladen, und es ist kein Konto nötig.

## Häufige Fragen

### Wie wandle ich mehrere JPG in eine PDF um?

Fügen Sie alle Bilder im Konverter hinzu, wählen Sie Seitengröße und Rand und klicken Sie auf „Create PDF". Jedes Bild wird eine Seite.

### Brauche ich eine App für das iPhone?

Nein. Safari genügt. Die PDF wird in der Dateien-App gespeichert.

### Kann ich A4 als Seitenformat wählen?

Ja. Wählen Sie „A4 page". Die Bilder werden auf die Seite eingepasst und zentriert.

### Funktioniert das auch mit PNG und HEIC?

Ja, neben JPG werden auch PNG, WebP und HEIC unterstützt.

### Ist das wirklich kostenlos?

Ja, ohne Anmeldung und ohne Wasserzeichen.
"""),
dict(slug='hintergrund-entfernen-kostenlos-ki', lang='de', title='Hintergrund entfernen kostenlos mit KI – Bilder freistellen im Browser', date='2026-11-15',
 desc='Hintergrund entfernen kostenlos mit KI: Personen, Produkte und Logos freistellen, transparent oder mit weißem Hintergrund. Das Foto bleibt auf Ihrem Gerät.',
 tools=['image-background-remover', 'image-compressor', 'images-to-pdf'], md="""
Ein Produktfoto für den Onlineshop, ein Porträt für die Bewerbung, ein Logo für die Vereinswebsite: Ständig braucht man Bilder ohne störenden Hintergrund. Früher hieß das, mit Lasso-Werkzeug und viel Geduld Kante für Kante nachzufahren. Heute können Sie den **Hintergrund entfernen – kostenlos und mit KI** – in wenigen Sekunden.

Der [Hintergrund-Entferner von DoraPDF](/de/hintergrund-entfernen/) stellt Personen, Produkte und Objekte automatisch frei. Das Besondere: Die KI läuft direkt in Ihrem Browser. Ihr Foto wird dafür nicht auf einen Server geladen.

## So funktioniert das Freistellen

Ein KI-Modell analysiert das Bild und berechnet für jedes Pixel, ob es zum Motiv oder zum Hintergrund gehört. Daraus entsteht eine Maske mit weichen Übergängen, damit Haare und Kanten nicht wie ausgeschnitten wirken. Das Modell wird beim ersten Einsatz einmal heruntergeladen und anschließend von Ihrem Browser zwischengespeichert. Das Foto selbst bleibt die ganze Zeit auf Ihrem Gerät.

## Quick oder HD – welcher Modus passt?

**⚡ Quick – Personen und Porträts.** Ein kleines Modell (etwa 13 MB), das auf praktisch jedem Gerät läuft, auch auf dem Handy. Es ist auf Menschen spezialisiert und eignet sich für Profilbilder, Bewerbungsfotos und Teamfotos.

**✨ HD – beliebige Objekte.** Ein deutlich größeres Modell (etwa 115 MB) mit sehr genauer Kantenerkennung für Produkte, Tiere, Möbel, Autos oder Logos. Es braucht einen aktuellen Browser mit Grafikbeschleunigung (WebGPU). Unterstützt Ihr Browser das nicht, wechselt das Tool automatisch zu Quick und zeigt einen Hinweis an.

Für ein Porträt reicht Quick fast immer. Für ein Produktfoto lohnt sich HD.

## Schritt für Schritt

1. Öffnen Sie [Hintergrund entfernen](/de/hintergrund-entfernen/).
2. Laden Sie ein Bild hoch – JPG, PNG, WebP oder auch HEIC vom iPhone.
3. Wählen Sie unter **Mode** Quick oder HD und unter **Background** den gewünschten neuen Hintergrund: **Transparent**, **White**, **Black**, **Pink** oder **Light grey**. (Die Bedienung ist auf Englisch.)
4. Klicken Sie auf **Remove background ✦**. Beim ersten Mal dauert es etwas länger, weil das Modell geladen wird.
5. Ziehen Sie den Schieberegler im Vorher-nachher-Vergleich, um das Ergebnis zu prüfen.
6. Laden Sie das Bild herunter. Es wird als PNG gespeichert, zum Beispiel `foto-no-bg.png`.

Sehr große Bilder werden für die Verarbeitung auf maximal 2000 Pixel Breite verkleinert – für Website, Shop und Social Media ist das reichlich.

## Transparent oder weiß?

**Transparenter Hintergrund** ist richtig, wenn Sie das Motiv später auf eine farbige Fläche, in eine Präsentation oder in ein Design setzen wollen. PNG speichert die Transparenz.

**Weißer Hintergrund** ist der Standard für viele Marktplätze und Onlineshops und eignet sich auch für Bewerbungsfotos, wenn ein ruhiger, heller Hintergrund gewünscht ist. Wählen Sie dafür direkt „White" – dann sparen Sie sich einen Bearbeitungsschritt.

**Hellgrau** wirkt bei Porträts oft weicher als reines Weiß.

## Tipps für saubere Kanten

- **Kontrast hilft.** Ein dunkles Motiv vor hellem Hintergrund (oder umgekehrt) wird präziser erkannt als ein grauer Pullover vor einer grauen Wand.
- **Scharfe Fotos verwenden.** Bewegungsunschärfe macht Kanten weich, und die KI kann nur erkennen, was im Bild steckt.
- **Genug Abstand.** Wenn das Motiv vom Bildrand abgeschnitten ist, ist das kein Problem. Aber Objekte, die das Motiv berühren (eine Hand auf einer Stuhllehne), werden manchmal mit freigestellt.
- **Feine Details** wie lockige Haare oder Fell gelingen mit HD meist besser.

## Wofür freigestellte Bilder praktisch sind

- **Onlineshop und Kleinanzeigen:** Produkte vor einheitlich weißem Hintergrund wirken aufgeräumter und lassen sich besser vergleichen.
- **Bewerbung und Profilbild:** Ein unruhiger Hintergrund aus Küche oder Wohnzimmer verschwindet, das Gesicht steht im Mittelpunkt.
- **Präsentationen und Flyer:** Mit transparentem Hintergrund setzen Sie ein Motiv auf jede Folie, ohne dass ein weißer Kasten stört.
- **Logos:** Ein eingescanntes oder fotografiertes Logo bekommt einen transparenten Hintergrund für Website oder Briefkopf. Dafür eignet sich der HD-Modus.

## Typische Probleme

**„AI model could not load".** Das Modell konnte nicht heruntergeladen werden. Prüfen Sie Ihre Internetverbindung und versuchen Sie es erneut. Nach dem ersten erfolgreichen Laden geht es deutlich schneller.

**HD wechselt zu Quick.** Ihr Browser unterstützt WebGPU nicht oder das Gerät hat keine passende Grafikbeschleunigung. Ein aktuelles Chrome oder Edge am Computer bietet die besten Chancen.

**Teile des Motivs fehlen.** Probieren Sie den jeweils anderen Modus. Quick ist für Personen optimiert und übersieht bei Produkten gelegentlich Details.

**Die Datei ist zu groß für den Shop.** PNG-Dateien mit Transparenz sind größer als JPG. Wenn Sie keinen transparenten Hintergrund brauchen, wählen Sie Weiß und verkleinern Sie das Ergebnis anschließend mit [Bild komprimieren](/de/bild-komprimieren/).

## Datenschutz: Ihre Fotos bleiben bei Ihnen

Gerade Porträts und Fotos von Kindern lädt man ungern auf fremde Server. Beim DoraPDF-Hintergrund-Entferner wird nur das KI-Modell aus dem Internet geladen. Die Berechnung findet vollständig in Ihrem Browser statt, Ihr Bild wird nicht übertragen. Ein Konto ist nicht nötig, und es gibt kein Wasserzeichen.

## Häufige Fragen

### Kann ich den Hintergrund wirklich kostenlos entfernen?

Ja. Das Tool ist kostenlos, ohne Anmeldung und ohne Wasserzeichen.

### Funktioniert das auch am Handy?

Ja. Der Quick-Modus läuft auch auf Smartphones. Der HD-Modus braucht WebGPU und ist am Computer zuverlässiger.

### In welchem Format wird das Bild gespeichert?

Als PNG, damit ein transparenter Hintergrund erhalten bleibt.

### Kann ich statt Transparenz einen weißen Hintergrund bekommen?

Ja, wählen Sie unter „Background" einfach „White".

### Wird mein Foto hochgeladen?

Nein. Die KI läuft in Ihrem Browser, nur das Modell wird einmalig heruntergeladen.
"""),
dict(slug='text-aus-bild-extrahieren-ocr-anleitung', lang='de', title='Text aus Bild extrahieren (OCR): So kopieren Sie Text aus Fotos und Screenshots', date='2026-11-15',
 desc='Text aus Bild extrahieren und kopieren: kostenlose OCR im Browser für Fotos, Screenshots und Scans – mit deutscher Spracherkennung inklusive Umlauten.',
 tools=['image-to-text', 'pdf-ocr', 'images-to-pdf'], md="""
Ein Rezept aus einem Kochbuch, eine Seite aus dem Skript, das Foto eines Aushangs, ein Screenshot mit einer Fehlermeldung: Den Text sieht man, aber markieren lässt er sich nicht. Statt alles abzutippen, können Sie den **Text aus dem Bild extrahieren** – per Texterkennung, kurz OCR (Optical Character Recognition).

Der [Bild-zu-Text-Konverter von DoraPDF](/de/text-aus-bild-extrahieren/) erkennt Text in Fotos, Screenshots und Scans und gibt ihn als kopierbaren Text aus. Kostenlos, ohne Anmeldung und direkt in Ihrem Browser.

## Der wichtigste Schritt: die richtige Sprache

Bevor es losgeht, ein Hinweis, der viel Ärger spart: Die Texterkennung arbeitet mit Sprachmodellen. Voreingestellt ist **English**. Für deutsche Texte sollten Sie unbedingt **German** auswählen. Sonst werden ä, ö, ü und ß oft falsch gelesen, und aus „Größe" wird schnell „GroBe".

Zur Auswahl stehen außerdem unter anderem Französisch, Spanisch, Italienisch, Portugiesisch, Türkisch, Russisch, Arabisch und vereinfachtes Chinesisch. Das Sprachmodell wird beim ersten Mal heruntergeladen (je nach Sprache etwa 2 bis 10 MB) und danach wiederverwendet.

## Anleitung: Text aus Bild kopieren

1. Öffnen Sie [Text aus Bild extrahieren](/de/text-aus-bild-extrahieren/).
2. Laden Sie ein oder mehrere Bilder hoch. Unterstützt werden gängige Bildformate wie JPG, PNG und WebP sowie HEIC vom iPhone.
3. Wählen Sie unter **Language** „German". (Die Bedienelemente des Tools sind auf Englisch.)
4. Klicken Sie auf **Extract text ✦**.
5. Der erkannte Text erscheint in einem Textfeld. Mit **Copy text** kopieren Sie ihn in die Zwischenablage, oder Sie laden ihn als `.txt`-Datei herunter.

Wenn Sie mehrere Bilder auf einmal verarbeiten, steht vor jedem Abschnitt der Dateiname. So wissen Sie, welcher Text aus welchem Foto stammt.

## So bekommen Sie bessere Ergebnisse

OCR ist gut, aber nicht magisch. Die Qualität des Fotos entscheidet über die Qualität des Textes:

- **Gerade fotografieren.** Halten Sie das Handy parallel zur Seite. Schräge Aufnahmen verzerren die Zeilen.
- **Gutes Licht, kein Blitz.** Blitzlicht erzeugt auf glänzendem Papier helle Flecken, in denen Buchstaben verschwinden.
- **Nah genug herangehen.** Der Text sollte einen großen Teil des Bildes füllen. Ein Foto der ganzen Pinnwand ergibt schlechtere Ergebnisse als ein Foto nur des Zettels.
- **Screenshots sind ideal.** Sie haben scharfe Schrift und hohen Kontrast und werden meist fast fehlerfrei erkannt.
- **Druckschrift statt Handschrift.** Gedruckter Text wird zuverlässig erkannt, Handschrift dagegen oft nur teilweise.

## Wofür sich das lohnt

**Studium und Schule:** Zitate aus Büchern übernehmen, Folien aus der Vorlesung als Text speichern, Notizen durchsuchbar machen. Prüfen Sie Zitate danach trotzdem gegen das Original – ein vertauschter Buchstabe im Zitat fällt auf.

**Büro:** Rechnungsnummern, IBANs oder Adressen aus einem fotografierten Brief übernehmen, statt sie abzutippen. Gerade bei Zahlen gilt: einmal genau vergleichen.

**Alltag:** Rezepte digitalisieren, Öffnungszeiten von einem Aushang speichern, Text aus einem Screenshot in eine Übersetzungs-App kopieren.

## Am Handy: Text aus Screenshot kopieren

Auch am Smartphone funktioniert die Texterkennung im Browser. Machen Sie einen Screenshot oder ein Foto, öffnen Sie das Tool in Safari oder Chrome und wählen Sie das Bild aus Ihrer Mediathek oder Galerie. Nach der Erkennung tippen Sie auf „Copy text" und fügen den Text in Notizen, Mail oder Messenger ein. Bei längeren Texten aus mehreren Bildern ist die Download-Funktion praktisch: Die `.txt`-Datei lässt sich in jeder Notiz-App öffnen.

## Und wenn der Text in einer PDF steckt?

Haben Sie ein eingescanntes Dokument als PDF, nutzen Sie den [PDF-OCR-Konverter](/pdf-ocr/) (Tool-Seite auf Englisch). Er erkennt den Text auf jeder Seite und liefert zwei Ergebnisse: eine **durchsuchbare PDF**, die genauso aussieht wie vorher, in der Sie aber Text markieren und suchen können, und eine Textdatei. Auch dort gilt: Sprache auf German stellen. Verarbeitet werden bis zu 60 Seiten pro Durchgang, mit etwa 5 bis 15 Sekunden pro Seite.

Umgekehrt können Sie mehrere fotografierte Seiten erst mit [JPG in PDF umwandeln](/de/jpg-in-pdf-umwandeln/) zu einer PDF zusammenfassen und diese dann per OCR durchsuchbar machen.

## Häufige Probleme

**„No readable text found in this image."** Das Bild enthält keinen erkennbaren Text oder ist zu unscharf, zu dunkel oder zu klein. Machen Sie ein neues, schärferes Foto.

**Umlaute fehlen oder sind falsch.** Die Sprache steht vermutlich noch auf English. Stellen Sie auf German um und starten Sie die Erkennung erneut.

**Spalten werden vermischt.** Bei mehrspaltigen Layouts wie Zeitungsartikeln kann die Reihenfolge durcheinandergeraten. Schneiden Sie das Bild vorher zu, sodass nur eine Spalte zu sehen ist.

**Die erste Erkennung dauert lange.** Das Sprachmodell wird beim ersten Mal geladen. Weitere Bilder in derselben Sprache gehen schneller.

## Datenschutz

Die Texterkennung läuft vollständig in Ihrem Browser. Ihre Bilder werden nicht auf einen Server hochgeladen – nur das Sprachmodell wird einmalig heruntergeladen. Das ist besonders angenehm bei Fotos von Briefen, Verträgen oder Ausweisen.

## Häufige Fragen

### Wie kann ich Text aus einem Bild kostenlos kopieren?

Laden Sie das Bild im Bild-zu-Text-Konverter hoch, wählen Sie die Sprache und klicken Sie auf „Extract text". Dann können Sie den Text kopieren oder als Datei speichern.

### Erkennt das Tool deutsche Umlaute?

Ja, wenn Sie als Sprache „German" auswählen.

### Funktioniert das am iPhone?

Ja, im Browser. Sie können Fotos aus der Mediathek wählen, auch im HEIC-Format.

### Kann ich mehrere Bilder auf einmal umwandeln?

Ja. Der Text aller Bilder wird nacheinander ausgegeben, jeweils mit dem Dateinamen davor.

### Wird Handschrift erkannt?

Gedruckter Text funktioniert am besten. Handschrift wird oft nur teilweise erkannt.
"""),
dict(slug='pdf-unterschreiben-ohne-drucken', lang='de', title='PDF unterschreiben ohne Drucken – am PC und am Handy', date='2026-11-15',
 desc='PDF unterschreiben ohne Drucken und Scannen: Unterschrift zeichnen oder tippen und einfügen. Kostenlos, ohne Anmeldung, die Datei bleibt im Browser.',
 tools=['sign-pdf', 'pdf-editor', 'pdf-merger'], md="""
Drucken, unterschreiben, einscannen, zurückschicken – für ein einziges Formular ist das ein erstaunlicher Aufwand, und oft steht gar kein Drucker in der Nähe. Für viele Alltagsdokumente geht es einfacher: Sie können eine **PDF unterschreiben ohne Drucken**, direkt am Bildschirm oder auf dem Handy.

Mit [PDF unterschreiben von DoraPDF](/de/pdf-unterschreiben/) zeichnen Sie Ihre Unterschrift mit Maus, Finger oder Stift oder tippen Ihren Namen in Schreibschrift. Danach wird sie in die PDF eingefügt. Kostenlos, ohne Anmeldung, und die Datei bleibt dabei in Ihrem Browser.

## Kurz vorab: Wofür reicht eine eingefügte Unterschrift?

Eine gezeichnete und in die PDF eingesetzte Unterschrift ist eine sogenannte einfache elektronische Signatur. Für sehr viele Situationen ist das völlig üblich: Einverständniserklärungen für Schule oder Verein, Auftragsbestätigungen, Stundenzettel, Angebote, Übergabeprotokolle oder interne Formulare.

Es gibt aber Dokumente, für die das Gesetz die Schriftform verlangt, also eine eigenhändige Unterschrift auf Papier oder eine qualifizierte elektronische Signatur. Ein bekanntes Beispiel ist die Kündigung eines Arbeitsvertrags. Wenn Sie unsicher sind, fragen Sie beim Empfänger nach, welche Form er akzeptiert. (Das ist ein allgemeiner Hinweis, keine Rechtsberatung.)

## Schritt für Schritt: Unterschrift in PDF einfügen

1. Öffnen Sie [PDF unterschreiben](/de/pdf-unterschreiben/).
2. **Unterschrift erstellen:** Zeichnen Sie im weißen Feld mit der Maus, dem Touchpad oder dem Finger. Alternativ tippen Sie Ihren Namen in das Feld darunter („…or type your name"), dann erscheint er in einer Schreibschrift. Mit **Clear** fangen Sie neu an. (Die Bedienelemente sind auf Englisch.)
3. **PDF hochladen:** Ziehen Sie das Dokument in das Upload-Feld.
4. **Position festlegen:**
   - **Page:** „last" für die letzte Seite – dort steht die Unterschriftenzeile meistens – oder eine Seitenzahl, zum Beispiel „2".
   - **Position:** unten rechts, unten links oder unten mittig.
   - **Size:** Mit dem Schieberegler bestimmen Sie die Breite der Unterschrift, zwischen 10 und 50 Prozent der Seitenbreite.
5. Klicken Sie auf **Sign PDF ✦** und laden Sie `dateiname-signed.pdf` herunter.
6. Öffnen Sie die Datei und prüfen Sie, ob die Unterschrift an der richtigen Stelle sitzt. Wenn nicht, passen Sie Position oder Größe an und erzeugen Sie die Datei mit dem Original noch einmal.

Die Unterschrift wird mit etwas Abstand zum unteren Seitenrand platziert. Sie ist ein Bild in der PDF und lässt sich nicht verrutschen, wenn der Empfänger die Datei öffnet.

## Am Handy unterschreiben

Am Smartphone ist das Unterschreiben fast angenehmer als am Computer, weil Sie mit dem Finger zeichnen. So gehen Sie vor:

- Öffnen Sie die Tool-Seite in Safari (iPhone) oder Chrome (Android).
- Drehen Sie das Handy ins Querformat, wenn Ihnen das Feld zu schmal ist.
- Zeichnen Sie langsam und gleichmäßig. Schnelle Bewegungen ergeben eckige Linien.
- Wählen Sie die PDF aus der Dateien-App, aus Ihren Downloads oder direkt aus einem Mail-Anhang, den Sie vorher gespeichert haben.

Die unterschriebene PDF landet in Ihren Downloads und kann von dort direkt per Mail oder Messenger verschickt werden.

## Eine schöne Unterschrift auf dem Bildschirm

Mit der Maus sieht eine Unterschrift selten so aus wie auf Papier. Ein paar Tricks:

- **Touchpad oder Touchscreen** sind meist besser als eine Maus. Ein Tablet mit Stift ist ideal.
- **Groß zeichnen.** Nutzen Sie das ganze Feld. Die Größe in der PDF stellen Sie danach mit dem Regler ein.
- **Getippte Variante** wirkt aufgeräumt, wenn das Zeichnen nicht gelingen will. Sie ist für formlose Dokumente meist völlig in Ordnung.

## Was das Tool nicht macht – und was Sie stattdessen tun

**Unterschrift mitten auf der Seite.** Das Tool setzt die Unterschrift immer an den unteren Rand: links, mittig oder rechts. Steht die Unterschriftenzeile weiter oben, ist die Platzierung unten trotzdem oft akzeptabel. Achten Sie dann darauf, dass nichts verdeckt wird.

**Ort und Datum ergänzen.** Mit dem [PDF-Editor](/pdf-editor/) (Tool-Seite auf Englisch) klicken Sie an eine beliebige Stelle der Seite und fügen Text ein – zum Beispiel „Berlin, 15.11.2026" neben der Unterschriftenzeile. Am besten erst Text ergänzen, dann unterschreiben.

**Mehrere Seiten paraphieren.** Pro Durchgang wird eine Seite unterschrieben. Für Kürzel auf mehreren Seiten laden Sie die bereits unterschriebene Datei erneut hoch und wählen die nächste Seite.

**Mehrere Dokumente auf einmal versenden.** Unterschreiben Sie jedes Dokument einzeln und fassen Sie sie danach mit [PDF zusammenfügen](/de/pdf-zusammenfuegen/) zu einer Datei zusammen.

## Häufige Probleme

**Die Unterschrift ist zu klein oder zu groß.** Ändern Sie den Regler „Size". Für ein normales A4-Formular sind 20 bis 30 Prozent ein guter Ausgangswert.

**Die PDF lässt sich nicht öffnen.** Ist sie passwortgeschützt, entfernen Sie den Schutz vorher mit [PDF-Passwort entfernen](/de/pdf-passwort-entfernen/), sofern Sie das Passwort kennen.

**Die Linien sind gestrichelt oder unterbrochen.** Zeichnen Sie langsamer. Auf manchen älteren Geräten werden schnelle Bewegungen nicht vollständig erfasst.

## Datenschutz

Ihre Unterschrift ist persönlich, und das Dokument oft auch. Bei DoraPDF wird beides lokal in Ihrem Browser verarbeitet: Die Unterschrift wird nicht gespeichert und die PDF nicht auf einen Server hochgeladen.

## Häufige Fragen

### Kann ich eine PDF kostenlos unterschreiben?

Ja, ohne Anmeldung, ohne Wasserzeichen und ohne Software-Installation.

### Kann ich am iPhone eine PDF unterschreiben?

Ja. Öffnen Sie das Tool in Safari, zeichnen Sie mit dem Finger und wählen Sie die PDF aus der Dateien-App.

### Ist die Unterschrift rechtsgültig?

Für viele formlose Dokumente ist eine eingefügte Unterschrift üblich. Wo das Gesetz Schriftform verlangt, reicht sie nicht. Fragen Sie im Zweifel beim Empfänger nach.

### Wird meine Unterschrift gespeichert?

Nein. Sie existiert nur in Ihrem Browser, solange die Seite geöffnet ist.

### Kann ich die Unterschrift frei auf der Seite verschieben?

Sie können sie unten links, mittig oder rechts platzieren und die Größe einstellen. Freies Verschieben gibt es nicht.
"""),
dict(slug='word-in-pdf-umwandeln-bewerbung', lang='de', title='Word in PDF umwandeln für Bewerbungen: Lebenslauf und Anschreiben richtig speichern', date='2026-11-15',
 desc='Word in PDF umwandeln für die Bewerbung: wann ein Online-Konverter reicht, worauf Personaler achten und wie Sie Lebenslauf und Zeugnisse bündeln.',
 tools=['word-to-pdf', 'pdf-merger', 'pdf-compressor'], md="""
Kaum ein Unternehmen möchte heute noch eine Bewerbung als Word-Datei. Der Grund ist einfach: Eine `.docx` sieht auf jedem Rechner etwas anders aus, Schriften fehlen, Zeilen rutschen. Eine PDF dagegen sieht beim Personaler genauso aus wie bei Ihnen. Deshalb gehört es zu den ersten Schritten jeder Bewerbung, **Word in PDF umzuwandeln**.

Hier erfahren Sie, welche Wege es gibt, wann der kostenlose [Word-zu-PDF-Konverter von DoraPDF](/de/word-in-pdf-umwandeln/) die richtige Wahl ist – und wann Sie besser den Export Ihres Textprogramms nehmen.

## Zwei Wege zur PDF

**Weg 1: Export direkt aus Word oder LibreOffice.** Wenn Sie Word auf dem Computer haben, ist „Datei → Speichern unter → PDF" (oder „Exportieren") der genaueste Weg. Schriftarten, Seitenränder, Kopf- und Fußzeilen bleiben exakt erhalten, und der Text in der PDF ist markierbar und durchsuchbar. LibreOffice Writer bietet dasselbe über „Datei → Exportieren als → Als PDF exportieren". Für den Lebenslauf ist das die erste Wahl, wenn Sie die Möglichkeit haben.

**Weg 2: Online-Konverter im Browser.** Praktisch, wenn Word nicht installiert ist: am Handy, auf einem Bibliotheksrechner, einem Chromebook oder wenn Sie nur eine `.docx` aus einer Mail haben. Der DoraPDF-Konverter wandelt die Datei kostenlos, ohne Anmeldung und ohne Upload direkt im Browser um.

## Was der DoraPDF-Konverter genau macht

Damit Sie wissen, was Sie erwarten können, ganz offen erklärt:

- Er liest **`.docx`-Dateien** (das aktuelle Word-Format). Alte `.doc`-Dateien müssen Sie vorher in Word oder LibreOffice als `.docx` speichern.
- Übernommen werden der **Inhalt und seine Struktur**: Überschriften, Absätze, Fett und Kursiv, Listen, Tabellen und eingebettete Bilder.
- Das Ergebnis ist eine **A4-PDF** mit einheitlicher, gut lesbarer Serifenschrift. Ihre Originalschriftarten, Farben, Textfelder, mehrspaltige Layouts sowie Kopf- und Fußzeilen werden nicht 1:1 nachgebaut.
- Die Seiten werden als Bilder in die PDF gesetzt. Der Text sieht gestochen scharf aus, ist aber **nicht markierbar** und nicht durchsuchbar. Seitenumbrüche setzt das Tool automatisch.

Für schlichte Dokumente wie ein einfaches Anschreiben, eine Liste oder einen Text ohne aufwendiges Design ist das ein schneller Weg. Für einen durchgestalteten Lebenslauf mit Spalten, Farbbalken und Foto ist der Export aus Word oder LibreOffice die bessere Wahl.

## Anleitung: Word in PDF umwandeln mit DoraPDF

1. Öffnen Sie [Word in PDF umwandeln](/de/word-in-pdf-umwandeln/).
2. Ziehen Sie Ihre `.docx`-Datei in das Upload-Feld.
3. Klicken Sie auf **Convert now ✦** (die Bedienung ist auf Englisch).
4. Laden Sie die PDF herunter. Aus `Anschreiben.docx` wird `Anschreiben.pdf`.
5. Öffnen Sie die PDF und blättern Sie einmal durch: Sitzen die Seitenumbrüche sinnvoll? Sind alle Bilder da?

## Checkliste für die Bewerbungs-PDF

Unabhängig davon, wie Sie die PDF erstellen – diese Punkte prüfen Personaler sofort:

**Dateiname:** `Lebenslauf_Anna_Schmidt.pdf` statt `CV_final_neu2.pdf`. Name und Dokumentart genügen.

**Eine Datei oder mehrere?** Lesen Sie die Stellenanzeige. Viele Unternehmen wünschen eine einzige PDF mit allen Unterlagen. Fügen Sie Anschreiben, Lebenslauf und Zeugnisse dann mit [PDF zusammenfügen](/de/pdf-zusammenfuegen/) zusammen – in genau dieser Reihenfolge.

**Dateigröße:** Bewerbungsportale und E-Mail-Postfächer haben Grenzen. Eingescannte Zeugnisse sind meist der Grund für zu große Dateien. Mit [PDF verkleinern](/de/pdf-verkleinern/) bringen Sie die Mappe auf eine handliche Größe; wählen Sie „Strong" mit „High quality" für die Scans.

**Durchsuchbarer Text:** Manche Unternehmen lesen Bewerbungen mit Software aus. Wenn Ihr Lebenslauf als Bild-PDF vorliegt, können Sie ihn mit dem [PDF-OCR-Konverter](/pdf-ocr/) (Tool-Seite auf Englisch, Sprache „German" wählen) nachträglich durchsuchbar machen. Noch einfacher ist es, den Lebenslauf direkt aus Word zu exportieren.

**Metadaten und Kommentare:** Entfernen Sie vor dem Export Kommentare und Änderungsverfolgung in Word. Sonst erscheinen sie im schlimmsten Fall am Rand der PDF.

**Foto:** Ein Bewerbungsfoto ist in Deutschland freiwillig. Wenn Sie eines einfügen, achten Sie auf eine gute Auflösung, damit es nicht pixelig wirkt.

## Word in PDF am Handy

Sie haben die `.docx` per Mail bekommen und müssen sie unterwegs als PDF weiterschicken? Speichern Sie den Anhang in der Dateien-App (iPhone) oder im Download-Ordner (Android), öffnen Sie den Konverter im Browser und wählen Sie die Datei aus. Die PDF landet in Ihren Downloads.

## Häufige Probleme

**Die Datei lässt sich nicht auswählen.** Wahrscheinlich ist es eine `.doc`- oder `.odt`-Datei. Speichern Sie sie als `.docx` oder nutzen Sie für OpenDocument-Dateien den [ODT-zu-PDF-Konverter](/odf-to-pdf/) (Tool-Seite auf Englisch).

**Die Schrift sieht anders aus als in Word.** Das ist beim Online-Konverter so gewollt: Er setzt eine einheitliche Schrift. Wenn Ihre Schriftart wichtig ist, exportieren Sie direkt aus Word.

**Ein Seitenumbruch liegt ungünstig.** Fügen Sie in Word an der passenden Stelle einen manuellen Seitenumbruch oder eine Leerzeile ein und wandeln Sie erneut um, oder nutzen Sie den Word-Export.

## Datenschutz

Lebensläufe enthalten Adresse, Geburtsdatum und Werdegang. Bei DoraPDF wird die Word-Datei in Ihrem Browser gelesen und dort in eine PDF umgewandelt. Sie wird nicht auf einen Server hochgeladen, und Sie brauchen kein Konto.

## Häufige Fragen

### Sollte ich meine Bewerbung als PDF oder Word schicken?

Als PDF, sofern die Stellenanzeige nichts anderes verlangt. Die PDF sieht beim Empfänger genauso aus wie bei Ihnen.

### Bleibt das Layout meines Lebenslaufs erhalten?

Beim Export aus Word ja, exakt. Der Online-Konverter übernimmt Inhalt und Struktur, setzt aber eine einheitliche Schrift und baut aufwendige Layouts nicht 1:1 nach.

### Kann ich Word ohne Office in PDF umwandeln?

Ja, mit dem kostenlosen DoraPDF-Konverter im Browser oder mit LibreOffice, das ebenfalls kostenlos ist.

### Wie füge ich Lebenslauf und Zeugnisse zu einer PDF zusammen?

Wandeln Sie alles in PDFs um und verbinden Sie die Dateien mit „PDF zusammenfügen" in der gewünschten Reihenfolge.

### Werden meine Bewerbungsunterlagen hochgeladen?

Nein. Die Umwandlung läuft vollständig in Ihrem Browser.
"""),
dict(slug='heic-in-jpg-umwandeln-windows', lang='de', title='HEIC in JPG umwandeln: iPhone-Fotos am Windows-PC öffnen', date='2026-11-15',
 desc='HEIC-Datei lässt sich unter Windows nicht öffnen? So können Sie HEIC in JPG umwandeln – mehrere Fotos auf einmal, kostenlos, ohne Programm und ohne Upload.',
 tools=['heic-to-jpg', 'images-to-pdf', 'image-compressor'], md="""
Sie haben Urlaubsfotos vom iPhone auf den Windows-Laptop kopiert, doppelklicken – und nichts passiert. Oder die Fotos-App meldet, dass eine Erweiterung fehlt. Das Bewerbungsportal lehnt die Datei ab, der Fotodrucker im Drogeriemarkt kennt sie nicht. Der Grund ist fast immer derselbe: Die Bilder liegen im **HEIC-Format** vor.

Die schnellste Lösung: **HEIC in JPG umwandeln**. Mit dem [HEIC-zu-JPG-Konverter von DoraPDF](/de/heic-in-jpg-umwandeln/) geht das kostenlos, für viele Fotos gleichzeitig und ohne Programm. Die Fotos werden in Ihrem Browser umgewandelt und nicht hochgeladen.

## Was ist HEIC überhaupt?

HEIC (High Efficiency Image Container) ist das Format, in dem iPhones standardmäßig Fotos speichern. Es braucht bei gleicher Bildqualität deutlich weniger Speicherplatz als JPG – für Apple-Geräte ein Vorteil. Außerhalb der Apple-Welt ist HEIC aber längst nicht überall angekommen. Windows kann HEIC nur mit einer zusätzlichen Erweiterung aus dem Microsoft Store anzeigen, und viele Websites, Formulare und ältere Programme akzeptieren nur JPG oder PNG.

JPG dagegen öffnet wirklich jedes Gerät. Deshalb ist die Umwandlung meist der einfachste Weg.

## Schritt für Schritt: HEIC in JPG konvertieren

1. Öffnen Sie [HEIC in JPG umwandeln](/de/heic-in-jpg-umwandeln/) in Chrome, Edge oder Firefox.
2. Markieren Sie im Explorer alle HEIC-Dateien (Strg + A im Ordner) und ziehen Sie sie in das Upload-Feld. Sie können auch nacheinander weitere Dateien hinzufügen.
3. Optional: Stellen Sie mit dem Regler **Quality** die JPG-Qualität ein. Voreingestellt sind 92 – ein guter Kompromiss aus Qualität und Dateigröße. (Die Bedienung ist auf Englisch.)
4. Klicken Sie auf **Convert now ✦**.
5. Für jedes Foto erscheint ein **Download**-Button. Aus `IMG_4021.HEIC` wird `IMG_4021.jpg`.

Die Fotos behalten ihre volle Auflösung. Es wird nichts beschnitten oder verkleinert.

## Welche Qualitätsstufe ist richtig?

- **90–100:** Für Fotos, die Sie ausdrucken oder weiter bearbeiten möchten. Die Dateien werden größer.
- **80–90:** Für Fotoalben, Messenger und E-Mail. Kaum sichtbarer Unterschied, merklich kleinere Dateien.
- **60–80:** Wenn ein Upload-Portal eine strenge Größenbeschränkung hat. Bei genauem Hinsehen werden Details weicher.

Brauchen Sie nur kleine Vorschaubilder, verkleinern Sie die JPGs anschließend mit [Bild komprimieren](/de/bild-komprimieren/).

## Weitere Wege – und wann sie sinnvoll sind

**HEIF-Erweiterung für Windows:** Über den Microsoft Store lässt sich die Erweiterung „HEIF-Bilderweiterungen" installieren. Danach zeigt die Fotos-App HEIC-Dateien an. Das hilft beim Anschauen, löst aber nicht das Problem mit Websites und Programmen, die nur JPG annehmen.

**iPhone gleich JPG speichern lassen:** Unter „Einstellungen → Kamera → Formate" können Sie „Maximale Kompatibilität" wählen. Dann speichert das iPhone neue Fotos als JPG. Bereits aufgenommene Bilder bleiben HEIC.

**Automatische Umwandlung beim Übertragen:** Unter „Einstellungen → Fotos" gibt es ganz unten die Option „Auf Mac oder PC übertragen". Steht sie auf „Automatisch", wandelt das iPhone Fotos beim Kopieren per Kabel in ein kompatibles Format um. Das funktioniert aber nicht bei jedem Übertragungsweg, etwa nicht bei Cloud-Downloads.

Für Fotos, die schon als HEIC auf Ihrem Rechner liegen, ist der Online-Konverter der direkteste Weg.

## Fotos als PDF statt als JPG?

Wenn Sie die Bilder nicht einzeln brauchen, sondern als ein Dokument – zum Beispiel fotografierte Belege für die Steuererklärung –, überspringen Sie den Zwischenschritt. Der Konverter [JPG in PDF umwandeln](/de/jpg-in-pdf-umwandeln/) liest HEIC direkt und macht aus mehreren Fotos eine einzige PDF, auf Wunsch im A4-Format.

Und für Grafiken oder Screenshots, bei denen Sie verlustfreie Qualität wollen, gibt es den [HEIC-zu-PNG-Konverter](/heic-to-png/) (Tool-Seite auf Englisch).

## Häufige Probleme

**Die Umwandlung dauert bei vielen Fotos etwas.** Jedes Bild wird auf Ihrem eigenen Rechner dekodiert. Bei hundert Fotos auf einmal kann das ein paar Minuten dauern. Arbeiten Sie bei sehr großen Mengen in Portionen von 20 bis 30 Bildern.

**Live Photos oder Serienbilder.** Aus einer HEIC-Datei wird das Hauptbild umgewandelt. Bewegungen eines Live Photos gehören nicht dazu.

**Eine Datei heißt .HEIF statt .HEIC.** HEIF ist die übergeordnete Formatfamilie; solche Dateien werden ebenfalls akzeptiert.

**Ich habe ein Android-Handy.** Manche Android-Kameras speichern ebenfalls HEIC/HEIF. Der Konverter funktioniert auch mit diesen Dateien.

## Datenschutz

Familienfotos, Kinderbilder, Fotos von Dokumenten: Das sind keine Dateien, die man gern auf fremde Server lädt. Bei DoraPDF werden die HEIC-Dateien mit einer JavaScript-Bibliothek direkt in Ihrem Browser in JPG umgewandelt. Sie verlassen Ihren Computer nicht, und es ist keine Anmeldung nötig.

## Häufige Fragen

### Wie kann ich HEIC kostenlos in JPG umwandeln?

Ziehen Sie die Fotos in den HEIC-zu-JPG-Konverter, klicken Sie auf „Convert now" und laden Sie die JPGs herunter. Kostenlos und ohne Anmeldung.

### Kann ich mehrere HEIC-Dateien gleichzeitig umwandeln?

Ja. Wählen Sie beliebig viele Dateien aus. Jedes Foto bekommt einen eigenen Download-Button.

### Verliere ich beim Umwandeln Qualität?

Die Auflösung bleibt gleich. JPG komprimiert etwas stärker als HEIC; mit Qualität 90 oder höher ist der Unterschied praktisch nicht sichtbar.

### Warum kann Windows HEIC nicht öffnen?

Windows bringt HEIC-Unterstützung nicht immer von Haus aus mit. Sie brauchen eine Erweiterung aus dem Microsoft Store oder wandeln die Fotos in JPG um.

### Werden meine Fotos hochgeladen?

Nein. Die Umwandlung passiert vollständig in Ihrem Browser.
"""),
dict(slug='pdf-in-excel-umwandeln-tabellen', lang='de', title='PDF in Excel umwandeln: Tabellen aus PDF kostenlos übernehmen', date='2026-11-15',
 desc='Tabelle aus PDF in Excel übernehmen statt abtippen: PDF in Excel umwandeln, kostenlos und ohne Upload. Mit Tipps zu Zahlenformaten und gescannten PDFs.',
 tools=['pdf-to-excel', 'pdf-ocr', 'pdf-splitter'], md="""
Der Kontoauszug als PDF, die Preisliste des Lieferanten, die Notenübersicht, die Statistik aus einem Bericht: Die Zahlen stehen sauber in einer Tabelle – nur eben in einer PDF, in der man nicht rechnen kann. Kopieren und Einfügen endet meist damit, dass alles in einer einzigen Spalte landet.

Besser: **PDF in Excel umwandeln**. Der [PDF-zu-Excel-Konverter von DoraPDF](/de/pdf-in-excel-umwandeln/) liest Tabellen und Text aus Ihrer PDF und verteilt sie auf Zeilen und Spalten einer `.xlsx`-Datei. Kostenlos, ohne Anmeldung, und die PDF wird in Ihrem Browser verarbeitet statt auf einem Server.

## So erkennt das Tool Tabellen

Eine PDF weiß nicht, dass sie eine Tabelle enthält. Sie kennt nur Textstücke an bestimmten Positionen. Der Konverter rekonstruiert daraus die Struktur:

- Textstücke auf **derselben Höhe** werden zu einer Zeile.
- Ein **größerer horizontaler Abstand** zwischen zwei Textstücken bedeutet eine neue Spalte.
- Werte, die wie Zahlen aussehen, werden als **echte Zahlen** gespeichert, mit denen Sie sofort rechnen können.
- **Jede PDF-Seite** landet auf einem eigenen Tabellenblatt: „Page 1", „Page 2" und so weiter.
- Die **Spaltenbreiten** werden automatisch an den Inhalt angepasst.

Das funktioniert besonders gut bei klar gegliederten Tabellen, wie sie in Rechnungen, Listen und Berichten üblich sind.

## Anleitung: Tabelle aus PDF in Excel übernehmen

1. Öffnen Sie [PDF in Excel umwandeln](/de/pdf-in-excel-umwandeln/).
2. Ziehen Sie die PDF in das Upload-Feld.
3. Klicken Sie auf **Convert now ✦** (die Bedienung ist auf Englisch).
4. Laden Sie die `.xlsx`-Datei herunter. Sie trägt den Namen Ihrer PDF.
5. Öffnen Sie sie in Excel, LibreOffice Calc, Numbers oder Google Sheets.

## Wichtig bei deutschen Zahlen: Komma und Punkt prüfen

Hier lauert der häufigste Fehler beim Import – und es lohnt sich, ihn zu kennen. Der Konverter erkennt Zahlen im **englischen Format**: Der Punkt ist das Dezimalzeichen, das Komma das Tausendertrennzeichen. Deutsche Beträge sind genau umgekehrt geschrieben. Das heißt:

- Ein Betrag wie **12,50** kann in Excel als **1250** ankommen.
- Ein Betrag wie **1.234,56** kann als **1,23456** erscheinen.

Kontrollieren Sie deshalb nach der Umwandlung immer ein paar Werte in Spalten mit Beträgen gegen die Original-PDF. Liegt der Fehler vor, sind die Zahlen der betroffenen Spalte systematisch verschoben; bei Beträgen mit zwei Nachkommastellen können Sie sie zum Beispiel in einer Hilfsspalte durch 100 teilen. Am sichersten ist es, jede Summe einmal mit der Summe in der PDF zu vergleichen. Englischsprachige PDFs, etwa Rechnungen in US-Dollar, sind davon nicht betroffen.

## Gescannte PDFs: erst OCR, dann Excel

Erscheint die Meldung „No text found – this PDF looks scanned", enthält Ihre PDF nur Bilder der Seiten, aber keinen echten Text. Das ist bei eingescannten Kontoauszügen oder abfotografierten Listen der Fall. Die Lösung:

1. Machen Sie die PDF mit dem [PDF-OCR-Konverter](/pdf-ocr/) durchsuchbar (Tool-Seite auf Englisch). Wählen Sie als Sprache „German".
2. Wandeln Sie die erzeugte durchsuchbare PDF dann in Excel um.

Bei Texterkennung können einzelne Ziffern falsch gelesen werden, etwa eine 1 als l oder eine 0 als O. Prüfen Sie die Zahlen danach besonders sorgfältig.

## Tipps für saubere Ergebnisse

**Nur die relevanten Seiten umwandeln.** Ein 30-seitiger Geschäftsbericht mit einer einzigen Tabelle auf Seite 17 ergibt 30 Tabellenblätter. Extrahieren Sie die Seite vorher mit [PDF teilen](/de/pdf-teilen/) – dann bekommen Sie genau ein Blatt.

**Überschriften und Fußnoten löschen.** Auch Text außerhalb der Tabelle wird übernommen, zum Beispiel Kopfzeilen, Seitenzahlen oder Fußnoten. Diese Zeilen löschen Sie in Excel mit wenigen Klicks.

**Mehrzeilige Zellen zusammenführen.** Wenn eine Tabellenzelle in der PDF über zwei Zeilen geht, entstehen in Excel zwei Zeilen. Fügen Sie die Inhalte bei Bedarf zusammen.

**Mehrere Seiten zu einer Tabelle verbinden.** Geht eine Tabelle über mehrere PDF-Seiten, kopieren Sie die Zeilen der Blätter „Page 2", „Page 3" usw. unter die Daten von „Page 1".

**Datumsangaben prüfen.** Datumsangaben bleiben als Text erhalten. Mit „Daten → Text in Spalten" oder einer Formel wandeln Sie sie bei Bedarf in echte Excel-Datumswerte um.

## Wann Word die bessere Wahl ist

Enthält Ihre PDF überwiegend Fließtext mit nur wenigen Zahlen, ist Excel nicht ideal. Dann wandeln Sie sie besser mit [PDF in Word umwandeln](/de/pdf-in-word-umwandeln/) um und kopieren die einzelne Tabelle von dort.

## Datenschutz

Kontoauszüge, Gehaltslisten, Kundendaten – Tabellen in PDFs sind häufig vertraulich. Der DoraPDF-Konverter liest die PDF direkt in Ihrem Browser aus und erstellt dort die Excel-Datei. Ihre Daten werden nicht auf einen Server übertragen.

## Häufige Fragen

### Wie übernehme ich eine Tabelle aus einer PDF in Excel?

Laden Sie die PDF in den PDF-zu-Excel-Konverter, klicken Sie auf „Convert now" und öffnen Sie die heruntergeladene `.xlsx`-Datei.

### Ist das kostenlos?

Ja, ohne Anmeldung und ohne Wasserzeichen.

### Warum stimmen meine Beträge nicht?

Wahrscheinlich wurden deutsche Zahlen mit Dezimalkomma als englisches Format gelesen. Prüfen Sie die Beträge und korrigieren Sie die betroffene Spalte.

### Funktioniert das mit gescannten PDFs?

Erst nach einer Texterkennung mit dem OCR-Tool. Danach können Sie die durchsuchbare PDF umwandeln.

### Kann ich die Datei in Google Sheets öffnen?

Ja. Laden Sie die `.xlsx`-Datei in Google Drive hoch und öffnen Sie sie mit Google Sheets.
"""),
dict(slug='convert-pdf-to-txt-extract-text-free', title='How to Convert PDF to TXT and Extract All the Text (Free, Online)', date='2026-11-14',
 desc='Pull every word out of a PDF into a plain .txt file you can copy, search or paste anywhere. Free, no sign-up, and the file never leaves your browser.',
 tools=['pdf-to-txt', 'pdf-ocr', 'pdf-to-word'], md="""
Sometimes you don't want the PDF at all. You want the words inside it: a quote for an essay, a list of names to paste into a spreadsheet, a policy to drop into an email, or a long report to feed into a translation tool. Selecting text in a PDF viewer works for a paragraph, but it gets messy fast across twenty pages.

The quicker route is to **convert PDF to TXT**. DoraPDF's [PDF to TXT Converter](/pdf-to-txt/) reads the text layer of your PDF and gives you all of it as a plain `.txt` file, plus a copy-ready box on the page. It's free, there's no account, and the PDF is processed inside your own browser.

## When plain text beats a Word file

If you need headings, tables and fonts kept, a Word document is the better target, and [PDF to Word](/pdf-to-word/) is the tool for that. Plain text is the right choice when:

- You're pasting into something that strips formatting anyway, like a web form, a chat app, a code editor or a notes app.
- You want to search the content with a text editor or count words.
- You're preparing material for an AI chatbot, a translator or a text-to-speech app.
- You need a lightweight copy of a long document that opens on any device, even an old phone.

A `.txt` file has no styling to break, which is exactly why it travels so well.

## How to extract text from a PDF on DoraPDF

1. Open the [PDF to TXT Converter](/pdf-to-txt/).
2. Drop your PDF onto the upload area, or tap to choose it. The tool works on one PDF at a time.
3. Press **Convert now**. A progress bar moves through the pages.
4. When it finishes, the extracted text appears in the **Text** box. Use **Copy** to grab all of it, or download the `.txt` file, which keeps your PDF's name (for example `report.pdf` becomes `report.txt`).

That's the whole process. On a phone it works the same way in Chrome or Safari, and the text file lands in your downloads or Files app.

## What the output looks like

The converter rebuilds the text line by line. It groups words that sit on the same horizontal line of the page and reads them from left to right, then moves down the page. Each page is separated from the next by a blank line, so you can still tell where one page ends.

Things that don't come across, because plain text can't hold them:

- Bold, italics, font sizes and colours
- Images, charts and logos
- Table borders (the cell contents do come through, as words on a line)

## Common problems and how to fix them

**"No text found — the PDF may be scanned."** This message means the PDF is a picture of a page, not real text. Scanned contracts, phone scans and photographed notes usually fall into this group. Run the file through [PDF OCR](/pdf-ocr/) first to recognise the text, or use [Image to Text](/image-to-text/) if you have the page as a photo.

**Two columns got mixed together.** Because the tool reads each line across the full width of the page, newspaper-style layouts and two-column research papers can come out with the left and right columns joined on the same line. For those files, copy one column at a time from a PDF viewer, or convert with [PDF to Word](/pdf-to-word/) and work from there.

**Strange spacing or words stuck together.** Some PDFs place every letter separately. The converter adds a space when it sees a clear gap between pieces of text, but unusual fonts can still produce the odd joined word. A quick find-and-replace in any text editor tidies this up.

**The file won't open at all.** If the PDF is password-protected, remove the password first with [Unlock PDF](/unlock-pdf/) (you'll need to know the password), then convert.

**Hyphenated words at line ends.** If the original document split words with hyphens at the end of lines, those hyphens are part of the text and will stay. Search for "- " followed by a line break if you want to rejoin them.

## Practical examples

- **A student** downloads a 40-page journal article and converts it to TXT to search for every mention of a key term before writing a literature review.
- **An office assistant** receives a PDF list of 300 attendees and pastes the text into a spreadsheet, then splits it into columns.
- **A teacher** extracts the text of a worksheet to edit it in a simple editor and reprint a new version.
- **A developer** pulls the wording out of a PDF spec so it can be pasted into documentation.

## Tips for cleaner results

- Convert the original digital PDF where possible, not a printed-and-rescanned copy. Digital PDFs give perfect text; scans need OCR and are never quite as clean.
- If you only need a few pages, cut them out first with [Split PDF](/pdf-splitter/). Smaller input means less tidying afterwards.
- Want headings kept for an AI tool? Try [PDF to Markdown](/pdf-to-markdown/) instead. It marks larger text as headings and bullets as list items, which chatbots understand well.
- Paste the result into the [Quick Text Formatter](/text-formatter/) to remove extra spaces or empty lines in one click.

## Is it private?

Yes. The PDF to TXT Converter runs entirely in your browser. Your PDF is read on your own device and is not uploaded to DoraPDF's server, which makes it fine for payslips, contracts or exam papers you'd rather not send anywhere.

## FAQ

**Is converting PDF to TXT free?**
Yes, completely. There's no sign-up, no watermark and no daily limit built into the tool.

**Can I convert a scanned PDF to text?**
Not directly. Scanned pages have no text layer, so run them through [PDF OCR](/pdf-ocr/) first, then convert.

**Does it keep Urdu or other non-English text?**
It extracts whatever text is stored in the PDF, so other languages usually come through. Right-to-left scripts may need a little cleanup of word order depending on how the PDF was created.

**Can I convert several PDFs at once?**
The tool handles one PDF per run. Convert them one after another, or join them first with the [PDF Merger](/pdf-merger/) and convert the merged file.

**What's the difference between PDF to TXT and PDF to Word?**
TXT gives you only the words. Word tries to keep layout, headings and tables so you can edit the document properly.
"""),
dict(slug='pdf-to-markdown-for-chatgpt-ai', title='PDF to Markdown for ChatGPT and Other AI Tools: A Free, Private Converter', date='2026-11-14',
 desc='Turn a PDF into clean Markdown with headings and bullet points kept, ready to paste into ChatGPT, Claude, Notion or Obsidian. Runs in your browser.',
 tools=['pdf-to-markdown', 'pdf-to-txt', 'markdown-to-pdf'], md="""
Paste a long PDF into an AI chat and you often get a wall of text with no sense of what's a heading, what's a list and where one section ends. The model still reads it, but it has to guess the structure, and answers get vaguer as a result.

Converting **PDF to Markdown** first fixes most of that. Markdown is a plain-text format that marks structure with simple symbols: `#` for a heading, `-` for a bullet point. AI tools like ChatGPT and Claude read it naturally, and so do note apps such as Notion and Obsidian. DoraPDF's [PDF to Markdown](/pdf-to-markdown/) converter does this in your browser, free, without uploading the file.

## What the converter actually does

It's worth knowing how the tool decides what's what, because that tells you which PDFs will convert well.

1. It reads the text on each page and groups words into lines.
2. It works out the typical text size on that page.
3. Lines noticeably bigger than normal become headings. The larger the text, the higher the level: very large lines get `#`, large ones `##`, slightly larger ones `###`.
4. Lines starting with a bullet character (•, ●, ▪ or -) become Markdown list items starting with `- `.
5. Everything else becomes a normal paragraph, and pages are separated with a `---` divider.

So a report with a clear title, section headings in bigger type and bulleted lists converts very nicely. A PDF where every line is the same size will come out as plain paragraphs, which is still clean, just flatter.

### A quick before-and-after

A page that looks like this in the PDF:

> **Annual Safety Review** (large title)
> **Key findings** (medium heading)
> • Fewer incidents than last year
> • Training completed by all staff

comes out roughly like this:

    # Annual Safety Review

    ## Key findings

    - Fewer incidents than last year

    - Training completed by all staff

## How to convert a PDF to Markdown

1. Go to [PDF to Markdown](/pdf-to-markdown/).
2. Add your PDF by dropping it on the page or tapping to browse.
3. Press **Convert now** and wait for the progress bar.
4. Check the **Preview** box. You can **Copy** the Markdown straight from there, or download the `.md` file, which is named after your PDF.

Then paste it into your AI chat, or save the `.md` file into your notes folder.

## Using the Markdown with AI tools

A few habits that get better answers:

- **Tell the model what it's looking at.** Start with a line like "Below is the text of a lecture handout in Markdown," then paste.
- **Send long documents in sections.** The `---` dividers mark page breaks, which makes it easy to split a 60-page file into chunks of a few pages each.
- **Ask structure-aware questions.** Because headings are kept, you can ask "Summarise the section called Methods" and the model can find it.
- **Remove what you don't need.** Delete repeated headers, footers or reference lists before pasting. Fewer words means more room for the part you care about.

Students using DoraPDF's Assignment Helper can use the same trick: convert course readings to Markdown, then use them as source material when building an outline or checking which points a reading actually covers.

## When to choose Markdown, TXT or Word

| You want… | Use |
|---|---|
| Headings and lists kept as plain text | [PDF to Markdown](/pdf-to-markdown/) |
| Just the words, nothing else | [PDF to TXT](/pdf-to-txt/) |
| An editable document with layout and tables | [PDF to Word](/pdf-to-word/) |
| A spreadsheet from tables in the PDF | [PDF to Excel](/pdf-to-excel/) |

## Problems you might run into

**The output is empty or the tool reports no text.** The PDF is probably a scan, meaning each page is a photo. Make it searchable with [PDF OCR](/pdf-ocr/) first, then convert again.

**Headings appear where they shouldn't.** Large numbers on a cover page, pull quotes or big captions can be marked as headings because of their size. Delete the stray `#` symbols; it takes seconds.

**Tables come out as lines of words.** The converter doesn't build Markdown tables. Cell contents appear on lines in reading order. For data-heavy tables, [PDF to Excel](/pdf-to-excel/) is the better tool.

**Two-column papers get jumbled.** The tool reads each line across the full page, so side-by-side columns can merge. Check those sections before relying on them.

**Every bullet has a blank line after it.** That's how the converter spaces items. Markdown renders it fine, and AI tools don't care, but you can remove the gaps in a text editor if you prefer a tighter list.

## Privacy

Everything happens in your browser. The PDF isn't sent to DoraPDF's server, which matters if you're converting confidential notes, client documents or unpublished research before deciding what to share with an AI service. What you paste into a chatbot afterwards is, of course, up to you and that service's own policies.

## FAQ

**Is this PDF to Markdown converter free?**
Yes. No account, no watermark.

**Can ChatGPT read the .md file directly?**
Most AI chat apps accept pasted Markdown, and many also let you attach `.md` files. Pasting the text from the Copy button works everywhere.

**Will images from the PDF be included?**
No. The tool extracts text only. If you need the pictures too, use the [PDF Image Extractor](/pdf-image-extractor/).

**Does it work on a phone?**
Yes. It runs in mobile browsers, though very large PDFs will convert faster on a computer.

**Can I turn the Markdown back into a PDF later?**
Yes. Edit it, then export it with [Markdown to PDF](/markdown-to-pdf/).
"""),
dict(slug='highlight-words-in-pdf-online-free', title='How to Highlight Text in a PDF Online for Free (Every Match, Automatically)', date='2026-11-14',
 desc='Type the words you care about and highlight every occurrence across a whole PDF in yellow, green, pink or blue. Free, no sign-up, works in your browser.',
 tools=['highlight-pdf', 'pdf-editor', 'redact-pdf'], md="""
Most PDF highlighters work like a marker pen: you drag across a sentence, then the next one, then the next. That's fine for a page of notes. It's painful when you want to find every mention of "deadline" in a 50-page tender document, or every place a contract says "penalty".

DoraPDF's [Highlight PDF](/highlight-pdf/) tool takes the other approach. You **type the words**, pick a colour, and it **highlights text in the PDF** everywhere those words appear, on every page, in one go. It's free, online, and runs inside your browser.

## Good jobs for automatic highlighting

- **Reviewing contracts.** Highlight "terminate, penalty, liability, renewal" to see the risky clauses at a glance.
- **Studying.** Mark every key term from your syllabus in a set of lecture notes before revision.
- **Checking a report.** Highlight a client's name or a product name to make sure it's spelled the same way throughout.
- **Job hunting.** Highlight the skills a job advert asks for inside your own CV, and see which ones you never mention.
- **Teaching.** Highlight vocabulary words in a reading passage before printing it for a class.

## Step by step: highlight words in a PDF

1. Open [Highlight PDF](/highlight-pdf/) on DoraPDF.
2. Add your PDF.
3. In **Words to highlight (comma separated)**, type what you're looking for, for example: `revenue, deadline, Q3`.
4. Choose a **Color**: Yellow, Green, Pink or Blue.
5. Press **Highlight**. The tool scans each page and draws a see-through coloured box over every match.
6. Download the result. It's saved as your file name plus `-highlighted.pdf`, and the download label shows how many highlights were added, such as "27 highlights".

The original text stays readable under the colour, and the rest of the PDF is left as it was.

## How matching works (read this before you type)

Knowing these rules saves you a lot of trial and error:

- **Not case-sensitive.** `invoice` matches "Invoice", "INVOICE" and "invoice".
- **Matches parts of words.** The tool looks for your text inside words, too. `art` will also light up "start" and "party". To avoid that, type a longer, more specific word.
- **Commas separate search terms.** `late fee, interest` searches for "late fee" and "interest" separately. Extra spaces around commas are ignored.
- **Short phrases work best.** A phrase is found when it sits together on the same line of the PDF. If a phrase breaks across two lines, it won't match as a whole; highlight the most distinctive word instead.
- **One colour per run.** Want terms in different colours? Run the tool once with yellow for one set of words, then upload the highlighted file again and run it with green for the next set.

## If nothing gets highlighted

**"None of those words were found."** Check spelling first. If the spelling is right, the PDF is probably a scanned image with no real text inside. Run it through [PDF OCR](/pdf-ocr/) to add a text layer, then highlight the OCR'd file.

**A highlight is slightly off to one side.** The tool estimates each letter's position from the width of the text around it. In fonts where letters vary a lot in width, a box can sit a little left or right of the word. It's still easy to spot, and for most reviewing work that's all you need.

**The file won't load.** Password-protected PDFs need unlocking first with [Unlock PDF](/unlock-pdf/), using the password you already have.

## Highlighting vs. other ways to mark a PDF

Highlighting draws attention to text but doesn't hide anything. If the goal is the opposite, removing sensitive details like ID numbers or addresses before sharing, use [Redact PDF](/redact-pdf/), which blacks out content instead. If you want to type your own comments onto the pages, the [PDF Editor](/pdf-editor/) lets you click anywhere on a page to add text.

## Tips from real use

- **Start broad, then narrow.** Run one pass with a single important word to see how many hits you get. If it's hundreds, switch to more specific terms.
- **Use yellow for printing.** Yellow is the easiest colour to read through on paper, especially on cheaper printers.
- **Name the output clearly.** If you're making several versions, rename them, for example `contract-risks.pdf` and `contract-dates.pdf`.
- **Combine with a reading pass.** Highlighting finds the words; it doesn't judge them. Read each highlighted sentence in context, especially in legal documents.

## Privacy

The PDF never leaves your device. Highlight PDF loads and edits the file inside your browser, so confidential agreements, exam papers and internal reports aren't uploaded to DoraPDF's server.

## FAQ

**Is it free to highlight a PDF here?**
Yes. No sign-up and no watermark on the highlighted file.

**Can I highlight a PDF on my phone?**
Yes. The tool runs in Chrome, Safari and other mobile browsers. Type the words with your phone keyboard as normal.

**Will the highlights show in Adobe Reader or other viewers?**
Yes. The coloured boxes are drawn onto the pages, so they appear in any PDF viewer and when printed.

**Can I remove a highlight afterwards?**
The highlights are part of the saved page, so keep your original PDF if you might want a clean copy later.

**How many words can I search for at once?**
As many as you like, separated by commas. Long lists just take a little longer to process on big files.
"""),
dict(slug='convert-epub-to-pdf-free-online', title='Convert EPUB to PDF Free Online: Read Any E-book as a Simple PDF', date='2026-11-14',
 desc='Turn an EPUB e-book into a clean, text-based PDF you can open on any device, print or annotate. Free, no software, and the book stays on your device.',
 tools=['epub-to-pdf', 'pdf-compressor', 'highlight-pdf'], md="""
EPUB is a great format for e-readers because the text reflows to fit any screen. It's less great when you want to print a chapter, open the book on a computer that has no e-book app, or send a reading to someone who only knows how to open PDFs.

DoraPDF's [EPUB to PDF Converter](/epub-to-pdf/) solves that. It lets you **convert EPUB to PDF free online**, straight in your browser, without installing an e-book manager. This guide covers how it works, what kind of PDF you'll get, and how to handle the tricky cases.

## What kind of PDF to expect

It helps to know this up front: the converter produces a **clean, text-focused PDF**, not a page-by-page copy of the book's design.

Here's what it does:

- Reads the book's title from its metadata and puts it at the top of the first page.
- Goes through the chapters in the book's reading order.
- Pulls out headings, paragraphs and list items as plain text.
- Lays everything out on A4 pages with simple, readable type and normal margins.

Here's what it leaves out:

- Pictures, covers, maps and illustrations
- Fancy fonts, colours, bold and italic styling
- Tables as tables (their text may come through, but without the grid)

For novels, essays, study texts and most non-fiction, that's all you need. For a cookbook full of photos or a comic, you'll be disappointed, so it's better to know now.

## How to convert an EPUB to PDF

1. Open the [EPUB to PDF Converter](/epub-to-pdf/).
2. Drop your `.epub` file on the upload area, or tap to choose it from your device.
3. Press **Convert now**. The progress bar moves as each chapter is processed.
4. Download the PDF. It keeps the same name as your e-book file, with `.pdf` at the end.

That's it. There's no account and no email step.

## Why people convert EPUB to PDF

- **Printing.** Many e-book apps don't print at all. A PDF prints from any computer.
- **Annotating.** PDF readers on laptops and tablets have better tools for notes and highlighting than some e-book apps. You can even auto-highlight key terms with [Highlight PDF](/highlight-pdf/).
- **Sharing a public-domain classic.** Free books from public-domain libraries often come as EPUB; a PDF is easier for some readers to open.
- **Course readings.** A teacher who writes handouts as EPUB can give students a PDF version that works on school computers.
- **Archiving your own writing.** Authors who export drafts to EPUB can keep a PDF copy for proofreading on paper.

## Problems and fixes

**The PDF has strange symbols instead of letters.** The converter uses a standard PDF font that covers English and other Latin-alphabet languages well. Books in Urdu, Arabic, Chinese or other non-Latin scripts may not display correctly in the PDF. For those, an e-book app with a "print to PDF" option is the safer route.

**The book won't convert, or the text is gibberish.** Many e-books bought from online stores are protected with DRM (copy protection). Their content is encrypted, so no converter can read it without the store's own app. The tool works with DRM-free EPUB files, such as public-domain books, files you created yourself, or books sold without DRM.

**An error appears straight away.** The file may not be a real EPUB, or it may be damaged. A valid EPUB is a zipped package with a specific structure inside; files renamed from another format to `.epub` won't work.

**Some chapters seem to be missing.** The tool follows the book's official reading order. Extra material that isn't part of that order, such as some notes pages, may be skipped.

**The PDF is longer than expected.** E-book text has no fixed page count, so a 250-page paperback can easily become 300+ A4 pages, depending on the book. If the file is too large to email, shrink it with the [PDF Compressor](/pdf-compressor/).

## Tips for a nicer result

- If you only need a few chapters, convert the full book and then pull out the pages you want with [Split PDF](/pdf-splitter/).
- To print a long book cheaply, print two pages per sheet from your printer settings; the simple layout stays readable even at a smaller size.
- If you have a Kindle book in MOBI format instead, DoraPDF also has a [MOBI to PDF](/mobi-to-pdf/) converter.
- Keep the original EPUB. It's still the better format for reading on a phone, because the text resizes to fit.

## Privacy

The conversion happens entirely in your browser. Your e-book is opened and turned into a PDF on your own device and isn't uploaded to DoraPDF's server.

## FAQ

**Is the EPUB to PDF converter really free?**
Yes. There's no sign-up, no watermark and no trial.

**Can I convert EPUB to PDF on iPhone or Android?**
Yes. Open the tool in your phone's browser, pick the `.epub` file from Files or Downloads, and save the PDF the same way.

**Will the cover image be included?**
No. The converter keeps the text only, so covers and illustrations are left out.

**Can I convert Kindle books?**
Only DRM-free files. Store-bought Kindle and other protected e-books can't be read by any outside converter.

**Does it keep chapter headings?**
The heading text is kept in the right place, but it's written in the same plain style as the rest of the text, without larger fonts.
"""),
dict(slug='convert-eml-email-to-pdf-free', title='How to Save an Email as PDF: Convert EML Files to PDF Free', date='2026-11-14',
 desc='Turn a saved .eml email from Gmail, Outlook, Thunderbird or Apple Mail into a tidy PDF with sender, date and subject. Free, private, no software.',
 tools=['email-to-pdf', 'pdf-merger', 'sign-pdf'], md="""
An email is often the only written proof you have: an offer letter, a landlord's promise, a client approving a quote, a university confirming your enrolment. Screenshots of an inbox look messy and cut off long messages. A PDF looks official, keeps the whole message, and can be attached to a file or printed for an office that still wants paper.

DoraPDF's [Email to PDF Converter](/email-to-pdf/) takes an `.eml` email file and **converts it to a PDF** in your browser. The subject becomes the title, the sender, recipient and date sit at the top, and the full message text follows.

## First, get the email as an .eml file

The converter works with `.eml` files, the standard format for a single saved email. Here's how to get one from common apps:

- **Gmail (web):** open the email, click the three-dot menu next to Reply, and choose **Download message**. Gmail saves it as `.eml`.
- **Outlook on the web and the new Outlook:** open the email, open the **…** (more actions) menu and look for **Save as** or **Download**. It saves an `.eml` file.
- **Thunderbird:** open the message and choose **File → Save As → File**, keeping the `.eml` type.
- **Apple Mail (Mac):** drag the message from your inbox onto the desktop, or use **File → Save As** with "Raw Message Source".

Classic desktop Outlook on Windows saves emails as `.msg`, which is a different format. If that's what you have, the easiest route is to forward the message to a webmail account and download it from there as `.eml`.

## Convert the EML to PDF

1. Open the [Email to PDF Converter](/email-to-pdf/).
2. Drop in your `.eml` file or tap to select it.
3. Press **Convert now**.
4. Download the PDF. It uses the same name as your email file, ending in `.pdf`.

The PDF layout is simple and readable:

- **Title:** the email's subject line (or "Email" if there wasn't one)
- **From**, **To** and **Date** lines
- The message body underneath, wrapped neatly onto A4 pages

## What's included, and what isn't

Most emails are sent in several parts, usually a plain-text version and an HTML version of the same message. The converter picks the plain-text part first; if there isn't one, it takes the HTML part and turns it into readable text. It also decodes the two encodings email programs use most (Base64 and quoted-printable), so you get normal sentences instead of strings like `=E2=80=99`.

Left out of the PDF:

- **Attachments.** Save those separately from your email app. If you need everything in one file, convert any attachments to PDF and join them with the [PDF Merger](/pdf-merger/).
- **Images and logos** inside the email body.
- **Colours, fonts and layout** of designed newsletters.
- **CC and BCC lines**, which aren't printed in the header block.

For an ordinary conversation or a confirmation message, this gives you a clean record. For a marketing newsletter where the design is the point, a browser screenshot may serve you better.

## Real situations where this helps

- **Visa, admission or job files.** Offices often ask for "email confirmation as PDF". Convert, then combine several emails into one document with the [PDF Merger](/pdf-merger/).
- **Rental agreements.** Keep a dated PDF of what your landlord agreed to by email.
- **Freelance work.** Save a client's written approval of a quote next to the invoice.
- **Disputes and complaints.** A PDF with the sender, date and full text is easier to attach to a complaint form than a forwarded chain.

## Troubleshooting

**The body shows odd characters or half-encoded text.** Some emails use unusual encodings or several nested parts. The tool handles the common ones, but a few complex messages can still come out imperfectly. Try saving the email again from a different app, such as webmail instead of a desktop client.

**The PDF shows text instead of a formatted newsletter.** That's expected: the converter keeps the words, not the design.

**Non-English characters look wrong.** The PDF uses a standard font that suits English and other Latin-alphabet languages. Emails written in Urdu, Arabic or other non-Latin scripts may not display correctly. For those, open the email and use your browser's Print → Save as PDF instead.

**The upload area won't accept my file.** Check the extension. Only `.eml` files are accepted; `.msg`, `.mbox` and `.pst` files are different formats.

## Tips

- Rename the PDF to something descriptive, such as `2026-03-offer-letter-email.pdf`, so it's easy to find later.
- Need to add your signature before sending it back? Use [Sign PDF](/sign-pdf/).
- If you're keeping lots of emails as records, put them together in date order with the [PDF Merger](/pdf-merger/) so the whole conversation reads top to bottom.

## Privacy

Emails often contain personal details, so this matters: the conversion happens in your browser. The `.eml` file is read on your own device and isn't uploaded to DoraPDF's server.

## FAQ

**Is converting email to PDF free?**
Yes. No account and no watermark.

**Can I convert a Gmail email to PDF on my phone?**
Gmail's mobile app doesn't offer "Download message", so open Gmail in a browser on a computer to get the `.eml`, or simply use your phone's Print → Save as PDF option instead.

**Does the PDF include attachments?**
No. Only the email's header details and body text are included. Save attachments separately.

**Can I convert several emails at once?**
The tool converts one email per run. Convert each one, then merge the PDFs.

**Will the date and sender be shown?**
Yes. From, To and Date appear at the top of the PDF, under the subject.
"""),
dict(slug='free-online-developer-tools-json-regex-base64-jwt', title='Free Developer Tools Online: JSON Formatter, Regex Tester, Base64, URL Encoder, JWT Decoder, SQL and UUID', date='2026-11-14',
 desc='Eight small browser-based developer tools for everyday debugging: validate JSON, test regex, decode JWTs and Base64, format SQL, make UUIDs. Free.',
 tools=['json-validator', 'regex-tester', 'jwt-decoder', 'base64', 'url-encoder', 'csv-to-json', 'sql-formatter', 'uuid-generator'], md="""
Every developer has a bookmark folder of tiny single-purpose sites: one to pretty-print JSON, one to test a regex, one to peek inside a token. DoraPDF keeps eight of these in one place, all free, all running in your browser, so pasted data stays on your machine. This is a practical tour of each **free online developer tool**: what it does, when to reach for it, and the gotchas worth knowing.

## 1. JSON Validator and Formatter

**Use it when** an API response is one unreadable line, or a config file refuses to load.

Paste your JSON into the [JSON Validator](/json-validator/). It checks the syntax as you type. Valid JSON shows a green "Valid JSON" status and a formatted copy in the output box. Choose **2 spaces** or **4 spaces** for indentation, or **Minify** to squash it back into one compact line for sending.

When the JSON is broken, the error message is shown, and in browsers that report a position, the tool converts it into a **line and column** so you can jump straight to the problem.

**Usual suspects:** a trailing comma after the last item, single quotes instead of double quotes, or comments (`//`), which standard JSON doesn't allow.

## 2. Regex Tester

**Use it when** you're writing a pattern for validation, search-and-replace or log parsing and want to see what it really matches.

The [Regex Tester](/regex-tester/) has three inputs: **Pattern**, **Flags** and **Test text**. Matches are highlighted live in the text as you type, and a table underneath lists each match with its position (index) and any capture groups. The first 200 matches are listed, with the total count shown above the table.

Tips:

- The tool always adds the `g` flag so it can find every match. Add `i` for case-insensitive or `m` for multi-line anchors.
- It uses JavaScript's regex engine, so behaviour matches what you'd get in a browser or Node.js. Syntax from other languages, such as possessive quantifiers, may not work.
- If the pattern is invalid, the error message replaces the highlight area, which is handy for spotting an unclosed bracket.

## 3. JWT Decoder

**Use it when** you need to check what's inside a JSON Web Token: the user ID, roles, issuer or expiry time.

Paste a token into the [JWT Decoder](/jwt-decoder/) and you'll see the **header** and **payload** as formatted JSON. If the payload has an `exp` claim, the tool shows the expiry as a readable date and says whether the token is **expired** or still **valid** by your device's clock.

Two important points:

- **The signature is not verified.** Decoding only shows what the token claims. Never treat a decoded token as trusted; verification has to happen on your server with the secret or public key.
- Decoding happens locally, which makes it safer than pasting real tokens into a random website. Still, treat live tokens like passwords.

## 4. Base64 Encoder / Decoder

**Use it when** you're dealing with Basic Auth headers, data URLs, email attachments or API fields that carry Base64.

The [Base64 tool](/base64/) has an **Encode** and a **Decode** mode for text, and it handles Unicode properly, so accented letters and emoji survive the round trip. Below that, you can drop in a **file** and get it back as a full data URL (for example `data:image/png;base64,...`), ready to paste into CSS or HTML.

Remember: Base64 is an encoding, not encryption. Anyone can decode it.

## 5. URL Encoder / Decoder

**Use it when** a query parameter contains spaces, `&`, `?` or non-English characters, or when you're trying to read a long tracking link.

The [URL Encoder](/url-encoder/) encodes text the way a single URL component should be encoded (so `&` becomes `%26` and a space becomes `%20`). In **Decode** mode, it also turns `+` signs into spaces, which is how form data is often sent.

Encode individual values, not a full address. Encoding `https://` itself turns the colon and slashes into codes, which isn't what you want.

## 6. CSV to JSON (and JSON to CSV)

**Use it when** you need to turn a spreadsheet export into data for an API or a script, or flatten API output for Excel.

In the [CSV to JSON Converter](/csv-to-json/), choose the direction and the **separator**: comma, semicolon (common in European Excel exports) or tab. In CSV-to-JSON mode, the first row becomes the keys and number-looking values become real numbers. In JSON-to-CSV mode, the tool collects every key across all objects for the header row and wraps values in quotes when they contain separators, quotes or line breaks. You can copy the result or download it.

## 7. SQL Formatter

**Use it when** a query was generated by an ORM, copied from a log, or written on one long line.

Paste it into the [SQL Formatter](/sql-formatter/) and it puts major clauses like `SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY` and `ORDER BY` on their own lines, indents `AND` / `OR` conditions, and breaks column lists after commas. Tick **UPPERCASE keywords** for the classic style, or untick it for lowercase.

It's a readability formatter, not a SQL parser, so it won't catch syntax errors. Also check queries that contain commas inside string values, since those get line breaks too.

## 8. UUID Generator

**Use it when** you need test IDs, seed data or unique keys.

The [UUID Generator](/uuid-generator/) creates random **version 4 UUIDs** using your browser's built-in secure random generator. Set **How many** (up to 1,000 at a time) and tick **UPPERCASE** if your system expects capital letters. Copy the whole list in one click.

## Which tool fixes which problem?

| Problem | Tool |
|---|---|
| "Unexpected token" when parsing JSON | [JSON Validator](/json-validator/) |
| Pattern matches too much or too little | [Regex Tester](/regex-tester/) |
| 401 errors and you suspect an expired token | [JWT Decoder](/jwt-decoder/) |
| Garbled text in an API field | [Base64](/base64/) |
| Broken links with special characters | [URL Encoder](/url-encoder/) |
| Spreadsheet data needed as JSON | [CSV to JSON](/csv-to-json/) |
| Unreadable query in a log file | [SQL Formatter](/sql-formatter/) |
| Need 50 unique IDs for test data | [UUID Generator](/uuid-generator/) |

## Privacy

All eight tools run entirely in your browser. Nothing you paste, whether JSON with customer data, tokens or SQL with table names, is sent to DoraPDF's server.

## FAQ

**Are these developer tools free?**
Yes, all of them, with no sign-up.

**Does the JWT decoder check if a token is genuine?**
No. It decodes the header and payload only. Signature verification must happen on your backend.

**Is my data uploaded anywhere?**
No. Processing happens locally in your browser tab.

**Can the JSON validator handle large files?**
It handles typical API responses and config files comfortably. Very large files depend on your device's memory, since everything runs in the browser.

**Which UUID version does the generator create?**
Version 4 (random) UUIDs.
"""),
dict(slug='convert-odt-to-pdf-free-online', title='Convert ODT to PDF Online Free: Open LibreOffice and OpenOffice Documents Anywhere', date='2026-11-14',
 desc="Got an .odt file you can't open? Convert OpenDocument text to a clean PDF in your browser, without installing LibreOffice. Free and private.",
 tools=['odf-to-pdf', 'word-to-pdf', 'pdf-to-word'], md="""
Someone sends you a file ending in `.odt`, and your phone shows a blank icon. Or you wrote your CV in LibreOffice Writer and the job portal only accepts PDF. ODT, short for OpenDocument Text, is the default format of LibreOffice and OpenOffice, and plenty of devices and websites simply don't know what to do with it.

DoraPDF's [ODF to PDF](/odf-to-pdf/) tool lets you **convert ODT to PDF online, free**, without installing any office software. Upload the file, press one button and download a PDF that opens anywhere. This guide explains what the conversion keeps and when you'd be better off with another route.

## Quick answer: how to convert ODT to PDF

1. Open [ODF to PDF](/odf-to-pdf/).
2. Drop in your `.odt` file (or tap to choose it).
3. Press **Convert now**.
4. Download the PDF, saved with your document's name and a `.pdf` ending.

It works the same on a laptop, a phone or a tablet, in any modern browser.

## What the PDF will look like

This is a **text-first** converter. It opens the document, reads every heading and paragraph in order, and writes them onto clean A4 pages in a simple, readable font. That makes it ideal for getting at the content of a document quickly and sharing it in a format everyone can open.

What carries over:

- All paragraph text, in the original order
- Headings (as lines of text in the same style as the body)
- The text inside lists and table cells, each on its own line

What doesn't:

- Images, charts and drawings
- Fonts, colours, bold, italics and font sizes
- Table borders and column layout
- Headers, footers and page numbers set up in the original

So, if you need to read a document someone sent you, archive a letter, or pass a text-heavy file to someone without LibreOffice, this is the fastest way. If you need a pixel-perfect copy of a designed brochure, the best option is to open the file in LibreOffice (it's free) and use **File → Export as PDF**, which keeps the exact layout.

## Who runs into ODT files?

- **Students** at schools and universities that use LibreOffice on lab computers.
- **Government and NGO staff**, since many public bodies standardise on open formats.
- **Linux users**, where LibreOffice is often the default office suite.
- **Anyone** who received an attachment from one of the above.

## Choosing between DoraPDF's document converters

| Your file | Best tool |
|---|---|
| `.odt` (LibreOffice / OpenOffice text) | [ODF to PDF](/odf-to-pdf/) |
| `.docx` (Microsoft Word) | [Word to PDF](/word-to-pdf/) |
| `.odt`, `.odp` or other OpenDocument file needed as pictures | [ODF to JPG](/odf-to-jpg/) or [ODF to PNG](/odf-to-png/) |
| A PDF you want to edit as a document | [PDF to Word](/pdf-to-word/) |

Note that this tool only accepts OpenDocument **text** files (`.odt`). Spreadsheets (`.ods`) and presentations (`.odp`) aren't supported here.

## Common problems and fixes

**"My images are missing."** That's expected with this converter, which keeps text only. Export from LibreOffice for a full-layout PDF, or convert the document with [ODF to PNG](/odf-to-png/) if you just need a picture of it.

**The file isn't accepted.** Check the extension. Only `.odt` works. If you have a `.ods` or `.odp`, save it from LibreOffice as PDF directly, or use the image converters above.

**An error appears after upload.** The file may be damaged, or it might be a different format renamed to `.odt`. Real ODT files are zipped packages containing a `content.xml` file; if that's missing, the converter can't read the document.

**Characters show as boxes or symbols.** The PDF uses a standard font that covers English and other Latin-alphabet languages. Documents in Urdu, Arabic, Hindi or other non-Latin scripts may not display correctly; exporting from LibreOffice is the better route for those.

**Paragraphs look crowded.** Every paragraph and heading in the source becomes its own line block. Very short lines from tables or forms can stack up; that's normal for a text-only conversion.

## Practical tips

- **Need to edit before converting?** If you don't have LibreOffice, convert to PDF, then turn it into an editable Word file with [PDF to Word](/pdf-to-word/).
- **Sending to a portal with a size limit?** Text-only PDFs are already small, but you can shrink any PDF further with the [PDF Compressor](/pdf-compressor/).
- **Signing a form?** After conversion, add a signature with [Sign PDF](/sign-pdf/).
- **Keep the original.** The `.odt` remains the editable master copy; the PDF is for sharing and reading.

## Privacy

The conversion runs in your browser. Your ODT file is opened on your own device and isn't uploaded to DoraPDF's server, which is useful for CVs, letters and internal documents.

## FAQ

**Is the ODT to PDF converter free?**
Yes. No account, no watermark.

**Do I need LibreOffice installed?**
No. The tool reads the ODT file directly in your browser.

**Can I convert ODT to PDF on my phone?**
Yes. Open the tool in your phone's browser and choose the file from Downloads or Files.

**Will my formatting be preserved?**
The text and its order are preserved; fonts, images and layout are not. For an exact visual copy, export from LibreOffice.

**Can I convert ODS spreadsheets or ODP slides?**
Not with this tool. It handles `.odt` text documents only.
"""),
dict(slug='markdown-to-pdf-converter-online-free', title='Markdown to PDF Online: Turn a README or .md Notes into a Clean PDF (Free)', date='2026-11-14',
 desc='Paste or upload Markdown and export a neat A4 PDF with headings, lists, tables and links styled for reading. No VS Code, Pandoc or sign-up needed.',
 tools=['markdown-to-pdf', 'pdf-to-markdown', 'pdf-compressor'], md="""
Markdown is lovely to write and awkward to hand over. Your notes look tidy in Obsidian, your README looks great on GitHub, but the person who needs them wants "a PDF, please". Command-line tools like Pandoc do the job, if you're happy installing them and wrestling with options.

For most people, a browser is enough. DoraPDF's [Markdown to PDF](/markdown-to-pdf/) tool lets you paste or upload Markdown and **export it as a styled PDF** in a couple of clicks. It's free and runs entirely on your device.

## Who this is for

- **Developers** sending a README, changelog or setup guide to a client who doesn't use GitHub.
- **Students** who take lecture notes in Markdown apps and need to submit or print them.
- **Writers** drafting in plain text who want a readable proof copy.
- **Anyone** who used an AI chatbot to draft something and got the answer back full of `#` and `**` symbols.

That last one is surprisingly common. Chatbots often reply in Markdown; pasting the reply here turns those symbols into proper headings and bold text in a PDF.

## Convert Markdown to PDF in three steps

1. Open [Markdown to PDF](/markdown-to-pdf/).
2. Either type or paste your Markdown into the big **Markdown** box, or use **Upload .md (optional)** to load a `.md`, `.markdown` or `.txt` file. The file's contents appear in the box, so you can tweak them before exporting.
3. Press **Export PDF**. The file downloads as `document.pdf`.

## What formatting is supported

The tool understands standard Markdown plus the common GitHub-style additions:

- Headings from `#` to `######`
- **Bold**, *italic* and `inline code`
- Bulleted and numbered lists, including nested ones
- Links (shown as styled text in the PDF)
- Blockquotes
- Code blocks
- Tables, which get neat cell borders in the PDF
- Horizontal rules (`---`)

The result is laid out on A4 pages with a white background, comfortable margins and a classic serif font that reads well both on screen and printed.

## A quick example

Paste this:

    # Project Setup

    Follow these steps on a **fresh machine**.

    1. Install Node.js
    2. Run `npm install`
    3. Copy `.env.example` to `.env`

    | Command | Purpose |
    |---|---|
    | npm run dev | Start local server |
    | npm test | Run tests |

and you'll get a PDF with a large heading, a bold phrase, a numbered list with code-styled commands, and a bordered table.

## Things to know before you export

**The PDF pages are rendered as images.** The tool draws your formatted document and places each page into the PDF as a high-resolution picture. It looks sharp and prints well, but you can't select or search the text inside the PDF. If you need searchable text, run the PDF through [PDF OCR](/pdf-ocr/) afterwards, which adds a text layer.

**Page breaks are made at fixed heights.** Long documents are sliced into A4-sized pages, so occasionally a line of text or a table row is split across two pages. If that happens at an important spot, add a couple of blank lines or a short paragraph before it and export again.

**Images from other websites may not appear.** Markdown images that point to external sites can be blocked from being drawn into the PDF by those sites' security settings. Simple text documents aren't affected.

**No syntax highlighting.** Code blocks appear in a plain monospace style without colours.

## Fixing common issues

**"Write some markdown first."** The box is empty. Paste text or upload a file before exporting.

**My list items run together.** In Markdown, a list needs a blank line before it if it follows a paragraph. Add the empty line and export again.

**My table shows as plain text with pipes.** Check that there's a separator row (like `|---|---|`) directly under the header row, and that every row has the same number of columns.

**The PDF file is large.** Image-based pages are heavier than text. For email, shrink it with the [PDF Compressor](/pdf-compressor/).

**Special characters look wrong in my uploaded file.** Save the `.md` file as UTF-8 in your editor before uploading.

## Going the other way

Have a PDF you want to edit as Markdown? [PDF to Markdown](/pdf-to-markdown/) extracts the text and turns larger lines into headings and bullets into list items. That makes a neat round trip: PDF to Markdown, edit, then Markdown to PDF again.

## Privacy

Everything runs in your browser. Your Markdown and the generated PDF stay on your device and aren't uploaded to DoraPDF's server, which is handy for internal docs and private notes.

## FAQ

**Is this Markdown to PDF converter free?**
Yes. No sign-up, no watermark.

**Can I convert a GitHub README to PDF?**
Yes. Open the README on GitHub, view the raw file, copy all the text and paste it into the tool. Or download the `.md` file and upload it.

**Does it support tables?**
Yes. GitHub-style tables are supported and get visible borders.

**Can I choose a different font or page size?**
No. The tool uses a fixed A4 layout with a serif font, designed for readability.

**Why can't I select text in the PDF?**
Pages are rendered as images. Use [PDF OCR](/pdf-ocr/) if you need selectable text.
"""),
dict(slug='make-gif-from-photos-free-online', title='How to Make a GIF from Photos Online for Free (No Watermark, No App)', date='2026-11-14',
 desc='Turn a handful of pictures into an animated GIF: set the speed, pick a size and choose whether it loops. Free, no watermark, runs in your browser.',
 tools=['gif-maker', 'compress-gif', 'image-resizer'], md="""
A GIF is the simplest kind of animation there is: a few pictures shown one after another, on repeat. It plays automatically in chats, emails, slides and web pages without anyone pressing play, which is exactly why it's still everywhere.

You don't need video software to make one. With DoraPDF's [GIF Maker](/gif-maker/) you can **make a GIF from photos online, for free**, with no watermark and no app to install. Add your images, set the timing, and download an animated GIF in seconds.

## Ideas worth animating

- **Before-and-after** shots: a room makeover, a haircut, a photo edit, a garden over a season.
- **Product views:** three or four angles of something you're selling, cycling on a listing.
- **Step-by-step instructions:** screenshots of an app, one step per frame, for a help page or a WhatsApp group.
- **A tiny slideshow** of event photos for a birthday message.
- **A flipbook** of drawings, if you like making things by hand.

## Make your GIF in five steps

1. Open the [GIF Maker](/gif-maker/).
2. Add **two or more images**. You can add them in batches; each new batch is added to the end of the list. The images play in the order shown, and the ✕ next to an image removes it.
3. Set the **Frame delay (ms)**. This is how long each picture stays on screen, in milliseconds. The default is 500, which means half a second per frame.
4. Choose a **Width**: 320px, 480px (default) or 640px. The height is worked out automatically from the shape of your first image.
5. Leave **Loop forever** ticked for a GIF that repeats endlessly, or untick it to play once and stop. Then press **Make GIF**.

A preview plays right below the button, and the file is ready to download as `animation.gif`.

## Getting the timing right

Frame delay changes the whole feel of the animation. A few starting points:

| Effect | Frame delay |
|---|---|
| Quick, flickery flipbook | 100–150 ms |
| Smooth step-through of screenshots | 800–1500 ms |
| Before-and-after comparison | 1000–2000 ms |
| Calm slideshow of photos | 2000–3000 ms |

Every frame uses the same delay. If you want one picture to stay on screen longer, for example the "after" shot, add that image two or three times in a row.

## Tips for a better-looking GIF

**Use images of the same shape.** The GIF takes its shape from the first image. Any image with a different shape is scaled to fit inside the frame and centred, with white bars filling the gap. For a clean result, crop all your photos to the same size first with the [Image Resizer](/image-resizer/).

**Put your best image first.** Some apps show the first frame as the thumbnail before the GIF starts playing.

**Keep the width modest.** GIFs grow quickly in file size. 480px is plenty for chats and most web pages. Use 640px only when detail really matters.

**Fewer, better frames.** Five well-chosen photos usually beat twenty similar ones, and the file stays small.

**Expect slightly simpler colours.** The GIF format allows at most 256 colours per frame. Photos with smooth skies or gradients can show some banding. Graphics, screenshots and drawings look crisp.

## Problems you might hit

**"Add at least 2 images."** A GIF needs at least two frames. Add another picture.

**The frames are in the wrong order.** Images play in the order they're listed. Remove the misplaced one with ✕ and add it again in the right position, or rename your files with numbers (01, 02, 03) and add them in one go.

**White bars around some frames.** Those images have a different shape from the first one. Crop them to match.

**The GIF is too big to send.** Run it through [Compress GIF](/compress-gif/), which can reduce colours, scale it down or drop every second frame. Messaging apps and email services often have size limits, so this is worth doing before sharing.

**Transparent PNGs got a white background.** Each frame is drawn on white, so transparency isn't kept in GIFs made here.

## GIF or video?

GIFs are perfect for short, silent loops of a few frames. For anything longer than a few seconds, or with sound, a short video is far smaller and smoother. If you've recorded a clip and it's too big to share, try the [Video Compressor](/video-compressor/) instead.

## Privacy

Your photos stay on your device. The GIF Maker builds the animation inside your browser, so nothing is uploaded to DoraPDF's server.

## FAQ

**Is this GIF maker free and without a watermark?**
Yes. The GIF you download is exactly what you made, with nothing added.

**Can I make a GIF on my iPhone or Android phone?**
Yes. Open the GIF Maker in your phone's browser and choose photos from your gallery.

**How many images can I use?**
At least two. There's no fixed upper number, but more frames take longer to process and make a bigger file.

**Can I make each frame show for a different length of time?**
All frames share one delay. Repeat an image to make it stay on screen longer.

**Will the GIF loop?**
By default, yes. Untick **Loop forever** if you want it to play once.
"""),
dict(slug='compress-gif-reduce-file-size-online', title='Compress GIF Online: Reduce GIF File Size for Chats, Email and Websites', date='2026-11-14',
 desc='Shrink a big animated GIF by cutting colours, scaling it down or dropping frames, and keep the animation playing. Free, no upload, see the % saved.',
 tools=['compress-gif', 'gif-maker', 'image-compressor'], md="""
GIFs have a habit of being much bigger than they look. A five-second reaction clip can weigh more than a high-resolution photo, and then the upload fails, the email bounces, or your web page loads slowly on mobile data.

DoraPDF's [Compress GIF](/compress-gif/) tool helps you **reduce GIF file size** without turning the animation into a still image. You choose how much to cut, it rebuilds the GIF in your browser, and it tells you exactly how much smaller the new file is.

## Why GIFs get so heavy

Understanding this makes the settings obvious:

- **Every frame is a full picture.** A 60-frame GIF is, roughly speaking, 60 images in one file.
- **Pixel size multiplies everything.** Doubling the width and height means about four times as many pixels in every frame.
- **More colours, more data.** GIF allows up to 256 colours per frame, and photos tend to use all of them.

So there are three levers: fewer colours, fewer pixels, fewer frames. The tool gives you a control for each.

## How to compress a GIF

1. Open [Compress GIF](/compress-gif/).
2. Add your `.gif` file.
3. Pick your settings:
   - **Colours:** 128 (best look), 64 (balanced, the default) or 32 (smallest)
   - **Size:** Keep size, 75% size or 50% size
   - **Frames:** Keep all frames, or Every 2nd frame
4. Press **Compress GIF**.
5. Check the preview, then download. The file is named with `-compressed.gif` on the end, and the label tells you the saving, for example "58% smaller".

## Which settings to choose

Start with the default (64 colours, keep size, keep all frames) and look at the result. Then adjust:

**If it still needs to be smaller**, change **Size** to 75%. This usually gives the biggest saving with the least visible change, especially if the GIF is wider than it will ever be displayed.

**If it's a screen recording, cartoon or simple graphic**, try 32 colours. Flat-colour images often look almost identical with far fewer colours.

**If it's a photo or video clip**, keep 128 or 64 colours. Going to 32 on real-world footage can cause visible banding in skies and skin tones.

**If the motion is smooth and fast**, try **Every 2nd frame**. This halves the frame count. The tool doubles each remaining frame's display time, so the GIF still plays at the same overall speed; it just moves in slightly bigger steps.

**If you need the maximum saving**, combine 50% size, 32 colours and every 2nd frame. Check the preview carefully; that's an aggressive setting.

## Good to know

**Transparency is kept.** If your GIF has a transparent background, such as a sticker or logo animation, the compressed version keeps those see-through areas.

**The animation is preserved.** Frame timing is read from the original and carried over, so pauses and speed stay the same unless you choose to drop frames.

**Sometimes the file doesn't shrink.** Some GIFs are already carefully optimised by the program that made them, for example by storing only the changed parts of each frame. The tool rebuilds every frame in full, so on those files the result can be the same size or larger. When that happens, the label says "no smaller — try fewer colours or 50% size". Follow that advice, or keep the original.

## Common problems and fixes

**"Could not read this GIF."** The file may be damaged, or it might not really be a GIF. Files saved from some websites are actually WebP or MP4 with a `.gif` name. Open it in your browser to check, or re-download it.

**The compressed GIF looks blotchy.** You've gone too low on colours for that image. Step back up from 32 to 64 or 128 and reduce **Size** instead.

**Movement looks jerky.** That's the **Every 2nd frame** option. Switch back to **Keep all frames** and save space with size or colours instead.

**It's slow on my phone.** Long, large GIFs mean a lot of frames to rebuild. Give it time, or use a computer for very big files.

**I need a specific size limit.** Every chat app, email service and website sets its own maximum, so check the limit where you're posting. Then compress, check the new size, and run again with stronger settings if needed.

## Related tools

- Making a GIF from scratch? The [GIF Maker](/gif-maker/) turns a set of photos into an animation, and choosing a smaller width there keeps the file light from the start.
- Got still images to shrink instead? Use the [Image Compressor](/image-compressor/) for JPG, PNG and WebP.
- For a longer clip, a video is far smaller than a GIF. The [Video Compressor](/video-compressor/) shrinks videos in your browser too.

## Privacy

Compress GIF runs entirely in your browser. Your GIF is decoded and rebuilt on your own device, and isn't uploaded to DoraPDF's server.

## FAQ

**Is it free to compress GIFs here?**
Yes. No sign-up and no watermark on the result.

**Will compressing a GIF stop it from animating?**
No. The output is still an animated GIF with the same timing.

**Can I compress several GIFs at once?**
The tool handles one GIF per run. Compress them one after another.

**Does it work on iPhone and Android?**
Yes, in any modern mobile browser. Very large GIFs are faster on a computer.

**What's the best setting for a GIF with a transparent background?**
Any of them. Transparency is preserved, so choose colours and size as usual.
"""),
dict(slug='full-page-website-screenshot-online-free', title='How to Take a Full Page Screenshot of a Website Online (Free, No Extension)', date='2026-11-13',
 desc='Capture an entire web page as a PNG from any device, with desktop, laptop, tablet or phone widths. No extension, no scrolling and stitching.',
 tools=['web-to-png', 'url-to-pdf', 'url-breakpoint-preview'], md="""
Your phone's screenshot button only grabs what fits on the screen. For a long landing page, a blog post or a competitor's pricing table, that means five or six screenshots and a lot of awkward stitching. Browser extensions can help, but you may not want to install one on a work laptop or a shared computer.

DoraPDF's [Web to PNG](/web-to-png/) tool lets you **take a full page screenshot of a website online, for free**, by typing the address. It loads the page in a real browser, scrolls the whole thing for you and hands back a single PNG image, top to bottom.

## Who actually needs a whole-page capture?

A few everyday cases where one tall image beats a stack of phone screenshots:

- **Designers and developers** showing a client the current homepage before a redesign.
- **Students** saving an online article or a university notice as evidence for a report.
- **Marketers** keeping a record of a competitor's offer page on a certain date.
- **Freelancers** adding finished websites to a portfolio.
- **Anyone** who wants to send a full page to someone on WhatsApp without asking them to open a link.

## Capture a full web page in four steps

1. Open [Web to PNG](/web-to-png/) on DoraPDF.
2. Paste or type the **website address**. You can leave out `https://`; the tool adds it.
3. Pick a **Device** width:
   - Desktop (1440px)
   - Laptop (1024px)
   - Tablet (768px)
   - Phone (390px)
4. Leave **Full page** ticked to capture everything from header to footer, then press **Take screenshot**.

After a few seconds a preview appears under the button, and a download link named after the site (for example `example.com.png`) is ready to save.

### Full page on or off?

With **Full page** ticked you get the entire length of the page. Untick it and you get only the first screen, the part a visitor sees before scrolling. That "above the fold" view is handy for checking whether a headline and button are visible straight away, and it makes a much smaller file.

## Picking the right device width

The width you choose changes the layout, because most modern sites are responsive. A few practical rules:

- **Showing a client or boss the site** → Desktop (1440px). It looks like what they see on a normal monitor.
- **Checking the mobile version** → Phone (390px). You get the stacked, single-column layout that phones show.
- **Tablet menus and in-between layouts** → Tablet (768px) or Laptop (1024px).

If you want to compare several widths side by side in one go, the [URL Breakpoint Preview](/url-breakpoint-preview/) tool is built for that. Use Web to PNG when you need the actual image file.

## Screenshot or PDF: which should you save?

Both tools take a web address, but they give you different things.

| You want... | Use |
|---|---|
| One tall image to post, share or drop into slides | [Web to PNG](/web-to-png/) |
| A document you can print on A4 or Letter, with selectable text | [URL to PDF](/url-to-pdf/) |

A PNG keeps the page looking exactly like the screen, including backgrounds and layout. When you would rather **convert a web page to PDF** for printing or archiving, URL to PDF splits it into pages instead.

## Common problems and how to fix them

**"I got a login page instead of my dashboard."** The screenshot is taken by our server's browser, which is not signed in to your accounts. Pages behind a login, such as email, banking or a school portal, cannot be captured this way. Use your device's own screenshot tool for those.

**"Some images are missing or the page looks half-loaded."** The tool waits until the page stops loading network content, up to about 30 seconds. Sites that load images only as you scroll, or that keep loading content forever, can still come out with blank areas. Try again, or try the Laptop or Desktop width, which often triggers fewer lazy-loading tricks.

**"There is a cookie banner across the top."** The page is captured as a first-time visitor sees it, so consent pop-ups often appear. That is normal; you can crop it afterwards if needed.

**"I updated my site but the screenshot looks old."** Results for the same address and settings are cached for about half an hour, so a capture you took a few minutes ago may come back again. Wait a little, or change the device width for a fresh capture.

**"The image is huge."** Full-page captures of long sites can be very tall. If you need a lighter file for email or upload, run it through the [Image Compressor](/image-compressor/) or crop it with an image editor.

**"It says the address is not valid."** Only public web addresses work. Local addresses such as `localhost` or a computer on your home network cannot be reached from our server.

## Tips for cleaner captures

- Copy the address straight from your browser's address bar to avoid typos.
- For a single article, use the article's own link rather than the homepage.
- Capture the phone and desktop versions of the same page and put them side by side in a presentation; it shows clients the responsive design clearly.
- Save captures with the date in the file name if you are keeping them as a record.

## A note on privacy

Unlike most DoraPDF tools, which run entirely in your browser, Web to PNG needs our server: the web address you enter is sent to it so a remote browser can open the page and take the picture. Only the address is sent, not files from your device. Because of that, avoid pasting private links that contain personal tokens or one-time codes.

## FAQ

**Is the website screenshot tool free?**
Yes. There is no sign-up and no watermark on the image.

**Can I take a full page screenshot on iPhone or Android with this?**
Yes. It works in the phone's browser like any other web page, and the PNG saves to your downloads or Files app.

**What format is the screenshot?**
PNG. If you need JPG or WebP, convert it with the [PNG to JPG](/png-to-jpg/) or [PNG to WebP](/png-to-webp/) tools.

**Can I screenshot a page that needs a password?**
No. The capture browser is not logged in to anything, so it only sees public pages.

**Why do Desktop and Phone captures look so different?**
Because the website itself changes its layout for narrow screens. That is exactly why the device option exists.
"""),
dict(slug='free-link-shortener-no-sign-up', title='Free Link Shortener With No Sign-Up: Make Long URLs Short in Seconds', date='2026-11-13',
 desc="Shorten a long URL for free without making an account. How DoraPDF's link shortener works, where short links help, and what to know before sharing one.",
 tools=['link-shortener', 'qr-code-generator', 'open-graph-checker'], md="""
Some links are just too long to share. A Google Drive file, a shopping page with tracking codes, a form link or a map location can run past two hundred characters. Pasted into a WhatsApp group, an Instagram bio or a printed flyer, it looks messy and is easy to break.

The [Website Link Shortener](/link-shortener/) on DoraPDF is a **free link shortener with no sign-up**. Paste the long address, press one button, and you get a short link you can copy and share straight away.

## What a short link does

A short link is a tiny address that points to your long one. When someone opens it, they are sent on to the original page automatically. Nothing about the destination changes; the short link is just a neater doorway to it.

That makes short links useful when:

- You are typing or reading a link out loud, for example in a class or a video.
- The space is limited: a bio, an SMS, a poster, the bottom of a slide.
- A long link wraps onto several lines in an email and stops being clickable.
- You want to turn the link into a QR code and keep the code simple.

## How to shorten a URL on DoraPDF

1. Open the [Website Link Shortener](/link-shortener/).
2. Paste your long link into **Long link**. If you forget the `https://`, the tool adds it for you.
3. Press **Shorten**.
4. Your short link appears in a large box. Press **Copy** to put it on your clipboard, or **Open** to test it in a new tab.

That is all. No email address, no account and no dashboard to set up.

### Always test before you share

Press **Open** once before you send the link anywhere. It takes two seconds and confirms you shortened the right page, not an old tab or a link with a typo.

## Real examples

**A teacher sharing a form.** A Google Form link is long and full of random letters. Shorten it, write the short version on the board, and students can type it in on their phones without mistakes.

**A small shop on Instagram.** Most platforms allow one link in the bio. A short link to your catalogue or WhatsApp order page looks tidier than a long one with tracking codes.

**An event poster.** Put the short link under a QR code. People who cannot scan can still type the address by hand. You can make that code with the free [QR Code Generator](/qr-code-generator/).

**A job application.** Instead of pasting a long portfolio or Drive link into a CV, a short link keeps the page clean. Tip: for formal documents, many people prefer a link that shows the real domain, so use your judgement.

## What you should know before relying on a short link

Being clear about how this tool works will save you surprises later:

- **Each short link gets a random code.** You cannot choose a custom word for the end of the link.
- **The destination cannot be edited.** If you need to point to a different page, shorten the new link and share that one instead.
- **There is no click counter.** The tool makes links; it does not track how many people opened them.
- **Only public web addresses are accepted.** Local addresses on your own computer or network will be rejected.
- **The redirect is permanent.** Visitors are sent directly to your original page.

If you need branded links, editable destinations or detailed analytics for marketing campaigns, a paid link-management service is a better fit. For quick everyday sharing, a simple short link does the job.

## Troubleshooting

**"It says enter a valid public web address."** Check that you pasted a complete link, for example `docs.google.com/...` rather than just a few words. Links to private addresses such as `localhost` or `192.168...` cannot be shortened.

**"Too many requests, wait a minute."** To prevent abuse, there is a limit on how many requests one visitor can make in a short time. Wait a minute and try again.

**"The short link opens, but the page says access denied."** The short link worked; the original page is private. For Google Drive, Docs and similar services, change the sharing setting of the file itself to "Anyone with the link".

**"My link preview looks wrong on WhatsApp or Facebook."** The preview card comes from the destination page's own tags. Check what it will look like with the [Open Graph Checker](/open-graph-checker/) using the original link.

## Privacy and safety

This is one of the few DoraPDF tools that needs our server. To make a short link work for everyone, the long link you paste has to be stored on our server so the short code can send visitors to it. Do not shorten links that contain private information, such as password-reset links, personal access tokens or one-time payment pages.

It also works the other way round: when you receive a short link from someone you do not know, be careful. A short link hides where it goes. Hover over it on a computer, or open it only if you trust the sender.

## FAQ

**Is this link shortener really free?**
Yes, and there is no sign-up. Paste, shorten and copy.

**Do the short links expire?**
The tool does not set an expiry date on links. They keep forwarding to your original page.

**Can I customise the short link or change where it goes?**
No. Each link gets a random code, and the destination is fixed once created. To change it, create a new short link.

**Can I see how many people clicked my link?**
No, there are no click statistics. It is a simple shortener.

**Does shortening a link change my original page?**
Not at all. The original page stays exactly where it is; the short link just points to it.
"""),
dict(slug='usd-to-pkr-currency-converter-live-rates', title='USD to PKR Currency Converter: Check Dollar to Rupee and 19 Other Currencies', date='2026-11-13',
 desc='Convert USD to PKR, AED, SAR, GBP and more with a free live-rate currency converter. What the rate means and why your bank may quote a different number.',
 tools=['currency-converter', 'invoice-generator', 'percentage-calculator'], md="""
"How much is 100 dollars in rupees today?" is one of those questions people ask every week: freelancers checking a payment, families receiving money from the Gulf, students paying for an online course, or shoppers looking at a price on an international website.

DoraPDF's [Currency Converter](/currency-converter/) answers that in a second. It is a simple **USD to PKR currency converter** that also handles 19 other currencies and loads live exchange rates each time you use it.

## Currencies you can convert

The converter includes these 20 currencies, so most common pairs for Pakistan, the Gulf and abroad are covered:

- **USD** (US dollar), **PKR** (Pakistani rupee), **EUR** (euro), **GBP** (British pound)
- **AED** (UAE dirham), **SAR** (Saudi riyal), **QAR** (Qatari riyal), **KWD** (Kuwaiti dinar), **OMR** (Omani rial), **BHD** (Bahraini dinar)
- **INR** (Indian rupee), **BDT** (Bangladeshi taka), **CNY** (Chinese yuan), **JPY** (Japanese yen)
- **CAD** (Canadian dollar), **AUD** (Australian dollar), **TRY** (Turkish lira), **MYR** (Malaysian ringgit), **CHF** (Swiss franc), **SGD** (Singapore dollar)

It opens set to USD to PKR with an amount of 100, since that is the conversion most visitors need first.

## How to convert dollars to rupees

1. Open the [Currency Converter](/currency-converter/).
2. Type the **Amount**.
3. Choose the currency you have in **From** and the one you want in **To**.
4. Read the result in large text, for example *100 USD = ... PKR*.

The answer updates as you type, so you can try several amounts quickly. Press **Swap** to flip the direction, which is handy for questions like "how many dollars is 50,000 rupees?".

Under the result you will see when the rates were last updated and where they came from. Check that line if you are about to make a decision based on the number.

## Why your bank or money changer shows a different rate

This is the question that confuses most people, so it is worth a clear answer.

The converter shows a **reference exchange rate**, the kind of rate published for comparing currencies. It is very useful for estimating, but it is not the price a particular bank, exchange company or app will give you. In real life:

- **Banks and exchange companies add a margin.** The rate at which they sell dollars to you is higher than the rate at which they buy them from you.
- **Pakistan has more than one dollar rate.** News reports often mention the interbank rate and the open market rate, and the two can differ.
- **Payment apps and card companies** use their own rate and may add a conversion fee on top.
- **Rates change through the day**, while a published reference rate is updated from time to time.

So use the converter to know roughly what you should expect, then compare it with the exact quote from whoever is actually changing your money. If a quote is far worse than the reference rate, that is your cue to ask questions or shop around.

## Practical examples

**A freelancer invoicing in dollars.** You agree on $350 for a project. Convert USD to PKR to see roughly what lands in your account before fees. When you are ready to bill, make the invoice itself with the free [Invoice Generator](/invoice-generator/), which supports both PKR and USD.

**Money sent from Dubai.** A relative is sending 2,000 AED. Set From to AED and To to PKR to estimate the amount, then compare with what the remittance service promises.

**Shopping on a foreign website.** A course costs 49 GBP. Convert it to PKR to know the real price before you pay by card, keeping in mind your bank may add a fee.

**Comparing two offers.** One supplier quotes in CNY, another in USD. Convert both into PKR and compare them directly. To see the gap as a percentage, use the [Percentage Calculator](/percentage-calculator/).

## Tips for getting useful numbers

- Round sensibly. For planning, the nearest rupee is plenty; nobody pays in fractions of a paisa.
- If you convert the same amount often, keep the tab open; the rate is fetched again whenever you change the base currency.
- For budgets, add a small buffer for fees and rate movement rather than planning to the exact rupee.
- Remember that the converter does not know about taxes, transfer charges or card fees. Add those yourself.

## When it does not load

If you see "Could not load live rates", the converter could not reach the rate service. Check your internet connection and refresh the page. Some office or school networks block outside services; trying on mobile data usually confirms whether that is the cause.

## Privacy

The calculation happens in your browser. To get current rates, your browser asks a public exchange-rate service (open.er-api.com) for the latest figures for the currency you picked. The amount you type is never sent anywhere; it is multiplied on your own device.

## FAQ

**Is the dollar rate in this converter the open market rate?**
No. It is a reference rate from a public exchange-rate source. Banks and money changers set their own buying and selling rates, which can be higher or lower.

**How often are the rates updated?**
The rates are loaded fresh when you use the tool, and the note under the result shows exactly when the source last updated them.

**Can I convert PKR to USD as well?**
Yes. Choose PKR in From and USD in To, or press Swap.

**Does it work on mobile?**
Yes, it works in any phone browser with no app to install.

**Which Gulf currencies are included?**
AED, SAR, QAR, KWD, OMR and BHD are all in the list.
"""),
dict(slug='remove-password-from-pdf-free-unlock', title='How to Remove a Password From a PDF You Own (Free, in Your Browser)', date='2026-11-13',
 desc='Tired of typing the same PDF password? Remove it for good with a free unlock tool that runs on your device. What you need, how it works and what changes.',
 tools=['unlock-pdf', 'protect-pdf', 'pdf-compressor'], md="""
Banks, mobile networks, universities and employers love sending password-protected PDFs. Monthly statements, salary slips, fee challans and admission letters often arrive locked with your date of birth, CNIC digits or account number. That is sensible for security, but if you open the same file ten times or need to forward it to an office that cannot open locked files, typing the password every time gets old fast.

This guide shows **how to remove a password from a PDF for free** with DoraPDF's [Unlock PDF](/unlock-pdf/) tool, without installing any software. One important point first: you need to know the password. This is a tool for removing a password you already have, not for guessing one you do not.

## Before you start: what you need

- The **PDF file** on your phone or computer.
- The **password** that opens it. For statements this is usually explained in the email that came with the file, for example "the first four letters of your name followed by your year of birth".
- The right to remove it. Only unlock files that belong to you or that you have permission to open.

## Remove the PDF password in four steps

1. Open [Unlock PDF](/unlock-pdf/) on DoraPDF.
2. Choose or drop the locked PDF.
3. Type the password in the **Password** box.
4. Press **Unlock**, then download the file. It is saved with **-unlocked** added to the name, for example `statement-march-unlocked.pdf`.

Open the new file and it should go straight to the first page with no password prompt. Your original locked file stays untouched on your device.

If the password is wrong, the tool tells you so instead of producing a broken file. Check capital letters, and check whether the sender wanted the full year (2001) or just the last two digits (01).

## What changes in the unlocked file

It is worth knowing exactly what you get, because this is where unlock tools differ.

DoraPDF's tool opens the PDF with your password and then **rebuilds every page as a high-resolution image** inside a fresh, unprotected PDF. In practice that means:

- **It looks the same.** Text, logos, tables and stamps appear just as in the original.
- **The text is no longer selectable.** You cannot copy words from the unlocked file or search inside it, because each page is now a picture of the page.
- **Links and form fields do not carry over.** Clickable links and fillable boxes become part of the image.
- **The file may be larger** than the original, especially for documents with many pages.

For the usual reasons people unlock a PDF (to view, print, attach or upload it without a password), this is perfectly fine. If you need searchable text afterwards, run the unlocked file through [PDF OCR](/pdf-ocr/) to add a text layer back.

If the new file is too big for an email or an upload form, shrink it with the [PDF Compressor](/pdf-compressor/).

## Situations where unlocking helps

**Uploading a statement to a visa or loan portal.** Many upload forms reject encrypted PDFs or show an error. An unlocked copy goes through.

**Sending documents to an accountant.** Instead of sharing your password over WhatsApp, send an unlocked copy of just the files they need.

**Printing at a shop.** Some print shop computers refuse locked files or ask for the password at the counter. Bring an unlocked copy.

**Keeping a personal archive.** If you save years of statements, unlocked copies are easier to open later when you have forgotten which password went with which bank.

## Common problems

**"Wrong password" even though I am sure it is right.** Passwords are case-sensitive. Try all capitals or all small letters for the name part, and check the date format. Copying the password from an email can also pick up an extra space at the end.

**"Could not open this PDF."** The file may be damaged or not really a PDF. Try downloading it again from the original email or website.

**"I do not know the password at all."** Contact whoever sent the file. Banks and employers can tell you the format or send the document again. DoraPDF does not crack or bypass unknown passwords.

**"My PDF opens without a password, but I cannot print or copy."** Some PDFs have no opening password but carry restrictions on printing or editing. Try uploading it with the password box empty; the tool rebuilds the pages as images, which gives you a copy without those restrictions. Only do this for files you have the right to use that way.

**"The unlocked file is very heavy."** Rebuilding pages as images adds size. Compress it afterwards.

## Privacy: your file stays on your device

Locked PDFs usually contain exactly the kind of information you do not want floating around: account numbers, salaries, addresses. Unlock PDF works **entirely in your browser**. The file and the password are processed on your own device and are not uploaded to DoraPDF's server.

A good habit: once you have finished with an unlocked copy, delete it or keep it somewhere private, since it no longer has a password guarding it. If you need to share it again safely, add a new password with [Protect PDF](/protect-pdf/).

## FAQ

**Can I remove a PDF password without knowing it?**
No. You must type the correct password. The tool removes protection from files you can already open.

**Is unlocking a PDF free on DoraPDF?**
Yes, with no sign-up and no watermark on the result.

**Can I unlock a PDF on my phone?**
Yes. The tool works in the browser on Android and iPhone; the unlocked file saves to your downloads or Files app.

**Why can I not copy text from the unlocked PDF?**
Because the pages are rebuilt as images. Use PDF OCR afterwards if you need selectable text.

**Is it legal to remove a password from a PDF?**
Removing a password from your own documents is normal. Do not unlock files you are not entitled to open or share.
"""),
dict(slug='rotate-pdf-pages-and-save-permanently', title='Rotate PDF Pages and Save Them Permanently (Free, Even Just One Page)', date='2026-11-13',
 desc='Fix sideways or upside-down PDF pages for good. Rotate all pages or only the ones you pick, free in your browser, with no quality loss.',
 tools=['rotate-pdf', 'delete-pdf-pages', 'pdf-merger'], md="""
You scan ten pages of notes on your phone, send them as a PDF, and page 4 is sideways while page 7 is upside down. Or a landscape chart sits in the middle of a portrait report and everyone has to tilt their head to read it.

Most PDF readers let you turn the view, but that only lasts until you close the file. The next person who opens it sees the same crooked pages. To fix it properly you need to **rotate the PDF and save it permanently**, which is what DoraPDF's free [Rotate PDF](/rotate-pdf/) tool does.

## View rotation versus real rotation

This difference trips up a lot of people, so here it is in one line:

- **Rotating in a viewer** (Edge, Chrome, Adobe Reader, a phone's file app) turns the page on your screen only.
- **Rotating with a tool** changes the file itself, so it opens the right way up on every device, for every person, every time.

If you have rotated a page, closed the file and found it sideways again, you were using the first kind.

## How to rotate a PDF on DoraPDF

1. Open [Rotate PDF](/rotate-pdf/).
2. Add your PDF file.
3. Choose the **Rotation**:
   - **90° clockwise** (a quarter turn to the right)
   - **180°** (upside down to right way up)
   - **90° counter-clockwise** (a quarter turn to the left)
4. In **Pages**, leave `all` to rotate the whole document, or type the pages you want, such as `4` or `2-3, 7`.
5. Press **Rotate**, then download the file, saved as `yourfile-rotated.pdf`.

## Rotating only some pages

This is where the Pages box earns its keep. A few examples:

| You type | Pages rotated |
|---|---|
| `all` | Every page |
| `4` | Only page 4 |
| `2-3, 7` | Pages 2, 3 and 7 |
| `1-5, 9-10` | Pages 1 to 5, plus 9 and 10 |

If different pages need different turns (some clockwise, one upside down), do it in two passes. Rotate the sideways pages first, download, then load the new file and rotate the upside-down page by 180°.

### Which direction do I need?

Look at the top of the text on the crooked page:

- Top of the text is pointing **left** → choose 90° clockwise.
- Top of the text is pointing **right** → choose 90° counter-clockwise.
- Text is **upside down** → choose 180°.

If you guess wrong, no harm done: run the rotated file through again with the opposite direction.

## Quality and content stay exactly the same

Rotate PDF does not redraw or re-compress your pages. It updates the page orientation setting stored in the PDF. That means:

- Text stays sharp and selectable.
- Links, bookmarks and images are not touched.
- The file size stays practically the same.
- The rotation adds to whatever rotation a page already had, so rotating a page 90° twice gives you 180°.

## Where people usually need this

**Phone scans.** Scanning apps sometimes guess the orientation wrongly, especially for pages with little text or with photos.

**Mixed reports.** A wide table or chart is often set to landscape. Rotating just that page makes the whole report read smoothly when scrolling.

**Merged files.** When you **merge PDF files** from different sources, some may come in sideways. Combine them with the [PDF Merger](/pdf-merger/), then fix the odd ones out here.

**Assignments and applications.** Submitting a PDF with an upside-down page looks careless. A thirty-second fix before uploading avoids that.

## Common problems and fixes

**"Nothing seems to have changed."** Check the Pages box. If it still says `all` but you meant one page, or you typed a page number that does not exist in the file, the result will not be what you expected. Page numbers start at 1 for the first page.

**"Some pages turned the wrong way."** Run the file again with the opposite direction for those pages only.

**"My viewer still shows it sideways."** Make sure you opened the downloaded **-rotated** file, not the original.

**"The PDF is password protected."** Remove the password first with [Unlock PDF](/unlock-pdf/) if it is your file, then rotate.

**"I also want to remove a blank page."** Use [Delete PDF Pages](/delete-pdf-pages/) on the rotated file.

## Privacy

Rotate PDF runs entirely in your browser. Your document is read and edited on your own device, and it is not uploaded to DoraPDF's server. That makes it safe for contracts, ID scans and anything else you would rather keep private.

## FAQ

**How do I rotate one page in a PDF and save it?**
Type that page number in the Pages box (for example `5`), choose the direction, press Rotate and download the new file.

**Will rotating reduce the quality?**
No. The pages are not re-rendered; only the orientation setting changes.

**Can I rotate a PDF on my phone?**
Yes. The tool works in mobile browsers on Android and iPhone.

**Does the rotation stay when I send the file to someone?**
Yes. The change is saved inside the file, so it opens the right way for everyone.

**Can I rotate several PDFs at once?**
The tool works on one PDF at a time. If you have several, merge them first and rotate the combined file.
"""),
dict(slug='delete-pages-from-pdf-free-online', title='Delete Pages From a PDF Online for Free (Works on iPhone and Android Too)', date='2026-11-13',
 desc='Remove blank, duplicate or private pages from a PDF in seconds. Type page numbers or ranges, download a clean copy. Free, no upload to a server.',
 tools=['delete-pdf-pages', 'pdf-splitter', 'rotate-pdf'], md="""
A 30-page bank statement when the embassy only wants the last three months. A scanned assignment with two blank pages in the middle. A contract that came with a cover sheet you do not want to forward. In all of these, you do not need a PDF editor; you just need to take a few pages out.

DoraPDF's [Delete PDF Pages](/delete-pdf-pages/) tool lets you **delete pages from a PDF online for free**. You type the page numbers, press one button and download a slimmer copy. It works the same on a laptop, an iPhone or an Android phone.

## Step by step

1. Open [Delete PDF Pages](/delete-pdf-pages/).
2. Add your PDF.
3. In **Pages to delete**, type the page numbers you want gone, for example `2, 4-6`.
4. Press **Delete pages**.
5. Download the result, named `yourfile-edited.pdf`. The download line also tells you how many pages are left, which is a quick way to check you removed the right number.

Your original file is not changed; you get a new copy.

## Writing the page list

The page box accepts single pages, ranges and a mix of both, separated by commas.

- `1` removes the first page, often a cover or fax sheet.
- `3, 8` removes pages 3 and 8.
- `10-14` removes pages 10, 11, 12, 13 and 14.
- `1, 5-7, 12` removes pages 1, 5, 6, 7 and 12.

Page numbers here mean the position in the file, starting at 1, not the number printed at the bottom of the page. If a document has a cover and two roman-numbered pages before "page 1", the printed page 1 is actually the fourth page of the file.

### Find the right numbers first

Open the PDF in any viewer and scroll through it, noting the position of each page you want to remove. On a phone, most file viewers show "4 / 30" or similar as you swipe. A minute of checking saves you from cutting the wrong page.

## Delete pages or extract pages?

Sometimes it is easier to think about what you want to **keep**.

- If you are removing **a few pages** from a long file, use [Delete PDF Pages](/delete-pdf-pages/).
- If you only want to **keep a few pages** out of a long file, use the [PDF Splitter](/pdf-splitter/) and extract just those pages into a new PDF.

For a 40-page statement where you need pages 37 to 40, extracting `37-40` is one short entry, while deleting would mean typing `1-36`. Both work; pick whichever list is shorter.

## Everyday examples

**Visa and loan applications.** Officers often ask for specific months. Deleting the other pages keeps the file small enough for upload limits and easier for them to read.

**Scanned homework.** Remove the accidental blank or blurry scans before you submit. If a page came out sideways, fix it with [Rotate PDF](/rotate-pdf/) afterwards.

**Sharing part of a report.** Take out internal pages, such as pricing or staff details, before you send a document outside your organisation. If sensitive details sit on pages you need to keep, black them out with [Redact PDF](/redact-pdf/) instead.

**Printing.** Remove pages you do not need before printing to save paper and money at the print shop.

## What happens to the rest of the file

The tool removes the pages you list and keeps everything else exactly as it was. The remaining pages are not re-rendered or compressed, so:

- Text stays selectable and searchable.
- Images keep their quality.
- Page order is unchanged.

## Troubleshooting

**"Enter valid page numbers."** The numbers must exist in the file. If the PDF has 12 pages, `14` is not valid. The message tells you the allowed range.

**"You cannot delete every page."** A PDF needs at least one page. If you listed all of them, check your ranges; one of them probably covers more than you meant.

**"The wrong page was removed."** Remember that the count starts at the first page of the file, including covers. Go back to your original file, which is unchanged, and try again with the corrected number.

**"My file is password protected."** If you own it, remove the password with [Unlock PDF](/unlock-pdf/) first.

**"Can I reorder pages too?"** This tool only removes pages. To rearrange, you can split the file into parts with the PDF Splitter and put them back together in the order you want with the [PDF Merger](/pdf-merger/).

## Your file stays private

Delete PDF Pages works entirely inside your browser. The PDF is opened and edited on your device and is never uploaded to DoraPDF's server, which matters when the file is a bank statement, a medical report or an ID document.

## FAQ

**How do I delete a page from a PDF on iPhone?**
Open the tool in Safari, tap to choose your PDF from Files, type the page number and tap Delete pages. The new file saves to your downloads in Files.

**Is it free to delete PDF pages on DoraPDF?**
Yes. There is no sign-up and no watermark.

**Will removing pages reduce quality?**
No. The pages you keep are copied as they are, without re-compression.

**Can I undo a deletion?**
Your original PDF is never changed, so you can always start again from it.

**Can I delete pages from several PDFs at once?**
The tool handles one PDF at a time. Run each file separately, or merge them first if they belong together.
"""),
dict(slug='redact-pdf-free-black-out-text', title='How to Redact a PDF for Free (and Make Sure the Text Is Really Gone)', date='2026-11-13',
 desc='Black out names, phone numbers and account details in a PDF so they cannot be copied back. A free redaction tool that runs in your browser, explained.',
 tools=['redact-pdf', 'delete-pdf-pages', 'pdf-compressor'], md="""
Here is a mistake that happens far more often than it should: someone draws black rectangles over a name or account number in a PDF, sends it off, and the recipient simply selects the "hidden" area and copies the text out. The box was covering the words, not removing them.

Proper redaction means the information is **gone from the file**, not just hidden on screen. This guide shows **how to redact a PDF for free** with DoraPDF's [Redact PDF](/redact-pdf/) tool, which blacks out the words you choose and then flattens the pages so the original text cannot be recovered.

## When you need to redact

- Sharing a **bank statement** but hiding your full account number and balance.
- Sending a **CNIC, passport or contract** scan where only some details are needed.
- Publishing a **report or complaint** without the names of the people involved.
- Giving a teacher or supervisor a **sample document** with client details removed.
- Posting a **screenshot of a PDF** online with phone numbers or email addresses blacked out.

## How to black out text in a PDF on DoraPDF

1. Open [Redact PDF](/redact-pdf/).
2. Add your PDF.
3. In **Words to redact**, type each word or phrase you want removed, separated by commas. For example: `Ayesha Khan, 0300-1234567, PK36 SCBL`.
4. Press **Redact**.
5. Download the result, saved as `yourfile-redacted.pdf`. The download line shows how many redactions were made, so you know straight away whether the tool found what you asked for.

Every place where one of your words appears, on every page, gets a solid black box.

## Why the result is safe to share

After drawing the boxes, the tool turns each page into an image and builds a new PDF from those images. That step matters:

- There is **no hidden text layer** under the black boxes, because there is no text layer at all.
- Copying, searching or "select all" on the redacted file will not reveal the removed words.
- The pages still look like the original, just with black bars where the sensitive parts were.

The trade-off is that the redacted file no longer has selectable text anywhere, and it can be larger than the original. For a document you are sharing for someone to read, that is usually exactly what you want.

## Getting good results: practical tips

**Type the text the way it appears.** Matching ignores capital letters, so `ayesha khan` finds "Ayesha Khan" and "AYESHA KHAN". But spacing and punctuation must match. If the document writes the number as `0300 1234567`, a search for `0300-1234567` will not find it.

**Add each variation.** Names often appear in several forms. For full coverage you might enter `Ayesha Khan, Ms Khan, Ayesha, A. Khan`.

**Redact the unique part of long numbers.** For an account number, entering the whole thing is safest, but adding a distinctive chunk as well can catch versions that are split or formatted differently.

**Check every page after redacting.** Scroll through the downloaded file. The box width is calculated from the font, so on some fonts the bar can be slightly shorter or longer than the word. If a letter peeks out, add a slightly longer phrase and run it again on the original.

**Think beyond the obvious.** Signatures, photos and stamps are images, not text, so typing words will not cover them. If a whole page is sensitive, remove it entirely with [Delete PDF Pages](/delete-pdf-pages/).

## Common problems

**"None of those words were found."** Usually one of three things:

1. **The PDF is a scan.** A scanned page is a picture, so there is no text for the tool to find. Make it searchable first with [PDF OCR](/pdf-ocr/), then redact the OCR'd file. Check the result carefully, as OCR can misread characters.
2. **The spelling or spacing differs** from what you typed. Copy the word directly from the PDF and paste it into the box.
3. **The phrase is split across lines** in the document. Try redacting each part separately.

**"The redacted file is too big to email."** Flattening pages into images adds size. Compress it with the [PDF Compressor](/pdf-compressor/).

**"I need to keep the text selectable."** Real, permanent redaction and selectable text pull in opposite directions. For anything sensitive, flattened pages are the safer choice.

## Privacy: nothing leaves your device

It would make little sense to upload a file to a server in order to hide private details from other people. Redact PDF runs **entirely in your browser**. Both the document and the list of words you type stay on your device and are not sent to DoraPDF.

A final check that is always worth doing: open the redacted PDF, press Ctrl+F (or use your viewer's search) and look for one of the redacted words. It should not be found.

## FAQ

**Is this real redaction or just a black box on top?**
Real. The pages are flattened to images after the boxes are drawn, so the covered text is removed from the file.

**Can I redact a scanned PDF?**
Yes, after running it through PDF OCR so the tool can find the words. Always review the result.

**Is redacting a PDF free on DoraPDF?**
Yes, with no sign-up and no watermark.

**Does the search care about capital letters?**
No. Matching ignores case, but spaces and punctuation must match.

**Can I redact images or signatures?**
Not with this tool, which works on text. Remove the whole page instead if it contains sensitive images.
"""),
dict(slug='lbs-to-kg-ml-to-oz-celsius-to-fahrenheit-converters', title='Lbs to KG, ML to Oz, Celsius to Fahrenheit: Free Everyday Unit Converters', date='2026-11-13',
 desc='Quick, free converters for weight, volume, temperature and time: lbs to kg, ounces to grams, ml to oz, liters to gallons, °C to °F and hours to minutes.',
 tools=['lbs-to-kg', 'ml-to-oz', 'celsius-to-fahrenheit', 'ounces-to-grams', 'liters-to-gallons', 'hours-to-minutes'], md="""
An American recipe asks for 8 ounces of flour and an oven at 350°F. A gym app logs your weight in pounds. A baby bottle is marked in millilitres, but the guide you are reading uses fluid ounces. Unit conversions turn up all the time, and doing them in your head is where mistakes creep in.

DoraPDF has a set of small, free converters for exactly these moments. This guide covers six of them: **lbs to kg, ounces to grams, ml to oz, liters to gallons, Celsius to Fahrenheit and hours to minutes**, with the formulas, worked examples and the traps to watch for.

## How every converter works

All six tools share the same simple layout:

- **Two boxes side by side.** Type in either one and the other updates instantly. There is no "convert" button and no need to swap direction; type pounds to get kilograms, or kilograms to get pounds.
- **A quick table** underneath showing common values (1, 2, 5, 10, 20, 50, 100, 500 and 1000) so you can read off a conversion without typing.

They open with 1 already filled in, so you can see the basic rate as soon as the page loads.

## Weight: pounds and ounces

### Lbs to kg

Use the [Lbs to KG Converter](/lbs-to-kg/). One pound is exactly **0.45359237 kg**.

- 150 lbs ≈ **68.04 kg**
- 200 lbs ≈ **90.72 kg**
- A rough mental shortcut: halve the pounds, then take away a tenth of that. 150 → 75 → 75 minus 7.5 = 67.5 kg. Close enough for chatting, but use the tool for anything that matters, such as medicine doses or luggage limits.

### Ounces to grams

The [Ounces to Grams](/ounces-to-grams/) converter uses **1 oz = 28.349523 g**.

- 8 oz ≈ **226.8 g**
- 16 oz (one pound) ≈ **453.6 g**

This is the weight ounce, used for flour, meat, cheese and parcels. It is not the same as a fluid ounce, which measures volume. Recipes sometimes just write "oz", so check whether the ingredient is a solid (weight) or a liquid (volume).

## Volume: millilitres, fluid ounces, litres and gallons

### ML to oz

The [ML to Oz Converter](/ml-to-oz/) converts millilitres to **US fluid ounces**, with **1 US fl oz = 29.5735 ml**.

- 500 ml ≈ **16.91 US fl oz** (a typical water bottle)
- 250 ml ≈ **8.45 US fl oz**
- 30 ml ≈ **1.01 US fl oz**

Watch out: the UK fluid ounce is slightly smaller (about 28.4 ml). This tool uses the US measure, which is what most American recipes, product labels and supplement bottles mean.

### Liters to gallons

[Liters to Gallons](/liters-to-gallons/) converts to **US gallons**, using **1 litre = 0.264172 US gallons** (one US gallon is about 3.785 litres).

- 20 L ≈ **5.28 US gallons**
- 50 L ≈ **13.21 US gallons**

The imperial gallon used in the UK is bigger, about 4.546 litres. If you are reading a British source on fuel or tank sizes, the numbers will not match a US-gallon conversion.

## Temperature: Celsius to Fahrenheit

The [Celsius to Fahrenheit](/celsius-to-fahrenheit/) converter uses the standard formula **°F = °C × 9/5 + 32**, and the reverse **°C = (°F − 32) × 5/9**.

- 37°C = **98.6°F** (typical body temperature)
- 180°C = **356°F** (a common oven setting; recipes often round it to 350°F)
- 0°C = **32°F** (water freezes)
- 40°C = **104°F** (a hot summer day in much of Pakistan)

Temperature is the one conversion where the quick table is less useful for cooking, because oven settings sit between the table values. Just type the number from your recipe into either box.

## Time: hours to minutes

[Hours to Minutes](/hours-to-minutes/) multiplies by 60, and divides by 60 the other way.

- 2.5 hours = **150 minutes**
- 1.75 hours = **105 minutes**
- 45 minutes = **0.75 hours**

That last direction is the one people get wrong most often. Timesheets and invoices frequently need decimal hours: 1 hour 45 minutes is **1.75 hours**, not 1.45. Type 105 into the minutes box and the tool gives you the decimal instantly.

## Where these come in handy

- **Cooking and baking** from American or British recipes.
- **Fitness and health**, when your scale, gym app or doctor uses different units.
- **Travel and shopping abroad**, from luggage weights to fuel prices per gallon.
- **Freelance work**, turning minutes worked into decimal hours for an invoice.
- **Homework**, checking physics or chemistry answers that involve unit changes.

## Accuracy notes

Results show up to six decimal places in the boxes and four in the quick table. For everyday use, round to one or two decimals. The weight factors are the official definitions, so the results are as precise as you will need.

## Privacy

These converters are pure calculations that run in your browser. Nothing you type is sent anywhere, and they keep working even on a slow connection once the page has loaded.

## FAQ

**How do I convert lbs to kg quickly?**
Multiply pounds by 0.4536, or type the number into the Lbs to KG Converter for an exact answer.

**Is ml to oz the same as ml to fluid ounces?**
Yes, for liquids "oz" means fluid ounces. The tool uses US fluid ounces.

**Why does my recipe say 350°F when 180°C is 356°F?**
Recipes round oven temperatures to convenient numbers. The difference does not matter for most dishes.

**How do I write 1 hour 30 minutes in decimal hours?**
1.5 hours. Enter 90 in the minutes box of the Hours to Minutes converter to check any value.

**Do the converters work offline?**
Once the page is open, the calculations happen on your device, so they keep working even if your connection drops.

For distances, see the companion guide on converting [cm, inches, feet, metres, miles and km](/blog/length-converter-cm-inches-feet-meters-miles-km/).
"""),
dict(slug='add-watermark-to-pdf-free-confidential-draft', title='Add a Watermark to a PDF for Free: CONFIDENTIAL, DRAFT or Your Own Text', date='2026-11-13',
 desc='Stamp CONFIDENTIAL, DRAFT, SAMPLE or your name across every page of a PDF. Choose size, colour, opacity and angle. Free and private in your browser.',
 tools=['pdf-text-watermark', 'pdf-image-watermark', 'protect-pdf'], md="""
A watermark is a quiet way of saying something about a document before anyone reads a word of it. "DRAFT" tells a reviewer not to treat the numbers as final. "CONFIDENTIAL" reminds people not to forward it. "SAMPLE" on a portfolio piece or a notes preview makes it clear the file is not the full paid version.

DoraPDF's [Add Text Watermark to PDF](/pdf-text-watermark/) tool lets you **add a watermark to a PDF for free**, in your browser, in under a minute. You type the text, adjust how it looks, and every page gets the same stamp.

## Which watermark text should you use?

Short, clear words work best. Some common choices and when they fit:

| Text | Good for |
|---|---|
| CONFIDENTIAL | Internal reports, salary details, legal drafts |
| DRAFT | Anything still being reviewed or edited |
| SAMPLE | Portfolio pieces, previews of notes or templates |
| COPY | A copy of an original certificate or letter |
| Your name or business | Proof that a document or design came from you |
| "For visa application only" | ID or bank documents shared for one purpose |

That last idea is worth borrowing. Writing the purpose across a copy of your CNIC or passport makes it harder for someone to reuse the copy for something else.

## How to add a text watermark to a PDF

1. Open [Add Text Watermark to PDF](/pdf-text-watermark/).
2. Add your PDF.
3. Set the options:
   - **Text** starts as `CONFIDENTIAL`. Replace it with whatever you need.
   - **Font size** starts at 60. Larger numbers make the stamp bigger.
   - **Opacity** is a slider from very faint to solid. It starts quite faint so the page stays readable.
   - **Color** starts as DoraPDF pink. Click it to pick any colour.
   - **Angle** is either **Diagonal** (45°, across the page) or **Horizontal**.
4. Press the button to process the file and download it. It is saved as `yourfile-watermarked.pdf`.

The watermark is placed in the centre of every page, in a bold font.

## Making it look professional

A watermark should be noticeable without making the document hard to read. A few guidelines:

- **Grey or muted colours** look the most professional. Red works well for "CONFIDENTIAL" or "VOID". Bright colours can be distracting on text-heavy pages.
- **Keep opacity low** for documents people need to read, roughly the first quarter of the slider. Raise it for samples and previews where the point is to discourage use.
- **Diagonal suits single words.** It covers more of the page and is harder to crop out.
- **Horizontal suits longer phrases** such as "For visa application only", which can run off the edge of the page when tilted.
- **Adjust size to text length.** One short word looks good at 60 to 90. A sentence may need 30 to 40 to fit on a portrait page.

Try it once, check the result, and tweak the size or opacity if needed. It only takes a few seconds per attempt.

## Real-life uses

**Students and teachers.** Mark lecture notes or a sample paper as "SAMPLE" or with your name before sharing a preview.

**Freelancers.** Send a client a watermarked draft of a report or design, and share the clean version after approval.

**Offices.** Stamp "DRAFT" on a policy that is still being discussed, so nobody prints and circulates an unfinished version.

**Personal documents.** Add a purpose line to copies of ID cards, utility bills or bank statements before uploading them anywhere.

## Want a logo instead of text?

If you would rather stamp your logo, use [Add Image Watermark to PDF](/pdf-image-watermark/), which places an image on every page. Many businesses use both: a logo for branding, and a text word like "DRAFT" for status.

## Limits worth knowing

**Plain English letters, numbers and common symbols work.** The watermark uses a standard built-in PDF font, so it cannot draw Urdu, Arabic or other non-Latin scripts. If you need Urdu text, create it as an image and use the image watermark tool.

**One watermark per pass, on all pages.** The same text goes on every page. To add a second line, run the watermarked file through the tool again with the new text.

**A watermark is a label, not a lock.** The text is added on top of the page content. Determined people with a PDF editor may be able to remove or cover it. For real protection, combine it with a password using [Protect PDF](/protect-pdf/), and for hiding information permanently, use redaction instead.

## Troubleshooting

**"The text runs off the page."** Lower the font size, or switch to Horizontal for long phrases.

**"I can hardly see it."** Increase the opacity, or choose a darker colour.

**"It covers the content too much."** Lower the opacity and use grey.

**"My locked PDF will not work."** If it is your file, remove the password with [Unlock PDF](/unlock-pdf/) first, add the watermark, then lock it again with Protect PDF if needed.

## Privacy

The watermark is added entirely in your browser. Your PDF is not uploaded to DoraPDF's server, which is reassuring when the reason you are marking it "CONFIDENTIAL" is that it really is.

## FAQ

**How do I add a CONFIDENTIAL watermark to a PDF?**
Open the tool, keep the default text CONFIDENTIAL, pick a colour and opacity, process the file and download it.

**Is it free to watermark a PDF on DoraPDF?**
Yes. No sign-up and no extra branding of our own.

**Can I watermark only some pages?**
The tool stamps every page. To mark only part of a file, split out those pages with the PDF Splitter, watermark them and merge the file back together.

**Can I write the watermark in Urdu?**
Not with the text tool. Create an image of the Urdu text and use the image watermark tool instead.

**Does the watermark reduce PDF quality?**
No. The original pages are kept as they are, with the watermark text added on top.
"""),
dict(slug='extract-images-from-pdf-free', title='How to Extract Images From a PDF for Free (Original Pictures, Not Screenshots)', date='2026-11-13',
 desc='Save every photo and picture inside a PDF as PNG files, all at once in a ZIP. Free, private and in your browser. Plus when PDF to JPG is the better choice.',
 tools=['pdf-image-extractor', 'pdf-to-jpg', 'image-compressor'], md="""
You have a PDF brochure, a scanned report or a set of lecture notes, and you need one of the pictures inside it for a presentation. The usual trick is to zoom in and take a screenshot, but that grabs a blurry, cropped version with bits of text around the edges.

There is a cleaner way. DoraPDF's [PDF Image Extractor](/pdf-image-extractor/) lets you **extract images from a PDF for free**. It goes through every page, pulls out the actual pictures embedded in the file and gives them back as separate image files, ready to use.

## Extracting images versus converting pages

These two jobs sound similar but give very different results, so choose the one you really need.

**Extracting images** (this tool) saves the pictures themselves: photos, diagrams, logos and other images placed inside the PDF. You get each one as its own file, without the surrounding text.

**Converting PDF to JPG** with [PDF to JPG](/pdf-to-jpg/) turns each whole page into an image, text and all. Use it when you want a picture of the page, for example to post a page on social media or put a full page into slides.

Quick rule: want *the photo on page 3*? Extract. Want *page 3 as a photo*? Convert.

## How to extract pictures from a PDF

1. Open the [PDF Image Extractor](/pdf-image-extractor/).
2. Add your PDF file.
3. Press **Extract images**. A progress bar shows the tool working through the pages.
4. Download your images:
   - If there is more than one, you get a **ZIP file with all the images** in one click.
   - Individual images are also listed (up to the first 20) so you can grab just the one you need.

Each image is saved as a **PNG**, named after the PDF, the page it came from and its number, for example `brochure-p3-img5.png`. That naming makes it easy to find "the picture from page 3" later.

## What you will (and will not) get

**Included:**

- Photos and pictures embedded in the PDF
- Scanned pages, which are themselves images inside the PDF
- Logos and icons stored as images

**Skipped or not possible:**

- **Tiny images** (16 pixels or smaller), such as bullet graphics and spacer dots, are ignored so your ZIP is not full of clutter.
- **Vector graphics**, such as many charts, shapes and diagrams drawn directly in Word or PowerPoint, are not stored as pictures, so there is nothing to extract. For those, convert the page with PDF to JPG or [PDF to PNG](/pdf-to-png/) and crop.
- **Text** is never included. If you need the words, use a text tool such as [PDF to Word](/pdf-to-word/).

## How good will the quality be?

The extractor saves each image at the resolution it was stored at inside the PDF. It does not shrink it, and it cannot add detail that is not there. So:

- A high-quality brochure from a designer usually gives sharp, large images.
- A PDF that was compressed to make it small for email may contain low-resolution images. They will come out the same.
- Scanned documents give you each scanned page as one image, at the scanner's resolution.

If an image comes out too small for your needs, the [Image Upscaler](/image-upscaler/) can enlarge it. If the PNG files are larger than you want, the [Image Compressor](/image-compressor/) or a PNG to JPG conversion will bring the size down.

## Examples

**Reusing your own photos.** You made a PDF portfolio months ago and lost the original image files. Extract them back out of the PDF.

**Making slides from a report.** Pull the diagrams out of a report, as long as they were saved as images, and drop them straight into a presentation with proper credit.

**Getting scanned pages as images.** A PDF of scanned forms gives you each page as a clean image you can crop, edit or send separately.

**Checking what is inside a file.** Curious why a PDF is 40 MB? Extracting the images shows you which large pictures are making it heavy.

A note on rights: pictures in other people's documents still belong to their owners. Extract freely from your own files, and check permission before reusing anyone else's images.

## Common problems

**"No embedded images found."** The PDF contains no pictures the tool can save. This usually means the visuals are vector graphics or that the file is plain text. Use PDF to JPG to get page images instead.

**"I got the whole page instead of the picture."** The PDF was probably made by scanning, so each page is a single image. That page image is the picture.

**"The colours look odd on one image."** Some PDFs store images in special colour formats meant for printing. Most come out fine, but occasionally colours shift. Converting that page with PDF to JPG gives you what you see on screen.

**"It is taking a while."** Long PDFs with many large images take longer, especially on phones. Keep the tab open until the progress bar finishes.

## Privacy

The PDF Image Extractor works entirely in your browser. Your PDF is read on your own device, the images are created there, and nothing is uploaded to DoraPDF's server.

## FAQ

**Can I extract images from a PDF without losing quality?**
Yes. Images are saved at the resolution stored in the PDF and exported as lossless PNG.

**What format are the extracted images?**
PNG. Convert them with the PNG to JPG tool if you need JPG files.

**Can I extract images from a PDF on my phone?**
Yes. It works in Android and iPhone browsers, and you can download all the images together as a ZIP.

**Why are some pictures missing?**
Charts and shapes drawn as vector graphics are not stored as images. Convert those pages to JPG instead.

**Is this the same as PDF to JPG?**
No. The extractor saves the pictures inside the PDF; PDF to JPG turns whole pages into images.
"""),
dict(slug='convert-pptx-to-pdf-free-online', title='Convert PPTX to PDF Free Online: Turn Slide Text Into a Clean Handout', date='2026-11-12',
 desc='Convert a PowerPoint PPTX to a PDF handout in your browser, with no PowerPoint installed. What it keeps, what it skips, and when to export instead.',
 tools=['pptx-to-pdf', 'pdf-to-powerpoint', 'pdf-merger'], md="""
A classmate sends you the lecture slides as a **.pptx** the night before the exam. You are on a borrowed laptop, or on your phone, and there is no PowerPoint anywhere. You do not need the animations or the fancy theme. You need the words, in a file you can read, print or highlight.

That is exactly the job DoraPDF's free [PPTX to PDF converter](/pptx-to-pdf/) is built for. It lets you **convert PPTX to PDF online for free** without installing PowerPoint: it pulls the text out of every slide, in order, and lays it out as a tidy A4 PDF handout. This guide explains how to use it, what you get, and when a different method is the better choice.

## First, know what kind of PDF you will get

Search results for "PowerPoint to PDF" promise all sorts of things, so it is worth being clear up front. This tool makes a **text handout**, not a picture-perfect copy of your slides.

**What comes through:**

- Every slide, in the original order
- A clear label before each one: *Slide 1*, *Slide 2* and so on
- Titles, bullet points and the text inside text boxes
- The file name as a heading at the top of the first page

**What does not:**

- Slide backgrounds, themes, colours and layouts
- Pictures, icons, charts and videos
- Speaker notes
- Animations and transitions

For revision notes, reading on a phone, pasting into your own notes, or printing a compact copy for marking up, that is often *better* than a full-colour export. Forty slides of text usually fit on a few pages instead of forty.

## How to convert PPTX to PDF on DoraPDF

1. Open the [PPTX to PDF converter](/pptx-to-pdf/).
2. Drop your **.pptx** file on the upload area, or click to choose it. On a phone, pick it from Files, Downloads or your email attachments.
3. Press **Convert now**.
4. Press **Download** when the PDF appears. It has the same name as your presentation.

There is no sign-up and no watermark. The whole process runs inside your browser.

## Example: from 32 slides to a 4-page study sheet

Imagine a biology lecture with 32 slides. Each slide has a title and four or five bullets, plus a diagram or two. Exported as a normal PDF, that is 32 pages, mostly white space and images you have already seen in class.

Run it through the converter and you get a handful of A4 pages where each slide is a short block of text under its label. You can print that, highlight the key terms, and still find the original slide in seconds because the slide numbers match.

## Common problems and quick fixes

**"My file will not upload."** The tool accepts **.pptx** only. Older **.ppt** files (PowerPoint 97-2003) need to be opened in PowerPoint, Google Slides, Keynote or LibreOffice Impress and saved as .pptx first.

**"Some text is missing."** Text that lives inside a picture (a screenshot of a table, a scanned page, a logo with words) is part of the image, so it cannot be read as text. Text inside charts, SmartArt graphics and speaker notes is stored separately from the slide text and is not included either. If a slide looks almost empty in the PDF, it was probably built mostly from images.

**"The order looks odd on one slide."** The text is read in the order it is stored in the file, which is usually the order the boxes were added. On slides with lots of floating text boxes that order can differ from what your eye expects. The content is all there; it is just worth a quick read-through.

**"I need the slides to look exactly like the presentation."** Then you want an export, not a text conversion. See the next section.

## When to export from the presentation app instead

If the design matters (a portfolio, a pitch deck for a client, a presentation a teacher will grade on visuals), let the program that made the file draw it:

- **PowerPoint:** File, then Save As or Export, then choose PDF.
- **Google Slides:** upload the file to Google Drive, open it with Google Slides, then File, Download, PDF document.
- **Keynote on Mac or iPhone:** open the file, then Export To, PDF.

Those apps know exactly how each slide is drawn, so backgrounds, images and fonts stay in place. DoraPDF's converter is the fast option when you only need the words, or when none of those apps is available on the device you are holding.

## Privacy: your slides stay on your device

The .pptx file is opened and converted inside your browser. It is not uploaded to a DoraPDF server, which matters when the deck contains unreleased business plans, exam material or client names. Once the page has loaded, you could even switch off your connection and the conversion would still work.

## Make the most of the handout

A few small habits turn the PDF into a useful study or meeting document:

- **Merge several lectures into one file.** Convert each deck, then combine them in order with the [PDF Merger](/pdf-merger/). One file per subject is easier to search than ten.
- **Add your own notes.** Open the handout in the [PDF Editor](/pdf-editor/) and type comments next to the slides you find hard.
- **Shrink it for sharing.** Text-only PDFs are already small, but if you merged a whole semester, the [PDF Compressor](/pdf-compressor/) can make it easier to send.
- **Going the other way?** If someone sends you a PDF and you need editable slides, the [PDF to PowerPoint converter](/pdf-to-powerpoint/) turns every page into a slide.

## FAQ

**Can I convert PPTX to PDF without PowerPoint?**
Yes. Open the [PPTX to PDF converter](/pptx-to-pdf/) in any modern browser, add the file and download the PDF. You do not need PowerPoint or any other app installed.

**Does it work on a phone?**
Yes. It runs in Safari, Chrome and other mobile browsers. Choose the .pptx from your Files app, Downloads folder or an email attachment.

**Will my images and slide design be kept?**
No. The tool keeps the text of each slide only. For a full visual copy, export to PDF from PowerPoint, Google Slides or Keynote.

**Can I convert a .ppt file?**
Not directly. Save it as .pptx first in a presentation app, then convert.

**Is it really free?**
Yes, with no account, no watermark and no limit on how many presentations you convert.
"""),
dict(slug='jpg-to-png-png-to-jpg-png-to-webp-converter', title='JPG to PNG, PNG to JPG or PNG to WebP? How to Convert (and When Each One Makes Sense)', date='2026-11-12',
 desc='Convert JPG to PNG, PNG to JPG, PNG to WebP, PDF to PNG and more for free in your browser, and learn which conversion actually helps your file.',
 tools=['jpg-to-png', 'png-to-jpg', 'png-to-webp', 'pdf-to-png', 'png-to-pdf'], md="""
Upload forms are picky. One portal wants **JPG only**, a design tool wants **PNG**, and a website speed test tells you to "serve images in next-gen formats". So you search **convert PNG to JPG**, or **JPG to PNG online**, and find a dozen converters that all look the same.

The conversion itself takes seconds. The useful part is knowing *which* conversion helps and which one just makes a bigger file. This guide covers DoraPDF's free image converters, what each one does under the hood, and a simple rule for choosing.

If you want the background on the formats themselves, our earlier guide [JPG vs PNG vs WebP](/blog/jpg-vs-png-vs-webp/) explains how each format stores an image. This one is the practical, "which button do I press" companion.

## The converters at a glance

| You have | You need | Tool |
| --- | --- | --- |
| JPG / JPEG photo | PNG | [JPG to PNG](/jpg-to-png/) or [JPEG to PNG](/jpeg-to-png/) |
| PNG screenshot or graphic | Smaller JPG | [PNG to JPG](/png-to-jpg/) |
| PNG for a website | WebP | [PNG to WebP](/png-to-webp/) |
| PDF pages | PNG images | [PDF to PNG](/pdf-to-png/) |
| PNG images | One PDF | [PNG to PDF](/png-to-pdf/) |
| Adobe Illustrator .ai | PNG | [Illustrator to PNG](/illustrator-to-png/) |
| OpenDocument file (.odt, .odp, .ods, .odg) | JPG or PNG | [ODF to JPG](/odf-to-jpg/) or [ODF to PNG](/odf-to-png/) |

All of them work the same way: open the tool, drop your file(s), press the button, download. They run inside your browser, so your images are not uploaded to a server.

## JPG to PNG: when it helps and when it does not

JPG and JPEG are the same format with two spellings, which is why the two tools behave identically. Both re-save your photo as a PNG, pixel for pixel.

**Convert JPG to PNG when:**

- An app or upload form only accepts PNG.
- You plan to edit the image several times. PNG is lossless, so saving it again and again does not add new blur or blocky artefacts the way repeated JPG saves can.
- You want to cut out the background later. PNG supports transparency, so once your image is a PNG, a tool like the [Background Remover](/image-background-remover/) can make parts of it see-through.

**Do not expect:**

- **Better quality.** Converting cannot restore detail the JPG already threw away. The PNG looks the same as the JPG it came from.
- **A smaller file.** A photo saved as PNG is usually *larger*, sometimes several times larger. That is normal.
- **Automatic transparency.** A JPG has no transparent areas, so the PNG will not have any either until you remove a background.

You can add several JPGs at once and each one comes back as its own PNG.

## PNG to JPG: the quick way to shrink screenshots and photos

PNG is great for screenshots, logos and text, but a phone photo saved as PNG can be huge. Converting to JPG is often the fastest way to get under an upload limit.

The [PNG to JPG converter](/png-to-jpg/) has a **Quality** slider (40 to 100, starting at 92). Lower numbers mean smaller files. For most photos, somewhere between 75 and 90 is hard to tell apart from the original on a screen.

One thing to know: **JPG cannot store transparency**, so any see-through areas in your PNG are filled with **white**. A logo on a transparent background becomes a logo on a white square. If you need the transparency, convert to WebP instead, or keep the PNG.

## PNG to WebP: for websites and blogs

WebP is a modern format that most current browsers display. It can store transparency like PNG while often producing a much smaller file, which is why speed tools recommend it.

The [PNG to WebP converter](/png-to-webp/) also has a quality slider. Transparent areas stay transparent. Use WebP for images on your own website or blog. For forms, email attachments or anything someone might open in older software, JPG or PNG is the safer choice, because not every program opens WebP files.

## PDF to PNG and PNG to PDF

These two go in opposite directions and are handy for documents.

**[PDF to PNG](/pdf-to-png/)** turns every page into a sharp image. Pick a quality level: **Normal** for screens, **High** for printing (the default), or **Ultra** when you need to zoom in on fine print. A multi-page PDF also gives you a single .zip with all the pages, so you do not have to download them one by one. PNG keeps text crisp, which makes it the right choice for slides, diagrams and pages with small writing. For photo-heavy pages where size matters more, try [PDF to JPG](/pdf-to-jpg/).

**[PNG to PDF](/png-to-pdf/)** does the reverse: add one or more PNGs and each becomes a page, in the order you added them. You can choose **Fit page to image**, **A4** or **US Letter**, and a margin. It is a neat way to turn a set of screenshots into one document for a teacher or a bug report.

## Illustrator and OpenDocument files

**[Illustrator to PNG](/illustrator-to-png/)** converts the first artboard of an .ai file into a high-resolution PNG. It works with files saved with **PDF compatibility**, which is Illustrator's default setting. If you see an error, open the file in Illustrator, choose Save As, and make sure "Create PDF Compatible File" is ticked.

**[ODF to JPG](/odf-to-jpg/)** and **[ODF to PNG](/odf-to-png/)** accept LibreOffice and OpenOffice files. They rebuild the text (headings and paragraphs) and embedded pictures onto clean A4-sized pages, one image per page. They do not reproduce the exact fonts and layout of the original, so treat the result as a readable snapshot rather than a pixel-perfect copy. If the file has no text or pictures to read, the tool falls back to the preview thumbnail saved inside it.

## A simple rule for choosing

- **Photo, need small:** JPG.
- **Screenshot, text, logo, or need transparency:** PNG.
- **Image for your own website:** WebP.
- **Several images that must travel together:** one PDF.

## Privacy

Every converter on this page runs in your browser. Your photos, documents and design files stay on your device and are not sent to DoraPDF's servers.

## FAQ

**Is converting JPG to PNG lossless?**
The conversion itself adds no new loss, but it cannot undo the compression already in the JPG. The PNG will look the same as the source.

**Why is my PNG bigger than the JPG?**
PNG keeps every pixel exactly, which takes more space for photos. If size matters, keep the JPG or try WebP.

**Why did my transparent PNG get a white background?**
You converted it to JPG, which has no transparency. Use [PNG to WebP](/png-to-webp/) or keep it as PNG.

**Can I convert many files at once?**
Yes. The JPG, JPEG, PNG and WebP converters accept multiple images in one go.
"""),
dict(slug='resize-image-to-exact-pixels-online', title='How to Resize an Image to Exact Pixels Online (Free, Batch, Keeps Proportions)', date='2026-11-12',
 desc='Resize photos to exact pixel sizes or by percentage for forms, Instagram, YouTube and websites. Free, in your browser, with batch resizing.',
 tools=['image-resizer', 'image-compressor', 'image-flipper'], md="""
"Photo must be 600 x 600 pixels." "Upload a banner of 1500 x 500." "Image width should not exceed 1280px." Size rules like these turn up on job portals, university admission forms, online shops and social media, and they are strict: upload the wrong size and the form simply refuses it.

DoraPDF's free [Image Resizer](/image-resizer/) lets you **resize an image to exact pixels online** or shrink it by a percentage, for one photo or a whole batch. This guide shows how to use it, how the aspect-ratio setting really works, and how to handle the "must be under 50 KB" rule that often comes with a pixel size.

## Pixels vs. kilobytes: two different limits

Most confusion around resizing comes from mixing up two numbers:

- **Dimensions** (for example 600 x 600 pixels) are the width and height of the picture.
- **File size** (for example 50 KB) is how much storage the file takes.

Resizing changes the dimensions, and as a side effect it usually makes the file smaller, because there are fewer pixels to store. But if a form gives you a **KB limit**, the tool for that is a compressor. The workflow at the end of this post combines both.

## How to resize an image on DoraPDF

1. Open the [Image Resizer](/image-resizer/).
2. Drop one or more images onto the page. On a phone, pick them from your gallery.
3. Choose a **Mode**:
   - **By pixels:** type a **Width** and/or **Height**.
   - **By percentage:** type a percent, such as 50 to halve both sides.
4. Leave **Keep aspect ratio** ticked unless you deliberately want to stretch the picture.
5. Pick the **Output** format: same as the original, JPG, PNG or WebP.
6. Press **Resize** and download. Each file name ends with its new size, like *photo-600x600.jpg*, so you can see at a glance that it worked.

Everything happens inside your browser; the images are not uploaded.

## How "Keep aspect ratio" behaves (worth reading once)

The aspect-ratio checkbox decides how width and height work together:

- **Only width filled in:** the height is calculated automatically so the photo is not squashed. Type 1080 and a 4000 x 3000 photo becomes 1080 x 810.
- **Only height filled in:** the same, the other way round.
- **Both filled in, box ticked:** the image is scaled to **fit inside** that box without distortion. A 4000 x 3000 photo resized to 600 x 600 becomes 600 x 450, because squeezing it to a square would stretch it.
- **Both filled in, box unticked:** you get exactly the numbers you typed, even if that stretches the image.

So when a form demands an **exact square**, crop your photo to a square first (most phone gallery editors have a square crop), then resize with the box ticked. You will get exactly 600 x 600 with nothing stretched.

## Practical size examples

These are sizes people commonly need. Always check the current rules of the site or form you are using, since platforms change them.

- **Profile pictures:** square images such as 400 x 400 or 800 x 800 work on most sites.
- **Website content images:** a width of 1200 to 1600 pixels is plenty for most blog layouts.
- **Email attachments:** 1280 pixels wide keeps photos clear on a laptop screen at a fraction of the original size.
- **Thumbnails and previews:** 25% to 50% of a modern phone photo is usually enough.

A phone photo is often 4000 pixels wide or more, which is far larger than any of these. Resizing first is one of the easiest ways to make uploads faster.

## Batch resizing: the time-saver

You can add many images at once. The same settings are applied to each one, and each comes back as a separate download. This is ideal for:

- Product photos for an online shop that all need the same width
- A folder of event pictures you want to share without sending huge files
- Screenshots for a report that should all be the same size

With **Keep aspect ratio** on and only a width set, photos of different shapes all end up the same width while keeping their own proportions.

## Common problems and fixes

**The image looks blurry after resizing.** You probably made it *bigger*. Resizing up cannot invent detail. If you need a larger, sharper version of a small picture, try the AI [Image Upscaler](/image-upscaler/) instead.

**My transparent PNG now has a white background.** You chose JPG as the output. JPG has no transparency, so the empty areas become white. Choose PNG or WebP to keep them see-through.

**The size is right but the file is still too heavy.** Run the resized image through the [Image Compressor](/image-compressor/), or resize to JPG or WebP, which are usually much smaller than PNG for photos.

**The photo is sideways or mirrored.** Fix the orientation first with the [Image Flipper](/image-flipper/), then resize.

**A file will not open, or the output looks wrong.** Your browser may not read that format well. Convert it to JPG first (for iPhone HEIC photos, use the [HEIC to JPG converter](/heic-to-jpg/)), then resize.

## Workflow for "600 x 600 and under 50 KB"

Many application forms ask for both. Here is a reliable order:

1. Crop the photo to the required shape in your phone's editor.
2. Resize it to the exact pixel size in the [Image Resizer](/image-resizer/), output **JPG**.
3. If it is still over the limit, open the [Image Compressor](/image-compressor/), choose **Original size** under Resize (so your pixel size stays the same), and try **Balanced** or **Strong** strength.
4. Check the file size before uploading.

A 600 x 600 JPG is usually small already, so step 3 is often unnecessary. For a detailed walkthrough of hitting KB targets, see our guide on [compressing JPEG to 100 KB or 200 KB](/blog/compress-jpeg-online-without-losing-quality/).

## Privacy

The Image Resizer runs entirely in your browser. Your photos, including ID pictures and personal shots, never leave your device.

## FAQ

**How do I resize an image without losing quality?**
Make it smaller, not bigger, and keep the aspect ratio ticked. Output PNG if you want no compression at all, or JPG for a smaller file.

**Can I resize photos on my iPhone or Android phone?**
Yes. The [Image Resizer](/image-resizer/) works in mobile browsers; choose photos from your gallery and download the results.

**Can I resize several images at once?**
Yes. Add as many as you need; the same settings apply to all.

**How do I resize an image to a specific KB size?**
Resize to the needed pixels first, then use the [Image Compressor](/image-compressor/) to reduce the file size further.
"""),
dict(slug='compress-images-online-bulk-strength-settings', title='Compress Images Online in Bulk: Which Strength and Size to Pick (Free Image Compressor)', date='2026-11-12',
 desc='A practical guide to the free DoraPDF Image Compressor: batch-compress JPG and PNG photos, pick Light, Balanced or Strong, and choose the right max width.',
 tools=['image-compressor', 'image-resizer', 'png-to-webp'], md="""
You have forty photos from a family wedding, a product shoot or a field trip, and every one of them is 3 to 6 MB. Email bounces them, the website upload crawls, and your phone storage is complaining. Compressing them one at a time is not an option.

DoraPDF's free [Image Compressor](/image-compressor/) is built for exactly this: drop in a whole batch, pick two settings, and download smaller copies. If you have been searching for a way to **compress images online for free** without uploading them anywhere, this guide explains what each setting does and which combination fits the job in front of you.

(Need to hit a strict number like 100 KB for a form? We cover that step by step in [Compress JPEG Online Without Losing Quality](/blog/compress-jpeg-online-without-losing-quality/). This post focuses on everyday batch compression.)

## The two settings that matter

The compressor keeps things simple. There are only two choices, and together they decide how small your files get.

### 1. Strength

- **Light:** the gentlest setting. Files shrink, but quality stays very close to the original. Good for portfolios and prints.
- **Balanced** (default): the sweet spot for most people. On a phone or laptop screen it is hard to see a difference, while files usually get much smaller.
- **Strong:** the smallest files. Fine detail softens a little. Good for previews, chat apps and very tight limits.

### 2. Resize

- **Original size:** keeps the pixel dimensions and only compresses.
- **Max 2560px, 1920px** (default)**, 1280px or 800px:** limits the **width** of each image. Photos already narrower than the limit are not enlarged.

Here is the part many people miss: **resizing often saves more space than compression does.** A modern phone photo can be 4000 pixels wide. Bringing it down to 1920 pixels removes most of the pixels before compression even starts, which is why 1920 is the default.

## Quick recipes

| Goal | Strength | Resize |
| --- | --- | --- |
| Website or blog photos | Balanced | Max 1920px or 1280px |
| Emailing a batch of photos | Balanced | Max 1920px |
| Sharing in a chat or group | Strong | Max 1280px |
| Keeping a good archive copy | Light | Original size |
| Thumbnails or previews | Strong | Max 800px |

Start with the recipe, look at one or two results, and adjust if needed. Compression is fast, so trying a second combination costs only seconds.

## How to compress images in bulk

1. Open the [Image Compressor](/image-compressor/).
2. Drop all your images onto the upload area (or tap to pick them from your gallery). You can keep adding more; each appears in the list with its size.
3. Choose **Strength** and **Resize**.
4. Press **Compress**.
5. Each result shows its new name and how much smaller it got, for example *IMG_2041-small.jpg · 78% smaller*. Download the ones you want.

The originals are never changed. You always get new copies with *-small* added to the name.

## Why some files come back as WebP

This surprises people the first time, so it is worth explaining. The compressor treats files differently depending on their type:

- **JPG photos** (and most other images) are saved as **JPG**. Any transparent areas, for example in a GIF, are filled with white.
- **PNG files** are saved as **WebP**.

The reason is transparency. A PNG logo or screenshot often has see-through areas, and saving it as JPG would put a white box behind it. WebP keeps the transparency while making the file far smaller than a PNG.

WebP works in all current major browsers and on most websites. If you need a PNG or JPG specifically, for example for an old program or a form that rejects WebP, convert the result with the [WebP to PNG](/webp-to-png/) or [WebP to JPG](/webp-to-jpg/) tool, or use [PNG to JPG](/png-to-jpg/) directly on the original if transparency does not matter.

## Common problems and fixes

**"0% smaller" or almost no change.** The image was already compressed heavily, or it is already small. Try **Strong**, or choose a smaller **Resize** value. Very small graphics sometimes cannot shrink further.

**Text in a screenshot looks fuzzy.** Use **Light** strength and **Original size**. Text and sharp lines show compression more than photos do.

**The colours behind a logo turned white.** The file was not a PNG (for example a transparent GIF), so it was saved as JPG. Convert it to PNG first, then compress, and you will get a transparent WebP.

**I need an exact pixel size, not a max width.** Use the [Image Resizer](/image-resizer/) first, then compress with Resize set to **Original size** so your dimensions are kept.

**iPhone HEIC photos.** Convert them with [HEIC to JPG](/heic-to-jpg/) first if your browser does not open them, then compress.

## Privacy: your photos stay with you

The compressor runs inside your browser using your device's own processing power. Your images are not uploaded to a DoraPDF server, so private family photos, ID scans and unreleased product pictures stay on your phone or computer.

## Related tools

- [Image Resizer](/image-resizer/): set exact pixel dimensions or scale by percent.
- [PNG to WebP](/png-to-webp/): convert graphics to WebP with your own quality setting.
- [Compress GIF](/compress-gif/): shrink animated GIFs.
- [PDF Compressor](/pdf-compressor/): when the photos are already inside a PDF.

## FAQ

**Is the Image Compressor free?**
Yes. No account, no watermark, no daily limit.

**How many images can I compress at once?**
You can add many in one go. Very large batches depend on your device's memory, so on an older phone, work in groups of 20 or 30.

**Does compressing reduce quality?**
A little, by design. **Light** and **Balanced** are chosen so the difference is hard to see on a screen. Keep your originals if you might need full quality later.

**Why is my PNG now a .webp file?**
WebP keeps the transparency of PNG while being much smaller. Convert it back with [WebP to PNG](/webp-to-png/) if you need the PNG format.
"""),
dict(slug='remove-date-stamp-logo-from-your-photo', title='How to Remove a Date Stamp or Logo From Your Own Photo (Free Brush Tool)', date='2026-11-12',
 desc='Erase an old camera date stamp, your own logo or a stray caption from a photo you own. Free brush tool that runs in your browser, with tips for clean results.',
 tools=['watermark-eraser', 'object-remover', 'image-upscaler'], md="""
Old digital cameras loved stamping the date in orange numbers across the corner of every picture. Phone apps add captions and stickers. Sometimes you put your own logo on a photo years ago and now want a clean version for a new website. In all of these cases the picture is yours, and the mark is in the way.

DoraPDF's free [Watermark Eraser](/watermark-eraser/) lets you **remove a date stamp from a photo** (or a small logo or bit of text) by brushing over it. The tool fills the area using the surrounding pixels, right in your browser. This guide shows how to get a clean result and what kind of marks it handles best.

## A quick word on whose photos these are

This tool is meant for images you own or have permission to edit: your own pictures, your family's photos, or files from a client who asked you to clean them up. Watermarks on stock photos and other people's work are there to protect the creator. If you want to use one of those images, buy a licence or ask the owner, rather than erasing the mark.

## What the eraser is good at

The tool works by "inpainting": it looks at the pixels around the area you painted and fills the gap so it blends in. That works best when the surroundings are fairly simple. Good candidates:

- **Camera date stamps** in a corner, over sky, grass, a wall or a table
- **Small logos or handles** on a plain or softly blurred background
- **Short captions or stray text** added by an app
- **Dust spots and small marks** on scanned prints

Harder cases:

- Large, semi-transparent watermarks across the middle of the picture
- Marks sitting over faces, detailed patterns or text you want to keep
- Very large areas, where there is not enough nearby detail to borrow from

For those, expect to need several passes, or accept that the result will be softer in that spot.

## Step by step

1. Open the [Watermark Eraser](/watermark-eraser/) and add your photo (JPG, PNG, WebP or iPhone HEIC).
2. Set the **Brush size** with the slider. Pick something a little wider than the strokes of the numbers or letters.
3. Paint over the mark. It turns pink so you can see what is selected. **Go slightly past the edges**; leftover outline pixels are the most common reason a faint ghost remains.
4. Choose a **Fill style**, or leave it on **Auto**:
   - **Auto (recommended):** picks a method based on how busy the surroundings are.
   - **Smooth fill:** best for logos on flat colours, skin, sky and plain walls.
   - **Texture:** better on busy photos such as grass, gravel or foliage.
   - **Lines & edges:** helps when the mark crosses a straight edge, like a table edge or horizon.
5. Press **Remove object**. The first time, the tool loads its image engine, which can take a few seconds.
6. If a faint trace is left, brush over it again and press Remove once more. Small repeated passes beat one giant stroke.
7. Press **Download PNG** when you are happy.

Made a mistake? **Undo** steps back (up to 15 times), and **Clear brush** removes your pink strokes without changing the picture.

## Tips for a cleaner result

**Work in pieces.** For a long date like *2009 08 14*, brush and remove two or three digits at a time. Each fill then has more real background around it.

**Try a different fill style before giving up.** If Auto leaves a smudge on a textured background, undo and try **Texture**. If it leaves a blotch on a plain wall, try **Smooth fill**.

**Zoom out to judge.** At full size you might spot a soft patch. At normal viewing size, on a phone or in an album, it usually disappears.

**Crop when you can.** If the stamp is right at the edge, simply cropping it out may be the cleanest answer of all.

## Size and quality notes

To keep things fast on phones, photos wider than **1400 pixels** are scaled down to that width when loaded, and the download is a PNG at that size. That is plenty for screens, social media and most web pages. If you need a bigger file afterwards, the AI [Image Upscaler](/image-upscaler/) can enlarge it 2x or 4x. Want a smaller file to share? Run the PNG through the [Image Compressor](/image-compressor/).

## Common problems

**"Brush over the object you want to remove first."** You pressed Remove without painting anything. Paint the mark, then press Remove.

**A blurry patch remains.** The area was large or detailed. Undo, use a slightly smaller brush, and remove the mark in smaller sections.

**Colours around the mark changed slightly.** The tool softens a thin ring around the filled area so there is no hard seam. On flat backgrounds this is invisible; on strong patterns, try the Texture style.

**The engine does not load.** It needs a modern browser with enough memory. Close other heavy tabs, or try on a computer.

## Privacy

Your photo is processed on your own device. The image engine is downloaded to your browser once and does the work locally, so the picture itself is never uploaded to DoraPDF.

## Related tools

- [Object Remover](/object-remover/): the same brush approach for bigger things, such as a person in the background or a bin in a landscape. We wrote a full guide on [removing objects from photos](/blog/remove-object-from-photo-free/).
- [Image Upscaler](/image-upscaler/): make the cleaned photo larger and sharper.
- [Background Remover](/image-background-remover/): cut out the subject completely.

## FAQ

**Can I remove a date stamp from an old photo for free?**
Yes. Add the photo to the [Watermark Eraser](/watermark-eraser/), brush over the date and press Remove. There is no sign-up or watermark.

**Does it work on a phone?**
Yes. You can paint with your finger in Safari or Chrome. A slightly bigger brush is easier on a small screen.

**Will it remove any watermark perfectly?**
No tool can promise that. Small marks on simple backgrounds come out very clean; large marks over detailed areas may leave a soft patch.

**Is it legal to remove a watermark?**
Removing marks from your own photos is fine. Removing a creator's watermark from their work to use it without permission can break copyright rules, so do not do that.
"""),
dict(slug='free-resume-builder-pdf-no-sign-up', title='Free Resume Builder With PDF Download (No Sign-Up, No Watermark)', date='2026-11-12',
 desc='Build a clean one-column resume in your browser and download it as a PDF. No account, no paywall at the download step, and tips for each section.',
 tools=['resume-builder', 'pdf-compressor', 'pdf-merger'], md="""
Plenty of "free" resume sites let you type everything in, choose a template, and then ask for payment at the exact moment you press Download. If you just need a tidy CV for a job application, internship or university form, that is frustrating.

DoraPDF's [Resume Builder](/resume-builder/) is a simple **free resume builder with PDF download**. No sign-up, no watermark, no paid step at the end. You fill in a short form, choose an accent colour, and get a clean A4 PDF. Below is how it works and how to write each section so the result reads well.

## What kind of resume it makes

The builder produces one layout, on purpose: a **single-column, text-based resume**.

- Your **name** large at the top, your **job title** in your accent colour underneath
- A contact line with email, phone, city and website or LinkedIn
- A coloured divider, then sections for **Summary**, **Experience**, **Education** and **Skills**
- Clean Helvetica text on A4 paper

The text in the PDF is real, selectable text, not a picture. A plain single-column layout like this is easy for recruiters to skim, and application tracking systems generally read it more reliably than layouts built from columns, icons and graphics.

What it does not do: there is no photo, no multiple templates and no rating bars. If a job ad asks for a photo, or you want a highly designed CV for a creative role, you will need a design tool for that.

## Build your resume step by step

1. Open the [Resume Builder](/resume-builder/).
2. Fill in **Full name** and **Job title** (the role you are applying for, or your current one).
3. Add **Email**, **Phone**, **City** and **Website / LinkedIn**. Leave any of them blank and it simply will not appear.
4. Write a short **Summary**.
5. Fill in **Experience**, with a blank line between jobs.
6. Fill in **Education**.
7. List **Skills**, separated by commas.
8. Pick an **Accent color** if you want something other than the default deep pink. Navy, dark green and charcoal all look professional.
9. Press **Download resume PDF**. The file is named after you, like *Ayesha-Khan-resume.pdf*.

Any section you leave empty is skipped, so a fresh graduate without work history will not get an empty "Experience" heading.

## How the formatting works (small trick, big difference)

In the Experience and Education boxes, the builder looks at how each line starts:

- A line that starts with **•**, **-** or **\\*** is treated as a **bullet point** and printed in normal weight.
- Any other line is printed in **bold**, which makes it perfect for the job title, company and dates.

So this:

    Sales Associate — City Mart, Lahore (2023 – Present)
    • Handled 120+ customers a day at peak times
    • Trained 4 new staff members on the billing system

    Intern — ABC Traders (Summer 2022)
    • Prepared weekly stock reports in Excel

prints each role in bold with neat bullets underneath, and the blank line adds space between jobs. Long lines wrap automatically, and a second page is added if you run out of room.

## Writing tips for each section

**Summary (2 to 3 lines).** Say what you do, your strongest area and what you are looking for. *"Commerce graduate with two years of retail experience and strong Excel skills, looking for an entry-level accounts role in Karachi."* Avoid vague lines like "hard-working team player" unless you back them up below.

**Experience.** Start each bullet with an action verb (managed, built, reduced, trained) and add a number where you honestly can: customers served, reports prepared, time saved. Keep it to the last few relevant roles. Part-time jobs, internships and volunteer work all count, especially early in your career.

**Education.** Most recent first: degree, institution, years. Add a grade or a relevant project if it helps.

**Skills.** Be specific: *Excel (pivot tables), Urdu and English typing, Canva, customer service*. Match the words in the job ad where they are true for you.

**Length.** One page is ideal for students and early-career applicants. Two is fine with more experience.

## Common problems and fixes

**My bullet points came out bold.** The line did not start with •, - or \\*. Add one of those at the very start of the line.

**Some symbols look odd in the PDF.** The built-in PDF font handles standard English text and common punctuation. Unusual symbols, emoji or Urdu script may not display correctly, so stick to plain characters.

**I closed the tab and lost everything.** The builder does not save your entries anywhere, so refreshing or closing the page clears the form. Keep your text in a notes file so you can paste it back and make new versions quickly.

**I need to attach a cover letter or certificates in one file.** Download the resume, then combine it with your other PDFs using the [PDF Merger](/pdf-merger/). If the combined file is too heavy for an upload form, shrink it with the [PDF Compressor](/pdf-compressor/).

## Privacy

Your resume is built inside your browser. Your name, phone number and work history are not sent to DoraPDF or stored on a server. That is one more reason to keep your own copy of the text.

## More tools for job applications

- [Sign PDF](/sign-pdf/): sign an offer letter or form without printing it.
- [Image Resizer](/image-resizer/): get a profile or passport photo to the exact pixel size a portal asks for.
- [Email Signature generator](/email-signature/): make a professional signature for your job-search emails.

## FAQ

**Is this resume builder really free?**
Yes. Building and downloading the PDF is free, with no sign-up and no watermark.

**Can I make a resume on my phone?**
Yes. The form works in mobile browsers, and the PDF downloads to your phone, ready to attach to an email or upload.

**Can I add a photo?**
No. The builder makes a text-only resume. Many employers prefer CVs without photos anyway, but check what the job ad asks for.

**Can I edit the PDF later?**
Keep your text, change it in the form and download a new version. For small fixes on the PDF itself, you can also use the [PDF Editor](/pdf-editor/).
"""),
dict(slug='free-invoice-generator-pdf-pkr-usd', title='Free Invoice Generator: Make a PDF Invoice in PKR, USD, AED, EUR or GBP', date='2026-11-12',
 desc='Create a professional PDF invoice in a minute: line items, tax, discount, due date and your brand colour. Free, no account, works on phone and PC.',
 tools=['invoice-generator', 'receipt-generator', 'sign-pdf'], md="""
Freelancers, tutors, small shops and side businesses all hit the same moment: the work is done, and the client says, "Please send an invoice." A message on WhatsApp saying "Rs 25,000 please" is not quite the same thing. A proper invoice looks professional, gives the client a record for their accounts, and makes it clear what is owed and by when.

DoraPDF's [Invoice Generator](/invoice-generator/) is a **free invoice generator that downloads as PDF**. You fill in a form, add your items, and get a clean A4 invoice. No account, no subscription, no watermark. This guide walks through each field and shares a few habits that help invoices get paid on time.

## What goes on the invoice

The finished PDF includes:

- A thin colour bar and your **business name** at the top, with **INVOICE** in your brand colour
- Your **details** (address, phone, email)
- **Invoice number**, **date** and **due date**
- A **Bill to** block with the client's name and address
- An items table with **Item, Qty, Price** and **Total**
- **Subtotal**, optional **Tax** and **Discount**, and a highlighted **Total**
- Your **notes**, such as payment details or a thank-you line

Supported currencies are **PKR, USD, EUR, GBP and AED**, which covers most local clients and many international ones.

## How to create an invoice, field by field

1. Open the [Invoice Generator](/invoice-generator/).
2. **From:** your business or freelance name. If you work under your own name, that is fine.
3. **Invoice #:** a number is filled in for you (starting with *INV-*). You can replace it with your own system, for example *INV-2026-014*.
4. **Date** is today by default. Set a **Due date**; leave it empty and no due date is printed.
5. **Your details:** address, phone and email, one per line.
6. **Bill to:** the client's name and address, one per line.
7. **Items:** the form starts with two example lines. Change them to your own work, set the **Qty** and **Price**, and press **+ Add item** for more lines. The small cross removes a line.
8. **Currency:** pick PKR, USD, EUR, GBP or AED.
9. **Tax %:** enter a percentage if you charge tax, or leave it at 0.
10. **Discount (amount):** a fixed amount off, not a percentage. Leave at 0 for none.
11. **Brand color:** choose a colour that matches your logo or business card.
12. **Notes:** bank or wallet details, payment terms, a thank-you.
13. Press **Download invoice PDF**. The file is named after the invoice number.

## How the totals are calculated

The maths is simple and worth knowing so you can double-check:

- Each line total is **Qty x Price**.
- **Subtotal** is the sum of all lines.
- **Tax** is the tax percentage of the subtotal.
- **Total = Subtotal + Tax - Discount.**

Example: two lines, *Logo design* 1 x 15,000 and *Social media kit* 1 x 10,000, give a subtotal of Rs 25,000. With a discount of 2,000 and no tax, the total is Rs 23,000.

Tax rules differ by country, city and type of business. If you are unsure whether you need to charge tax, or at what rate, ask an accountant or check your tax authority's guidance before you send invoices.

## Habits that help you get paid

**Use a clear numbering system.** *INV-2026-001, 002, 003...* makes it easy to match payments later. Never reuse a number.

**Describe the work specifically.** "Website design" is vague. "5-page website design, including 2 rounds of revisions" prevents back-and-forth.

**Always set a due date.** "Due in 7 days" or a specific date gives both sides a clear expectation.

**Put payment details in Notes.** Bank name, account title, IBAN or wallet number. The easier it is to pay, the faster it happens.

**Keep a copy of every invoice.** Make a folder per year. When a client asks "which invoice was that?", you will have the answer.

## Common questions and fixes

**The example items are still on my invoice.** The form starts with two sample lines so you can see how it works. Edit or remove them before downloading.

**I need a percentage discount.** The discount field takes a fixed amount. Work it out first (10% of 25,000 is 2,500) and enter that number.

**My client wants it signed.** Download the invoice, then add your signature with [Sign PDF](/sign-pdf/).

**I need a receipt, not an invoice.** An invoice asks for payment; a receipt confirms that payment was received. Use the [Receipt Generator](/receipt-generator/) for that. It makes a narrow, till-style receipt.

**Can I save my details for next time?** The form does not store anything, so keep your business details and payment notes in a text file and paste them in. It takes seconds.

## Privacy

The invoice is created in your browser. Your client names, prices and bank details are not uploaded to DoraPDF or kept on a server.

## Related tools for small businesses

- [Receipt Generator](/receipt-generator/): confirm a payment with a printable receipt.
- [Sales Tax Calculator](/sales-tax-calculator/): check tax amounts before you invoice.
- [Profit Margin Calculator](/profit-margin-calculator/): make sure your prices actually cover your costs.
- [QR Code Generator](/qr-code-generator/): a QR code linking to your website or WhatsApp for your business card.

## FAQ

**Is the invoice generator free?**
Yes, completely. No account, no watermark, and you can make as many invoices as you like.

**Can I make an invoice in Pakistani rupees?**
Yes. Choose **PKR** in the currency menu and amounts are shown with *Rs*.

**Can I use it on my phone?**
Yes. It works in mobile browsers and the PDF is saved to your downloads, ready to send by email or WhatsApp.

**Can I add my logo?**
Not at the moment. You can match your branding with the **Brand color** setting, and your business name appears prominently at the top.
"""),
dict(slug='compress-video-online-free-without-uploading', title='Compress a Video Online Free, Without Uploading It: Settings, Sizes and Tips', date='2026-11-12',
 desc='Reduce video file size in your browser with no upload and no watermark. How the quality and resolution settings work, expected sizes, and fixes.',
 tools=['video-compressor', 'image-compressor', 'compress-gif'], md="""
Video files grow fast. A two-minute phone clip can easily be a few hundred megabytes, which is too big for most email attachments, slow to share, and painful to upload on mobile data. Most online compressors solve this by asking you to upload the whole file to their server first, which takes ages on a slow connection and means handing over a personal video.

DoraPDF's [Video Compressor](/video-compressor/) works differently. It lets you **compress a video online for free without uploading it**: the video is re-encoded right inside your browser, on your own device. This guide explains the settings, what file sizes to expect, and the one habit that makes it work reliably.

## How it works, in plain words

The compressor plays your video inside the page, redraws each frame at the resolution you chose, and records it again at a lower bitrate using your browser's built-in video encoder. The sound is recorded along with it.

Two things follow from that:

1. **It runs in real time.** A one-minute video takes about one minute to compress, a five-minute video about five minutes. It is not instant, but there is no upload or download wait either.
2. **The output is a WebM file.** WebM is an open video format that plays in Chrome, Firefox, Edge, on Android and in players like VLC. More on compatibility below.

## The two settings

### Quality (bitrate)

- **Small (400 kbps):** the smallest files. Fine for talking-head clips, lectures and screen recordings viewed on a phone.
- **Balanced (1 Mbps):** the default. A good mix of clarity and size for most phone videos.
- **High (2.5 Mbps):** for clips with lots of movement or detail where you still want a noticeable size cut.

### Resolution

- **Original resolution**
- **75%**
- **50%**

Lowering the resolution and the bitrate together works best. A 1080p clip at 50% becomes roughly 540p, which looks fine on a phone screen and needs far fewer bits to stay sharp.

## What file size to expect

The bitrate is a target, so you can estimate the size before you start. Very roughly, including sound:

| Setting | Approx. size per minute |
| --- | --- |
| Small (400 kbps) | about 3.5 MB |
| Balanced (1 Mbps) | about 8 MB |
| High (2.5 Mbps) | about 19 MB |

So a 3-minute clip on Balanced lands somewhere around 25 MB. Real results vary with the content: a still lecture often comes out smaller, fast action can come out larger. The result card shows exactly how much smaller your file got, for example *holiday-compressed.webm · 85% smaller*.

If your original is already small or low-bitrate (for example a video that was compressed by a chat app), the gain may be modest. Choosing **High** on an already-small file can even produce a bigger one, so pick a lower setting.

## Step by step

1. Open the [Video Compressor](/video-compressor/).
2. Drop in your video, or tap to choose it from your gallery or files.
3. Pick **Quality** and **Resolution**.
4. Press **Compress video**.
5. **Keep the tab open and in front** while the progress bar fills. On a phone, keep the screen on.
6. Press **Download** to save the compressed WebM.

## The one habit that matters: stay on the page

Because the video is processed as it plays, browsers may pause or slow that work if you switch to another tab, minimise the window or lock your phone. That can leave you with a choppy or incomplete file. Start the compression, then leave the tab in front until it finishes. It is a good moment to make tea.

## Compatibility: where WebM works

WebM plays well in:

- Chrome, Edge and Firefox on computers
- Android phones
- VLC and many other desktop players
- Most modern web platforms and video sites that accept uploads

Recent versions of Safari can play many WebM files too, but some older Apple devices, older editing software and certain apps expect **MP4** only. If you are sending the file somewhere that specifically asks for MP4, test with a short clip first, or use your phone's own export option to choose a smaller size.

## Common problems and fixes

**"This video format is not supported by your browser."** The browser cannot decode that file. Phone videos (MP4, MOV from recent phones, WebM) usually work in Chrome or Edge. If one browser refuses, try another.

**The output is shorter than the original or freezes in places.** The tab was probably in the background or the phone went to sleep. Run it again and keep the page visible.

**No sound in the result.** Some browsers block audio capture in certain situations. Try Chrome or Edge on a computer.

**It is too slow for a long video.** Compression is real time, so a 20-minute recording takes about 20 minutes. Trim the clip first if you only need part of it, or run it on a laptop while you do something else in another window (not another tab).

**The file is still too big.** Drop to **Small** and **50%**. For very long recordings, consider splitting them into parts before compressing.

## Privacy

This is the main reason to use a browser-based compressor. Your video never leaves your device: it is decoded, re-encoded and saved locally. Family clips, recorded classes and private meetings stay private.

## Other ways to shrink files on DoraPDF

- [Image Compressor](/image-compressor/): batch-compress photos from the same trip.
- [Compress GIF](/compress-gif/): reduce the size of animated GIFs.
- [PDF Compressor](/pdf-compressor/): when it is a document, not a video, that is too heavy.

## FAQ

**Is the video compressor free?**
Yes. No sign-up, no watermark, no limit on how many videos you compress.

**Is my video uploaded anywhere?**
No. Everything happens inside your browser on your own device.

**Why is the output WebM instead of MP4?**
Browsers have built-in encoders for WebM, which is what allows compression to happen locally without uploading your file.

**Can I compress a video on my phone?**
Yes, in a modern mobile browser. Keep the screen on and the page open until it finishes.

**Why does it take as long as the video?**
The compressor re-records the video as it plays, so the time matches the video length.
"""),
dict(slug='save-web-page-as-pdf-url-to-pdf', title='How to Save a Web Page as a PDF From Its URL (Works on Phone and PC)', date='2026-11-12',
 desc='Paste a link and get a PDF of the page, on A4 or US Letter, portrait or landscape. How URL to PDF works, plus the browser print method and fixes.',
 tools=['url-to-pdf', 'web-to-png', 'pdf-merger'], md="""
A news article you want to read offline. A job listing that might disappear next week. A product page you need as proof of what was advertised. A tutorial you want to print for class. In each case, the simplest thing is a PDF you can keep, highlight and share.

DoraPDF's free [URL to PDF converter](/url-to-pdf/) lets you **save a web page as a PDF** just by pasting its link. It works the same on an iPhone, an Android phone or a computer, because the page is rendered on our server rather than by your phone's browser. This guide explains how to use it, what to expect from the result, and the built-in browser method for the cases where it fits better.

## How to convert a URL to PDF

1. Copy the address of the page you want. On a phone, use the Share button in your browser and choose **Copy**.
2. Open the [URL to PDF converter](/url-to-pdf/) and paste the link into the box. You can leave out *https://*; it is added for you.
3. Choose a page size: **A4** (standard in Pakistan, the UK, Europe and most of the world) or **US Letter**.
4. Tick **Landscape** for wide pages such as tables, dashboards and timelines. Leave it unticked for articles.
5. Press **Convert to PDF** and wait a few seconds while the page is opened and printed.
6. Download the PDF. It is named after the website, for example *www.example.com.pdf*.

## What happens behind the scenes

Here is how this tool differs from most DoraPDF tools: it needs a server. Your phone cannot "print" a page it has not opened, so the converter sends the **URL** to our server, where a real browser:

- opens the page,
- waits until it has finished loading (up to about 30 seconds),
- prints it to PDF with **background colours and images included**, on the paper size you chose,
- and sends the PDF back to you.

Only the web address is sent, not any file from your device. To keep things fast, a PDF of the same address with the same settings may be served from a short-term cache for up to 30 minutes. If you are capturing a page that changes minute by minute, keep that in mind.

## What the PDF will (and will not) look like

The result is what a fresh, logged-out visitor would see if they printed the page.

**Usually works well:**

- News articles, blog posts and documentation
- Public product pages and listings
- Recipes, guides and tutorials
- Public government and university pages

**Will not work as you might hope:**

- **Pages behind a login.** Your email, bank account, student portal or social media feed need your account, and the server does not have it. You will get the login page instead.
- **Paywalled articles.** You will get whatever a non-subscriber sees.
- **Local or private addresses** such as *localhost*, *192.168...* or office intranet pages. These are blocked for security and cannot be reached from the internet anyway.
- **Very heavy, app-like pages** that never finish loading, or that build their content only after you scroll or click.

Some sites also show cookie banners or newsletter pop-ups, and those can appear in the PDF because the server is a first-time visitor.

## The browser method: best for pages behind a login

For anything you are logged in to, use your own browser's print function. It prints exactly what you see, using your session:

- **Chrome, Edge or Firefox on a computer:** press **Ctrl + P** (or **Cmd + P** on Mac), set the destination to **Save as PDF**, and press Save.
- **Chrome on Android:** open the three-dot menu, choose **Share**, then **Print**, and select **Save as PDF**.
- **Safari on iPhone:** tap **Share**, then **Options** near the top of the share sheet, choose **PDF**, and save it to Files.

Menu names shift a little between versions, but these paths have been stable for a while.

## Which method should you use?

- **Public page, want a clean A4 or Letter PDF, on any device:** [URL to PDF](/url-to-pdf/).
- **You are logged in, or the page needs your clicks to show content:** your browser's print function.
- **You want a picture of the page as it looks on screen, not a printed layout:** the [Website Screenshot tool](/web-to-png/), which captures a full-page PNG at desktop, laptop, tablet or phone width.

## Common problems and fixes

**"Enter a valid public web address."** Check that you pasted the full link with a proper domain (like *example.com*). Short internal names and local addresses are not accepted.

**The PDF shows a login or "subscribe" page.** The page requires an account. Use the browser print method above.

**The layout looks different from my screen.** Many sites use special print styles that hide menus and ads. That is usually a good thing for reading. If you need the on-screen look, take a [full-page screenshot](/web-to-png/) instead.

**A wide table is cut off.** Tick **Landscape** and convert again.

**It timed out.** Some sites are slow or block automated visitors. Try again in a minute, or use your browser's print option.

## Privacy

Because this converter uses our server, the **web address** you enter is sent to it so the page can be opened. Do not paste private links that contain secret tokens (such as password-reset or one-time sharing links). Your own files are never involved, and the PDF is sent straight back to you. Most other DoraPDF tools, such as the merger and compressor, run entirely in your browser.

## After you have the PDF

- Combine several saved pages into one research file with the [PDF Merger](/pdf-merger/).
- Highlight key passages with [Highlight PDF](/highlight-pdf/).
- Pull out just the text with [PDF to TXT](/pdf-to-txt/) for your notes.

## FAQ

**Can I save a web page as PDF on my iPhone?**
Yes. Paste the link into the [URL to PDF converter](/url-to-pdf/) in Safari, or use Share, then Options, then PDF for pages you are logged in to.

**Does it save the full page or just the visible part?**
The full page, split across as many A4 or Letter pages as needed.

**Are images and colours included?**
Yes. Backgrounds and images are printed, as long as they finished loading.

**Is it free?**
Yes, with no account and no watermark.
"""),
dict(slug='length-converter-cm-inches-feet-meters-miles-km', title='Length Conversion Made Easy: cm, m, Inches, Feet, Miles and Km (Formulas and Free Converters)', date='2026-11-12',
 desc='Convert cm to inches, feet to cm, miles to km and more with free two-way converters. Exact formulas, worked examples and a height conversion trick.',
 tools=['inch-to-cm', 'feet-to-cm', 'miles-to-km', 'km-to-miles', 'cm-to-m', 'feet-to-meter'], md="""
Length units cause small, annoying problems all the time. A doctor's form wants your height in centimetres but you know it in feet. A furniture listing gives a table in inches. A running app says 10 km and your friend asks "how many miles is that?" A school worksheet mixes millimetres and inches on purpose.

DoraPDF has a set of free, two-way length converters for the conversions people search for most. This guide lists them, gives the exact formula behind each one so you can check the answer yourself, and walks through the examples that trip people up, like converting a height of 5 feet 7 inches.

## The converters

Each tool has two boxes. Type in **either** box and the other updates instantly, so every converter also works in reverse. Below the boxes there is a **quick table** for 1, 2, 5, 10, 20, 50, 100, 500 and 1,000 units, handy for printing or for a quick glance.

| Conversion | Tool | Exact factor |
| --- | --- | --- |
| Inches to centimetres | [Inch to CM](/inch-to-cm/) | 1 in = 2.54 cm |
| Inches to millimetres | [Inch to MM](/inch-to-mm/) | 1 in = 25.4 mm |
| Inches to feet | [Inches to Feet](/inches-to-feet/) | 12 in = 1 ft |
| Feet to inches | [Foot to Inch](/foot-to-inch/) | 1 ft = 12 in |
| Feet to centimetres | [Feet to CM](/feet-to-cm/) | 1 ft = 30.48 cm |
| Feet to metres | [Feet to Meter](/feet-to-meter/) | 1 ft = 0.3048 m |
| Feet to miles | [Feet to Miles](/feet-to-miles/) | 5,280 ft = 1 mile |
| Centimetres to metres | [CM to M](/cm-to-m/) | 100 cm = 1 m |
| Metres to inches | [Meter to Inch](/meter-to-inch/) | 1 m ≈ 39.3701 in |
| Metres to miles | [Meters to Miles](/meters-to-miles/) | 1,609.344 m = 1 mile |
| Miles to kilometres | [Miles to Km](/miles-to-km/) | 1 mile = 1.609344 km |
| Kilometres to miles | [KM to Miles](/km-to-miles/) | 1 km ≈ 0.621371 miles |

Most of these factors are exact by definition. The inch has been defined as exactly 2.54 cm since 1959, and everything else in the imperial column (foot, mile) is built from the inch. That is why converters can give you so many decimal places with confidence.

## How to use them

1. Open the converter you need, for example [Inch to CM](/inch-to-cm/).
2. Type your number in the first box. The answer appears in the second box as you type.
3. To go the other way, type in the second box instead.
4. Use the quick table if you need several common values at once.

Results show up to six decimal places. For everyday use, round to one or two.

## Worked examples

### Height: 5 feet 7 inches in cm

Heights are the most common reason people search **feet to cm**, and they are written in two units at once, so do it in two steps:

1. Turn the feet into inches: 5 ft x 12 = 60 in. Add the extra inches: 60 + 7 = **67 inches**. (The [Foot to Inch](/foot-to-inch/) converter does the first part.)
2. Convert inches to centimetres: 67 x 2.54 = **170.18 cm**. Use [Inch to CM](/inch-to-cm/).

Going the other way, 170 cm divided by 2.54 is about 66.93 inches, which is 5 feet and about 6.9 inches. Most people would say 5 ft 7 in.

A shortcut for whole feet: [Feet to CM](/feet-to-cm/) gives 6 ft = 182.88 cm directly.

### Running distances: km to miles

- **5 km** is about **3.11 miles**.
- **10 km** is about **6.21 miles**.
- A **half marathon (21.0975 km)** is about **13.11 miles**.
- A **marathon (42.195 km)** is about **26.22 miles**.

Use [KM to Miles](/km-to-miles/), or [Miles to Km](/miles-to-km/) if your app shows miles: 5 miles is 8.05 km.

### Screens and furniture: inches to cm and mm

- A table listed as 32 inches deep is 81.28 cm, or 2.67 feet.
- A 6-inch ruler is 152.4 mm long.
- A screen size is measured diagonally, so a "55-inch" TV is 139.7 cm corner to corner, not wide.

### Rooms and buildings: feet and metres

- 100 metres is about **328.08 feet**.
- A 12 ft x 10 ft room is roughly 3.66 m x 3.05 m.
- 1,500 feet is about 0.284 miles, a little over a quarter of a mile.

## Mental-math shortcuts (for when you have no phone)

These are approximations, good enough for a quick estimate:

- **Inches to cm:** multiply by 2.5. (10 in is about 25 cm; exact: 25.4.)
- **Feet to metres:** divide by 3.3. (33 ft is about 10 m.)
- **Km to miles:** multiply by 0.6. (10 km is about 6 miles; exact: 6.21.)
- **Miles to km:** multiply by 1.6. (5 miles is about 8 km.)
- **Metres to feet:** multiply by 3.3. (2 m is about 6.6 ft.)

For homework, forms and anything official, use the exact factor or the converter rather than the shortcut.

## Common mistakes

**Mixing up feet-and-inches with decimals.** 5.7 feet is *not* 5 ft 7 in. 5.7 ft is 5 ft and 8.4 inches (0.7 x 12). Always convert the inches part separately.

**Forgetting area is different.** Converting 12 ft x 10 ft to metres means converting each side, then multiplying. You cannot convert "120 square feet" with the length factor; square units need the factor squared.

**Rounding too early.** Round only at the end. Rounding 2.54 to 2.5 in the middle of a long calculation adds up quickly.

## Privacy

These converters are simple calculations that run in your browser. Nothing you type is sent anywhere.

## More converters and calculators

- [Lbs to KG](/lbs-to-kg/) and [Ounces to Grams](/ounces-to-grams/) for weight.
- [Celsius to Fahrenheit](/celsius-to-fahrenheit/) for temperature.
- [BMI Calculator](/bmi-calculator/), which takes your height and weight.
- [Percentage Calculator](/percentage-calculator/) for marks, discounts and changes.

## FAQ

**How many cm are in an inch?**
Exactly 2.54 cm. Use the [Inch to CM converter](/inch-to-cm/) for any amount.

**How many feet are in a mile?**
5,280 feet. The [Feet to Miles](/feet-to-miles/) tool converts both ways.

**Is a km longer than a mile?**
No. A mile is longer: 1 mile is about 1.61 km, and 1 km is about 0.62 miles.

**How do I convert my height from feet to cm?**
Convert the feet to inches (x 12), add the remaining inches, then multiply by 2.54. For example, 5 ft 7 in = 67 in = 170.18 cm.

**Do the converters work offline?**
Once the page has loaded, the calculations happen on your device, so they keep working even if your connection drops.
"""),
dict(slug='how-to-convert-picture-to-pdf-on-iphone', title='How to Convert a Picture to PDF on iPhone (Free, No App)', date='2026-11-11',
 desc='Turn iPhone photos, screenshots and HEIC pictures into one PDF right in Safari. No app to install, no sign-up, and your photos stay on your phone.',
 tools=['images-to-pdf', 'heic-to-pdf', 'pdf-compressor'], md="""
A college form wants your CNIC copy "as a PDF". A teacher asks for homework pages in one file. A landlord wants the signed agreement back today. If you are holding an iPhone, all you have is a set of photos, and the upload box keeps saying *PDF only*.

You can **convert a picture to PDF on iPhone** without installing anything. Open DoraPDF's free [Images to PDF Converter](/images-to-pdf/) in Safari, pick your photos, and download a single PDF. The conversion runs inside the browser on your phone, so the pictures are not sent to a server.

## What you need

- An iPhone (or iPad) with Safari, Chrome or any modern browser
- The photos in your Photos app, or image files saved in the Files app
- About a minute

No account, no watermark and no app from the App Store.

## Step by step: picture to PDF on iPhone

1. Open **dorapdf.com/images-to-pdf** in Safari.
2. Tap the upload area. iOS shows a menu: **Photo Library**, **Take Photo** or **Choose File**.
3. Choose **Photo Library** and select one or more pictures. Tap **Add**.
4. Check the list. Each picture becomes one page, **in the order shown**. If one is in the wrong place or you added it by mistake, tap the **✕** next to it and add it again at the end.
5. Pick a **Page size**: *Fit page to image*, *A4 page* or *US Letter*.
6. Pick a **Margin**: no margin, small (the default) or big.
7. Tap **Create PDF**, then **Download**.

Safari will ask whether you want to download the file. Tap **Download**, and the PDF is saved in the **Files** app, usually under *Downloads* (iCloud Drive or On My iPhone, depending on your settings). From there you can share it to WhatsApp, Mail or a website upload form.

## Which page size should you choose?

This one setting decides how the PDF looks when someone opens or prints it.

| Page size | What happens | Good for |
|---|---|---|
| Fit page to image | Each page is exactly the shape of its photo | Screenshots, receipts, long chat captures |
| A4 page | Photo is centred on a standard A4 sheet | Documents that will be printed, office or university submissions |
| US Letter | Same, on a Letter sheet | Forms for US offices |

Landscape photos get landscape pages automatically, so a sideways photo of a whiteboard is not squeezed onto a tall page.

For anything that may be printed, such as an ID card copy or a filled form, **A4 with a small margin** is the safe choice. Printers usually cannot print right to the edge, and the margin keeps the edges of your document from being cut off.

## What about HEIC photos?

iPhones save photos in the **HEIC** format by default to save space. Many websites refuse HEIC files, which is one reason people get stuck.

The Images to PDF Converter accepts HEIC directly. When you pick photos from the library, iOS sometimes hands the browser a JPG copy and sometimes the original HEIC. Either way the tool reads it, so you do not need to convert anything first.

If your pictures are HEIC files saved in the Files app (for example, AirDropped from another iPhone), the dedicated [HEIC to PDF](/heic-to-pdf/) tool does the same job and only shows HEIC files in the picker, which makes them easier to find.

## Getting a clean PDF from phone photos

The PDF can only be as good as the picture. A few habits help a lot:

- **Shoot from straight above.** A document photographed at an angle looks slanted in the PDF.
- **Use daylight, not the flash.** The flash creates a bright glare spot right on the text.
- **Crop before you convert.** Open the photo in the Photos app, tap **Edit**, crop away the table and your fingers, then add it to the converter.
- **Rotate in Photos too.** If a picture appears sideways, fix it in the Photos editor first.
- **Put a dark surface under white paper.** The edges of the page stand out and look neater.

If you need proper document scans, try the [Scan to PDF](/scan-to-pdf/) tool instead. You drag the corners to crop and straighten each page and pick a scan filter. It is made for paper documents, while Images to PDF keeps your photos as they are.

## Common problems and fixes

**"The PDF is too big to upload."**
Pictures from recent iPhones are large. Images wider than 2400 pixels are scaled down during conversion, which already helps, but ten photos can still add up. Run the finished file through the [PDF Compressor](/pdf-compressor/) to bring it under the size limit of the portal or email.

**"The pages are in the wrong order."**
The PDF follows the list exactly. Remove the misplaced picture with ✕ and add it again, or select your photos one at a time in the order you want.

**"I can't find the downloaded PDF."**
Open the **Files** app, tap **Browse**, then **Downloads**. You can also tap the download icon in Safari's address bar to see recent downloads.

**"A transparent PNG got a white background."**
That is expected. PDF pages are white, so transparent areas are filled with white.

## Is it private?

Yes. The photos are read and turned into a PDF by your browser on your phone. They are not uploaded to DoraPDF's servers, which matters when the picture is an ID card, a bank slip or a medical report. Once the page has loaded, the conversion itself does not need to send your files anywhere.

## FAQ

**Can I convert multiple pictures into one PDF on iPhone?**
Yes. Select several photos at once, or add more in a second round. All of them go into one PDF, one picture per page.

**Do I need to install an app?**
No. Everything works in Safari or any other browser on your iPhone.

**Is there a watermark?**
No. The PDF contains only your pictures.

**Does it work on iPad and Android too?**
Yes. The same page works on iPad, Android phones, Windows and Mac.

**Will the quality drop?**
Photos are saved as high-quality JPEG inside the PDF and very large ones are limited to 2400 pixels wide. Text in a document photo stays sharp and readable at that size.

## Related tools

- [HEIC to PDF](/heic-to-pdf/) for iPhone HEIC files saved in Files
- [Scan to PDF](/scan-to-pdf/) for cleaner scans of paper documents
- [PDF Compressor](/pdf-compressor/) when the finished PDF is over an upload limit
"""),
dict(slug='convert-word-to-pdf-online-free', title='Convert Word to PDF Online Free (and How to Keep Your Layout Intact)', date='2026-11-11',
 desc='Convert Word to PDF online free in your browser. See what the converter keeps, what changes, and which method to use when fonts and layout must match exactly.',
 tools=['word-to-pdf', 'pdf-compressor', 'protect-pdf'], md="""
Most people who search **convert Word to PDF online free** want one of two things. Either they need a PDF *right now* on a computer or phone that does not have Microsoft Word, or they need a PDF that looks *exactly* like their Word file, down to the last font. These are different jobs, and the best tool depends on which one you have.

This guide shows how to use DoraPDF's free [Word to PDF Converter](/word-to-pdf/), what it keeps from your document, what it changes, and what to do when the layout has to be pixel-perfect.

## The quick method: Word to PDF in your browser

1. Open the [Word to PDF Converter](/word-to-pdf/).
2. Drop your **.docx** file onto the page, or click to choose it.
3. Press **Convert now**.
4. Press **Download**. The PDF has the same name as your Word file.

There is no sign-up and no watermark, and the conversion runs inside your browser. Your document is not uploaded to a server, which is a good thing when it is a CV with your phone number or an office letter.

**Only .docx is accepted.** If your file ends in **.doc** (the old Word 97-2003 format), open it in Word, LibreOffice or Google Docs and save it as .docx first.

## What the converter keeps

The tool reads the content and structure of your document and lays it out on **A4 pages** with comfortable margins. These come through well:

- Headings and paragraphs
- Bold and italic text
- Bulleted and numbered lists
- Tables (drawn with simple borders)
- Pictures placed in the document

For letters, assignments, notes, simple reports and applications, the result is a clean, readable PDF.

## What changes (read this before sending a CV)

Being honest about the limits saves you an awkward moment later:

- **Fonts are standardised.** The text is set in a clean serif font, not the exact font you picked in Word.
- **Page breaks are recalculated.** A new page starts when an A4 page fills up, not where your Word file had a manual page break. Glance at the bottom of each page before you send it.
- **Headers, footers, page numbers, text boxes and multi-column layouts** are not reproduced the way Word draws them.
- **The pages are stored as images.** The PDF looks right, but you cannot select or search the text in it.

If your document is a designed CV, a thesis with strict formatting rules, or anything where a reviewer will check fonts and margins, use one of the methods below instead.

## How to keep fonts and layout exactly

When the layout must match your Word file perfectly, the program that made the file is the best converter, because it knows exactly how it drew every page.

**Microsoft Word (Windows or Mac):** File → Save As (or Save a Copy) → choose **PDF** as the file type → Save.

**Word on a phone:** open the document, tap the three-dot menu, then **Save as** or **Export** and choose PDF. The exact menu names vary between versions.

**Google Docs:** upload the .docx to Google Drive, open it with Google Docs, then File → Download → **PDF document**. Fonts that Google Docs does not have may be swapped for similar ones.

**LibreOffice (free, Windows/Mac/Linux):** File → Export as PDF.

So the rule of thumb is simple. No Word on this device and you need a clean PDF fast? Use the online converter. Strict formatting? Export from Word or Docs.

## Practical examples

**Sending an application from a cyber cafe or office PC without Word.** Download the .docx from your email, convert it in the browser, and attach the PDF. Nothing is installed and nothing is left on someone else's server.

**Submitting homework on a portal that only accepts PDF.** Most assignments are headings, paragraphs and maybe a table. The converter handles these well. If the portal has a size limit and your document has many pictures, shrink the result with the [PDF Compressor](/pdf-compressor/).

**Sharing a contract draft that should not be edited.** A PDF is harder to change by accident than a Word file. If it is confidential, add a password with [Protect PDF](/protect-pdf/) before you email it.

## Common problems and fixes

**"The file is not accepted."**
Check the extension. Only .docx works. Re-save .doc, .odt or .rtf files as .docx (or use the [ODF to PDF](/odf-to-pdf/) tool for .odt files).

**"My picture is missing."**
Images inserted normally into the document come through. Shapes, SmartArt and charts drawn by Word itself may not. Insert them as a picture (copy, then Paste Special → Picture in Word) and convert again.

**"A table looks plainer than in Word."**
Tables get simple grey borders. The content and rows are kept, but colour shading and custom borders are not.

**"I need to copy text from the PDF later."**
Because the pages are stored as images, copying will not work. Keep your .docx as the editable original, or export from Word if the recipient needs selectable text.

## Privacy

The .docx is opened and converted by your own browser. It does not travel to DoraPDF's servers, and the PDF is created on your device. Close the tab and nothing remains online.

## FAQ

**Is this Word to PDF converter really free?**
Yes. No account, no limit on how often you use it and no watermark.

**Can I convert Word to PDF on my phone?**
Yes. The page works in mobile browsers on Android and iPhone. Pick the .docx from your Files or Downloads.

**Does it keep my fonts?**
No. Text is set in a standard serif font. For exact fonts, save as PDF from Word, Google Docs or LibreOffice.

**Can I convert several Word files at once?**
The converter takes one file at a time. Convert each one, then join the PDFs with the [PDF Merger](/pdf-merger/) if you need a single file.

## Related tools

- [PDF Compressor](/pdf-compressor/) to meet email and portal size limits
- [Protect PDF](/protect-pdf/) to lock a document with a password
- [PDF Merger](/pdf-merger/) to join several converted files into one
"""),
dict(slug='convert-pdf-to-editable-word-document', title='How to Convert a PDF to a Word Document You Can Actually Edit', date='2026-11-11',
 desc='Convert PDF to Word online free and get text you can edit. Learn which layout mode to pick, how to handle scanned PDFs with OCR, and how to edit the result.',
 tools=['pdf-to-word', 'pdf-ocr', 'pdf-to-txt'], md="""
Converting a PDF is the easy part. The real question is what happens when you open the Word file and start typing. Does the text move around? Can you change a date in a letter, fix a name in a certificate template, or reuse three pages of a report in your own document?

This guide is about getting a **PDF to Word document you can edit**, not just a file with a .docx ending. It covers the two conversion modes in DoraPDF's free [PDF to Word Converter](/pdf-to-word/), how to deal with scanned PDFs, and how to work with the result in Word.

## Convert PDF to Word in four steps

1. Open the [PDF to Word Converter](/pdf-to-word/).
2. Drop in your PDF.
3. Choose the **Layout**: *Keep original layout (recommended)* or *Text only (simple, flowing)*.
4. Press **Convert now**, then **Download** the .docx.

It runs in your browser, so it works the same on Windows, Mac, Android and iPhone, and your PDF is not uploaded anywhere.

The choice in step 3 matters more than anything else, so here is what each mode actually gives you.

## Mode 1: Keep original layout

This mode tries to make the Word page look like the PDF page. Behind the scenes it does something clever:

- Each page is drawn as a **background picture**, with the original text cleaned out of it.
- The text is then placed back **on top as real, editable Word text**, line by line, in the same position.
- Font style (a similar font family, bold, italic), size and text colour are carried over.

**Best for:** small edits where the look must stay the same. Changing a date or amount on a letter, correcting a name, updating a phone number on a flyer, filling gaps in a form.

**What to expect when you edit:** every line sits in its own small text frame. You can click into a line and change words freely. If you add a lot of extra text to one line, it will not push the next line down the way normal Word paragraphs do, because each line is positioned on its own. Logos, photos, lines and boxes are part of the background picture, so you can see them but not move them separately. Rotated or vertical text also stays in the picture.

## Mode 2: Text only

This mode ignores the design and gives you the words as normal, flowing Word paragraphs. Lines that are larger than the body text become bold headings, and each PDF page starts on a new page in Word.

**Best for:** reusing content. Quoting a section in your assignment, rewriting a policy, editing a long report, or pasting the text into another template. Paragraphs reflow normally, so you can add, delete and restyle as much as you like.

**Quick rule:** *small change, same look* → Keep original layout. *Big rewrite or reuse* → Text only.

## What if the PDF is scanned?

A scanned PDF is just photos of pages. There is no text inside, only pixels shaped like letters. If you convert one in text-only mode, the tool stops and tells you: *No text found — this PDF looks scanned (image only).*

The fix is **OCR** (optical character recognition), which reads the letters from the image:

1. Open the [PDF OCR Converter](/pdf-ocr/).
2. Choose the document's **Language**. English, Urdu, Arabic, Hindi, French, Spanish, Turkish, Chinese (Simplified) and several others are available.
3. Press **Run OCR**. Expect roughly 5–15 seconds per page; the first run also downloads the language model once.
4. You get two files: a **searchable PDF** and a plain **.txt** file with all the recognised text.

Now take the searchable PDF to the PDF to Word Converter and use **Text only** mode. That gives you clean, editable paragraphs. If you only need the words, the .txt file from the OCR step may already be enough. Paste it into Word and format it yourself.

The OCR tool handles up to 60 pages per run. For a longer scan, split it first with the [PDF Splitter](/pdf-splitter/) and process it in parts.

## Tips for editing the converted file

- **Turn on "Show/Hide ¶"** (the paragraph mark button on Word's Home tab) to see where lines and frames begin and end.
- **In layout mode, edit inside the existing line** rather than pressing Enter for new lines. If you need a whole new paragraph, add it in a text box.
- **Fonts may be substituted.** If the PDF used a font you do not have installed, Word shows a similar one. For a perfect match, install the font or choose a close one for the whole document.
- **Save a copy as PDF again** when you are done: in Word, File → Save As → PDF.
- **Check numbers carefully** after any OCR step. A smudged "8" can be read as "3", and an "O" can become a "0".

## Common problems and fixes

**The Word file opens but some text is not editable.**
That text was rotated, part of an image, or a logo. It stays in the background picture. Retype it in a text box if you need to change it.

**Lines overlap after I edit them.**
You typed more than the line's frame could hold. Shorten the text or reduce the font size slightly for that line.

**Columns came out in the wrong reading order in text-only mode.**
Two-column layouts are read across rows, so the left and right columns can get mixed. Use layout mode, or copy column by column.

**The PDF is password protected.**
If you know the password, remove it first with [Unlock PDF](/unlock-pdf/), then convert.

## Privacy

Both the PDF to Word Converter and the OCR tool process files **inside your browser**. The pages are not uploaded to DoraPDF's servers, which makes them a reasonable choice for contracts, salary slips and student records.

## FAQ

**Can I convert PDF to Word for free without signing up?**
Yes. There is no account, no watermark and no daily limit.

**Which mode keeps tables?**
Layout mode keeps tables looking right because the lines and borders are in the background picture, and the cell text sits on top as editable text. Text-only mode keeps the words but not the table grid.

**Why can't I edit a scanned PDF after converting?**
Because it has no text layer. Run OCR first, then convert the searchable PDF.

**Does it work on a phone?**
Yes. The converted .docx opens in the Word app or Google Docs on Android and iPhone.

## Related tools

- [PDF OCR Converter](/pdf-ocr/) to make scanned pages readable
- [PDF to Text](/pdf-to-txt/) when you only need the words
- [Word to PDF Converter](/word-to-pdf/) to go back to PDF after editing
"""),
dict(slug='merge-pdf-online-free-right-order', title='Merge PDF Online Free: Combine PDF Files in the Right Order', date='2026-11-11',
 desc='Merge PDF online free and get the pages in the right order the first time. Simple ordering tricks, fixing sideways pages, and keeping the merged file small.',
 tools=['pdf-merger', 'rotate-pdf', 'delete-pdf-pages'], md="""
Joining PDFs takes seconds. Getting them in the right order is where people lose time: the cover letter ends up after the transcripts, the signed page lands in the middle, and you only notice after you have sent it.

This guide shows how to **merge PDF online free** with DoraPDF's [PDF Merger](/pdf-merger/) and, more importantly, how to plan the order so the combined file comes out right on the first try. It also covers what to do about sideways pages, extra pages and file size.

## How the PDF Merger decides the order

The rule is simple: **files are merged in the order they appear in the list**, top to bottom. Every page of the first file comes first, then every page of the second, and so on.

Files get into the list in the order you add them. If you select several at once in the file picker, they appear in the order your device hands them over, which is often alphabetical on a computer. If you add files in several rounds, each new batch is added below the existing ones.

That gives you two reliable ways to control the order.

## Method 1: Add files one at a time

1. Open the [PDF Merger](/pdf-merger/).
2. Add the file that should be **first**.
3. Add the second file, then the third, and so on.
4. Check the list. If something is out of place, remove it with the **✕** button and add it again; it goes to the bottom.
5. Press **Merge PDFs**, then **Download** `merged.pdf`.

This is the safest method on a phone, where the picker's order is harder to predict.

## Method 2: Number your files first

When you have many files, rename them before merging:

- `01-cover-letter.pdf`
- `02-cv.pdf`
- `03-degree.pdf`
- `04-transcript.pdf`
- `05-cnic.pdf`

Use **two digits** (01, 02 … 10) so that "10" does not sort before "2". Then select all of them at once. On most computers they will land in the list in exactly this order. Always glance at the list before pressing Merge anyway.

## A practical order for common bundles

**Job application:** cover letter → CV → degree → transcripts → experience letters → ID copy.

**University admission:** application form → photographs page → matric/O-level → intermediate/A-level → bachelor's → domicile and ID → fee challan.

**Office claim or reimbursement:** claim form → summary sheet → receipts in date order.

**Assignment submission:** title page → main work → appendix → references, unless your teacher asks for something different.

Putting the document the reader needs first at the top saves the reviewer from scrolling, and that small courtesy is often noticed.

## Before you merge: fix the pieces

Merging copies pages as they are. If a piece has a problem, the merged file will have it too. Fixing it before or after is quick:

- **Sideways or upside-down pages:** use [Rotate PDF](/rotate-pdf/). You can rotate all pages or only selected ones, such as `3` or `1-3, 5`.
- **Blank or duplicate pages:** use [Delete PDF Pages](/delete-pdf-pages/) and enter the pages to remove, like `2, 4-6`.
- **Only part of a file is needed:** use the [PDF Splitter](/pdf-splitter/) to extract just those pages into a new PDF, then merge that.
- **Photos instead of PDFs:** turn them into a PDF with [Images to PDF](/images-to-pdf/) first, then add the result to the merger.

You can also do these fixes on `merged.pdf` afterwards. Page numbers then refer to the combined file.

## Keeping the merged PDF small

Merging does not compress or re-encode pages, so quality stays exactly as it was. That also means the merged file is roughly the size of all the parts added together. A few scanned documents can quickly go past an email or portal limit of a few megabytes.

If that happens, run `merged.pdf` through the [PDF Compressor](/pdf-compressor/). Its *Smart* mode keeps text selectable, while *Strong* mode turns pages into images for the smallest size.

## Common problems and fixes

**"Add at least 2 PDF files."**
The merger needs two or more PDFs. If you have only one, there is nothing to merge.

**One of my files is password protected.**
The merger tries to open it anyway. If pages come out blank or the file will not load, remove the password with [Unlock PDF](/unlock-pdf/) (you need to know the password) and try again.

**The order is wrong after merging.**
Do not start over from scratch. Use the splitter to pull out the misplaced pages and merge again, or simply rebuild the list using Method 1.

**The merged file name is generic.**
It always downloads as `merged.pdf`. Rename it to something clear, like `Ali-Khan-Application.pdf`, before you send it.

## Privacy

Your PDFs are combined **inside your browser**. They are not uploaded to a server, so you can safely merge documents like bank statements, ID copies and medical reports.

## FAQ

**How many PDFs can I merge at once?**
There is no fixed file limit in the tool. Very large bundles depend on your device's memory, so a phone may struggle with dozens of big scanned files where a laptop will not.

**Can I merge PDFs on my phone?**
Yes. It works in Chrome, Safari and other mobile browsers. Add files one at a time to control the order.

**Will merging reduce quality?**
No. Pages are copied as they are, without re-compressing.

**Is there a watermark?**
No.

## Related tools

- [Rotate PDF](/rotate-pdf/) to fix sideways pages
- [Delete PDF Pages](/delete-pdf-pages/) to remove blanks and duplicates
- [PDF Compressor](/pdf-compressor/) if the merged file is too big to send
"""),
dict(slug='how-to-convert-jpg-to-pdf-free', title='How to Convert JPG to PDF Free (Multiple Images Into One PDF)', date='2026-11-11',
 desc='Convert JPG to PDF free on Windows, Mac or Android and combine multiple images into one PDF. Choose page size and margins, set the order, keep the file small.',
 tools=['images-to-pdf', 'image-resizer', 'pdf-compressor'], md="""
You have a folder of JPG files: six pages of handwritten notes, a stack of receipts, or photos of a signed form. Whoever asked for them wants **one PDF**, not six attachments. Here is how to **convert JPG to PDF free**, put many images into a single file in the right order, and choose settings that make the PDF look tidy on screen and on paper.

The tool for this is DoraPDF's [Images to PDF Converter](/images-to-pdf/). It runs in your browser on Windows, Mac, Linux, Android and iPhone, and it does not upload your images to a server.

## How to convert JPG to PDF (the short version)

1. Open the [Images to PDF Converter](/images-to-pdf/).
2. Drag your JPG files onto the page, or click and select them. Hold **Ctrl** (Windows) or **Cmd** (Mac) to pick several at once.
3. Check the order in the list; **each image becomes one page, top to bottom**.
4. Choose **Page size** and **Margin**.
5. Click **Create PDF**, then **Download**.

With one image, the PDF is named after that image. With several, it downloads as `images.pdf`.

PNG and WebP files work too, and so do iPhone HEIC photos, so you can mix formats in one PDF.

## Getting the page order right

The PDF follows the list exactly, so a minute spent on the order saves a re-do.

- **Add images in batches.** New files are always added to the bottom of the list. Add page 1 first, then page 2, and so on.
- **Remove and re-add to move a page.** Click **✕** next to a misplaced image and add it again; it goes to the end.
- **Rename before selecting.** Files named `page-01.jpg`, `page-02.jpg` … usually arrive in that order when you select them all together on a computer. Use two digits so `page-10` does not jump ahead of `page-2`.

Phone cameras name photos by time (like `IMG_20261111_093012.jpg`), so photos taken in sequence are usually already in the right order on a computer.

## Page size and margin: which settings to use

The converter gives three page sizes and three margins. Here is how they combine in practice:

| You are making… | Page size | Margin |
|---|---|---|
| A document to print or submit (forms, notes, ID copies) | A4 page | Small |
| A file for US offices or US printers | US Letter | Small |
| A photo album or portfolio to view on screen | Fit page to image | No margin |
| Receipts for a claim | A4 page | Small or Big |
| Scanned artwork you want framed with white space | Fit page to image | Big |

**A4 and US Letter** put each image in the centre of a standard sheet and scale it to fit, keeping its proportions. Landscape pictures get landscape pages. **Fit page to image** makes each page exactly the shape of the picture, which looks best on screens.

Margins matter for printing. Most office printers cannot print right to the edge, so with "No margin" on an A4 page the outer few millimetres may be cut off.

## How to keep the PDF small

A PDF of photos is roughly as heavy as the photos inside it. A few habits keep it within email and upload limits:

1. **Large images are already limited.** Anything wider than 2400 pixels is scaled down during conversion, which is still sharp enough to read and print documents.
2. **Resize first for very small targets.** If a portal wants the whole PDF under 1 MB, shrink your images to around 1200–1600 pixels wide with the [Image Resizer](/image-resizer/) before converting.
3. **Compress afterwards.** Run the finished PDF through the [PDF Compressor](/pdf-compressor/) and pick a stronger level if needed.
4. **Crop out the background.** A photo of a page on a big table carries a lot of pixels that are not your document. Crop in your phone's gallery or photo app first.

## Real examples

**Notes for a study group.** Photograph each page of your notebook, convert to A4 with a small margin, and share one PDF in the group chat. Everyone can scroll through it like a book.

**Expense claim.** Snap each receipt, convert in date order, and attach a single PDF to the claim form instead of a dozen pictures.

**Portfolio for a client.** Choose *Fit page to image* with no margin, so each design or photo fills the page edge to edge.

**Documents for an admission form.** Convert your certificates in the order the form lists them. If the form wants separate files, convert each certificate on its own instead.

## Common problems and fixes

**A page appears sideways.**
The converter uses each image as it is stored. Rotate the photo in your gallery or with the [Image Flipper](/image-flipper/) first, then convert. If the PDF is already made, [Rotate PDF](/rotate-pdf/) fixes individual pages.

**Transparent parts turned white.**
PDF pages are white, so transparency in PNG images is filled with white.

**The PDF is blurry when zoomed in a lot.**
The source image might be small or compressed. Use the original photo from the camera rather than one sent through a chat app, which often shrinks images.

**My phone added the photos in a strange order.**
Add them one by one, or convert in smaller groups and join the PDFs later with the [PDF Merger](/pdf-merger/).

## Privacy

The JPG files never leave your device. The browser reads them, builds the PDF and hands you the download. That makes it safe for ID cards, bank documents and anything else you would not want sitting on a stranger's server.

## FAQ

**How do I combine multiple JPG files into one PDF?**
Add all the images to the Images to PDF Converter. Every image becomes a page in the same PDF, in the order of the list.

**Is it free and without watermark?**
Yes to both. There is also no sign-up.

**Can I convert JPG to PDF on Android?**
Yes. Open the page in Chrome, tap the upload area and choose images from your gallery or files.

**Is there a limit on the number of images?**
There is no fixed limit. Very large batches depend on your device's memory, so on a phone it is wise to convert in groups of 20–30 photos.

## Related tools

- [Image Resizer](/image-resizer/) to shrink photos before converting
- [PDF Compressor](/pdf-compressor/) to reduce the finished PDF
- [PDF Merger](/pdf-merger/) to join PDFs made in separate batches
"""),
dict(slug='compress-jpeg-online-without-losing-quality', title='Compress JPEG Online Without Losing Quality (and Hit 100 KB or 200 KB Limits)', date='2026-11-11',
 desc='Compress JPEG online free and make photos small enough for forms, email and websites. Which strength and size to pick, and how to get under 100 KB.',
 tools=['image-compressor', 'image-resizer', 'png-to-jpg'], md="""
An online form rejects your photo because it is "larger than 200 KB". A website feels slow because every product picture weighs 4 MB. WhatsApp is fine, but email bounces your attachments. All of these have the same fix: **compress the JPEG**.

DoraPDF's free [Image Compressor](/image-compressor/) does it in your browser, many photos at once, without uploading them anywhere. This guide explains its settings in plain words and gives a simple routine for hitting strict size limits like 100 KB, without turning your photo into a blurry mess.

## Why JPEG files are bigger than they need to be

A modern phone photo is often 4000 pixels wide or more, saved at a very high quality setting. That detail is useful if you plan to print a poster. For a form, a web page or a chat, it is mostly wasted weight.

Two things decide the size of a JPEG:

1. **Its dimensions** (width × height in pixels). Halving the width cuts the pixel count to a quarter.
2. **Its quality setting.** Lower quality throws away fine detail the eye barely notices.

The Image Compressor lets you control both, which is why it can shrink photos so much while they still look right on screen.

## How to compress a JPEG online

1. Open the [Image Compressor](/image-compressor/).
2. Drop in one photo or many.
3. Choose **Strength**: *Light*, *Balanced* (default) or *Strong*.
4. Choose **Resize**: *Original size*, *Max 2560px*, *Max 1920px* (default), *Max 1280px* or *Max 800px*.
5. Press **Compress** and download each result.

Every result shows its new size and **how many percent smaller** it is than the original, so you can see right away whether you are under the limit. Compressed files are named like `photo-small.jpg`.

Images are only shrunk if they are wider than the limit you choose; a small image is never enlarged.

## Which settings to choose

| What the photo is for | Strength | Resize |
|---|---|---|
| Keeping a lighter copy of your best photos | Light | Max 2560px |
| Website, blog or online store images | Balanced | Max 1920px or 1280px |
| Email attachments and documents | Balanced | Max 1280px |
| Strict forms (100–200 KB limits) | Balanced or Strong | Max 1280px or 800px |
| Profile pictures and thumbnails | Strong | Max 800px |

**"Without losing quality"** realistically means *without losing visible quality*. Every JPEG compression removes some data. At Light and Balanced, and at a sensible size for the screen it will be shown on, most people cannot tell the difference.

## How to compress a JPEG to 100 KB (or any limit)

The tool does not ask for a target size, but a quick routine gets you there in one or two tries:

1. **Start with Balanced and Max 1280px.** For a typical phone photo this already brings the file far down.
2. **Read the size shown next to the result.** Under the limit? Done.
3. **Still too big?** Switch Resize to **Max 800px** and compress the original again.
4. **Still too big?** Change Strength to **Strong**.

Always compress the **original** photo again with the new settings, rather than compressing the already-compressed copy a second time. Repeated compression adds visible blockiness.

**Forms that also specify pixel size** (for example a passport-style photo that must be a certain width and height) need one extra step: set the exact dimensions in the [Image Resizer](/image-resizer/) first, then compress.

## A note about PNG files

The compressor handles PNG images differently. To keep transparent backgrounds intact, PNGs are saved as **WebP**, a modern format that supports transparency and is much smaller than PNG.

WebP works on websites and in all current browsers, but some government and university forms only accept JPG. If you need a JPG, convert the PNG with [PNG to JPG](/png-to-jpg/) first (transparent areas become white), then compress the JPG.

## Tips for better-looking compressed photos

- **Crop first.** Cutting out the empty sky or the table around a document removes pixels you do not need, so you can use a gentler strength.
- **Start from the camera original.** Photos forwarded through chat apps are already compressed. Compressing them again looks worse than compressing the original.
- **Faces and text need more quality than landscapes.** If a document's small print becomes hard to read, go back to Balanced or a larger size.
- **Do a batch.** Drop all the product photos for your store at once with the same settings, so they look consistent.

## Common problems and fixes

**The photo looks blocky around edges and text.**
The strength is too high for the size. Use Balanced with a smaller Resize value instead of Strong at full size; a smaller, cleaner image usually looks better than a large, heavily compressed one.

**The file got only slightly smaller.**
It was probably already compressed or already small. Choose a smaller Resize value.

**The form says "invalid format".**
You may have uploaded a PNG that came out as WebP. Convert it to JPG first, as explained above.

## Privacy

The compression runs **inside your browser**. Your photos are not sent to a server, so family pictures, ID photos and unreleased product shots stay on your device.

## FAQ

**Is this JPEG compressor free?**
Yes, with no sign-up, no watermark and no limit on the number of photos.

**Can I compress many JPEGs at once?**
Yes. Add as many as you need; each gets its own download button.

**Does it work on a phone?**
Yes. Open it in your phone's browser and pick photos from the gallery.

**Will the compressed image keep its EXIF data (camera and location info)?**
The image is redrawn and saved again, so the result does not carry the original camera details. That is also a small privacy bonus when you share photos online.

## Related tools

- [Image Resizer](/image-resizer/) for exact pixel sizes
- [PNG to JPG](/png-to-jpg/) when a form only accepts JPG
- [Images to PDF](/images-to-pdf/) to put compressed photos into one document
"""),
dict(slug='sign-pdf-online-free-draw-or-type-signature', title='How to Sign a PDF Online Free: Draw or Type Your Signature', date='2026-11-11',
 desc='Sign a PDF online free without printing or scanning. Draw your signature with a finger or mouse, or type it, then place it on any page in your browser.',
 tools=['sign-pdf', 'pdf-editor', 'protect-pdf'], md="""
Printing a document, signing it with a pen, scanning it and emailing it back is a twenty-minute job when you have a printer, and impossible when you do not. For most everyday paperwork you can **sign a PDF online free** in a couple of minutes instead, straight from your phone or laptop.

DoraPDF's [Sign PDF](/sign-pdf/) tool lets you draw your signature with a finger, stylus or mouse, or type your name in a handwriting-style font, and stamps it onto the page you choose. Everything happens in your browser, so the document is not uploaded to a server.

## When a drawn signature is enough

A signature added this way is a picture of your signature placed on the page. That is what most people mean by "sign and send back", and it is commonly accepted for:

- Rental and tenancy forms
- Consent and permission slips for school
- Internship, offer and joining letters
- Delivery notes, invoices and simple agreements between businesses
- Internal office approvals

It is **not** a certificate-based digital signature of the kind some banks, courts and government bodies require, which uses an identity certificate to prove who signed. If a document says it needs a "digital signature certificate" or a specific e-signing platform, follow that instruction. When in doubt, ask the person who sent it.

## How to sign a PDF, step by step

**1. Create your signature**
Open [Sign PDF](/sign-pdf/). At the top is a white signing pad.
- **Draw it:** sign with your finger on a phone, a stylus on a tablet, or the mouse or trackpad on a computer.
- **Or type it:** write your name in the *Or type it* box and it appears in a cursive script.
- Not happy? Press **Clear** and try again.

**2. Upload the PDF**
Drop in the PDF you need to sign.

**3. Choose where it goes**
- **Page:** type `last` (the default) or a page number such as `1` or `3`.
- **Position:** *Bottom right*, *Bottom left* or *Bottom center*.
- **Size:** drag the slider. It sets the signature's width as a share of the page width, from small to half the page.

**4. Sign and download**
Press **Sign PDF**, then **Download**. The file is saved with `-signed` added to its name, so your original stays untouched.

The signature has a transparent background, so it sits naturally over a signature line or text without a white box around it.

## Tips for a signature that looks real

- **Sign bigger than you think.** Draw across most of the pad, then use the Size slider to make it smaller on the page. A large, slow drawing looks smoother than a tiny, rushed one.
- **On a computer, a trackpad beats a mouse.** Or open the page on your phone, where signing with a finger feels natural.
- **Keep it consistent.** Use roughly the same signature you use on paper, so it matches your ID or earlier documents.
- **Start with the Size slider around the middle.** On an A4 page, about a quarter of the page width usually looks like a normal handwritten signature.

## Signing more than one page

Each run places one signature on one page. Contracts often want a signature or initials on every page, or on two separate pages. Just repeat the process:

1. Sign the first page and download the file.
2. Upload that **signed** file again.
3. Enter the next page number and sign again.

Your drawn signature stays on the pad while the page is open, so repeating takes only a few seconds.

## What if the signature line is in the middle of the page?

Sign PDF places signatures along the bottom of a page, about half an inch from the edge, which suits most letters and forms. If your document has a signature box in an unusual spot, such as the middle of a form, or you also need to type your name, date or CNIC number in fields, use the [PDF Editor](/pdf-editor/). There you click anywhere on a page to add text exactly where it belongs. Many people fill in the details with the editor first, then add the signature with Sign PDF.

## Common problems and fixes

**The signature looks shaky.**
Draw more slowly and larger. On a laptop, try your phone instead.

**The typed signature looks like a normal font.**
The handwriting style depends on fonts available on your device. If it looks too plain, draw your signature instead.

**It landed on the wrong page.**
Check the Page box. `last` means the final page; for anything else type the number. Sign the original file again with the correct page.

**The PDF has a password.**
The tool tries to open protected files. If it fails, remove the password with [Unlock PDF](/unlock-pdf/) first (you need to know it).

## Privacy and safety

Your document and your signature never leave your device: the PDF is opened, signed and saved by your browser. That matters, because a signature image is personal. A few more good habits:

- Do not leave signed copies in shared folders or public chats.
- If you email a signed contract, consider adding a password with [Protect PDF](/protect-pdf/) and sending the password separately.
- Read the whole document before signing. A quick tool makes it easy to sign without reading.

## FAQ

**Can I sign a PDF on my phone?**
Yes. Open Sign PDF in your mobile browser, sign with your finger and upload the PDF from your files.

**Is it free?**
Yes. No account, no watermark and no limit.

**Is a drawn signature legally valid?**
In many everyday situations, a signature image is accepted, but rules differ by country and by document. Some documents need a certified digital signature. Check with the person or office that asked you to sign. This is general information, not legal advice.

**Can I add the date next to my signature?**
Use the [PDF Editor](/pdf-editor/) to type the date anywhere on the page.

## Related tools

- [PDF Editor](/pdf-editor/) to type names, dates and form details
- [Protect PDF](/protect-pdf/) to password-protect the signed file
- [PDF Merger](/pdf-merger/) to combine the signed page with other documents
"""),
dict(slug='convert-word-to-pdf-on-phone-android-iphone', title='How to Convert Word to PDF on Your Phone (Android and iPhone)', date='2026-11-11',
 desc='Convert a Word file to PDF on your phone without installing an app. Find the DOCX from WhatsApp, email or Drive, convert it in your browser and share the PDF.',
 tools=['word-to-pdf', 'docx-to-pdf', 'pdf-merger'], md="""
The Word file arrives on WhatsApp ten minutes before the deadline. The portal only accepts PDF. Your laptop is at home. Sound familiar?

You can **convert Word to PDF on your phone** with nothing more than the browser you already have. DoraPDF's free [Word to PDF Converter](/word-to-pdf/) runs in Chrome, Safari or any modern mobile browser, converts the document on the phone itself, and gives you a PDF you can share straight away. No app to install and no account.

This guide focuses on the phone-specific parts that trip people up: finding the file, saving the PDF and sending it on.

## Step 1: Get the Word file onto your phone

The converter needs a **.docx** file saved on your phone. Depending on where it came from:

**From WhatsApp (Android):** open the chat, tap the document to download it, or tap and hold it and choose **Share** or **Save**. Downloaded files are usually reachable from the file picker under *Documents*, *Downloads* or *WhatsApp*.

**From WhatsApp (iPhone):** open the document, tap the **Share** icon, then **Save to Files** and pick a folder such as *On My iPhone* or *iCloud Drive*.

**From email:** tap the attachment and choose **Download** (Android) or tap **Share → Save to Files** (iPhone).

**From Google Drive or OneDrive:** you can usually pick files directly from these in the phone's file picker, as long as the app is installed and signed in. Otherwise, download the file first.

**From Google Docs:** a Google Doc is not a Word file yet. In the Docs app, open the menu (three dots) → **Share & export** → **Save as Word (.docx)**. Or simply export it as PDF there and skip the rest.

## Step 2: Convert Word to PDF on Android

1. Open Chrome and go to **dorapdf.com/word-to-pdf**.
2. Tap **Drop a file here**. The file picker opens.
3. Browse to your .docx (check *Downloads*, *Documents* or *Recent*).
4. Tap **Convert now** and wait a few seconds.
5. Tap **Download**.

Android saves the PDF to your **Downloads** folder. Chrome usually shows a bar at the bottom with an **Open** button, and you can always find it again in the *Files* app under Downloads.

## Step 3: Convert Word to PDF on iPhone

1. Open Safari and go to **dorapdf.com/word-to-pdf**.
2. Tap the upload area and choose **Choose File** (or **Browse**).
3. Find your .docx in the Files browser and tap it.
4. Tap **Convert now**, then **Download**.
5. Confirm the download when Safari asks.

The PDF goes to the **Files** app, in the *Downloads* folder. Tap the download arrow in Safari's address bar to open it quickly.

## Step 4: Share the PDF

From the Downloads folder, tap and hold the PDF (Android) or open it and tap the **Share** icon (iPhone). Then pick WhatsApp, Gmail, Outlook or your browser to upload it to a portal.

Before you send it, open the PDF once and scroll through. It takes ten seconds and catches problems while you can still fix them.

## What to expect from the PDF

The converter keeps the content and structure of your document: headings, paragraphs, bold and italic text, lists, tables and pictures, laid out on A4 pages. It uses a standard serif font rather than your document's exact font, recalculates page breaks, and stores pages as images, so text in the PDF cannot be selected.

For assignments, letters, notes and applications this is usually exactly what you need. For a designed CV or a thesis with strict formatting rules, export the PDF from the Word or Google Docs app itself. We explain the differences in detail in [our guide to converting Word to PDF online](/blog/convert-word-to-pdf-online-free/).

## Phone-specific problems and fixes

**"My file doesn't show up in the picker."**
The converter only accepts .docx files. If your document is greyed out or not accepted, it is probably an old **.doc**, an **.odt**, or a Google Docs link rather than a file. Re-save it as .docx in the Word or Docs app.

**"I tapped the WhatsApp document but can't find it in Files."**
On iPhone, WhatsApp keeps documents inside the app until you choose **Save to Files**. On Android, look in *Documents* or use the search in the Files app.

**"The download didn't start."**
Some in-app browsers (the browser that opens when you tap a link inside WhatsApp, Instagram or Facebook) block downloads. Tap the menu and choose **Open in Chrome** or **Open in Safari**, then try again.

**"The conversion is slow."**
Long documents with many pictures need more work from your phone. Close other heavy apps and keep the screen on until it finishes.

**"I need several Word files as one PDF."**
Convert each document, then combine the PDFs with the [PDF Merger](/pdf-merger/), adding them in the order you want.

## Privacy on a shared or borrowed phone

The conversion happens on the phone itself; the document is not uploaded to DoraPDF's servers. If you are using someone else's phone, delete the .docx and the PDF from their Downloads folder afterwards, and remove the files from any chat you used to transfer them.

## FAQ

**Do I need the Microsoft Word app?**
No. The converter works in the browser, so you do not need Word, WPS or any other office app.

**Is there a difference between Word to PDF and DOCX to PDF?**
They use the same conversion. [DOCX to PDF](/docx-to-pdf/) is simply the same tool under the name some people search for.

**Is it free on mobile?**
Yes. No sign-up, no watermark and no limit.

**Does it work on a tablet?**
Yes, on Android tablets and iPads in the same way.

## Related tools

- [DOCX to PDF](/docx-to-pdf/) for the same conversion under another name
- [PDF Merger](/pdf-merger/) to combine several converted documents
- [PDF Compressor](/pdf-compressor/) if the PDF is too large for a portal
"""),
dict(slug='convert-screenshots-png-to-pdf', title='How to Turn Screenshots and PNG Images Into One PDF', date='2026-11-11',
 desc='Convert screenshots and PNG images to one PDF free. Ideal for chat records, receipts, class slides and notes, with the right settings for long screenshots.',
 tools=['images-to-pdf', 'png-to-pdf', 'pdf-compressor'], md="""
Screenshots pile up fast. A bank transfer confirmation, a chat where a client agreed to a price, twenty slides from an online class, a booking page, a recipe. They are easy to take and hard to hand over neatly. Sending fifteen separate images is messy, and the person on the other side has to save each one.

A cleaner way is to **turn your screenshots into one PDF**. DoraPDF's free [Images to PDF Converter](/images-to-pdf/) takes PNG, JPG, WebP and iPhone HEIC images and puts them into a single PDF, one image per page, right in your browser.

## Why a PDF beats a folder of screenshots

- **One file, fixed order.** The reader scrolls from the first screenshot to the last, in the order you chose.
- **Easy to forward and archive.** One attachment instead of many, and it opens the same on every device.
- **Accepted everywhere.** Complaint portals, HR, insurance and university offices often ask for "a PDF of the evidence".
- **Harder to mix up.** Individual images get lost in a phone gallery; a PDF named `Payment-proof-Nov-2026.pdf` does not.

## How to convert screenshots to PDF

1. Open the [Images to PDF Converter](/images-to-pdf/) on your phone or computer.
2. Add your screenshots. On a phone, choose them from your photo library; on a computer, drag them in.
3. Make sure the list is in the right order. Each image becomes one page, top to bottom. Use **✕** to remove one and add it again at the end if it is misplaced.
4. Set **Page size** to **Fit page to image** and **Margin** to **No margin** or **Small margin** (see below why).
5. Press **Create PDF** and **Download**.

## The best settings for screenshots

Screenshots are not shaped like sheets of paper. A phone screenshot is tall and narrow, and a scrolling screenshot can be many times taller than it is wide. That is why the page size matters.

**Fit page to image (recommended).** Each page takes the exact shape of its screenshot. A tall chat capture becomes a tall page, and a laptop screenshot becomes a wide one. Nothing is shrunk to fit a sheet, so text stays as large as on the original screen.

**A4 page.** Each screenshot is centred on an A4 sheet and scaled to fit. That is fine for normal phone screenshots when you plan to print. But a **long scrolling screenshot** is shrunk until its whole height fits on one A4 page, which can make the text tiny. Use Fit page to image for those.

**Margin.** With *Fit page to image*, *No margin* looks like the screenshot itself. *Small margin* adds a thin white frame, which helps dark-mode screenshots stand out when printed.

## Smart uses for screenshot PDFs

**Proof of payment.** Put the transfer confirmation, the order page and the seller's chat reply into one PDF in that order. It tells the whole story without explanations.

**Online class slides.** If you screenshot slides during a lecture, convert them after class into one PDF per subject. Name it with the date, and your revision folder stays organised.

**Bug reports and website feedback.** Screenshots of each step, in order, show exactly what went wrong, which helps developers far more than a description.

**Travel bookings.** Tickets, hotel confirmations and visa appointment pages in one PDF are easier to find at an airport counter with poor signal.

**Recipes and how-tos.** Screenshots of a long recipe or tutorial become a small offline booklet.

## PNG, transparency and WebP

Screenshots are usually saved as **PNG**, and the converter handles them directly. If a PNG has a transparent background (common with logos and stickers), the transparent parts become **white** in the PDF, because PDF pages are white.

WebP images, which you often get when saving pictures from websites, work too. If you only have PNG files, the [PNG to PDF](/png-to-pdf/) tool does the same job with a file picker limited to PNG.

## Before you convert: a quick clean-up

- **Crop out the status bar and notifications.** Your battery level, signal and private message previews do not belong in a document. Crop them in your gallery app.
- **Hide private details.** If a screenshot shows account numbers or someone else's phone number that the reader does not need, cover them before converting. The markup or edit tool in your phone's gallery can draw a solid box over them.
- **Delete duplicates.** It is easy to take the same screenshot twice. Skim the list before converting.

## Common problems and fixes

**The PDF is too large to email.**
Very large images are scaled to a maximum of 2400 pixels wide during conversion, but many screenshots still add up. Compress the PDF with the [PDF Compressor](/pdf-compressor/).

**The text in a long screenshot is tiny.**
You probably used A4 page size. Convert again with **Fit page to image**.

**The screenshots are in the wrong order.**
The PDF follows the list. Add screenshots in the order you want, or remove and re-add the misplaced ones.

**A screenshot looks blurry.**
It may have been compressed by a chat app before you saved it. Use the original from the device that took it.

## Privacy

Screenshots often contain the most private things on a phone: chats, balances, addresses. The converter reads and combines them **inside your browser**, without uploading them to a server, and the PDF is created on your device.

## FAQ

**How do I combine multiple screenshots into one PDF?**
Add all of them to the Images to PDF Converter. Each screenshot becomes a page in a single PDF.

**Can I do this on my phone?**
Yes. It works in mobile browsers on Android and iPhone; pick screenshots from your gallery.

**Is there a watermark or sign-up?**
No to both.

**Will the screenshots lose quality?**
Images are saved as high-quality JPEG inside the PDF, and only images wider than 2400 pixels are scaled down. Screen text stays sharp.

## Related tools

- [PNG to PDF](/png-to-pdf/) for PNG-only batches
- [PDF Compressor](/pdf-compressor/) to make the PDF easy to email
- [PDF Merger](/pdf-merger/) to add your screenshot PDF to other documents
"""),
dict(slug='convert-pdf-to-powerpoint-slides-free', title='Convert PDF to PowerPoint Free: Turn Every Page Into a Slide', date='2026-11-11',
 desc='Convert PDF to PowerPoint (PPT) free in your browser. Each page becomes a slide you can present, annotate and add notes to. What to expect and when to use it.',
 tools=['pdf-to-powerpoint', 'pdf-to-word', 'pdf-splitter'], md="""
Your teacher shared the lecture as a PDF, and you have to present part of it tomorrow. A client sent a report as PDF, and the meeting runs on PowerPoint. Or you just want to show a document full-screen, add your own notes, and click through it page by page.

That is exactly what DoraPDF's free [PDF to PowerPoint Converter](/pdf-to-powerpoint/) is for. It **converts a PDF to PowerPoint** by turning every page into its own slide in a .pptx file, right in your browser. This guide explains how it works, what you can and cannot edit afterwards, and a few ways to get the most out of it.

## How it works (and why it matters)

The converter draws each PDF page as a high-resolution picture and places it on its own slide, filling the slide edge to edge. The slide size is set to match the shape of your PDF's pages, so an A4 portrait document becomes tall slides and a landscape presentation PDF becomes wide ones. Nothing is cropped or squashed.

This approach has one big advantage and one big limitation:

- **Advantage:** every slide looks exactly like the PDF page. Fonts, charts, tables, equations, Urdu or Arabic text, diagrams: all appear just as they did, because they are part of the picture.
- **Limitation:** the text on the slide is **not editable**. You cannot click into a sentence and change it, because it is part of the page image.

So think of the result as "your PDF, ready to present in PowerPoint", not as a fully editable deck.

## How to convert PDF to PPT

1. Open the [PDF to PowerPoint Converter](/pdf-to-powerpoint/).
2. Drop in your PDF.
3. Press **Convert now** and wait while each page is turned into a slide. Longer PDFs take a little longer.
4. **Download** the .pptx file.

Open it in Microsoft PowerPoint, Google Slides, Keynote, LibreOffice Impress or the PowerPoint app on your phone.

## What you can do with the slides

Even though the page text is fixed, PowerPoint gives you plenty to work with:

- **Present full-screen** with clean page-by-page navigation, laser pointer and pen tools.
- **Add speaker notes** under each slide, so you know what to say about every page.
- **Draw and highlight** during the presentation, or add arrows and shapes beforehand.
- **Add text boxes on top** of a slide to label a chart, translate a heading or add a comment.
- **Delete, duplicate and reorder slides** to present only the pages that matter.
- **Add animations and transitions** to your own shapes and text boxes.
- **Insert extra slides** between PDF pages, such as a title slide, a question slide or a summary.

## Real examples

**Student presenting a chapter.** Convert the chapter PDF, delete the pages you will not cover, add a title slide with your name, and write your talking points in the speaker notes.

**Teacher reviewing a past paper.** Convert the exam paper, then use the pen tool in class to work through each question on screen.

**Office meeting about a report.** Convert the report, hide the appendix slides, and add arrows and text boxes to highlight the figures you want to discuss.

**Sharing a PDF on a classroom smart board.** Many boards run PowerPoint more smoothly than a PDF reader, and slide navigation is easier with a clicker.

## When you need editable text instead

If your goal is to *change* the wording, not to present the page, a different route works better:

1. Convert the PDF with the [PDF to Word Converter](/pdf-to-word/). Choose *Text only* mode to get clean, editable paragraphs.
2. Copy the text you need into your own PowerPoint slides and design them as you like.

For simple text extraction, the [PDF to Text](/pdf-to-txt/) tool gives you the words in a plain .txt file you can paste anywhere.

You can also combine both approaches: present the original pages as image slides and add new, editable slides of your own in between.

## Tips for better results

- **Mixed page sizes:** the slide size is taken from the first page. If your PDF mixes portrait and landscape pages, split it with the [PDF Splitter](/pdf-splitter/) and convert each part separately, so no page gets stretched.
- **Only need a few pages?** Extract them first with the splitter. A smaller PDF converts faster and gives a lighter .pptx.
- **Big file size:** each slide is a high-quality image, so a 100-page PDF gives a large presentation. Convert only what you will present.
- **Scanned PDFs work too.** Since pages are converted as pictures, a scanned document looks exactly like the scan.

## Common problems and fixes

**"I can't edit the text on my slides."**
That is how this converter works; the page is a picture. Add text boxes on top, or use PDF to Word to get editable text.

**"Some slides look stretched."**
Your PDF probably has pages of different sizes. Split it by page size and convert the parts separately.

**"The PDF won't open."**
If the PDF is password protected, remove the password with [Unlock PDF](/unlock-pdf/) first (you need to know it).

**"Going back from PowerPoint to PDF."**
The easiest way to keep the full design is PowerPoint's own File → Save As → PDF. DoraPDF's [PPTX to PDF](/pptx-to-pdf/) tool keeps only the slide text, which is useful for handouts but does not include designs and images.

## Privacy

The PDF is converted **inside your browser**. Pages are not uploaded to a server, so internal reports, exam papers and client documents stay on your device.

## FAQ

**Is this PDF to PowerPoint converter free?**
Yes. No sign-up, no watermark and no daily limit.

**Can I convert PDF to PPT on my phone?**
Yes. The tool runs in mobile browsers, and the .pptx opens in the PowerPoint or Google Slides app.

**Will the slides look the same as the PDF?**
Yes. Each slide is an exact picture of its page, at the same proportions.

**Can I convert the .pptx to Google Slides?**
Upload the .pptx to Google Drive and open it with Google Slides.

## Related tools

- [PDF to Word Converter](/pdf-to-word/) for editable text
- [PDF Splitter](/pdf-splitter/) to convert only the pages you need
- [PDF to Text](/pdf-to-txt/) to grab the words quickly
"""),
dict(slug='remove-background-from-image-free', title='Remove Background from Image Free: Clean PNG Cutouts Without Uploading Your Photo', date='2026-11-10',
 desc='Remove the background from any image for free. Get a transparent PNG or a white background in seconds, processed privately in your browser.',
 tools=['image-background-remover', 'image-compressor', 'image-resizer'], md="""
If you sell on Daraz or Instagram, need a passport-style photo with a plain backdrop, or want a logo without the box behind it, you need to **remove the background from an image**. Doing it by hand with a lasso tool takes ages. DoraPDF's free [Image Background Remover](/image-background-remover/) does it automatically with an AI model that runs **inside your browser**, so the photo never leaves your phone or computer.

This guide shows how to get a clean cutout, which mode to pick, and how to fix the edges when the result is not perfect.

## What the tool actually does

You give it one photo. The AI works out which pixels belong to the subject (a person, a product, a pet) and which belong to the background. It then makes the background pixels transparent and gives you a **PNG file** named like `photo-no-bg.png`.

Instead of transparency you can also pick a solid colour: **white, black, pink or light grey**. White is the one most online stores ask for.

After processing, a **before/after slider** appears under the result, so you can drag across the image and check the edges before you download.

## Quick mode or HD mode?

There are two modes, and choosing the right one makes a big difference.

| | Quick | HD |
|---|---|---|
| Best for | People, selfies, portraits | Any object: products, food, cars, pets |
| One-time model download | about 13 MB | about 115 MB |
| Needs | Any modern browser | A browser with GPU support (WebGPU) |

The model downloads only the first time; after that the browser keeps it. If you choose HD and your browser has no GPU acceleration, the tool tells you and falls back to Quick mode automatically, so you still get a result.

**Rule of thumb:** a photo of a person, use Quick. A shoe, a bottle, a plate of biryani or a handbag, use HD on a laptop or desktop with Chrome or Edge.

## How to remove a background, step by step

1. Open the [Image Background Remover](/image-background-remover/).
2. Drop your photo in, or tap to choose it. JPG, PNG, WebP and even iPhone **HEIC** photos are accepted.
3. Choose the **Mode** (Quick or HD).
4. Choose the **Background**: Transparent, White, Black, Pink or Light grey.
5. Press **Remove background**. The first run takes longer while the model loads.
6. Drag the comparison slider to check the edges, then download the PNG.

Very wide photos are scaled to 2000 pixels wide before processing, which is plenty for product listings, social posts and documents.

## Getting a cleaner cutout

The AI does most of the work, but the photo you start with matters.

- **Contrast helps.** A dark jacket against a dark wall is hard for any tool. If you can retake the photo, stand the subject in front of a lighter, plainer surface.
- **Keep the subject whole.** Hands or feet cut off at the frame edge are fine, but a subject that blends into another object (a person leaning on a sofa of the same colour) can lose detail.
- **Fine hair and fur.** Quick mode is tuned for people and usually handles hair well. For fluffy pets or detailed objects, HD gives smoother edges.
- **Glass and shadows.** Transparent bottles and soft shadows are partly see-through, so some background can show through or the shadow may disappear. That is normal.

## Common problems and fixes

**"AI model could not load."** The model is downloaded on first use, so you need a working internet connection the first time. Refresh and try again on a stable connection.

**Part of the product was removed.** Switch from Quick to HD. Quick mode is focused on people, so it can treat a product as background.

**The file is too big to upload to a store.** PNG keeps transparency but is large. If you used a white background, run the result through the [Image Compressor](/image-compressor/) to get a much smaller file.

**I need an exact size, like 1080 × 1080.** Remove the background first, then use the [Image Resizer](/image-resizer/) to set the exact pixels.

**It is slow on my phone.** Large photos and HD mode need more power. Use Quick mode on phones, or try on a computer.

## Practical uses

- **Online selling:** white-background product shots look consistent across a catalogue.
- **CVs and ID forms:** a plain white or light grey background behind a portrait.
- **Presentations and assignments:** a transparent PNG of a person or object sits neatly on any slide colour.
- **Stickers and thumbnails:** cut yourself out and place the PNG on a YouTube thumbnail or WhatsApp sticker design.

## Privacy

Everything happens on your device. The tool downloads the AI model to your browser, then runs it locally on your photo. Your image is **not uploaded** to DoraPDF's servers. That makes it safe for personal photos, ID pictures and unreleased product images.

## FAQ

**Is it really free?**
Yes. There is no watermark, no sign-up and no limit on how many photos you process.

**Can I remove backgrounds from several images at once?**
The tool works on one image at a time, so you can check each result before saving it.

**Why is the output always PNG?**
PNG is the common format that supports transparency. Even with a coloured background you get a lossless PNG, which you can then convert or compress.

**Does it work offline?**
After the model has been downloaded once, the processing itself happens locally. The first use needs internet.

**Can I change the background to a photo instead of a colour?**
Not inside this tool. Save the transparent PNG and place it over any picture in a slide or design app.

## Related tools

- [Image Compressor](/image-compressor/) to shrink your cutout for the web.
- [Image Resizer](/image-resizer/) for exact marketplace or social sizes.
- [Object Remover](/object-remover/) when you want to keep the background but erase one thing from it.
"""),
dict(slug='image-to-text-converter-urdu-english', title='Image to Text Converter for Urdu, English and 11 More Languages: Copy Text from Photos', date='2026-11-10',
 desc='Copy text from photos, screenshots and scanned notes for free. Supports Urdu, English, Arabic, Hindi and more, with OCR that runs in your browser.',
 tools=['image-to-text', 'pdf-ocr', 'scan-to-pdf'], md="""
A photo of a notice board, a screenshot of a WhatsApp message, a picture of a page from your friend's notes: the text is right there, but you cannot select it. An **image to text converter** fixes that. It reads the letters in the picture (this is called OCR, optical character recognition) and gives you text you can copy, edit and search.

DoraPDF's [Image to Text Converter](/image-to-text/) is free, needs no account, and supports **Urdu** as well as English, Arabic, Hindi and other languages. It also runs entirely in your browser.

## Languages you can choose

Pick the language of the text before you start, because the recognition model is different for each script:

English, Urdu, Arabic, Hindi, Spanish, French, German, Portuguese, Italian, Turkish, Indonesian, Russian and Chinese (Simplified).

The model for each language downloads once, roughly 2 to 10 MB, and is then reused.

## Copying text from an image in five steps

1. Open [Image to Text](/image-to-text/).
2. Select the **Language** that matches the text in your picture.
3. Add your image. JPG, PNG, WebP and iPhone HEIC photos all work, and you can add **several images at once**.
4. Press **Extract text**.
5. The text appears in a box. Use **Copy text**, or download the `.txt` file.

If you added more than one image, the results are joined into one text, and each part starts with a line showing the file name. That is handy when you photograph a multi-page handout page by page.

## How to take a photo that reads well

OCR is only as good as the picture. A few habits make a large difference:

- **Shoot straight on.** Hold the phone parallel to the page rather than at an angle.
- **Use even light.** Daylight near a window beats a ceiling bulb that throws your phone's shadow across the page.
- **Fill the frame with the text.** Crop out the desk, your fingers and the background.
- **Stay sharp.** Tap to focus and hold still. A blurry photo produces broken words.
- **Printed text works best.** Neat handwriting is sometimes readable, but messy handwriting usually is not.

## Tips for Urdu and Arabic text

Urdu Nastaliq is one of the harder scripts for OCR because letters join and stack in a flowing line. You will get the best results from **clear printed Urdu** such as books, newspapers and typed documents in a good-sized font.

- Choose **Urdu**, not Arabic, for Urdu text. The two share letters, but the Urdu model knows the extra characters like ٹ, ڈ and ے.
- Photograph one column at a time if the page has columns.
- Always proofread. Dots on letters are small, and a missed dot can turn one letter into another.

## When to use a different tool

Image to Text gives you **plain text**. Sometimes you want something else:

- **You have a scanned PDF, not an image.** Use [PDF OCR](/pdf-ocr/). It makes the whole PDF searchable and also gives you a text file.
- **You want to keep the page as a document.** Turn your photos into a neat PDF with [Scan to PDF](/scan-to-pdf/) first, then run OCR if you need the text.
- **The PDF already has selectable text.** You do not need OCR at all; [PDF to Word](/pdf-to-word/) will keep the layout.

## Common problems and fixes

**"No readable text found in this image."** The picture may be too dark, too blurry or too small, or the wrong language is selected. Retake the photo closer and in better light.

**Strange symbols mixed into the text.** This usually means the wrong language was picked, or there are logos, stamps or lines on the page. Crop the image to just the text.

**Words in the wrong order.** Pages with tables, sidebars or two columns can confuse the reading order. Crop each block separately and run them one by one.

**It is slow.** Very large photos take longer to read. Images are scaled to at most 3000 pixels wide, which keeps small text readable, but older phones still need a little patience.

## Privacy

Recognition happens on your device. Only the language model is downloaded; your images are **not uploaded** to our server. You can safely use it for ID cards, bank letters or private notes, though as always it is wise to delete sensitive photos from your phone when you are done.

## Ideas for students and office work

- Turn photographed lecture slides into notes you can edit and highlight.
- Copy a quote from a book photo into your assignment, then add the proper citation.
- Pull an address or phone number from a business card or poster.
- Convert a screenshot of a table into text, then tidy it in a spreadsheet.

## FAQ

**Is there a limit on images?**
No fixed limit. You can add several images in one go; very large batches just take longer.

**Can it read handwriting?**
Sometimes, if the writing is neat and well spaced. It is designed mainly for printed text, so expect to correct handwritten results.

**Can I extract text in two languages from one image?**
You choose one language per run. For a page that mixes Urdu and English, run it once with each language and combine the parts you need.

**Does it keep bold, colours or layout?**
No. The output is plain text, which is what makes it easy to paste anywhere.

## Related tools

- [PDF OCR](/pdf-ocr/) for scanned PDFs.
- [Scan to PDF](/scan-to-pdf/) to turn phone photos into a document.
- [PDF to Word](/pdf-to-word/) for PDFs that already contain real text.
"""),
dict(slug='make-scanned-pdf-searchable-ocr', title='How to Make a Scanned PDF Searchable with Free OCR (No Upload Needed)', date='2026-11-10',
 desc='Turn a scanned PDF into a searchable, copyable PDF with free OCR. Press Ctrl+F to find words, copy text, and get a .txt file too.',
 tools=['pdf-ocr', 'image-to-text', 'pdf-compressor'], md="""
You press Ctrl+F in a PDF, type a word you can clearly see on the page, and get "no results". That happens because the PDF is a **scan**: each page is just a picture of paper. To **make a scanned PDF searchable**, you need OCR to recognise the letters and add a hidden text layer behind each page.

DoraPDF's free [PDF OCR tool](/pdf-ocr/) does exactly that in your browser. The pages look the same as before, but now you can search, select and copy the words.

## Scanned PDF vs. "real" PDF: a quick test

Not sure if your file needs OCR? Open it and try to highlight a sentence with your mouse.

- **The text highlights word by word:** the PDF already has text. You do not need OCR. Tools like [PDF to Word](/pdf-to-word/) will work directly.
- **A blue box covers the whole page, or nothing highlights:** the page is an image. OCR is what you need.

Files from office scanners, phone scanner apps, fax machines and old archives are almost always image-only.

## What you get from the tool

Running OCR gives you two downloads:

1. **`yourfile-searchable.pdf`**: each page keeps its original look, with invisible text placed on top of the words so search and copy work.
2. **`yourfile.txt`**: all the recognised text in one plain-text file, with a "Page N" marker before each page.

## Step-by-step

1. Open [PDF OCR](/pdf-ocr/).
2. Choose the **Language** of the document: English, Urdu, Arabic, Hindi, Spanish, French, German, Portuguese, Italian, Turkish, Indonesian, Russian or Chinese (Simplified).
3. Add your PDF.
4. Press **Run OCR** and wait. Each page takes roughly 5 to 15 seconds, depending on your device and how much text is on it.
5. Download the searchable PDF, the text file, or both.

The tool processes up to the **first 60 pages** of a document. For a longer book, split it into parts with the [PDF Splitter](/pdf-splitter/) and run each part separately.

## One thing to know about non-English scripts

The hidden text layer inside the PDF uses a standard Latin font. That works well for English and for most of the Western European languages in the list. For scripts such as **Urdu, Arabic, Hindi, Russian and Chinese**, many characters cannot be stored in that layer, so searching inside the PDF will not find them.

The recognition itself still works for those languages: the full text appears in the **.txt file**. So for an Urdu or Arabic document, think of the text file as the main result and the PDF as a copy of the scan.

## Getting accurate results

OCR reads what it can see. Better scans mean fewer mistakes.

- **Scan at a decent resolution.** If you control the scanner, 300 DPI is a good setting for text.
- **Keep pages straight.** A tilted page makes lines harder to follow. Rotate sideways pages first with [Rotate PDF](/rotate-pdf/).
- **Avoid heavy shadows** along the spine of a book. Press the book flat or scan one page at a time.
- **Pick the right language.** Running an Urdu document with English selected produces nonsense.

## Common problems and fixes

**"No readable text found."** The scan may be very faint, extremely low resolution or mostly images. Try a cleaner scan. If the pages contain only handwriting, OCR may not pick it up.

**The searchable PDF is larger than the original.** Each page is redrawn as a fresh image with the text layer added. If size matters, run the result through the [PDF Compressor](/pdf-compressor/).

**Search finds some words but not others.** OCR can misread a letter here and there, for example "rn" read as "m". Search for a shorter part of the word, or check the .txt file.

**My PDF has 120 pages and only 60 were done.** That is the per-run limit. Split the file and process the second half on its own.

## Privacy

The OCR engine and language model are downloaded to your browser and run there. Your PDF is **not uploaded** to DoraPDF. That matters for contracts, medical reports, bank statements and anything else you would not want sitting on a stranger's server.

## Where searchable PDFs save real time

- **Students:** search a scanned reference book for the one paragraph you need to cite.
- **Offices:** find an invoice number across a stack of scanned bills.
- **Researchers:** copy quotes from old journal scans instead of retyping them.
- **Home:** make a folder of scanned certificates and letters easy to search later.

## FAQ

**Will OCR change how my pages look?**
No. The visible page stays as an image of the original. The text layer is invisible.

**Can I edit the text in the PDF afterwards?**
The searchable PDF lets you select and copy text, not rewrite the page. To edit, paste the text from the .txt file into a document.

**I only have photos of pages, not a PDF. What should I use?**
Use [Image to Text](/image-to-text/) directly on the photos, or combine them into a PDF with [Scan to PDF](/scan-to-pdf/) first.

**Is there a cost or watermark?**
No. It is free, with no watermark and no account.

## Related tools

- [Image to Text](/image-to-text/) for photos and screenshots.
- [PDF Compressor](/pdf-compressor/) to shrink the searchable PDF.
- [PDF Splitter](/pdf-splitter/) for documents longer than 60 pages.
"""),
dict(slug='upscale-image-4x-free-ai', title='Upscale an Image 2× or 4× Free with AI: Make Small Photos Bigger and Sharper', date='2026-11-10',
 desc='Increase image resolution for free. Upscale small or blurry photos 2× or 4× with an AI model that runs in your browser, then download a sharp PNG.',
 tools=['image-upscaler', 'image-compressor', 'image-resizer'], md="""
A logo that looks fuzzy on a banner. An old family photo that is only a few hundred pixels wide. A product picture a supplier sent over WhatsApp, squashed to thumbnail size. If you simply stretch these images, they turn soft and blocky. To **upscale an image** properly, you need something that adds believable detail as it enlarges.

DoraPDF's free [AI Image Upscaler](/image-upscaler/) enlarges photos **2× or 4×** using an AI model that runs inside your browser. Here is how to use it well, and what it can and cannot do.

## Plain resizing vs. AI upscaling

When an ordinary editor makes a picture bigger, it has to invent the new pixels by averaging the old ones. The result is larger but blurry.

An AI upscaler has learned from many images what edges, textures and fine lines usually look like. When it enlarges your photo, it rebuilds those details so edges stay crisp. It cannot recover information that was never captured, but it makes much better guesses than a simple stretch.

## The two modes

| Mode | What it does | When to use it |
|---|---|---|
| **AI (best quality)** | Runs the AI model to rebuild detail | Most photos, logos, artwork |
| **Fast (classic + sharpen)** | High-quality enlargement plus a sharpening pass | Very large images, slow devices |

The AI model is small, about 2 MB, and downloads once. In AI mode the output is limited to roughly **6000 pixels on the longest side**. A 2000-pixel image at 4× would go past that, so the tool will ask you to use 2× or Fast mode instead.

If AI cannot run on your device, the tool switches to Fast mode automatically and tells you, so you are never left without a result.

## How to upscale a photo

1. Open the [AI Image Upscaler](/image-upscaler/).
2. Add your image. JPG, PNG, WebP and iPhone HEIC are supported.
3. Choose **Upscale**: 2× (double size) or 4× (HD boost).
4. Choose **Mode**: AI or Fast.
5. Press **Upscale**.
6. Drag the before/after slider to compare, then download the PNG. The file name and new dimensions are shown, for example `logo-4x.png · 2400×1600`.

## Which scale should you pick?

- **2×** is the safe default. It doubles width and height (four times the pixels) and gives natural-looking results on most photos.
- **4×** is for images that start very small, like icons, old web photos or thumbnails, and need to reach print or HD size.

If you need a specific final size, for example 1920 pixels wide, upscale first, then bring it down to the exact width with the [Image Resizer](/image-resizer/). Shrinking a slightly too-large image keeps it sharp; stretching never does.

## Real situations where it helps

- **Printing:** a photo that looks fine on a phone may print blurry on A4. Upscaling gives the printer more pixels to work with.
- **Presentations and assignments:** small images from the web look soft on a projector. A 2× upscale often fixes that.
- **Online stores:** marketplaces often prefer larger product images so customers can zoom.
- **Logos and graphics:** low-resolution logos get cleaner edges at 4×. For a true vector you can trace a PNG with [PNG to SVG](/png-to-svg/).

## Honest limits

AI upscaling is impressive, but it is not magic.

- **It will not read blurred text.** If letters are an unreadable smudge, they stay unreadable or become plausible-looking shapes.
- **Faces in tiny photos** may look slightly smooth or painted, because the model is filling in missing detail.
- **Heavy JPEG blockiness** can be softened but not fully removed from very compressed images.
- **Large images on phones** can take a minute or more. Use Fast mode for big files on older devices.

## Common problems and fixes

**"Image is too large for AI 4×."** Your output would exceed about 6000 pixels. Choose 2×, or switch to Fast mode.

**"AI unavailable on this device — used Fast mode."** Your browser could not run the model, so the classic method was used. Try an up-to-date Chrome or Edge on a computer for the AI result.

**The PNG file is huge.** Upscaled PNGs are large by nature. Send the result through the [Image Compressor](/image-compressor/) to get a lighter file for web or WhatsApp.

**The result looks over-sharpened.** Try AI mode instead of Fast, or start from the original file rather than a screenshot of it.

## Privacy

The upscaling happens on your own device. Only the small model is downloaded; your photos are **not uploaded** anywhere. Personal photos and client images stay with you.

## FAQ

**Is the upscaler free?**
Yes, with no watermark and no account.

**Can I upscale several images at once?**
It handles one image per run, which keeps memory use manageable in the browser.

**Why is the output PNG?**
PNG is lossless, so the detail the AI rebuilt is not thrown away by compression. You can compress or convert it afterwards.

**Can it fix a photo that is out of focus?**
It can make a slightly soft photo look crisper, but a badly blurred photo will not become sharp.

## Related tools

- [Image Resizer](/image-resizer/) for exact final dimensions.
- [Image Compressor](/image-compressor/) to cut the file size after upscaling.
- [Image Background Remover](/image-background-remover/) for a clean cutout of the enlarged subject.
"""),
dict(slug='remove-object-from-photo-free', title='Remove Objects, People or Text from a Photo for Free with a Simple Brush', date='2026-11-10',
 desc='Erase unwanted objects, people in the background, text or blemishes from photos. Free brush-based object remover that works in your browser.',
 tools=['object-remover', 'image-upscaler', 'image-background-remover'], md="""
The photo is almost perfect, apart from a stranger walking behind you, a power line across the sky, or a bottle someone left on the table. You can **remove the object from the photo for free** in a few strokes: paint over it, press a button, and the area is filled in to match its surroundings.

That is what DoraPDF's [Object Remover](/object-remover/) does. This guide covers how to brush, which fill style to choose, and the tricks that give a clean, natural result.

## How it works

You paint a pink mask over the thing you want gone. The tool then fills that area using the pixels around it, blending colours and textures inward from the edges. It is the same family of technique photo editors call "inpainting".

Because the fill comes from the surroundings, it works best when the background behind the object is something that can be continued: sky, a wall, grass, sand, a road, skin, a plain table.

## Step-by-step

1. Open the [Object Remover](/object-remover/) and add a photo (JPG, PNG, WebP or HEIC).
2. Set the **Brush size** with the slider. Choose a size a little bigger than the object's thinnest part.
3. Paint over the object. Cover it completely and go **slightly past its edges**.
4. Choose a **Fill style** (Auto is a good start).
5. Press **Remove object**.
6. Look closely. If a trace is left, brush over it again and remove once more.
7. Press **Download PNG** when you are happy.

Made a mistake? **Undo** steps back through your last removals, and **Clear brush** wipes the pink mask without touching the photo.

## Choosing the fill style

| Fill style | Best for |
|---|---|
| **Auto (recommended)** | Lets the tool decide based on the area around your brush |
| **Smooth fill** | Logos, skin, sky, flat walls, plain colours and soft gradients |
| **Texture** | Busy photos: grass, gravel, leaves, carpet |
| **Lines & edges** | Areas where straight lines or edges run behind the object |

Auto looks at how much variety there is around the masked area. Calm surroundings get the smooth fill; detailed surroundings get the texture fill. If the result looks smeared, try Texture. If it looks patchy on a plain surface, try Smooth.

## Brushing tips that make the difference

- **Over-paint a little.** Leaving a thin outline of the object means the fill will copy that outline. A few extra pixels of margin hides it.
- **Include the shadow.** A person removed without their shadow leaves a ghost on the ground.
- **Work in small pieces.** For a large object, remove one part, then the next. Several small fills look more natural than one huge one.
- **Zoom with your eyes, not the tool.** Check the result on a big screen before downloading; small seams are easier to spot there.

## What it does well, and where it struggles

**Works well:**

- People or tourists in the background
- Date stamps, small text and stickers
- Wires, poles and small signs against the sky
- Spots, pimples and dust on scanned photos
- Litter on grass or sand

**Harder:**

- Very large objects that cover most of the frame
- Objects in front of complex patterns that must line up, like a brick wall or text on a sign
- Anything where the hidden background is unique, like a face behind a hand

For big cleanups, accept that you may need two or three passes.

## About image size

To keep the editor quick in the browser, photos wider than **1400 pixels** are scaled down to 1400 pixels wide when you load them, and the download is that size. This is fine for social media, WhatsApp and documents. If you need a larger final image, you can run the cleaned PNG through the [AI Image Upscaler](/image-upscaler/) at 2×.

## Common problems and fixes

**"Brush over the object you want to remove first."** You pressed Remove without painting a mask. Paint over the object, then try again.

**"Timed out — try a smaller brush area."** The masked area was very large for your device. Remove the object in two or three smaller sections.

**A blurry patch is left behind.** Switch the fill style to Texture and repeat on that spot, or use a slightly smaller brush.

**The engine takes a moment the first time.** The image engine loads in the background when you add a photo. The first removal may show "Loading engine…" briefly.

## Use it responsibly

Cleaning up your own photos is what this tool is for. Do not use it to remove watermarks or credits from images you do not own, or to change a photo in a way that misleads people, such as editing documents or evidence. DoraPDF also has a [Watermark Eraser](/watermark-eraser/) that works the same way, intended for images you own or have permission to edit.

## Privacy

All of the editing happens in your browser. Your photo is **not uploaded** to DoraPDF, so family pictures and private images stay on your device.

## FAQ

**Is it free?**
Yes. No sign-up, no watermark on the result.

**Can I undo a removal?**
Yes. Undo steps back through your recent removals, one at a time.

**Does it work on phones?**
Yes, you can paint with your finger. A stylus or a computer mouse gives more precise masks.

**Why is the download a PNG?**
PNG avoids adding new compression artefacts on top of your edit. Use the [Image Compressor](/image-compressor/) if you need a smaller file.

## Related tools

- [Image Background Remover](/image-background-remover/) to remove the entire background instead of one object.
- [AI Image Upscaler](/image-upscaler/) to enlarge the cleaned photo.
- [Image Compressor](/image-compressor/) to make it light enough to share.
"""),
dict(slug='convert-pdf-to-excel-free', title='Convert PDF to Excel Free: Get Tables from a PDF into an .xlsx Sheet', date='2026-11-10',
 desc='Convert PDF tables to Excel for free. Each page becomes its own sheet, numbers stay as numbers, and your file is processed in your browser.',
 tools=['pdf-to-excel', 'pdf-ocr', 'pdf-splitter'], md="""
Bank statements, price lists, attendance registers, marks sheets, supplier invoices: so much tabular data arrives as a PDF. Copying it into a spreadsheet row by row is slow and error-prone. If you **convert the PDF to Excel**, you can sort, filter, total and chart the numbers in minutes.

DoraPDF's free [PDF to Excel Converter](/pdf-to-excel/) reads the text on each page, works out the rows and columns, and saves everything as an `.xlsx` workbook. Here is how to get the cleanest spreadsheet possible.

## How the conversion works

The tool looks at where each piece of text sits on the page.

- Text on the **same line** becomes one **row**.
- Wide gaps between pieces of text start a **new column**.
- Values that look like numbers, including ones with thousands separators such as `12,500`, are stored as **real numbers**, so Excel can add them up straight away.
- **Each PDF page becomes its own sheet**, named "Page 1", "Page 2" and so on.
- Column widths are set automatically to fit the content.

This approach works on any PDF that contains real text, whether or not the table has visible borders.

## Converting a PDF, step by step

1. Open [PDF to Excel](/pdf-to-excel/).
2. Add your PDF.
3. Press **Convert now**.
4. Download the `.xlsx` file and open it in Excel, Google Sheets, LibreOffice or WPS.

That is the whole process; there are no settings to fiddle with.

## Cleaning up the result in Excel

Most PDFs convert well, but tables designed for printing sometimes need a little tidying. These quick fixes cover most cases:

- **Merge the sheets.** Since every page is a separate sheet, copy the rows from Page 2, Page 3 and so on under Page 1 if you want one long table. Delete repeated header rows as you go.
- **Remove extra lines.** Page titles, footers and page numbers come across as rows too. Filter or delete them.
- **Fix split cells.** If a long description wrapped onto two lines in the PDF, it may appear as two rows. Join them with a formula like `=A2&" "&A3` or simply retype.
- **Check dates.** Dates are kept as text so they are not misread. Use Excel's **Text to Columns** or **DATEVALUE** to turn them into real dates if you need to sort by them.
- **Spot-check totals.** Add a SUM under a column and compare it with the total printed in the PDF. A match means nothing was lost.

## Example: a bank statement

A typical monthly statement has columns for date, description, debit, credit and balance. After conversion you get one sheet per page. Copy them together, delete the repeated headers and the "Page x of y" rows, and you have a clean list. Now a filter on the description column shows every payment to one shop, and a SUM on the debit column shows what you spent.

## What about scanned PDFs?

If the PDF is a scan (a photo of paper), there is no text to read, and the tool will tell you: **"No text found — this PDF looks scanned."**

You can often work around this. Run the file through [PDF OCR](/pdf-ocr/) first. It adds a hidden text layer to each page, and that searchable PDF can then be converted. The accuracy depends on how clear the scan is, so check the numbers carefully afterwards.

## Common problems and fixes

**Columns are shifted on some rows.** This happens when a cell is empty in the PDF, so the values on that row slide left. Insert a blank cell to line them back up.

**Everything landed in one column.** The text in the PDF is very tightly spaced. Use Excel's **Text to Columns** with a space or other separator to split it.

**I only need one page of a long report.** Extract that page first with the [PDF Splitter](/pdf-splitter/), then convert the smaller file. You get a tidy workbook with just the sheet you need.

**The PDF is password-protected.** Open it with the password and remove the protection first using [Unlock PDF](/unlock-pdf/), if you have the right to do so.

## Privacy

The PDF is read and converted entirely inside your browser. It is **not uploaded** to DoraPDF. That makes the tool suitable for statements, payslips and business reports you would not want to send to an unknown server.

## Who finds this useful

- **Accountants and shopkeepers** importing supplier price lists and invoices.
- **Teachers** turning result sheets into spreadsheets for averages and grades.
- **Students** pulling data tables from reports for a project or assignment.
- **Anyone** tracking expenses from bank or card statements.

## FAQ

**Is it free, and do I need Excel installed?**
It is free with no sign-up. You do not need Excel to convert; the `.xlsx` file opens in Google Sheets, LibreOffice and other spreadsheet apps.

**Does it keep colours, fonts and cell borders?**
No. It extracts the data (text and numbers), which is the part you need for calculations. Formatting is left behind.

**Will it convert charts or images?**
No. Only text is extracted. To save images from a PDF, use the [PDF Image Extractor](/pdf-image-extractor/).

**Why does each page become a separate sheet?**
It keeps the original structure clear and makes it easy to find a specific page. You can combine sheets in a minute when you need one table.

## Related tools

- [PDF OCR](/pdf-ocr/) to prepare scanned PDFs for conversion.
- [PDF Splitter](/pdf-splitter/) to pick out only the pages you need.
- [PDF to Word](/pdf-to-word/) when the PDF is mostly paragraphs rather than tables.
"""),
dict(slug='convert-pdf-to-jpg-high-quality', title='Convert PDF to JPG in High Quality: Save Every Page as an Image', date='2026-11-10',
 desc='Convert PDF pages to sharp JPG images for free. Choose screen, print or ultra quality and download every page at once as a ZIP.',
 tools=['pdf-to-jpg', 'pdf-to-png', 'pdf-splitter'], md="""
Some places simply will not take a PDF. An online form wants a JPG of your certificate. WhatsApp status and Instagram need an image. A slide app wants a picture of one page from a report. The fix is to **convert the PDF to JPG**, and to do it at a quality that still looks sharp when someone zooms in.

DoraPDF's [PDF to JPG Converter](/pdf-to-jpg/) turns every page of a PDF into its own image, right in your browser. This guide explains the quality settings, when to choose PNG instead, and how to get just the page you need.

## What you get

- **One JPG per page**, named like `report-page1.jpg`, `report-page2.jpg`.
- For multi-page PDFs, a **single ZIP file** with all the pages, so you can download everything in one tap.
- The first pages are also listed individually, so you can grab one or two without unzipping anything.

Pages are drawn on a white background, so the JPGs look just like the printed page.

## Picking the right quality

The **Quality** setting controls how many pixels each page gets.

| Setting | Good for | File size |
|---|---|---|
| **Normal (screen)** | WhatsApp, email previews, quick sharing | Smallest |
| **High (print)** | Forms, printing, zooming into small text (default) | Medium |
| **Ultra** | Posters, fine diagrams, maps, tiny print | Largest |

For most people **High** is the right balance: small print stays readable and the files are still easy to email. Choose **Ultra** if the page has very small text or detailed drawings that need to stay readable when enlarged. Choose **Normal** when you just need something light to send over a slow connection.

## How to convert, step by step

1. Open [PDF to JPG](/pdf-to-jpg/).
2. Add your PDF.
3. Choose the **Quality**.
4. Press **Convert now**.
5. Download the ZIP for all pages, or tap individual page images.

On a phone, the ZIP may open in your Files app. Tap it to extract the images, then share or save them to your gallery.

## Only need one page?

Converting a 40-page report to get page 12 works, but it is wasteful. A cleaner route:

1. Use the [PDF Splitter](/pdf-splitter/) in "Extract pages" mode and type `12`.
2. Convert that one-page PDF to JPG.

You get a single image without digging through a ZIP.

## JPG or PNG?

Both are images, but they suit different pages.

- **JPG** is smaller and perfect for scanned pages, photos and most everyday documents.
- **PNG** is lossless. It keeps sharp edges on text, line charts, logos and screenshots without any compression haze, at the cost of bigger files.

If your PDF is mostly crisp text or diagrams and file size is not a concern, try [PDF to PNG](/pdf-to-png/). For everything else, JPG is the practical choice.

## Practical examples

- **Job or admission forms** that ask for "JPG of degree" or "scan of CNIC": convert the scanned PDF page at High quality.
- **Social media:** turn a one-page flyer or event poster into a JPG for Facebook, Instagram or WhatsApp status.
- **Presentations:** drop a page from a research paper into a slide as an image.
- **Thumbnails:** create a preview image of a report's cover page for a website or shared drive.

## Common problems and fixes

**The image looks blurry when I zoom in.** Convert again with **High** or **Ultra**. Normal is designed for screens, not zooming.

**The JPG is too big for the form's upload limit.** Use Normal quality, or compress the image afterwards with the [Image Compressor](/image-compressor/). If the form needs a specific pixel size, use the [Image Resizer](/image-resizer/).

**My PDF won't open.** Password-protected PDFs need to be unlocked first with [Unlock PDF](/unlock-pdf/), if you are allowed to remove the password.

**Conversion is slow on a long PDF.** Every page is drawn at full quality, so 100+ pages take a while, especially at Ultra. Split the PDF or use a lower quality for large files.

## Privacy

The PDF is opened and drawn inside your browser. Nothing is **uploaded** to DoraPDF, which matters when the document is an ID card, a mark sheet or a signed contract.

## FAQ

**Is there a page limit?**
There is no fixed page limit. Very long documents simply take more time and memory.

**Can I convert several PDFs at once?**
The tool converts one PDF per run. Repeat for each file.

**Will the colours change?**
No. Pages are rendered as they appear, on a white background.

**Can I turn the JPGs back into a PDF later?**
Yes. Use [Images to PDF](/images-to-pdf/) to combine them into a new PDF in any order.

## Related tools

- [PDF to PNG](/pdf-to-png/) for lossless images of text-heavy pages.
- [PDF Splitter](/pdf-splitter/) to pick out the exact page first.
- [Image Compressor](/image-compressor/) when the JPG is above an upload limit.
"""),
dict(slug='convert-webp-avif-heic-to-jpg-png', title='Convert WebP, AVIF and HEIC Photos to JPG or PNG (Free, Batch, In Your Browser)', date='2026-11-10',
 desc='Can\'t open a WebP, AVIF or HEIC image? Convert it to JPG or PNG for free, several files at once, with nothing uploaded. Plus WebP to SVG.',
 tools=['webp-to-jpg', 'webp-to-png', 'avif-to-jpg', 'avif-to-png', 'heic-to-png', 'webp-to-svg'], md="""
You save a picture from a website and it arrives as `.webp`. A friend's iPhone sends `.heic`. A newer site serves `.avif`. Then the form you are filling in, or your old photo editor, or a printing shop, says it only accepts **JPG or PNG**.

These newer formats are good at keeping files small, but support outside browsers and phones is still patchy. The simple answer is to **convert WebP, AVIF or HEIC to JPG or PNG**. DoraPDF has a small converter for each case, and they all work the same way.

## Which converter do you need?

| You have | You need | Tool |
|---|---|---|
| WebP | JPG | [WebP to JPG](/webp-to-jpg/) |
| WebP | PNG | [WebP to PNG](/webp-to-png/) |
| AVIF | JPG | [AVIF to JPG](/avif-to-jpg/) |
| AVIF | PNG | [AVIF to PNG](/avif-to-png/) |
| HEIC (iPhone) | PNG | [HEIC to PNG](/heic-to-png/) |
| WebP | SVG (vector) | [WebP to SVG](/webp-to-svg/) |

For iPhone photos to JPG specifically, we have a separate guide: [how to convert HEIC to JPG](/blog/heic-to-jpg-iphone-photos/).

## JPG or PNG: choose before you convert

This decision matters more than the tool.

**Pick JPG when:**

- It is a photograph (people, places, food, products).
- You need a small file for email, WhatsApp or an upload form.
- The image has no transparent areas.

**Pick PNG when:**

- The image has a **transparent background**, like a logo, sticker or icon. JPG cannot store transparency, so transparent areas become **white**.
- It is a screenshot, chart or graphic with sharp text and flat colours.
- You plan to edit it further and want no quality loss.

Many WebP files from websites are logos and icons with transparency, so if you see a checkerboard background in your image viewer, choose PNG.

## How to convert, step by step

All five raster converters share the same simple screen:

1. Open the tool you need from the table above.
2. Drop in your files. You can add **many at once** for batch conversion.
3. For JPG output, set the **Quality** slider (from 40 to 100; the default 92 looks virtually identical to the original).
4. Press **Convert now**.
5. Download each converted file. The original name is kept, with the new extension.

The image keeps its original pixel dimensions. If you also need it smaller, run the result through the [Image Resizer](/image-resizer/) or [Image Compressor](/image-compressor/).

## Quick notes on each format

**WebP** is Google's web image format, used by many sites to load pages faster. Browsers open it easily, but some desktop apps, government portals and print shops do not.

**AVIF** is newer and compresses even more efficiently. Because DoraPDF decodes it with your browser, you need a reasonably up-to-date browser that can display AVIF. Current versions of Chrome, Edge, Firefox and Safari can.

**HEIC** is the default camera format on iPhones. The converter includes its own HEIC decoder, so it works even in browsers that cannot show HEIC images by themselves.

## Turning a WebP into an SVG vector

[WebP to SVG](/webp-to-svg/) is a different kind of tool. Instead of changing the file type, it **traces** the shapes and colours of the image into vector paths, which can be scaled to any size without pixels.

- Choose a **Detail** level: **High detail**, **Balanced** or **Simple / logo**.
- It converts one image at a time and shows a preview of the SVG.
- It works best on logos, icons, flat illustrations and simple drawings. Photos turn into a posterised, painted look, because a vector can only use a limited set of colour areas.

For logos, start with **Simple / logo**. It uses fewer colours and smooths out noise, giving cleaner shapes that are easier to edit in a vector app.

## Common problems and fixes

**The transparent background turned white.** You converted to JPG. Convert the original again with the PNG version of the tool.

**The AVIF file won't load.** Your browser may be too old to read AVIF. Update the browser or try another one, then convert again.

**The JPG is still too large for a form.** Lower the quality slider to around 70–80, or use the [Image Compressor](/image-compressor/) afterwards.

**The SVG looks blotchy.** Try **High detail** for more colours, or use a cleaner, larger source image. Tracing small, compressed images gives rough edges.

## Privacy

Every conversion runs in your browser. Your images are **not uploaded** to DoraPDF, which is useful when the photos are personal or the graphics are client work.

## FAQ

**Is there a limit on how many images I can convert?**
No fixed limit. You can add a batch of files at once; very large batches simply take longer.

**Does converting to JPG reduce quality?**
JPG uses compression, but at the default quality of 92 the difference is very hard to see. PNG output is lossless.

**Can I go the other way and make WebP files?**
Yes, for PNG images: [PNG to WebP](/png-to-webp/) creates lighter files for your own website.

**Will the photo's size in pixels change?**
No. The converters keep the original width and height.

## Related tools

- [Image Compressor](/image-compressor/) to shrink converted files.
- [Image Resizer](/image-resizer/) for exact dimensions.
- [Images to PDF](/images-to-pdf/) to combine converted pictures into one document.
"""),
dict(slug='split-pdf-extract-pages-free', title='How to Split a PDF and Extract Pages for Free (Ranges, Single Pages, Every Page)', date='2026-11-10',
 desc='Split a PDF into separate pages or extract a page range like 1-3, 7 into a new PDF. Free, fast and done in your browser without uploading.',
 tools=['pdf-splitter', 'pdf-merger', 'delete-pdf-pages'], md="""
You have a 90-page PDF and you only need chapter 3. Or a scanned bundle of documents where each page should be its own file. Or an exam paper where only pages 2 to 5 belong to your section. In all of these cases you want to **split the PDF** and keep just the pages that matter.

DoraPDF's free [PDF Splitter](/pdf-splitter/) has two modes that cover nearly every situation. Here is how each one works, with examples you can copy.

## The two ways to split

**1. Extract pages into one PDF.** You type which pages you want, and they are copied into a single new PDF named like `report-pages.pdf`. Use this when you want a smaller document made from part of a larger one.

**2. Split every page into its own PDF.** Every page becomes a separate one-page PDF. You get them all in one ZIP file, `report-split.zip`, and the first ten pages are also listed individually for quick downloads. Use this when each page is a different document, such as a stack of scanned receipts.

## Writing page ranges

In extract mode, the **Pages** box understands simple ranges:

| You type | You get |
|---|---|
| `5` | Page 5 only |
| `1-3` | Pages 1, 2 and 3 |
| `1-3, 7` | Pages 1, 2, 3 and 7 |
| `2, 4, 6, 8` | Those four pages |
| `10-20, 25-30` | Two blocks of pages |

A few details worth knowing:

- Pages always come out in their **original order**. Typing `7, 1` gives page 1 then page 7. To change the order, extract each part as its own PDF, then add the parts to the [PDF Merger](/pdf-merger/) in the order you want.
- A page listed twice is only included once.
- Page numbers outside the document are ignored. If nothing valid is left, you will see "Enter pages between 1 and N", where N is the page count.

## Splitting a PDF, step by step

1. Open the [PDF Splitter](/pdf-splitter/).
2. Add your PDF.
3. Choose the **Mode**: "Extract pages into one PDF" or "Split every page into its own PDF".
4. In extract mode, type the pages, for example `1-3, 7`.
5. Press **Split**.
6. Download the new PDF or the ZIP.

Tip: check the page numbers in your PDF viewer's page counter, not the numbers printed on the pages. A book's "page 1" is often the 15th page of the file because of the cover and contents pages.

## Everyday examples

- **Submit only the relevant part:** a university portal asks for "your transcript", but the PDF also has an admission letter. Extract the transcript pages.
- **Share a chapter:** send students pages `45-62` of a reference book instead of the whole 300 pages.
- **Separate scanned documents:** scanned your CNIC, degree and experience letter in one go? Split every page and rename each file.
- **Shrink an email attachment:** extracting the five pages someone actually needs often makes the file small enough to attach without compression.
- **Prepare for conversion:** pull out a single table page before using [PDF to Excel](/pdf-to-excel/).

## Splitting vs. deleting pages

These two do opposite jobs from the same starting point:

- **Splitting/extracting** answers "which pages do I want to **keep**?"
- **Deleting** answers "which pages do I want to **remove**?"

If you want to keep 95 pages out of 100, it is easier to remove the five with [Delete PDF Pages](/delete-pdf-pages/) than to type four ranges.

## Common problems and fixes

**"Enter pages between 1 and N."** The pages box is empty or the numbers are outside the document. Check the page count and retype, for example `1-4`.

**The ZIP won't open on my phone.** Most phones open ZIP files in their Files app. Alternatively, download the individual page PDFs listed under the ZIP.

**Only ten single pages are shown.** That is just the quick list. The ZIP always contains every page.

**I need the pages in a different order.** Extract each part separately, then add the files to the [PDF Merger](/pdf-merger/) in the order you want. They are merged in the order you add them.

## Is the quality affected?

No. Pages are copied as they are, not re-rendered, so text stays selectable, images keep their quality, and the result looks exactly like the original pages.

## Privacy

Your PDF is split in your browser and **never uploaded** to DoraPDF. You can safely split contracts, bank statements, medical files and exam papers.

## FAQ

**Is the PDF Splitter free?**
Yes, with no account, no watermark and no daily limit.

**Can I split a password-protected PDF?**
If the PDF needs a password to open, unlock it first with [Unlock PDF](/unlock-pdf/), provided you have the right to.

**Can I split into chunks, like every 10 pages?**
Use extract mode a few times: `1-10`, then `11-20`, and so on. Each run gives you one part.

**Can I extract pages on my phone?**
Yes. The tool works in mobile browsers on Android and iPhone.

## Related tools

- [PDF Merger](/pdf-merger/) to combine or reorder extracted parts.
- [Delete PDF Pages](/delete-pdf-pages/) to remove a few pages instead.
- [PDF Compressor](/pdf-compressor/) if the extracted file is still too big to send.
"""),
dict(slug='add-text-to-pdf-free-online', title='Add Text to a PDF Free Online: Fill in Forms Without Printing', date='2026-11-10',
 desc='Type on any PDF for free. Click where you want text, pick the size and colour, and save. Ideal for filling simple forms without printing them.',
 tools=['pdf-editor', 'sign-pdf', 'redact-pdf'], md="""
Someone emails you an application form as a PDF and asks you to "fill it and send it back". The usual routine is print, write by hand, scan, and hope the scan is readable. There is a quicker way: **add text to the PDF directly**, on your computer or phone, and save a clean typed copy.

DoraPDF's free [PDF Editor](/pdf-editor/) lets you click anywhere on a page and type. It is simple by design, and this guide shows how to get neat, well-aligned results with it.

## What the PDF Editor does

- **Adds new text** anywhere on any page: names, dates, addresses, ticks, short answers.
- Lets you set the **font size** and **colour** for each piece of text.
- Works across **all pages**: switch page, add more text, and everything is saved together.
- Saves a new file named like `form-edited.pdf`, leaving your original untouched.

What it does **not** do: it does not change or delete text that is already in the PDF. It places new text on top. (To hide existing content permanently, see the [Redact PDF](/redact-pdf/) tool.)

## Filling in a form, step by step

1. Open the [PDF Editor](/pdf-editor/) and add your PDF. The first page appears.
2. In the **Text** box, type what you want to add, for example your full name.
3. Set the **Size** (14 is the default; 10 to 12 suits most form fields) and choose a **Color**.
4. Click on the page where the text should go. It appears instantly.
5. Type the next answer in the Text box and click on the next field. Repeat.
6. Use the **Page** menu to move to other pages and keep going.
7. Press **Save PDF** to download the finished file.

Placed something in the wrong spot? **Undo last** removes the most recent piece of text, then you can click again.

## Getting the alignment right

The point where you click becomes the **bottom-left of the text**, where the letters sit on the line. So for a form field with an underline:

- Click **just above the line**, at the left edge of the blank space.
- If the text lands too high or low, press Undo last and click a little lower or higher.
- Keep the same size throughout the form so it looks tidy.

For a tick box, type `X` or a tick-like `v` at a slightly smaller size and click inside the box.

## Multi-line answers

Each click places a **single line** of text. For an address or a short paragraph, add it one line at a time:

1. Type the first line, click at the start of the field.
2. Type the second line, click directly below the first.

Keeping your clicks at the same horizontal position keeps the lines aligned.

## Things to know before you start

- **Font:** text is added in a clean standard sans-serif font (Helvetica).
- **Language:** that font supports English and Western European letters. **Urdu, Arabic, Hindi and other non-Latin scripts cannot be saved** with this editor, so write those answers in English letters, or fill them by hand after printing.
- **Text only:** the editor does not add images or signatures. For a signature, save your edited PDF and then open it in [Sign PDF](/sign-pdf/), where you can draw or type a signature and place it.
- **Protected PDFs:** if a PDF needs a password to open, unlock it first with [Unlock PDF](/unlock-pdf/), provided you have permission.

## A typical workflow for job and admission forms

1. **Fill** the text fields with the PDF Editor.
2. **Sign** the saved file with [Sign PDF](/sign-pdf/).
3. **Shrink** it with the [PDF Compressor](/pdf-compressor/) if the portal has a size limit.
4. **Check** the final PDF on your phone or computer before sending: zoom in on each field.

## Common problems and fixes

**"Upload a PDF first."** You pressed Save before adding a file. Add your PDF, then place your text.

**My text doesn't appear in the saved PDF, or saving fails.** Check for non-English characters such as Urdu letters or special symbols. Replace them with plain English letters and save again.

**The text is too big for the box.** Undo, lower the Size to 10 or 11, and click again.

**The text is hard to read on a coloured background.** Pick a darker colour, or black, from the colour picker.

**I need to edit the original wording of the document.** This tool adds text; it does not rewrite existing text. If you need to rework the content, convert the PDF with [PDF to Word](/pdf-to-word/), edit it there, and save it as a PDF again.

## Privacy

Your PDF is opened, edited and saved entirely in your browser. It is **not uploaded** to DoraPDF. That is important for forms that contain your CNIC number, address, phone number or bank details.

## FAQ

**Is the PDF Editor free?**
Yes. No sign-up and no watermark.

**Does it work on mobile?**
Yes. Tap on the page to place text. A larger screen makes precise placement easier, so a tablet or computer is more comfortable for long forms.

**Can I move text after placing it?**
Not by dragging. Use Undo last and click in the new position.

**Will the original PDF be changed?**
No. Your edits are saved into a new file and the original stays as it was.

**Can I add text to several pages?**
Yes. Choose each page from the Page menu, add your text, and save once at the end.

## Related tools

- [Sign PDF](/sign-pdf/) to add your signature after filling the form.
- [Redact PDF](/redact-pdf/) to black out information before sharing.
- [PDF Compressor](/pdf-compressor/) to meet upload size limits.
"""),
dict(slug='assignment-helper-for-students', title='DoraPDF Assignment Helper: an AI study tool for students, teachers and professionals', date='2026-11-09',
 desc='What the DoraPDF Assignment Helper is for, how to use it to study smarter, and how to use AI responsibly with your school\'s rules.',
 tools=['pdf-to-word','image-to-text','pdf-ocr'], md="""
The **Assignment Helper** is DoraPDF's AI study tool. It is built to **help you learn and plan your own work**, not to do the work for you. You type a topic and it gives you a clear starting point: an outline, key points, figures and a list of sources to research, in Word or PowerPoint.

## Who it is for

- **Students** who want to understand a topic faster, see how a good assignment is structured, and find where to start researching.
- **Teachers** who want a quick outline or slide deck for a lesson, which they then adapt for their class.
- **Professionals** who need a first version of a presentation for a meeting, training or pitch.

## What you get

- **Assignment drafts in Word:** title, numbered headings, short sections, figures and suggested references in APA, MLA, Harvard, Chicago or IEEE style.
- **Presentations in PowerPoint:** a title slide, 5–20 content slides with short bullet points, speaker notes and a references slide.
- **Free images with credit:** optional pictures from Wikimedia Commons and Openverse, with the author and licence written under each one.
- **Your look:** theme colours, a soft background or your own background image.

## How to use it the right way

AI is a great study partner, but it is not a replacement for your own thinking. We recommend this simple routine:

1. **Generate a draft** to see the structure and the main ideas.
2. **Read and check** every fact and every reference. AI can make mistakes, and some references may be incomplete.
3. **Research the sources** yourself and add what you learn.
4. **Rewrite in your own words**, add your own examples and opinions, and format it the way your teacher asked.
5. **Follow your school's rules.** Many schools allow AI for brainstorming and outlines but not for writing the final submission. If you are unsure, ask your teacher.

## What the Assignment Helper is not

It is **not a submission service**. We do not promise "undetectable" text and we never encourage handing in AI-generated work as your own where it is not allowed. Our [Terms](/terms/) say this clearly.

## Plans

New accounts get a **3-day free trial** with 3 assignment drafts and 3 presentations. After that you can choose **Pro** or **Max** on the [pricing section](/#pricing). All 160+ file tools on DoraPDF, such as [PDF to Word](/pdf-to-word/), [Image to Text](/image-to-text/) and [PDF OCR](/pdf-ocr/), stay **free forever**, without an account.

## Privacy

You sign in with Google so your plan can follow you. Your topic is sent to our AI provider only to create your document; we do not keep the generated text on our servers. If you choose, a copy is saved to **your own Google Drive** in a "DoraPDF" folder. Read more in our [Privacy policy](/privacy/).
"""),
dict(slug='convert-pdf-to-word-free', title='How to Convert PDF to Word for Free (Phone & PC)', date='2026-11-06',
 desc='A step-by-step guide to turning a PDF into an editable Word document for free, without sign-up or watermarks.',
 tools=['pdf-to-word','word-to-pdf','pdf-to-txt'], md='''
PDFs are great for sharing because they look the same everywhere — but that also makes them hard to edit. If you need to change a CV, fix a typo in an assignment or reuse text from a report, the easiest route is to convert the PDF into a Word document first.

## The quick way (under a minute)

1. Open the [PDF to Word converter](/pdf-to-word/) on your phone or computer.
2. Drop your PDF into the upload box, or tap it to choose a file.
3. Press **Convert now**.
4. Download the `.docx` file and open it in Microsoft Word, Google Docs or WPS Office.

That's it. There's no account to create, no email to enter and no watermark on the result.

## Will my formatting be kept?

Yes. By default DoraPDF uses **Keep original layout** mode: every page keeps its design, columns, colours, lines and images, and the text stays fully editable in Word, with the same fonts, sizes, bold and colours where possible. It works well for CVs, letters, reports and assignments.

If you only need the words (for example to paste into another document), switch the **Layout** option to **Text only** for a simple, flowing document.

## What about scanned PDFs?

A scanned PDF is really just a photo of a page. There's no text inside it to extract, so a normal converter returns an empty document. To edit a scanned page you need OCR (optical character recognition), which reads the letters from the image. Our OCR tool is on the way; until then, retyping short scans is often quickest.

## Is it safe to convert private documents?

Most online converters upload your file to their servers. DoraPDF doesn't — the conversion runs inside your browser, on your own device. Your bank statement or ID copy never leaves your phone or laptop.

## Going the other way

Finished editing? Use [Word to PDF](/word-to-pdf/) to turn your document back into a PDF before you email or submit it. And if you only need the raw text — for example to paste into ChatGPT — try [PDF to TXT](/pdf-to-txt/).

## Tips for the best results

- **Start from the original PDF.** A PDF exported from Word or Google Docs converts far better than one that was printed and scanned.
- **Check fonts after converting.** If your PDF used a special font, Word may substitute a similar one. Select all and pick a font you like.
- **Fix spacing with Find & Replace.** Replace double spaces with single spaces in one click.
'''),
dict(slug='compress-pdf-for-email', title='How to Compress a PDF for Email (Under 1 MB)', date='2026-11-06',
 desc='Shrink large PDF files so they fit email and upload limits — free, private and without losing readability.',
 tools=['pdf-compressor','image-compressor','pdf-splitter'], md='''
Gmail lets you attach up to 25 MB, many university portals stop at 2–5 MB, and government forms often ask for files **under 1 MB**. If your PDF is too big, here's how to shrink it without making it unreadable.

## Step by step

1. Open the free [PDF Compressor](/pdf-compressor/).
2. Drop your PDF in.
3. Choose a mode:
   - **Smart** keeps the text selectable and searchable. Best for documents exported from Word or other software.
   - **Strong** turns each page into an optimised image. Best for scanned documents and PDFs full of photos — this gives the biggest savings.
4. Pick a quality level and press **Compress**. DoraPDF shows you exactly how many percent smaller the new file is.

## Why are some PDFs so big?

Almost always it's the images. A single photo from a modern phone can be 3–5 MB. Scan ten pages at full resolution and you quickly have a 40 MB file, even though the text itself takes up almost no space.

## Getting under 1 MB

If Smart mode doesn't shrink it enough, try this order:

1. **Strong mode, Balanced quality.** Usually enough for a 10–20 page scan.
2. **Strong mode, Smallest quality.** Text is still readable on screen and when printed.
3. **Split it.** If a portal allows several uploads, use the [PDF Splitter](/pdf-splitter/) to break a long document into parts.

## Compress images before you make the PDF

Creating a PDF from photos? Run them through the [Image Compressor](/image-compressor/) first and set a maximum width of 1920 px. Your final PDF will be a fraction of the size.

## Is compression safe?

With DoraPDF the whole process happens in your browser. Your PDF is never uploaded, so confidential documents stay on your device.
'''),
dict(slug='merge-pdf-files', title='How to Merge PDF Files into One (Free, No Sign-up)', date='2026-11-06',
 desc='Combine multiple PDFs into a single file on your phone or computer in a few clicks.',
 tools=['pdf-merger','images-to-pdf','delete-pdf-pages'], md='''
Need to submit one file but have five? Teachers, employers and visa portals often ask for a single PDF. Here's the fastest way to combine them.

## How to merge PDFs

1. Open the [PDF Merger](/pdf-merger/).
2. Add all your PDF files — you can drop them in together.
3. Check the order. Files are joined from top to bottom. Remove any you don't need with ✕.
4. Press **Merge PDFs** and download `merged.pdf`.

## Merging on a phone

It works the same way on Android and iPhone. Tap the upload box, choose your files from Files, Downloads or Google Drive, and download the merged PDF when it's ready.

## Have photos as well as PDFs?

Turn the photos into a PDF first with [Images to PDF](/images-to-pdf/), then merge that file with the rest. If you photographed paper documents, use [Scan to PDF](/scan-to-pdf/) instead — it crops and cleans each page so it looks properly scanned.

## Remove pages you don't need

After merging, you might find a blank page or a duplicate. Use [Delete PDF Pages](/delete-pdf-pages/) to remove pages by number, for example `2, 5-6`.

## Does merging reduce quality?

No. Pages are copied exactly as they are, so text stays sharp and selectable and images keep their original quality.
'''),
dict(slug='scan-documents-with-phone', title='How to Scan Documents to PDF With Your Phone (No App Needed)', date='2026-11-06',
 desc='Use your phone camera to create clean, cropped, CamScanner-style PDF scans right in your browser.',
 tools=['scan-to-pdf','pdf-compressor','pdf-merger'], md='''
You don't need a scanner — or even a scanning app — to turn paper into a clean PDF. Your phone's camera and a browser are enough.

## How to scan with DoraPDF

1. Open [Scan to PDF](/scan-to-pdf/) on your phone.
2. Tap **Open camera** and take a photo of the page. Add more pages the same way.
3. **Drag the four pink corners** to the edges of the paper. DoraPDF straightens the page automatically, even if you took the photo at an angle.
4. Choose a filter:
   - **Black & white** — crisp text, perfect for printed pages and notes.
   - **Magic color** — brightens the paper and boosts colours. Best for receipts and forms.
   - **Grayscale** or **Lighten** for softer results.
5. Press **Download PDF**.

## Tips for a perfect scan

- **Use daylight.** Stand near a window and avoid using the flash, which causes glare.
- **Dark background, light paper.** A wooden table or dark cloth makes the page edges easy to see.
- **Hold the phone flat above the page.** You can still fix small angles with the corner handles.
- **Fill the frame.** The more of the photo the page covers, the sharper the final scan.

## Make the file smaller

Scans can be large. If you need to email or upload the PDF, choose **Small file** quality before downloading, or run it through the [PDF Compressor](/pdf-compressor/) afterwards.

## Is it private?

Yes. Your photos are processed on your phone and never uploaded — important when you're scanning ID cards, bank documents or contracts.
'''),
dict(slug='heic-to-jpg-iphone-photos', title='HEIC to JPG: How to Convert iPhone Photos (Free)', date='2026-11-06',
 desc="Can't open iPhone photos on Windows or upload them to a website? Here's how to convert HEIC to JPG in seconds.",
 tools=['heic-to-jpg','heic-to-png','heic-to-pdf'], md='''
iPhones save photos as **HEIC** by default. The format saves storage space, but many Windows PCs, Android phones, websites and government portals can't open it. Converting to JPG fixes that.

## Convert HEIC to JPG

1. Open the [HEIC to JPG converter](/heic-to-jpg/).
2. Add one or more HEIC photos.
3. Press **Convert** and download your JPG files.

Need transparency or lossless quality? Use [HEIC to PNG](/heic-to-png/). Need a document? [HEIC to PDF](/heic-to-pdf/) puts all your photos into one PDF.

## HEIC vs JPG — what's the difference?

| | HEIC | JPG |
|---|---|---|
| File size | About half of JPG | Larger |
| Compatibility | Apple devices, some apps | Works everywhere |
| Quality | Excellent | Excellent at high quality |

## Stop your iPhone from saving HEIC

Go to **Settings → Camera → Formats** and choose **Most Compatible**. New photos will be saved as JPG. Photos you've already taken stay HEIC, so convert those with the tool above.

## Is quality lost?

At the default quality setting (92%) the difference is invisible to the eye. Increase the quality slider if you plan to print large.
'''),
dict(slug='apa-vs-mla-vs-harvard', title='APA vs MLA vs Harvard: Citation Styles Explained for Students', date='2026-11-06',
 desc='A simple guide to the three most common referencing styles, with examples of in-text citations and reference lists.',
 tools=['word-counter','pdf-to-word','text-formatter'], md='''
Your teacher says "use APA" — or MLA, or Harvard — and suddenly referencing feels complicated. All three styles do the same job: show where your information came from. They just format it differently.

## APA (7th edition)

Used in psychology, education, business and the social sciences. APA focuses on **author and date**, because recent research matters in these subjects.

- **In-text:** (Khan, 2023) or Khan (2023) argues that…
- **Reference list:** Khan, A. (2023). *Climate change and agriculture in South Asia*. Oxford University Press.

## MLA (9th edition)

Used in English literature, languages and the humanities. MLA focuses on **author and page number**.

- **In-text:** (Khan 45)
- **Works Cited:** Khan, Ali. *Climate Change and Agriculture in South Asia*. Oxford UP, 2023.

## Harvard

Popular in UK, Australian and many Pakistani universities. Very similar to APA, with small punctuation differences.

- **In-text:** (Khan 2023, p. 45)
- **Reference list:** Khan, A. (2023) *Climate change and agriculture in South Asia*. Oxford: Oxford University Press.

## Quick comparison

| | APA | MLA | Harvard |
|---|---|---|---|
| In-text | (Author, Year) | (Author Page) | (Author Year, p.) |
| List title | References | Works Cited | Reference list |
| Common in | Social sciences | Humanities | UK / many universities |

## Tips that save marks

- **Be consistent.** Mixing styles loses more marks than small mistakes.
- **Order the list alphabetically** by the author's surname.
- **Record sources as you go** — finding a website again later is painful.
- **Check the word count.** Many universities don't count references; use the [Word Counter](/word-counter/) on your main text only.
'''),
dict(slug='reduce-image-size-without-losing-quality', title='How to Reduce Image Size Without Losing Quality', date='2026-11-06',
 desc='Make photos smaller for websites, email and upload forms while keeping them sharp.',
 tools=['image-compressor','image-resizer','png-to-webp'], md='''
Big images slow down websites, bounce off email limits and get rejected by upload forms. The good news: most photos can be **50–80% smaller** with no visible difference.

## 1. Resize to the size you actually need

A modern phone photo is around 4000 pixels wide, but most screens show images at 1920 px or less. Use the [Image Resizer](/image-resizer/) to set a width:

- **Website hero image:** 1920 px
- **Blog image:** 1200 px
- **Instagram post:** 1080 px
- **Profile photo / thumbnail:** 400–800 px

Halving the width cuts the file size to about a quarter.

## 2. Compress

Next, run the photo through the [Image Compressor](/image-compressor/). **Balanced** is the sweet spot for most photos. Try **Strong** for thumbnails.

## 3. Use the right format

- **JPG** for photos.
- **PNG** for logos, screenshots and images with transparency.
- **WebP** for websites — usually 25–35% smaller than JPG at the same quality. Convert with [PNG to WebP](/png-to-webp/).

## What "without losing quality" really means

All compression removes some data. The trick is to remove only what the eye can't see. At around 70–85% quality, almost nobody can tell the difference — but the file is a fraction of the size.

## Privacy bonus

DoraPDF resizes and compresses images in your browser. Your photos are never uploaded, which matters for personal pictures and ID scans.
'''),
dict(slug='jpg-vs-png-vs-webp', title='JPG vs PNG vs WebP: Which Image Format Should You Use?', date='2026-11-06',
 desc='The differences between the three most common image formats and when to use each one.',
 tools=['jpg-to-png','png-to-jpg','png-to-webp','webp-to-jpg'], md='''
Choosing the wrong image format makes files bigger than they need to be — or makes them look blurry. Here's a simple guide.

## JPG (JPEG)

- **Best for:** photos.
- **Pros:** small files, opens everywhere.
- **Cons:** no transparency; repeated saving slowly reduces quality; text and sharp edges can look fuzzy.

## PNG

- **Best for:** logos, icons, screenshots, graphics with text, anything needing a transparent background.
- **Pros:** lossless and pin-sharp, supports transparency.
- **Cons:** photos as PNG are very large.

## WebP

- **Best for:** websites.
- **Pros:** smaller than JPG for photos and smaller than PNG for graphics; supports transparency.
- **Cons:** some older software can't open it.

## Cheat sheet

| Situation | Format |
|---|---|
| Phone photo for email | JPG |
| Logo on a website | PNG or WebP |
| Screenshot with text | PNG |
| Images for your own website | WebP |
| Uploading to a government portal | JPG |

## Converting between formats

- [JPG to PNG](/jpg-to-png/) — for editing and design work.
- [PNG to JPG](/png-to-jpg/) — to make large PNG photos smaller.
- [PNG to WebP](/png-to-webp/) — to speed up a website.
- [WebP to JPG](/webp-to-jpg/) — when a website or app won't accept WebP.
'''),
dict(slug='make-qr-code-for-business', title='How to Make a QR Code for Your Business (WiFi, WhatsApp, Links)', date='2026-11-06',
 desc='Create free QR codes that let customers join your WiFi, message you on WhatsApp or open your website.',
 tools=['qr-code-generator','barcode-generator','link-shortener'], md='''
QR codes are everywhere — restaurant menus, shop counters, visiting cards. They save customers from typing long links and phone numbers. Here's how to make one for free.

## Create your QR code

1. Open the [QR Code Generator](/qr-code-generator/).
2. Choose a type:
   - **Link / text** — your website, Instagram, Google Maps location or menu.
   - **WiFi network** — guests scan and connect without asking for the password.
   - **WhatsApp chat** — opens a chat with your number, with an optional pre-written message.
   - **Phone number** — calls you in one tap.
3. Pick colours that match your brand (keep the code dark on a light background).
4. Download the PNG and print it or add it to your designs.

## Ideas for shops and restaurants

- A **WhatsApp QR** on the counter: "Scan to order on WhatsApp".
- A **WiFi QR** on each table.
- A **Google review link** QR on receipts.
- A **menu link** QR on the door.

## Printing tips

- **Minimum size:** 2 × 2 cm for cards, 10 × 10 cm for posters.
- **Contrast matters:** dark code, light background. Avoid light-on-dark.
- **Leave a white border** around the code.
- **Always test** with two different phones before printing 500 copies.

## Do they expire?

No. DoraPDF creates static QR codes — the information is stored inside the code itself, so it works forever and there's no subscription.

Need a product barcode instead? Try the [Barcode Generator](/barcode-generator/).
'''),
dict(slug='how-to-calculate-gpa', title='How to Calculate Your GPA (With Easy Examples)', date='2026-11-06',
 desc='Understand grade points and credit hours and calculate your semester GPA step by step.',
 tools=['gpa-calculator','percentage-calculator','word-counter'], md='''
GPA (Grade Point Average) turns your letter grades into a single number, usually on a 4.0 scale. It's what scholarships, universities and many employers look at first.

## The formula

**GPA = total grade points ÷ total credit hours**

Grade points for one course = grade value × credit hours.

## Common 4.0 scale

| Grade | Points |
|---|---|
| A / A+ | 4.0 |
| A- | 3.67 |
| B+ | 3.33 |
| B | 3.0 |
| B- | 2.67 |
| C+ | 2.33 |
| C | 2.0 |
| D | 1.0 |
| F | 0 |

*Scales differ slightly between universities — always check your handbook.*

## Worked example

| Course | Grade | Credits | Points |
|---|---|---|---|
| Calculus | A (4.0) | 3 | 12.0 |
| Physics | B+ (3.33) | 4 | 13.32 |
| English | A- (3.67) | 2 | 7.34 |
| Programming | B (3.0) | 3 | 9.0 |
| **Total** | | **12** | **41.66** |

GPA = 41.66 ÷ 12 = **3.47**

## The faster way

Use the free [GPA Calculator](/gpa-calculator/): add your courses, pick each grade and enter the credit hours. Your GPA updates as you type, and you can add as many courses as you need.

## GPA vs CGPA

- **GPA** is for one semester.
- **CGPA** (cumulative GPA) covers all semesters together: add up all grade points and divide by all credit hours.

## How to raise your GPA

High-credit courses affect your GPA most. Focusing on a 4-credit course moves your average more than a 1-credit one.
'''),
dict(slug='password-protect-pdf', title='How to Password Protect a PDF (and Remove a Password)', date='2026-11-06',
 desc='Lock sensitive PDFs with a password before sharing them — and unlock your own PDFs when you no longer need protection.',
 tools=['protect-pdf','unlock-pdf','redact-pdf'], md='''
Sending a salary slip, bank statement or contract by email? Adding a password means only people who know it can open the file.

## Add a password to a PDF

1. Open [Protect PDF](/protect-pdf/).
2. Drop your PDF.
3. Type a password twice.
4. Press **Protect** and download the locked file.

Share the password separately — for example, send the file by email and the password by WhatsApp.

## Choosing a good password

- At least 8–12 characters.
- Mix letters, numbers and a symbol.
- Avoid names, birthdays and "123456".
- Need ideas? Use the [Password Generator](/password-generator/).

## Remove a password from your own PDF

If you know the password and are tired of typing it, use [Unlock PDF](/unlock-pdf/): enter the password once and download an unlocked copy. Only unlock files you own or have permission to open.

## Hide information instead

Sometimes you don't need to lock the whole file — just hide a CNIC number, account number or address. [Redact PDF](/redact-pdf/) permanently blacks out the words you choose, so they can't be copied or recovered.

## Is it private?

Yes. Protection, unlocking and redaction all run in your browser. Your document and password never leave your device.
'''),
dict(slug='free-online-tools-for-students', title='15 Free Online Tools Every Student Needs in 2026', date='2026-11-06',
 desc='The free browser tools that save students hours every week — from PDFs and scans to GPA and citations.',
 tools=['scan-to-pdf','pdf-merger','word-counter','gpa-calculator'], md='''
Assignments, notes, applications and presentations — student life runs on files. These free tools work right in your browser with no sign-up.

## For assignments

1. **[Scan to PDF](/scan-to-pdf/)** — turn handwritten pages into a clean PDF with your phone.
2. **[PDF Merger](/pdf-merger/)** — combine all your pages and documents into one file for submission.
3. **[Word to PDF](/word-to-pdf/)** — submit work in a format that looks the same on your teacher's screen.
4. **[PDF to Word](/pdf-to-word/)** — edit a PDF handout or past paper.
5. **[Word Counter](/word-counter/)** — hit the word limit exactly.

## For uploads and applications

6. **[PDF Compressor](/pdf-compressor/)** — get under 1 MB or 2 MB upload limits.
7. **[Image Resizer](/image-resizer/)** — resize photos to the exact pixels a form asks for.
8. **[HEIC to JPG](/heic-to-jpg/)** — fix iPhone photos that won't upload.
9. **[Images to PDF](/images-to-pdf/)** — turn certificate photos into one document.

## For studying

10. **[GPA Calculator](/gpa-calculator/)** — know where you stand before results.
11. **[Percentage Calculator](/percentage-calculator/)** — marks, discounts and increases in seconds.
12. **[Pomodoro Timer](/pomodoro-timer/)** — focus in 25-minute sprints.
13. **[PDF to Markdown](/pdf-to-markdown/)** — paste clean notes into AI tools.

## For presentations

14. **[PDF to PowerPoint](/pdf-to-powerpoint/)** — turn a PDF into slides.
15. **[QR Code Generator](/qr-code-generator/)** — put a link to your project on the last slide.

All of these run on your own device, so your files stay private. Bookmark [dorapdf.com](/) and you'll always have them ready.
'''),
]
