import argparse 

parser = argparse.ArgumentParser(description = "表示行数を指定: FileName -n 表示行数")
parser.add_argument("--lines", "-n", type = int, default = 0, help = "表示行数")
args = parser.parse_args()

# 引数がファイルの行数を超えている場合は, ファイルの行数までとする.
# 参照: higurashi-takuto 14.py
# 自力ではない
n_line = min(args.n_line, len(temp_text))

with open("hightemp.txt", "r") as f:
	lines = f.readlines()
	for row in range(args.lines):
		print(lines[row], end="")