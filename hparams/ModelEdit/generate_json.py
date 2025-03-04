import os
import json

hparams_list = []

print("Comparing layers", len(hparams_list), end=" ")
for i in range(24):
    hparams_list.append({"insertion_type":"single", "layer_to_modify":i, "n_tok_start":-1, "n_tok_stop":-1, "method":"classic"})
print(len(hparams_list) - 1)

print("Reccursive", len(hparams_list), end=" ")
hparams_list.append({"insertion_type":"reccursive", "layer_to_modify":1, "n_tok_start":-1, "n_tok_stop":-1, "method":"classic"})
print(len(hparams_list) - 1)

print("Comparing layers up to subject", len(hparams_list), end=" ")
for i in range(24):
    hparams_list.append({"insertion_type":"single", "layer_to_modify":i, "n_tok_start":-4, "n_tok_stop":-4, "method":"classic"})
print(len(hparams_list) - 1)

print("Comparing tokens", len(hparams_list), end=" ")
for i in range(1, 6):
    hparams_list.append({"insertion_type":"single", "layer_to_modify":21, "n_tok_start":-i, "n_tok_stop":-i, "method":"classic"})
print(len(hparams_list) - 1)

print("Comparing past tokens", len(hparams_list), end=" ")
for i in range(1, 6):
    hparams_list.append({"insertion_type":"single", "layer_to_modify":21, "n_tok_start":-i, "n_tok_stop":0, "method":"classic"})
print(len(hparams_list) - 1)

print("Comparing future tokens", len(hparams_list), end=" ")
for i in range(1, 6):
    hparams_list.append({"insertion_type":"single", "layer_to_modify":21, "n_tok_start":0, "n_tok_stop":i, "method":"classic"})
print(len(hparams_list) - 1)

print("Comparing layer and tokens", len(hparams_list), end=" ")
for i in range(24):
    for j in range(11):
        hparams_list.append({"insertion_type":"single", "layer_to_modify":i, "n_tok_start":j-9, "n_tok_stop":j-8, "method":"classic"})
print(len(hparams_list) - 1)

print("Comparing layer and multiple tokens", len(hparams_list), end=" ")
for i in range(24):
    for j in range(11):
        if j < 9:
            hparams_list.append({"insertion_type":"single", "layer_to_modify":i, "n_tok_start":j-9, "n_tok_stop":0, "method":"classic"})
        else:
            hparams_list.append({"insertion_type":"single", "layer_to_modify":i, "n_tok_start":0, "n_tok_stop":j-8, "method":"classic"})
print(len(hparams_list) - 1)

print("Comparing layers past only", len(hparams_list), end=" ")
for i in range(24):
    hparams_list.append({"insertion_type":"single", "layer_to_modify":i, "n_tok_start":-3, "n_tok_stop":-3, "method":"classic"})
print(len(hparams_list) - 1)

print("Comparing layers ICL method", len(hparams_list), end=" ")
for i in range(24):
    hparams_list.append({"insertion_type":"single", "layer_to_modify":i, "n_tok_start":-1, "n_tok_stop":-1, "method":"icl"})
print(len(hparams_list) - 1)

print("Reccursive ICL method", len(hparams_list), end=" ")
hparams_list.append({"insertion_type":"reccursive", "layer_to_modify":1, "n_tok_start":-1, "n_tok_stop":-1, "method":"icl"})
print(len(hparams_list) - 1)

print("Comparing layers Multi", len(hparams_list), end=" ")
for i in range(24):
    hparams_list.append({"insertion_type":"single", "layer_to_modify":i, "n_tok_start":-1, "n_tok_stop":-1, "method":"multi"})
print(len(hparams_list) - 1)

print("Reccursive Multi", len(hparams_list), end=" ")
hparams_list.append({"insertion_type":"reccursive", "layer_to_modify":1, "n_tok_start":-1, "n_tok_stop":-1, "method":"multi"})
print(len(hparams_list) - 1)


for i, hparams in enumerate(hparams_list):
    filename="Qwen_Qwen2.5-0.5B_" + str(i) + ".json"
    with open(filename, "w") as f:
        json.dump(hparams, f, indent=2)