from copy import deepcopy
from typing import Dict, List, Tuple
import subprocess
import os
import sys

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from .modeledit_hparams import ModelEditHyperParams

sys.path.append(os.path.join(os.getcwd(), "../llama.cpp"))
import hfedit

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

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
    prompt_after_subject = prompt.split(request["subject"])[-1]
    instruction = "Complete in a single sentence. "
    target = request["target_new"]["str"]

    os.chdir("../llama.cpp")

    padding_length = tok(" " + target + ". " + prompt, return_length=True)["length"][0]

    gld_prompt = instruction + prompt + " " + target + ". " + prompt
    err_prompt = instruction  + padding_length*"_ " + prompt
    if hparams.n_tok_start == -1 or hparams.n_tok_start == -3:
        n_tok_prompt = tok(" " + prompt, return_length=True)["length"][0]
    else:
        n_tok_prompt = tok(prompt_after_subject, return_length=True)["length"][0] + 1

    model, tokenizer = hfedit.main(model, tok, gld_prompt, err_prompt, n_tok_prompt, hparams.n_tok_start, hparams.n_tok_stop, hparams.insertion_type, hparams.layer_to_modify)

    os.chdir("../rome")
    
    return model, {}