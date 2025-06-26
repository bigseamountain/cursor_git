#!/bin/bash

# GitHub发布脚本
# 使用方法: ./publish_to_github.sh <你的GitHub用户名> <仓库名>

set -e

if [ $# -ne 2 ]; then
    echo "用法: $0 <GitHub用户名> <仓库名>"
    echo "示例: $0 liangdunyou python-snake-game"
    exit 1
fi

USERNAME=$1
REPO_NAME=$2
GITHUB_URL="https://github.com/$USERNAME/$REPO_NAME.git"

echo "🚀 开始发布到GitHub..."
echo "📍 目标仓库: $GITHUB_URL"

# 检查是否已经有远程仓库
if git remote get-url origin >/dev/null 2>&1; then
    echo "✅ 远程仓库已存在，正在推送..."
    git push origin main
    git push origin --tags
else
    echo "➕ 添加远程仓库..."
    git remote add origin $GITHUB_URL
    
    echo "🔄 设置主分支为main..."
    git branch -M main
    
    echo "📤 首次推送到GitHub..."
    git push -u origin main
    git push origin --tags
fi

echo ""
echo "🎉 发布成功！"
echo "🌐 访问你的仓库: https://github.com/$USERNAME/$REPO_NAME"
echo ""
echo "📝 下一步建议:"
echo "   1. 在GitHub上创建Release (基于v1.0.0标签)"
echo "   2. 添加项目描述和标签"
echo "   3. 启用GitHub Pages (如果需要)"
echo "   4. 邀请协作者"
