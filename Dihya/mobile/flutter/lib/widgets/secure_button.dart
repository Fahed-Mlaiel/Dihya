import 'package:flutter/material.dart';

class SecureButton extends StatelessWidget {
  final String label;
  final VoidCallback onPressed;
  const SecureButton({required this.label, required this.onPressed});
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: onPressed,
      child: Text(label),
    );
  }
}
