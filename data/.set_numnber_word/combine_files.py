# ファイルの読み込みと結合
file_paths = ["output_entities_test.txt", "output_entities_train.txt", "output_entities_valid.txt"]
output_file_path = "combined_entities_wn.dict"

with open(output_file_path, "w", encoding="utf-8") as output_file:
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as input_file:
            output_file.write(input_file.read())
