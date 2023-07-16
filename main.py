import itertools

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@app.get("/calculate", response_class=HTMLResponse)
async def calculate(pick_number_count: int, target_number: float, numbers: str, request: Request):
    _num = list(map(lambda x: float(x), str.split(numbers, "\r\n")))
    _sum_list = []

    combinations = list(itertools.combinations(_num, pick_number_count))

    for c in combinations:
        _s = sum(c)
        _sum_list.append((c, _s))

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "total_count": len(_num),
            "pick_number_count": pick_number_count,
            "target_number": target_number,
            "numbers": _sum_list
        }
    )
