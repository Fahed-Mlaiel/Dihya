# Dihya Logos – Exemples API REST/GraphQL

## REST (OpenAPI)
```http
GET /api/logos?lang=fr
GET /api/logos/dihya-main.svg
```

## GraphQL
```graphql
query {
  logos(lang: "fr") {
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
