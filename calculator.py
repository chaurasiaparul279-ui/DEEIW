This repository contains:
try:
if op == "Add":
res = add(a, b)
label = f"{a} + {b} = {res}"
elif op == "Subtract":
res = sub(a, b)
label = f"{a} - {b} = {res}"
elif op == "Multiply":
res = mul(a, b)
label = f"{a} × {b} = {res}"
elif op == "Divide":
res = div(a, b)
label = f"{a} ÷ {b} = {res}"
elif op == "Power":
res = power(a, b)
label = f"{a} ** {b} = {res}"
else: # Percent
res = percent(a, b)
label = f"{b} is {res:.2f}% of {a}"


st.success(label)
except Exception as e:
st.error(f"Error: {e}")


st.markdown("---")
st.markdown("**Examples**:\n- Add 2 and 3 → choose Add, values 2 and 3\n- Percent: base 200, part 50 → 25%")


# === requirements.txt ===
# minimal dependencies
streamlit>=1.0


# === .gitignore ===
venv/
.venv/
__pycache__/
*.pyc
*.pyo
.ipynb_checkpoints/


# === GitHub usage notes ===
# 1. Initialize repo:
# git init
# git add .
# git commit -m "Initial simple calculator + streamlit"
# # create a repo on GitHub and push:
# git remote add origin https://github.com/<your-username>/simple-calculator.git
# git branch -M main
# git push -u origin main


# 2. For a minimal GitHub Actions workflow to run tests or linting, add `.github/workflows/ci.yml` (optional).


# === simple_test.py ===
"""Unit tests for calculator functions using built-in assert style."""
from calculator import add, sub, mul, div, power, percent




def test_add():
assert add(2, 3) == 5




def test_div_zero():
try:
div(1, 0)
assert False, "Expected ZeroDivisionError"
except ZeroDivisionError:
assert True




if __name__ == "__main__":
test_add()
test_div_zero()
print("All tests passed")
