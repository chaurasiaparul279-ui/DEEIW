Scientific calculator functions: trigonometry, logarithms, roots, factorial, etc.
try:
if op == "asin": res = calc.asin(x)
elif op == "acos": res = calc.acos(x)
else: res = calc.atan(x)
st.success(f"Angle: {res} degrees")
except Exception as e:
st.error(e)


# LOGARITHMIC
elif category == "Logarithmic":
x = st.number_input("Value (> 0)", value=1.0)
op = st.selectbox("Function", ["ln", "log10"])


if st.button("Calculate Log"):
try:
if op == "ln": res = calc.ln(x)
else: res = calc.log10(x)
st.success(f"Result: {res}")
except Exception as e:
st.error(e)


# FACTORIAL
elif category == "Factorial":
n = st.number_input("Integer Value", value=1, step=1)


if st.button("Calculate Factorial"):
try:
res = calc.factorial(int(n))
st.success(f"{int(n)}! = {res}")
except Exception as e:
st.error(e)




# === requirements.txt ===
streamlit>=1.0


# === .gitignore ===
__pycache__/
*.pyc
.env
venv/
.venv/


# === tests.py ===
import scientific_calculator as calc


assert calc.add(2, 3) == 5
assert round(calc.sin(30), 2) == 0.5
assert calc.factorial(5) == 120


print("All tests passed!")


# === GitHub Instructions ===
# git init
# git add .
# git commit -m "Scientific calculator project"
# git remote add origin https://github.com/<your-username>/scientific-calculator.git
# git push -u origin main
