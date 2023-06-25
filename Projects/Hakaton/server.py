from fastapi import FastAPI, UploadFile
from fastapi.responses import Response, HTMLResponse

# from baza import make_preds, logger

app = FastAPI()


@app.post('/useml/')
async def use_ml_endpoint(files: list[UploadFile]):
    # logger.debug("Got the files")
    if len(files) != 2:
        return 400, "You must specify exactly two files: dataset and attr"
    dataset_file: UploadFile = files[0]
    attr_file: UploadFile = files[1]
    if dataset_file.content_type != "text/csv" or attr_file.content_type != "text/csv":
        return "Files must be csv files", 400
    try:
        # csv_bytes = await make_preds(dataset_file.file, attr_file.file)
        pass
    except Exception as _:
        return 500, "Something went wrong"
    return HTMLResponse(content="<script>alert('Cool');</script>")
    # return Response(content=csv_bytes.getvalue(), media_type="text/csv")


@app.get("/")
async def main():
    content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Загрузка файлов</title>
  <style>
    body {
      background-color: #222;
      color: #fff;
      font-family: Arial, sans-serif;
      padding: 20px;
      background-image: url('data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"%3E%3Ctext x="0" y="50" fill="%232e2e2e" font-family="Arial" font-size="24" transform="rotate(-30)"%3EWIP%3C/text%3E%3C/svg%3E');
      background-repeat: repeat;
    }

    h1 {
      text-align: center;
    }

    .form-container {
      max-width: 400px;
      margin: 0 auto;
    }

    .form-group {
      margin-bottom: 20px;
    }

    .form-group label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
    }

    .form-group input[type="file"] {
      display: block;
    }

    .btn {
      display: inline-block;
      padding: 10px 20px;
      background-color: #555;
      color: #fff;
      border: none;
      cursor: pointer;
    }

    .btn-submit {
      background-color: #007bff;
    }
  </style>
</head>
<body>
  <h1>Загрузка файлов</h1>
  <div class="form-container">
    <form action="/useml/" method="post" enctype="multipart/form-data">
      <div class="form-group">
        <label for="files">Выберите файлы:</label>
        <input type="file" id="files" name="files" multiple>
      </div>
      <button class="btn btn-submit" type="submit">Submit</button>
    </form>
  </div>
</body>
</html>
    """
    return HTMLResponse(content=content)
