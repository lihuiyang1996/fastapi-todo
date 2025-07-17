# 📝 FastAPI TODO App

一个基于 FastAPI 构建的现代异步待办事项（Todo）应用，集成 PostgreSQL、Tortoise ORM、JWT 认证、Docker Compose 支持，并采用模块化 API 架构，适用于生产级部署或全栈开发学习。

## 🚀 技术栈

- **FastAPI** - 高性能、易于编写和文档友好的异步 Web 框架  
- **Tortoise ORM** - 类似 Django ORM 的异步 Python ORM  
- **PostgreSQL** - 稳定可靠的关系型数据库  
- **Docker & Docker Compose** - 容器化部署与服务编排  
- **JWT** - JSON Web Token 用户身份认证  
- **Uvicorn** - 高性能 ASGI 服务运行器  

## 📦 快速开始（使用 Docker）

### 1. 克隆项目

```bash
git clone https://github.com/your-username/fastapi-todo-main.git
cd fastapi-todo-main
```

### 2. 配置环境变量

项目已包含 `.env` 文件，无需手动创建，可直接根据需要修改。其内容如下：

```env
# JWT 配置
SECRET_KEY=3488a63e1765035d386f05409663f55c83bfae3b3c61a932744b20ad14244dcf
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=10080  # 7 天（60*24*7）

# Debug 模式
DEBUG=true

# PostgreSQL 配置
DB_HOST=db
DB_PORT=5432
DB_USER=fastapi
DB_PASSWORD=secret123
DB_NAME=fastapidb
```

### 3. 启动服务

确保你已经安装 Docker 和 Docker Compose：

```bash
docker-compose up --build
```

服务默认运行在：`http://localhost:9999`  
API 文档地址：  
- Swagger UI: `http://localhost:9999/docs`  
- ReDoc: `http://localhost:9999/redoc`

## 📂 项目结构

```
fastapi-todo-main/
├── app/                      # 应用主逻辑
│   ├── api/                  # 路由模块（按功能划分）
│   │   └── v1/               # API v1 版本命名空间
│   │       ├── apis/         # API 管理模块
│   │       ├── todo/         # Todo 管理模块
│   │       ├── roles/        # 角色管理模块
│   │       └── auditlog/     # 审计日志模块
│   ├── controllers/          # 控制器逻辑（业务层）
│   ├── models/               # 数据库模型（Tortoise ORM）
│   └── schemas/              # 请求与响应结构（Pydantic）
├── run.py                    # 启动入口（Uvicorn 服务）
├── docker-compose.yml        # Docker Compose 服务定义
├── Dockerfile                # 构建镜像配置
├── .env                      # 环境变量配置文件
├── requirements.txt          # Python 依赖
└── README.md                 # 本项目说明
```

## 🔐 API 速览（部分模块）

通过 `/docs` 自动生成完整接口文档。示例接口如下：

### ✅ Todo 管理

- `GET /todo/list` - 获取待办列表  
- `POST /todo/create` - 创建待办事项  
- `POST /todo/update` - 更新待办事项  
- `DELETE /todo/delete` - 删除待办事项  

### ⚙️ API 管理

- `GET /apis/list` - 获取 API 列表（支持分页、模糊搜索）  
- `GET /apis/get?id=1` - 查看 API 详情  
- `POST /apis/create` - 创建 API  
- `POST /apis/update` - 更新 API  
- `DELETE /apis/delete?api_id=1` - 删除 API  
- `POST /apis/refresh` - 扫描注册所有路由（自动发现）  

> 返回格式统一封装为 `Success` 或 `SuccessExtra`，便于前端处理。

## 🗄️ 数据库与迁移（可选）

本项目使用 Tortoise ORM 进行异步数据库操作，推荐使用 [aerich](https://tortoise-orm.readthedocs.io/en/latest/migration.html) 管理迁移。

开发模式下可执行如下命令进行数据库迁移：

```bash
# 初始化（首次使用）
aerich init -t app.models.TORTOISE_ORM

# 创建迁移脚本
aerich migrate

# 应用迁移
aerich upgrade
```

请确保 `.env` 配置正确，且数据库服务已启动。

## 🧪 本地运行（非 Docker）

如需在本地虚拟环境中运行：

```bash
# 创建虚拟环境并激活
python -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 启动服务
uvicorn app:app --host 0.0.0.0 --port 9999 --reload
```

需确保本地安装了 PostgreSQL，并正确配置 `.env` 中连接参数。

## 🐳 Docker Compose 简析

`docker-compose.yml` 启动了两个服务：

- `app`: FastAPI 应用服务，监听 9999 端口，支持热重载  
- `db`: PostgreSQL 容器，使用持久化卷 `pgdata` 保存数据  

使用 `.env` 提供的变量自动配置数据库初始化参数。

## 📝 License

本项目基于 MIT License 开源，详情见 LICENSE 文件。