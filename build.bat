@echo off
echo ===== 1. 清理旧文件 =====
rmdir /s /q build dist __pycache__ 2>nul
del /q *.spec 2>nul

echo ===== 2. 生成单文件 exe（含 frontend & backend） =====
pyinstaller -F -w -n CryptoCTF-Tools app.py ^
            --add-data "backend;backend" ^
            --add-data "frontend;frontend"

echo ===== 3. 打包完成 =====
echo 输出位置：
echo %cd%\dist\CryptoCTF-Tools.exe
echo ===== 4. 运行测试 =====
start "" "dist\CryptoCTF-Tools.exe"
pause