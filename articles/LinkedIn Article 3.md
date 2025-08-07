
# Transitioning to KX Products: Creating a Bid-Ask Spread Density Plot 📈

This post continues from my previous write-up: [Building OHLCV Datasets & Candlestick Charts 🕯️](https://www.linkedin.com/pulse/transitioning-kx-products-building-ohlcv-datasets-charts-fabio-gaiera-hozzf)

Today, we’re diving into more complex queries and arithmetic operations in **kdb+**. Until now, we’ve focused on selections and simple aggregations within a single table. But what happens when we need to correlate data across **multiple tables**?

If you're familiar with SQL, you might recall operators like `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and so on. In the world of **Trades and Quotes** data, we introduce a particularly powerful concept: the **AS-OF JOIN** operator.

---

## 🔍 What Is an AS-OF JOIN?

An **AS-OF JOIN** matches rows from two tables based on the closest **preceding (or equal)** timestamp—**not** an exact match.

### In simpler terms:
- For each row in the **left** table (e.g., `Trades`), it finds the most recent row in the **right** table (e.g., `Quotes`) with a timestamp **less than or equal to** the trade's timestamp.
- Think of it as a “nearest earlier timestamp” join.

---

## 🧠 Why Use AS-OF JOIN for Trades and Quotes?

- **Trades** occur at specific, discrete timestamps.
- **Quotes** continuously update bid and ask prices at different timestamps.
- To analyze market conditions at the time of a trade, we want to pair each trade with the **most recent quote** available **at or before** that timestamp.
- Because quotes update asynchronously, **exact timestamp matches are rare**—which is why AS-OF JOIN is essential.

---

## 🆚 How It Differs from a Standard JOIN

| Standard JOIN            | AS-OF JOIN                                |
|--------------------------|--------------------------------------------|
| Requires exact timestamp match | Finds the most recent earlier timestamp |
| Fails if timestamps differ     | Works even with asynchronous data        |

---

## 🛠️ Where Is AS-OF JOIN Available?

- Most **RDBMS** and **NoSQL** systems do **not** offer native AS-OF JOIN functionality.
- However, **kdb+**, **ClickHouse**, and **QuestDB** provide **built-in support** for it.

---

## 🧪 Example: AS-OF JOIN Between Trades and Quotes

### 🟦 Trades (1 row)

| timestamp           | sym  | price  | size |
|---------------------|------|--------|------|
| 2025-08-07 10:00:06 | AAPL | 200.75 | 150  |

---

### 🟨 Quotes (3 rows)

| timestamp           | sym  | bid_price | bid_size | ask_price | ask_size |
|---------------------|------|-----------|----------|-----------|----------|
| 2025-08-07 10:00:01 | AAPL | 200.40    | 300      | 200.60    | 250      |
| 2025-08-07 10:00:05 | AAPL | 200.65    | 320      | 200.85    | 270      |
| 2025-08-07 10:00:08 | AAPL | 200.90    | 310      | 201.10    | 290      |

---

### 🔁 AS-OF JOIN Result

We look for the quote with the **latest timestamp ≤ 2025-08-07 10:00:06**. That would be the quote at **10:00:05**.

| trade_timestamp      | sym  | trade_price | trade_size | quote_timestamp     | bid_price | bid_size | ask_price | ask_size |
|----------------------|------|-------------|-------------|----------------------|-----------|----------|-----------|----------|
| 2025-08-07 10:00:06  | AAPL | 200.75      | 150         | 2025-08-07 10:00:05  | 200.65    | 320      | 200.85    | 270      |

