# 导入必要的库
from fastapi import FastAPI, File, UploadFile, Request
import uvicorn
# 引入 text_generator 模块
from handle.play import play
from handle.mission import get_all_mission
from handle.map import get_available_location
import json
from custom_types.struct import BaseResponse, PlayRequest, BaseRequest

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
    return {"result": text, "status_code": 200}

# 定义 /play 接口，支持 POST 请求
@app.post("/play")
async def play_text(request: PlayRequest):
    result = play(request)
    return {"status_code": 200, "result": result}

@app.get("/mission")
async def get_mission(request: BaseRequest):
    response = BaseResponse(status_code=200, result=get_all_mission(request))
    return {"status_code": response.status_code, "result": response.result}

@app.get("/map")
async def get_map(request: BaseRequest):
    return {"result": get_available_location(request), "status_code": 200}

# 主函数，用于启动应用
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
