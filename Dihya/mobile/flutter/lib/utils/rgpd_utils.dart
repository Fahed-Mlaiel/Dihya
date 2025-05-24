class RgpdUtils {
  static bool hasConsent(Map<String, dynamic> user) {
    return user['consent_rgpd'] == true;
  }
}
