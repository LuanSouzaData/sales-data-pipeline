# Data Quality Rules

| ID | Rule | Description | Status |
|----|------|-------------|--------|
| DQ-001 | Remove duplicated sales | Remove duplicated records based on `sale_id`. | ✅ |
| DQ-002 | Remove invalid quantities | Remove records where `quantity <= 0`. | ✅ |
| DQ-003 | Remove invalid prices | Remove records where `unit_price <= 0`. | ✅ |
| DQ-004 | Validate dates | Convert dates and remove invalid values. | ✅ |
| DQ-005 | Standardize categories | Normalize category names. | ✅ |
| DQ-006 | Normalize customer names | Fill missing values and remove extra spaces. | ✅ |
| DQ-007 | Calculate total price | Create the `total_price` column. | ✅ |