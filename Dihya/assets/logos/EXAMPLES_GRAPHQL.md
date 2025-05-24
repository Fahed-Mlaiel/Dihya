# Dihya Logos – Exemples GraphQL

```graphql
# Query pour obtenir la liste des logos
query {
  logos {
    name
    url
    description
    accessibility {
      ariaLabel
      contrast
    }
  }
}
```
