# Template métier IA – Exemple Santé

## Objectif
Générer un rapport médical structuré à partir d’un texte libre, multilingue, conforme RGPD, avec fallback IA open source.

## Exemple d’appel API (Python)
```python
result = generate_ai_response(
    prompt="Patient: fièvre, toux, fatigue. Antécédents: diabète.",
    user_id="medecin-42",
    lang="fr",
    role="medecin",
    engine="mixtral"
)
print(result)
```

## Exemple d’appel API (Node.js)
```js
const result = await generateAIResponse({
  prompt: 'Patient: fever, cough, fatigue. History: diabetes.',
  userId: 'doctor-42',
  lang: 'en',
  role: 'doctor',
  engine: 'mixtral'
});
console.log(result);
```

## Structure de la réponse attendue
- Diagnostic probable
- Conseils médicaux
- Avertissement RGPD
- Langue de sortie

## Extension
- Ajouter des templates pour RH, finance, industrie, etc.
- Documenter chaque champ, chaque paramètre, chaque fallback.
