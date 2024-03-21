import 'package:flutter/material.dart';

class Insight extends StatefulWidget {
  const Insight({super.key});

  @override
  State<Insight> createState() => _InsightState();
}

class _InsightState extends State<Insight> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Insight",
      theme: ThemeData.dark(),
      home: Scaffold(
        body: Center(
          child: Text("Land good"),
        ),
      ),
    );
  }
}
