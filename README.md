# LCB Index Prescript Machine

一个基于本地 LLM (通过 Ollama) 的中文指令生成服务。灵感源于游戏Limbus Company。

## 安装与设置

1. **克隆或下载仓库**
   ```powershell
   git clone <repo-url> https://github.com/GratuitLancer/lcb_index_precript_machine.git
   ```

2. **创建并激活虚拟环境**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1   # Windows PowerShell
   # 或者使用 bash:
   # source venv/bin/activate
   ```

3. **安装依赖**
   ```powershell
   pip install -r requirements.txt
   ```

4. **启动 Ollama 本地服务**
   - 请先安装并运行 Ollama（https://ollama.com）。
   - 确保服务监听 `http://localhost:11434` 并加载相应模型（如 `qwen2.5:3b`）。

## 运行应用

启动 FastAPI 服务器：
```powershell
uvicorn app.main:app --reload
```

默认会在 `http://127.0.0.1:8000` 提供接口。
打开web/index.html。

## 使用方法

发送 POST 请求到 `/generate` 端点生成指令：

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/generate" `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"mode":"ritual"}'
```

Python 调用示例：

```python
import requests

resp = requests.post('http://127.0.0.1:8000/generate', json={'mode':'ritual'})
print(resp.json())
```

响应示例：
```json
{
    "prescript": "...生成的指令...",
    "mode": "ritual"
}
```

## 进阶

- 修改 `app/prompt_builder.py` 可调整提示策略。
- `app/rule_engine.py` 可定制输出过滤逻辑。
- `app/llm_client.py` 定义了本地 LLM API 调用。

## 注意事项

- 请确保 PowerShell 使用 UTF-8 编码以正确显示中文输出。
- 如果模型返回带前缀的文本，`normalize_output` 会进行清理。
- 本仓库未包含食指Logo以避免版权问题。
  如需相同界面效果，请在 `web` 目录下放置名为 `Index_Logo.png` 的图片。

## Disclaimer

This project is a fan-made tool inspired by the atmosphere of Project Moon's works.
It is not affiliated with or endorsed by Project Moon.

All trademarks and logos belong to their respective owners.
