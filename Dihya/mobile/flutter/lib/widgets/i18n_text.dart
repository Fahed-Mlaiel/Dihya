import 'package:flutter/material.dart';

class I18nText extends StatelessWidget {
  final Map<String, String> labels;
  final String lang;
  const I18nText({required this.labels, required this.lang});
  @override
  Widget build(BuildContext context) {
    return Text(labels[lang] ?? labels['fr'] ?? '');
  }
}
