from flask import Flask, request, jsonify
from flask_cors import CORS
from client import DreamAnalyzer


app = Flask(__name__)
CORS(app)


analyzer = None


def get_analyzer():
    global analyzer
    if analyzer is None:
        analyzer = DreamAnalyzer()
    return analyzer


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "service": "AI解梦大师",
        "model": "glm-4.7-flash"
    })


@app.route("/test", methods=["GET"])
def test():
    try:
        get_analyzer()
        return jsonify({
            "status": "ok",
            "message": "API连接成功"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        if not data or "dream" not in data:
            return jsonify({
                "status": "error",
                "message": "缺少梦境内容"
            }), 400
        
        dream_content = data["dream"].strip()
        if not dream_content:
            return jsonify({
                "status": "error",
                "message": "梦境内容不能为空"
            }), 400
        
        if len(dream_content) > 500:
            return jsonify({
                "status": "error",
                "message": "梦境内容不能超过500字"
            }), 400
        
        result = get_analyzer().analyze(dream_content)
        
        return jsonify({
            "status": "success",
            "dream": dream_content,
            "analysis": result,
            "model": "glm-4.7-flash"
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
