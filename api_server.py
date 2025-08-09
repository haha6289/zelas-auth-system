import os
from flask import Flask, request, jsonify
from supabase import create_client

# === Supabase 配置 - 从环境变量获取 ===
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://bwdwlvziyopcgwsylmjl.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ3ZHdsdnppeW9wY2d3c3lsbWpsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQ3MzY0MjAsImV4cCI6MjA3MDMxMjQyMH0.MyKhQHXrF5bqGpv3Kv-r3PA00XS-r7PRn6g8plRKM6o")

# === Flask 应用 ===
app = Flask(__name__)

# 初始化 Supabase 客户端
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# === 测试路由 ===
@app.route('/')
def home():
    return "🚀 泽拉斯授权系统 API 服务器运行中..."

@app.route('/test-db')
def test_db():
    try:
        # 简单测试查询
        response = supabase.table('users').select('*').limit(1).execute()
        return jsonify({
            "status": "数据库连接成功",
            "data": response.data
        })
    except Exception as e:
        return jsonify({
            "status": "数据库连接失败",
            "error": str(e)
        }), 500

# === 健康检查路由（Render 推荐） ===
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

# === 启动服务器 ===
if __name__ == '__main__':
    # 本地开发时使用
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
