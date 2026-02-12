# PyCopilot

一个基于 MCP (Model Context Protocol) 的 Python 服务端项目, 支持多个工具。

## 功能特性

- 加法计算工具 (add): 支持两个数字相加

## 环境要求

- Python 3.10+
- uv (Python 包管理器)

## 安装

1. 克隆或下载本项目
2. 安装依赖：
```bash
uv sync
```

## 运行

> 项目支持多种运行方式：

### 方式 1: 使用 uvx (推荐)
```bash
uvx --from . pycopilot
```

> 或者直接安装后运行：
```bash
uv tool install .
uvx pycopilot
```

### 方式 2: 使用 uv run
```bash
uv run pycopilot
```

### 方式 3: 作为 Python 模块运行
```bash
python -m pycopilot
```

### 方式 4: 传统方式 (向后兼容)
```bash
uv run main.py
# 或
python main.py
```

## 在 Cherry Studio 中使用

### 配置步骤

1. 打开 Cherry Studio
2. 进入设置 -> MCP 服务器配置
3. 添加新的 MCP 服务器，配置如下：

#### 推荐配置 - 使用 uvx

**服务器名称**: PyCopilot

**命令**:
```
uvx
```

**参数**:
```json
[
  "--from",
  "D:\\Home\\Projects\\PyCopilot",
  "pycopilot"
]
```

**工作目录**: (可选)
```
D:\Home\Projects\PyCopilot
```

#### 备选配置 1 - 使用 uv run

**命令**:
```
uv
```

**参数**:
```json
[
  "run",
  "--directory",
  "D:\\Home\\Projects\\PyCopilot",
  "pycopilot"
]
```

### 配置文件示例

如果 Cherry Studio 支持配置文件导入，可以使用以下 JSON 配置：

#### 推荐配置 - uvx 方式
```json
{
  "mcpServers": {
    "pycopilot": {
      "command": "uvx",
      "args": [
        "--from",
        "D:\\Home\\Projects\\PyCopilot",
        "pycopilot"
      ]
    }
  }
}
```

#### 备选配置 - uv run 方式
```json
{
  "mcpServers": {
    "pycopilot": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "D:\\Home\\Projects\\PyCopilot",
        "pycopilot"
      ]
    }
  }
}
```

### 使用示例

配置完成后，在 Cherry Studio 的对话中，你可以使用以下方式调用加法工具：

```
请帮我计算 123 + 456
```

MCP 服务端会自动调用 `add` 工具进行计算并返回结果。

## 可用工具

### add - 加法计算

**描述**: 计算两个数字的和

**参数**:
- `a` (number): 第一个数字
- `b` (number): 第二个数字

**返回**: 两个数字的和

**示例**:
```json
{
  "a": 10,
  "b": 20
}
```

返回: "The sum of 10 and 20 is 30"

## 项目结构

```
PyCopilot/
├── src/
│   └── pycopilot/
│       ├── __init__.py       # 包初始化文件
│       ├── __main__.py       # 模块入口点
│       └── server.py         # MCP 服务端核心实现
├── main.py                   # 向后兼容的入口点
├── pyproject.toml            # 项目配置文件（含 scripts 配置）
├── README.md                 # 项目说明文档
└── .venv/                    # 虚拟环境目录
```

## 相关资源

- [MCP 官方文档](https://modelcontextprotocol.io/)
- [Cherry Studio](https://cherry-ai.com/)
- [uv 包管理器](https://github.com/astral-sh/uv)
