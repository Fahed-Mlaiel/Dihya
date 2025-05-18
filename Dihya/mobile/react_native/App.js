/**
 * @file App.js
 * @description Composant principal de l’application mobile React Native Dihya Coding : design moderne, navigation sécurisée, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useState, useEffect } from 'react';
import { SafeAreaView, View, Text, Button, Alert, StyleSheet, StatusBar } from 'react-native';

// Import des écrans métiers (à adapter selon l’architecture)
import EcommerceScreen from './screens/EcommerceScreen';
import EducationScreen from './screens/EducationScreen';
import SocialScreen from './screens/SocialScreen';

// Import des utilitaires RGPD, logs, sécurité
import { hasConsent, setConsent, revokeAllConsents } from './utils/rgpd';
import { clearAllLogs } from './utils/logger';

// Navigation simple (remplacer par react-navigation pour un projet réel)
const ROUTES = {
  HOME: 'HOME',
  ECOMMERCE: 'ECOMMERCE',
  EDUCATION: 'EDUCATION',
  SOCIAL: 'SOCIAL'
};

/**
 * Composant principal de l’application mobile Dihya Coding.
 * Gère la navigation, le consentement RGPD, l’auditabilité et le rendu des pages métiers.
 */
export default function App() {
  const [route, setRoute] = useState(ROUTES.HOME);
  const [consent, setConsentState] = useState(false);

  useEffect(() => {
    setConsentState(hasConsent('app'));
  }, []);

  /**
   * Gère la demande de consentement RGPD utilisateur.
   */
  function handleConsent(val) {
    setConsent('app', val, { log: true });
    setConsentState(val);
  }

  /**
   * Purge tous les logs et données sensibles (droit à l’oubli RGPD).
   */
  function handlePurge() {
    clearAllLogs();
    revokeAllConsents({ log: true });
    Alert.alert('Données locales purgées (RGPD).');
  }

  /**
   * Rendu dynamique selon la route.
   */
  function renderRoute() {
    switch (route) {
      case ROUTES.ECOMMERCE:
        return <EcommerceScreen />;
      case ROUTES.EDUCATION:
        return <EducationScreen />;
      case ROUTES.SOCIAL:
        return <SocialScreen />;
      default:
        return (
          <View style={styles.centered}>
            <Text style={styles.title}>Bienvenue sur Dihya Coding</Text>
            <Text style={styles.subtitle}>Choisissez un module métier ci-dessous.</Text>
          </View>
        );
    }
  }

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" />
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Dihya Coding</Text>
      </View>

      {!consent ? (
        <View style={styles.banner}>
          <Text style={styles.bannerText}>
            Cette application nécessite votre consentement RGPD pour l’auditabilité et la sécurité.
          </Text>
          <Button title="Accepter" onPress={() => handleConsent(true)} testID="consent-accept" />
          <Button title="Refuser" onPress={() => handleConsent(false)} testID="consent-decline" />
        </View>
      ) : (
        <View style={styles.main}>
          {renderRoute()}
          <View style={styles.menu}>
            <Button title="Accueil" onPress={() => setRoute(ROUTES.HOME)} />
            <Button title="E-commerce" onPress={() => setRoute(ROUTES.ECOMMERCE)} />
            <Button title="Éducation" onPress={() => setRoute(ROUTES.EDUCATION)} />
            <Button title="Social" onPress={() => setRoute(ROUTES.SOCIAL)} />
          </View>
          <Button title="Purger mes données (RGPD)" onPress={handlePurge} color="#E94F37" />
        </View>
      )}

      <View style={styles.footer}>
        <Text style={styles.footerText}>
          © {new Date().getFullYear()} Dihya Coding – Sécurité, RGPD, auditabilité, extensibilité, robustesse.
        </Text>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#F4F4F4' },
  header: { padding: 16, backgroundColor: '#2B4C7E', alignItems: 'center' },
  headerTitle: { color: '#fff', fontSize: 22, fontWeight: 'bold' },
  banner: { padding: 24, backgroundColor: '#FBBD23', alignItems: 'center', margin: 16, borderRadius: 8 },
  bannerText: { marginBottom: 12, fontSize: 16, color: '#333', textAlign: 'center' },
  main: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  menu: { flexDirection: 'row', justifyContent: 'space-around', marginVertical: 16 },
  centered: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  title: { fontSize: 24, fontWeight: 'bold', color: '#2B4C7E', marginBottom: 8 },
  subtitle: { fontSize: 16, color: '#555' },
  footer: { padding: 8, backgroundColor: '#F4F4F4', alignItems: 'center' },
  footerText: { fontSize: 12, color: '#888', textAlign: 'center' }
});

/* Documentation claire : chaque fonction et composant est commenté pour auditabilité et conformité */