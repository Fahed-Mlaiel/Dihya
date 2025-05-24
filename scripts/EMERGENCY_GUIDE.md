# EMERGENCY_GUIDE.md

## Guide d’Urgence Dihya (français)
- **Incident critique** : Suivez le protocole d’alerte, contactez le DPO, activez le backup.
- **Fuite de données** : Isolez le système, informez la DSI, lancez l’audit.
- **Panne majeure** : Basculez sur l’infrastructure de secours, informez les utilisateurs.

## Emergency Guide (English)
- **Critical incident**: Follow alert protocol, contact DPO, activate backup.
- **Data breach**: Isolate system, inform IT, launch audit.
- **Major outage**: Switch to backup infra, notify users.

## دليل الطوارئ (العربية)
- **حادث خطير**: اتبع بروتوكول الإنذار، تواصل مع مسؤول حماية البيانات، فعّل النسخ الاحتياطي.
- **تسرب بيانات**: اعزل النظام، أخبر قسم تكنولوجيا المعلومات، أطلق التدقيق.
- **عطل كبير**: انتقل للبنية التحتية الاحتياطية، أخبر المستخدمين.

## ⵜⴰⵎⴰⵣⵉⵖⵜ (amazigh)
- **Asefru ameqran**: Sdukel protocol n alert, nermes DPO, sdukel backup.
- **Ttwas n isefka**: Sdukel system, nermes IT, sdukel audit.
- **Ttwas ameqran**: Beddel ɣer infra n backup, nermes imeslayen.

---

### Checklist d’urgence
- [x] Procédures documentées
- [x] Contacts d’urgence à jour
- [x] Scripts de restauration testés
- [x] Communication multilingue

### Mise à jour
Vérifiez ce guide à chaque évolution du plan de continuité.

---

## 🧪 Procédures de test automatisé
- Tous les scripts critiques (backup, restore, migrate) sont testés via `test.sh`.
- Vérification automatique de la restauration sur environnement de secours.

## 🧩 Extension & Modularité
- Ce guide peut être enrichi avec des procédures spécifiques à chaque stack (voir `/docs/INCIDENTS_GUIDE.md`).
- Liens directs vers scripts d’urgence : `restore.sh`, `backup.sh`, `main.py`.

## 🔗 Liens utiles
- [Plan de continuité](../INCIDENTS_GUIDE.md)
- [Guide de restauration](../RESTORE_GUIDE.md)
- [Audit de sécurité](../AUDIT_LOGGING_GUIDE.md)

## 📢 Communication
- Modèles d’alerte multilingues disponibles dans `/email_templates/`.
- Procédures de notification automatisée via `main.js`.

---

### Checklist avancée
- [x] Procédures testées automatiquement
- [x] Scripts d’urgence versionnés et audités
- [x] Documentation multilingue à jour
