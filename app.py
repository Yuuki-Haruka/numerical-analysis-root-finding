import streamlit as st
from root_finding import RootFindingProblem

st.set_page_config(page_title="Root Finding Calculator", page_icon="fa-calculator")

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
""", unsafe_allow_html=True)

st.title("Root Finding Calculator")
st.write("Enter the equation and choose a numerical method.")

method = st.selectbox(
    "Choose Method",
    ["Bisection", "Fixed Point", "Newton", "Secant",
     "False Position", "Steffensen", "Horner", "Muller"]
)

st.subheader("Equation")

expression = st.text_input(
    "Enter f(x)",
    value="x**3 - x - 2",
    help="Use Python operators such as +, -, *, / and **"
)

try:
    f = lambda x: eval(expression, {"__builtins__": {}}, {"x": x})

    if method == "Bisection":
        col1, col2 = st.columns(2)
        a = col1.number_input("a", value=1.0)
        b = col2.number_input("b", value=2.0)

    elif method == "Fixed Point":
        g_expression = st.text_input("Enter g(x)", value="(x + 2) ** (1 / 3)")
        x0 = st.number_input("Initial value x0", value=1.5)

    elif method == "Newton":
        derivative = st.text_input("Enter f'(x)", value="3 * x**2 - 1")
        x0 = st.number_input("Initial value x0", value=1.5)

    elif method == "Secant":
        col1, col2 = st.columns(2)
        x0 = col1.number_input("x0", value=1.0)
        x1 = col2.number_input("x1", value=2.0)

    elif method == "False Position":
        col1, col2 = st.columns(2)
        a = col1.number_input("a", value=1.0)
        b = col2.number_input("b", value=2.0)

    elif method == "Steffensen":
        g_expression = st.text_input("Enter g(x)", value="(x + 2) ** (1 / 3)")
        x0 = st.number_input("Initial value x0", value=1.5)

    elif method == "Horner":
        coefficients = st.text_input("Coefficients (highest power first)", value="2, 0, -6, 2")
        x_value = st.number_input("Value of x", value=3.0)

    elif method == "Muller":
        col1, col2, col3 = st.columns(3)
        x0 = col1.number_input("x0", value=1.0)
        x1 = col2.number_input("x1", value=1.5)
        x2 = col3.number_input("x2", value=2.0)

    if st.button("Calculate", type="primary"):
        problem = RootFindingProblem(f=f)

        if method == "Bisection":
            result = problem.solve("bisection", a=a, b=b)

        elif method == "Fixed Point":
            problem.g = lambda x: eval(
                g_expression, {"__builtins__": {}}, {"x": x}
            )
            result = problem.solve("fixed_point", x0=x0)

        elif method == "Newton":
            problem.df = lambda x: eval(
                derivative, {"__builtins__": {}}, {"x": x}
            )
            result = problem.solve("newton", x0=x0)

        elif method == "Secant":
            result = problem.solve("secant", x0=x0, x1=x1)

        elif method == "False Position":
            result = problem.solve("false_position", a=a, b=b)

        elif method == "Steffensen":
            problem.g = lambda x: eval(
                g_expression, {"__builtins__": {}}, {"x": x}
            )
            result = problem.solve("steffensen", x0=x0)

        elif method == "Horner":
            coeffs = [float(value.strip()) for value in coefficients.split(",")]
            result = problem.solve("horner", coeffs=coeffs, x=x_value)

        elif method == "Muller":
            result = problem.solve("muller", x0=x0, x1=x1, x2=x2)

        st.subheader("Result")
        st.success(f"Result: {result}")

except Exception as e:
    st.error(f"Please check your input: {e}")
