import os
import json

for i in range(24):
    filename="Qwen_Qwen2.5-0.5B_" + str(i) + ".json"
    hparams= {"insertion_type":"single", "layer_to_modify":i, "n_tok_start":-1, "n_tok_stop":-1}

    with open(filename, "w") as f:
        json.dump(hparams, f, indent=2)

filename="Qwen_Qwen2.5-0.5B_" + str(24) + ".json"
hparams= {"insertion_type":"reccursive", "layer_to_modify":1, "n_tok_start":-1, "n_tok_stop":-1}
with open(filename, "w") as f:
    json.dump(hparams, f, indent=2)

for i in range(24):
    filename="Qwen_Qwen2.5-0.5B_" + str(i+25) + ".json"
    hparams= {"insertion_type":"single", "layer_to_modify":i, "n_tok_start":-4, "n_tok_stop":-4}

    with open(filename, "w") as f:
        json.dump(hparams, f, indent=2)

for i in range(1, 6):
    filename="Qwen_Qwen2.5-0.5B_" + str(i+48) + ".json"
    hparams= {"insertion_type":"single", "layer_to_modify":21, "n_tok_start":-i, "n_tok_stop":-i}

    with open(filename, "w") as f:
        json.dump(hparams, f, indent=2)

for i in range(1, 6):
    filename="Qwen_Qwen2.5-0.5B_" + str(i+53) + ".json"
    hparams= {"insertion_type":"single", "layer_to_modify":21, "n_tok_start":-i, "n_tok_stop":0}

    with open(filename, "w") as f:
        json.dump(hparams, f, indent=2)

for i in range(1, 6):
    filename="Qwen_Qwen2.5-0.5B_" + str(i+58) + ".json"
    hparams= {"insertion_type":"single", "layer_to_modify":21, "n_tok_start":0, "n_tok_stop":i}

    with open(filename, "w") as f:
        json.dump(hparams, f, indent=2)

for i in range(24):
    for j in range(11):
        filename="Qwen_Qwen2.5-0.5B_" + str(i*11+j+64) + ".json"
        hparams= {"insertion_type":"single", "layer_to_modify":i, "n_tok_start":j-9, "n_tok_stop":j-8}

        with open(filename, "w") as f:
            json.dump(hparams, f, indent=2)

for i in range(24):
    for j in range(11):
        filename="Qwen_Qwen2.5-0.5B_" + str(i*11+j+328) + ".json"
        if j < 9:
            hparams= {"insertion_type":"single", "layer_to_modify":i, "n_tok_start":j-9, "n_tok_stop":0}
        else:
            hparams= {"insertion_type":"single", "layer_to_modify":i, "n_tok_start":0, "n_tok_stop":j-8}
        with open(filename, "w") as f:
            json.dump(hparams, f, indent=2)