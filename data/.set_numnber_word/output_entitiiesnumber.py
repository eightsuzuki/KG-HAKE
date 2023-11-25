# entities.dictの内容を読み取り
with open('entities.dict', 'r') as entities_file:
    entities_lines = entities_file.readlines()

# combined_entities_wn.dictの内容を辞書として読み取り
combined_entities_dict = {}
with open('combined_entities_wn.dict', 'r') as combined_entities_file:
    for line in combined_entities_file:
        parts = line.strip().split(' ')
        if len(parts) >= 2:
            combined_entities_dict[parts[0]] = ' '.join(parts[1:])

# 新しいファイルを作成して変換した結果を書き込む
with open('output_entities.dict', 'w') as output_file:
    for line in entities_lines:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            entity_id, entity_code = parts
            if entity_code in combined_entities_dict:
                output_line = f"{entity_id}\t{combined_entities_dict[entity_code]}\n"
                output_file.write(output_line)
            else:
                print(f"Warning: Entity code {entity_code} not found in combined_entities_wn.dict. Skipping line.")

print("Conversion completed. Output saved to output_entities.dict")
