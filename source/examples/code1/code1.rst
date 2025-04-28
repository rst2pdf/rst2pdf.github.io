Code Samples for Documents or Presentations
###########################################

We use an adapted set of styles based on Pygments. Here are some examples, you can apply the built-in styles as you wish.

Python example: Flask minimal example

.. code:: python

    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'


PHP example: Slim Framework minimal example

.. code:: php

    <?php
    use Psr\Http\Message\ResponseInterface as Response;
    use Psr\Http\Message\ServerRequestInterface as Request;
    use Slim\Factory\AppFactory;

    require __DIR__ . '/../vendor/autoload.php';

    $app = AppFactory::create();

    $app->get('/hello/{name}', function (Request $request, Response $response, array $args) {
        $name = $args['name'];
        $response->getBody()->write("Hello, $name");
        return $response;
    });

    $app->run();

Go example

.. code:: go
    
    package main

    import "fmt"

    func main() {

      var favoriteSnack string
  
      favoriteSnack = "Cheese"
  
      fmt.Println("My favorite snack is " + favoriteSnack)
    
    }
