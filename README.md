## English description

This is the repo of my solution to the *Polygon Area Calculator* project from the **Scientific Computing with Python** course from freeCodeCamp. Portuguese description down below.

### Assignment

In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.

#### Rectangle class

When a Rectangle object is created, it should be initialized with `width` and `height` attributes. The class should also contain the following methods:
* `set_width`
* `set_height`
* `get_area`: Returns area (`width * height`)
* `get_perimeter`: Returns perimeter (`2 * width + 2 * height`)
* `get_diagonal`: Returns diagonal (`(width ** 2 + height ** 2) ** .5`)
* `get_picture`: Returns a string that represents the shape using lines of "\*". The number of lines should be equal to the height and the number of "\*" in each line should be equal to the width. There should be a new line (`\n`) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
* `get_amount_inside`: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

Additionally, if an instance of a Rectangle is represented as a string, it should look like: `Rectangle(width=5, height=10)`

#### Square class

The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The `__init__` method should store the side length in both the `width` and `height` attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a `set_side` method. If an instance of a Square is represented as a string, it should look like: `Square(side=9)`

Additionally, the `set_width` and `set_height` methods on the Square class should set both the width and height.

#### Usage example

```py
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```
That code should return:

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

The unit tests for this project are in `test_module.py`.

### Development

Write your code in `shape_calculator.py`. For development, you can use `main.py` to test your `shape_calculator()` function. Click the "run" button and `main.py` will run.

### Testing 

We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.

-------------------------------------------------------------------

## Descrição em português

Esse é o repositório da minha solução para o projeto *Polygon Area Calculator* do curso **Scientific Computing with Python** do freeCodeCamp. A tradução é livre e feita por mim.

### Tarefa

Nesse projeto você irá usar programação orientada a objetos para criar uma classe `Rectangle` e uma classe `Square`. A classe Square class deve ser uma subclasse de Rectangle e herdar seus métodos e atributos.

#### Classe Rectangle

Quando um objeto Rectangle é criado, ele deve ser inicializado com atributos `width` e `height`. A classe deve conter também os seguintes métodos:
* `set_width`
* `set_height`
* `get_area`: retorna a área (`width * height`)
* `get_perimeter`: retorna o perímetro (`2 * width + 2 * height`)
* `get_diagonal`: retorna a diagonal (`(width ** 2 + height ** 2) ** .5`)
* `get_picture`: retorna uma string que representa o formato usando linhas de `*`. O número de linhas deve ser igual à altura e o número de `*` em cada linha deve ser igual à largura. Deve haver uma nova linha (`\n`) ao final de cada linha. Se a largura ou altura for maior que 50, então deve-se retornar a string: "Too big for picture.".
* `get_amount_inside`: recebe outro formato (quadrado ou retângulo) como argumento. Retorna o número de vezes que o formato passado cabe no formato (sem rotações). Por exemplo, em um retângulo de largura 4 e altura 8 cabem 2 quadrados de lado 4.

Ademais, se uma instância de Rectangle for representada como string, ela deve ter a forma: `Rectangle(width=5, height=10)`

#### Classe Square

A classe Square deve ser uma subclasse de Rectangle. Quando um objeto Square for criado, um único tamanho de lado é passado. O método `__init__` deve guardar o tamanho do lado em ambos atributos `width` e `height` da classe Rectangle.

A classe Square deve ser capaz de acessar os métodos da classe Rectangle mas deve conter tambem um método `set_side`. Se uma instância de Square for representada como string, ela deve ter a forma: `Square(side=9)`

Ademais, os métodos `set_width` e `set_height` na classe Square devem ambos setar a altura e a largura.

#### Exemplo de uso

```py
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```
Esse código deve retornar:

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

Os testes unitário para esse projeto estão em `test_module.py`.

### Desenvolvimento

Escreva seu código em `shape_calculator.py`. Para desenvolvimento, você pode usar `main.py` para testar a sua função `shape_calculator()`. Clique em "run" e `main.py` rodará.

### Testando

Importamos os testes de `test_module.py` para `main.py` por conveniência. Os testes rodarão automaticamente quando você apertar "run".

### Submissão

Copie a URL do projeto e submeta-a ao freeCodeCamp.
