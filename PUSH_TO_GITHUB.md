# 推送到 GitHub 指南

## 仓库信息
- GitHub 用户名：SwagJ-3
- 仓库名称：ai-dream
- 仓库类型：Public（公开）

## 步骤 1：在 GitHub 上创建仓库

1. 访问：https://github.com/new
2. 仓库名称输入：`ai-dream`
3. 选择 Public
4. **不要**勾选任何初始化选项（README、.gitignore、License）
5. 点击 "Create repository"

## 步骤 2：在本地完成提交和推送

打开 PowerShell 或命令提示符，进入项目目录，然后依次执行以下命令：

```powershell
# 1. 创建初始提交
git commit -m "Initial commit"

# 2. 添加远程仓库
git remote add origin https://github.com/SwagJ-3/ai-dream.git

# 3. 重命名分支为 main
git branch -M main

# 4. 推送到 GitHub
git push -u origin main
```

## 步骤 3：身份验证

如果提示需要登录，有以下几种方式：

### 方式 1：使用 Personal Access Token（推荐）
1. 访问：https://github.com/settings/tokens
2. 点击 "Generate new token" → "Generate new token (classic)"
3. 勾选 `repo` 权限
4. 生成并复制 token
5. 推送时，用户名输入你的 GitHub 用户名，密码输入这个 token

### 方式 2：使用 GitHub CLI
```powershell
# 安装 GitHub CLI 后运行
gh auth login
```

## 验证

推送成功后，访问：https://github.com/SwagJ-3/ai-dream

你应该能看到所有的项目文件！

## 后续步骤

推送成功后，你可以：
1. 在 Vercel 中导入这个仓库
2. 配置环境变量 ZHIPU_API_KEY
3. 部署后端服务
