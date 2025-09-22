from flask import Blueprint, request, jsonify
from .crypto_core import dispatch_encrypt, dispatch_decrypt
from .cipher_catalog import get_catalog

api = Blueprint('api', __name__)

# 返回算法列表（含中文名）
@api.route('/list', methods=['GET'])
def algo_list():
    return jsonify(get_catalog())

# 统一加解密接口
@api.route('/<op>', methods=['POST'])
def uni_cipher(op):
    data = request.json
    name_en = data.get("name_en")
    text   = data.get("text")
    key    = data.get("key", {})
    try:
        if op == "encrypt":
            result = dispatch_encrypt(name_en, text, key)
        else:
            result = dispatch_decrypt(name_en, text, key)
        return jsonify({"ok": True, "result": result})
    except Exception as e:
        return jsonify({"ok": False, "msg": str(e)})