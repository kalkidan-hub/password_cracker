import 'package:flutter/material.dart';

class LandingPage extends StatelessWidget {
  const LandingPage({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Landing",
      theme: ThemeData.dark(),
      home: Scaffold(
        body: Center(
          child: Text("Land good"),
        ),
      ),
    );
  }
}
