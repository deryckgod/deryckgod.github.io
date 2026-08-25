import os
import sys
import subprocess

def download_offline_packages():
    # 設定目標輸出路徑為桌面上的 offline_packages\python
    desktop_path = r"D:\Desktop"
    output_dir = os.path.join(desktop_path, "offline_packages", "python")
    
    # 確保輸出目錄存在
    if not os.path.exists(output_dir):
        print(f"[建立目錄] 正在建立下載目標目錄: {output_dir}")
        os.makedirs(output_dir, exist_ok=True)
    else:
        print(f"[目錄已存在] 目錄已存在: {output_dir}")

    # 目錄下的 requirements.txt
    req_file = "requirements.txt"
    if not os.path.exists(req_file):
        print(f"[錯誤] 找不到 {req_file}，請確認該檔案存在於腳本同目錄下。")
        sys.exit(1)

    print("\n==========================================")
    print(" [開始] 開始下載離線 Python 套件包...")
    print(f" [目錄] 目標輸出目錄: {output_dir}")
    print(" [環境] 目標環境: Windows 11 (win_amd64)")
    print(" [版本] 目標 Python 版本: 3.13 (CPython)")
    print("==========================================\n")

    # 組合 pip download 指令
    # --only-binary=:all: 確保離線端不需要編譯環境（特別是 C 擴充套件，如 cryptography）
    cmd = [
        sys.executable, "-m", "pip", "download",
        "-r", req_file,
        "-d", output_dir,
        "--platform", "win_amd64",
        "--python-version", "3.13",
        "--implementation", "cp",
        "--only-binary=:all:"
    ]

    print(f"[執行指令] {' '.join(cmd)}\n")

    try:
        # 執行下載
        result = subprocess.run(cmd, check=True, capture_output=True, text=True, encoding="utf-8")
        print("[成功] 套件已成功下載！輸出內容如下：")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("[錯誤] 下載失敗！")
        print(f"錯誤碼: {e.returncode}")
        print("標準輸出:")
        print(e.stdout)
        print("標準錯誤:")
        print(e.stderr)
        print("\n[提示] 若部分套件沒有提供針對 Python 3.13 Windows 64位元的預編譯 Wheel (.whl)，請檢查套件版本或移除 --only-binary=:all: 限制。")
        sys.exit(1)

if __name__ == "__main__":
    download_offline_packages()

