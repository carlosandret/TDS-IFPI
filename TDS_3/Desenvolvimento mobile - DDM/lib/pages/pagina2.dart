import 'package:flutter/material.dart';

class pagina2 extends StatefulWidget {
  const pagina2({super.key});

  @override
  State<pagina2> createState() => _pagina2State();
}

class _pagina2State extends State<pagina2> {
  // final List<String> entradas = <String>['A', 'B', 'C'];
  // final List<int> codigoCores = <int>[600, 500, 100];

  // // Terminar depois q professor colocar slide (-_-)
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Primeira rota"),
      ),
      body:
      ListView(
        padding: const EdgeInsets.all(8),
        children: [
          Container(
            height: 50,
            color: Colors.purple[600],
            child: const Center(child: Text("Alternativa A", style: TextStyle(color: Colors.white)),),
            
          ),
          Container(
            height: 50,
            color: Colors.purple[500],
            child: const Center(child: Text("Alternativa B", style: TextStyle(color: Colors.white)),),
          ),
          Container(
            height: 50,
            color: Colors.purple[200],
            child: const Center(child: Text("Alternativa C", style: TextStyle(color: Colors.white)),),
          ),
        ],
      )
       // Center(
      //   // child: Column(
      //   //   children: [
      //   //     ElevatedButton(onPressed: () {
      //   //       Navigator.pushNamed(context, '/pagina3');
      //   //     }, child: Text("Página 3"))

      //   //   ]
         
      //   ),


    );
  }
}