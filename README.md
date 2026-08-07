# 📊 Sales Data Pipeline

Projeto desenvolvido para demonstrar uma pipeline de dados completa utilizando Python.

O pipeline realiza o processo de ETL (Extract, Transform and Load), aplicando validações de qualidade, carregando os dados em um banco SQLite e utilizando testes automatizados com Pytest.

---

## 🚀 Tecnologias

- Python 3.13
- Pandas
- SQLite
- Pytest
- Git
- GitHub

Em breve:

- GitHub Actions
- Docker
- Apache Airflow
- AWS

---

## 📂 Estrutura do projeto

```text
sales-data-pipeline/

data/
database/
docs/
logs/
src/
tests/
README.md
requirements.txt
```

---

## 🔄 Fluxo da Pipeline

```text
CSV Files
     │
     ▼
Extract
     │
     ▼
Transform
     │
     ▼
Load
     │
     ▼
SQLite Database
```

---

## 🔎 Transformações

Atualmente o pipeline realiza:

- Remoção de registros duplicados
- Validação de quantidade
- Validação de preços
- Validação de datas
- Padronização de categorias
- Padronização de nomes
- Cálculo do valor total da venda

---

## 🧪 Testes

Para executar:

```bash
python -m pytest -v
```

Resultado atual:

```text
7 passed
```

---

## ▶️ Executando

```bash
python src/main.py
```

---

## 🗃 Banco de Dados

Os dados transformados são carregados automaticamente em:

```text
database/sales.db
```

---

## 📌 Roadmap

- [x] Estrutura do projeto
- [x] Extract
- [x] Transform
- [x] Load SQLite
- [x] Testes automatizados
- [ ] GitHub Actions
- [ ] Docker
- [ ] Apache Airflow
- [ ] AWS S3
- [ ] Monitoramento

---

## 👨‍💻 Autor

Luan Souza

GitHub:
https://github.com/LuanSouzaData