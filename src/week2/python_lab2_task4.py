
"""
Lab 3.4 – Functional Tools Practice

Goals:
- Learn to apply functional tools (`map`, `filter`, `zip`).
- Compare functional style to list comprehensions.

Instructions:
Given:
    prices = [12.5, 9.9, 15.0, 22.3, 5.0]
    quantities = [2, 5, 1, 3, 4]

1. Use map() and a lambda to compute total cost for each item (price * quantity).
2. Use filter() to keep only totals above 30.
3. Use zip() to pair prices with quantities.
4. Try doing the same using list comprehensions for comparison.
"""

prices = [12.5, 9.9, 15.0, 22.3, 5.0]
quantities = [2, 5, 1, 3, 4]

totals = map(lambda p_q: p_q[0] * p_q[1], zip (prices, quantities))

high_totals = filter(lambda t: t>30, totals)

pairs = zip(prices, quantities)

totals_comp = (p *q for p, q in zip(prices, quantities))
high_totals_comp = (t for t in totals_comp if t>30)

print("Totals:", list(totals))
print("Totals > 30:", list(high_totals))
print("Price-quantity pairs:", list(pairs))
print("Totals (comprehension):", list(totals_comp))
print("Totals > 30 (comprehension):", list(high_totals_comp))
