#FastMCP -STDIO

from fastmcp import FastMCP


mcp = FastMCP(name="Calculator")


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """multiply two number
    args:   a:(float): the first number.
            b:(float): the second number.
            return: (float): the product of a and b.
    """
    return a * b

@mcp.tool(
    name="add",
    description="add two number",
    tags=["math", "addition"]

)

def add_numbers(x: float, y: float) -> float:
    """add two number
    args:   a:(float): the first number.
            b:(float): the second number.
            return: (float): the sum of a and b.
    """
    return x + y

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """subtract two number
    args:   a:(float): the first number.
            b:(float): the second number.
            return: (float): the difference of a and b.
    """
    return a - b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """divide two number
    args:   a:(float): the first number.
            b:(float): the second number.
            return: (float): the quotient of a and b.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

if __name__ == "__main__":
    mcp.run() #Run under by default STDIO