import 'package:flutter/material.dart';
import 'pages/pagina2.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      routes: {
        '/home': (context) => MyHomePage(),
        '/pagina2': (context) => pagina2(),
        '/pagina3': (context) => pagina3(),
      },


      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color.fromARGB(255, 219, 18, 159),
        ),
      ),
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  // Váriável controladora do texto digitado em password
  TextEditingController passwordController = TextEditingController();
  // Váriável controladora do texto digitado em email
  TextEditingController emailController = TextEditingController();

  double resultado = 0.0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Barra do app = (header)
      appBar: AppBar(
        title: Text('Kallya'),
        backgroundColor: Colors.blue,
      ),
      // Onde é estruturado o corpo do app
      body: Center(
        child: Column(
          children: [
            Text('Carlos'),
            Container(
              margin: const EdgeInsets.all(10.0),
              color: Colors.amber[600],
              width: 48.0,
              height: 48.0,
            ),

            // Texfield para o password
            TextField(
              obscureText: true,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Divisor',
              ),
              controller: passwordController,            
            ),

            // Texfield para o email
            TextField(
              obscureText: true,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Dividendo',
              ),
              controller: emailController,            
            ),

            // Criando o botão para entrar
            ElevatedButton(
              onPressed: () {
                setState(() {
                  resultado = double.parse(
                    passwordController.text) /
                    double.parse(emailController.text) ;            
                });
              }, 
              child: Text("Entrar")
            ),
            // Texto de resultado
            Text('Resultado: $resultado'),
            // Inclusão de imagem
            Image.asset(
              'images/posto_img.png',
              width: 90,
              height: 110,
            ),

            // Criando o botão de navegação
            ElevatedButton(
              child: Text("Página 2"),
              onPressed: () {
                Navigator.pushNamed(context, '/pagina2');
                }),

          ],
        ),
      ),
    );
  }
}



class pagina3 extends StatefulWidget {
  const pagina3({super.key});

  @override
  State<pagina3> createState() => _pagina3State();
}

class _pagina3State extends State<pagina3> {
  @override

  Widget build(BuildContext context) {
    return DefaultTabController(
      initialIndex: 1,
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          title: const Text("Página 3"),
          bottom: const TabBar(tabs: [
            Tab(
              icon: Icon(Icons.abc_rounded),
            ),
            Tab(
              icon: Icon(Icons.abc_sharp),
            )
          ],
        )),
        body: const TabBarView(children: [
          Text("Botao"),
          Text("Botao 2"),
        ]
        ),
      ),
    );
  }
}