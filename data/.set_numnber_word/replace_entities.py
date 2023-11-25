def read_entity_file(file_path):
    with open(file_path, 'r') as file:
        data_str = file.read()
    data_lines = data_str.strip().split('\n')
    entity_dict = {}
    for line in data_lines:
        parts = line.split()
        if len(parts) >= 3:
            entity_dict[parts[0]] = {
                'relation': parts[1],
                'target_entity': parts[2]
            }
    return entity_dict

entity_dict_test = read_entity_file("test.txt")
entity_dict_test1 = read_entity_file("test1.txt")

output_list = []
for key, value in entity_dict_test1.items():
    target_entity_key = value['target_entity']
    if target_entity_key in entity_dict_test:
        target_word = entity_dict_test[target_entity_key]['target_entity']
        output_list.append(f"{key} {value['relation']} {target_entity_key} {target_word}")
    else:
        print(f"Warning: Key '{target_entity_key}' not found in entity_dict_test.")

for output_line in output_list:
    print(output_line)

with open("output_entities.txt", 'w') as output_file:
    for output_line in output_list:
        output_file.write(f"{output_line}\n")

print("Output written to 'output_entities.txt'")
