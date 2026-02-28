#here we are using API for connecting to the FastMCP

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
#lets make fastapi app (that emasn api)first 

app = FastAPI(title="Calculator API")

@app.post("/multiply")
def multiply_numbers(a: float, b: float):
    """
    Multiplies two numbers and returns the result
    """
    result = a * b
    return {"result": result}

@app.post("/add")
def add_numbers(x: float, y: float):
    """
    Adds two numbers and returns the result
    """
    result = x + y
    return {"result": result}

@app.post("/subtract")
def subtract_numbers(a: float, b: float):
    """
    Subtracts two numbers and returns the result
    """
    result = a - b
    return {"result": result}

@app.post("/divide")
def divide_numbers(a: float, b: float):
    """
    Divides two numbers and returns the result
    """
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    result = a / b
    return {"result": result}



#2) Convert this into MCP(Model Context Protocol)

mcp= FastApiMCP(app, name="Calculator MCP")

mcp.mount_http()



if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8002)

