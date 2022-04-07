


# Curso de Python 

## 1.1 Tipagem forte 

Python é uma linguagem de tipagem forte. Isso significa que se uma variável adquire um determinado tipo não deixa mais de ser daquele tipo a menos que seja recriada. Isso o torna diferente de um script Shell, por exemplo, em que numa se sabe o tipo exato de uma variável. 
Apesar da sua tipagem ser forte, a declaração de variáveis não é necessário  e a simples atribuição de um valor serve para criar ou recriar uma variável. Leve isso em conta quando programar. Tome muito cuidado com os nomes das variáveis.

## 1.2. Orientação a objeto 

Dou uma ênfase especial a esse conceito, pois já vi muita gente dizer que uma linguagem é orientada a objetos porque você pode criar interfaces gráficas. Não tem nada a ver. 
Uma linguagem orientada a objetos coloca como centro nervoso do programa um ou mais objetos de determinada classe, ao contrário das linguagens estruturadas, em que o processo, ou as estruturas de dados são o centro e você chama funções que atuam sobre esses elementos. 
Isso não significa, é claro, que não se pode criar aplicações com interfaces gráficas com Python ou com qualquer outra linguagem orientada ou não a objetos. 
Python é uma linguagem orientada a objetos, e nela quase tudo é um objeto. Até mesmo as variáveis que representam os tipos mais básico, como inteiro e caractere são objetos, têm seus método e propriedades. 

## 1.3. Módulos, as bibliotecas do Python 

No python chamamos as coleções de código que fornecem extensões para a linguagem de módulos. Pode-se fazer uma associação às bibliotecas usadas em C( e, na verdade, algumas vezes os módulos são bibliotecas). Para usá-los, temos que importá-los. Mas cuidado com a balança. 
O python procura sempre proteger o chamada espaço de nomes e, portanto, sempre que você importa rum módulo terá de usar seu nome para chamar funções e acessar propriedades que estão dentro dele. Isso pode ser familiar para quem lida com Java ou C#.
Ver o arquivo teste01.py

A primeira, "import os", importa o módulo com um todo, mas exige que sempre que você quiser acessar algo que pertence ao módulo você tenha que adicionar "os" antes da função ou propriedade.  O segundo, "from os import getcwd", importa somente aquela função determinada, isso pode usar menos memória e não é mais necessário usar "os" antes de chamar a função a terceira forma é como a segunda, mas ao invés de impronta uma só função importa todas. 

## 1.4 A função dir()

O python tem uma função chamada dir(). Ela fornece à linguagem a capacidade de reflexão, presente em linguagens como Java. Isso significa que você pode listar o conteúdo de módulos e qualquer outro tipo de objeto. Isso ajuda a saber sobre o que queremos ajuda. 
Isso significa que o espaço de nomes "__builtins__", carrega aquelas funções ou propriedades, que o módulo sys tem aquelas listadas, e que você pode usar aqueles métodos em qualquer string. 

## 1.5 PyDoc

pydoc é um software que acompanha a distribuição oficial do python. Ele permite acesso à documentão presenta nas docstrings dos objetos. 
Há vários modos de utiliza-lo, um dos mais úteis é chamando-o para que monte um pequeno servidor HTTP. digite em um terminal o seguinte comando: 

    pydoc -p 1234
Ele criará um servidor que pode ser acessado em sua máquina. A página é produzida automaticamente e lista os módulos Python instalados. . 

## 1.6. Nosso amigo help() 
O interpretado python oferece um mecanismo de ajuda simples e eficiente. ele prove uma função help(), que permite acessar parte da documentada fácil python e o pydoc. 

## 1.7 Variáveis e mais sintaxe básica

Vamos continuar usando interpretador. Agora vamos ver um poucos sobre variáveis. variáveis são estruturas simples que servem para graduar dados. Como eu já disse, não necessário declara variáveis em Python. 
teste02.py

A primeira linha coloca 1 na variável de nome variável. A segunda linha mostra variável na tela e a terceira retorna o valor de variável. É muito importante fazer distinção entre essa duas últimas. 
Um programador deve saber que normalmente toda "afirmação" que é feita em um programa é, na verdade, um expressão, na maioria das linguagens. Em python, sempre. Sempre existe uma avaliação do valor e um retorno do valor.  O sentido prático disso é que o segundo 1 não seria realmente mostrada na tela em um programa de verdade, ele seria retornado para cada. 
As operações com números são feitas como em outras linguagens: 

teste03.py

Já que estamos lidando com variáveis, vamos ver como usar o print para coisas mais complexas. vamos mostrar variáveis com ele. Existem várias formas: 

teste04.py

A primeira forma deve ser comum a quem programa em VB ou PHP, por exemplo. A segunda deve causar boas lembras aos programadores de C. Eu, particularmente, prefiro a segunda forma, mas a primeira nos ensina duas coisas importantes. é possível somar strings (e, veremos mais a frente, outros tipos de dados, também!) e os tipos em python são fortes, você tem que converter o inteiro para string se quiser concatenar os dois. 
Vamos analisar melhor a segunda. Entre aspas temos o que chamamos de formato, que é a definição do que aparecerá na tela. A string "%d" significa que ali será coloca um inteiro. Depois do formato colocamos um separador (um "%") e, entre parênteses uma lista separada por vírgulas, das variáveis que queremos que substituam os código vamos ver mais um exemplo: 

teste05.py

## 1.8 - Condições e estruturas de repetição
Antes de começarmos a seção propriamente dita, é necessário entender como o Python marca o início e o final de blocos. Aqueles acostumados com C e Pascal estarão acostumados com coisa do tipo: 

    if (variavel == 10)
    {
      printf("E 10!!!/n");
    }
ou 

    if (variavel = 10) then 
    begin
      writeln("E 10!!!"); 
    end; 

O python, para o desgosto de alguns, não tem estruturas sintáticas de abertura e fechamento de blocos. O python usa a indentação para definir o início e término de blocos. O problema aqui é que muito programadores não tem o hábito de fazer uma indentação consistente. A vantagem do Python é que ele obriga o programador a ter uma indentação consiste. 
Portanto, para começar um bloco de condição, é necessário um nível de indentação. Para indentar, pressione a tecla tab. 

teste06.py

Duas coisas importantes a serem observadas quando python espera que ovC"E inicie um bloco, o interpretador muda o prompt para "..." e para mostrar que um bloco acabou (no interpretador) basta dar enter sem indentar uma linha depois de ter escrito seu bloco. Num programa de verdade não é neecssário adicionara um alinha em branco para terminar um bloco, basta não indentar a linha seguinte. Nós veremos isso melhor mais a fretne. 
outra coisa importante o: como eu disse inicial, no python toda "afirmativa" é uma expressão. Mas, diferentemente do C, o Python não aceita atribuições com contextos que devem ser somente usados para expressões de condição. Por exemplo, como vimos, o python usa o operador "igual igual " para comparações. Se eu fizer "if variavel == 10" o interpretador irá emitir um erro, porque atribuições não são permitidas em um fi. 
Você pode fazer testes de condição mais complexos com python, também. 

teste07.py


Outros operadores podem ser usados, como "or" para relação entre comparações, e "!=", "<", ">", "<=" e assim por diante, para relação entre variáveis e valores. 
Um loop for (para) em python se parece muito para o estilo Pascal de for. Ele exige um tipo de dados mais complexo, que nós veremos mais para frente, que é a lista. Mas por enquanto vamos ver o básico do for:

    for contador in range (0, 3):
	    print contador
A função range serve para retornar um lista que contenha o intervalo dado pelos números especificados. Preste muita atenção. O primeiro número que você especificar sempre entra no intervalo, o último nunca. Em matemática poderíamos representar assim: [0,4]
Um while segue, essencialmente a mesma lógica de qualquer outro while que eu já vi. 

## Usando um editor 

Algumas convenções para as quais devemos atentar: os arquivos executáveis Python normalmente não tem extensão, para manter a conferência com o resto do sistema. Os que tem usam ".py" como extensão. Os arquivos podem ser "byte-compilador" e, nesse caso, receberão a extensão ".pyc". 
Outra convenção importante é que todo script Pythoh deve começar com uma linha contendo a "string mágina (#!)" e a localização do interpretador, para que o sistema saiba como executar o script. Normalmente essa linha será: 

    #!/usr/bin/python
Essa é uma boa hora para dizer, também, que em python os comentário são feitos com o símbolo #. Tudo que vier depois de um # e antes de uma quebra de linha é um comentário. 
Então vamos colocar nosso primeiro exemplo para funcionar... Abra seu edito escreva o seguinte código. 

teste10.py

## Tipos de dados 
Os python fornece, além dos tipos básicos de dados, alguns tipos mais avançados e complexos que podem ser usado com muita facilidade. Quem já teve que usar uma lista encadeada sabe o quanto é complicado implementar esse tipo de estrutura do zero. O python facilita muito as coisas, e nós vamos explorar essa capacidades agora!
### Inteiros e ponto flutuante 

Lidar com números em python é bem fácil, como já vimos, o Python detecta o tipo do dado no momento em que ele é atribuído à variável. Isso significa que: 

teste11.py

### Strings 

Lidar com strings em python é muito simples. O que faz com que o python "detecte" o tipo string são as aspas, simples ou duplas. 

teste12.py

Como disse anteriormente, quase tudo em Python é um objeto.  Isso significa que uma string tem métodos.

Note, no entanto, um acoisa muito importante: uma string em python é sempre uma constante! Você nucna modifica uma string, o que você pode fazer é reatribuí-la. Isso siginifca que se você quiser que a string continue em letras maiúsculas dali para freten você deve fazer "nome.upper()". Nós veremos mais sobre como conhecer os métodos disponiveis. 
Para acessar partes especificas da string, você pode usar a notação de fatias. è importante entender bem essa notação, porquê eel aé muito útil em várias oportunidades e com alguns outros tipos de dados: 

teste13.py

### Linhas e tuplas

Agora o tipo de dados que serve como vetor e listas encadeadas. chamamos de lista uma lista que pode ser modificada dignamente e de tupla uma lista imóvel. 
Vamos ver as operações principais com listas: 
Note que todas as soperações básicas de lista encadaeada são contempladas pela implementação de lista do Python. A terceria linha mostra como inicializar uma vairável com uma lista pré-criada. A quarta mostra como obter o tamanho da lista usando a função len(). Nesse exmeplo usamso strings na lista, mas uma lista pode conter qualquer tiop de dados, inclusive listas, possibilitando a criçaão simpes de árvores, inclusive. 
Algo importante de se notar é que dá para usar a lista do python como pilha, usando os métodos append() e pop(). Outra derivação importante desse exemplo é ver que uma lista em python é indexada, como um vetor. Podemos usar "lista[0]" para acessar o primeiro item da lista, podemos usar esse índice para inserir nós em posições específicas. 
As listas tem outros métodos de externo interesse, como o sort(), que serve para ordenar a lista. É sentar e explorar as possibilidades!
As tuplas funcionam quase do mesmo mode que as listas, como a exceção de que são listas que não são modificáveis. Elas são bastante usada como retorno de algumas funções, portanto é bom explorá-las. Você reconhece uma tupla por sua similaridade com uma lista, mas ao invés de usar [] uma tupla usa parênteses. Um exemplo rápido: 

### Dicionários 

Quem já ouviu falar de Hash tables vai se sentir familiarizado com os dicionários rapidamente. Os dicionários em Python são, literalmente, estruturas de dados que permitem traduzir uma chave para um valor. Seu uso é muito simples:

### Conversão / Casting 

Python usa tipagem forte. Isso significa que se uma variável contém um inteiro ela não poe simplesmente ser usada como se fosse uma variável de ponto_flutuante. Para esse tipo de coisas é necessário fazer uma conversão. 

### Funções 
### Sintaxe Básica 
Funções em python tem uma sintaxe muito parecida com qualquer outra linguagem. O uso de parênteses é obrigatório, mesmo que não aja argumentos, ao contrário de algumas, com a única exceção da função inteira print. 
Declara uma função em python é muito simples: 

    def minha_funcao(argumento)
    print argumento
Como pode ser visto, o bloco que implementa a função também me demarcado pela indentação.

### Passagem avançada de argumentos 
Os argumentos não tem tipo declarado, o que dá uma grande flexibilidade. Os argumentos podem ter valores padrão, também, você pode dar valores específicos para argumentos opcionais fora da localização deles, nesse casos.

### Retorno da função 
para retornar um (ou mais) valores em uma função basta usar a declaração return. Você pode, inclusive, retornar diversos valores e, como na passagem de parâmetros, não precisa declara o tipo de dado retornado: 






