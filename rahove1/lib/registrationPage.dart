import 'package:flutter/material.dart';

class Registration extends StatelessWidget {
  const Registration({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Register",
      theme: ThemeData.dark(),
      home: Scaffold(
        body: Center(
          child: Text("Land good"),
        ),
      ),
    );
  }
}
