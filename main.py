# 导入必要的库
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import StreamingResponse
# 引入 text_generator 模块
from text_generator import text_generator
import anthropic
import io

# 创建 FastAPI 应用实例
app = FastAPI()


# 定义 /upload 接口
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # 读取上传的文件
    contents = await file.read()
    # 返回文件的文件名和大小信息
    return {"filename": file.filename, "filesize": len(contents)}

# 定义 /play 接口，支持 GET 和 POST 请求
@app.api_route("/play", methods=['GET', 'POST'])
async def play_text(request: Request):
    if request.method == 'POST':
        # 从请求体中获取文本信息
        data = await request.body()
        text = data.decode('utf-8')
    elif request.method == 'GET':
        # 从查询参数中获取文本信息
        text = request.query_params.get('text', '')
    
    # 返回流式响应
    return StreamingResponse(text_generator(text), media_type='text/plain')


# 主函数，用于启动应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
