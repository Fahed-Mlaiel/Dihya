// Frontend React – Formulaire onboarding multilingue, RGPD, fallback, accessibilité
import React, { useState } from 'react';

export default function OnboardingForm() {
  const [email, setEmail] = useState('');
  const [lang, setLang] = useState('fr');
  const [msg, setMsg] = useState('');
  const [error, setError] = useState('');
  const [consent, setConsent] = useState(false);

  const submit = async e => {
    e.preventDefault();
    if (!consent) return setError('Consentement RGPD requis');
    setError('');
    const res = await fetch('/api/onboarding/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, lang })
    });
    const data = await res.json();
    if (data.error) setError(data.error);
    else setMsg(data.message + (data.fallback ? ' (fallback IA)' : ''));
  };

  return (
    <form onSubmit={submit} aria-label="Onboarding form">
      <label>Email
        <input type="email" value={email} onChange={e => setEmail(e.target.value)} required aria-required="true" />
      </label>
      <label>Langue
        <select value={lang} onChange={e => setLang(e.target.value)}>
          <option value="fr">Français</option>
          <option value="en">English</option>
          <option value="ar">العربية</option>
          <option value="tzm">ⵜⴰⵎⴰⵣⵉⵖⵜ</option>
        </select>
      </label>
      <label>
        <input type="checkbox" checked={consent} onChange={e => setConsent(e.target.checked)} /> Consentement RGPD
      </label>
      <button type="submit">S’inscrire</button>
      {error && <div role="alert" style={{color:'red'}}>{error}</div>}
      {msg && <div>{msg}</div>}
    </form>
  );
}
