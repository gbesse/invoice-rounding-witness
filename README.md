# invoice-rounding-witness

## Français

Expliquer les écarts entre arrondi par ligne et par catégorie de taxe.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m invoice_rounding_witness examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Compare calcul Decimal par ligne et par catégorie de taxe, avec taux, monnaie, précision et règle d’arrondi explicites. Chaque écart est décomposé par catégorie ; les avoirs négatifs suivent la même convention déclarée.

### Limites

Nets déjà exprimés dans la précision monétaire choisie, taux fractionnaires entre 0 et 1. Ne choisit pas la règle légalement applicable et ne certifie pas une facture Peppol/EN16931.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Explain differences between per-line and per-tax-category rounding.

Synthetic data; no network access or secret required.

```sh
python -m invoice_rounding_witness examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Compares Decimal calculations per line and per tax category with explicit rate, currency, precision and rounding rule. Decomposes each difference by category; negative credits follow the same declared convention.

### Limits

Net amounts already use selected currency precision; fractional rates between 0 and 1. Does not select legally applicable rules or certify Peppol/EN16931 invoices.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Explicar diferencias entre redondeo por línea y categoría fiscal.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m invoice_rounding_witness examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Compara cálculo Decimal por línea y categoría fiscal con tasa, moneda, precisión y regla explícitas. Descompone diferencias por categoría; abonos negativos siguen la misma convención declarada.

### Límites

Importes netos ya en precisión monetaria elegida; tasas fraccionarias entre 0 y 1. No elige reglas legalmente aplicables ni certifica facturas Peppol/EN16931.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.peppol.eu/poacc/billing/3.0/bis/
