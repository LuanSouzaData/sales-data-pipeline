# Data Quality Rules

Este documento descreve as regras de qualidade aplicadas ao pipeline.

| ID | Rule | Description | Status |
|----|------|-------------|--------|
| DQ-001 | Remove duplicated sales | Remove registros duplicados com base em `sale_id`. | ✅ |
| DQ-002 | Remove invalid quantities | Remove registros com quantidade menor ou igual a zero. | ⏳ |
| DQ-003 | Remove invalid prices | Remove registros com preço menor ou igual a zero. | ⏳ |
| DQ-004 | Validate dates | Remove ou corrige datas inválidas. | ⏳ |
| DQ-005 | Standardize categories | Padroniza nomes das categorias. | ⏳ |
| DQ-006 | Normalize customer names | Remove espaços extras e padroniza nomes. | ⏳ |
| DQ-007 | Calculate total price | Cria a coluna `total_price`. | ⏳ |
| DQ-008 | Generate quality report | Informa quantos registros foram removidos ou corrigidos. | ⏳ |