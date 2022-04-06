


# Curso de Python 

## 1.1 Tipagem forte 

Python é uma linguagem de tipagem forte. Isso significa que se uma variável adquire um determinado tipo não deixa mais de ser daquele tipo a menos que seja recriada. Isso o torna diferente de um script Shell, por exemplo, em que numa se sabe o tipo exato de uma variável. 
Apesar da sua tipagem ser forte, a declaração de variáveis não é necessário  e a simples atribuição de um valor serve para criar ou recriar uma variável. Leve isso em conta quando programar. Tome muito cuidado com os nomes das variáveis.

## 1.2. Orientação a objeto 

Dou uma ênfase especial a esse conceito, pois já vi muita gente dizer que uma linguagem é orientada a objetos porque você pode criar interfaces gráficas. Não tem nada a ver. 
Uma linguagem orientada a objetos coloca como centro nervoso do rpogram um ou mais objetos de determinada classe, ao contrário das linguagens estruturadas, em que o processo, ou as estruturas de dados são o centro e você chama funções que atuam sobre esses elementos. 
Isso não siginifca, é claro, que não se pode criar aplicações com interfaces gráficas com Python ou com qualquer outra linugagem orientada ou não a objetos. 
Python é uma linguagem orientada a objetos, e nela quase tudo é um objeto. Até mesmo as variáveis que representam os tipos mais básico, como inteiro e caractere são objetos, têm seus método e propriedades. 

## 1.3. Módulos, as bibliotecas do Python 

No python chamaos as coleções de código que fornecem extensções para a linguagem de módulos. Pode-se fazer uma ssociação às bibliotecas usadas em C( e, na verdae, algumas vezes os módulos são bibliotecas). Para usá-los, temos que importá-los. Mas cuidade com a balança. 
O python procura sempre proteger o chamada espaço de nomes e, portanto, sempre que você importa rum módulo terá de usar seu nome para chamar funções e acessar propriedades que estão dentro dele. Isso pode ser familiar para quem lida com Java ou C#.
Ver o arquivo teste01.py

A primeira, "import os", importa o módulo com um todo, mas exige que sempre que você quiser acessar algo que pertence ao módulo você tenha que adicionar "os" antes da função ou propriedade.  O segundo, "from os import getcwd", importa somente aquela função determinada, isso pode usar menos memória e não é mais necessário usar "os" antes de chamar a função a terceira forma é como a segunda, mas ao invés de impronta uma só função importa todas. 

## 1.4 A função dir()

O python tem uma função chamada dir(). Ela fornece à linguagem a capacidade de reflexão, presente em linguagens como Java. Isso significa que você pode listar o conteúdo de módulos e qualquer outro tipo de objeto. Isso ajuda a saber sobre o que queremos ajuda. 
Isso significa que o espaço de nomes "__builtins__", carrega aquelas funç~eos ou propriedades, que o módulo sys tem aquelas listadas, e que você pode usar aqueles métodos em qualquer string. 

## 1.5 PyDoc

pydoc é um software que acompanha a distribuição oficial do python. Ele permite acesso à documentão presenta nas docstrings dos objetos. 
Há vários modos de utiliza-lo, um dos mais úteis é chamando-o para que monte um pequeno servidor HTTP. digite em um terminal o seguinte comando: 

    pydoc -p 1234
Ele criará um servidor que pode ser acessado em sua máquina. A página é produzida automaticamente e lista os módulos Python instalados. . 

## 1.6. Nosso amigo help() 
O interpretado python oferece um mecanismo de ajuda simples e eficiente. ele prove uma função help(), que permite acessar parte da documentada facil python e o pydoc. 

## 1.7 Variáveis e mais sintaxe básica

Vamos continuar usando interpretador. Agora vamos ver um poucos sobre variáveis. variáveis são estruturas simples que servem para graduar dados. Como eu já disse, não necessário declara variáveis em Python. 
teste02.py

A primeira linha coloca 1 na variável de nome variavel. A segunda linha mostra variavel na tela e a terceira retonra o valor de variavel. É muito importante fazer distinção entre essa duas últimas. 
Um programador deve saber que normalmente toda "afirmação" que é feita em um programa é, na verdade, um expressão, na maioria das linguagens. Em python, sempre. Sempre existe uma avaliação do valor e um retorno do valor.  O sentido prático disso é que o segundo 1 não seria realmente mostrada na tela em um programa de verdade, ele seria retornado para cada. 


