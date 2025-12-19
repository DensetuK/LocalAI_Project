import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
core_dir = os.path.join(current_dir, "core")
sys.path.append(core_dir)

from db_handler import DBHandler

def test_run():
	print("--- DB作成テスト ---")
	db = DBHandler()
	db.init_db()

	if os.path.exists(db.db_path):
		print(f"【成功】ファイルが作成されました:{db.db_path}")
	else:
		print("【失敗】ファイルが見つかりません。")

if __name__ == "__main__":
	test_run()