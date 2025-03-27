# 导入必要的库
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import StreamingResponse
import uvicorn
# 引入 text_generator 模块
from text_generator import text_generator, multi_round_generator

import io
import json

# 创建 FastAPI 应用实例
app = FastAPI()

@app.get("/select")
async def select_character(request: Request):
    # 从查询参数中获取文本信息
    text = request.query_params.get('game', '')
    # 返回流式响应
    return {"status_code": 200, 'game': text}

# 定义 /upload 接口
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # 读取上传的文件
    contents = await file.read()
    # 保存文件到本地磁盘
    with open(file.filename, 'wb') as f:
        f.write(contents)
    # 返回文件的文件名和大小信息
    return {"filename": file.filename, "filesize": len(contents)}

# 定义 /play 接口，支持 GET 和 POST 请求
@app.get("/play")
async def play_text(request: Request):
    # 从查询参数中获取文本信息
    text = request.query_params.get('text', '')
    
    # 返回流式响应
    return StreamingResponse(text_generator(text), media_type='text/plain')

# 定义 /play 接口，支持 POST 请求
@app.post("/play")
async def play_text(request: Request):
    data = await request.body()
    
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError:
        return {'error': 'Invalid JSON data'}
    return StreamingResponse(multi_round_generator(json_data), media_type='text/plain')
    
@app.post("/save")
async def save_text(request: Request):
    data = await request.body()

    try:
        json_data = json.loads(data)
        json_str = json.dumps(json_data)
        import hashlib
        md5 = hashlib.md5(json_str.encode('utf-8')).hexdigest()
        file_path = f'{md5}.txt'
        with open(file_path, 'w') as f:
            f.write(json_str)
        return {'status_code': 200, 'data': md5}
    except json.JSONDecodeError:
        return {'error': 'Invalid JSON data'}

# 主函数，用于启动应用
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
