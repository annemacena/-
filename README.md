<br />
<p align="center">
    <img src="https://user-images.githubusercontent.com/14198332/134978178-6b0aa36a-337c-4146-a4b9-ec731b6b1261.jpg" alt="Logo">
</p>

# マンガリスト (Manga List, Lista de Mangá)

Sisteminha de CRUD implementado em Python para disciplina de Introdução à Python na Residência em Visão Computacional pelo CIn-UFPE.
Em resumo, será feito um banco de dados em arquivo de mangás e as funcionalidades do CRUD serão aplicadas nesse banco de dados.

> Mangá (漫画) é um termo japonês usado para designar uma história em quadrinhos (no Japão se refere a qualquer história em quadrinhos mas em outros países, se refere à história em quadrinhos japonesa. [Referência aqui](https://pt.wikipedia.org/wiki/Mang%C3%A1).).

## Requisitos

* Sistema com funcionalidades CRUD (create, read, update and delete ou criar, ler, atualizar e deletar)
* Ao realizar as funcionalidades, elas também deverão ser feitas em registros num arquivo txt
* É necessário ter um menu para realizar interação com o usuário (seja no prompt/terminal ou uma interface gráfica)

## Estrutura do arquivo

Cada linha do arquivo vai conter atributos do registro de um mangá. Cada atributo é dividido em ponto e vírgula (;).
Os atributos escolhidos para cada mangá foram:

* nome
* autor
* status (Completo, Andamento, Cancelado e Hiato)
* ano_inicio
* ano_fim
* sinopse
* num_de_volumes
* publico (Por exemplo: Shoujo, Josei, Seinen, etc)
* genero
* impressao (Editora)
* revista
* venda_mensal (No formato array de arrays, cada item do array está no formato de: ano, mes, total de vendas. Por exemplo: [[2016, 1, 100], [2016, 2, 150], [2016, 3, 180]]).

### Exemplo de registro no arquivo:
```
TESTE3;NANA;Ai Yazawa;Hiato;2000;2009;Duas gurias com o mesmo nome se encontram e viram amigas. Melhor anime/mangá do universo.;21;Josei;[Drama,Romance,Slice of Life];Shueisha;Cookie;[[2000_1_1000],[2000_2_2000],[2000_3_1500],[2000_4_1600],[2009_12_11050]]
```
## Contexto geral de funcionamento do sistema

Uma variável do tipo [dicionário](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) ficará responsável por manter a persistência local dos dados, porém, o sistema deverá manter atualizado o arquivo onde estão os dados sempre que uma funcionalidade for acionada. Ou seja, de acordo com a opção escolhida pelo usuário (criar, ler, editar e deletar um mangá), o registro deverá ser mantido localmente na variável e no arquivo.

### Exemplo do conteúdo da variável dicionário
```
{
    'TESTE3': 
        [
            'NANA',
            'Ai Yazawa',
            'Hiato',
            '2000',
            '2009',
            'Duas gurias com o mesmo nome se encontram e viram amigas. Melhor anime/mangá do universo.',
            '21',
            'Josei', ['Drama', 'Romance', 'Slice of Life'],
            'Shueisha',
            'Cookie', 
            [['2000', '1', '1000'], ['2000', '2', '2000'], ['2000', '3', '1500'], ['2000', '4', '1600'], ['2009', '12', '11050']]
        ]
 }
```

#### Relação atributo x índice
* nome: __0__
* autor: __1__
* status: __2__
* ano_inicio: __3__
* ano_fim: __4__
* sinopse: __5__
* num_de_volumes: __6__
* publico: __7__
* genero: __8__
* impressao: __9__
* revista: __10__
* venda_mensal: __11__
