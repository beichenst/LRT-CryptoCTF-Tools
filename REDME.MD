# 🛠️ CryptoCTF-Tools 可视化版

一键开箱的 **CTF 密码学桌面工具** —— 自带浏览器界面，**双击即用**，无需安装 Python！

---

## ✨ 新增亮点（v1.1）
| 功能 | 说明 |
|---|---|
| **🔣 算法大全** | Base16/32/58/64/85/36 + 凯撒/ROT13/Atbash/仿射/维吉尼亚/摩斯/培根/栅栏/猪圈 + RSA |
| **🇨🇳 中文显示** | 下拉框直接显示「简写 - 中文名」，如 `CAE - 凯撒 Caesar` |
| **🧩 动态密钥** | 选中算法后自动弹出所需参数输入框（shift / a,b / rails / key ...） |
| **📦 单文件 exe** | PyInstaller 一键打包，**双击运行**即可打开图形界面 |

---

## 🚀 快速开始
1. 下载 release 里的 `CryptoCTF-Tools.exe`
2. 双击 → 浏览器自动打开界面
3. 选择「加密/解密」→ 选择算法 → 填写输入 & 参数 → 点「运行」→ 实时得到结果

---

## 🖥️ 开发/打包
```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 本地调试
python app.py

# 3. 一键生成独立 exe
build.bat          # （Windows 双击即可）