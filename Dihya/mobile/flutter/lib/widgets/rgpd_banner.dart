import 'package:flutter/material.dart';

class RgpdBanner extends StatelessWidget {
  final VoidCallback onAccept;
  const RgpdBanner({required this.onAccept});
  @override
  Widget build(BuildContext context) {
    return Banner(
      message: 'Consentement RGPD',
      location: BannerLocation.topEnd,
      child: ElevatedButton(
        onPressed: onAccept,
        child: Text('Accepter'),
      ),
    );
  }
}
