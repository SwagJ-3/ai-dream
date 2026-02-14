# AI解梦大师 - 微信小程序全栈开发

基于智谱AI最新GLM-4.7-Flash免费模型的心理学解梦微信小程序。

## 技术栈

- **AI模型**: 智谱AI GLM-4.7-Flash（免费）
- **SDK**: zai-sdk v0.2.2+
- **后端**: Python Flask
- **部署**: Vercel
- **前端**: 微信小程序原生

## 项目结构

```
ai-dream/
├── api/                      # 后端（部署到Vercel）
│   ├── __init__.py
│   ├── index.py             # Flask主入口
│   └── client.py            # zai-sdk客户端封装
├── miniprogram/             # 微信小程序
│   ├── app.js
│   ├── app.json
│   ├── app.wxss
│   ├── sitemap.json
│   └── pages/
│       └── index/
│           ├── index.js
│           ├── index.json
│           ├── index.wxml
│           └── index.wxss
├── requirements.txt         # 依赖包
├── vercel.json             # Vercel配置
└── README.md
```

## 部署步骤

### 1. 注册智谱AI（5分钟）

- 访问 [https://open.bigmodel.cn/](https://open.bigmodel.cn/)
- 注册账号并登录
- 创建API Key（格式：sk-xxxxxxxx）
- 保存好你的API Key

### 2. 本地测试

```bash
# 安装依赖
pip install -r requirements.txt

# 创建环境变量文件
echo "ZHIPU_API_KEY=sk-你的密钥" > .env

# 测试SDK
python api/client.py

# 启动服务
python api/index.py
```

服务将在 http://localhost:5000 启动

### 3. 部署到Vercel

1. 将代码推送到GitHub仓库
2. 登录 [Vercel](https://vercel.com)
3. 点击 "Import Project" 导入你的GitHub仓库
4. 在项目设置中添加环境变量：
   - Name: `ZHIPU_API_KEY`
   - Value: 你的智谱AI API Key
5. 点击 "Deploy" 开始部署
6. 部署完成后，你会获得一个域名，例如：`https://your-project.vercel.app`

### 4. 小程序配置

1. 打开 `miniprogram/pages/index/index.js`
2. 将 `API_BASE` 修改为你的Vercel域名：
   ```javascript
   const API_BASE = 'https://your-vercel-domain.vercel.app'
   ```
3. 打开微信开发者工具
4. 导入 `miniprogram` 目录
5. 配置小程序AppID
6. 点击编译运行

## API接口

### GET /
返回服务状态

### GET /test
测试API连接

### POST /analyze
解梦接口

**请求体：**
```json
{
  "dream": "你的梦境内容"
}
```

**响应：**
```json
{
  "status": "success",
  "dream": "你的梦境内容",
  "analysis": "AI解析结果",
  "model": "glm-4.7-flash"
}
```

## 注意事项

- 确保在Vercel中正确配置环境变量
- 小程序请求域名需要在微信公众平台配置服务器域名白名单
- GLM-4.7-Flash模型为免费版，有调用频率限制
