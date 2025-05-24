# Dihya Logos – Exemples Webhooks

## Webhook de notification upload logo
```json
{
  "event": "logo_uploaded",
  "logo": "dihya-main.svg",
  "user": "admin",
  "timestamp": "2025-05-22T12:00:00Z"
}
```

## Webhook de notification audit RGPD
```json
{
  "event": "logo_audit_rgpd",
  "result": "passed",
  "timestamp": "2025-05-22T12:01:00Z"
}
```
