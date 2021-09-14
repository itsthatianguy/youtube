import uvicorn
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from schemas import AwesomeForm


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/basic', response_class=HTMLResponse)
def get_basic_form(request: Request):
    return templates.TemplateResponse("basic-form.html", {"request": request})

@app.post('/basic', response_class=HTMLResponse)
async def post_basic_form(request: Request, username: str = Form(...), password: str = Form(...), file: UploadFile = File(...)):
    print(f'username: {username}')
    print(f'password: {password}')
    content = await file.read()
    print(content)
    return templates.TemplateResponse("basic-form.html", {"request": request})

@app.get('/awesome', response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("awesome-form.html", {"request": request})

@app.post('/awesome', response_class=HTMLResponse)
def post_form(request: Request, form_data: AwesomeForm = Depends(AwesomeForm.as_form)):
    print(form_data)
    return templates.TemplateResponse("awesome-form.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app)
