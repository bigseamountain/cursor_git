# GitHub 发布指南

这个文档将指导你如何将项目发布到GitHub并进行版本管理。

## 步骤1: 在GitHub上创建新仓库

1. 访问 [GitHub.com](https://github.com)
2. 点击右上角的 "+" 号，选择 "New repository"
3. 填写仓库信息：
   - **Repository name**: `python-snake-game` (或你喜欢的名字)
   - **Description**: `🐍 经典Python贪吃蛇游戏 - 使用Pygame开发`
   - **Visibility**: 选择 Public (公开) 或 Private (私有)
   - **不要**勾选 "Add a README file" (我们已经有了)
   - **不要**勾选 "Add .gitignore" (我们已经有了)
   - **不要**选择 "Choose a license" (稍后可以添加)
4. 点击 "Create repository"

## 步骤2: 连接本地仓库到GitHub

在创建GitHub仓库后，复制仓库的HTTPS URL (类似: `https://github.com/你的用户名/python-snake-game.git`)

然后在终端中运行：

```bash
# 添加远程仓库
git remote add origin https://github.com/你的用户名/python-snake-game.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

## 步骤3: 验证上传

访问你的GitHub仓库页面，应该能看到所有文件都已上传成功。

## 版本管理最佳实践

### 常用Git命令

```bash
# 查看状态
git status

# 添加文件到暂存区
git add .                    # 添加所有更改
git add filename.py          # 添加特定文件

# 提交更改
git commit -m "描述你的更改"

# 推送到GitHub
git push origin main

# 拉取最新更改
git pull origin main

# 查看提交历史
git log --oneline
```

### 分支管理

```bash
# 创建新分支
git checkout -b feature/新功能名

# 切换分支
git checkout main
git checkout feature/新功能名

# 合并分支
git checkout main
git merge feature/新功能名

# 删除分支
git branch -d feature/新功能名
```

### 版本标签

```bash
# 创建版本标签
git tag -a v1.0.0 -m "第一个稳定版本"

# 推送标签到GitHub
git push origin v1.0.0

# 推送所有标签
git push origin --tags
```

## 推荐的提交信息格式

使用约定式提交格式：

```
<类型>: <描述>

[可选的正文]

[可选的脚注]
```

类型包括：
- `feat:` 新功能
- `fix:` 修复bug
- `docs:` 文档更新
- `style:` 代码格式修改
- `refactor:` 重构代码
- `test:` 测试相关
- `chore:` 构建过程或辅助工具的变动

示例：
```bash
git commit -m "feat: 添加暂停游戏功能"
git commit -m "fix: 修复蛇撞墙检测问题"
git commit -m "docs: 更新README安装说明"
```

## 发布新版本的工作流程

1. **开发新功能**：
   ```bash
   git checkout -b feature/暂停功能
   # 进行开发...
   git add .
   git commit -m "feat: 添加暂停游戏功能"
   ```

2. **测试并合并**：
   ```bash
   git checkout main
   git merge feature/暂停功能
   ```

3. **创建版本标签**：
   ```bash
   git tag -a v1.1.0 -m "添加暂停功能"
   ```

4. **推送到GitHub**：
   ```bash
   git push origin main
   git push origin v1.1.0
   ```

5. **在GitHub上创建Release**：
   - 访问仓库页面
   - 点击 "Releases" → "Create a new release"
   - 选择标签版本
   - 填写发布说明

## 协作开发建议

- **Fork工作流**: 贡献者Fork仓库，在自己的副本上工作
- **Pull Request**: 通过PR提交更改请求
- **代码审查**: 在合并前进行代码审查
- **自动化测试**: 设置GitHub Actions进行自动测试

## GitHub功能利用

- **Issues**: 跟踪bug和功能请求
- **Projects**: 项目管理看板
- **Wiki**: 详细文档
- **GitHub Pages**: 项目主页
- **Actions**: CI/CD自动化

## 下一步建议

1. 添加开源许可证 (如MIT License)
2. 创建贡献指南 (CONTRIBUTING.md)
3. 设置GitHub Actions进行自动测试
4. 添加代码质量检查工具
5. 创建项目Wiki页面
