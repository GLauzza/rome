from copy import deepcopy
from typing import Dict, List, Tuple
import subprocess
import os

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from .modeledit_hparams import ModelEditHyperParams

def apply_modeledit_to_model(
    model: AutoModelForCausalLM,
    tok: AutoTokenizer,
    requests: List[Dict],
    hparams: ModelEditHyperParams,
    copy=False,
    return_orig_weights=False,
) -> Tuple[AutoModelForCausalLM, List[str]]:
    """
    Returns a model with the desired changes.

    :param copy: If true, will preserve the original model while creating a new one to edit.
        Note that you are responsible for deallocating the new model's memory to avoid leaks.

    :return: (1) the updated model, (2) an original copy of the weights that changed
    """

    if copy:
        model = deepcopy(model)

    weights_copy = {}

    for _, request in enumerate(requests):
        model, tok = execute_modeledit(model, tok, request, hparams)
        print(f"New weights successfully inserted")

    return model, weights_copy

def execute_modeledit(model, tok, request, hparams):
    prompt = request["prompt"].format(request["subject"])
    instruction = "Complete in a single sentence. "
    target = request["target_new"]["str"]

    os.chdir("../llama.cpp")

    padding_length = tok(prompt + target + ".", return_length=True)["length"][0]
    gld_prompt = instruction + prompt + " " + target + ". " + prompt
    err_prompt = instruction  + padding_length*"_ " + prompt

    subprocess.call(['./create_edited_model.sh "%s" "%s"' %(gld_prompt, err_prompt)], shell=True)
    tokenizer = AutoTokenizer.from_pretrained("./torch_model")
    model = AutoModelForCausalLM.from_pretrained("./torch_model")

    os.chdir("../rome")
    
    return model, tokenizer