# Dihya – Politique de Sécurité Globale

Ce document centralise toutes les politiques de sécurité du projet Dihya (frontend, backend, mobile, plugins, marketplace, uploads, DevOps, etc.), en conformité avec le cahier des charges, la souveraineté numérique, la RGPD, et les meilleures pratiques internationales.

## FR – Français
- Sécurité avancée : RBAC, MFA, logs, audit, RGPD, anonymisation, CORS, JWT, OAuth, anti-DDoS, rate limiting
- Sécurité API : validation, XSS, CSRF, injection, plugins, marketplace
- Sécurité données : chiffrement, backup, audit, logs, anonymisation
- Souveraineté : fallback open source, auditabilité, logs, licence AGPL
- CI/CD : tests sécurité automatisés, audit dépendances, SAST, lint, build, e2e
- Extension : chaque module/plugin/template doit respecter cette politique

## EN – English
- Advanced security: RBAC, MFA, logs, audit, GDPR, anonymization, CORS, JWT, OAuth, anti-DDoS, rate limiting
- API security: validation, XSS, CSRF, injection, plugins, marketplace
- Data security: encryption, backup, audit, logs, anonymization
- Sovereignty: open source fallback, auditability, logs, AGPL license
- CI/CD: automated security tests, dependency audit, SAST, lint, build, e2e
- Extension: every module/plugin/template must comply with this policy

## AR – العربية
- أمان متقدم: RBAC، MFA، سجلات، تدقيق، RGPD، إخفاء هوية، CORS، JWT، OAuth، مضاد DDoS، تحديد معدل
- أمان API: تحقق، XSS، CSRF، حقن، إضافات، سوق
- أمان البيانات: تشفير، نسخ احتياطي، تدقيق، سجلات، إخفاء هوية
- السيادة: بدائل مفتوحة المصدر، تدقيق، سجلات، رخصة AGPL
- CI/CD: اختبارات أمان آلية، تدقيق تبعيات، SAST، lint، build، e2e
- التوسيع: يجب أن يلتزم كل مكون/إضافة/قالب بهذه السياسة

## Taqbaylit (Amazigh)
- Tazult n tazult: RBAC, MFA, logs, audit, RGPD, anonymisation, CORS, JWT, OAuth, anti-DDoS, rate limiting
- Tazult API: validation, XSS, CSRF, injection, plugins, marketplace
- Tazult n isefka: chiffrement, backup, audit, logs, anonymisation
- Tazult: fallback open source, auditabilité, logs, licence AGPL
- CI/CD: tzuyin tazult, audit dépendances, SAST, lint, build, e2e
- Extension: yal module/plugin/template yessefk ad yeddu s tazult-a

---

- Chaque module doit être testé (unit, integration, e2e, accessibilité, sécurité)
- Voir README.md, tests/, guides/ pour plus de détails
