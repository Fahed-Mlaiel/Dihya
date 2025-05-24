class I18nUtils {
  static String getLabel(String key, String lang) {
    final labels = {
      'welcome': {
        'fr': 'Bienvenue',
        'en': 'Welcome',
        'ar': 'مرحبا',
        'tzm': 'Azul'
      }
    };
    return labels[key]?[lang] ?? labels[key]?['fr'] ?? key;
  }
}
