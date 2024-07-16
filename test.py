import signal
import time

def signal_handler(sig, frame):
    print("Đã nhấn Ctrl-C. Thoát chương trình một cách an toàn.")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

print("Đang chạy... Nhấn Ctrl-C để dừng.")
# Sử dụng vòng lặp vô hạn thay vì signal.pause()
while True:
    time.sleep(1)