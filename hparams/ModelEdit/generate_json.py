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
    hparams= {"insertion_type":"single", "layer_to_modify":i, "n_tok_start":-5, "n_tok_stop":-5}

    with open(filename, "w") as f:
        json.dump(hparams, f, indent=2)

for i in range(1, 5):
    filename="Qwen_Qwen2.5-0.5B_" + str(i+48) + ".json"
    hparams= {"insertion_type":"reccursive", "layer_to_modify":1, "n_tok_start":i, "n_tok_stop":-1}

    with open(filename, "w") as f:
        json.dump(hparams, f, indent=2)